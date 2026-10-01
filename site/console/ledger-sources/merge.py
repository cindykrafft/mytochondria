import json, re, glob, sys
exec(open('norm.py').read())
SEEN='/home/user/research-software-audit/site/console/seen.json'
j=json.load(open(SEEN))
dirs=[d for d in BATCHES]+sorted(glob.glob('r-*'))
cls={}; bodies={}
for d in dirs:
    led,thr=load(d,'.')
    tm={key(y):y for y in thr}
    for e in led:
        k=(e['repo'],int(e['number'])); y=tm.get(k)
        if y is None or unreadable(y) or e.get('status') not in ('resolved','rejected','withdrawn','in progress','unanswered'): continue
        md=meta(y)
        body=md.get('body') or y.get('body') or (y.get('pull') or {}).get('body') or (y.get('issue') or {}).get('body') or ''
        bodies[k]=body
        cls[k]=dict(e=e, md=md)
# overrides decided on reading (2026-10-01)
fs_issue={1464:1463,1466:1465,1468:1467,1470:1469,1472:1471}
for pr,iss in fs_issue.items():
    k=('freesurfer/freesurfer',pr); c=cls[k]
    c['e']=dict(c['e'], status='rejected', whose_move=None, confidence='high',
        evidence={'quote':"Please do not file the output from code analysis tools as de-facto issues.  We can run code analysis tools and it is not clear that code deficiencies are worth updating or patching in older releases dating back to 6.0.0.",
                  'author':'buildqa','date':cls[('freesurfer/freesurfer',iss)]['e']['evidence'].get('date'),
                  'url':f'https://github.com/freesurfer/freesurfer/issues/{iss}'},
        reason=f'The PR is open with no response, but the issue it fixes (#{iss}) was declined and closed by buildqa; the decline covers the fix.')
cls[('fieldtrip/fieldtrip',2622)]['e']['whose_move']='them'
today='2026-10-01'
MANUAL={('lme4/lme4',1000):[867]}  # kit: LM2 is the comment on #867 plus PR #1000
def pairs(repo, body):
    return sorted({int(n) for n in re.findall(r'(?i)\b(?:fix(?:es|ed)?|close[sd]?|resolve[sd]?)\s+#(\d+)', body or '')})
extras={('samtools/samtools',696):'ST3 (our comment with the reproduction; PR #2388 fixes it)',
        ('arq5x/bedtools2',1142):'BT2 (our comment; PR #1144)',
        ('deeptools/deepTools',1108):'DT1 (our comment; fixed by the maintainers in #1452)',
        ('deeptools/deepTools',1118):'DT4 (our comment; PR #1466)'}
have={(x['repo'],x['number']) for x in j['items']}
for k,why in extras.items():
    if k not in have:
        c=cls[k]; md=c['md']
        j['items'].append(dict(repo=k[0], number=k[1], kind='comment', state=md.get('state') or 'open', merged=False,
            comments=None, updated=None, title=md.get('title') or c['e'].get('title'),
            note=f'our comment on a maintainer-opened issue: {why}; not returned by the author search, checked by number (WATCH.md)'))
n=0; missing=[]
for it in j['items']:
    k=(it['repo'],it['number'])
    if it['repo'].startswith('cindykrafft/'):
        it.update(status='internal', whose_move=None, evidence=None, status_checked=today); continue
    c=cls.get(k)
    if not c: missing.append(k); continue
    e=c['e']; md=c['md']; ev=e.get('evidence') or {}
    it['status']=e['status']; it['whose_move']=e.get('whose_move') if e['status']=='in progress' else None
    it['evidence']={'quote':(ev.get('quote') or '')[:300],'author':ev.get('author'),'date':ev.get('date'),'url':ev.get('url')}
    for f in ('fixed_by','superseded_by'):
        if e.get(f): it[f]=e[f]
        else: it.pop(f,None)
    it['status_checked']=today
    if md.get('state'): it['state']=md['state']
    if md.get('merged') is not None and it['kind']=='pr': it['merged']=bool(md['merged'])
    if it['kind']=='pr':
        p=pairs(it['repo'], bodies.get(k,''))
        p=sorted(set(p)|set(MANUAL.get(k,[])))
        if p: it['fixes']=p
    if not it.get('title') and (md.get('title') or e.get('title')): it['title']=md.get('title') or e.get('title')
    n+=1
j['status_schema']={'status':['resolved','rejected','withdrawn','in progress','unanswered','internal'],
  'whose_move':'us|them, only for in progress','evidence':'the decisive human quote or action (verbatim, author, date, url)',
  'fixes':'issues this PR says it fixes; an issue and its PR count as one finding','status_checked':'date the thread was last read in full'}
json.dump(j,open(SEEN,'w'),indent=1,ensure_ascii=False); open(SEEN,'a').write('\n')
print('classified',n,'missing',missing)
import collections
print(collections.Counter(x.get('status') for x in j['items']))
