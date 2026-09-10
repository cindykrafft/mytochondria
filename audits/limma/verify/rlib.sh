#!/bin/sh
# Select which built limma goes on R_LIBS_USER. Usage: . ./rlib.sh <version>
# Versions built for this audit (private libraries under the scratchpad; see ../README.md):
#   3.58.1  the apt r-bioc-limma on this host (system library)
#   3.34.0  Ubuntu pool orig tarball (cohort names 3.34.9)
#   3.42.2  Ubuntu pool orig tarball
#   3.62.2  Ubuntu pool orig tarball (a cohort version)
#   3.68.4  Ubuntu pool orig tarball (Bioconductor 3.23 release)
#   3.68.5  bioc/limma mirror, branch RELEASE_3_23 @ 825d1c83 (2026-08-10)
#   devel   bioc/limma mirror, branch devel @ 57a8de72 (3.99.0, 2026-08-30)
S=${LIMMA_SCRATCH:-/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/scratchpad/limma}
case "$1" in
  3.58.1|system) unset R_LIBS_USER ;;
  3.34.0)  export R_LIBS_USER=$S/lib_3.34.0 ;;
  3.42.2)  export R_LIBS_USER=$S/lib_3.42.2 ;;
  3.62.2)  export R_LIBS_USER=$S/lib_3.62.2 ;;
  3.68.4)  export R_LIBS_USER=$S/lib_3.68.4 ;;
  3.68.5)  export R_LIBS_USER=$S/lib_rel323 ;;
  devel)   export R_LIBS_USER=$S/lib_devel ;;
  *) echo "unknown version $1" >&2; exit 1 ;;
esac
