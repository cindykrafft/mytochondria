**Title:** image::resampleImage: NEAREST ignores ImageSampler::sourceRegion

**Describe the bug**
With `ImageSampler::sourceRegion` set to part of the image, `resampleImage()` with the `NEAREST` filter returns the wrong pixels. Resampling the right half of an 8-pixel ramp (`0 1 2 ... 7`) to 4 pixels gives `0 0 0 7` instead of `4 5 6 7`. The left half gives `0 0 0 0` instead of `0 1 2 3`. The same resample over the full image works (`1 3 5 7`), and `BOX` on the right half gives `4 5 6 7`.

As far as I can tell from reading `generateMadProgram()`, the range of source pixels searched for each target pixel is computed from the target coordinate without mapping it through `left`/`right`. The weights, however, use the region-relative coordinate. Filters with a wide enough bound still find the right pixels. `NEAREST` has `boundingRadius = 0`, so it only looks at one or two source pixels, and those can be outside the region.

**To Reproduce**
`sampler_repro.cpp`:
```cpp
#include <image/ImageSampler.h>
#include <image/LinearImage.h>
#include <cstdio>
#include <initializer_list>

using namespace image;

static void run(LinearImage const& src, Filter filter, const char* name,
        Region region, const char* regionName) {
    ImageSampler sampler;
    sampler.horizontalFilter = filter;
    sampler.verticalFilter = Filter::BOX;
    sampler.sourceRegion = region;
    LinearImage dst = resampleImage(src, 4, 1, sampler);
    printf("%-8s %-10s -> 4 px: ", name, regionName);
    for (int i = 0; i < 4; i++) printf("%g ", dst.getPixelRef()[i]);
    printf("\n");
}

int main() {
    // 8x1 single-channel ramp: pixel i has value i
    LinearImage src(8, 1, 1);
    for (int i = 0; i < 8; i++) src.getPixelRef()[i] = float(i);

    run(src, Filter::NEAREST,  "NEAREST",  { 0.0f, 0.0f, 1.0f, 1.0f }, "full");
    run(src, Filter::NEAREST,  "NEAREST",  { 0.0f, 0.0f, 0.5f, 1.0f }, "left half");
    run(src, Filter::NEAREST,  "NEAREST",  { 0.5f, 0.0f, 1.0f, 1.0f }, "right half");
    run(src, Filter::BOX,      "BOX",      { 0.5f, 0.0f, 1.0f, 1.0f }, "right half");
    run(src, Filter::MITCHELL, "MITCHELL", { 0.5f, 0.0f, 1.0f, 1.0f }, "right half");

    // centres of pixels 0, 4 and 7 in texture space
    SingleSample s;
    for (int i : { 0, 4, 7 }) {
        float const x = (i + 0.5f) / 8.0f;
        computeSingleSample(src, x, 0.5f, &s, Filter::BOX);
        printf("computeSingleSample(x=%g, BOX) = %g\n", x, s[0]);
    }
}
```
Built against a desktop debug build (`./build.sh -p desktop debug`, clang 18, libc++) at a5e4a836:
```sh
F=/path/to/filament
B=$F/out/cmake-debug
clang++ -std=c++17 -stdlib=libc++ -g \
  -I$F/libs/image/include -I$F/libs/utils/include -I$F/libs/math/include \
  sampler_repro.cpp -o sampler_repro \
  $B/libs/image/libimage.a $B/libs/utils/libutils.a $B/libs/math/libmath.a -lpthread -ldl
./sampler_repro
```

**Expected behavior**
`NEAREST` over the left half gives `0 1 2 3`, and over the right half gives `4 5 6 7`, like `BOX` does.

**Screenshots**
N/A

**Logs**
```
NEAREST  full       -> 4 px: 1 3 5 7 
NEAREST  left half  -> 4 px: 0 0 0 0 
NEAREST  right half -> 4 px: 0 0 0 7 
BOX      right half -> 4 px: 4 5 6 7 
MITCHELL right half -> 4 px: 4.05882 5 6 6.94118 
computeSingleSample(x=0.0625, BOX) = 0
computeSingleSample(x=0.5625, BOX) = 3.5
computeSingleSample(x=0.9375, BOX) = 6.5
```

**Desktop (please complete the following information):**
 - OS: Ubuntu 24.04 (Linux x86_64)
 - GPU: none (CPU-only; the repro doesn't render)
 - Backend: N/A

**Smartphone (please complete the following information):**
 - Device: N/A
 - OS: N/A

**Additional context**
[ImageSampler.cpp#L116-L117](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/image/src/ImageSampler.cpp#L116-L117) describes `left`/`right` as:
```cpp
// The given left / right floats define a source range within [0,1] such that 0 is at the left edge
// of the the left-most pixel and 1 is at the right edge of the right-most pixel.
```
In the loop ([L135-L156](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/image/src/ImageSampler.cpp#L135-L156)), `xtarget` runs over `[0,1]` of the target row. The search window turns it into source indices as if it were an image coordinate, while `xsource` is converted into the region's coordinates before the weight is computed:
```cpp
    const float filterBounds = domainScale * std::abs(filter.boundingRadius);
    ...
        const auto isource_lower = int32_t((xtarget - filterBounds) * nsource);
        const auto isource_upper = int32_t(std::ceil((xtarget + filterBounds) * nsource));
        for (int32_t isource = isource_lower; isource <= isource_upper; ++isource) {
            const float xsource = (((isource + 0.5f) / nsource) - left) / (right - left);
            ...
            const float t = domainScale * std::abs(xsource - xtarget);
```
Here is target pixel 0 of the right-half case worked through: `xtarget = 0.125`, `filterBounds = 0` for `NEAREST`, so the window is source pixel 1 only. Its `xsource` is `(1.5/8 - 0.5) / 0.5 = -0.625`, which is outside the region and gets rejected. So target pixel 0 gets no samples and stays 0.

One possible fix is to map the window into image space, e.g. centre it on `left + xtarget * (right - left)` and scale the half-width by `(right - left)`.

Two related things I noticed but am less sure about:
- Since `t = domainScale * |xsource - xtarget|` and the filter is zero for `t` beyond `boundingRadius`, I'd have expected the half-width to be `boundingRadius / domainScale` rather than `domainScale * boundingRadius`. Is that intended?
- `computeSingleSample()` at the centre of pixel 4 (`x = 4.5/8`) returns 3.5 with `BOX`, and at the centre of pixel 7 returns 6.5. The header says "(0.0f, 0.0f) is the upper-left boundary of the top-left pixel" ([ImageSampler.h#L130-L131](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/image/include/image/ImageSampler.h#L130-L131)), so I expected 4 and 7. It calls `resampleImage1D` with a sub-range too, so it may have the same cause, but I haven't confirmed that.

I'd be happy to send a PR if this is something you'd like fixed.
