## checkConv() reports "component %d" in the max|grad| warning from which.max() applied to a
## scalar, so the component number is always 1 whichever gradient component is largest.
## Run:  Rscript note_checkconv_component.R   (library on R_LIBS_USER)
suppressPackageStartupMessages(library(lme4))
cat("lme4", as.character(packageVersion("lme4")), "from", dirname(system.file(package = "lme4")), "\n")
ctrl <- lmerControl()$checkConv
derivs <- list(gradient = c(1e-6, 0.5, 1e-6), Hessian = diag(3))
coefs <- c(1, 1, 1)
msg <- tryCatch(lme4:::checkConv(derivs, coefs, ctrl = ctrl, lbound = c(0, 0, 0)),
                warning = function(w) conditionMessage(w))
cat("gradient =", derivs$gradient, "-> largest is component", which.max(abs(derivs$gradient)), "\n")
cat("warning text:", strsplit(msg, "\n")[[1]][1], "\n")
## and on a real fit: perturb the optimum so that the second theta component carries the gradient
data(sleepstudy, package = "lme4")
fm <- lmer(Reaction ~ Days + (Days | Subject), sleepstudy)
dev <- getME(fm, "devfun")
th <- getME(fm, "theta"); th2 <- th; th2[2] <- th[2] + 0.2
dd <- lme4:::deriv12(dev, th2)
cat("perturbed theta gradient =", format(dd$gradient, digits = 3), "-> largest is component", which.max(abs(dd$gradient)), "\n")
msg2 <- tryCatch(lme4:::checkConv(dd, th2, ctrl = ctrl, lbound = c(0, -Inf, 0)),
                 warning = function(w) conditionMessage(w))
cat("warning text:", strsplit(msg2, "\n")[[1]][1], "\n")
