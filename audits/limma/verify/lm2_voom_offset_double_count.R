# LM2: voom() (3.68.0+) treats an edgeR-style offset matrix -- one that carries the log
# library sizes, as edgeR's y$offset from scaleOffset()/cqn/EDASeq does -- by row-centring it
# and ADDING it to log(lib.size) (R/voom.R:55-67), so the effective library size becomes
# lib.size^2/geomean(lib.size) (times the gene-specific part): the library sizes are counted
# twice. edgeR's own cpm() reverted the same construction in August 2026, and devel's
# voomLmFit() uses exp(offset) as the library size, so voom() and voomLmFit() now disagree on
# the same DGEList. Run: . ./rlib.sh <version>; Rscript lm2_voom_offset_double_count.R
suppressMessages(library(limma)); suppressMessages(library(edgeR))
cat("limma", as.character(packageVersion("limma")), "edgeR", as.character(packageVersion("edgeR")), R.version.string, "\n")
mx <- function(a, b) max(abs(a - b), na.rm=TRUE)
if(!"offset" %in% names(formals(voom))) cat("voom() has no offset argument in this version; a DGEList $offset is ignored:\n")

## ---- A. minimal example: an offset equal to log(lib.size) must be a no-op --------------
set.seed(81)
counts <- matrix(rnbinom(6*4, mu=100, size=10), 6, 4)
lib <- c(1e6, 4e6, 2e6, 8e6)                                   # four-fold to eight-fold library sizes
y <- DGEList(counts, lib.size=lib)
y$offset <- matrix(log(lib), 6, 4, byrow=TRUE)                 # the trivial edgeR offset: log library sizes, as scaleOffset(y, 0) would store
a <- voom(y, plot=FALSE); b <- voom(counts, lib.size=lib, plot=FALSE)
d <- a$E - b$E
cat("A. voom(DGEList with $offset = log(lib.size))$E - voom(counts, lib.size)$E, by column:\n")
print(signif(d, 5))
gm <- exp(mean(log(lib)))
cat("   -log2(lib.size/geomean(lib.size)) =", format(-log2(lib/gm), digits=5), "\n")
cat(sprintf("   max |difference| = %.4f log2 units (expected 0)\n", mx(a$E, b$E)))
Lused <- (counts[1,] + 0.5)/2^a$E[1,]*1e6 - 1
cat("   library sizes voom actually used / lib.size:", format(Lused/lib, digits=5), " = lib.size/geomean:", format(lib/gm, digits=5), "\n")
if(exists("voomLmFit", asNamespace("limma"))) {
  fl <- suppressMessages(voomLmFit(y))
  cat(sprintf("   devel voomLmFit(same DGEList): max |E - voom(counts, lib.size)$E| = %.2e (uses exp(offset) as library size)\n", mx(fl$EList$E, b$E)))
}

## ---- B. effect on a two-group analysis when library sizes differ between groups ----------
set.seed(82)
G <- 6000; n <- 8
grp <- rep(0:1, each=4); design <- cbind(Int=1, grp=grp)
mu <- rexp(G, 1/200)
L <- c(0.5, 0.7, 0.6, 0.8, 1.6, 2.0, 1.8, 1.4)                # group 2 sequenced 2.5x deeper (factor on mu)
lambda <- outer(mu, L) * (1 + outer(rep(c(0,1), c(G-500, 500)), grp))    # 500 genes 2x up in group 2
cts <- matrix(rnbinom(G*n, mu=lambda, size=8), G, n)
ls <- colSums(cts)
y <- DGEList(cts); y$offset <- matrix(log(ls), G, n, byrow=TRUE)      # offset carrying only the library sizes
vo <- voom(y, design, plot=FALSE); vr <- voom(cts, design, lib.size=ls, plot=FALSE)
fo <- eBayes(lmFit(vo, design)); fr <- eBayes(lmFit(vr, design))
cat(sprintf("B. logFC(grp): offset run - reference run: median %.4f, range %.4f..%.4f (log2 of the group library-size ratio: %.4f)\n",
            median(fo$coefficients[,2]-fr$coefficients[,2]), min(fo$coefficients[,2]-fr$coefficients[,2]), max(fo$coefficients[,2]-fr$coefficients[,2]),
            mean(log2(ls[grp==1]/exp(mean(log(ls))))) - mean(log2(ls[grp==0]/exp(mean(log(ls)))))))
dto <- as.vector(decideTests(fo)[,2]); dtr <- as.vector(decideTests(fr)[,2])
cat(sprintf("   genes at adj.P<0.05: offset run %d (%d up, %d down; %d true) vs reference %d (%d up, %d down; %d true); true DE = 500\n",
            sum(dto != 0), sum(dto > 0), sum(dto < 0), sum(dto[(G-499):G] != 0),
            sum(dtr != 0), sum(dtr > 0), sum(dtr < 0), sum(dtr[(G-499):G] != 0)))
# cqn/EDASeq-style offset: log(lib.size) + gene-specific term with zero row means
dg <- matrix(rnorm(G*n, 0, 0.3), G, n); dg <- dg - rowMeans(dg)
y$offset <- matrix(log(ls), G, n, byrow=TRUE) + dg
vo2 <- voom(y, design, plot=FALSE)
E.edger <- log2((cts + 0.5)/(exp(y$offset) + 1)*1e6)                       # counts over the effective library size the offset encodes
E.voom  <- log2((cts + 0.5)/(exp(y$offset + rep(log(ls/exp(mean(log(ls)))), each=G)) + 1)*1e6)   # lib.size counted twice
cat(sprintf("   gene-specific offset log(lib.size)+d: voom$E vs edgeR reading exp(offset): %.4f ; vs lib.size^2/geomean * exp(d): %.2e\n", mx(vo2$E, E.edger), mx(vo2$E, E.voom)))
cat(sprintf("   offset.prior = d given explicitly instead: voom$E vs edgeR reading: %.2e\n", mx(voom(cts, design, lib.size=ls, offset.prior=dg, plot=FALSE)$E, E.edger)))
cat("\nVERDICT:", if(mx(a$E, b$E) > 0.01) "AFFECTED" else "unaffected", "\n")
