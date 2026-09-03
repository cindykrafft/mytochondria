"""Property check for the #518 fix: on random reads with a planted adapter and
random pre-trimming (-u / -q / --nextseq-trim, optionally --revcomp, --times 2,
--action=retain, paired --info-file-paired, -j 2), the first info-file row of
every read must satisfy: columns 5-7 concatenate to the (possibly reverse-
complemented) original read, and column 6 equals the original read sliced at
columns 3-4, and an error-free match of the planted adapter must show a substring
of the adapter. Prints the number of rows checked per configuration."""
import random
import subprocess
import sys
import tempfile
from pathlib import Path

random.seed(518)
ADAPTER = "GATTACAGATTACA"
COMP = str.maketrans("ACGT", "TGCA")


def rc(s):
    return s.translate(COMP)[::-1]


def make_reads(n):
    reads = []
    for i in range(n):
        left = "".join(random.choice("ACGT") for _ in range(random.randint(5, 40)))
        right = "".join(random.choice("ACGT") for _ in range(random.randint(0, 20)))
        seq = left + ADAPTER + right
        qual = "".join(random.choice("#####IIIIIIIIIIIIII") for _ in seq)
        reads.append((f"r{i}", seq, qual))
    return reads


def check(label, args, paired=False, cores=1):
    reads = make_reads(300)
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        fq = "".join(f"@{n}\n{s}\n+\n{q}\n" for n, s, q in reads)
        (d / "in1.fastq").write_text(fq)
        cmd = [sys.executable, "-m", "cutadapt", "-j", str(cores), "--info-file", d / "info1.tsv",
               "-o", d / "out1.fastq", *args]
        if paired:
            (d / "in2.fastq").write_text(fq)
            cmd += ["--info-file-paired", d / "info2.tsv", "-p", d / "out2.fastq", "-A", "ad=" + ADAPTER,
                    d / "in1.fastq", d / "in2.fastq"]
        else:
            cmd += [d / "in1.fastq"]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        infos = [d / "info1.tsv"] + ([d / "info2.tsv"] if paired else [])
        original = {n: (s, q) for n, s, q in reads}
        checked = bad = 0
        verified = [0]
        for info in infos:
            seen = set()
            for line in info.read_text().splitlines():
                f = line.split("\t")
                name = f[0].replace(" rc", "")
                if f[1] == "-1" or name in seen:
                    continue  # no match, or a later --times row
                seen.add(name)
                seq, qual = original[name]
                if f[-1] == "1":
                    seq, qual = rc(seq), qual[::-1]
                rstart, rstop = int(f[2]), int(f[3])
                ok = (f[4] + f[5] + f[6] == seq and f[8] + f[9] + f[10] == qual
                      and f[5] == seq[rstart:rstop] and f[9] == qual[rstart:rstop])
                # an error-free match of the adapter named "ad" must show a
                # substring of the adapter (the whole adapter unless the
                # pre-trimming cut into it, then a prefix or suffix of it)
                if f[7] == "ad" and f[1] == "0":
                    ok = ok and f[5] in ADAPTER
                    verified[0] += 1
                if not ok and bad == 0:
                    print("   first wrong row:", line)
                checked += 1
                bad += not ok
        print(f"{label:55s} rows checked: {checked:4d} (against planted adapter: {verified[0]:4d})  wrong: {bad}")
        return bad


total = 0
total += check("-u 7 -a", ["-u", "7", "-a", "ad=" + ADAPTER])
total += check("-u 7 -u -4 -a", ["-u", "7", "-u", "-4", "-a", "ad=" + ADAPTER])
total += check("-q 20,20 -a", ["-q", "20,20", "-a", "ad=" + ADAPTER])
total += check("-u 3 -q 20 --nextseq-trim 20 -a", ["-u", "3", "-q", "20", "--nextseq-trim", "20", "-a", "ad=" + ADAPTER])
total += check("-u 7 -q 20,20 --revcomp -a", ["-u", "7", "-q", "20,20", "--revcomp", "-a", "ad=" + ADAPTER])
total += check("-u 7 -q 20,20 --times 2 -a -a", ["-u", "7", "-q", "20,20", "--times", "2", "-a", "ad=" + ADAPTER, "-a", "ad2=TTTTT"])
total += check("-u 7 -q 20,20 --action=retain -a", ["-u", "7", "-q", "20,20", "--action=retain", "-a", "ad=" + ADAPTER])
total += check("-u 7 -q 20,20 -g (5' adapter)", ["-u", "7", "-q", "20,20", "-g", "ad=" + ADAPTER])
total += check("-u 7 -q 20,20 linked -a ^X...Y", ["-u", "7", "-q", "20,20", "-a", "ad=^GATTACA...TTTTTTTTTT"])
total += check("-u 7 -q 20,20 -j 2 -a", ["-u", "7", "-q", "20,20", "-a", "ad=" + ADAPTER], cores=2)
total += check("paired -u 7 -U 5 -q 20,20 -a/-A --info-file-paired", ["-u", "7", "-U", "5", "-q", "20,20", "-a", "ad=" + ADAPTER], paired=True)
print("all rows consistent" if total == 0 else f"{total} inconsistent rows")
