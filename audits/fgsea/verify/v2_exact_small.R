## p-values and NES for scoreType std / pos / neg on short lists, for comparison with an exact
## enumeration of all C(n, k) gene sets (v2_exact_small.py).  The lists include tied and zero
## statistics.  Usage: R_LIBS=<fgsea lib>:<deps lib> Rscript v2_exact_small.R <dir> <label>
args <- commandArgs(TRUE); d <- args[1]; label <- args[2]
suppressPackageStartupMessages({library(fgsea); library(jsonlite); library(BiocParallel)})
designs <- list(
  list(name = "N24k3", N = 24, ties = FALSE, sets = list(c(1, 2, 12), c(8, 12, 16), c(20, 22, 23), c(2, 13, 23))),
  list(name = "N30k5", N = 30, ties = FALSE, sets = list(c(1, 2, 3, 4, 14), c(1, 2, 15, 29, 30), c(3, 9, 26, 28, 30), c(5, 11, 17, 21, 25))),
  list(name = "N32k4t", N = 32, ties = TRUE, sets = list(c(1, 2, 5, 9), c(14, 15, 16, 17), c(25, 28, 30, 31), c(3, 12, 20, 29)))
)
REP <- 20
out <- list(version = as.character(packageVersion("fgsea")), designs = list())
for (dz in designs) {
    set.seed(100 + dz$N)
    st <- sort(rnorm(dz$N), decreasing = TRUE)
    if (dz$ties) { st <- round(st * 2) / 2 }        # ties, including a block of exact zeros
    names(st) <- sprintf("g%02d", seq_len(dz$N))
    rec <- list(stats = as.list(st), sets = list())
    for (ix in dz$sets) {
        pw <- list(S = names(st)[ix]); key <- paste(ix, collapse = "_")
        r <- list(members = ix - 1)
        for (typ in c("std", "pos", "neg")) {
            ml <- t(sapply(seq_len(REP), function(i) { set.seed(i)
                x <- suppressWarnings(fgseaMultilevel(pw, st, minSize = 1, maxSize = dz$N - 1, eps = 0, scoreType = typ, BPPARAM = SerialParam()))
                c(x$pval, x$NES, x$ES) }))
            set.seed(1)
            s <- suppressWarnings(fgseaSimple(pw, st, nperm = 2e5, minSize = 1, maxSize = dz$N - 1, scoreType = typ, BPPARAM = SerialParam()))
            r[[typ]] <- list(ES = ml[1, 3], ml_p = ml[, 1], ml_nes = ml[, 2], simple_p = s$pval, simple_nes = s$NES)
        }
        rec$sets[[key]] <- r
        cat(label, dz$name, key, "std p", signif(median(r$std$ml_p), 4), "\n")
    }
    out$designs[[dz$name]] <- rec
}
write_json(out, file.path(d, paste0("v2_", label, ".json")), digits = NA, auto_unbox = FALSE)
