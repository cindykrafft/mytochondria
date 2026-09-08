## Gamma GLMM (log link, estimated dispersion): glmer() against (a) the exact marginal
## likelihood (adaptive Gauss-Hermite centred on each cluster's conditional mode, certified
## with integrate()) and (b) an independent Laplace approximation evaluated at glmer's own
## estimates, so that the approximation error and any formula error in the reported
## log-likelihood are separated.
##
## Run:  Rscript gamma_glmm_loglik.R   (library on R_LIBS_USER)
suppressPackageStartupMessages({library(lme4); library(statmod)})
cat("lme4", as.character(packageVersion("lme4")), "from", dirname(system.file(package = "lme4")), "\n")
cat(R.version.string, "\n\n")
options(digits = 10, width = 130)
f10 <- function(x) format(x, digits = 10)
gq40 <- gauss.quad.prob(40, dist = "normal")
lse <- function(v) { m <- max(v); m + log(sum(exp(v - m))) }

set.seed(14)
J <- 40; nj <- 8; phi.true <- 0.25
g <- gl(J, nj); x <- rnorm(J * nj); b <- rnorm(J, sd = 0.7)
mu <- exp(1.0 + 0.5 * x + b[g])
y <- rgamma(J * nj, shape = 1 / phi.true, scale = mu * phi.true)
d <- data.frame(y, x, g); X <- cbind(1, x); n <- length(y)
cl <- split(seq_len(n), g)

cl_logdens <- function(bvec, sig, eta0, yj, phi) {     # sum_i log dgamma(y_ij | mu = exp(eta0_i + sig b)), vectorised in b
    eta <- outer(eta0, sig * bvec, "+")
    v <- colSums(matrix(suppressWarnings(dgamma(yj, shape = 1 / phi, scale = exp(eta) * phi, log = TRUE)), nrow = length(yj)))
    v[!is.finite(v)] <- -1e300; v
}
mode_scale <- function(f) {
    b0 <- optimize(function(b) -f(b), c(-12, 12), tol = 1e-9)$minimum
    c0 <- f(b0); eps <- 1e-3; h2 <- (f(b0 + eps) - 2 * c0 + f(b0 - eps)) / eps^2
    list(b0 = b0, c0 = c0, h2 = h2, s = if (is.finite(h2) && h2 < 0) 1 / sqrt(-h2) else 1)
}
exact_ll <- function(beta, sig, phi, method = "agh") {
    eta0 <- drop(X %*% beta); ll <- 0
    for (j in cl) {
        f <- function(bb) cl_logdens(bb, sig, eta0[j], y[j], phi) + dnorm(bb, log = TRUE)
        m <- mode_scale(f)
        ll <- ll + if (method == "agh") {
            m$c0 + log(m$s) + lse(f(m$b0 + m$s * gq40$nodes) - m$c0 - dnorm(gq40$nodes, log = TRUE) + log(gq40$weights))
        } else {
            gfun <- function(t) exp(f(m$b0 + m$s * t) - m$c0)
            m$c0 + log(m$s) + log(sum(vapply(list(c(-12, -2), c(-2, 2), c(2, 12)),
                                             function(r) integrate(gfun, r[1], r[2], rel.tol = 1e-10, subdivisions = 500L)$value, 0)))
        }
    }
    if (is.finite(ll)) ll else -1e10
}
## independent Laplace approximation: per cluster, log L_j ~= h(b*) + 0.5 log(2 pi) - 0.5 log(-h''(b*))
laplace_ll <- function(beta, sig, phi) {
    eta0 <- drop(X %*% beta); ll <- 0
    for (j in cl) {
        f <- function(bb) cl_logdens(bb, sig, eta0[j], y[j], phi) + dnorm(bb, log = TRUE)
        m <- mode_scale(f)
        ll <- ll + m$c0 + 0.5 * log(2 * pi) - 0.5 * log(-m$h2)
    }
    if (is.finite(ll)) ll else -1e10
}
nll <- function(p) -exact_ll(p[1:2], exp(p[3]), exp(p[4]))
o <- optim(c(1, 0.5, log(0.7), log(0.25)), nll, method = "BFGS", control = list(reltol = 1e-13, maxit = 500))
o <- optim(o$par, nll, method = "Nelder-Mead", control = list(reltol = 1e-14, maxit = 3000))
H <- optimHess(o$par, nll)
cat(sprintf("exact ML: logLik %s (AGH-40) | integrate() %s\n          beta %s ; sd(RE) %s ; phi %s ; SE(beta) %s\n", f10(-o$value),
            f10(exact_ll(o$par[1:2], exp(o$par[3]), exp(o$par[4]), method = "integrate")),
            paste(f10(o$par[1:2]), collapse = " "), f10(exp(o$par[3])), f10(exp(o$par[4])),
            paste(f10(sqrt(diag(solve(H)))[1:2]), collapse = " ")))
nll.lap <- function(p) -laplace_ll(p[1:2], exp(p[3]), exp(p[4]))
ol <- optim(o$par, nll.lap, method = "BFGS", control = list(reltol = 1e-10, maxit = 200))
cat(sprintf("independent Laplace ML: logLik %s ; beta %s ; sd(RE) %s ; phi %s\n", f10(-ol$value),
            paste(f10(ol$par[1:2]), collapse = " "), f10(exp(ol$par[3])), f10(exp(ol$par[4]))))

show <- function(label, fit) {
    vc <- as.data.frame(VarCorr(fit)); sd.re <- vc$sdcor[1]; phi <- sigma(fit)^2
    ex <- exact_ll(fixef(fit), sd.re, phi, method = "integrate"); la <- laplace_ll(fixef(fit), sd.re, phi)
    cat(sprintf("%s\n  beta %s ; sd(RE) %s ; sigma(fit)^2 %s ; SE(beta) %s\n", label,
                paste(f10(fixef(fit)), collapse = " "), f10(sd.re), f10(phi), paste(f10(sqrt(diag(as.matrix(vcov(fit))))), collapse = " ")))
    cat(sprintf("  logLik(fit) %s | exact logLik at these estimates %s (diff %+.4f) | independent Laplace at these estimates %s (diff %+.4f)\n",
                f10(as.numeric(logLik(fit))), f10(ex), as.numeric(logLik(fit)) - ex, f10(la), as.numeric(logLik(fit)) - la))
    dev <- sum(residuals(fit, type = "deviance")^2)
    cat(sprintf("  residual deviance %s ; deviance/n %s ; deviance/(n - rank[X,Z]) %s\n  devcomp$cmp: %s\n", f10(dev), f10(dev / n), f10(dev / (n - 2 - J)),
                paste(names(fit@devcomp$cmp), f10(fit@devcomp$cmp), collapse = " ")))
    invisible(NULL)
}
fit <- glmer(y ~ x + (1 | g), d, Gamma(link = "log"))
show("glmer(Gamma(log)) defaults", fit)
ctrl.args <- names(formals(glmerControl))
if ("disp_method" %in% ctrl.args)
    show("glmer(..., disp_method = 'old/buggy')", glmer(y ~ x + (1 | g), d, Gamma(link = "log"), control = glmerControl(disp_method = "old/buggy")))
if ("disp_dof_correction" %in% ctrl.args)
    show("glmer(..., disp_dof_correction = FALSE)", glmer(y ~ x + (1 | g), d, Gamma(link = "log"), control = glmerControl(disp_dof_correction = FALSE)))
## the pieces of the reported deviance on this version: -2 logLik = ldL2 + sqrL + aic (- 2 on master)
dev <- sum(residuals(fit, "deviance")^2)
cat("\nGamma()$aic at the reported mu with dispersion = deviance/n (base R convention, includes +2):",
    f10(Gamma()$aic(y, rep(1, n), fitted(fit), rep(1, n), dev)), "\n")
cat("-2 sum log dgamma(y | mu, phi = sigma(fit)^2):", f10(-2 * sum(dgamma(y, shape = 1 / sigma(fit)^2, scale = fitted(fit) * sigma(fit)^2, log = TRUE))), "\n")
ph <- dev / n
cat("-2 sum log dgamma(y | mu, phi = deviance/n):", f10(-2 * sum(dgamma(y, shape = 1 / ph, scale = fitted(fit) * ph, log = TRUE))), "\n")
cat("ldL2 + sqrL from the fit:", f10(fit@devcomp$cmp[["ldL2"]] + fit@devcomp$cmp[["ussq"]]), "; -2 logLik(fit):", f10(-2 * as.numeric(logLik(fit))), "\n")
cat("\ndone\n")
