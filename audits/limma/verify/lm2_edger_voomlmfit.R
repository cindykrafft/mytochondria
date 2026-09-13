# LI2 scope check on edgeR's voomLmFit: edgeR 4.10.5 (RELEASE_3_23) carries the same
# offset handling as limma::voom 3.68 (row-centre the offset and add it to log lib.size);
# edgeR 4.0.16 has no offset argument. Run with the edgeR builds from the edgeR audit:
#   R_LIBS_USER=<edger scratch>/libdeps:<edger scratch>/lib_rel323 Rscript lm2_edger_voomlmfit.R   (edgeR 4.10.5)
#   Rscript lm2_edger_voomlmfit.R                                                            (edgeR 4.0.16, apt)
suppressMessages(library(edgeR))
cat("edgeR", as.character(packageVersion("edgeR")), "limma", as.character(packageVersion("limma")), R.version.string, "\n")
set.seed(81)
counts <- matrix(rnbinom(6*4, mu=100, size=10), 6, 4)
lib <- c(1e6, 4e6, 2e6, 8e6)
y <- DGEList(counts, lib.size=lib)
y$offset <- matrix(log(lib), 6, 4, byrow=TRUE)
if(!"offset" %in% names(formals(edgeR::voomLmFit))) { cat("edgeR::voomLmFit has no offset argument in this version; a DGEList $offset is ignored: ") }
a <- suppressMessages(edgeR::voomLmFit(y)); b <- suppressMessages(edgeR::voomLmFit(counts, lib.size=lib))
d <- a$EList$E - b$EList$E
cat("voomLmFit(DGEList with $offset = log(lib.size)) E minus voomLmFit(counts, lib.size) E, column medians:", format(apply(d, 2, median), digits=4), "\n")
cat("-log2(lib.size/geomean):", format(-log2(lib/exp(mean(log(lib)))), digits=4), "\n")
cat("VERDICT:", if(max(abs(d)) > 0.01) "AFFECTED" else "unaffected", "\n")
