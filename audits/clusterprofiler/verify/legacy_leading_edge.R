## Legacy leading edge for negative enrichment scores (DOSE <= 3.30 leading_edge(), the code behind
## clusterProfiler <= 4.18 GSEA()/gseGO()/gseKEGG() core_enrichment, rank, leading_edge columns).
## DOSE picks the hit with the lowest running score *after* the hit; GSEA (Subramanian 2005, GSEA
## user guide) defines the leading edge of a negative-ES set as the members at or after the minimum
## of the running sum, which is always reached just *before* a hit. The two rules differ whenever an
## earlier hit's post-hit score undercuts the post-hit score following the global minimum.
## Usage: R_LIBS_USER=<lib-legacy>:<lib> Rscript legacy_leading_edge.R
suppressPackageStartupMessages({library(DOSE); library(clusterProfiler)})
cat("DOSE", as.character(packageVersion("DOSE")), " clusterProfiler", as.character(packageVersion("clusterProfiler")), "\n")
gseaScores <- get("gseaScores", envir = asNamespace("DOSE"))
leading_edge <- get("leading_edge", envir = asNamespace("DOSE"))

## reference rule (independent of DOSE's code): running sum from the definition, peak = global extreme
ref_ledge <- function(geneList, geneSet, exponent = 1) {
    hits <- names(geneList) %in% geneSet
    N <- length(geneList); Nh <- sum(hits)
    w <- abs(geneList)^exponent
    rs <- cumsum(ifelse(hits, w, 0)) / sum(w[hits]) - cumsum(!hits) / (N - Nh)
    imax <- which.max(rs); imin <- which.min(rs)
    if (abs(rs[imax]) >= abs(rs[imin])) list(ES = rs[imax], genes = names(geneList)[hits & seq_len(N) <= imax], rank = imax)
    else list(ES = rs[imin], genes = names(geneList)[hits & seq_len(N) >= imin], rank = N - imin + 1)
}

set.seed(4)
N <- 15000
geneList <- sort(setNames(rnorm(N), sprintf("g%05d", 1:N)), decreasing = TRUE)
genes <- names(geneList)
## 300 random sets and 300 sets planted towards the bottom (negative ES), sizes 15..500
sets <- list()
for (i in 1:300) sets[[sprintf("R%03d", i)]] <- sample(genes, sample(15:500, 1))
for (i in 1:300) { n <- sample(15:500, 1); sets[[sprintf("D%03d", i)]] <- c(sample(genes[(N - 3000):N], round(n * 0.4)), sample(genes, n - round(n * 0.4))) }
sets <- lapply(sets, unique)

obs <- lapply(sets, function(gs) gseaScores(geneSet = gs, geneList = geneList, exponent = 1))
led <- leading_edge(obs)
tab <- do.call(rbind, lapply(names(sets), function(id) {
    r <- ref_ledge(geneList, sets[[id]])
    dose <- led$core_enrichment[[id]]
    data.frame(id = id, ES = obs[[id]]$ES, size = length(intersect(sets[[id]], genes)),
               n_ref = length(r$genes), n_dose = length(dose),
               same = setequal(dose, r$genes), extra = length(setdiff(dose, r$genes)), missing = length(setdiff(r$genes, dose)),
               rank_dose = led$rank[[id]], rank_ref = r$rank, stringsAsFactors = FALSE)
}))
neg <- tab[tab$ES < 0, ]; pos <- tab[tab$ES >= 0, ]
cat(sprintf("positive-ES sets: %d, leading edge == reference: %d\n", nrow(pos), sum(pos$same)))
cat(sprintf("negative-ES sets: %d, leading edge == reference: %d (%.1f%% differ)\n", nrow(neg), sum(neg$same), 100 * mean(!neg$same)))
d <- neg[!neg$same, ]
cat(sprintf("  among the differing negative sets: DOSE lists %d..%d extra genes (median %.0f), misses %d..%d; reference size %d..%d\n",
            min(d$extra), max(d$extra), median(d$extra), min(d$missing), max(d$missing), min(d$n_ref), max(d$n_ref)))
cat(sprintf("  extra genes as a fraction of the reference leading edge: median %.0f%%, max %.0f%%\n", 100 * median(d$extra / d$n_ref), 100 * max(d$extra / d$n_ref)))
cat(sprintf("  planted (down) sets differing: %d of %d; random negative sets differing: %d of %d\n",
            sum(!neg$same & grepl("^D", neg$id)), sum(grepl("^D", neg$id)), sum(!neg$same & grepl("^R", neg$id)), sum(grepl("^R", neg$id))))
cat(sprintf("  rank column == reference for all sets: %s\n", all(tab$rank_dose == tab$rank_ref)))
## the wrapper path on one differing set: clusterProfiler 4.12.0 GSEA() -> DOSE::GSEA_internal -> leading_edge()
id <- d$id[which.max(d$extra)]
t2g <- data.frame(term = id, gene = sets[[id]])
set.seed(5)
x <- suppressWarnings(GSEA(geneList, TERM2GENE = t2g, minGSSize = 10, maxGSSize = 500, pvalueCutoff = 1, eps = 0, verbose = FALSE))
ce <- strsplit(x@result[id, "core_enrichment"], "/")[[1]]
r <- ref_ledge(geneList, sets[[id]])
cat(sprintf("  clusterProfiler 4.12.0 GSEA() on %s: ES=%.4f NES=%.3f; core_enrichment has %d genes, reference leading edge %d, extra %d; leading_edge='%s'\n",
            id, x@result[id, "enrichmentScore"], x@result[id, "NES"], length(ce), length(r$genes), length(setdiff(ce, r$genes)), x@result[id, "leading_edge"]))
## and the master engine on the same set (enrichit, via a fresh R process to avoid the S3 clash)
writeLines(c(sprintf("suppressPackageStartupMessages(library(enrichit))"),
             "gl <- readRDS(commandArgs(TRUE)[1]); gs <- readRDS(commandArgs(TRUE)[2])",
             "e <- suppressWarnings(enrichit::gsea(gl, gs, minGSSize = 10, maxGSSize = 500, method = 'multilevel', seed = 1, eps = 0, verbose = FALSE))",
             "cat(sprintf('  enrichit %s on the same set: core_enrichment has %d genes\\n', as.character(packageVersion('enrichit')), length(strsplit(e$core_enrichment, '/')[[1]])))"),
           f <- tempfile(fileext = ".R"))
saveRDS(geneList, g1 <- tempfile()); saveRDS(sets[id], g2 <- tempfile())
system2("Rscript", c(f, g1, g2), env = paste0("R_LIBS_USER=", strsplit(Sys.getenv("R_LIBS_USER"), ":")[[1]][2]))
## the sapply() simplification in DOSE::geneSet_filter (by = "DOSE" path): equal-sized sets become a matrix
gf <- get("geneSet_filter", envir = asNamespace("DOSE"))
eq <- list(A = genes[1:20], B = genes[101:120])
cat(sprintf("  DOSE::geneSet_filter on two equal-sized sets returns class '%s' (list expected); length %d\n", class(gf(eq, geneList, 10, 500))[1], length(gf(eq, geneList, 10, 500))))
