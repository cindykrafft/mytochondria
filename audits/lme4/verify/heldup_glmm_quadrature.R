## glmer() against an exact marginal likelihood for random-intercept GLMMs.
## The one-dimensional integral over each cluster's random intercept is done by my own
## adaptive Gauss-Hermite rule (40 nodes centred at the conditional mode and scaled by the
## conditional curvature; statmod supplies the nodes), and the values that matter are
## certified with R's adaptive integrate() (three pieces on the mode-scaled axis, rel.tol
## 1e-10). The exact log-likelihood is maximised directly with optim().
##
## Run:  Rscript heldup_glmm_quadrature.R   (library on R_LIBS_USER)
suppressPackageStartupMessages({library(lme4); library(statmod)})
cat("lme4", as.character(packageVersion("lme4")), "from", dirname(system.file(package = "lme4")), "\n")
cat(R.version.string, "\n\n")
options(digits = 10, width = 130)
f10 <- function(x) format(x, digits = 10)
gq40 <- gauss.quad.prob(40, dist = "normal")
gq100 <- gauss.quad.prob(100, dist = "normal")
lse <- function(v) { m <- max(v); m + log(sum(exp(v - m))) }

## per-cluster log p(y_j | b) with b in standard-normal units (eta = eta0 + sig * b); vectorised in b
cl_logdens <- function(b, sig, eta0, yj, family, sizej = NULL, phi = NULL) {
    eta <- outer(eta0, sig * b, "+")
    ld <- switch(family,
                 bernoulli = dbinom(yj, 1, plogis(eta), log = TRUE),
                 binomial  = dbinom(yj, sizej, plogis(eta), log = TRUE),
                 poisson   = dpois(yj, exp(eta), log = TRUE),
                 gamma     = suppressWarnings(dgamma(yj, shape = 1 / phi, scale = exp(eta) * phi, log = TRUE)))
    v <- colSums(matrix(ld, nrow = length(yj)))
    v[!is.finite(v)] <- -1e300
    v
}
## log integral of exp(f(b)) db, f = log p(y_j|b) + log dnorm(b), by adaptive GH or integrate()
cl_logint <- function(f, method) {
    b0 <- optimize(function(b) -f(b), c(-12, 12), tol = 1e-9)$minimum
    c0 <- f(b0); eps <- 1e-3
    h2 <- (f(b0 + eps) - 2 * c0 + f(b0 - eps)) / eps^2
    s <- if (is.finite(h2) && h2 < 0) 1 / sqrt(-h2) else 1
    if (method == "agh")
        return(c0 + log(s) + lse(f(b0 + s * gq40$nodes) - c0 - dnorm(gq40$nodes, log = TRUE) + log(gq40$weights)))
    if (method == "gh100")            # plain (non-adaptive) 100-point rule, for the record
        return(lse(f(gq100$nodes) - dnorm(gq100$nodes, log = TRUE) + log(gq100$weights)))
    g <- function(t) exp(f(b0 + s * t) - c0)
    val <- sum(vapply(list(c(-12, -2), c(-2, 2), c(2, 12)),
                      function(r) integrate(g, r[1], r[2], rel.tol = 1e-10, subdivisions = 500L)$value, 0))
    c0 + log(s) + log(val)
}
exact_ll <- function(par, y, X, g, family, size = NULL, method = "agh") {
    p <- ncol(X); beta <- par[1:p]; sig <- exp(par[p + 1])
    phi <- if (family == "gamma") exp(par[p + 2]) else NULL
    eta0 <- drop(X %*% beta); ll <- 0
    for (j in split(seq_along(y), g)) {
        f <- function(b) cl_logdens(b, sig, eta0[j], y[j], family, size[j], phi) + dnorm(b, log = TRUE)
        ll <- ll + cl_logint(f, method)
    }
    if (!is.finite(ll)) -1e10 else ll
}
maximise <- function(start, ...) {
    best <- NULL
    for (s in list(start, start + 0.3)) {
        o <- optim(s, function(p) -exact_ll(p, ...), method = "BFGS", control = list(reltol = 1e-13, maxit = 500))
        o <- optim(o$par, function(p) -exact_ll(p, ...), method = "Nelder-Mead", control = list(reltol = 1e-14, maxit = 3000))
        if (is.null(best) || o$value < best$value) best <- o
    }
    best
}
report <- function(fits, best, ...) {
    cat(sprintf("  exact maximum: logLik %s (AGH-40) | certified by integrate(): %s | plain GH-100: %s\n", f10(-best$value),
                f10(exact_ll(best$par, ..., method = "integrate")), f10(exact_ll(best$par, ..., method = "gh100"))))
    cat(sprintf("                 beta %s ; sd(RE) %s\n", paste(f10(best$par[1:2]), collapse = " "), f10(exp(best$par[3]))))
    for (nm in names(fits)) {
        f <- fits[[nm]]
        vc <- as.data.frame(VarCorr(f))
        par.f <- c(fixef(f), log(vc$sdcor[1]))
        cat(sprintf("  %-8s logLik %s (exact max %+.3e) ; beta %s ; sd(RE) %s ; SE(beta) %s\n           exact logLik at these estimates (integrate) %s\n", nm,
                    f10(as.numeric(logLik(f))), as.numeric(logLik(f)) + best$value,
                    paste(f10(fixef(f)), collapse = " "), f10(vc$sdcor[1]),
                    paste(f10(sqrt(diag(as.matrix(vcov(f))))), collapse = " "), f10(exact_ll(par.f, ..., method = "integrate"))))
    }
}

## ---------------------------------------------------------------- Bernoulli
set.seed(11)
J <- 40; nj <- 8
g <- gl(J, nj); x <- rnorm(J * nj); b <- rnorm(J, sd = 1.2)
eta <- -0.5 + 1.0 * x + b[g]
y <- rbinom(J * nj, 1, plogis(eta))
d <- data.frame(y, x, g)
X <- cbind(1, x)
best <- maximise(c(-0.5, 1, log(1.2)), y = y, X = X, g = g, family = "bernoulli")
fits <- list(Laplace = glmer(y ~ x + (1 | g), d, binomial),
             nAGQ25  = glmer(y ~ x + (1 | g), d, binomial, nAGQ = 25))
cat("Bernoulli random intercept, J =", J, "clusters x", nj, "\n"); report(fits, best, y = y, X = X, g = g, family = "bernoulli")
H <- optimHess(best$par, function(p) -exact_ll(p, y = y, X = X, g = g, family = "bernoulli"))
cat("  exact-likelihood SE(beta) from the observed information:", f10(sqrt(diag(solve(H)))[1:2]), "\n")
cat("  nAGQ=25 vcov(use.hessian=FALSE) SE:", f10(sqrt(diag(as.matrix(suppressWarnings(vcov(fits$nAGQ25, use.hessian = FALSE)))))), "\n")

## ---------------------------------------------------------------- binomial with size > 1 (normalising constants)
set.seed(12)
size <- sample(5:15, J * nj, replace = TRUE)
y2 <- rbinom(J * nj, size, plogis(eta))
d2 <- data.frame(y2, size, x, g)
best2 <- maximise(c(-0.5, 1, log(1.2)), y = y2, X = X, g = g, family = "binomial", size = size)
fits2 <- list(Laplace = glmer(cbind(y2, size - y2) ~ x + (1 | g), d2, binomial),
              nAGQ25  = glmer(cbind(y2, size - y2) ~ x + (1 | g), d2, binomial, nAGQ = 25))
cat("\nBinomial (sizes 5-15) random intercept\n"); report(fits2, best2, y = y2, X = X, g = g, family = "binomial", size = size)
cat("  saturated binomial log-likelihood, sum(dbinom(y, size, y/size, log)) =", f10(sum(dbinom(y2, size, y2 / size, log = TRUE))), "\n")

## ---------------------------------------------------------------- Poisson
set.seed(13)
y3 <- rpois(J * nj, exp(0.3 + 0.5 * x + 0.8 * b[g] / 1.2))
d3 <- data.frame(y3, x, g)
best3 <- maximise(c(0.3, 0.5, log(0.8)), y = y3, X = X, g = g, family = "poisson")
fits3 <- list(Laplace = glmer(y3 ~ x + (1 | g), d3, poisson),
              nAGQ25  = glmer(y3 ~ x + (1 | g), d3, poisson, nAGQ = 25))
cat("\nPoisson random intercept\n"); report(fits3, best3, y = y3, X = X, g = g, family = "poisson")
cat("  saturated Poisson log-likelihood, sum(dpois(y, y, log)) =", f10(sum(dpois(y3, y3, log = TRUE))), "\n")
cat("\ndone\n")
