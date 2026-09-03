// Driver around the shipped PLINK 2.0 exact-test code (include/plink2_stats.cc,
// compiled verbatim).  Reads one query per line on stdin:
//   H hets hom1 hom2 midp              -> HweLnP (natural log of p)
//   T hets hom1 hom2 midp thresh       -> HweThreshLn (1 = fails threshold, i.e. p < thresh)
//   F m11 m12 m21 m22 midp             -> Fisher22TwoSidedP, p and ln p
//   X fhets fhom1 fhom2 m1 m2 midp     -> HweXchrLnP (ln p)
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include "include/plink2_stats.h"
using namespace plink2;
int main() {
  char kind;
  long long a, b, c, d, e;
  int midp;
  double thresh;
  char line[512];
  while (fgets(line, sizeof line, stdin)) {
    if (sscanf(line, " %c", &kind) != 1) continue;
    if (kind == 'H') {
      if (sscanf(line, " H %lld %lld %lld %d", &a, &b, &c, &midp) != 4) continue;
      printf("H %lld %lld %lld %d %.17g\n", a, b, c, midp, HweLnP((int32_t)a, (int32_t)b, (int32_t)c, midp));
    } else if (kind == 'T') {
      if (sscanf(line, " T %lld %lld %lld %d %lf", &a, &b, &c, &midp, &thresh) != 5) continue;
      // caller convention (plink2_filter.cc EnforceHweThresh): ln_thresh scaled by 1+kSmallEpsilon
      double ln_thresh = log(thresh) * (1 + 5.684341886080802e-14);
      printf("T %lld %lld %lld %d %.17g %u\n", a, b, c, midp, thresh, HweThreshLn((int32_t)a, (int32_t)b, (int32_t)c, midp, exp(ln_thresh), ln_thresh));
    } else if (kind == 'F') {
      if (sscanf(line, " F %lld %lld %lld %lld %d", &a, &b, &c, &d, &midp) != 5) continue;
      printf("F %lld %lld %lld %lld %d %.17g %.17g\n", a, b, c, d, midp, Fisher22TwoSidedP(a, b, c, d, midp, 0), Fisher22TwoSidedP(a, b, c, d, midp, 1));
    } else if (kind == 'X') {
      if (sscanf(line, " X %lld %lld %lld %lld %lld %d", &a, &b, &c, &d, &e, &midp) != 6) continue;
      printf("X %lld %lld %lld %lld %lld %d %.17g\n", a, b, c, d, e, midp, HweXchrLnP((int32_t)a, (int32_t)b, (int32_t)c, (int32_t)d, (int32_t)e, midp));
    }
    fflush(stdout);
  }
  return 0;
}
