## ES, size and leadingEdge from fgseaMultilevel on a realistic ranked list, for comparison with
## the reference (_ref.py) in v1_es_leading_edge.py.  Lists: (a) t-like statistics, distinct;
## (b) the same rounded to 2 decimals (ties) with 5 % exact zeros; gseaParam 1 and 0 and 2;
## scoreType std / pos / neg.  p-values are not looked at here.
## Usage: R_LIBS=<fgsea lib>:<deps lib> Rscript v1_es_leading_edge.R <outdir> <label>
args <- commandArgs(TRUE); d <- args[1]; label <- args[2]
suppressPackageStartupMessages({library(fgsea); library(jsonlite); library(BiocParallel)})
set.seed(7)
n <- 5000
genes <- sprintf("G%05d", seq_len(n))
a <- setNames(rt(n, df = 4) * 1.3, genes)
b <- round(a, 2); b[sample(n, 250)] <- 0
lists <- list(a = a, b = b)
## 300 gene sets: 240 random (sizes 15-500, with 10 % of members absent from the list and some
## duplicated members) and 60 shifted towards either end so that ES is far from 0
rk <- names(sort(a, decreasing = TRUE))
pw <- list()
for (i in 1:300) {
    k <- sample(c(15:60, 61:200, 201:500), 1)
    if (i <= 240) mem <- sample(genes, k) else {
        top <- i %% 2 == 0
        pool <- if (top) rk[1:1500] else rk[3501:5000]
        mem <- c(sample(pool, round(k * 0.6)), sample(genes, k - round(k * 0.6)))
    }
    mem <- c(mem, sprintf("ABSENT%d_%d", i, seq_len(ceiling(k / 10))), mem[1:2])
    pw[[sprintf("S%03d", i)]] <- mem
}
out <- list(version = as.character(packageVersion("fgsea")), lists = lapply(lists, as.list), pathways = pw, runs = list())
for (ln in names(lists)) for (gp in c(1, 0, 2)) for (stype in c("std", "pos", "neg")) {
    if (gp != 1 && stype != "std") next
    set.seed(1)
    r <- suppressWarnings(fgseaMultilevel(pw, lists[[ln]], minSize = 15, maxSize = 500, gseaParam = gp,
                                          scoreType = stype, nPermSimple = 200, BPPARAM = SerialParam()))
    key <- sprintf("%s_g%g_%s", ln, gp, stype)
    out$runs[[key]] <- list(list = ln, gseaParam = gp, scoreType = stype, pathway = r$pathway, ES = r$ES,
                            size = r$size, leadingEdge = lapply(r$leadingEdge, as.character))
    cat(label, key, nrow(r), "pathways\n")
}
write_json(out, file.path(d, paste0("v1_", label, ".json")), digits = NA, auto_unbox = TRUE)
