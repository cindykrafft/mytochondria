## GSEA p-values against an exact enumeration of the gene-set permutation null on tiny lists.
## For each (N, k) design and each hand-picked gene set the engines report ES and p; the Python
## side enumerates all C(N, k) subsets and computes P(ES* >= ES | ES* >= 0) (the GSEA convention,
## which fgsea and DOSE document) and the unconditional P(ES* >= ES).
## Usage: R_LIBS_USER=<lib-legacy>:<lib> Rscript gsea_exact_small.R <outdir>
args <- commandArgs(TRUE); outdir <- if (length(args)) args[1] else tempdir()
dir.create(outdir, showWarnings = FALSE, recursive = TRUE)
suppressPackageStartupMessages({library(fgsea); library(enrichit); library(jsonlite)})
cat("fgsea", as.character(packageVersion("fgsea")), " enrichit", as.character(packageVersion("enrichit")), "\n")
has_dose <- requireNamespace("DOSE", quietly = TRUE) && packageVersion("DOSE") < "4.0.0"
if (has_dose) cat("DOSE", as.character(packageVersion("DOSE")), "\n")

designs <- list(
    list(name = "N24k3", N = 24, sets = list(top = 1:3, top_mid = c(1, 2, 12), mid = c(8, 12, 16), bottom = 22:24, mixed = c(2, 13, 23))),
    list(name = "N40k4", N = 40, sets = list(top = 1:4, top2 = c(1, 2, 3, 9), mid = c(15, 18, 22, 27), bottom = 37:40, mixed = c(1, 2, 39, 40))),
    list(name = "N30k5", N = 30, sets = list(top = 1:5, top2 = c(1, 2, 3, 4, 14), bottom = 26:30, mixed = c(1, 2, 15, 29, 30)))
)
REP <- 40
res <- list()
for (dz in designs) {
    set.seed(100 + dz$N)
    stats <- sort(rnorm(dz$N), decreasing = TRUE); names(stats) <- sprintf("g%02d", seq_len(dz$N))
    write_json(list(stats = as.list(stats)), file.path(outdir, paste0(dz$name, "_stats.json")), digits = NA)
    gsets <- lapply(dz$sets, function(ix) names(stats)[ix])
    k <- length(gsets[[1]])
    if (has_dose) {
        ## legacy DOSE::geneSet_filter() uses sapply(), which turns equal-sized sets into a matrix and then
        ## fails ("arguments imply differing number of rows"); pad the GSON with one set of another size
        gpad <- c(gsets, list(PAD = names(stats)[seq_len(k + 2)]))
        gs <- gson::gson(gsid2gene = data.frame(gsid = rep(names(gpad), lengths(gpad)), gene = unlist(gpad)),
                         gsid2name = data.frame(gsid = names(gpad), name = names(gpad)),
                         species = "s", gsname = "s", version = "0", accessed_date = "2026-09-08", keytype = "k")
        GI <- get("GSEA_internal", envir = asNamespace("DOSE"))
    }
    for (sn in names(gsets)) {
        one <- gsets[sn]
        set.seed(1); fs <- fgseaSimple(one, stats, nperm = 1e5, minSize = 1, maxSize = dz$N - 1, BPPARAM = BiocParallel::SerialParam())
        fml <- replicate(REP, { fgseaMultilevel(one, stats, minSize = 1, maxSize = dz$N - 1, eps = 0, BPPARAM = BiocParallel::SerialParam())$pval })
        eml <- replicate(REP, suppressWarnings(enrichit::gsea(stats, one, minGSSize = 1, maxGSSize = dz$N - 1, method = "multilevel", eps = 0, verbose = FALSE))$pvalue)
        esa <- suppressWarnings(enrichit::gsea(stats, one, minGSSize = 1, maxGSSize = dz$N - 1, method = "sample", nPerm = 2e5, seed = 5, verbose = FALSE))
        epe <- suppressWarnings(enrichit::gsea(stats, one, minGSSize = 1, maxGSSize = dz$N - 1, method = "permute", nPerm = 5e4, seed = 6, verbose = FALSE))
        ead <- suppressWarnings(enrichit::gsea(stats, one, minGSSize = 1, maxGSSize = dz$N - 1, method = "sample", adaptive = TRUE, minPerm = 1000, maxPerm = 2e5, seed = 7, verbose = FALSE))
        row <- list(design = dz$name, set = sn, N = dz$N, k = k, members = paste(one[[1]], collapse = "/"),
                    fgsea_ES = fs$ES, fgsea_simple_p = fs$pval, fgsea_nMoreExtreme = fs$nMoreExtreme, fgsea_NES = fs$NES,
                    fgsea_ml_p_mean = mean(fml), fgsea_ml_p_sd = sd(fml),
                    enrichit_ES = esa$enrichmentScore, enrichit_sample_p = esa$pvalue, enrichit_sample_NES = esa$NES,
                    enrichit_permute_p = epe$pvalue, enrichit_adaptive_p = ead$pvalue, enrichit_adaptive_nPerm = ead$nPerm,
                    enrichit_ml_p_mean = mean(eml), enrichit_ml_p_sd = sd(eml))
        if (has_dose) {
            set.seed(9)
            dd <- GI(geneList = stats, exponent = 1, minGSSize = 1, maxGSSize = dz$N - 1, eps = 0, pvalueCutoff = 1,
                     pAdjustMethod = "BH", verbose = FALSE, USER_DATA = gs, by = "DOSE", nPerm = 1e4)
            r <- dd@result; row$dose_perm_p <- r[sn, "pvalue"]; row$dose_perm_NES <- r[sn, "NES"]
        }
        res[[length(res) + 1]] <- as.data.frame(row)
        cat(sprintf("%s %-8s ES=%+.4f fgseaSimple p=%.4g  fgseaML %.4g±%.2g  enrichit sample %.4g  permute %.4g  adaptive %.4g (n=%d)  enrichit ML %.4g±%.2g%s\n",
                    dz$name, sn, fs$ES, fs$pval, mean(fml), sd(fml), esa$pvalue, epe$pvalue, ead$pvalue, ead$nPerm, mean(eml), sd(eml),
                    if (has_dose) sprintf("  DOSE perm %.4g", row$dose_perm_p) else ""))
    }
}
out <- do.call(rbind, res)
write.table(out, file.path(outdir, "engines.tsv"), sep = "\t", quote = FALSE, row.names = FALSE)
cat("done\n")
