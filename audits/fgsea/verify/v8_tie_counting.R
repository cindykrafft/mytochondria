## fgseaSimple counts permutation ES <= ES (or >=) with floating-point comparisons
## (R/fgsea.R:640-641 single pathway, src/fastGSEA.cpp:410-416 batch).  Gene sets whose running-sum
## extreme lies at the first hit (ES = -(S1 - 1)/(N - k)) or at the last hit
## (ES = 1 - (Sk - k)/(N - k)) share that ES exactly with every set having the same S1 (Sk), but
## calcGseaStat() computes it as (c/NR - a) - c/NR, which differs from -a in the last bit
## depending on c/NR.  This script writes, for every k-subset of a short list, fgsea's own ES
## (calcGseaStat on prepareStats() weights) so v8_tie_counting.py can count with exact integers;
## then it runs fgseaSimple on the observed sets, alone (R path) and with a companion set (C++ path).
## Usage: R_LIBS=<fgsea lib>:<deps lib> Rscript v8_tie_counting.R <dir> <label>
args <- commandArgs(TRUE); d <- args[1]; label <- args[2]
suppressPackageStartupMessages({library(fgsea); library(jsonlite); library(BiocParallel)})
designs <- list(list(name = "N24k3", N = 24, k = 3, seed = 124, obs = list(c(20, 22, 23), c(1, 2, 12), c(19, 21, 24))),
                list(name = "N60k4", N = 60, k = 4, seed = 160, obs = list(c(40, 50, 55, 58), c(30, 45, 52, 60), c(2, 5, 9, 20))))
out <- list(version = as.character(packageVersion("fgsea")), designs = list())
for (dz in designs) {
    set.seed(dz$seed); st <- sort(rnorm(dz$N), decreasing = TRUE); names(st) <- sprintf("g%02d", seq_len(dz$N))
    w <- suppressWarnings(fgsea:::prepareStats(st))            # fgsea's own (integer) weights
    cmb <- combn(dz$N, dz$k)
    es <- apply(cmb, 2, function(s) calcGseaStat(w, s))
    obs <- list()
    for (o in dz$obs) {
        pw <- list(S = names(st)[o]); key <- paste(o, collapse = "_")
        set.seed(1); a <- fgseaSimple(pw, st, nperm = 1e6, minSize = 1, maxSize = dz$N - 1, BPPARAM = SerialParam())
        ## companion set of another size so that the batch (C++) path is used
        pw2 <- c(pw, list(C = names(st)[seq(1, dz$N, by = 3)]))
        set.seed(1); b <- fgseaSimple(pw2, st, nperm = 1e6, minSize = 1, maxSize = dz$N - 1, BPPARAM = SerialParam())
        set.seed(1); m <- suppressWarnings(fgseaMultilevel(pw, st, minSize = 1, maxSize = dz$N - 1, eps = 0, BPPARAM = SerialParam()))
        obs[[key]] <- list(members = o, ES = sprintf("%.17g", a$ES), simple_R_p = a$pval, simple_Cpp_p = b[pathway == "S"]$pval, multilevel_p = m$pval)
        cat(label, dz$name, key, "ES", a$ES, "simple(R)", a$pval, "simple(C++)", b[pathway == "S"]$pval, "multilevel", m$pval, "\n")
    }
    out$designs[[dz$name]] <- list(N = dz$N, k = dz$k, w = as.numeric(w), es = sprintf("%.17g", es), obs = obs)
}
write_json(out, file.path(d, paste0("v8_", label, ".json")), digits = NA, auto_unbox = TRUE)
