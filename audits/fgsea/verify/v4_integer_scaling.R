## Since 1.37.1 prepareStats() rounds |stat|^gseaParam * floor(2^30 / sum) to integers (R/fgsea.R:63-73).
## How far does the reported ES move from the double-precision definition, on ranking metrics people
## use?  The reference ES is computed here in R from the definition (independent of fgsea code).
## Usage: R_LIBS=<fgsea lib>:<deps lib> Rscript v4_integer_scaling.R
suppressPackageStartupMessages({library(fgsea); library(BiocParallel)})
cat("fgsea", as.character(packageVersion("fgsea")), "\n")
refES <- function(stats, members, p = 1) {
    o <- order(stats, decreasing = TRUE); s <- stats[o]; n <- length(s)
    pos <- sort(match(members, names(s))); pos <- pos[!is.na(pos)]; k <- length(pos)
    w <- abs(s[pos])^p; NR <- sum(w); if (NR == 0) { w <- rep(1, k); NR <- k }
    tops <- cumsum(w) / NR - (pos - seq_len(k)) / (n - k); bottoms <- tops - w / NR
    mx <- max(tops); mn <- min(bottoms); if (mx > -mn) mx else if (mx < -mn) mn else 0
}
set.seed(11); n <- 20000; g <- sprintf("G%05d", 1:n)
pv <- c(runif(n - 1500), 10^-runif(1500, 2, 320)); lfc <- rnorm(n)
metrics <- list(
  "sign(lfc) * -log10(p), p down to 1e-320 (capped at 320)" = sign(lfc) * pmin(-log10(pv), 320),
  "Wald-like statistic, t(3) tails" = rt(n, 3) * 2,
  "log2FC (single-cell avg_log2FC-like, many near zero)" = c(rnorm(2000, 0, 2), rnorm(n - 2000, 0, 0.02)),
  "sign(lfc) * baseMean (sum >> 2^30)" = sign(lfc) * 10^runif(n, -1, 7)
)
pw <- lapply(1:400, function(i) sample(g, sample(15:500, 1)))
names(pw) <- sprintf("P%03d", 1:400)
for (mn in names(metrics)) for (gp in c(1, 2)) {
    st <- setNames(metrics[[mn]], g)
    r <- suppressWarnings(fgseaSimple(pw, st, nperm = 10, minSize = 15, maxSize = 500, gseaParam = gp, BPPARAM = SerialParam()))
    ref <- sapply(r$pathway, function(p) refES(st, pw[[p]], gp))
    d <- abs(r$ES - ref)
    sc <- 2^30 / sum(abs(st)^gp); sc <- if (sc >= 1) floor(sc) else sc
    nz <- sum(round(abs(st)^gp * sc) == 0 & st != 0)
    cat(sprintf("%-58s gseaParam=%d: scale %.4g; %d nonzero stats rounded to 0; max |ES - ref| = %.2e (median %.1e) over %d sets\n",
                mn, gp, sc, nz, max(d), median(d), length(d)))
}
