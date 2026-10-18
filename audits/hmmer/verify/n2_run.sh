#!/bin/sh
# Build n2_null2_bytrace.c against a HMMER build tree and run it.
# usage: n2_run.sh <build tree> <out file>     (fn3 model; test-2 sequences: human Swiss-Prot entries
# whose fn3 search has a clustered region, extracted to $HM_SCRATCH/data/uniprot/clu_fn3.fa)
B=$1; OUT=$2
S=${HM_SCRATCH:-/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/scratchpad/audit-hmmer}
D=$(dirname "$0")
DSS=""; [ -d "$B/libdivsufsort" ] && DSS="-L$B/libdivsufsort -ldivsufsort"
DEF=""; grep -q "p7_hmmfile_Open *(const char \*filename, char \*env, P7_HMMFILE \*\*ret_hfp)\|p7_hmmfile_Open *(char \*filename, char \*env, P7_HMMFILE \*\*ret_hfp)" "$B/src/hmmer.h" && DEF="-DHM_PRE34"
grep -q "ByPosteriorHeuristics(const ESL_SQ \*sq, P7_OPROFILE" "$B/src/hmmer.h" && DEF="$DEF -DHM_PRE32"
gcc -O2 $DEF -o "$S/n2.bin" "$D/n2_null2_bytrace.c" -I"$B/src" -I"$B/src/impl_sse" -I"$B/easel" -L"$B/src" -L"$B/easel" -lhmmer -leasel $DSS -lpthread -lm || exit 1
{ echo "# n2_null2_bytrace on $B ($("$B/src/hmmsearch" -h | sed -n 2p | sed 's/^# //'))"
  "$S/n2.bin" "$S/hmmer/tutorial/fn3.hmm" 7 "$S/data/uniprot/clu_fn3.fa"
  "$S/n2.bin" "$S/hmmer/tutorial/Pkinase.hmm" 7 "$S/data/uniprot/clu_Pkinase.fa"; } > "$OUT" 2>&1
cat "$OUT"
