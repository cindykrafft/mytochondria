library(fgsea)
set.seed(5)
n <- 20000; g <- sprintf("G%05d", 1:n)
st <- setNames(c(rnorm(n - 6000, 0, 0.6), rep(0, 6000)), g)   # 6,000 genes with stat exactly 0
st <- st[sample(n)]
zero <- names(st)[st == 0]
S <- zero[2001:2100]                     # 100 zero-stat genes that are adjacent in the input vector
run <- function(stats) { set.seed(1); fgsea(list(S = S), stats)[, .(ES, NES, pval)] }
cbind(order = c("as given", "set moved first", "set moved last", "shuffled"), rbind(run(st),
      run(st[order(names(st) %in% S, decreasing = TRUE)]),
      run(st[order(names(st) %in% S)]),
      run(st[sample(n)])))
packageVersion("fgsea")
