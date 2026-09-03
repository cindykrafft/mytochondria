// Driver around the shipped PLINK 1.9 exact-test code (plink_stats.c, linked as the
// compiled object from the 1.9 build).  Same query format as stats_driver2:
//   H hets hom1 hom2 midp          -> SNPHWE2 (p)
//   T hets hom1 hom2 midp thresh   -> SNPHWE_t / SNPHWE_midp_t (1 = fails, i.e. p < thresh)
//   F m11 m12 m21 m22 midp         -> fisher22 (p)
#include <stdio.h>
#include <stdint.h>
#include <math.h>
double SNPHWE2(int32_t obs_hets, int32_t obs_hom1, int32_t obs_hom2, uint32_t midp);
int32_t SNPHWE_t(int32_t obs_hets, int32_t obs_hom1, int32_t obs_hom2, double thresh);
int32_t SNPHWE_midp_t(int32_t obs_hets, int32_t obs_hom1, int32_t obs_hom2, double thresh);
double fisher22(uint32_t m11, uint32_t m12, uint32_t m21, uint32_t m22, uint32_t midp);
int main(void) {
  char line[512]; char kind; long long a, b, c, d; int midp; double thresh;
  while (fgets(line, sizeof line, stdin)) {
    if (sscanf(line, " %c", &kind) != 1) continue;
    if (kind == 'H') {
      if (sscanf(line, " H %lld %lld %lld %d", &a, &b, &c, &midp) != 4) continue;
      printf("H %lld %lld %lld %d %.17g\n", a, b, c, midp, SNPHWE2((int32_t)a, (int32_t)b, (int32_t)c, midp));
    } else if (kind == 'T') {
      if (sscanf(line, " T %lld %lld %lld %d %lf", &a, &b, &c, &midp, &thresh) != 5) continue;
      // caller convention (plink_filter.c enforce_hwe_threshold): thresh *= 1 - SMALL_EPSILON (2^-44)
      double t = thresh * (1 - 5.684341886080802e-14);
      printf("T %lld %lld %lld %d %.17g %d\n", a, b, c, midp, thresh, midp? SNPHWE_midp_t((int32_t)a, (int32_t)b, (int32_t)c, t) : SNPHWE_t((int32_t)a, (int32_t)b, (int32_t)c, t));
    } else if (kind == 'F') {
      if (sscanf(line, " F %lld %lld %lld %lld %d", &a, &b, &c, &d, &midp) != 5) continue;
      printf("F %lld %lld %lld %lld %d %.17g\n", a, b, c, d, midp, fisher22((uint32_t)a, (uint32_t)b, (uint32_t)c, (uint32_t)d, midp));
    }
    fflush(stdout);
  }
  return 0;
}
