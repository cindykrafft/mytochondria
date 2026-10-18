/* n2_null2_bytrace.c : HM1 and HM2, the null2 (biased-composition) correction computed
 * from stochastic traces in multidomain regions.
 *
 * Test 1 (HM1). For sequences emitted from the profile (so the true trace, including insert
 * states, is known), compare the production SSE p7_Null2_ByTrace() with the generic reference
 * p7_GNull2_ByTrace() on every domain of the trace. Both are documented as computing the same
 * null2 odds; the generic one counts an insert-state residue with the insert emission odds
 * (insert scores are 0 in a configured profile, so odds 1.0), and the SSE one sums the insert
 * slot with "insert odds implicitly 1.0" -- if it puts the counts there.
 *
 * Test 2 (HM2). For each sequence in <seqfile> whose domain definition sends a region to
 * stochastic traceback clustering, re-derive the per-residue null2 scores of the region from
 * the same 200 sampled traces (same RNG seed, same Forward matrix), once under the stated rule
 * ("residues outside domains get +1; residues inside domains get their null2 ratio", with the
 * domain spanning sqfrom..sqto, the first and last M-emitted residues) and once with the loop as
 * written (pos <= sqfrom counted as outside), and report which one the library's ddef->n2sc
 * reproduces.
 *
 * Build (against any build tree B):
 *   gcc -O2 -o n2 n2_null2_bytrace.c -I$B/src -I$B/src/impl_sse -I$B/easel -L$B/src -L$B/easel \
 *       [-L$B/libdivsufsort] -lhmmer -leasel [-ldivsufsort] -lpthread -lm
 * Usage: ./n2 <hmmfile> <seed> [seqfile for test 2]
 */
#include <p7_config.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include "easel.h"
#include "esl_random.h"
#include "esl_randomseq.h"
#include "esl_sq.h"
#include "esl_sqio.h"
#include "esl_vectorops.h"
#include "hmmer.h"

static int
count_inserts(const P7_TRACE *tr, int z1, int z2)
{
  int z, n = 0;
  for (z = z1; z <= z2; z++) if (tr->st[z] == p7T_I) n++;
  return n;
}

int
main(int argc, char **argv)
{
  char           *hmmfile = argv[1];
  int             seed    = (argc > 2 ? atoi(argv[2]) : 7);
  ESL_RANDOMNESS *r       = esl_randomness_CreateFast(seed);
  ESL_ALPHABET   *abc     = NULL;
  P7_HMMFILE     *hfp     = NULL;
  P7_HMM         *hmm     = NULL;
  P7_BG          *bg;
  P7_PROFILE     *gm;
  P7_OPROFILE    *om;
  ESL_SQ         *sq;
  P7_TRACE       *tr;
  P7_GMX         *gwrk;
  P7_OMX         *owrk;
  float           gn2[p7_MAXCODE], on2[p7_MAXCODE];
  int             n, d, x, L = 400;
  int             ndom_ins = 0, ndom_noins = 0, bad_ins = 0, bad_noins = 0;
  double          maxdiff_ins = 0., maxdiff_noins = 0.;

  setvbuf(stdout, NULL, _IONBF, 0);
  impl_Init();
#ifdef HM_PRE34   /* 3.3.2 and earlier: three-argument p7_hmmfile_Open() */
  if (p7_hmmfile_Open(hmmfile, NULL, &hfp) != eslOK) p7_Fail("open %s", hmmfile);
#else
  if (p7_hmmfile_Open(hmmfile, NULL, &hfp, NULL) != eslOK) p7_Fail("open %s", hmmfile);
#endif
  if (p7_hmmfile_Read(hfp, &abc, &hmm)           != eslOK) p7_Fail("read %s", hmmfile);
  bg   = p7_bg_Create(abc);  p7_bg_SetLength(bg, L);
  gm   = p7_profile_Create(hmm->M, abc);
  p7_ProfileConfig(hmm, bg, gm, L, p7_LOCAL);
  om   = p7_oprofile_Create(hmm->M, abc);
  p7_oprofile_Convert(gm, om);
  sq   = esl_sq_CreateDigital(abc);
  tr   = p7_trace_Create();
  gwrk = p7_gmx_Create(hmm->M, 1024);
  owrk = p7_omx_Create(hmm->M, 1024, 1024);

  /* ---------------- Test 1 ---------------- */
  for (n = 0; n < 500; n++)
    {
      p7_ProfileEmit(r, hmm, gm, bg, sq, tr);
      p7_trace_Index(tr);
      for (d = 0; d < tr->ndom; d++)
        {
          int    nins = count_inserts(tr, tr->tfrom[d], tr->tto[d]);
          double md   = 0.;
          p7_GNull2_ByTrace(gm, tr, tr->tfrom[d], tr->tto[d], gwrk, gn2);
          p7_Null2_ByTrace (om, tr, tr->tfrom[d], tr->tto[d], owrk, on2);
          for (x = 0; x < abc->K; x++) md = ESL_MAX(md, fabs(log(gn2[x]) - log(on2[x])));
          if (nins) { ndom_ins++;   if (md > 1e-4) bad_ins++;   maxdiff_ins   = ESL_MAX(maxdiff_ins, md); }
          else      { ndom_noins++; if (md > 1e-4) bad_noins++; maxdiff_noins = ESL_MAX(maxdiff_noins, md); }
        }
      p7_trace_Reuse(tr);
      esl_sq_Reuse(sq);
    }
  printf("TEST1 %s: domains without insert states: %d, SSE != generic in %d (max |log odds diff| %.2g)\n",
         hmm->name, ndom_noins, bad_noins, maxdiff_noins);
  printf("TEST1 %s: domains with insert states:    %d, SSE != generic in %d (max |log odds diff| %.2g)\n",
         hmm->name, ndom_ins, bad_ins, maxdiff_ins);

  /* ---------------- Test 2 ---------------- */
  if (argc > 3)
  {
    ESL_SQFILE *sqfp = NULL;
    ESL_SQ     *big  = esl_sq_CreateDigital(abc);
    P7_TRACE   *str  = p7_trace_Create();
    float      *n2_rule = NULL, *n2_code = NULL;
    float       null2[p7_MAXCODE];
    float       fwdsc;
    int         j, Lt, ireg, jreg, triggered, pos, t;
    int         nseq = 0, nclu = 0, ncmp = 0, match_code = 0, match_rule = 0, nseqclu = 0;
    double      maxd_code = 0., maxd_rule = 0.;

    if (esl_sqfile_OpenDigital(abc, argv[3], eslSQFILE_FASTA, NULL, &sqfp) != eslOK) p7_Fail("open %s", argv[3]);
    while (esl_sqio_Read(sqfp, big) == eslOK)
      {
        P7_DOMAINDEF *ddef = p7_domaindef_Create(esl_randomness_CreateFast(42));
        P7_OMX *oxf, *oxb, *fwd, *bck;
        int     seqclu = 0;
        Lt = big->n;
        p7_oprofile_ReconfigLength(om, Lt);
        p7_bg_SetLength(bg, Lt);
        oxf = p7_omx_Create(hmm->M, 0, Lt);   oxb = p7_omx_Create(hmm->M, 0, Lt);
        fwd = p7_omx_Create(hmm->M, Lt, Lt);  bck = p7_omx_Create(hmm->M, Lt, Lt);
        p7_ForwardParser (big->dsq, Lt, om, oxf, &fwdsc);
        p7_BackwardParser(big->dsq, Lt, om, oxf, oxb, NULL);
#ifdef HM_PRE32   /* 3.1b2: no <ntsq> argument */
        p7_domaindef_ByPosteriorHeuristics(big, om, oxf, oxb, fwd, bck, ddef, bg, FALSE, NULL, NULL, NULL);
#else
        p7_domaindef_ByPosteriorHeuristics(big, NULL, om, oxf, oxb, fwd, bck, ddef, bg, FALSE, NULL, NULL, NULL);
#endif
        nseq++;
        n2_rule = realloc(n2_rule, sizeof(float) * (Lt+1));
        n2_code = realloc(n2_code, sizeof(float) * (Lt+1));

        /* re-derive the regions from the decoding arrays, exactly as the library does */
        ireg = -1; triggered = FALSE;
        for (j = 1; j <= Lt; j++)
          {
            if (!triggered) {
              if      (ddef->mocc[j] - (ddef->btot[j] - ddef->btot[j-1]) < ddef->rt2) ireg = j;
              else if (ireg == -1) ireg = j;
              if      (ddef->mocc[j] >= ddef->rt1) triggered = TRUE;
            } else if (ddef->mocc[j] - (ddef->etot[j] - ddef->etot[j-1]) < ddef->rt2) {
              int z; float maxe = -1., e;
              jreg = j;
              for (z = ireg; z < jreg; z++) { e = ESL_MIN(ddef->etot[z]-ddef->etot[ireg-1], ddef->btot[jreg]-ddef->btot[z]); maxe = ESL_MAX(maxe, e); }
              if (maxe >= ddef->rt3) {   /* clustered region: replicate its trace ensemble */
                int Lr = jreg - ireg + 1;
                ESL_RANDOMNESS *r2 = esl_randomness_CreateFast(42);   /* ddef's RNG is reset to its seed (42) per region */
                nclu++; seqclu++;
                p7_oprofile_ReconfigMultihit(om, Lt);
                p7_omx_GrowTo(fwd, om->M, Lr, Lr);
                p7_Forward(big->dsq + ireg - 1, Lr, om, fwd, NULL);
                for (pos = ireg; pos <= jreg; pos++) n2_rule[pos] = n2_code[pos] = 0.;
                for (t = 0; t < ddef->nsamples; t++) {
                  int p1 = 1, p2 = 1, d;
                  p7_StochasticTrace(r2, big->dsq + ireg - 1, Lr, om, fwd, str);
                  p7_trace_Index(str);
                  for (d = 0; d < str->ndom; d++) {
                    p7_Null2_ByTrace(om, str, str->tfrom[d], str->tto[d], bck, null2);
                    /* as written in p7_domaindef.c region_trace_ensemble() */
                    for (; p1 <= str->sqfrom[d]; p1++) n2_code[ireg+p1-1] += 1.0;
                    for (; p1 <= str->sqto[d];   p1++) n2_code[ireg+p1-1] += null2[big->dsq[ireg+p1-1]];
                    /* stated rule: the domain is sqfrom..sqto inclusive */
                    for (; p2 <  str->sqfrom[d]; p2++) n2_rule[ireg+p2-1] += 1.0;
                    for (; p2 <= str->sqto[d];   p2++) n2_rule[ireg+p2-1] += null2[big->dsq[ireg+p2-1]];
                  }
                  for (; p1 <= Lr; p1++) n2_code[ireg+p1-1] += 1.0;
                  for (; p2 <= Lr; p2++) n2_rule[ireg+p2-1] += 1.0;
                  p7_trace_Reuse(str);
                }
                for (pos = ireg; pos <= jreg; pos++) {
                  double dc, dr;
                  n2_code[pos] = logf(n2_code[pos] / (float) ddef->nsamples);
                  n2_rule[pos] = logf(n2_rule[pos] / (float) ddef->nsamples);
                  dc = fabs(n2_code[pos] - ddef->n2sc[pos]); dr = fabs(n2_rule[pos] - ddef->n2sc[pos]);
                  ncmp++;
                  if (dc < 1e-5) match_code++;
                  if (dr < 1e-5) match_rule++;
                  maxd_code = ESL_MAX(maxd_code, dc); maxd_rule = ESL_MAX(maxd_rule, dr);
                }
                esl_randomness_Destroy(r2);
                p7_oprofile_ReconfigUnihit(om, Lt);
              }
              ireg = -1; triggered = FALSE;
            }
          }
        if (seqclu) nseqclu++;
        if (seqclu != ddef->nclustered) printf("TEST2 warning: %s: re-derived %d clustered regions, library %d\n", big->name, seqclu, ddef->nclustered);
        p7_oprofile_ReconfigMultihit(om, Lt);
        p7_omx_Destroy(oxf); p7_omx_Destroy(oxb); p7_omx_Destroy(fwd); p7_omx_Destroy(bck);
        esl_randomness_Destroy(ddef->r); p7_domaindef_Destroy(ddef);
        esl_sq_Reuse(big);
      }
    printf("TEST2 %s: %d sequences, %d with clustered regions, %d clustered regions re-derived; per-residue null2 scores compared: %d\n", hmm->name, nseq, nseqclu, nclu, ncmp);
    printf("TEST2 %s: library n2sc == loop as written (residue sqfrom counted outside): %d/%d residues (max diff %.2g)\n", hmm->name, match_code, ncmp, maxd_code);
    printf("TEST2 %s: library n2sc == stated rule (sqfrom..sqto counted inside):       %d/%d residues (max diff %.2g)\n", hmm->name, match_rule, ncmp, maxd_rule);
  }
  return 0;
}
