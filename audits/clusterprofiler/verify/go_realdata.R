## Magnitude of the engine-version behaviours on a real annotation: GO BP from org.Hs.eg.db 3.18.0
## (GO.db 3.18.0), built by clusterProfiler:::get_GO_data("org.Hs.eg.db", "BP", "ENTREZID") and saved
## as a GSON (go_bp_gson.rds). Run once per engine library:
##   R_LIBS_USER=<lib-enrichit-x.y.z>:<lib> Rscript go_realdata.R <go_bp_gson.rds>     (enrichit x.y.z)
##   R_LIBS_USER=<lib-legacy>:<lib>          Rscript go_realdata.R <go_bp_gson.rds>     (adds DOSE 3.30.0)
## Synthetic query / ranked list with known truth; the annotation is real.
args <- commandArgs(TRUE)
gs <- readRDS(args[1])
suppressPackageStartupMessages({library(enrichit); library(gson); library(qvalue)})
has_dose <- requireNamespace("DOSE", quietly = TRUE) && packageVersion("DOSE") < "4.0.0"
cat(sprintf("== enrichit %s%s\n", as.character(packageVersion("enrichit")), if (has_dose) paste0(" + DOSE ", as.character(packageVersion("DOSE"))) else ""))
g2g <- gs@gsid2gene; g2g$gsid <- as.character(g2g$gsid); g2g$gene <- as.character(g2g$gene)
sets <- split(g2g$gene, g2g$gsid); sizes <- lengths(sets)
universe_all <- unique(g2g$gene)
cat(sprintf("GO BP: %d terms, %d annotated genes, %d terms with 10 <= size <= 500\n", length(sets), length(universe_all), sum(sizes >= 10 & sizes <= 500)))

## ---- ORA: 100 genes from two mid-sized terms + 100 random annotated genes ----------------
set.seed(77)
mid <- names(sets)[sizes >= 150 & sizes <= 300]
t1 <- sample(mid, 1); t2 <- sample(setdiff(mid, t1), 1)
query <- unique(c(sample(sets[[t1]], 50), sample(sets[[t2]], 50), sample(universe_all, 100)))
x <- enrichit::ora_gson(gene = query, pvalueCutoff = 0.05, pAdjustMethod = "BH", universe = NULL,
                        minGSSize = 10, maxGSSize = 500, qvalueCutoff = 0.2, gson = gs)
r <- x@result; shown <- as.data.frame(x)
cat(sprintf("ORA default universe: query %d genes (%d annotated); @result rows = %d (Count = 0 rows: %d) -> BH over %d terms; terms with p.adjust <= 0.05: %d; rows shown (p, p.adjust <= 0.05 & q <= 0.2): %d; planted %s p.adjust = %.2e, %s p.adjust = %.2e\n",
            length(query), sum(query %in% universe_all), nrow(r), sum(r$Count == 0), nrow(r), sum(r$p.adjust <= 0.05), nrow(shown),
            t1, r[t1, "p.adjust"], t2, r[t2, "p.adjust"]))
## the q-value column: enrichit's policy vs the legacy one, on this engine's own p-values
p_tested <- r$pvalue[r$Count > 0]
q_legacy <- tryCatch(qvalue(p_tested, lambda = 0.05, pi0.method = "bootstrap")$qvalues, error = function(e) rep(NA, length(p_tested)))
q_new <- tryCatch(qvalue(p_tested)$qvalues, error = function(e) rep(NA, length(p_tested)))
cat(sprintf("   qvalue on the %d tested p-values: legacy (lambda=0.05, bootstrap) pi0 = %.3f, terms q <= 0.2: %d; default qvalue() pi0 = %.3f, terms q <= 0.2: %d; terms crossing 0.2 between the two: %d; engine column matches: legacy %s / default %s\n",
            length(p_tested), tryCatch(qvalue(p_tested, lambda = 0.05, pi0.method = "bootstrap")$pi0, error = function(e) NA), sum(q_legacy <= 0.2, na.rm = TRUE),
            tryCatch(qvalue(p_tested)$pi0, error = function(e) NA), sum(q_new <= 0.2, na.rm = TRUE), sum((q_legacy <= 0.2) != (q_new <= 0.2), na.rm = TRUE),
            isTRUE(all.equal(r$qvalue[r$Count > 0], q_legacy)), isTRUE(all.equal(r$qvalue[r$Count > 0], q_new))))

## ---- ORA with a user universe that omits 10 % of the query (legacy n-counting) ---------
set.seed(78)
u_user <- sample(universe_all, 12000)
q_in <- unique(c(sample(intersect(sets[[t1]], u_user), 45), sample(intersect(sets[[t2]], u_user), 45), sample(u_user, 90)))
q_out <- sample(setdiff(universe_all, u_user), 20)
query2 <- unique(c(q_in, q_out))
x2 <- enrichit::ora_gson(gene = query2, pvalueCutoff = 0.05, pAdjustMethod = "BH", universe = u_user,
                         minGSSize = 10, maxGSSize = 500, qvalueCutoff = 0.2, gson = gs)
r2 <- x2@result
cat(sprintf("ORA user universe (12,000 genes; %d of %d query genes outside it): enrichit n = %s, rows = %d, terms p.adjust <= 0.05: %d\n",
            length(q_out), length(query2), strsplit(r2$GeneRatio[1], "/")[[1]][2], nrow(r2), sum(r2$p.adjust <= 0.05)))
if (has_dose) {
    ei <- get("enricher_internal", envir = asNamespace("DOSE"))
    y2 <- ei(gene = query2, pvalueCutoff = 0.05, pAdjustMethod = "BH", universe = u_user, minGSSize = 10, maxGSSize = 500, qvalueCutoff = 0.2, USER_DATA = gs)
    d2 <- y2@result
    m <- merge(r2[, c("ID", "pvalue", "p.adjust", "Count")], d2[, c("ID", "pvalue", "p.adjust", "Count")], by = "ID", suffixes = c(".new", ".old"))
    cat(sprintf("   legacy DOSE: n = %s, rows = %d (with Count = 0: %d), terms p.adjust <= 0.05: %d; common terms %d: p ratio old/new median %.3f (min %.3f); terms whose p.adjust <= 0.05 call differs: %d\n",
                strsplit(d2$GeneRatio[1], "/")[[1]][2], nrow(d2), sum(d2$Count == 0), sum(d2$p.adjust <= 0.05), nrow(m),
                median(m$pvalue.old / m$pvalue.new), min(m$pvalue.old / m$pvalue.new), sum((m$p.adjust.new <= 0.05) != (m$p.adjust.old <= 0.05))))
    y1 <- ei(gene = query, pvalueCutoff = 0.05, pAdjustMethod = "BH", universe = NULL, minGSSize = 10, maxGSSize = 500, qvalueCutoff = 0.2, USER_DATA = gs)
    d1 <- y1@result; m1 <- merge(r[, c("ID", "pvalue", "p.adjust", "qvalue")], d1[, c("ID", "pvalue", "p.adjust", "qvalue")], by = "ID", suffixes = c(".new", ".old"))
    cat(sprintf("   legacy DOSE, default universe: rows = %d, max |p diff| vs enrichit = %.1e, max |p.adjust diff| = %.1e, max |qvalue diff| = %.3f, terms whose q <= 0.2 call differs: %d, shown rows %d\n",
                nrow(d1), max(abs(m1$pvalue.new - m1$pvalue.old)), max(abs(m1$p.adjust.new - m1$p.adjust.old)), max(abs(m1$qvalue.new - m1$qvalue.old), na.rm = TRUE),
                sum((m1$qvalue.new <= 0.2) != (m1$qvalue.old <= 0.2), na.rm = TRUE), nrow(as.data.frame(y1))))
}

## ---- GSEA: all annotated genes ranked, 5 terms planted up and 5 down -------------------
set.seed(79)
stats <- setNames(rnorm(length(universe_all)), universe_all)
up <- sample(names(sets)[sizes >= 30 & sizes <= 120], 5); dn <- sample(setdiff(names(sets)[sizes >= 30 & sizes <= 120], up), 5)
for (t in up) stats[sets[[t]]] <- stats[sets[[t]]] + 1.2
for (t in dn) stats[sets[[t]]] <- stats[sets[[t]]] - 1.2
stats <- sort(stats, decreasing = TRUE)
t0 <- Sys.time()
g <- suppressWarnings(enrichit::gsea_gson(geneList = stats, gson = gs, minGSSize = 10, maxGSSize = 500, pvalueCutoff = 0.05,
                                          pAdjustMethod = "BH", verbose = FALSE, eps = 1e-10, seed = 80))
res <- g@result
cat(sprintf("GSEA (multilevel, eps 1e-10, default cutoff 0.05): result rows = %d; rows with p.adjust > 0.05 = %d (p.adjust > 0.5: %d, max %.3f); planted terms in result: %d of 10 (all with p.adjust <= 0.05: %s); %s\n",
            nrow(res), sum(res$p.adjust > 0.05), sum(res$p.adjust > 0.5), max(res$p.adjust), sum(c(up, dn) %in% res$ID), all(res[intersect(c(up, dn), res$ID), "p.adjust"] <= 0.05), format(Sys.time() - t0)))
gg <- suppressWarnings(enrichit::gsea(stats, sets, minGSSize = 10, maxGSSize = 500, method = "multilevel", seed = 80, eps = 1e-10, verbose = FALSE))
cat(sprintf("   engine gsea(): %d sets tested (terms with 10 <= overlap <= 500 in this list: %d); pvalue <= 0.05: %d; BH p.adjust <= 0.05: %d\n",
            nrow(gg), sum(vapply(sets, function(s) { n <- sum(s %in% names(stats)); n >= 10 && n <= 500 }, logical(1))), sum(gg$pvalue <= 0.05, na.rm = TRUE), sum(p.adjust(gg$pvalue, "BH") <= 0.05, na.rm = TRUE)))
## a list with no planted signal at all (pure null): how many rows does the default table report?
set.seed(81)
null <- sort(setNames(rnorm(length(universe_all)), universe_all), decreasing = TRUE)
g0 <- suppressWarnings(enrichit::gsea_gson(geneList = null, gson = gs, minGSSize = 10, maxGSSize = 500, pvalueCutoff = 0.05, pAdjustMethod = "BH", verbose = FALSE, eps = 1e-10, seed = 82))
cat(sprintf("GSEA on a pure-null ranked list: result rows = %d (p.adjust <= 0.05 among them: %d)\n", if (is.null(g0)) 0 else nrow(g0@result), if (is.null(g0)) 0 else sum(g0@result$p.adjust <= 0.05)))
