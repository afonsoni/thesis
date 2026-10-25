"""Blind rater for the judge-validation sheet.

Serves a one-page rater built from judge-sheet.md (never from judge-key.json, so
the judge's verdicts stay hidden) and saves every rating to ratings.json next to
this file. Score the finished ratings with
`python scripts/judge_validation.py score --ratings data/eval/validation/ratings.json`.

Run from the repo root and leave the terminal open:
    python3 data/eval/validation/judge_rater.py
then open http://localhost:8768 (Ctrl+C stops it; ratings are already on disk).
"""
import http.server
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
# NAME=judge-noret rates the second sheet into ratings-judge-noret.json.
NAME = os.environ.get("NAME", "judge")
SHEET = os.path.join(HERE, f"{NAME}-sheet.md")
RATINGS = os.path.join(HERE, "ratings.json" if NAME == "judge" else f"ratings-{NAME}.json")
PORT = int(os.environ.get("PORT", "8768"))


def parse_sheet(path):
    """Items with question, answer, reference, context and the claims to rate."""
    items, cur, sec, metric, buf = [], None, None, None, []

    def flush():
        if cur is not None and sec:
            cur[sec] = "\n".join(buf).strip()
        buf.clear()

    for line in open(path, encoding="utf-8").read().split("\n"):
        m = re.match(r"^## item-(\d+)$", line)
        if m:
            flush()
            sec = None
            cur = {"item": int(m.group(1)), "metrics": {}}
            items.append(cur)
            continue
        if cur is None:
            continue
        if line.startswith("**Question:**"):
            flush()
            sec = None
            cur["question"] = line[len("**Question:**"):].strip()
        elif line == "**Answer:**":
            flush()
            sec = "answer"
        elif line == "**Reference answer:**":
            flush()
            sec = "reference"
        elif re.match(r"^\*\*(faithfulness|correctness_recall)\*\* — ", line):
            flush()
            sec = None
            metric = line.split("**")[1]
            cur["metrics"][metric] = []
        elif sec is None and metric and line.startswith("- [ ] "):
            cur["metrics"][metric].append(line[6:])
        elif line.startswith("relevance:"):
            flush()
            sec = metric = None
        elif line.startswith("<details>"):
            flush()
            sec = "context"
        elif line.startswith("</details>"):
            flush()
            sec = None
        elif sec:
            buf.append(line)
    flush()
    return items


PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Judge rating</title>
<style>
:root{--bg:#fafaf8;--card:#fff;--text:#1f1e1c;--muted:#6b6a65;--line:#e4e2dc;--yes:#1d7a4f;--yesbg:#e3f3ea;--no:#a3302d;--nobg:#fbe9e8;--acc:#185fa5;--accbg:#e6f1fb;--focus:#fff7d6}
@media (prefers-color-scheme:dark){:root{--bg:#1b1b1a;--card:#242423;--text:#ecebe6;--muted:#a3a29c;--line:#3a3a38;--yes:#7fd0a6;--yesbg:#183527;--no:#f19a97;--nobg:#3d1d1c;--acc:#85b7eb;--accbg:#10304f;--focus:#3a3520}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:15px/1.55 -apple-system,system-ui,sans-serif}
header{position:sticky;top:0;z-index:2;background:var(--bg);border-bottom:1px solid var(--line);padding:10px 16px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}
header .grow{flex:1}
button{font:inherit;border:1px solid var(--line);background:var(--card);color:var(--text);border-radius:7px;padding:5px 11px;cursor:pointer}
button:hover{border-color:var(--muted)}
button.on{background:var(--accbg);border-color:var(--acc);color:var(--acc)}
select{font:inherit;padding:4px;border-radius:7px;border:1px solid var(--line);background:var(--card);color:var(--text)}
main{max-width:1400px;margin:0 auto;padding:16px}
.q{font-size:18px;font-weight:600;margin:4px 0 14px}
.cols{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:14px}
@media (max-width:900px){.cols{grid-template-columns:minmax(0,1fr)}}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px}
.card h3{margin:0 0 8px;font-size:12px;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);font-weight:600}
.txt{white-space:pre-wrap;word-wrap:break-word;max-height:46vh;overflow:auto}
.ctx{max-height:70vh}
.claim{display:flex;gap:10px;align-items:flex-start;padding:7px 8px;border-radius:7px;border:1px solid transparent}
.claim.focus{background:var(--focus);border-color:var(--line)}
.claim .n{color:var(--muted);min-width:30px;font-variant-numeric:tabular-nums}
.claim .t{flex:1}
.claim .b{display:flex;gap:6px}
.claim .b button{padding:2px 10px}
.claim .b .y.sel{background:var(--yesbg);border-color:var(--yes);color:var(--yes)}
.claim .b .x.sel{background:var(--nobg);border-color:var(--no);color:var(--no)}
.rel{display:flex;gap:8px;align-items:center;margin:14px 0;flex-wrap:wrap}
.muted{color:var(--muted);font-size:13px}
.prog{font-size:13px;color:var(--muted)}
.warn{color:var(--no)}
textarea{width:100%;height:160px;font:12px/1.4 ui-monospace,monospace;background:var(--card);color:var(--text);border:1px solid var(--line);border-radius:7px}
kbd{border:1px solid var(--line);border-bottom-width:2px;border-radius:4px;padding:0 4px;font-size:12px}
</style>
</head>
<body>
<header>
  <button id="prev" aria-label="Previous item">&larr;</button>
  <select id="pick" aria-label="Item"></select>
  <button id="next" aria-label="Next item">&rarr;</button>
  <button id="tabR" class="on">Recall</button>
  <button id="tabF">Faithfulness</button>
  <span class="grow"></span>
  <span class="prog" id="prog"></span>
  <span class="prog" id="disk"></span>
  <button id="exp">Export</button>
</header>
<main>
  <div class="q" id="q"></div>
  <div class="cols">
    <div class="card"><h3>Answer</h3><div class="txt" id="ans"></div></div>
    <div class="card"><h3 id="rtitle">Reference answer</h3><div class="txt" id="right"></div></div>
  </div>
  <div class="card" style="margin-top:14px">
    <h3 id="ctitle"></h3>
    <div class="muted" id="chelp"></div>
    <div id="list"></div>
  </div>
  <div class="rel"><span>Relevance (does the answer address the question? Ignore the reference.)</span><span id="relb"></span><span class="muted">5 = directly and completely, 3 = partly or vaguely, 1 = does not answer</span></div>
  <p class="muted">Keys: <kbd>y</kbd> yes, <kbd>n</kbd> no, <kbd>u</kbd> clear, <kbd>&uarr;</kbd>/<kbd>&darr;</kbd> move between claims, <kbd>1</kbd>&ndash;<kbd>5</kbd> relevance, <kbd>&larr;</kbd>/<kbd>&rarr;</kbd> previous/next item, <kbd>f</kbd> switch metric. Every change is saved to ratings.json.</p>
  <div id="expbox" hidden><textarea id="exptxt" readonly aria-label="Ratings as JSON"></textarea></div>
</main>
<script>
const DATA = __DATA__;
const MET = {r: "correctness_recall", f: "faithfulness"};
let S = {}, idx = 0, tab = "r", focus = 0, timer = null;
const $ = id => document.getElementById(id);
function esc(s){return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
function md(s){return esc(s).replace(/\*\*(.+?)\*\*/g,"<b>$1</b>").replace(/^\*\s{1,4}/gm,"&bull; ")}
function rec(i){const k=String(DATA[i].item);S[k]=S[k]||{r:[],f:[],rel:null};return S[k]}
function claims(i,t){return DATA[i].metrics[MET[t]]||[]}
function done(a){return a.filter(v=>v===true||v===false).length}
function prog(){let r=0,rt=0,f=0,ft=0,rel=0;DATA.forEach((d,i)=>{const s=rec(i);rt+=claims(i,"r").length;ft+=claims(i,"f").length;r+=done(s.r);f+=done(s.f);if(s.rel)rel++});$("prog").textContent=`Recall ${r}/${rt} · Faithfulness ${f}/${ft} · Relevance ${rel}/${DATA.length}`}
function save(){prog();clearTimeout(timer);$("disk").textContent="saving…";$("disk").className="prog";
  timer=setTimeout(()=>fetch("/save",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(S)})
    .then(r=>{if(!r.ok)throw 0;$("disk").textContent="saved"})
    .catch(()=>{$("disk").textContent="not saved: is the server running?";$("disk").className="prog warn"}),300)}
function render(){
  const d=DATA[idx],s=rec(idx);
  $("pick").value=idx;$("q").textContent=`Item ${d.item}. ${d.question}`;
  $("ans").innerHTML=md(d.answer);
  $("tabR").classList.toggle("on",tab==="r");$("tabF").classList.toggle("on",tab==="f");
  if(tab==="r"){$("rtitle").textContent="Reference answer";$("right").className="txt";$("right").innerHTML=md(d.reference||"(no reference)");
    $("ctitle").textContent="Does the answer state this reference claim?";$("chelp").textContent="Yes if the answer states or directly implies it, even in other words. No if it leaves it out or contradicts it."}
  else{$("rtitle").textContent="Context the generator read";$("right").className="txt ctx";$("right").innerHTML=md(d.context||"");
    $("ctitle").textContent="Is the claim supported by the context?";$("chelp").textContent="Check against the context on the right. Optional: rate a few items, skip the rest."}
  const cs=claims(idx,tab),arr=s[tab];
  $("list").innerHTML=cs.map((c,j)=>{const v=arr[j];return `<div class="claim${j===focus?" focus":""}" data-j="${j}"><span class="n">${j+1}</span><span class="t">${esc(c)}</span><span class="b"><button class="y${v===true?" sel":""}" data-j="${j}" data-v="1">Yes</button><button class="x${v===false?" sel":""}" data-j="${j}" data-v="0">No</button></span></div>`}).join("")||'<p class="muted">No claims for this item.</p>';
  $("relb").innerHTML=[1,2,3,4,5].map(n=>`<button class="${s.rel===n?"on":""}" data-rel="${n}">${n}</button>`).join(" ");
  const el=document.querySelector(".claim.focus");if(el)el.scrollIntoView({block:"nearest"});
}
function mark(j,v){const a=rec(idx)[tab];while(a.length<=j)a.push(null);a[j]=v;save();if(v!==null&&j===focus&&focus<claims(idx,tab).length-1)focus++;render()}
function go(i){idx=Math.max(0,Math.min(DATA.length-1,i));focus=0;render();window.scrollTo(0,0)}
$("pick").innerHTML=DATA.map((d,i)=>`<option value="${i}">Item ${d.item}</option>`).join("");
$("pick").onchange=e=>go(+e.target.value);$("prev").onclick=()=>go(idx-1);$("next").onclick=()=>go(idx+1);
$("tabR").onclick=()=>{tab="r";focus=0;render()};$("tabF").onclick=()=>{tab="f";focus=0;render()};
$("list").onclick=e=>{const b=e.target.closest("button");if(b){mark(+b.dataset.j,b.dataset.v==="1");return}const c=e.target.closest(".claim");if(c){focus=+c.dataset.j;render()}};
$("relb").onclick=e=>{const b=e.target.closest("button");if(!b)return;const s=rec(idx),n=+b.dataset.rel;s.rel=s.rel===n?null:n;save();render()};
$("exp").onclick=()=>{$("expbox").hidden=!$("expbox").hidden;$("exptxt").value=JSON.stringify(S)};
document.addEventListener("keydown",e=>{if(e.target.tagName==="TEXTAREA"||e.target.tagName==="SELECT"||e.metaKey||e.ctrlKey||e.altKey)return;const n=claims(idx,tab).length;
  if(e.key==="y")mark(focus,true);else if(e.key==="n")mark(focus,false);else if(e.key==="u")mark(focus,null);
  else if(e.key==="ArrowDown"){focus=Math.min(n-1,focus+1);render();e.preventDefault()}else if(e.key==="ArrowUp"){focus=Math.max(0,focus-1);render();e.preventDefault()}
  else if(e.key==="ArrowRight")go(idx+1);else if(e.key==="ArrowLeft")go(idx-1);
  else if("12345".includes(e.key)){rec(idx).rel=+e.key;save();render()}
  else if(e.key==="f"){tab=tab==="r"?"f":"r";focus=0;render()}});
fetch("/ratings.json").then(r=>r.ok?r.json():{}).catch(()=>({})).then(d=>{S=d||{};prog();$("disk").textContent="loaded";render()});
</script>
</body>
</html>
"""


class Handler(http.server.BaseHTTPRequestHandler):
    def _send(self, code, body=b"", ctype="text/plain; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            data = json.dumps(parse_sheet(SHEET), ensure_ascii=False).replace("</", "<\\/")
            self._send(200, PAGE.replace("__DATA__", data).encode("utf-8"), "text/html; charset=utf-8")
        elif self.path == "/ratings.json":
            body = open(RATINGS, "rb").read() if os.path.exists(RATINGS) else b"{}"
            self._send(200, body, "application/json")
        else:
            self._send(404, b"not found")

    def do_POST(self):
        if self.path != "/save":
            self._send(404, b"not found")
            return
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        try:
            json.loads(body)  # refuse anything that is not JSON before touching the file
        except ValueError:
            self._send(400, b"not JSON")
            return
        tmp = RATINGS + ".tmp"
        with open(tmp, "wb") as f:
            f.write(body)
        os.replace(tmp, RATINGS)  # atomic: a crash never leaves half a file
        self._send(204)

    def log_message(self, *args):
        pass  # keep the terminal quiet


if __name__ == "__main__":
    items = parse_sheet(SHEET)
    print(f"{len(items)} items, {sum(len(v) for i in items for v in i['metrics'].values())} claims", flush=True)
    print(f"Ratings file: {RATINGS}", flush=True)
    print(f"Open http://localhost:{PORT}  (Ctrl+C to stop)", flush=True)
    http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
