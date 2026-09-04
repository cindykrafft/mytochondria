"""Index ERP CORE raw .set/.fdt files on OSF for a paradigm node -> TSV (subject, name, size, url)."""
import json, sys, urllib.request, re
node, tag = sys.argv[1], sys.argv[2]
def get(url):
    out=[]
    while url:
        d=json.load(urllib.request.urlopen(url, timeout=60)); out+=d['data']; url=d['links'].get('next')
    return out
top = get(f'https://api.osf.io/v2/nodes/{node}/files/osfstorage/')
raw = [f for f in top if 'Raw Data and Scripts Only' in f['attributes']['name']]
if not raw: print('top-level:', [f['attributes']['name'] for f in top]); sys.exit(1)
subs = get(raw[0]['relationships']['files']['links']['related']['href'])
rows=[]
for s in subs:
    nm=s['attributes']['name']
    if not re.fullmatch(r'\d+', nm): continue
    for f in get(s['relationships']['files']['links']['related']['href']):
        a=f['attributes']
        if a['kind']=='file' and re.fullmatch(rf'{nm}_{tag}\.(set|fdt)', a['name']):
            rows.append((int(nm), a['name'], a['size'], f['links']['download']))
rows.sort()
with open(f'{tag}_files.tsv','w') as fh:
    for r in rows: fh.write('\t'.join(map(str,r))+'\n')
print(tag, 'subjects', len({r[0] for r in rows}), 'files', len(rows), 'total GB', sum(r[2] for r in rows)/1e9)
