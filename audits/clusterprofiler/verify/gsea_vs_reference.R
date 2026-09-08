## GSEA core on one synthetic ranked list with known truth, run through every engine that
## computes published GSEA numbers for clusterProfiler users:
##   fgsea::fgseaMultilevel / fgseaSimple           (fgsea master; also the engine of clusterProfiler <= 4.18)
##   enrichit::gsea  method = multilevel | sample | permute   (engine of clusterProfiler >= 4.19.3)
##   DOSE:::GSEA_internal by = "fgsea" | "DOSE"    (legacy DOSE 3.30.0, if lib-legacy is on R_LIBS_USER)
##   clusterProfiler::GSEA(TERM2GENE)                (devel HEAD, if installed)
## Everything is dumped as TSV; gsea_vs_reference.py recomputes ES, leading edge, rank,
## tags/list/signal and set sizes from Subramanian et al. 2005 and compares.
## Usage: R_LIBS_USER=<lib-legacy>:<lib> Rscript gsea_vs_reference.R <outdir>
args <- commandArgs(TRUE); outdir <- if (length(args)) args[1] else tempdir()
dir.create(outdir, showWarnings = FALSE, recursive = TRUE)
suppressPackageStartupMessages({library(fgsea); library(enrichit); library(jsonlite)})
cat("fgsea", as.character(packageVersion("fgsea")), " enrichit", as.character(packageVersion("enrichit")), "\n")
set.seed(1)
N <- 2000
stats <- rnorm(N)
names(stats) <- sprintf("g%04d", 1:N)
## planted signal: genes 1..60 shifted up, 61..100 shifted down
stats[1:60] <- stats[1:60] + 2.5; stats[61:100] <- stats[61:100] - 2.5
stats <- sort(stats, decreasing = TRUE)
genes <- names(stats)
sets <- list()
set.seed(2)
for (i in 1:30) sets[[sprintf("R%02d", i)]] <- sample(genes, sample(10:300, 1))          # random
sets$UP1   <- c(sprintf("g%04d", 1:40),  sample(genes, 30))                               # enriched at top
sets$DOWN1 <- c(sprintf("g%04d", 61:95), sample(genes, 25))                               # enriched at bottom
sets$ABSENT <- c(sample(genes, 12), sprintf("zz%02d", 1:8))                               # 8 genes not in the list
sets$DUP    <- rep(sample(genes, 15), 2)                                                  # duplicated members
sets$SMALL  <- sample(genes, 6)                                                           # below minGSSize 10
sets$BIG    <- sample(genes, 600)                                                         # above maxGSSize 500
sets <- lapply(sets, function(s) unique(s))  # fgsea documents that duplicates are removed; keep DUP explicit below
sets$DUP <- rep(sets$DUP, 2)
write_json(list(stats = as.list(stats), sets = sets), file.path(outdir, "design.json"), digits = NA)

dump <- function(df, name) write.table(df, file.path(outdir, paste0(name, ".tsv")), sep = "\t", quote = FALSE, row.names = FALSE)
as_chr <- function(l) vapply(l, paste, character(1), collapse = "/")

## ---- fgsea ---------------------------------------------------------------------------------
set.seed(11)
fm <- fgseaMultilevel(sets, stats, minSize = 10, maxSize = 500, eps = 0)
fm$leadingEdge <- as_chr(fm$leadingEdge); dump(as.data.frame(fm), "fgsea_multilevel")
set.seed(12)
fs <- fgseaSimple(sets, stats, nperm = 20000, minSize = 10, maxSize = 500)
fs$leadingEdge <- as_chr(fs$leadingEdge); dump(as.data.frame(fs), "fgsea_simple")
for (gp in c(0, 2)) {
    set.seed(13)
    f <- fgseaSimple(sets, stats, nperm = 2000, minSize = 10, maxSize = 500, gseaParam = gp)
    f$leadingEdge <- as_chr(f$leadingEdge); dump(as.data.frame(f), sprintf("fgsea_simple_p%d", gp))
}
set.seed(14); fpos <- fgseaMultilevel(sets, stats, minSize = 10, maxSize = 500, eps = 0, scoreType = "pos")
fpos$leadingEdge <- as_chr(fpos$leadingEdge); dump(as.data.frame(fpos), "fgsea_multilevel_pos")
cat(sprintf("fgsea: multilevel rows=%d simple rows=%d\n", nrow(fm), nrow(fs)))

## ---- enrichit ------------------------------------------------------------------------------
em <- suppressWarnings(enrichit::gsea(stats, sets, minGSSize = 10, maxGSSize = 500, method = "multilevel", seed = 21, eps = 0, verbose = FALSE))
dump(em, "enrichit_multilevel")
es <- suppressWarnings(enrichit::gsea(stats, sets, minGSSize = 10, maxGSSize = 500, method = "sample", nPerm = 20000, seed = 22, verbose = FALSE))
dump(es, "enrichit_sample")
ep <- suppressWarnings(enrichit::gsea(stats, sets, minGSSize = 10, maxGSSize = 500, method = "permute", nPerm = 2000, seed = 23, verbose = FALSE))
dump(ep, "enrichit_permute")
for (ex in c(0, 2)) {
    e <- suppressWarnings(enrichit::gsea(stats, sets, minGSSize = 10, maxGSSize = 500, method = "sample", nPerm = 2000, exponent = ex, seed = 24, verbose = FALSE))
    dump(e, sprintf("enrichit_sample_p%d", ex))
    e <- suppressWarnings(enrichit::gsea(stats, sets, minGSSize = 10, maxGSSize = 500, method = "multilevel", exponent = ex, seed = 24, eps = 0, verbose = FALSE))
    dump(e, sprintf("enrichit_multilevel_p%d", ex))
}
epos <- suppressWarnings(enrichit::gsea(stats, sets, minGSSize = 10, maxGSSize = 500, method = "multilevel", seed = 25, eps = 0, scoreType = "pos", verbose = FALSE))
dump(epos, "enrichit_multilevel_pos")
cat(sprintf("enrichit: multilevel rows=%d sample rows=%d permute rows=%d\n", nrow(em), nrow(es), nrow(ep)))

## seeds: FALSE draws from R's RNG; numeric seed fixes; set.seed() before the call also fixes
a1 <- suppressWarnings(enrichit::gsea(stats, sets["UP1"], method = "multilevel", eps = 0, verbose = FALSE))
a2 <- suppressWarnings(enrichit::gsea(stats, sets["UP1"], method = "multilevel", eps = 0, verbose = FALSE))
b1 <- suppressWarnings(enrichit::gsea(stats, sets["UP1"], method = "multilevel", eps = 0, seed = 7, verbose = FALSE))
b2 <- suppressWarnings(enrichit::gsea(stats, sets["UP1"], method = "multilevel", eps = 0, seed = 7, verbose = FALSE))
set.seed(3); c1 <- suppressWarnings(enrichit::gsea(stats, sets["UP1"], method = "multilevel", eps = 0, verbose = FALSE))
set.seed(3); c2 <- suppressWarnings(enrichit::gsea(stats, sets["UP1"], method = "multilevel", eps = 0, verbose = FALSE))
cat(sprintf("enrichit seed: seed=FALSE twice identical p: %s (%.3e vs %.3e); seed=7 twice: %s; set.seed(3)+FALSE twice: %s\n",
            identical(a1$pvalue, a2$pvalue), a1$pvalue, a2$pvalue, identical(b1$pvalue, b2$pvalue), identical(c1$pvalue, c2$pvalue)))

## ties: two ways of ordering the same tied block must give the ES of the input order
st <- stats; st[c("g0005", "g0006", "g0007")] <- st["g0005"]   # a 3-way tie near the top
tie_set <- list(T = c("g0005", "g0006", "g0007", sample(genes[200:2000], 20)))
w <- NULL
r1 <- withCallingHandlers(fgseaSimple(tie_set, st, nperm = 10, minSize = 1), warning = function(x) { w <<- c(w, conditionMessage(x)); invokeRestart("muffleWarning") })
r2 <- withCallingHandlers(enrichit::gsea(st, tie_set, minGSSize = 1, method = "sample", nPerm = 10, verbose = FALSE), warning = function(x) { w <<- c(w, conditionMessage(x)); invokeRestart("muffleWarning") })
cat(sprintf("ties: fgsea ES=%.6f enrichit ES=%.6f; warnings issued: %d (%s)\n", r1$ES, r2$enrichmentScore, length(w), paste(substr(unique(w), 1, 40), collapse = " | ")))
write_json(list(stats = as.list(st), set = tie_set$T, fgsea_ES = r1$ES, enrichit_ES = r2$enrichmentScore), file.path(outdir, "ties.json"), digits = NA)

## ---- legacy DOSE 3.30.0 (fgsea backend and its own permutation backend) --------------------
if (requireNamespace("DOSE", quietly = TRUE) && packageVersion("DOSE") < "4.0.0") {
    cat("DOSE", as.character(packageVersion("DOSE")), "\n")
    gs <- gson::gson(gsid2gene = data.frame(gsid = rep(names(sets), lengths(sets)), gene = unlist(sets)),
                     gsid2name = data.frame(gsid = names(sets), name = names(sets)),
                     species = "s", gsname = "s", version = "0", accessed_date = "2026-09-08", keytype = "k")
    GI <- get("GSEA_internal", envir = asNamespace("DOSE"))
    set.seed(31)
    d1 <- GI(geneList = stats, exponent = 1, minGSSize = 10, maxGSSize = 500, eps = 0, pvalueCutoff = 1,
             pAdjustMethod = "BH", verbose = FALSE, USER_DATA = gs, by = "fgsea")
    dump(d1@result, "dose_fgsea")
    set.seed(32)
    d2 <- GI(geneList = stats, exponent = 1, minGSSize = 10, maxGSSize = 500, eps = 0, pvalueCutoff = 1,
             pAdjustMethod = "BH", verbose = FALSE, USER_DATA = gs, by = "DOSE", nPerm = 2000)
    dump(d2@result, "dose_perm")
    cat(sprintf("DOSE: by=fgsea rows=%d by=DOSE rows=%d\n", nrow(d1@result), nrow(d2@result)))
}
## ---- clusterProfiler devel wrapper --------------------------------------------------------
if (requireNamespace("clusterProfiler", quietly = TRUE) && packageVersion("clusterProfiler") >= "4.19.3") {
    suppressPackageStartupMessages(library(clusterProfiler))
    cat("clusterProfiler", as.character(packageVersion("clusterProfiler")), "\n")
    t2g <- data.frame(term = rep(names(sets), lengths(sets)), gene = unlist(sets))
    cp <- suppressWarnings(GSEA(stats, TERM2GENE = t2g, pvalueCutoff = 1, eps = 0, seed = 21, verbose = FALSE))
    dump(cp@result, "clusterProfiler_GSEA")
    cat(sprintf("clusterProfiler::GSEA rows=%d; identical to enrichit multilevel (same seed): ES %s, pvalue %s\n",
                nrow(cp@result), isTRUE(all.equal(cp@result[em$ID, "enrichmentScore"], em$enrichmentScore)),
                isTRUE(all.equal(cp@result[em$ID, "pvalue"], em$pvalue))))
}
cat("done\n")
