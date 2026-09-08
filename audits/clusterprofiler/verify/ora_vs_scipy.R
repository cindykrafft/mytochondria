## ORA (hypergeometric) core: enrichit::ora_gson (the engine behind clusterProfiler >= 4.19.3
## enricher/enrichGO/enrichKEGG) and legacy DOSE:::enricher_internal (the engine behind
## clusterProfiler <= 4.18), run on the same synthetic TERM2GENE with known truth.
## Writes one TSV per engine and a JSON of the design; ora_vs_scipy.py checks every
## p-value against scipy.stats.hypergeom and every derived column against its definition.
##
## Usage: R_LIBS_USER=<lib-legacy>:<lib> Rscript ora_vs_scipy.R <outdir>
args <- commandArgs(TRUE); outdir <- if (length(args)) args[1] else tempdir()
dir.create(outdir, showWarnings = FALSE, recursive = TRUE)
suppressPackageStartupMessages({library(enrichit); library(gson); library(jsonlite)})
cat("enrichit", as.character(packageVersion("enrichit")), "\n")
set.seed(20260908)

## ---- synthetic annotation: 3,000 annotated genes, 400 terms of size 3..700 ----------
genes <- sprintf("g%05d", 1:3000)
sizes <- pmax(3L, as.integer(round(exp(runif(400, log(3), log(700))))))
term2gene <- do.call(rbind, lapply(seq_along(sizes), function(i)
    data.frame(term = sprintf("T%03d", i), gene = sample(genes, sizes[i]), stringsAsFactors = FALSE)))
term2gene <- unique(term2gene)
## query: 60 genes from term T010 (size 120 by construction below) + 140 random annotated
## + 30 genes that carry no annotation at all (must be dropped from n)
t10 <- unique(term2gene$gene[term2gene$term == "T010"])
query <- unique(c(sample(t10, min(60, length(t10))), sample(genes, 140), sprintf("x%03d", 1:30)))
## a user universe: 2,000 of the annotated genes + 500 unannotated ids (must be dropped from N)
universe_user <- unique(c(sample(genes, 2000), sprintf("u%03d", 1:500)))

write_json(list(term2gene = term2gene, query = query, universe_user = universe_user,
                annotated = genes), file.path(outdir, "design.json"))

gs <- gson::gson(gsid2gene = setNames(term2gene, c("gsid", "gene")),
                 gsid2name = data.frame(gsid = unique(term2gene$term), name = unique(term2gene$term)),
                 species = "synthetic", gsname = "synthetic", version = "0", accessed_date = "2026-09-08",
                 keytype = "symbol")

run_enrichit <- function(universe, tag, minGSSize = 10, maxGSSize = 500) {
    x <- enrichit::ora_gson(gene = query, pvalueCutoff = 1, pAdjustMethod = "BH", universe = universe,
                            minGSSize = minGSSize, maxGSSize = maxGSSize, qvalueCutoff = 1, gson = gs)
    df <- x@result                                   # unfiltered table (as.data.frame applies cutoffs)
    df$N_universe_slot <- length(x@universe)
    write.table(df, file.path(outdir, paste0("enrichit_", tag, ".tsv")), sep = "\t", quote = FALSE, row.names = FALSE)
    cat(sprintf("enrichit %-12s rows=%d  |universe slot|=%d  min p=%.3e\n", tag, nrow(df), length(x@universe), min(df$pvalue)))
    invisible(x)
}
e1 <- run_enrichit(NULL, "default")
e2 <- run_enrichit(universe_user, "user")
e3 <- run_enrichit(NULL, "size1_inf", minGSSize = 1, maxGSSize = Inf)

## ---- get_enriched filtering with the default cutoffs (pvalueCutoff 0.05, qvalueCutoff 0.2)
x <- enrichit::ora_gson(gene = query, pvalueCutoff = 0.05, pAdjustMethod = "BH", universe = NULL,
                        minGSSize = 10, maxGSSize = 500, qvalueCutoff = 0.2, gson = gs)
shown <- as.data.frame(x)
cat(sprintf("enrichit default cutoffs: table rows=%d; all pvalue<=0.05: %s; all p.adjust<=0.05: %s; all qvalue<=0.2: %s\n",
            nrow(shown), all(shown$pvalue <= 0.05), all(shown$p.adjust <= 0.05), all(shown$qvalue <= 0.2)))
cat(sprintf("  rows in @result with p<=0.05 but p.adjust>0.05: %d (hidden by as.data.frame)\n",
            sum(x@result$pvalue <= 0.05 & x@result$p.adjust > 0.05)))

## ---- legacy engine (DOSE 3.30.0, Bioconductor 3.19) on the same input ----------------
legacy <- tryCatch({
    suppressPackageStartupMessages(library(DOSE))
    cat("DOSE", as.character(packageVersion("DOSE")), "\n")
    ei <- get("enricher_internal", envir = asNamespace("DOSE"))
    for (tag in c("default", "user")) {
        u <- if (tag == "user") universe_user else NULL
        y <- ei(gene = query, pvalueCutoff = 1, pAdjustMethod = "BH", universe = u,
                minGSSize = 10, maxGSSize = 500, qvalueCutoff = 1, USER_DATA = gs)
        df <- y@result; df$N_universe_slot <- length(y@universe)
        write.table(df, file.path(outdir, paste0("dose_", tag, ".tsv")), sep = "\t", quote = FALSE, row.names = FALSE)
        cat(sprintf("DOSE     %-12s rows=%d  |universe slot|=%d  min p=%.3e\n", tag, nrow(df), length(y@universe), min(df$pvalue)))
    }
    TRUE
}, error = function(e) { cat("legacy DOSE not run:", conditionMessage(e), "\n"); FALSE })
cat("done\n")
