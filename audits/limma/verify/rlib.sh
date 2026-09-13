#!/bin/sh
# Select which built limma goes on R_LIBS_USER. Usage: . ./rlib.sh <version>
# Builds made for this audit (private libraries under the scratchpad; see ../README.md):
#   3.58.1  the apt r-bioc-limma on this host (system library)
#   3.34.0  Ubuntu pool orig tarball r-bioc-limma_3.34.0+dfsg (Bioconductor 3.6, 2017)
#   3.42.2  Ubuntu pool orig tarball (Bioconductor 3.10, 2020)
#   3.62.2  Ubuntu pool orig tarball (Bioconductor 3.20, 2024-2025)
#   3.68.4  Ubuntu pool orig tarball (Bioconductor 3.23, 2026-08)
#   3.68.5  bioc/limma mirror, branch RELEASE_3_23 @ 825d1c83 (2026-08-10, current release branch)
#   devel   bioc/limma mirror, branch devel @ 57a8de72 (3.99.0, 2026-08-30)
#   devel-patched   the same plus the two kit patches (../upstream/0001*, 0002*)
#   3.68.5-patched  RELEASE_3_23 @ 825d1c83 plus ../upstream/0001-*.RELEASE_3_23.patch
# All installed with: R CMD INSTALL --no-docs --library=<lib> <source>
S=${LIMMA_SCRATCH:-/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/scratchpad/limma}
case "$1" in
  3.58.1|system) unset R_LIBS_USER ;;
  3.34.0)  export R_LIBS_USER=$S/lib_3.34.0 ;;
  3.42.2)  export R_LIBS_USER=$S/lib_3.42.2 ;;
  3.62.2)  export R_LIBS_USER=$S/lib_3.62.2 ;;
  3.68.4)  export R_LIBS_USER=$S/lib_3.68.4 ;;
  3.68.5)  export R_LIBS_USER=$S/lib_rel323 ;;
  devel)   export R_LIBS_USER=$S/lib_devel ;;
  devel-patched)  export R_LIBS_USER=$S/lib_kit_devel ;;
  3.68.5-patched) export R_LIBS_USER=$S/lib_kit_rel ;;
  *) echo "unknown version $1" >&2; exit 1 ;;
esac
