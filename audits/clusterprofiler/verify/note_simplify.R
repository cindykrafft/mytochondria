## simplify(): what the greedy cluster rule removes. For each removed term: does a kept term with
## similarity > cutoff and a smaller p.adjust exist (redundancy in the documented sense), or was the
## term removed because a *third* term, similar to the cluster seed but not to it, had a smaller p?
## Usage: R_LIBS_USER=<lib> Rscript note_simplify.R
suppressPackageStartupMessages({library(clusterProfiler); library(org.Hs.eg.db)})
cat("clusterProfiler", as.character(packageVersion("clusterProfiler")), "GOSemSim", as.character(packageVersion("GOSemSim")), "\n")
gs <- clusterProfiler:::get_GO_data("org.Hs.eg.db", "BP", "ENTREZID")
g2g <- gs@gsid2gene; sets <- split(as.character(g2g$gene), as.character(g2g$gsid)); sizes <- lengths(sets)
sd <- suppressWarnings(GOSemSim::godata("org.Hs.eg.db", ont = "BP", computeIC = FALSE))
for (seed in 5:7) {
    set.seed(seed)
    t1 <- sample(names(sets)[sizes >= 150 & sizes <= 300], 1)
    query <- unique(c(sample(sets[[t1]], 60), sample(unique(g2g$gene), 140)))
    e <- enrichGO(query, OrgDb = "org.Hs.eg.db", ont = "BP")
    df <- as.data.frame(e); rownames(df) <- df$ID
    s <- suppressWarnings(simplify(e, cutoff = 0.7, by = "p.adjust", select_fun = min, measure = "Wang", semData = sd))
    kept <- as.data.frame(s)$ID; removed <- setdiff(df$ID, kept)
    sim <- GOSemSim::mgoSim(df$ID, df$ID, semData = sd, measure = "Wang", combine = NULL)
    cls <- vapply(removed, function(id) {
        nb <- rownames(sim)[sim[, id] > 0.7 & rownames(sim) != id]              # terms similar to id
        better <- nb[df[nb, "p.adjust"] <= df[id, "p.adjust"]]                    # ... with p.adjust <= its own
        if (any(better %in% kept)) "redundant with a kept, better-ranked term"
        else if (length(better)) "better similar terms exist but all were removed too"
        else if (any(nb %in% kept)) "no better similar term; a worse-ranked similar term was kept"
        else "no similar term kept at all"
    }, character(1))
    cat(sprintf("seed %d: %d enriched terms -> %d kept, %d removed\n", seed, nrow(df), length(kept), length(removed)))
    for (k in names(table(cls))) cat(sprintf("   %-62s %d\n", k, table(cls)[[k]]))
    orphan <- removed[cls == "no similar term kept at all"]
    if (length(orphan)) cat(sprintf("   orphans (removed, not similar to any kept term), first 5: %s; their p.adjust ranks among %d terms: %s\n",
                                    paste(head(orphan, 5), collapse = ", "), nrow(df), paste(head(match(orphan, df$ID), 5), collapse = ", ")))
}
