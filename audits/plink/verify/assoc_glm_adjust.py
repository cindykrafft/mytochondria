#!/usr/bin/env python3
"""Association tests and --adjust on both binaries against scipy / statsmodels.

Part A  case/control: plink 1.9 --assoc (allelic chi-square, OR) and --assoc fisher,
        --model (GENO/TREND/ALLELIC/DOM/REC), --logistic; plink2 --glm (logistic,
        firth-fallback off) — Wald z / p vs statsmodels Logit, Fisher vs exact.
Part B  quantitative: plink 1.9 --assoc (t on beta), --linear with covariates;
        plink2 --glm with covariates — beta, SE, t, p vs statsmodels OLS.
Part C  --adjust: every column vs statsmodels.stats.multitest.multipletests /
        closed forms on the unadjusted p-values, both versions; the GC lambda;
        and PL-A: plink 1.9's GC column under --linear/quantitative --assoc when
        the residual df differ between variants (missing genotypes).
"""
import os, sys, tempfile, math
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from synth import simulate, write_pedmap, run, read_table, fnum, PLINK19, PLINK2, version
from exact_ref import fisher_p

rng = np.random.default_rng(2026)
n, m = 500, 200
g = simulate(n, m, rng, missing_rate=0.03)
obs = g >= 0
sex = rng.integers(1, 3, n)
cov = rng.normal(0, 1, n)
# case/control phenotype with 10 causal variants; quantitative trait with covariate effect
eta = -0.3 + 0.5 * (np.where(obs[:, :10], g[:, :10], 0).sum(1) - 5) * 0.4 + 0.3 * cov
cc = (rng.random(n) < 1 / (1 + np.exp(-eta))).astype(int)
qt = 0.4 * np.where(obs[:, 0], g[:, 0], 0) + 0.5 * cov + rng.normal(0, 1, n)

def snp_id(s): return int(s[3:]) - 1
print(version(PLINK19)); print(version(PLINK2))

with tempfile.TemporaryDirectory() as tmp:
    pre = write_pedmap(os.path.join(tmp, "cc"), g, pheno=cc + 1, sex=sex)
    covf = os.path.join(tmp, "cov.txt")
    with open(covf, "w") as f:
        f.write("FID IID cov1\n")
        for i in range(n): f.write(f"F{i+1} I{i+1} {cov[i]:.10g}\n")

    # ---------------- Part A: case/control
    # reference allelic chi-square (2x2 allele counts, no continuity correction), OR, Fisher on allele counts
    ref = {}
    for j in range(m):
        k = obs[:, j]
        x, y = g[k, j], cc[k]
        a1_case = int(x[y == 1].sum()); a2_case = int((2 - x[y == 1]).sum())
        a1_ctrl = int(x[y == 0].sum()); a2_ctrl = int((2 - x[y == 0]).sum())
        tab = np.array([[a1_case, a2_case], [a1_ctrl, a2_ctrl]], float)
        if tab.sum(0).min() == 0 or tab.sum(1).min() == 0:
            ref[j] = None; continue
        chi = stats.chi2_contingency(tab, correction=False)[0]
        odds = (a1_case * a2_ctrl) / (a2_case * a1_ctrl) if a2_case * a1_ctrl else float("nan")
        fp = float(fisher_p(a1_case, a2_case, a1_ctrl, a2_ctrl))
        # Cochran-Armitage trend (PLINK's "TREND" in --model): on genotype counts
        ct = np.array([[((x == d) & (y == 1)).sum() for d in (0, 1, 2)], [((x == d) & (y == 0)).sum() for d in (0, 1, 2)]], float)
        Nt = ct.sum(); R = ct[0].sum(); sc = np.array([0, 1, 2.]); C = ct.sum(0)
        T = (sc * (ct[0] * (Nt - R) - ct[1] * R)).sum()   # = N * sum s (r_i) - R * sum s c_i ... standard
        # standard CA statistic: T = sum s_i (r_i S - R c_i) / N? use textbook: chi = (N*sum s r - R*sum s c)^2 / (R(N-R)/N * (N sum s^2 c - (sum s c)^2))
        num = (Nt * (sc * ct[0]).sum() - R * (sc * C).sum()) ** 2
        den = (R * (Nt - R) / Nt) * (Nt * (sc ** 2 * C).sum() - (sc * C).sum() ** 2)
        trend = num / den if den > 0 else float("nan")
        # genotypic 2x3 chi-square (df = number of nonzero genotype columns - 1)
        nz = C > 0
        geno_chi = stats.chi2_contingency(ct[:, nz], correction=False)[0] if nz.sum() > 1 else float("nan")
        geno_df = int(nz.sum() - 1)
        # logistic Wald (additive, ALT count)
        X = sm.add_constant(x.astype(float))
        try:
            fit = sm.Logit(y, X).fit(disp=0, maxiter=200, tol=1e-10)
            lz = fit.tvalues[1]; lp = fit.pvalues[1]; lor = math.exp(fit.params[1])
        except Exception:
            lz = lp = lor = float("nan")
        # logistic with sex + cov1
        X2 = sm.add_constant(np.column_stack([x.astype(float), (sex[k] == 1).astype(float), cov[k]]))
        try:
            fit2 = sm.Logit(y, X2).fit(disp=0, maxiter=200, tol=1e-10)
            lz2, lp2, lor2 = fit2.tvalues[1], fit2.pvalues[1], math.exp(fit2.params[1])
        except Exception:
            lz2 = lp2 = lor2 = float("nan")
        ref[j] = dict(chi=chi, p=1 - stats.chi2.cdf(chi, 1), odds=odds, fisher=fp, trend=trend, trend_p=1 - stats.chi2.cdf(trend, 1),
                      geno=geno_chi, geno_df=geno_df, lz=lz, lp=lp, lor=lor, lz2=lz2, lp2=lp2, lor2=lor2)

    def cmp(label, ids, vals, key, transform=lambda v: v, rel=False):
        worst = 0.0; nn = 0
        for s, v in zip(ids, vals):
            j = snp_id(s); r = ref[j]
            if r is None or r[key] != r[key]: continue
            got = transform(fnum(v))
            if got != got: continue
            d = abs(got - r[key]) / (abs(r[key]) if rel else 1)
            worst = max(worst, d); nn += 1
        print(f"  {label:58s} n={nn:3d}  max {'rel ' if rel else ''}diff {worst:.2e}")

    run(PLINK19, ["--file", pre, "--assoc", "--out", os.path.join(tmp, "a19")])
    t = read_table(os.path.join(tmp, "a19.assoc"))
    print("A. plink 1.9 --assoc (allelic test; A1 = minor allele so OR may be inverted vs ALT):")
    cmp("CHISQ vs scipy 2x2 chi-square (no Yates)", t["SNP"], t["CHISQ"], "chi")
    cmp("P vs chi2 sf", t["SNP"], t["P"], "p", rel=True)
    # OR: plink reports for A1 (minor); compare min(OR,1/OR)
    worst = 0.0
    for s, v in zip(t["SNP"], t["OR"]):
        r = ref[snp_id(s)]
        if r and r["odds"] == r["odds"] and fnum(v) == fnum(v):
            worst = max(worst, min(abs(fnum(v) - r["odds"]), abs(1 / fnum(v) - r["odds"])))
    print(f"  {'OR vs allele-count odds ratio (either orientation)':58s}        max diff {worst:.2e}")
    run(PLINK19, ["--file", pre, "--assoc", "fisher", "--out", os.path.join(tmp, "a19f")])
    t = read_table(os.path.join(tmp, "a19f.assoc.fisher"))
    cmp("--assoc fisher P vs exact rational two-sided Fisher", t["SNP"], t["P"], "fisher", rel=True)
    run(PLINK19, ["--file", pre, "--model", "--out", os.path.join(tmp, "m19")])
    t = read_table(os.path.join(tmp, "m19.model"))
    rows = {(s, te): (c, p, df) for s, te, c, p, df in zip(t["SNP"], t["TEST"], t["CHISQ"], t["P"], t["DF"])}
    print("A. plink 1.9 --model:")
    cmp("TREND CHISQ vs Cochran-Armitage", [s for s, te in rows if te == "TREND"], [rows[(s, "TREND")][0] for s, te in rows if te == "TREND"], "trend")
    cmp("ALLELIC CHISQ vs 2x2 allele chi-square", [s for s, te in rows if te == "ALLELIC"], [rows[(s, "ALLELIC")][0] for s, te in rows if te == "ALLELIC"], "chi")
    cmp("GENO CHISQ vs 2x3 chi-square", [s for s, te in rows if te == "GENO"], [rows[(s, "GENO")][0] for s, te in rows if te == "GENO"], "geno")
    run(PLINK19, ["--file", pre, "--logistic", "--out", os.path.join(tmp, "l19")])
    t = read_table(os.path.join(tmp, "l19.assoc.logistic"))
    print("A. plink 1.9 --logistic (additive, no covariates) vs statsmodels Logit:")
    ids = [s for s, te in zip(t["SNP"], t["TEST"]) if te == "ADD"]
    for key, col, rel, tr in (("lz", "STAT", False, abs), ("lp", "P", True, lambda v: v), ("lor", "OR", True, lambda v: v)):
        vals = [v for v, te in zip(t[col], t["TEST"]) if te == "ADD"]
        if key == "lz":
            worst = max(abs(abs(fnum(v)) - abs(ref[snp_id(s)]["lz"])) for s, v in zip(ids, vals) if ref[snp_id(s)] and ref[snp_id(s)]["lz"] == ref[snp_id(s)]["lz"] and fnum(v) == fnum(v))
            print(f"  {'|STAT| vs |Wald z|':58s}        max diff {worst:.2e}")
        elif key == "lor":
            worst = max(min(abs(fnum(v) - ref[snp_id(s)]["lor"]), abs(1 / fnum(v) - ref[snp_id(s)]["lor"])) / ref[snp_id(s)]["lor"] for s, v in zip(ids, vals) if ref[snp_id(s)] and ref[snp_id(s)]["lor"] == ref[snp_id(s)]["lor"] and fnum(v) == fnum(v))
            print(f"  {'OR vs exp(beta) (either orientation)':58s}        max rel diff {worst:.2e}")
        else:
            cmp("P vs Wald p", ids, vals, "lp", rel=True)
    run(PLINK19, ["--file", pre, "--logistic", "sex", "--covar", covf, "--out", os.path.join(tmp, "l19c")])
    t = read_table(os.path.join(tmp, "l19c.assoc.logistic"))
    ids = [s for s, te in zip(t["SNP"], t["TEST"]) if te == "ADD"]
    vals = [v for v, te in zip(t["P"], t["TEST"]) if te == "ADD"]
    print("A. plink 1.9 --logistic sex --covar cov1:")
    cmp("P vs Wald p (Logit with sex + cov1)", ids, vals, "lp2", rel=True)
    # plink2 --glm
    run(PLINK2, ["--pedmap", pre, "--glm", "allow-no-covars", "no-firth", "omit-ref", "--out", os.path.join(tmp, "g2")])
    fn = [f for f in os.listdir(tmp) if f.startswith("g2.PHENO1.glm.logistic")][0]
    t = read_table(os.path.join(tmp, fn))
    print("A. plink2 --glm (logistic, no covariates, no-firth):")
    ids = [s for s, te in zip(t["ID"], t["TEST"]) if te == "ADD"]
    ps = [v for v, te in zip(t["P"], t["TEST"]) if te == "ADD"]
    zs = [v for v, te in zip(t["Z_STAT"], t["TEST"]) if te == "ADD"]
    cmp("P vs Wald p", ids, ps, "lp", rel=True)
    worst = max(abs(abs(fnum(v)) - abs(ref[snp_id(s)]["lz"])) for s, v in zip(ids, zs) if ref[snp_id(s)] and ref[snp_id(s)]["lz"] == ref[snp_id(s)]["lz"] and fnum(v) == fnum(v))
    print(f"  {'|Z_STAT| vs |Wald z|':58s}        max diff {worst:.2e}")
    run(PLINK2, ["--pedmap", pre, "--glm", "sex", "no-firth", "omit-ref", "hide-covar", "--covar", covf, "--out", os.path.join(tmp, "g2c")])
    fn = [f for f in os.listdir(tmp) if f.startswith("g2c.PHENO1.glm.logistic")][0]
    t = read_table(os.path.join(tmp, fn))
    ids = [s for s, te in zip(t["ID"], t["TEST"]) if te == "ADD"]
    ps = [v for v, te in zip(t["P"], t["TEST"]) if te == "ADD"]
    print("A. plink2 --glm sex --covar cov1 (logistic):")
    cmp("P vs Wald p (Logit with sex + cov1)", ids, ps, "lp2", rel=True)
    # Firth: compare against a reference Firth fit (Jeffreys-penalised Newton-Raphson port)
    def firth(y, X, maxit=200, tol=1e-10):
        b = np.zeros(X.shape[1])
        for _ in range(maxit):
            eta = X @ b; pi = 1 / (1 + np.exp(-eta)); W = pi * (1 - pi)
            XtW = X.T * W; I = XtW @ X
            H = (X * (np.linalg.solve(I, XtW)).T).sum(1) * W      # hat diagonal h_i = W_i x_i' I^-1 x_i
            U = X.T @ (y - pi + H * (0.5 - pi))
            step = np.linalg.solve(I, U)
            b = b + step
            if np.abs(step).max() < tol: break
        eta = X @ b; pi = 1 / (1 + np.exp(-eta)); I = (X.T * (pi * (1 - pi))) @ X
        se = np.sqrt(np.diag(np.linalg.inv(I)))
        return b, se
    run(PLINK2, ["--pedmap", pre, "--glm", "allow-no-covars", "firth", "omit-ref", "--out", os.path.join(tmp, "g2f")])
    fn = [f for f in os.listdir(tmp) if f.startswith("g2f.PHENO1.glm.")][0]
    t = read_table(os.path.join(tmp, fn))
    worst_b = worst_se = 0.0; nn = 0
    for s, te, o, se in zip(t["ID"], t["TEST"], t["OR"], t["LOG(OR)_SE"]):
        if te != "ADD": continue
        j = snp_id(s); k = obs[:, j]
        X = sm.add_constant(g[k, j].astype(float)); y = cc[k]
        if X[:, 1].std() == 0: continue
        b, ses = firth(y, X)
        if fnum(o) != fnum(o): continue
        worst_b = max(worst_b, abs(math.log(fnum(o)) - b[1])); worst_se = max(worst_se, abs(fnum(se) - ses[1])); nn += 1
    print(f"A. plink2 --glm firth vs Jeffreys-penalised Newton port: n={nn}, max |log OR diff| {worst_b:.2e}, max |SE diff| {worst_se:.2e}")

    # ---------------- Part B: quantitative
    preq = write_pedmap(os.path.join(tmp, "qt"), g, pheno=qt, sex=sex)
    refq = {}
    for j in range(m):
        k = obs[:, j]; x = g[k, j].astype(float)
        if x.std() == 0: refq[j] = None; continue
        f1 = sm.OLS(qt[k], sm.add_constant(x)).fit()
        f2 = sm.OLS(qt[k], sm.add_constant(np.column_stack([x, (sex[k] == 1).astype(float), cov[k]]))).fit()
        refq[j] = dict(beta=f1.params[1], se=f1.bse[1], t=f1.tvalues[1], p=f1.pvalues[1], df=int(f1.df_resid), r2=f1.rsquared,
                       beta2=f2.params[1], se2=f2.bse[1], t2=f2.tvalues[1], p2=f2.pvalues[1])
    ref = refq
    run(PLINK19, ["--file", preq, "--assoc", "--out", os.path.join(tmp, "q19")])
    t = read_table(os.path.join(tmp, "q19.qassoc"))
    print("B. plink 1.9 --assoc (quantitative) vs statsmodels OLS (A1 = minor allele; |t|, P, R2 compared):")
    worst = max(abs(abs(fnum(v)) - abs(ref[snp_id(s)]["t"])) for s, v in zip(t["SNP"], t["T"]) if ref[snp_id(s)] and fnum(v) == fnum(v))
    print(f"  {'|T| vs |t|':58s}        max diff {worst:.2e}")
    cmp("P vs OLS p", t["SNP"], t["P"], "p", rel=True)
    cmp("R2 vs OLS r-squared", t["SNP"], t["R2"], "r2")
    run(PLINK19, ["--file", preq, "--linear", "sex", "--covar", covf, "--out", os.path.join(tmp, "q19c")])
    t = read_table(os.path.join(tmp, "q19c.assoc.linear"))
    ids = [s for s, te in zip(t["SNP"], t["TEST"]) if te == "ADD"]
    print("B. plink 1.9 --linear sex --covar cov1:")
    cmp("P vs OLS p", ids, [v for v, te in zip(t["P"], t["TEST"]) if te == "ADD"], "p2", rel=True)
    run(PLINK2, ["--pedmap", preq, "--glm", "sex", "omit-ref", "hide-covar", "--covar", covf, "--out", os.path.join(tmp, "q2c")])
    fn = [f for f in os.listdir(tmp) if f.startswith("q2c.PHENO1.glm.linear")][0]
    t = read_table(os.path.join(tmp, fn))
    ids = [s for s, te in zip(t["ID"], t["TEST"]) if te == "ADD"]
    print("B. plink2 --glm sex --covar cov1 (linear; BETA/SE/T/P on the ALT allele):")
    cmp("BETA vs OLS beta", ids, [v for v, te in zip(t["BETA"], t["TEST"]) if te == "ADD"], "beta2")
    cmp("SE vs OLS se", ids, [v for v, te in zip(t["SE"], t["TEST"]) if te == "ADD"], "se2")
    cmp("P vs OLS p", ids, [v for v, te in zip(t["P"], t["TEST"]) if te == "ADD"], "p2", rel=True)

    # ---------------- Part C: --adjust
    def adjust_ref(pvals):
        p = np.asarray(pvals); mm = len(p); order = np.argsort(p, kind="stable"); ps = p[order]
        out = {"BONF": np.minimum(ps * mm, 1), "HOLM": multipletests(ps, method="holm")[1],
               "SIDAK_SS": 1 - (1 - ps) ** mm, "SIDAK_SD": multipletests(ps, method="holm-sidak")[1],
               "FDR_BH": multipletests(ps, method="fdr_bh")[1], "FDR_BY": multipletests(ps, method="fdr_by")[1]}
        return order, ps, out
    # plink2 --adjust on the logistic no-covariate run
    run(PLINK2, ["--pedmap", pre, "--glm", "allow-no-covars", "no-firth", "omit-ref", "--adjust", "cols=+qq", "--out", os.path.join(tmp, "adj2")])
    fn = [f for f in os.listdir(tmp) if f.startswith("adj2.PHENO1.glm.logistic") and not f.endswith(".adjusted")][0]
    t = read_table(os.path.join(tmp, fn))
    unadj = {s: fnum(p) for s, te, p in zip(t["ID"], t["TEST"], t["P"]) if te == "ADD" and fnum(p) == fnum(p)}
    ta = read_table(os.path.join(tmp, fn + ".adjusted"))
    ids = list(unadj); order, ps, refc = adjust_ref([unadj[s] for s in ids])
    sorted_ids = [ids[i] for i in order]
    print("C. plink2 --adjust vs statsmodels multipletests (logistic ADD p-values,", len(ids), "tests):")
    print(f"  row order matches sorted p: {ta['ID'] == sorted_ids}")
    for col in ("BONF", "HOLM", "SIDAK_SS", "SIDAK_SD", "FDR_BH", "FDR_BY"):
        worst = max(abs(fnum(v) - r) / r for v, r in zip(ta[col], refc[col]))
        print(f"  {col:9s} max rel diff {worst:.2e}")
    chis = np.array([stats.chi2.isf(unadj[s], 1) for s in ids])
    lam = np.median(chis) / 0.456
    lam_exact = np.median(chis) / stats.chi2.ppf(0.5, 1)
    gc_ref = stats.chi2.sf(np.sort(chis)[::-1] / max(lam, 1), 1)
    worst = max(abs(fnum(v) - r) / r for v, r in zip(ta["GC"], gc_ref))
    print(f"  GC column vs chi2.sf(chisq/lambda) with lambda=median/0.456: max rel diff {worst:.2e}  (lambda {lam:.4f}; with qchisq(0.5,1)=0.4549: {lam_exact:.4f})")
    qq_ref = (np.arange(len(ids)) + 0.5) / len(ids)
    print(f"  QQ column vs (i+0.5)/m: max diff {max(abs(fnum(v) - r) for v, r in zip(ta['QQ'], qq_ref)):.2e}")
    # plink 1.9 --adjust on --assoc (chi-square path) and on --linear (t path with varying df)
    run(PLINK19, ["--file", pre, "--assoc", "--adjust", "qq-plot", "--out", os.path.join(tmp, "adj19")])
    t = read_table(os.path.join(tmp, "adj19.assoc")); ta = read_table(os.path.join(tmp, "adj19.assoc.adjusted"))
    unadj = {s: fnum(p) for s, p in zip(t["SNP"], t["P"]) if fnum(p) == fnum(p)}
    ids = list(unadj); order, ps, refc = adjust_ref([unadj[s] for s in ids])
    print("C. plink 1.9 --assoc --adjust vs multipletests (", len(ids), "tests):")
    print(f"  row order matches sorted p: {ta['SNP'] == [ids[i] for i in order]}")
    for col in ("BONF", "HOLM", "SIDAK_SS", "SIDAK_SD", "FDR_BH", "FDR_BY"):
        worst = max(abs(fnum(v) - r) / r for v, r in zip(ta[col], refc[col]))
        print(f"  {col:9s} max rel diff {worst:.2e}")
    chis = np.array([unadj_c for unadj_c in (fnum(c) for c in t["CHISQ"]) if unadj_c == unadj_c])
    lam = np.median(chis) / 0.456
    gc_ref = stats.chi2.sf(np.sort(chis)[::-1] / max(lam, 1), 1)
    worst = max(abs(fnum(v) - r) / r for v, r in zip(ta["GC"], gc_ref))
    print(f"  GC column vs chi2.sf(chisq/lambda), lambda=median/0.456={lam:.4f}: max rel diff {worst:.2e}")
    # PL-A: --linear --adjust, GC column alignment when df differ (missing genotypes)
    for label, cmd, fn_assoc in (("--assoc (quantitative)", ["--assoc"], "adjq.qassoc"), ("--linear", ["--linear"], "adjl.assoc.linear")):
        outp = os.path.join(tmp, fn_assoc.split(".")[0])
        run(PLINK19, ["--file", preq, *cmd, "--adjust", "--out", outp])
        t = read_table(os.path.join(tmp, fn_assoc)); ta = read_table(os.path.join(tmp, fn_assoc + ".adjusted"))
        if "TEST" in t:
            keep = [te == "ADD" for te in t["TEST"]]
            t = {k: [v for v, kk in zip(vals, keep) if kk] for k, vals in t.items()}
        unadj = {s: fnum(p) for s, p in zip(t["SNP"], t["P"]) if fnum(p) == fnum(p)}
        tcol = "T" if "T" in t else "STAT"
        tstat = {s: fnum(v) for s, v in zip(t["SNP"], t[tcol])}
        nmiss = {s: int(v) for s, v in zip(t["SNP"], t["NMISS"])}
        ids = list(unadj)
        # lambda from the t^2 values (plink: median t^2 / 0.456); if lambda<1 -> 1, so GC should equal UNADJ
        chis = np.array([tstat[s] ** 2 for s in ids]); lam = np.median(chis) / 0.456
        print(f"C. plink 1.9 {label} --adjust: lambda = median(t^2)/0.456 = {lam:.4f} -> {'treated as 1: GC column should equal UNADJ' if lam < 1 else 'GC = p(t^2/lambda) with the ROW''S df'}")
        mism = 0; worst = 0.0; example = None
        for s, u, gcv in zip(ta["SNP"], ta["UNADJ"], ta["GC"]):
            k = 1 + (2 if "linear" in label else 1)      # predictors incl. intercept
            df = nmiss[s] - k
            expected = 2 * stats.t.sf(abs(tstat[s]) / math.sqrt(max(lam, 1)), df)
            d = abs(fnum(gcv) - expected) / expected
            worst = max(worst, d)
            if d > 1e-3:
                mism += 1
                if example is None: example = (s, u, gcv, f"{expected:.6g}", nmiss[s])
        print(f"  GC column vs p(t/sqrt(lambda), df of that row): {mism} of {len(ta['SNP'])} rows off by > 0.1%, max rel diff {worst:.2e}; example (SNP, UNADJ, GC, expected, NMISS) = {example}")
        # with --adjust gc, every downstream column is derived from the GC p-values
        run(PLINK19, ["--file", preq, *cmd, "--adjust", "gc", "--out", outp + "gc"])
        tg = read_table(os.path.join(tmp, fn_assoc.replace("adjq", "adjqgc").replace("adjl", "adjlgc") + ".adjusted"))
        bonf_from_row = [min(1.0, fnum(u) * len(tg["SNP"])) for u in tg["UNADJ"]]   # UNADJ is the unadjusted p of the row's SNP
        # with gc, BONF should be lambda-corrected p * m of the same row; when lambda<1 it equals UNADJ*m
        mism = sum(1 for b, r in zip(tg["BONF"], bonf_from_row) if abs(fnum(b) - r) / r > 1e-3)
        print(f"  --adjust gc: BONF vs min(1, UNADJ*m) of the same row (lambda<1 case): {mism} of {len(tg['SNP'])} rows differ by > 0.1%")
