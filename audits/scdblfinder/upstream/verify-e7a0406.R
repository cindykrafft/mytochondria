# The cluster-column lines of scDblFinder() on devel e7a0406 (R/scDblFinder.R:503-509),
# run on the same kind of object: .evaluateKNN() returns d as a base data.frame
# (R/scDblFinder.R:567, cluster=NA).
cells <- c("c1","c2","c3","c4")
mk <- function() data.frame(row.names=cells, type=rep("real",4), cluster=rep(NA,4))
clusters <- factor(c("T","B","T","NK"), levels=c("B","NK","T"))

cat("1. as committed (NA_character):\n")
d <- mk()
r <- try({
  d$cluster <- NA_character
  d[cells,"cluster"] <- as.character(clusters)
  if(is.factor(clusters)) d[cells,"cluster"] <- factor(d[cells,"cluster"], levels(clusters))
}, silent=TRUE)
cat("  ", if(inherits(r,"try-error")) conditionMessage(attr(r,"condition")) else "no error", "\n")

cat("2. with NA_character_ (the base-R constant):\n")
d <- mk()
d$cluster <- NA_character_
d[cells,"cluster"] <- as.character(clusters)
if(is.factor(clusters)) d[cells,"cluster"] <- factor(d[cells,"cluster"], levels(clusters))
cat("   cluster column:", d$cluster, " (labels were", as.character(clusters), ")\n")

cat("3. without the factor re-assignment (as in PR #148):\n")
d <- mk()
d[cells,"cluster"] <- if(is.factor(clusters)) as.character(clusters) else clusters
cat("   cluster column:", d$cluster, "\n")

cat("4. whole column as a factor with the given levels, then labels assigned:\n")
d <- mk()
d$cluster <- factor(NA, levels(clusters))
d[cells,"cluster"] <- as.character(clusters)
cat("   cluster column:", as.character(d$cluster), " levels:", levels(d$cluster), "\n")
