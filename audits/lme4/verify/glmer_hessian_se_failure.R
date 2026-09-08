## How often does the default glmer() standard error (finite-difference Hessian of the
## Laplace deviance, delta = 1e-4) come out far from the RX-based one on ordinary,
## well-specified Bernoulli random-intercept data, as a function of the number of
## observations? And is the mechanism the PIRLS-truncation noise in the deviance?
##
## Run:  Rscript glmer_hessian_se_failure.R   (library on R_LIBS_USER)
suppressPackageStartupMessages(library(lme4))
cat("lme4", as.character(packageVersion("lme4")), "from", dirname(system.file(package = "lme4")), "\n\n")
options(digits = 5, width = 130)
mk <- function(J, nj, sd.b = 1.2, beta = c(-0.5, 1)) {
    g <- gl(J, nj); x <- rnorm(J * nj); b <- rnorm(J, sd = sd.b)
    data.frame(y = rbinom(J * nj, 1, plogis(beta[1] + beta[2] * x + b[g])), x, g)
}
fit1 <- function(d) {
    w <- character(0)
    f <- withCallingHandlers(suppressMessages(glmer(y ~ x + (1 | g), d, binomial)),
                             warning = function(cnd) { w <<- c(w, conditionMessage(cnd)); invokeRestart("muffleWarning") })
    list(fit = f, warn = w)
}
set.seed(31)
R <- 25
cat(sprintf("%d replicates per size; Bernoulli y ~ x + (1|g), 10 obs per cluster, sd(RE) = 1.2, beta = (-0.5, 1)\n", R))
cat(sprintf("%-6s %-6s %-9s %-9s %-9s %-9s %-9s %-9s\n", "nobs", "hess", "med.ratio", "ratio<0.5", "ratio>2", "any.warn", "bad&warn", "bad&nowarn"))
bad.cases <- list()
for (J in c(20, 50, 100, 250, 500, 999, 1001)) {
    rat <- rep(NA_real_, R); warn <- logical(R); hess <- logical(R)
    for (r in seq_len(R)) {
        d <- mk(J, 10)
        o <- fit1(d); f <- o$fit
        hess[r] <- !is.null(f@optinfo$derivs$Hessian)
        warn[r] <- length(o$warn) > 0
        if (hess[r]) {
            se.h <- sqrt(diag(as.matrix(suppressWarnings(vcov(f, use.hessian = TRUE)))))
            se.r <- sqrt(diag(as.matrix(suppressWarnings(vcov(f, use.hessian = FALSE)))))
            se.d <- sqrt(diag(as.matrix(suppressWarnings(vcov(f)))))          # what summary() reports
            rat[r] <- se.h[1] / se.r[1]
            if (is.na(rat[r]) || rat[r] < 0.5 || rat[r] > 2)
                bad.cases[[length(bad.cases) + 1]] <- data.frame(
                    nobs = J * 10, rep = r, beta0 = fixef(f)[[1]], SE_default = se.d[1], SE_hess = se.h[1], SE_RX = se.r[1],
                    z_default = fixef(f)[[1]] / se.d[1], z_RX = fixef(f)[[1]] / se.r[1],
                    warning = if (length(o$warn)) sub("\n.*", "", o$warn[1]) else "none")
        }
    }
    bad <- !is.na(rat) & (rat < 0.5 | rat > 2)
    cat(sprintf("%-6d %-6d %-9.3f %-9d %-9d %-9d %-9d %-9d\n", J * 10, sum(hess), median(rat, na.rm = TRUE),
                sum(rat < 0.5, na.rm = TRUE), sum(rat > 2, na.rm = TRUE), sum(warn), sum(bad & warn), sum(bad & !warn)))
}
cat("\nThe replicates with SE_hess/SE_RX outside [0.5, 2] (SE_default is what summary() prints):\n")
print(do.call(rbind, bad.cases), row.names = FALSE, digits = 4)

## mechanism: the deviance returned by the PIRLS-based devfun is only accurate to ~tolPwrss * deviance,
## and the Hessian divides second differences by delta^2 = 1e-8
cat("\nMechanism on one nobs = 9990 replicate: second differences of the deviance at the optimum\n")
set.seed(32)
d <- mk(999, 10); o <- fit1(d); f <- o$fit
cat("  convergence warnings:", if (length(o$warn)) paste(sub("\n.*", "", o$warn), collapse = " | ") else "none", "\n")
dev <- getME(f, "devfun"); p0 <- unname(getME(f, "devarg")); f0 <- dev(p0)
cat(sprintf("  deviance at optimum %.6f ; nobs %d\n", f0, nobs(f)))
for (delta in c(1e-4, 1e-3, 1e-2, 5e-2)) {
    dd <- lme4:::deriv12(dev, p0, delta = delta, fx = f0)
    Vh <- tryCatch(2 * solve(dd$Hessian), error = function(e) NULL)
    se <- if (is.null(Vh)) rep(NA, 3) else sqrt(pmax(diag(Vh), 0))[-1]
    cat(sprintf("  delta = %-6g Hessian diag (theta, b0, b1) = %10.2f %10.2f %10.2f -> SE(beta) %s\n",
                delta, dd$Hessian[1, 1], dd$Hessian[2, 2], dd$Hessian[3, 3], paste(format(se, digits = 4), collapse = " ")))
}
se.r <- sqrt(diag(as.matrix(suppressWarnings(vcov(f, use.hessian = FALSE)))))
cat("  RX-based SE(beta):", format(se.r, digits = 4), "\n")
cat("  repeated evaluations of the deviance at the optimum (should be identical):",
    format(vapply(1:4, function(i) dev(p0), 0) - f0, digits = 3), "\n")
cat("  deviance at optimum +/- 1e-4 in beta0:", format(c(dev(p0 + c(0, 1e-4, 0)), dev(p0 - c(0, 1e-4, 0))) - f0, digits = 6),
    "| expected from RX curvature:", format(1e-8 / se.r[1]^2, digits = 3), "\n")
cat("\ndone\n")
