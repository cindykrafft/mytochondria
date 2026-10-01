import re, json, html
BATCHES=['afni-a','afni-b','freesurfer','fieldtrip','spm-macs-fastp','deeptools-suite2p','af3-kilosort-umap','deseq2-samtools-plink-cutadapt-iqtree','small']
def block(s, id_):
    m=re.search(r'<script[^>]*id="%s"[^>]*>(.*?)</script>'%id_, s, re.S)
    return json.loads(m.group(1)) if m else None
def login(c):
    for k in ('author','user','login'):
        v=c.get(k)
        if isinstance(v,dict): v=v.get('login')
        if isinstance(v,str) and v: return v
    return '?'
def key(y):
    md=y.get('metadata') or y.get('issue') or y.get('meta') or {}
    repo=y.get('repo') or md.get('repo'); num=y.get('number') or md.get('number')
    u=md.get('html_url') or md.get('url') or y.get('url') or ''
    m=re.search(r'github\.com/([^/]+/[^/]+)/(?:issues|pull)/(\d+)',u)
    if m: repo=repo or m.group(1); num=num or m.group(2)
    return repo, int(num) if num else None
def meta(y):
    md=dict(y.get('metadata') or y.get('issue') or y.get('meta') or {})
    for k in ('state','state_reason','closed_by','merged','merged_by','title','labels','assignees'):
        if k in y and k not in md: md[k]=y[k]
    if isinstance(y.get('pull'),dict):
        for k in ('merged','merged_by','merged_at'): md.setdefault(k,y['pull'].get(k))
    for k in ('closed_by','merged_by'):
        if isinstance(md.get(k),dict): md[k]=md[k].get('login')
    return md
def items(y):
    out=[]
    for k in ('comments','reviews','review_comments'):
        for c in y.get(k) or []:
            if isinstance(c,dict): out.append((login(c), c.get('body') or '', k, c.get('author_association') or c.get('association')))
    return out
def unreadable(y):
    return bool(y.get('fetch_error')) or y.get('readable') is False
def load(d, base):
    s=open(f'{base}/{d}/index.html', encoding='utf-8').read()
    led, thr = block(s,'ledger'), block(s,'threads')
    if isinstance(thr, dict):
        out=[]
        for k,v in thr.items():
            v=dict(v); m=re.match(r'(.+?)#(\d+)$',k)
            if m: v.setdefault('repo',m.group(1)); v.setdefault('number',int(m.group(2)))
            out.append(v)
        thr=out
    return led, thr
