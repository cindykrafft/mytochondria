import sys, re, json, html
exec(open(sys.path[0]+'/norm.py').read())
US='cindykrafft'
BOT=re.compile(r'(\[bot\]$|^github-actions|^codecov|^dependabot|^google-cla|^cla-|bot$)', re.I)
def n(t):
    t=html.unescape(t or ''); t=re.sub(r'[‘’]',"'",t); t=re.sub(r'[“”]','"',t)
    t=re.sub(r'[*_`>]','',t)
    return re.sub(r'\s+',' ',t).strip().lower()
def check(dirs, base):
    out=[]
    for d in dirs:
        led,thr=load(d,base)
        tm={key(y):y for y in thr}
        for e in led:
            k=(e['repo'],int(e['number'])); y=tm.get(k); P=[]
            if y is None: P.append('no raw thread')
            elif unreadable(y): out.append((d,e,['UNREADABLE'])); continue
            if y is not None:
                md=meta(y); it=items(y)
                hum=[a for a,b,kind,assoc in it if a and a.lower()!=US and not BOT.search(a)]
                # also human actions (merged_by/closed_by by others)
                actors=[x for x in [md.get('merged_by'),md.get('closed_by')] if x and x.lower()!=US and not BOT.search(x)]
                ev=e.get('evidence') or {}; q=ev.get('quote') or ''; st=e.get('status')
                if st!='unanswered' and q and not q.strip().startswith('['):
                    frags=[f.strip(' .') for f in re.split(r'\.\.\.|…|\[\.\.\.\]',n(q)) if len(f.strip(' .'))>10]
                    texts=[(a,n(b)) for a,b,kind,assoc in it]
                    found=[a for a,t in texts if frags and all(f in t for f in frags)]
                    if not found: P.append('quote not found verbatim')
                    elif ev.get('author') and ev['author'].lower() not in [f.lower() for f in found]: P.append(f'quote by {found} not {ev.get("author")}')
                if st=='unanswered' and (hum or actors): P.append(f'unanswered but humans: {sorted(set(hum+actors))}')
                if st in ('in progress','rejected','resolved') and not (hum or actors): P.append('no human item/action from others')
                if st=='resolved' and not (md.get('merged') or e.get('merged') or e.get('fixed_by') or md.get('state_reason')=='completed'): P.append('resolved w/o merge/fix/completed')
                if st=='withdrawn' and (md.get('closed_by') or '').lower()!=US and not e.get('superseded_by'): P.append(f'withdrawn, closed_by={md.get("closed_by")}')
                if st=='in progress' and e.get('whose_move') not in ('us','them'): P.append('no whose_move')
                if st in ('in progress','unanswered') and (md.get('state') or e.get('state'))=='closed': P.append('closed but '+st)
                if e.get('confidence')=='low': P.append('LOW conf')
                if st not in ('resolved','rejected','withdrawn','in progress','unanswered'): P.append(f'bad status {st}')
            out.append((d,e,P))
    return out
if __name__=='__main__':
    base=sys.argv[1]; dirs=sys.argv[2:]
    import collections
    rs=check(dirs,base); c=collections.Counter()
    for d,e,P in rs:
        if P==['UNREADABLE']: c['unreadable']+=1; continue
        c[e['status']]+=1
        print(('CHECK ' if P else 'ok    ')+f"{e['repo']}#{e['number']} [{e['kind']}] {e['status']}{'/'+str(e.get('whose_move')) if e['status']=='in progress' else ''}  {'; '.join(P)}")
    print(dict(c))
