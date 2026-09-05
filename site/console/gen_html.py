import json, html
import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
D=json.load(open(os.path.join(OUT,"data.json"))); FX=json.load(open(os.path.join(OUT,"fixes.json")))
order=["plink","htseq","deeptools","bedtools","fastp","cutadapt","umap","cellphonedb","scanpy","iqtree"]
labels={"plink":"PLINK 1.9","htseq":"HTSeq","deeptools":"deepTools","bedtools":"BEDTools","fastp":"fastp","cutadapt":"Cutadapt","umap":"umap-learn","cellphonedb":"CellPhoneDB","scanpy":"Scanpy (Scrublet port)","iqtree":"IQ-TREE 3"}
page=r'''<title>Mytochondria Filing Console</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{--ground:#F5F7F3;--surface:#FFFFFF;--ink:#181C19;--muted:#5F6A61;--line:#D5DBD3;--line-strong:#B9C2B8;--accent:#0E6F6B;--accent-ink:#FFFFFF;--done:#2E7B4B;--warn:#8A5A00;--warn-soft:#FFF3DC;--code:#EEF2ED;--shadow:0 1px 2px rgba(20,30,24,.06),0 8px 24px -16px rgba(20,30,24,.25)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ground:#121614;--surface:#191E1B;--ink:#E7EBE4;--muted:#9AA498;--line:#2B322D;--line-strong:#3B443D;--accent:#5AC9BD;--accent-ink:#0E1A18;--done:#6FCB8E;--warn:#E6B45C;--warn-soft:#2E2510;--code:#0F1311;--shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -16px rgba(0,0,0,.6)}}
:root[data-theme="dark"]{--ground:#121614;--surface:#191E1B;--ink:#E7EBE4;--muted:#9AA498;--line:#2B322D;--line-strong:#3B443D;--accent:#5AC9BD;--accent-ink:#0E1A18;--done:#6FCB8E;--warn:#E6B45C;--warn-soft:#2E2510;--code:#0F1311;--shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -16px rgba(0,0,0,.6)}
*{box-sizing:border-box}body{margin:0;background:var(--ground);color:var(--ink);font:15px/1.55 "IBM Plex Sans",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
main{max-width:840px;margin:0 auto;padding:40px 24px 80px}
h1{font-size:28px;line-height:1.15;font-weight:600;letter-spacing:-.01em;margin:0 0 6px;text-wrap:balance}
h2.repo{font-size:20px;font-weight:600;margin:36px 0 4px;display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}
h2.repo .eyebrow{font-weight:500}
.lede{color:var(--muted);margin:0 0 20px;max-width:66ch}
code,pre,.mono{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace}code{font-size:.92em;background:var(--code);padding:1px 5px;border-radius:4px}
.eyebrow{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}
.guide{border-left:3px solid var(--accent);padding:6px 14px;margin:0 0 14px;color:var(--muted);font-size:14px;max-width:72ch}
.note{border:1px solid var(--line);border-left:3px solid var(--warn);background:var(--warn-soft);border-radius:6px;padding:10px 14px;margin:0 0 14px;font-size:14px}
ol.steps{list-style:none;margin:0;padding:0;display:grid;gap:12px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:8px;box-shadow:var(--shadow);padding:14px 18px 12px}
.card header{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:baseline;justify-content:space-between;margin-bottom:6px}
.card h3{font-size:15.5px;font-weight:600;margin:0;line-height:1.3}
.actions{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:8px}
button,.btn{font:inherit;font-weight:500;font-size:13.5px;border-radius:6px;padding:7px 12px;border:1px solid var(--line-strong);background:var(--surface);color:var(--ink);cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;gap:8px;line-height:1.2}
button:hover,.btn:hover{border-color:var(--accent)}button:focus-visible,.btn:focus-visible,input:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.primary{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}.primary:hover{filter:brightness(1.07)}
.btn.disabled{opacity:.45;pointer-events:none}
.ghost{border-color:transparent;color:var(--accent);padding-left:6px;padding-right:6px}
label.num-in{display:inline-flex;align-items:center;gap:8px;font-size:13px;color:var(--muted)}
input[type=number]{font:inherit;font-family:"IBM Plex Mono",monospace;width:92px;padding:6px 10px;border:1px solid var(--line-strong);border-radius:6px;background:var(--surface);color:var(--ink)}
.hint{font-size:12.5px;color:var(--muted);margin:8px 0 0}
details{margin-top:10px;border-top:1px dashed var(--line);padding-top:6px}summary{cursor:pointer;color:var(--muted);font-size:13px;user-select:none}summary:hover{color:var(--ink)}
.field{margin-top:10px}.field .eyebrow{display:block;margin-bottom:4px}
pre.body{margin:0;background:var(--code);border:1px solid var(--line);border-radius:6px;padding:10px 12px;font-size:12.5px;line-height:1.5;white-space:pre-wrap;word-break:break-word;max-height:340px;overflow:auto}
.tier-block{margin:14px 0 18px}.eyebrow.tier{margin:0 0 4px;color:var(--accent)}details.tier-held{margin:10px 0 18px;border:1px dashed var(--line-strong);border-radius:8px;padding:8px 14px}details.tier-held>summary{font-size:13.5px;color:var(--muted)}details.tier-held ol.steps{margin-top:8px}
.done .card{border-color:var(--done)}.done h3::before{content:"✓ ";color:var(--done)}
.toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:var(--ink);color:var(--ground);padding:9px 14px;border-radius:6px;font-size:13px;opacity:0;pointer-events:none;transition:opacity .2s}.toast.show{opacity:1}
@media (prefers-reduced-motion:reduce){.toast{transition:none}}
</style>
<main>
  <p class="eyebrow">Mytochondria · sixteen packages · triaged 2026-09-04</p>
  <h1>Mytochondria Filing Console</h1>
  <p class="lede">One section per repository, newest first. Each section is split into what to file now, comments on issues the maintainers already have open, what is filed, and what is held back until a maintainer gives a positive signal. Where a finding matches an issue that is already open, the card opens that issue and the text is a comment to paste. The Cutadapt, umap-learn and CellPhoneDB sections carry what was filed on 2026-09-03. Each button opens GitHub with the form prefilled where the text fits in a URL; where it does not, the button opens the form with the title only and the Copy button carries the body. Repositories you have not forked yet show their PR steps greyed out: fork them and tell me, and I will push the branches. Scrublet's original repository is skipped as unmaintained (last commit 2020, open issues unanswered).</p>
  <div id="root"></div>
</main>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script>
const D = __DATA__; const FX = __FIXES__;
const ORDER = __ORDER__; const LABELS = __LABELS__;
const LIMIT = 6800;
const state = load();
function load(){ try{ return JSON.parse(localStorage.getItem("audit-filing-v1")||"{}"); }catch(e){ return {}; } }
function save(){ try{ localStorage.setItem("audit-filing-v1", JSON.stringify(state)); }catch(e){} }
function q(o){ return Object.entries(o).filter(([k,v])=>v!==undefined&&v!=="").map(([k,v])=>encodeURIComponent(k)+"="+encodeURIComponent(v)).join("&"); }
function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;"); }
function toast(m){ const t=document.getElementById("toast"); t.textContent=m; t.classList.add("show"); clearTimeout(t._h); t._h=setTimeout(()=>t.classList.remove("show"),1800); }
async function copy(t){ try{ await navigator.clipboard.writeText(t); toast("Copied"); }catch(e){ toast("Copy failed: use the expander and select the text"); } }
function fillBody(body, key, r, ex){ return body.replace(/#<[^>]*issue[^>]*>|#ISSUE\d|#<issue number>|#NNN/gi, (m)=>{ const n=state[r+"_"+key+"_num"]||ex; return n?("#"+n):m; }); }
function issueUrl(r, i){
  const base=`https://github.com/${r.owner}/${r.repo}/issues/new?`;
  let params;
  if (i.description!==undefined) params={template:r.template, title:i.title, description:i.description, code:i.code, traceback:i.traceback, versions:i.versions};
  else params=Object.assign(r.template?{template:r.template}:{}, {title:i.title, body:i.body});
  let url=base+q(params);
  if (url.length>LIMIT){ const p2=Object.assign(r.template?{template:r.template}:{}, {title:i.title, body:"(body pasted from the filing console)"}); url=base+q(p2); return {url, copyNeeded:true}; }
  return {url, copyNeeded:false};
}
function issueText(i){ if (i.description!==undefined) return "# "+i.title+"\n\n### What happened?\n\n"+i.description+"\n\n### Minimal code sample\n\n```python\n"+i.code+"```\n\n### Error output\n\n```\n"+i.traceback+"\n```\n\n### Versions\n\n"+i.versions; return "# "+i.title+"\n\n"+i.body; }
function prUrl(r, p, body){ const owner=r.fork.split("/")[0]; return `https://github.com/${r.owner}/${r.repo}/compare/${r.base||"main"}...${owner}:${r.repo}:${p.branch}?`+q({expand:"1", title:p.title, body}); }
function card(cls, inner){ return `<li class="${cls}"><div class="card">${inner}</div></li>`; }
function issueCard(r,key,i){
  const done=!!state[key+"_"+i.id+"_done"]||i.tier==="filed";
  if (i.existing){
    const url=`https://github.com/${r.owner}/${r.repo}/issues/${i.existing}`;
    return card(done?"done":"", `<header><h3>Comment ${esc(i.id)} on #${i.existing} · ${esc(i.title)}</h3><span class="eyebrow">comment on an open issue</span></header>
      <div class="actions"><a class="btn primary" href="${url}" target="_blank" rel="noopener">Open issue #${i.existing} ↗</a><button data-copy="${key}|issue|${i.id}">Copy comment</button><button class="ghost" data-done="${key}|${i.id}">${done?"Mark not done":"Mark done"}</button></div>
      <p class="hint">GitHub cannot prefill a comment: read the thread first, then paste the copied text into the comment box.</p>
      <details><summary>Show the comment</summary><div class="field"><pre class="body">${esc(i.body)}</pre></div></details>`);
  }
  const u=issueUrl(r,i);
  return card(done?"done":"", `<header><h3>Issue ${esc(i.id)} · ${esc(i.title)}</h3><span class="eyebrow">${i.tier==="filed"?"filed as "+esc(i.filed_as):"issue"}</span></header>
    <div class="actions"><a class="btn primary ${i.tier==="filed"?"disabled":""}" href="${u.url}" target="_blank" rel="noopener">${u.copyNeeded?"Open form (title only) ↗":"Open prefilled on GitHub ↗"}</a>
    <button data-copy="${key}|issue|${i.id}">Copy ${u.copyNeeded?"body to paste":"full text"}</button>
    <label class="num-in">Filed as # <input type="number" min="1" data-num="${key}|${i.id}" value="${state[key+"_"+i.id+"_num"]||""}" placeholder="0000"></label>
    <button class="ghost" data-done="${key}|${i.id}">${done?"Mark not done":"Mark done"}</button></div>
    ${u.copyNeeded?`<p class="hint">This report is longer than GitHub accepts in a URL. The button opens the form with the title; paste the body from Copy into the text box.</p>`:""}
    <details><summary>Show the text that will be submitted</summary>${i.description!==undefined?
      `<div class="field"><span class="eyebrow">What happened?</span><pre class="body">${esc(i.description)}</pre></div><div class="field"><span class="eyebrow">Minimal code sample</span><pre class="body">${esc(i.code)}</pre></div><div class="field"><span class="eyebrow">Error output</span><pre class="body">${esc(i.traceback)}</pre></div><div class="field"><span class="eyebrow">Versions</span><pre class="body">${esc(i.versions)}</pre></div>`
      :`<div class="field"><span class="eyebrow">Body</span><pre class="body">${esc(i.body)}</pre></div>`}</details>`);
}
function discCard(r,key,d){
  const url=`https://github.com/${r.owner}/${r.repo}/discussions/new?`+q({title:d.title, body:d.body}); const done=!!state[key+"_"+d.id+"_done"];
  return card(done?"done":"", `<header><h3>Discussion ${esc(d.id)} · ${esc(d.title)}</h3><span class="eyebrow">discussion</span></header>
    <div class="actions"><a class="btn primary" href="${url}" target="_blank" rel="noopener">Open prefilled discussion ↗</a><button data-copy="${key}|disc|${d.id}">Copy body</button><button class="ghost" data-done="${key}|${d.id}">${done?"Mark not done":"Mark done"}</button></div>
    <p class="hint">GitHub will ask you to pick a category (General or Q&amp;A).</p>
    <details><summary>Show the text</summary><div class="field"><pre class="body">${esc(d.body)}</pre></div></details>`);
}
function prCard(r,key,p){
  const n=state[key+"_"+p.needs+"_num"]||p.existing||""; const body=fillBody(p.body, p.needs, key, p.existing); const done=!!state[key+"_PR"+p.id+"_done"]||p.tier==="filed";
  const url=r.fork?prUrl(r,p,body):"#";
  return card(done?"done":"", `<header><h3>PR for ${esc(p.id)} · ${esc(p.title)}</h3><span class="eyebrow">${p.tier==="filed"?"filed as "+esc(p.filed_as):"pull request"} · <span class="mono">${esc(p.branch)}</span></span></header>
    <div class="actions"><a class="btn primary ${(r.forked&&p.tier!=="filed")?"":"disabled"}" href="${url}" target="_blank" rel="noopener">Open prefilled compare ↗</a><button data-copy="${key}|pr|${p.id}">Copy body</button>
    <label class="num-in">Closes issue # <input type="number" min="1" data-num="${key}|${p.needs}" value="${n}" placeholder="0000"></label><button class="ghost" data-done="${key}|PR${p.id}">${done?"Mark not done":"Mark done"}</button></div>
    ${r.forked?"":`<p class="hint">Fork ${esc(r.owner+"/"+r.repo)} to your account, then tell me and I will push <span class="mono">${esc(p.branch)}</span> to it; the button activates on the next publish.</p>`}
    ${(!n)?`<p class="hint">Enter the issue number so the body says Closes #.</p>`:""}
    <details><summary>Show the body</summary><div class="field"><pre class="body">${esc(body)}</pre></div></details>`);
}
const TIERS=[["now","File now","changes published numbers under default or common settings on the current release; at most two per repository until a maintainer responds"],
             ["comment","Comment on an open issue","the maintainers already keep this thread; a cause and a patch on it cost little goodwill"],
             ["filed","Already filed",""],
             ["held","Held back","crashes, rare options, API-only paths, documentation drift, or a third finding for a repository that has not answered yet; file after a positive signal"]];
function fixCard(f){
  const done=!!state["fix_"+f.pkg+"_"+f.issue+"_done"];
  const issueUrl=`https://github.com/${f.owner}/${f.repo}/issues/${f.issue}`;
  const cmp=`https://github.com/${f.owner}/${f.repo}/compare/${f.base}...${f.fork.split("/")[0]}:${f.fork.split("/")[1]}:${f.branch}?`+q({expand:"1", title:f.title, body:f.body});
  if (f.assigned) return card(done?"done":"", `<header><h3>${esc(f.owner+"/"+f.repo)} #${f.issue} · ${esc(f.title)}</h3><span class="eyebrow">assigned issue · comment only</span></header>
    <div class="actions"><a class="btn primary" href="${issueUrl}" target="_blank" rel="noopener">Open issue #${f.issue} ↗</a><button data-fixcopy="${f.pkg}|${f.issue}|comment">Copy comment</button><button class="ghost" data-done="fix_${f.pkg}|${f.issue}">${done?"Mark not done":"Mark done"}</button></div>
    <p class="hint">${esc(f.assigned)} No PR: the comment carries the diagnosis and the branch link; the assignee decides.</p>
    <details><summary>Show the comment</summary><div class="field"><pre class="body">${esc(f.comment)}</pre></div></details>`);
  if (f.filed){ const w=f.filed.what==="pr"?`PR #${f.filed.num} (${f.filed.state})`:`comment posted on #${f.filed.num}`;
    return card("done", `<header><h3>${esc(f.owner+"/"+f.repo)} #${f.issue} · ${esc(f.title)}</h3><span class="eyebrow">filed · ${esc(w)}</span></header>
    <div class="actions"><a class="btn" href="https://github.com/${f.owner}/${f.repo}/issues/${f.issue}" target="_blank" rel="noopener">Open issue #${f.issue} ↗</a>${f.filed.what==="pr"?`<a class="btn" href="https://github.com/${f.owner}/${f.repo}/pull/${f.filed.num}" target="_blank" rel="noopener">Open PR #${f.filed.num} ↗</a>`:""}</div>`); }
  if (f.stale) return card("", `<header><h3>${esc(f.owner+"/"+f.repo)} #${f.issue} · ${esc(f.title)}</h3><span class="eyebrow">held · issue closed upstream</span></header><p class="hint">PR #1451 was opened against 3.5.6 on 2026-09-04 and closed the next day; deepTools closed the issue on 2026-09-05 with the 4.0.0 merge: the Rust computeMatrix reads gzipped BEDs. The residual failure in computeMatrixOperations sort is fixed on branch fix4/issue-1423-gzipped-bed-sortmatrix on the fork; hold it unless the maintainers want a follow-up.</p>`);
  if (f.declines) return card("", `<header><h3>${esc(f.repo)} #${f.issue} · ${esc(f.title)}</h3><span class="eyebrow">not to be filed</span></header><p class="hint">This repository declines AI-generated contributions; the fix stays in the audit repository.</p>`);
  return card(done?"done":"", `<header><h3>${esc(f.owner+"/"+f.repo)} #${f.issue} · ${esc(f.title)}</h3><span class="eyebrow">issue fix · <span class="mono">${esc(f.branch)}</span></span></header>
    <div class="actions"><a class="btn" href="${issueUrl}" target="_blank" rel="noopener">Open issue #${f.issue} ↗</a>
    <a class="btn primary ${f.forked?"":"disabled"}" href="${cmp}" target="_blank" rel="noopener">Open prefilled PR ↗</a>
    <button data-fixcopy="${f.pkg}|${f.issue}|body">Copy PR body</button>${f.comment?`<button data-fixcopy="${f.pkg}|${f.issue}|comment">Copy issue comment</button>`:""}
    <button class="ghost" data-done="fix_${f.pkg}|${f.issue}">${done?"Mark not done":"Mark done"}</button></div>
    ${f.forked?"":`<p class="hint">Branch not on the fork yet (${esc(f.fork)}); the button activates on the next publish.</p>`}
    <p class="hint">Order: open the PR first, then paste the comment on the issue with the PR number filled in.</p>
    <details><summary>Show the PR body</summary><div class="field"><pre class="body">${esc(f.body)}</pre></div></details>
    ${f.comment?`<details><summary>Show the issue comment</summary><div class="field"><pre class="body">${esc(f.comment)}</pre></div></details>`:""}`);
}
function render(){
  const root=document.getElementById("root"); root.innerHTML="";
  if (FX.length){
    const sec=document.createElement("section");
    sec.innerHTML=`<h2 class="repo">Fixes for the projects' own open issues <span class="eyebrow">README step 6 · ${FX.length}</span></h2><div class="guide"><span class="eyebrow">what this is</span><br>Each card answers a bug a user or maintainer already reported. Open the issue and read the thread first (its comments are not visible from the audit session), then open the PR, then paste the comment with the PR number.</div><ol class="steps">${FX.map(fixCard).join("")}</ol>`;
    root.appendChild(sec);
  }
  for (const key of ORDER){
    const r=D[key]; const sec=document.createElement("section");
    let h=`<h2 class="repo">${esc(LABELS[key])} <span class="eyebrow">${esc(r.owner+"/"+r.repo)}${r.fork?(" · fork "+esc(r.fork)+(r.forked?"":" (not created yet)")):""}</span></h2>`;
    h+=`<div class="guide"><span class="eyebrow">what the repo asks for</span><br>${esc(r.guide)}</div>`;
    if (r.declines_ai){ h+=`<div class="note"><strong>Do not file.</strong> The maintainers of ${esc(r.owner+"/"+r.repo)} have said they do not take AI-generated contributions (topic <span class="mono">upstream-declines-ai-contributions</span> on the fork). Nothing below is to be opened, commented or pushed; open items are theirs to close.</div>`; sec.innerHTML=h; root.appendChild(sec); continue; }
    if (r.order_note) h+=`<div class="note">${r.stale?"<strong>Upstream rewritten.</strong> ":""}${esc(r.order_note)}</div>`;
    const buckets={now:[],comment:[],filed:[],held:[]};
    for (const i of r.issues){ buckets[i.tier].push(issueCard(r,key,i)); for (const p of r.prs) if (p.needs===i.id) buckets[p.tier].push(prCard(r,key,p)); }
    for (const p of r.prs) if (!r.issues.some(i=>i.id===p.needs)) buckets[p.tier].push(prCard(r,key,p));
    for (const d of (r.discussions||[])) buckets[d.tier||"held"].push(discCard(r,key,d));
    for (const [t,label,why] of TIERS){
      const items=buckets[t]; if (!items.length) continue;
      const inner=`<p class="eyebrow tier">${esc(label)} · ${items.length}</p>${why?`<p class="hint" style="margin:0 0 8px">${esc(why)}</p>`:""}<ol class="steps">${items.join("")}</ol>`;
      h+= t==="held" ? `<details class="tier-held"><summary>${esc(label)} · ${items.length} — click to expand</summary>${inner}</details>` : `<div class="tier-block">${inner}</div>`;
    }
    sec.innerHTML=h; root.appendChild(sec);
  }
  root.querySelectorAll("[data-copy]").forEach(b=>b.addEventListener("click",()=>{ const [k,kind,id]=b.dataset.copy.split("|"); const r=D[k];
    if(kind==="issue"){ const i=r.issues.find(x=>x.id===id); copy(i.existing?i.body:issueText(i)); }
    else if(kind==="disc"){ copy(r.discussions.find(x=>x.id===id).body); }
    else { const p=r.prs.find(x=>x.id===id); copy(fillBody(p.body,p.needs,k,p.existing)); } }));
  root.querySelectorAll("[data-fixcopy]").forEach(b=>b.addEventListener("click",()=>{ const [pkg,n,what]=b.dataset.fixcopy.split("|"); const f=FX.find(x=>x.pkg===pkg&&String(x.issue)===n); copy(what==="body"?f.body:f.comment); }));
  root.querySelectorAll("[data-num]").forEach(inp=>inp.addEventListener("change",()=>{ const [k,id]=inp.dataset.num.split("|"); state[k+"_"+id+"_num"]=inp.value; save(); render(); }));
  root.querySelectorAll("[data-done]").forEach(b=>b.addEventListener("click",()=>{ const [k,id]=b.dataset.done.split("|"); state[k+"_"+id+"_done"]=!state[k+"_"+id+"_done"]; save(); render(); }));
}
render();
</script>
'''
page=page.replace("__DATA__", json.dumps(D).replace("</","<\\/")).replace("__ORDER__", json.dumps(order)).replace("__FIXES__", json.dumps(FX).replace("</","<\\/")).replace("__LABELS__", json.dumps(labels))
open(os.path.join(OUT,"filing-console.html"),"w").write(page); print(len(page),"bytes")
