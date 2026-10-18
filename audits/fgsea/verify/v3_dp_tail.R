## Runs fgseaMultilevel (eps = 0, defaults otherwise) REPS times per planted set of v3_spec.json,
## with scoreType "pos" (unconditional tail) and "std" (default), and writes p-values and log2err.
## Usage: R_LIBS=<fgsea lib>:<deps lib> Rscript v3_dp_tail.R <dir> <label> [reps]
args <- commandArgs(TRUE); d <- args[1]; label <- args[2]; REPS <- if (length(args) > 2) as.integer(args[3]) else 20
suppressPackageStartupMessages({library(fgsea); library(jsonlite); library(BiocParallel)})
spec <- fromJSON(file.path(d, "v3_spec.json"), simplifyVector = FALSE)
stats <- setNames(unlist(spec$stats), unlist(spec$names))
out <- list(version = as.character(packageVersion("fgsea")), reps = REPS, sets = list())
for (st in spec$sets) {
    pw <- list(P = names(stats)[unlist(st$pos) + 1])
    rec <- list()
    for (typ in c("pos", "std")) {
        if (typ == "pos" && !is.null(st$p_neg_exact)) next
        pv <- le <- numeric(REPS); es <- NA
        for (r in seq_len(REPS)) {
            set.seed(1000 + r)
            res <- suppressWarnings(fgseaMultilevel(pw, stats, eps = 0, scoreType = typ, BPPARAM = SerialParam()))
            pv[r] <- res$pval; le[r] <- res$log2err; es <- res$ES
        }
        rec[[typ]] <- list(pval = pv, log2err = le)
        rec$ES <- es
    }
    out$sets[[st$name]] <- rec
    cat(label, st$name, "ES", rec$ES, "median p(std)", median(rec$std$pval), "\n")
}
write_json(out, file.path(d, paste0("v3_", label, ".json")), digits = NA, auto_unbox = TRUE)
