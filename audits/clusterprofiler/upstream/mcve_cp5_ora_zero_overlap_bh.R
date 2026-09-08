## CP5 (issue #819): with enrichit <= 0.1.5 the ORA of clusterProfiler 4.19.3-4.20.x adjusted p-values
## over every gene set in the size window, including sets with no query gene (Count = 0).
library(enrichit); library(gson)
set.seed(3)
genes <- paste0("g", 1:2000)
t2g <- unique(data.frame(gsid = rep(paste0("S", 1:200), each = 30), gene = sample(genes, 6000, replace = TRUE)))
gs <- gson::gson(gsid2gene = t2g, gsid2name = data.frame(gsid = unique(t2g$gsid), name = unique(t2g$gsid)),
                 species = "s", gsname = "s", version = "0", accessed_date = "2026-09-08", keytype = "k")
query <- unique(c(t2g$gene[t2g$gsid == "S1"][1:15], sample(genes, 30)))    # 15 genes of S1 + 30 random
x <- enrichit::ora_gson(query, pvalueCutoff = 1, universe = NULL, minGSSize = 10, maxGSSize = 500, qvalueCutoff = 1, gson = gs)
r <- x@result
cat("enrichit", as.character(packageVersion("enrichit")), "\n")
cat("rows in @result:", nrow(r), "  rows with Count = 0:", sum(r$Count == 0), "  S1 p =", signif(r["S1", "pvalue"], 3), " p.adjust =", signif(r["S1", "p.adjust"], 3),
    "  (BH over the", sum(r$Count > 0), "sets with Count > 0 would give", signif(p.adjust(r$pvalue[r$Count > 0], "BH")[which(r$ID[r$Count > 0] == "S1")], 3), ")\n")
stopifnot(all(r$Count > 0))   # expected (clusterProfiler <= 4.18, enrichit >= 0.2.0): only sets with at least one query gene are tested
