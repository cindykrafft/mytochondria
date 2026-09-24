# createDoublets with the input order kept, the halving counted over all pairs, and the
# single-pair case handled (the change proposed upstream; see ../upstream/)
createDoubletsFixed <- function(x, dbl.idx, clusters=NULL, resamp=0.5, halfSize=0.5, adjustSize=FALSE, prefix="dbl."){
  ns <- asNamespace("scDblFinder")
  adjustSize <- ns$.checkPropArg(as.numeric(adjustSize),FALSE); halfSize <- ns$.checkPropArg(as.numeric(halfSize),FALSE); resamp <- ns$.checkPropArg(as.numeric(resamp),FALSE)
  if(is(x,"SingleCellExperiment")) x <- counts(x)
  npairs <- nrow(dbl.idx)
  wAd <- sample.int(npairs, size=round(adjustSize*npairs))
  x1 <- x[,dbl.idx[,1],drop=FALSE]+x[,dbl.idx[,2],drop=FALSE]
  if(length(wAd)>0){
    if(is.null(clusters)) stop("If `adjustSize=TRUE`, clusters must be given.")
    adj <- as.data.frame(dbl.idx[wAd,,drop=FALSE]); ls <- Matrix::colSums(x)
    csz <- vapply(split(ls,clusters), FUN=median, FUN.VALUE=numeric(1))
    adj$ls.ratio <- ls[adj[,1]]/(ls[adj[,1]]+ls[adj[,2]])
    ls1 <- csz[as.character(clusters[adj[,1]])]; ls2 <- csz[as.character(clusters[adj[,2]])]
    adj$factor <- pmin(0.8, pmax(0.2, (adj$ls.ratio+ls1/(ls1+ls2))/2))
    adj$ls <- ls[adj[,1]]+ls[adj[,2]]
    x2 <- x[,adj[,1],drop=FALSE]*adj$factor + x[,adj[,2],drop=FALSE]*(1-adj$factor)
    x2 <- x2 %*% Matrix::Diagonal(x=adj$ls/Matrix::colSums(x2))
    x1[,wAd] <- x2
  }
  x <- x1; rm(x1)
  if(halfSize>0){
    wAd <- sample.int(npairs, size=ceiling(halfSize*npairs))
    if(length(wAd)>0) x[,wAd] <- x[,wAd]/2
  }
  if(resamp>0){
    if(resamp!=halfSize) wAd <- sample.int(ncol(x), ceiling(resamp*ncol(x)))
    if(length(wAd)>0) x[,wAd] <- matrix(as.integer(rpois(nrow(x)*length(wAd), as.numeric(as.matrix(x[,wAd])))), nrow=nrow(x))
  }else{
    x <- round(x)
  }
  x <- as(x,"CsparseMatrix"); colnames(x) <- paste0( prefix, seq_len(ncol(x)) ); x
}
