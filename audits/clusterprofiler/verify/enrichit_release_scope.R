## Version scope of the enrichit engine behaviours that changed after the Bioconductor 3.23 release
## of clusterProfiler 4.20.0 (2026-04-28). Run once per enrichit version by putting that version's
## library first on R_LIBS_USER (CRAN 0.1.4 = what a May-2026 install got, 0.2.0 = July, 0.2.1 =
## August; 0.2.2 = GitHub master, not on CRAN as of the cran/enrichit mirror on 2026-08-04).
## Same synthetic ORA design as ora_vs_scipy.R and the same ranked list as gsea_vs_reference.R.
## Usage: R_LIBS_USER=<lib-enrichit-x.y.z>:<lib> Rscript enrichit_release_scope.R
suppressPackageStartupMessages({library(enrichit); library(gson)})
v <- as.character(packageVersion("enrichit"))
cat(sprintf("== enrichit %s\n", v))

## ---- ORA design (identical to ora_vs_scipy.R) ---------------------------------------------
set.seed(20260908)
genes <- sprintf("g%05d", 1:3000)
sizes <- pmax(3L, as.integer(round(exp(runif(400, log(3), log(700))))))
term2gene <- do.call(rbind, lapply(seq_along(sizes), function(i)
    data.frame(term = sprintf("T%03d", i), gene = sample(genes, sizes[i]), stringsAsFactors = FALSE)))
term2gene <- unique(term2gene)
t10 <- unique(term2gene$gene[term2gene$term == "T010"])
query <- unique(c(sample(t10, min(60, length(t10))), sample(genes, 140), sprintf("x%03d", 1:30)))
universe_user <- unique(c(sample(genes, 2000), sprintf("u%03d", 1:500)))
gs <- gson::gson(gsid2gene = setNames(term2gene, c("gsid", "gene")),
                 gsid2name = data.frame(gsid = unique(term2gene$term), name = unique(term2gene$term)),
                 species = "synthetic", gsname = "synthetic", version = "0", accessed_date = "2026-09-08", keytype = "symbol")
x <- enrichit::ora_gson(gene = query, pvalueCutoff = 0.05, pAdjustMethod = "BH", universe = NULL,
                        minGSSize = 10, maxGSSize = 500, qvalueCutoff = 0.2, gson = gs)
r <- x@result
cat(sprintf("ORA: rows in @result = %d (with Count = 0: %d); BH denominator implied = %d; T010 p = %.3e p.adjust = %.3e; rows shown by as.data.frame (p<=0.05 & p.adjust<=0.05 & q<=0.2) = %d\n",
            nrow(r), sum(r$Count == 0), nrow(r), r["T010", "pvalue"], r["T010", "p.adjust"], nrow(as.data.frame(x))))

## ---- GSEA design (identical to gsea_vs_reference.R) ----------------------------------------
set.seed(1)
N <- 2000; stats <- rnorm(N); names(stats) <- sprintf("g%04d", 1:N)
stats[1:60] <- stats[1:60] + 2.5; stats[61:100] <- stats[61:100] - 2.5
stats <- sort(stats, decreasing = TRUE); gl <- names(stats)
sets <- list(); set.seed(2)
for (i in 1:30) sets[[sprintf("R%02d", i)]] <- sample(gl, sample(10:300, 1))
sets$UP1 <- c(sprintf("g%04d", 1:40), sample(gl, 30)); sets$DOWN1 <- c(sprintf("g%04d", 61:95), sample(gl, 25))
sets$ABSENT <- c(sample(gl, 12), sprintf("zz%02d", 1:8)); sets$DUP <- rep(sample(gl, 15), 2)
sets$SMALL <- sample(gl, 6); sets$BIG <- sample(gl, 600)
sets <- lapply(sets, unique); sets$DUP <- rep(sets$DUP, 2)
## extra sets that separate "raw size" from "overlap size": 480 present + 40 absent genes (raw 520, overlap 480);
## 6 present + 10 absent (raw 16, overlap 6)
sets$RAW520_OV480 <- c(sample(gl, 480), sprintf("zz%03d", 1:40))
sets$RAW16_OV6    <- c(sample(gl, 6), sprintf("zz%03d", 101:110))
gs2 <- gson::gson(gsid2gene = data.frame(gsid = rep(names(sets), lengths(sets)), gene = unlist(sets)),
                  gsid2name = data.frame(gsid = names(sets), name = names(sets)),
                  species = "s", gsname = "s", version = "0", accessed_date = "2026-09-08", keytype = "k")
args <- list(geneList = stats, gson = gs2, minGSSize = 10, maxGSSize = 500, pvalueCutoff = 0.05, pAdjustMethod = "BH", verbose = FALSE, eps = 0)
if ("seed" %in% names(formals(enrichit::gsea_gson))) args$seed <- 21 else args$seed <- 21   # 0.1.x: reaches gsea() through ...
g <- suppressWarnings(do.call(enrichit::gsea_gson, args))
res <- g@result
cat(sprintf("GSEA: sets in result = %d; tested SMALL(6) %s BIG(600) %s RAW520_OV480 %s RAW16_OV6 %s; rows with p.adjust > 0.05 in the result table = %d of %d (max p.adjust %.3f)\n",
            nrow(res), "SMALL" %in% res$ID, "BIG" %in% res$ID, "RAW520_OV480" %in% res$ID, "RAW16_OV6" %in% res$ID,
            sum(res$p.adjust > 0.05), nrow(res), max(res$p.adjust)))
cat(sprintf("      UP1 NES=%.3f p=%.3e; DOWN1 NES=%.3f p=%.3e; R01 p=%.3f (if present)\n",
            res["UP1", "NES"], res["UP1", "pvalue"], res["DOWN1", "NES"], res["DOWN1", "pvalue"], if ("R01" %in% res$ID) res["R01", "pvalue"] else NA))
## the unfiltered engine table, to see what was tested
gg <- suppressWarnings(enrichit::gsea(stats, sets, minGSSize = 10, maxGSSize = 500, method = "multilevel", seed = 21, eps = 0, verbose = FALSE))
cat(sprintf("      engine gsea(): %d sets tested; setSize reported for RAW520_OV480 = %s, RAW16_OV6 = %s, ABSENT = %s\n",
            nrow(gg), if ("RAW520_OV480" %in% gg$ID) gg$setSize[gg$ID == "RAW520_OV480"] else "not tested",
            if ("RAW16_OV6" %in% gg$ID) gg$setSize[gg$ID == "RAW16_OV6"] else "not tested", gg$setSize[gg$ID == "ABSENT"]))
## multilevel rank scaling: tiny-magnitude statistics (e.g. correlation coefficients / 1000)
tiny <- stats * 1e-7
gt <- suppressWarnings(enrichit::gsea(tiny, sets["UP1"], minGSSize = 10, maxGSSize = 500, method = "multilevel", seed = 21, eps = 0, verbose = FALSE))
gn <- suppressWarnings(enrichit::gsea(stats, sets["UP1"], minGSSize = 10, maxGSSize = 500, method = "multilevel", seed = 21, eps = 0, verbose = FALSE))
cat(sprintf("      multilevel on stats*1e-7: UP1 ES=%.4f NES=%s p=%s  (same list at native scale: ES=%.4f NES=%.3f p=%.3e)\n",
            gt$enrichmentScore, format(gt$NES, digits = 4), format(gt$pvalue, digits = 3), gn$enrichmentScore, gn$NES, gn$pvalue))
