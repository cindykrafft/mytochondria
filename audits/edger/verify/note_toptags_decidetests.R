#!/usr/bin/env Rscript
# Notes on topTags() and decideTests(): which set BH runs over, the sort order, and the two
# functions' treatment of the p.value boundary (topTags keeps FDR <= p.value, decideTests
# calls FDR < p.value).
suppressMessages(library(edgeR))
cat("edgeR", as.character(packageVersion("edgeR")), "\n")
set.seed(3)
G <- 500
tab <- data.frame(logFC=rnorm(G), logCPM=runif(G, 0, 10), PValue=c(runif(50, 0, 1e-3), runif(G-50)))
et <- new("DGEExact", list(table=tab, comparison=c("A", "B"), genes=NULL))
tt <- topTags(et, n=Inf)$table
cat("BH in topTags equals p.adjust over all", G, "genes:", isTRUE(all.equal(tt$FDR[order(as.integer(rownames(tt)))], p.adjust(tab$PValue, "BH"))), "\n")
cat("topTags(n=20) after topTags(p.value=0.05): rows ordered by PValue then |logFC| desc:",
    !is.unsorted(tt$PValue) && all(diff(abs(tt$logFC))[diff(tt$PValue) == 0] <= 0), "\n")
# boundary: one gene with p exactly 0.05 (BH adjusted = 0.05 exactly for a single gene)
et1 <- new("DGEExact", list(table=data.frame(logFC=1, logCPM=5, PValue=0.05), comparison=c("A", "B"), genes=NULL))
cat("single gene, FDR exactly 0.05: topTags(p.value=0.05) returns", nrow(topTags(et1, p.value=0.05)$table), "row(s);",
    "decideTests(p.value=0.05) calls it", as.integer(decideTests(et1, p.value=0.05)), "(1 = Up, 0 = NotSig)\n")
# lfc in decideTests applies to the (shrunk) logFC column, not to a threshold test
et2 <- new("DGEExact", list(table=data.frame(logFC=c(0.9, 1.1, -1.1), logCPM=5, PValue=c(1e-6, 1e-6, 1e-6)), comparison=c("A", "B"), genes=NULL))
cat("decideTests(lfc=1) on logFC 0.9/1.1/-1.1 with p=1e-6:", as.integer(decideTests(et2, lfc=1)), "\n")
# glmQLFTest with several coefficients: topTags sorts by the first logFC column with a warning
set.seed(4)
y <- matrix(rnbinom(300*6, mu=50, size=10), 300, 6)
d <- DGEList(y, group=factor(c(1,1,2,2,3,3))); design <- model.matrix(~d$samples$group)
fit <- glmQLFit(d, design, dispersion=0.1)
q <- glmQLFTest(fit, coef=2:3)
w <- tryCatch({topTags(q, sort.by="logFC"); "no warning"}, warning=function(w) conditionMessage(w))
cat("topTags(sort.by='logFC') on a 2-df test:", w, "\n")
cat("columns of a 2-df glmQLFTest table:", paste(colnames(q$table), collapse=", "), "\n")
