#!/usr/bin/env Rscript
# Held-up check against fgsea (Korotkevich et al.), the independent R implementation of
# the same enrichment statistic: ES and leading edge on the ranked list / gene sets that
# heldup_preranked_vs_reference.py wrote and ran through GseaPreranked (weighted, p = 1).
# fgsea's NES uses its own permutation null (different RNG), so NES is compared only in
# sign and rough size; ES and the leading-edge gene sets must agree exactly.
#
# Run after heldup_preranked_vs_reference.py:  Rscript heldup_fgsea_vs_gsea.R
.libPaths(c("/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/scratchpad/clusterprofiler/lib", .libPaths()))
suppressMessages(library(fgsea))
W <- "/tmp/gseawork/heldup_preranked"
rnk <- read.table(file.path(W, "list.rnk"), sep = "\t", stringsAsFactors = FALSE)
stats <- setNames(rnk$V2, rnk$V1)
gs <- gmtPathways(file.path(W, "sets.gmt"))
set.seed(1)
fg <- fgsea(gs, stats, nperm = 1000, gseaParam = 1, minSize = 15, maxSize = 500, scoreType = "std")

run <- sort(list.files(file.path(W, "out_weighted"), pattern = "^run\\.GseaPreranked", full.names = TRUE))
run <- run[length(run)]
rep <- do.call(rbind, lapply(list.files(run, pattern = "^gsea_report_for_.*\\.tsv$", full.names = TRUE),
                             function(f) read.delim(f, check.names = FALSE, stringsAsFactors = FALSE)))
# leading edge from results.edb (HIT_INDICES / RANK_AT_ES, 0-based ranks)
edb <- readLines(file.path(run, "edb", "results.edb"))
dtg <- grep("<DTG ", edb, value = TRUE)
attr1 <- function(line, key) sub(paste0('.*', key, '="([^"]*)".*'), "\\1", line)
le_gsea <- list()
for (l in dtg) {
  name <- sub(".*#", "", attr1(l, "GENESET"))
  hits <- as.integer(strsplit(attr1(l, "HIT_INDICES"), " ")[[1]])
  rk <- as.integer(as.numeric(attr1(l, "RANK_AT_ES")))
  es <- as.numeric(attr1(l, "ES"))
  core <- if (es >= 0) hits[hits <= rk] else hits[hits >= rk]
  le_gsea[[name]] <- sort(names(stats)[core + 1])
}
cat(sprintf("fgsea %s, R %s; %d sets in fgsea, %d in the GSEA report\n",
            as.character(packageVersion("fgsea")), R.version.string, nrow(fg), nrow(rep)))
m <- merge(as.data.frame(fg[, c("pathway", "ES", "NES", "size")]), rep[, c("NAME", "ES", "NES", "SIZE")],
           by.x = "pathway", by.y = "NAME", suffixes = c("_fgsea", "_gsea"))
cat(sprintf("max |ES_fgsea - ES_gsea| = %.2e over %d sets; sizes equal: %s\n",
            max(abs(m$ES_fgsea - m$ES_gsea)), nrow(m), all(m$size == m$SIZE)))
cat(sprintf("NES sign agreement: %d of %d; max |NES_fgsea - NES_gsea| = %.3f (different nulls)\n",
            sum(sign(m$NES_fgsea) == sign(m$NES_gsea)), nrow(m), max(abs(m$NES_fgsea - m$NES_gsea))))
n_le_ok <- 0
for (i in seq_len(nrow(fg))) {
  a <- sort(fg$leadingEdge[[i]])
  b <- le_gsea[[fg$pathway[i]]]
  if (identical(a, b)) n_le_ok <- n_le_ok + 1 else cat("  leading edge differs:", fg$pathway[i], length(a), length(b), "\n")
}
cat(sprintf("leading-edge gene sets identical: %d of %d\n", n_le_ok, nrow(fg)))
