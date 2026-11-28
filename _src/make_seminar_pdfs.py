# Makes a printable seminar report PDF per seminar and language: files/seminars/<date>-<lang>.pdf
# Only for seminars that have content (participants or photos). Needs Chrome + Playwright.
# Run after adding attendance/photos to seminars.py, then run build.py so the page shows the button:
#   python3 _src/make_seminar_pdfs.py && python3 _src/build.py
import os, sys, subprocess, time, html
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seminars as S
import tprofile as TP, lprofile as LP
from teachers import LEADERS
from about import FULL

LANGS = ["kaa", "en", "uz", "ru"]
R = dict(
 kicker=("Kásiplik rawajlanıw kúni", "Professional Development Day", "Kasbiy rivojlanish kuni", "День профессионального развития"),
 title=("Seminar esabatı", "Seminar report", "Seminar hisoboti", "Отчёт о семинаре"),
 topic=("Tema", "Topic", "Mavzu", "Тема"),
 date=("Sánesi", "Date", "Sana", "Дата"),
 time=("Waqtı", "Time", "Vaqti", "Время"),
 trainer=("Seminar-trener", "Seminar trainer", "Seminar-trener", "Ведущий"),
 subj=("Pán", "Subject", "Fan", "Предмет"),
 count=("Qatnasıwshılar sanı", "Number of participants", "Ishtirokchilar soni", "Число участников"),
 about=("Seminar haqqında", "About the seminar", "Seminar haqida", "О семинаре"),
 photos=("Súwretler", "Photos", "Suratlar", "Фотографии"),
 list=("Qatnasıwshılar dizimi", "List of participants", "Ishtirokchilar ro‘yxati", "Список участников"),
 director=("Mektep direktorı", "School director", "Maktab direktori", "Директор школы"),
 stamp=("M.O.", "Stamp", "M.O‘.", "М.П."),
 src=("Elektron nusqa", "Online version", "Elektron nusxa", "Электронная версия"),
)
DOMAIN = "kegeyliqm.uz"


def report(s, i):
    lang = LANGS[i]; e = html.escape
    names = ", ".join(e(S.person(w, lang, lambda k: k, TP.sub_of, LP.sub_of)[0]) for w in s["who"]) or "—"
    d_la, d_cy, _ = LEADERS[0]
    director = d_cy if lang == "ru" else d_la
    att = s.get("attended", [])
    photos = s.get("photos", [])[:4]
    rows = [(R["topic"][i], e(S.topic(s, i)) or "—"), (R["date"][i], S.fmt_long(s["date"], lang)), (R["time"][i], S.TIME),
            (R["trainer"][i], names), (R["subj"][i], e(S.subj_name(s["subj"], i)))] + ([(R["count"][i], str(len(att)))] if att else [])
    meta = "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in rows)
    about = f'<h2>{R["about"][i]}</h2><p>{e(s["about"][i])}</p>' if s.get("about") else ""
    gal = (f'<h2>{R["photos"][i]}</h2><div class="gal">' + "".join(f'<img src="/_rep_{k}.jpg">' for k, f in enumerate(photos)) + "</div>") if photos else ""
    lst = (f'<div class="keep"><h2>{R["list"][i]}</h2><ol class="att">' + "".join(f"<li>{e(n)}</li>" for n in att) + "</ol></div>") if att else ""
    url = f'{DOMAIN}/{"" if lang == "kaa" else lang + "/"}{S.psub(s)}'
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page{{size:A4;margin:14mm 15mm}}*{{box-sizing:border-box}}
body{{font-family:"Liberation Sans",Arial,"DejaVu Sans",sans-serif;color:#17262c;font-size:10.5pt;line-height:1.45;margin:0}}
.hd{{display:flex;align-items:center;gap:12px;padding-bottom:10px;border-bottom:3px solid #0b5f78}}
.hd img{{width:46px;height:46px}}.hd .sc{{flex:1}}.hd b{{display:block;font-size:12pt}}.hd small{{color:#5b6b72;font-size:9pt;text-transform:uppercase;letter-spacing:.4px}}
.hd .tt{{text-align:right;font-weight:700;color:#0b5f78;font-size:13pt}}
h1{{font-size:19pt;margin:16px 0 10px;color:#0b5f78;line-height:1.2}}
h2{{font-size:11.5pt;margin:16px 0 6px;color:#0b5f78;text-transform:uppercase;letter-spacing:.4px}}
table{{width:100%;border-collapse:collapse}}th,td{{text-align:left;padding:5px 8px;border-bottom:1px solid #dfe7ea;vertical-align:top}}th{{width:34%;color:#5b6b72;font-weight:600}}
p{{margin:0}}.gal{{display:grid;grid-template-columns:1fr 1fr;gap:6px}}.gal img{{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:4px}}
.keep{{break-inside:avoid}}h2{{break-after:avoid}}.att{{columns:3;column-gap:16px;margin:0;padding-left:20px;font-size:9.5pt}}.att li{{break-inside:avoid;margin:1px 0}}
.sign{{display:flex;justify-content:space-between;align-items:flex-end;margin-top:26px;break-inside:avoid}}
.sign .ln{{display:inline-block;width:150px;border-bottom:1px solid #17262c;margin:0 8px}}.st{{width:70px;height:70px;border:1px dashed #9aabb2;border-radius:50%;display:grid;place-items:center;color:#9aabb2;font-size:9pt}}
.ft{{margin-top:14px;padding-top:6px;border-top:1px solid #dfe7ea;font-size:8.5pt;color:#5b6b72}}
</style></head><body>
<div class="hd"><img src="/logo-80.png"><div class="sc"><small>{R["kicker"][i]}</small><b>{FULL[i]}</b></div><div class="tt">{R["title"][i]}</div></div>
<h1>{e(S.topic(s, i)) or R["title"][i]}</h1><table>{meta}</table>{about}{gal}{lst}
<div class="sign"><div>{R["director"][i]}:<span class="ln"></span>{e(director)}</div><div class="st">{R["stamp"][i]}</div></div>
<div class="ft">{R["src"][i]}: {url}</div></body></html>"""


def main():
    todo = [s for s in S.SEMINARS if s.get("attended") or s.get("photos")]
    out = os.path.join(ROOT, "files", "seminars"); os.makedirs(out, exist_ok=True)
    tmp = os.path.join(ROOT, "_seminar_report_tmp.html")
    srv = subprocess.Popen([sys.executable, "-m", "http.server", "8798"], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg = b.new_page()
            from PIL import Image
            for s in todo:
                for k, f in enumerate(s.get("photos", [])[:4]):  # small copies only for the PDF
                    im = Image.open(os.path.join(ROOT, "photos", "seminars", f)).convert("RGB")
                    w, h = im.size; t = 4 / 3  # crop to 4:3 so nothing is wasted
                    if w / h > t: nw = int(h * t); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
                    im.resize((440, 330), Image.LANCZOS).save(os.path.join(ROOT, f"_rep_{k}.jpg"), quality=48, optimize=True, subsampling=2, progressive=True)
                for i, lang in enumerate(LANGS):
                    open(tmp, "w", encoding="utf-8").write(report(s, i))
                    pg.goto(f"http://localhost:8798/_seminar_report_tmp.html?v={s['date']}-{lang}"); pg.wait_for_timeout(400)
                    f = os.path.join(out, f'{s["date"]}-{lang}.pdf')
                    pg.pdf(path=f, format="A4", print_background=True, prefer_css_page_size=True)
                    subprocess.run(["qpdf", "--object-streams=generate", "--recompress-flate", "--compression-level=9", "--replace-input", f], check=False)
                    print(f, os.path.getsize(f) // 1024, "KB")
            b.close()
    finally:
        srv.terminate()
        for f in [tmp] + [os.path.join(ROOT, f"_rep_{k}.jpg") for k in range(4)]:
            if os.path.exists(f):
                os.remove(f)


if __name__ == "__main__":
    main()
