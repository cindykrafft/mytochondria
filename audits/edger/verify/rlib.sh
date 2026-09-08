#!/bin/sh
# Select which built edgeR goes on R_LIBS_USER. Usage: . ./rlib.sh <version>
# Versions built for this audit (private libraries under the scratchpad; see ../README.md):
#   4.0.16  the apt r-bioc-edger on this host (system library, limma 3.58.1)
#   4.4.2   Ubuntu pool orig tarball, built against limma 3.68.4
#   4.10.1  Ubuntu pool orig tarball (Bioconductor 3.23 as of 2026-05-23)
#   4.10.5  bioc/edgeR mirror, branch RELEASE_3_23 @ c4a54bda (2026-09-04)
#   devel   bioc/edgeR mirror, branch devel @ db4e697f (4.99.4, 2026-09-06)
#   3.36.0  Ubuntu pool orig tarball, FCONE-patched to compile on R 4.3 (see README)
S=${EDGER_SCRATCH:-/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/scratchpad/edger}
case "$1" in
  4.0.16|system) unset R_LIBS_USER ;;
  4.4.2)   export R_LIBS_USER=$S/libdeps:$S/lib4.4.2 ;;
  4.10.1)  export R_LIBS_USER=$S/libdeps:$S/lib4.10.1 ;;
  4.10.5)  export R_LIBS_USER=$S/libdeps:$S/lib_rel323 ;;
  devel)   export R_LIBS_USER=$S/libdeps:$S/lib_src ;;
  3.36.0)  export R_LIBS_USER=$S/lib3.36.0 ;;
  *) echo "unknown version $1" >&2; exit 1 ;;
esac
