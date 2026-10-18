## A gene set whose members are all present but all have stat exactly 0 (e.g. genes expressed in
## neither group when every gene is ranked by avg_log2FC, or NA statistics replaced by 0).
## calcGseaStat() gives such a set equal weights (R/fgsea.R:133-147, "equivalent to rAdj being
## rep(eps, m)"), so its ES is set by where the zero block sits in the ranking and by the input
## order inside the block; prepareStats() leaves zeros out of the ties warning (R/fgsea.R:47).
## Usage: R_LIBS=<fgsea lib>:<deps lib> Rscript v7_zero_block.R
suppressPackageStartupMessages({library(fgsea); library(BiocParallel)})
cat("fgsea", as.character(packageVersion("fgsea")), "\n")
set.seed(5)
n <- 20000; g <- sprintf("G%05d", 1:n)
nz <- 6000                                         # genes with stat exactly 0 (30 %)
st <- setNames(c(rnorm(n - nz, 0, 0.6), rep(0, nz)), g)
st <- st[sample(n)]                                # input order unrelated to the stats
zeros <- names(st)[st == 0]
pw <- c(list(ALL_ZERO_RANDOM = sample(zeros, 100),               # 100 zero genes scattered in input order
             ALL_ZERO_CLUSTERED = zeros[2001:2100],              # 100 zero genes adjacent in input order
             ZERO_PLUS_ONE = c(sample(zeros, 99), names(st)[st > 0.3][1])),  # one non-zero member
        setNames(lapply(1:200, function(i) sample(g, 100)), sprintf("RANDOM_%03d", 1:200)))
set.seed(1)
r <- fgseaMultilevel(pw, st, minSize = 15, maxSize = 500, BPPARAM = SerialParam())
cat("warnings above (if any) are fgsea's; none mentions the 6,000 zero statistics\n")
print(r[pathway %in% c("ALL_ZERO_RANDOM", "ALL_ZERO_CLUSTERED", "ZERO_PLUS_ONE"), .(pathway, ES, NES, pval, padj, size)])
rr <- r[grepl("^RANDOM_", pathway)]
cat(sprintf("200 random 100-gene sets: |ES| median %.3f, max %.3f; min padj %.3g\n", median(abs(rr$ES)), max(abs(rr$ES)), min(rr$padj)))
## the same zero-gene set when the input order inside the zero block changes
st2 <- st[order(names(st) %in% pw$ALL_ZERO_CLUSTERED, decreasing = TRUE)]  # members first in input order
st3 <- st[order(names(st) %in% pw$ALL_ZERO_CLUSTERED)]                      # members last in input order
for (lab in c("members first in input order", "members last in input order")) {
    s <- if (lab == "members first in input order") st2 else st3
    set.seed(1); x <- fgseaMultilevel(pw["ALL_ZERO_CLUSTERED"], s, BPPARAM = SerialParam())
    cat(sprintf("ALL_ZERO_CLUSTERED, %s: ES %.3f  NES %.2f  pval %.3g\n", lab, x$ES, x$NES, x$pval))
}
