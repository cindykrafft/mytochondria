# The cluster-column lines of scDblFinder() on devel 6b3ecdf (after 34368ed "fixed typo" and
# 6b3ecdf "fixed conversion to factor"), run on a base data.frame as built by .evaluateKNN().
cells <- c("c1","c2","c3","c4","c5")
mk <- function() data.frame(row.names=cells, type=rep("real",5), cluster=rep(NA,5))
run <- function(clusters, sce_cells=cells[1:4]) {
  d <- mk()
  d$cluster <- NA_character_
  d[sce_cells,"cluster"] <- as.character(clusters)
  if(is.factor(clusters)) d$cluster <- factor(d$cluster, levels(clusters))
  d$cluster
}
f <- factor(c("T","B","T","NK"), levels=c("B","NK","T"))
cat("factor:    "); print(run(f))
cat("character: "); print(run(c("T","B","T","NK")))
cat("integer:   "); print(run(c(3L,1L,3L,2L)))
