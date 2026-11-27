#!/usr/bin/env python3
"""Create downloadable weekly timetable PDFs (every class and teacher, every language) into /pdf/<lang>/.
Run after build.py:  python3 _src/make_pdfs.py   (needs playwright + Chrome)"""
import json, os, re, subprocess, sys, time
sys.path.insert(0, os.path.dirname(__file__))
from texts import ORDER, MAIN
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TT = json.load(open(os.path.join(ROOT, "_src", "timetable.json"), encoding="utf-8"))
classes = list(TT["classes"])
teachers = sorted({t for c in TT["classes"].values() for d in c.values() for l in d.values() for _, t in l if t})
slug = lambda t: "t-" + re.sub(r"-+$", "", re.sub(r"[^a-z0-9]+", "-", t.lower()))
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8766"], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1); n = 0
try:
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = b.new_page(viewport={"width": 1200, "height": 900})
        for lang in ORDER:
            out = os.path.join(ROOT, "pdf", lang); os.makedirs(out, exist_ok=True)
            base = f"http://localhost:8766/{'' if lang == MAIN else lang + '/'}timetable/"
            for key, fname in [(c.lower(), "c-" + c.lower()) for c in classes] + [(slug(t), slug(t)) for t in teachers]:
                pg.goto("about:blank")  # full reload so the page reads the #class / #teacher
                pg.goto(base + "#" + key); pg.wait_for_timeout(120)
                pg.evaluate("document.querySelectorAll('.ttmain .seg button')[1].click()")
                pg.evaluate("document.querySelectorAll('.printhead img').forEach(function(i){i.src=i.src.replace(/logo\\.png$/,'logo-80.png')})")
                pg.wait_for_timeout(60)
                pg.emulate_media(media="print")
                pg.pdf(path=os.path.join(out, fname + ".pdf"), format="A4", landscape=True, print_background=True,
                       margin={"top": "10mm", "bottom": "10mm", "left": "10mm", "right": "10mm"})
                pg.emulate_media(media="screen"); n += 1
                # smaller files: recompress streams, pack objects (same look)
                f = os.path.join(out, fname + ".pdf")
                subprocess.run(["qpdf", "--object-streams=generate", "--recompress-flate", "--compression-level=9", "--replace-input", f], check=False)
        b.close()
finally:
    srv.kill()
print("pdfs:", n)
