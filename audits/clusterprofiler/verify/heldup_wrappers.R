## clusterProfiler wrappers on real annotations (org.Hs.eg.db 3.18.0, GO.db 3.18.0), devel HEAD
## built against enrichit 0.2.2: enrichGO through the ENTREZID and the SYMBOL path, gseGO through
## the wrapper vs the engine, simplify(), compareCluster(), setReadable(), and the documented
## `method` values. Usage: R_LIBS_USER=<lib> Rscript heldup_wrappers.R
suppressPackageStartupMessages({library(clusterProfiler); library(org.Hs.eg.db); library(AnnotationDbi)})
cat("clusterProfiler", as.character(packageVersion("clusterProfiler")), "enrichit", as.character(packageVersion("enrichit")),
    "GOSemSim", as.character(packageVersion("GOSemSim")), "org.Hs.eg.db", as.character(packageVersion("org.Hs.eg.db")), "\n")
gs <- clusterProfiler:::get_GO_data("org.Hs.eg.db", "BP", "ENTREZID")
g2g <- gs@gsid2gene; sets <- split(as.character(g2g$gene), as.character(g2g$gsid)); sizes <- lengths(sets)
set.seed(5)
t1 <- sample(names(sets)[sizes >= 150 & sizes <= 300], 1)
query <- unique(c(sample(sets[[t1]], 60), sample(unique(g2g$gene), 140)))

## ---- enrichGO(ENTREZID) equals enrichit::ora_gson on the same GSON ------------------------
e1 <- enrichGO(query, OrgDb = "org.Hs.eg.db", keyType = "ENTREZID", ont = "BP", pvalueCutoff = 1, qvalueCutoff = 1)
e0 <- enrichit::ora_gson(query, pvalueCutoff = 1, universe = NULL, minGSSize = 10, maxGSSize = 500, qvalueCutoff = 1, gson = gs)
cat(sprintf("enrichGO(ENTREZID) rows %d, engine rows %d, identical pvalue/p.adjust/Count: %s; universe = all BP-annotated genes: %d (annotated %d)\n",
            nrow(e1@result), nrow(e0@result), isTRUE(all.equal(e1@result[e0@result$ID, c("pvalue", "p.adjust", "Count")], e0@result[, c("pvalue", "p.adjust", "Count")], check.attributes = FALSE)),
            length(e1@universe), length(unique(g2g$gene))))

## ---- enrichGO(SYMBOL): mapped to ENTREZID first (since 4.19.5, #805); one-to-many symbols ---
sym_map <- suppressMessages(AnnotationDbi::select(org.Hs.eg.db, keys = unique(g2g$gene), keytype = "ENTREZID", columns = "SYMBOL"))
multi <- names(which(table(sym_map$SYMBOL) > 1))
cat(sprintf("SYMBOL keys mapping to > 1 ENTREZID among BP-annotated genes: %d of %d (e.g. %s)\n", length(multi), length(unique(sym_map$SYMBOL)), paste(head(multi, 5), collapse = ", ")))
qsym <- unique(sym_map$SYMBOL[match(query, sym_map$ENTREZID)])
qsym <- unique(c(qsym, head(multi, 5)))         # add five ambiguous symbols
es <- enrichGO(qsym, OrgDb = "org.Hs.eg.db", keyType = "SYMBOL", ont = "BP", pvalueCutoff = 1, qvalueCutoff = 1)
back <- suppressWarnings(bitr(qsym, fromType = "SYMBOL", toType = "ENTREZID", OrgDb = "org.Hs.eg.db"))
cat(sprintf("enrichGO(SYMBOL) with %d symbols: n in GeneRatio = %s (symbols mapped to %d Entrez ids); the ENTREZID run on those ids gives identical p-values: %s\n",
            length(qsym), strsplit(es@result$GeneRatio[1], "/")[[1]][2], length(unique(back$ENTREZID)),
            isTRUE(all.equal(es@result[e1@result$ID[1:50], "pvalue"], enrichGO(unique(back$ENTREZID), OrgDb = "org.Hs.eg.db", ont = "BP", pvalueCutoff = 1, qvalueCutoff = 1)@result[e1@result$ID[1:50], "pvalue"]))))
cat(sprintf("   geneID column is in symbols: %s; keytype slot: %s\n", grepl("^[A-Z]", strsplit(es@result$geneID[1], "/")[[1]][1]), es@keytype))

## ---- setReadable -----------------------------------------------------------------------
er <- setReadable(e1, "org.Hs.eg.db", keyType = "ENTREZID")
ids <- strsplit(e1@result[t1, "geneID"], "/")[[1]]; syms <- strsplit(er@result[t1, "geneID"], "/")[[1]]
exp_syms <- suppressMessages(mapIds(org.Hs.eg.db, ids, "SYMBOL", "ENTREZID"))
cat(sprintf("setReadable: %d ids -> %d symbols, equal to mapIds(ENTREZID->SYMBOL) in order: %s; numbers untouched: %s\n",
            length(ids), length(syms), identical(unname(exp_syms), syms), identical(er@result$pvalue, e1@result$pvalue)))

## ---- simplify() --------------------------------------------------------------------------
e5 <- enrichGO(query, OrgDb = "org.Hs.eg.db", keyType = "ENTREZID", ont = "BP", pvalueCutoff = 0.05, qvalueCutoff = 0.2)
df5 <- as.data.frame(e5)
t0 <- Sys.time(); s5 <- simplify(e5, cutoff = 0.7, by = "p.adjust", select_fun = min, measure = "Wang"); ds <- as.data.frame(s5)
cat(sprintf("simplify(cutoff 0.7, Wang): %d -> %d terms in %s; every kept term is in the input: %s; p-values unchanged: %s\n",
            nrow(df5), nrow(ds), format(Sys.time() - t0), all(ds$ID %in% df5$ID), isTRUE(all.equal(ds$p.adjust, df5[ds$ID, "p.adjust"]))))
## the rule: a term is removed when a term with similarity > cutoff has a smaller p.adjust (ties: more ancestors)
sd <- GOSemSim::godata("org.Hs.eg.db", ont = "BP", computeIC = FALSE)
sim <- GOSemSim::mgoSim(df5$ID, df5$ID, semData = sd, measure = "Wang", combine = NULL)
removed <- setdiff(df5$ID, ds$ID)
has_better <- vapply(removed, function(id) { j <- which(sim[, id] > 0.7 & rownames(sim) != id); any(df5[rownames(sim)[j], "p.adjust"] <= df5[id, "p.adjust"]) }, logical(1))
kept_pairs <- sum(sim[ds$ID, ds$ID] > 0.7) - nrow(ds)
cat(sprintf("   every removed term has a >0.7-similar term with p.adjust <= its own: %s; pairs of kept terms still > 0.7 similar: %d; removed terms whose only better neighbour was itself removed: %d\n",
            all(has_better), kept_pairs / 2,
            sum(vapply(removed, function(id) { j <- rownames(sim)[sim[, id] > 0.7 & rownames(sim) != id & df5[rownames(sim), "p.adjust"] <= df5[id, "p.adjust"]]; length(j) > 0 && all(j %in% removed) }, logical(1)))))

## ---- compareCluster: per-cluster enrichGO, per-cluster BH -------------------------------
set.seed(6)
cl <- list(A = query, B = unique(c(sample(sets[[sample(names(sets)[sizes >= 150 & sizes <= 300], 1)]], 60), sample(unique(g2g$gene), 140))))
cc <- compareCluster(cl, fun = "enrichGO", OrgDb = "org.Hs.eg.db", ont = "BP", pvalueCutoff = 1, qvalueCutoff = 1)
ccd <- as.data.frame(cc)
eB <- enrichGO(cl$B, OrgDb = "org.Hs.eg.db", ont = "BP", pvalueCutoff = 1, qvalueCutoff = 1)
a <- ccd[ccd$Cluster == "A", ]; b <- ccd[ccd$Cluster == "B", ]
cat(sprintf("compareCluster(enrichGO): cluster A rows %d == enrichGO(A) rows %d with identical p.adjust: %s; cluster B identical to enrichGO(B): %s (BH is per cluster, not over both)\n",
            nrow(a), nrow(e1@result), isTRUE(all.equal(a$p.adjust[match(e1@result$ID, a$ID)], e1@result$p.adjust)),
            isTRUE(all.equal(b$p.adjust[match(eB@result$ID, b$ID)], eB@result$p.adjust))))
cc5 <- compareCluster(cl, fun = "enrichGO", OrgDb = "org.Hs.eg.db", ont = "BP")
cat(sprintf("   default cutoffs: compareCluster table rows %d (A %d, B %d) vs as.data.frame(enrichGO) A %d, B %d\n",
            nrow(as.data.frame(cc5)), sum(as.data.frame(cc5)$Cluster == "A"), sum(as.data.frame(cc5)$Cluster == "B"),
            nrow(as.data.frame(enrichGO(cl$A, OrgDb = "org.Hs.eg.db", ont = "BP"))), nrow(as.data.frame(enrichGO(cl$B, OrgDb = "org.Hs.eg.db", ont = "BP")))))

## ---- gseGO wrapper vs engine; documented `method` values ---------------------------------
set.seed(7)
gl <- sort(setNames(rnorm(length(unique(g2g$gene))), unique(g2g$gene)), decreasing = TRUE)
gl[sets[[t1]]] <- gl[sets[[t1]]] + 1.5; gl <- sort(gl, decreasing = TRUE)
gw <- suppressWarnings(gseGO(gl, ont = "BP", OrgDb = "org.Hs.eg.db", pvalueCutoff = 1, seed = 9, verbose = FALSE))
ge <- suppressWarnings(enrichit::gsea_gson(gl, gs, minGSSize = 10, maxGSSize = 500, pvalueCutoff = 1, seed = 9, verbose = FALSE))
cat(sprintf("gseGO wrapper vs enrichit::gsea_gson (same seed): rows %d / %d, identical NES and pvalue: %s; planted term %s NES = %.2f p.adjust = %.2e\n",
            nrow(gw@result), nrow(ge@result), isTRUE(all.equal(gw@result[ge@result$ID, c("NES", "pvalue")], ge@result[, c("NES", "pvalue")], check.attributes = FALSE)),
            t1, gw@result[t1, "NES"], gw@result[t1, "p.adjust"]))
for (m in c("fgsea", "monte carlo", "sample", "permute")) {
    r <- tryCatch({ suppressWarnings(GSEA(gl[1:3000], TERM2GENE = data.frame(term = t1, gene = sets[[t1]]), method = m, nPerm = 200, pvalueCutoff = 1, verbose = FALSE)); "runs" },
                  error = function(e) paste("ERROR:", conditionMessage(e)))
    cat(sprintf("   GSEA(method = \"%s\"): %s\n", m, substr(r, 1, 90)))
}
r <- tryCatch({ suppressWarnings(GSEA(gl[1:3000], TERM2GENE = data.frame(term = t1, gene = sets[[t1]]), by = "fgsea", pvalueCutoff = 1, verbose = FALSE)); "runs" }, error = function(e) paste("ERROR:", conditionMessage(e)))
cat(sprintf("   GSEA(by = \"fgsea\") (the <= 4.18 argument): %s\n", substr(r, 1, 90)))
