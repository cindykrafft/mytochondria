## glmer.nb() against an exact marginal likelihood (adaptive Gauss-Hermite, 40 nodes,
## certified with integrate()) maximised over (beta, log sigma, log theta).
##
## Run:  Rscript heldup_glmer_nb.R   (library on R_LIBS_USER)
suppressPackageStartupMessages({library(lme4); library(statmod)})
cat("lme4", as.character(packageVersion("lme4")), "from", dirname(system.file(package = "lme4")), "\n\n")
options(digits = 10, width = 130)
f10 <- function(x) format(x, digits = 10)
gq40 <- gauss.quad.prob(40, dist = "normal")
lse <- function(v) { m <- max(v); m + log(sum(exp(v - m))) }

set.seed(51)
J <- 40; nj <- 8; theta.true <- 2
g <- gl(J, nj); x <- rnorm(J * nj); b <- rnorm(J, sd = 0.8)
mu <- exp(0.5 + 0.6 * x + b[g])
y <- rnbinom(J * nj, mu = mu, size = theta.true)
d <- data.frame(y, x, g); X <- cbind(1, x); cl <- split(seq_along(y), g)

cl_logdens <- function(bvec, sig, eta0, yj, th) {
    eta <- outer(eta0, sig * bvec, "+")
    v <- colSums(matrix(dnbinom(yj, mu = exp(eta), size = th, log = TRUE), nrow = length(yj)))
    v[!is.finite(v)] <- -1e300; v
}
exact_ll <- function(par, method = "agh") {
    beta <- par[1:2]; sig <- exp(par[3]); th <- exp(par[4])
    eta0 <- drop(X %*% beta); ll <- 0
    for (j in cl) {
        f <- function(bb) cl_logdens(bb, sig, eta0[j], y[j], th) + dnorm(bb, log = TRUE)
        b0 <- optimize(function(bb) -f(bb), c(-12, 12), tol = 1e-9)$minimum
        c0 <- f(b0); eps <- 1e-3; h2 <- (f(b0 + eps) - 2 * c0 + f(b0 - eps)) / eps^2
        s <- if (is.finite(h2) && h2 < 0) 1 / sqrt(-h2) else 1
        ll <- ll + if (method == "agh") {
            c0 + log(s) + lse(f(b0 + s * gq40$nodes) - c0 - dnorm(gq40$nodes, log = TRUE) + log(gq40$weights))
        } else {
            gfun <- function(t) exp(f(b0 + s * t) - c0)
            c0 + log(s) + log(sum(vapply(list(c(-12, -2), c(-2, 2), c(2, 12)),
                                         function(r) integrate(gfun, r[1], r[2], rel.tol = 1e-10, subdivisions = 500L)$value, 0)))
        }
    }
    if (is.finite(ll)) ll else -1e10
}
o <- optim(c(0.5, 0.6, log(0.8), log(2)), function(p) -exact_ll(p), method = "BFGS", control = list(reltol = 1e-13, maxit = 500))
o <- optim(o$par, function(p) -exact_ll(p), method = "Nelder-Mead", control = list(reltol = 1e-14, maxit = 3000))
cat(sprintf("exact ML: logLik %s (AGH-40) | integrate() %s\n          beta %s ; sd(RE) %s ; theta %s\n", f10(-o$value), f10(exact_ll(o$par, "integrate")),
            paste(f10(o$par[1:2]), collapse = " "), f10(exp(o$par[3])), f10(exp(o$par[4]))))
fit <- glmer.nb(y ~ x + (1 | g), d)
vc <- as.data.frame(VarCorr(fit)); th.hat <- getME(fit, "glmer.nb.theta")
cat(sprintf("glmer.nb: logLik %s (exact max %+.4f) ; beta %s ; sd(RE) %s ; theta %s ; SE(beta) %s\n", f10(as.numeric(logLik(fit))),
            as.numeric(logLik(fit)) + o$value, paste(f10(fixef(fit)), collapse = " "), f10(vc$sdcor[1]), f10(th.hat),
            paste(f10(sqrt(diag(as.matrix(vcov(fit))))), collapse = " ")))
cat("exact logLik at the glmer.nb estimates:", f10(exact_ll(c(fixef(fit), log(vc$sdcor[1]), log(th.hat)), "integrate")), "\n")
cat("logLik df =", attr(logLik(fit), "df"), "(2 fixed + 1 theta + NB dispersion expected: 4)\n")
cat("\ndone\n")
