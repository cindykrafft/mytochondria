## LM3: the max|grad| convergence warning always reports "component 1"
library(lme4)
ctrl <- lmerControl()$checkConv
derivs <- list(gradient = c(1e-6, 0.5, 1e-6), Hessian = diag(3))      # the gradient is large in component 2 only
lme4:::checkConv(derivs, coefs = c(1, 1, 1), ctrl = ctrl, lbound = c(0, 0, 0))
cat("lme4", as.character(packageVersion("lme4")), "|", R.version.string, "\n")
