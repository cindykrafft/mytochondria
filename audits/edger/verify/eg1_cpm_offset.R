#!/usr/bin/env Rscript
# EG1: cpm()/rpkm() on a DGEList that carries an offset matrix, and aveLogCPM()
# with an offset argument.
#
# edgeR's convention (getOffset.R, scaleOffset.R, glmFit) is that y$offset is the
# FULL offset: log of the effective library size for each observation, i.e. it
# replaces log(lib.size * norm.factors). The cpm.default() of the 4.10.0/4.10.1
# tarball (R/cpm.R, "Last modified 12 Apr 2026") instead row-centres the offset
# and adds it to log(lib.size), so a library-size pattern that is present in the
# offset is applied twice. The release branch reverted this on 2026-08-09
# ("Restoring previous behavior in that offset matrix input to cpm() take
# precedence over lib.size and offset.prior") and fixed aveLogCPM() with an
# offset on 2026-08-29 (4.10.4). Neither change has a NEWS entry.
#
# Reference values are plain arithmetic on the counts, not edgeR functions:
#   cpm_ref  = counts / exp(offset) * 1e6
#   logcpm_ref = log2((counts + p_j) / (exp(offset) + 2 p_j) * 1e6),
#                p_j = prior.count * exp(offset_j) / mean_j exp(offset_j)   (row-wise)
suppressMessages(library(edgeR))
cat("edgeR", as.character(packageVersion("edgeR")), " limma", as.character(packageVersion("limma")), "\n")
set.seed(1)
G <- 2000; n <- 6
L <- c(1e6, 2e6, 4e6, 1e6, 2e6, 4e6)           # four-fold range of library sizes
mu <- rgamma(G, shape=2, scale=50)
y <- matrix(rnbinom(G*n, mu=outer(mu, L/1e6), size=10), G, n)
dge <- DGEList(y, lib.size=L)                  # norm.factors are 1

relerr <- function(a, b) { ok <- is.finite(a) & is.finite(b) & b != 0; max(abs(a[ok]/b[ok] - 1)) }

# --- A: an offset equal to log(lib.size) must reproduce cpm() without offset ------
off <- matrix(log(L), G, n, byrow=TRUE)
stopifnot(all.equal(scaleOffset(dge, off)$offset, off))   # scaleOffset() leaves it unchanged
dgeA <- dge; dgeA$offset <- off
ref <- t(t(y)/L)*1e6
c0 <- cpm(dge); cA <- cpm(dgeA)
cat("\n[A] offset == log(lib.size)\n")
cat("  cpm(no offset)   vs counts/L*1e6 : max rel err", signif(relerr(c0, ref), 3), "\n")
cat("  cpm(with offset) vs counts/L*1e6 : max rel err", signif(relerr(cA, ref), 3), "\n")
cat("  per-column median cpm(offset)/cpm(none):", signif(apply(cA/c0, 2, median, na.rm=TRUE), 4), "\n")
cat("  L / geomean(L)                          :", signif(L/exp(mean(log(L))), 4), "\n")
lc0 <- cpm(dge, log=TRUE); lcA <- cpm(dgeA, log=TRUE)
cat("  log2-cpm: max |cpm(offset,log) - cpm(none,log)| =", signif(max(abs(lcA - lc0)), 4), "\n")

# --- B: gene-specific offsets on the log-library-size scale (cqn / EDASeq style) ---
dev <- matrix(rnorm(G*n, 0, 0.3), G, n); dev <- dev - rowMeans(dev)
offB <- off + dev
dgeB <- dge; dgeB$offset <- offB
refB <- y/exp(offB)*1e6
pj <- 2 * exp(offB) / rowMeans(exp(offB))
lrefB <- log2((y + pj)/(exp(offB) + 2*pj)*1e6)
cB <- cpm(dgeB); lcB <- cpm(dgeB, log=TRUE)
cat("\n[B] gene-specific offset = log(L_j) + centred deviation\n")
cat("  cpm      vs counts/exp(offset)*1e6        : max rel err", signif(relerr(cB, refB), 3), "\n")
cat("  log2-cpm vs prior-count formula on exp(offset): max |diff|", signif(max(abs(lcB - lrefB)), 3), "\n")
fit <- glmFit(dgeB, design=matrix(1, n, 1), dispersion=0.1)
rowspread <- apply(fit$fitted.values/exp(offB), 1, function(r) diff(range(r))/mean(r))
cat("  glmFit treats the offset as the full log library size: max within-gene spread of fitted/exp(offset) =", signif(max(rowspread), 3), "\n")
dgeB$genes <- data.frame(Length=rep(1000, G))
rB <- rpkm(dgeB)
cat("  rpkm (length 1 kb) vs counts/exp(offset)*1e6 : max rel err", signif(relerr(rB, refB), 3), "\n")

# --- C: aveLogCPM(y, offset=) --------------------------------------------------------
# reference: one-group NB fit with prior counts (edgeR's own definition; port in
# ../verify/heldup_cpm_avelogcpm.py checks the fit itself). Here only: does the
# offset argument change the answer relative to lib.size when offset == log(lib.size)?
a0 <- aveLogCPM(y, lib.size=L)
aA <- aveLogCPM(y, offset=off)
cat("\n[C] aveLogCPM(y, offset=log L) vs aveLogCPM(y, lib.size=L): max |diff| =", signif(max(abs(aA - a0)), 4), "\n")
aB <- aveLogCPM(y, offset=offB)
cat("    aveLogCPM(y, offset=gene-specific) range:", signif(range(aB), 5), "   (lib.size version range:", signif(range(a0), 5), ")\n")

# --- D: getOffset() with a prior offset whose rows are not centred -----------------
dgeC <- dge; dgeC$offset.prior <- dev + 0.1
o <- try(getOffset(dgeC), silent=TRUE)
if (inherits(o, "try-error")) {
  cat("\n[D] getOffset() with non-centred offset.prior: ERROR:", conditionMessage(attr(o, "condition")), "\n")
} else {
  cat("\n[D] getOffset() with non-centred offset.prior: dim", paste(dim(o), collapse="x"),
      " max |offset - (log L + centred prior)| =", signif(max(abs(o - t(t(dev) + log(L)))), 4), "\n")
}
