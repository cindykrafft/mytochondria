#!/usr/bin/env python3
"""Run every FieldTrip test function marked `% DATA no` under GNU Octave and record the outcome.

Offered to the FieldTrip maintainers on issue #2614 (2026-09-07) and accepted on 2026-09-16
("the proof of the pudding is in the eating"): a point estimate of how much of the test suite
runs on a recent Octave, for the Octave FAQ page.

Each test runs in its own Octave process (so one crash cannot take the others down) with a
time limit derived from the test's own `% WALLTIME` header, the shims used for the #2608 and
#2610 test runs on the path, figures invisible and warnings off. Results go to a TSV, one row
per test, and the run can be resumed: tests already in the TSV are skipped.

    octave_survey.py --fieldtrip /path/to/fieldtrip --shims /path/to/shims --out survey.tsv
                     [--workers 3] [--only REGEX] [--cap-minutes 30] [--list]

Outcome column: PASS | FAIL | TIMEOUT | CRASH (Octave exited without printing a result).
The message column keeps the first 300 characters of the error message and, when the stack
is available, the file and line where it was raised.
"""
import argparse, concurrent.futures, os, re, subprocess, sys, tempfile, time

HEADER = "test\toutcome\tseconds\twalltime\tmem\tmessage\n"


def parse_header(path):
    h = {"data": None, "walltime": None, "mem": None}
    with open(path, errors="replace") as f:
        for i, line in enumerate(f):
            if i > 40:
                break
            m = re.match(r"^%\s*(DATA|WALLTIME|MEM)\s+(.*?)\s*$", line, re.I)
            if m:
                h[m.group(1).lower()] = m.group(2)
    return h


def walltime_seconds(s):
    if not s:
        return 600
    m = re.match(r"(\d+):(\d+):(\d+)", s)
    if not m:
        return 600
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))


def run_one(name, ft, shims, limit, tmpdir):
    wrapper = os.path.join(tmpdir, name + "_run.m")
    with open(wrapper, "w") as f:
        f.write(
            "pkg load statistics signal\n"
            f"addpath('{ft}'); ft_defaults; addpath('{ft}/test'); "
            f"addpath('{ft}/external/signal/dpss_hack'); addpath('{shims}');\n"
            "warning('off','all'); set(0,'DefaultFigureVisible','off'); more off;\n"
            "try\n"
            f"  {name};\n"
            "  printf('\\nRESULT PASS\\n');\n"
            "catch e\n"
            "  msg = strrep(strtrim(e.message), char(10), ' ');\n"
            "  printf('\\nRESULT FAIL: %s\\n', msg(1:min(end,300)));\n"
            "  if ~isempty(e.stack), printf('RESULT AT %s:%d\\n', e.stack(1).file, e.stack(1).line); end\n"
            "end\n"
            "exit(0);\n"
        )
    t0 = time.time()
    try:
        p = subprocess.run(["octave", "--no-gui", "--quiet", "--eval", f"run('{wrapper}')"],
                           capture_output=True, text=True, timeout=limit, cwd=tmpdir,
                           env=dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1"))
        out = p.stdout + "\n" + p.stderr
        dt = time.time() - t0
        m = re.search(r"^RESULT (PASS|FAIL: .*)$", out, re.M)
        if not m:
            tail = " ".join(out.strip().splitlines()[-3:])[-300:]
            return "CRASH", dt, f"exit {p.returncode}: {tail}"
        if m.group(1) == "PASS":
            return "PASS", dt, ""
        at = re.search(r"^RESULT AT (.*)$", out, re.M)
        msg = m.group(1)[6:]
        if at:
            msg += " @ " + os.path.relpath(at.group(1).split(":")[0], ft) + ":" + at.group(1).rsplit(":", 1)[-1]
        return "FAIL", dt, msg
    except subprocess.TimeoutExpired:
        return "TIMEOUT", time.time() - t0, f"limit {limit}s"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fieldtrip", required=True)
    ap.add_argument("--shims", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--only", default=None, help="regex on the test name")
    ap.add_argument("--cap-minutes", type=float, default=30)
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    ft = os.path.abspath(a.fieldtrip)
    tests = []
    for fn in sorted(os.listdir(os.path.join(ft, "test"))):
        if not (fn.startswith("test_") and fn.endswith(".m")):
            continue
        h = parse_header(os.path.join(ft, "test", fn))
        if not h["data"] or h["data"].strip().lower() != "no":
            continue
        name = fn[:-2]
        if a.only and not re.search(a.only, name):
            continue
        tests.append((name, h))
    if a.list:
        for name, h in tests:
            print(name, h["walltime"], h["mem"])
        print(len(tests), "tests")
        return
    done = set()
    if os.path.exists(a.out):
        for line in open(a.out):
            if line and not line.startswith("test\t"):
                done.add(line.split("\t")[0])
    else:
        open(a.out, "w").write(HEADER)
    todo = [(n, h) for n, h in tests if n not in done]
    print(f"{len(tests)} DATA-no tests, {len(done)} done, {len(todo)} to run, {a.workers} workers", flush=True)
    tmpdir = tempfile.mkdtemp(prefix="ftsurvey_")
    lock = __import__("threading").Lock()

    def job(item):
        name, h = item
        limit = min(max(2 * walltime_seconds(h["walltime"]), 120), a.cap_minutes * 60)
        outcome, dt, msg = run_one(name, ft, os.path.abspath(a.shims), limit, tmpdir)
        row = f"{name}\t{outcome}\t{dt:.0f}\t{h['walltime'] or ''}\t{h['mem'] or ''}\t{msg}\n"
        with lock:
            open(a.out, "a").write(row)
            print(row.rstrip()[:200], flush=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as ex:
        list(ex.map(job, todo))
    rows = [l.rstrip("\n").split("\t") for l in open(a.out) if not l.startswith("test\t")]
    from collections import Counter
    c = Counter(r[1] for r in rows)
    print("summary:", dict(c), flush=True)


if __name__ == "__main__":
    main()
