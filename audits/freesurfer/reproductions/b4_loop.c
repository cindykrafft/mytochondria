/* Verbatim reproduction of the mri_vol2surf projection loop.
 *
 * Source: freesurfer/mri_vol2surf/mri_vol2surf.cpp (dev, identical in
 * v6.0.0 and v7.1.1):
 *   line 203: static float ProjFrac = 0;
 *   line 207: static float ProjFracMin=0.0,ProjFracMax=0.0,ProjFracDelta=1.0;
 *   lines 596-598:
 *       for (ProjFrac=ProjFracMin;
 *            ProjFrac <= ProjFracMax;
 *            ProjFrac += ProjFracDelta) {
 *   line 635: if (!GetProjMax) MRImultiplyConst(SurfVals, 1.0/nproj, SurfVals);
 * Args are parsed with sscanf(pargv[i],"%f",...) exactly as below.
 */
#include <stdio.h>

static float ProjFrac = 0;
static float ProjFracMin = 0.0, ProjFracMax = 0.0, ProjFracDelta = 1.0;

int main(int argc, char **argv)
{
  if (argc != 4) { fprintf(stderr, "usage: %s min max delta\n", argv[0]); return 1; }
  sscanf(argv[1], "%f", &ProjFracMin);   /* mri_vol2surf.cpp:1069 */
  sscanf(argv[2], "%f", &ProjFracMax);
  sscanf(argv[3], "%f", &ProjFracDelta);

  int nproj = 0;
  double sum_depth = 0.0, max_depth = -1e9;
  printf("invocation: --projfrac-avg %s %s %s\n", argv[1], argv[2], argv[3]);
  for (ProjFrac = ProjFracMin;
       ProjFrac <= ProjFracMax;
       ProjFrac += ProjFracDelta) {          /* the exact loop */
    printf("  sample %2d at ProjFrac = %.9g\n", nproj + 1, ProjFrac);
    sum_depth += ProjFrac;
    if (ProjFrac > max_depth) max_depth = ProjFrac;
    nproj++;
  }
  /* the average is over the samples actually taken (divides by nproj) */
  double intended_n = (double)((int)(( ( (double)ProjFracMax - ProjFracMin ) / ProjFracDelta ) + 1.0 + 1e-9));
  double intended_mean = (ProjFracMin + ProjFracMax) / 2.0;
  printf("  -> nproj=%d (intended %d)  max sampled depth=%.9g (intended %g)\n",
         nproj, (int)intended_n, max_depth, ProjFracMax);
  printf("  -> effective mean depth=%.6f (intended %.6f)  bias=%+.6f of thickness\n\n",
         sum_depth / nproj, intended_mean, sum_depth / nproj - intended_mean);
  return 0;
}
