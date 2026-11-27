# School Profile 2026–2027 (English): a two-page A4 document for universities, built from the same data as the website.
# Written to school-profile/index.html; the PDF is made from it with make_profile_pdf.py.
import collections, html, json, os, statistics
import graduates as G, achieve as A, offers as OF, profile_data as PD, schoolcal as CAL
from teachers import TEACHERS

e = html.escape
YEAR = "2026–2027"
PDF = "files/kegeyli-school-profile-2026-2027.pdf"
DRAFT = False   # True adds noindex and a DRAFT ribbon

SUBJ_EN = {"Matematika": "Mathematics", "Fizika": "Physics", "Inglis til": "English", "Ana til": "Karakalpak language & literature",
           "Tariyx": "History", "Informatika": "Computer science", "Ozbek til": "Uzbek language", "Russ til": "Russian language",
           "Dene tarbiya": "Physical education", "JSHSHT": "Pre-conscription training", "Tarbiya": "Character education",
           "Biologiya": "Biology", "Ximiya": "Chemistry", "Geografiya": "Geography", "Texnologiya": "Technology", "ART": "Art"}


SHORT = {"Matematika": "mathematics", "Fizika": "physics", "Inglis til": "English", "Informatika": "computer science", "Ozbek til": "Uzbek", "Russ til": "Russian", "Ana til": "Karakalpak"}
def _join(xs):
    t = ", ".join(xs[:-1]) + " and " + xs[-1] if len(xs) > 1 else "".join(xs)
    return t[:1].upper() + t[1:]


def _weekly(root, cls):
    d = json.load(open(os.path.join(root, "timetable.json"), encoding="utf-8"))["classes"][cls]
    cnt, split = collections.Counter(), set()
    for day in d.values():
        for ls in day.values():
            names = [x[0] for x in ls]
            for s in set(names):
                cnt[s] += 1
                if names.count(s) > 1:
                    split.add(s)
    return cnt, split


def _fmt_date(d):
    y, m, dd = d.split("-")
    return f"{int(dd)} {['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][int(m)-1]} {y}"


def data(root):
    years = G.YEARS
    rec = []
    for y, n in years:
        pl = G.PLACED[y]
        kinds = collections.Counter(G.INST[k][5] for k, f in pl)
        c = G.CERTS[y]
        rec.append(dict(year=y, grads=n, uni=kinds["uni"], col=kinds["college"], cert=c["with_"], ielts=c["ielts"], sat=c["sat"]))
    last_y, last_n = years[-1]
    pl = G.PLACED[last_y]
    unis = collections.Counter(G.INST[k][1] for k, f in pl)
    fields = collections.Counter(G.FIELD[f][1] for k, f in pl)
    ncert = sum(len(c) for c in G.CERT_SUBJ[last_y])
    ielts = sorted(r[6] for r in A.IELTS)
    sat = sorted(s["total"] for s in A.SAT)
    best_sat = max(A.SAT, key=lambda s: s["total"])
    tot_g = sum(n for _, n in years); tot_p = sum(len(G.PLACED[y]) for y, _ in years)
    tot_u = sum(r["uni"] for r in rec)
    all_inst = {k for y, _ in years for k, f in G.PLACED[y]}
    return dict(rec=rec, last_y=last_y, last_n=last_n, last_uni=len(pl), unis=unis, fields=fields, ncert=ncert,
                ielts=ielts, sat=sat, best_sat=best_sat, tot_g=tot_g, tot_p=tot_p, tot_u=tot_u, n_inst=len(all_inst),
                students=sum(PD.ENROLMENT.values()), teachers=len(TEACHERS))


CSS = """
@page{size:A4;margin:0}
*{box-sizing:border-box}
body{margin:0;background:#e9eef0;font:9.2pt/1.38 Inter,"Helvetica Neue",Arial,sans-serif;color:#13232b}
.pg{width:210mm;height:297mm;margin:10mm auto;background:#fff;padding:11mm 12mm 9mm;position:relative;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.12);display:flex;flex-direction:column}
@media print{body{background:#fff}.pg{margin:0;box-shadow:none;page-break-after:always}.noprint{display:none!important}}
h1{font-size:19pt;line-height:1.1;margin:0;color:#0b5f78;letter-spacing:-.2px}
h2{font-size:10.5pt;margin:9px 0 4px;color:#0b5f78;text-transform:uppercase;letter-spacing:.6px;border-bottom:1.5px solid #0b5f78;padding-bottom:2px}
p{margin:0 0 5px}
.top{display:grid;grid-template-columns:64px 1fr auto;gap:12px;align-items:center;padding-bottom:8px;border-bottom:4px solid #a3202c}
.top img{width:64px;height:64px;border-radius:10px}
.kick{font-size:8pt;font-weight:700;letter-spacing:1.4px;color:#a3202c;text-transform:uppercase}
.sub{color:#4b5d65;font-size:8.6pt;margin-top:2px}
.ceeb{border:1.5px solid #0b5f78;border-radius:8px;padding:6px 10px;text-align:center;font-size:7.8pt;color:#4b5d65;min-width:118px}
.ceeb b{display:block;font-size:10.5pt;color:#0b5f78}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:0 14px}
.facts{display:grid;grid-template-columns:repeat(4,1fr);gap:5px;margin:6px 0 2px}
.facts div{background:#e6f2f5;border-radius:6px;padding:5px 7px}.facts b{display:block;font-size:12.5pt;color:#0b5f78;line-height:1.1}.facts span{font-size:7.6pt;color:#4b5d65}
table{width:100%;border-collapse:collapse;font-size:8.4pt;margin:2px 0 4px}
th,td{padding:2.6px 5px;border-bottom:1px solid #d7e3e7;text-align:left;vertical-align:top}
th{background:#0b5f78;color:#fff;font-weight:600;font-size:7.9pt}
td.n,th.n{text-align:right;white-space:nowrap}
tr.tot td{font-weight:700;border-top:1.5px solid #0b5f78}
.box{background:#f6f9fa;border-left:3px solid #0b5f78;padding:6px 9px;border-radius:4px;margin:4px 0}
.contact{display:grid;grid-template-columns:1fr 1fr;gap:4px 14px;font-size:8.6pt}
.contact b{color:#0b5f78}
.small{font-size:7.6pt;color:#4b5d65}
.foot{margin-top:auto;padding-top:6px;border-top:1px solid #d7e3e7;font-size:7.3pt;color:#4b5d65;display:flex;justify-content:space-between;gap:10px}
.bar{display:grid;grid-template-columns:175px 1fr 22px;gap:6px;align-items:center;font-size:8pt;margin:1.5px 0}
.bar i{display:block;height:8px;background:#0b5f78;border-radius:4px}
.star{color:#7c3aed;font-weight:700}
.ribbon{position:absolute;top:16px;right:-38px;transform:rotate(45deg);background:#a3202c;color:#fff;font-weight:800;padding:3px 44px;font-size:9pt;letter-spacing:2px}
.dl{position:fixed;right:18px;bottom:18px;background:#a3202c;color:#fff;text-decoration:none;font:600 14px Inter,Arial,sans-serif;padding:12px 18px;border-radius:999px;box-shadow:0 4px 14px rgba(0,0,0,.2)}
"""


def build(root, domain="https://kegeyliqm.uz/"):
    d = data(root)
    wk, split = _weekly(root, "11-A")
    lessons = sum(wk.values())
    t0, t1 = CAL.TERMS[0][1], CAL.TERMS[-1][2]
    rib = '<div class="ribbon">DRAFT</div>' if DRAFT else ""

    # ---------- page 1 ----------
    facts = [("2022", "Founded"), ("Grades 5–11", "Ages about 10–17"), (f"≈{d['students']}", "Students (2026–27)"), ("17", "Classes"),
             (str(d["teachers"]), "Teachers"), (f"≈{round(d['students'] / d['teachers'])} : 1", "Student–teacher ratio"),
             (f"≈{round(d['students'] / 17)}", "Students per class"), ("Karakalpak", "Language of instruction")]
    facts_h = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in facts)
    order = ["Matematika", "Fizika", "Inglis til", "Informatika", "Ana til", "Ozbek til", "Russ til", "Tariyx", "JSHSHT", "Dene tarbiya", "Tarbiya"]
    rows = "".join(f'<tr><td>{SUBJ_EN.get(s, s)}</td><td class="n">{wk[s]}</td></tr>'
                   for s in order if wk.get(s))
    grade_rows = "".join(f"<tr><td><b>{m}</b></td><td>{w}</td><td>{us}</td></tr>" for m, w, us in [
        ("5", "Excellent (a’lo)", "A"), ("4", "Good (yaxshi)", "B"), ("3", "Satisfactory (qoniqarli)", "C"), ("2", "Unsatisfactory (qoniqarsiz) — fail", "F")])
    chsb = PD.CHSB["2025/2026"][11]
    chsb_rows = "".join(f'<tr><td>{n}</td><td class="n">{v[0]}</td><td class="n">{v[1]}</td><td class="n">{v[2]}</td><td class="n">{v[3]}</td><td class="n">{v[4]}</td><td class="n">{round((v[1]*5+v[2]*4+v[3]*3+v[4]*2)/v[0],2):.2f}</td></tr>'
                        for n, v in [("Mathematics", chsb["math"]), ("Physics", chsb["phys"]), ("Chemistry", chsb["chem"])])
    c = PD.COUNSELOR
    p1 = f"""<section class="pg">{rib}
<div class="top"><img src="../logo-512.png" alt="">
<div><div class="kick">School Profile {YEAR}</div><h1>Kegeyli District Specialized School</h1>
<div class="sub">Kegeyli tumani ixtisoslashtirilgan maktabi · 9 Kegeyli Gúzari, Kegeyli, Republic of Karakalpakstan, Uzbekistan</div>
<div class="sub">kegeyliqm.uz · {c["email"]} · +998 90 654 33 98</div></div>
<div class="ceeb">College Board code<b>Applied for</b>November 2026</div></div>

<div class="cols"><div>
<h2>The school</h2>
<p>A <b>state (public) specialized secondary school</b> for exact and natural sciences, founded in 2022. It is governed by the
<b>Agency for Specialized Educational Institutions under the Ministry of Education and Science of the Republic of Uzbekistan</b>,
which runs Uzbekistan’s Presidential, creative and specialized schools. The school is in Kegeyli, a rural district of the Republic of Karakalpakstan. Since January 2026 it has been an <b>official IELTS Registration Point</b> in partnership with the British Council.</p>
<p><b>Admission is selective:</b> students enter through competitive entrance examinations held by the Agency at <b>Grade 5 and Grade 7</b>. Tuition is free.</p>
<div class="facts">{facts_h}</div>
<h2>Calendar</h2>
<p>School year {_fmt_date(t0)} – {_fmt_date(t1)}, four terms. Classes Monday–Friday, 45-minute periods. Uzbekistan has 11 years of general schooling; Grade 11 is the final year.</p>
<h2>Graduation</h2>
<p>Graduates receive the <b>State certificate (attestat) of complete general secondary education</b>, issued to students who pass all Grade 11 subjects and the state final examinations. Many also take the national subject certificate exams and international tests (IELTS, SAT).</p>
</div><div>
<h2>Curriculum</h2>
<p>National curriculum of Uzbekistan with an <b>extended programme in mathematics, physics and English</b>. All courses are compulsory; the school does not offer AP or IB courses and does not weight grades.</p>
<table><tr><th>Grades 10–11: weekly periods (45 min)</th><th class="n">Periods</th></tr>{rows}
<tr class="tot"><td>Total per week</td><td class="n">{lessons}</td></tr></table>
<p class="small">{_join([SHORT.get(x, SUBJ_EN[x]) for x in order if x in split])} are taught in half-class groups. Biology, chemistry, geography, art and technology are taught in the lower grades.</p>
<h2>Grading</h2>
<table><tr><th>Mark</th><th>Meaning</th><th>Approx. US</th></tr>{grade_rows}</table>
<p class="small">The school does not rank students. US equivalents are approximate and for guidance only.</p>
</div></div>

<h2>External assessment — Grade 11, {G.YEARS[-1][0].replace("/", "–")}</h2>
<p class="small" style="margin-bottom:2px">ChSB: the official state assessment of student knowledge, set and marked outside the school. Number of students by mark.</p>
<table><tr><th>Subject</th><th class="n">Students</th><th class="n">5</th><th class="n">4</th><th class="n">3</th><th class="n">2</th><th class="n">Average</th></tr>{chsb_rows}</table>

<h2>Contact for universities</h2>
<div class="contact"><div><b>{c["name"]}</b>, {c["role"]}<br>{c["email"]} · +998 90 654 33 98</div>
<div><b>Feruza Nizamatdinova</b>, Director<br>School office: Monday–Saturday, 08:30–17:00 (UTC+5)</div></div>
<div class="foot"><span>Kegeyli District Specialized School · School Profile {YEAR}</span><span>Page 1 of 2</span></div>
</section>"""

    # ---------- page 2 ----------
    rec_rows = "".join(f'<tr><td>{r["year"].split("/")[1]}</td><td class="n">{r["grads"]}</td><td class="n">{r["uni"]}</td><td class="n">{r["col"]}</td>'
                       f'<td class="n">{round((r["uni"] + r["col"]) / r["grads"] * 100)}%</td><td class="n">{r["cert"]}</td><td class="n">{r["ielts"]}</td><td class="n">{r["sat"]}</td></tr>' for r in d["rec"])
    tot = dict(g=sum(r["grads"] for r in d["rec"]), u=sum(r["uni"] for r in d["rec"]), c=sum(r["col"] for r in d["rec"]),
               ce=sum(r["cert"] for r in d["rec"]), i=sum(r["ielts"] for r in d["rec"]), s=sum(r["sat"] for r in d["rec"]))
    rec_rows += (f'<tr class="tot"><td>Total</td><td class="n">{tot["g"]}</td><td class="n">{tot["u"]}</td><td class="n">{tot["c"]}</td>'
                 f'<td class="n">{round((tot["u"] + tot["c"]) / tot["g"] * 100)}%</td><td class="n">{tot["ce"]}</td><td class="n">{tot["i"]}</td><td class="n">{tot["s"]}</td></tr>')
    fmax = max(d["fields"].values())
    fbars = "".join(f'<div class="bar"><span>{k}</span><i style="width:{v / fmax * 100:.0f}%"></i><b>{v}</b></div>' for k, v in d["fields"].most_common())
    top_unis = "".join(f'<tr><td>{e(k)}</td><td class="n">{v}</td></tr>' for k, v in d["unis"].most_common(6))
    other = d["last_uni"] - sum(v for k, v in d["unis"].most_common(6))
    top_unis += f'<tr><td>{len(d["unis"]) - 6} other universities</td><td class="n">{other}</td></tr>'
    by = collections.OrderedDict()
    for o in sorted(OF.OFFERS, key=lambda o: (OF.UNI[o["uni"]][1] or 9999, o["uni"])):
        by.setdefault(o["uni"], []).append(o)
    off_rows = ""
    for uni, os_ in by.items():
        u = OF.UNI[uni]; o = os_[0]
        progs = "; ".join(dict.fromkeys(x["prog"][1] for x in os_ if x.get("prog"))) or "—"
        notes = []
        for x in os_:
            n = ("Conditional offer, foundation pathway" if x.get("status") else
                 (f'${x["grant"]:,} grant' if x.get("grant") else (x["award"][1] if x.get("award") else "Admitted")))
            if n not in notes: notes.append(n)
        who = f" <span class=small>({len(os_)} students)</span>" if len({x["student"][1] for x in os_}) > 1 else ""
        qs = f'<span class="star">#{u[2]}</span>' if u[1] and u[1] <= 100 else (f"#{u[2]}" if u[1] else "—")
        off_rows += f'<tr><td>{e(uni)}{who}</td><td>{OF.COUNTRY[o["country"]][1][1]}</td><td class="n">{qs}</td><td>{e(progs)}</td><td>{"; ".join(notes)}</td></tr>'
    n_students = len({o["student"][1] for o in OF.OFFERS})
    ielts, sat = d["ielts"], d["sat"]
    bs = d["best_sat"]
    olymp = "; ".join(f'{o["name"][1]} — {A.AWARD[o["award"]][0][1].lower()}' + (f' ({o["year"].replace("/", "–")})' if o["year"] else "")
                      for o in A.OLYMP if o["stage"] in ("republic", "intl"))
    p2 = f"""<section class="pg">{rib}
<h2 style="margin-top:0">Graduates: four-year record</h2>
<table><tr><th>Class of</th><th class="n">Graduates</th><th class="n">University</th><th class="n">College</th><th class="n">Continuing</th><th class="n">With a certificate*</th><th class="n">IELTS</th><th class="n">SAT</th></tr>{rec_rows}</table>
<p class="small">“Continuing” = enrolled at a university or college in the autumn after graduation, from school records reported to the Agency. *Graduates holding at least one national subject, CEFR or IELTS certificate. IELTS and SAT columns count graduates with that test.</p>

<div class="cols"><div>
<h2>Class of {d["last_y"].split("/")[1]}</h2>
<p><b>{d["last_uni"]} of {d["last_n"]}</b> graduates ({round(d["last_uni"] / d["last_n"] * 100)}%) entered <b>{len(d["unis"])} universities</b>; the class earned <b>{d["ncert"]} national and CEFR certificates</b>.</p>
<table><tr><th>Most frequent destinations</th><th class="n">Students</th></tr>{top_unis}</table>
</div><div>
<h2>Fields of study, Class of {d["last_y"].split("/")[1]}</h2>{fbars}
</div></div>

<h2>Offers from universities abroad</h2>
<p class="small" style="margin-bottom:2px">{len(OF.OFFERS)} offers to {n_students} students of the Class of 2025 from {len({o["uni"] for o in OF.OFFERS})} universities in the USA and the UK. All three chose to study in Uzbekistan. QS = QS World University Rankings 2025; <span class="star">#</span> = world top 100.</p>
<table><tr><th>University</th><th>Country</th><th class="n">QS 2025</th><th>Programme</th><th>Offer</th></tr>{off_rows}</table>

<div class="cols"><div>
<h2>International tests</h2>
<p><b>IELTS Academic</b> — {len(ielts)} students tested: overall band {ielts[0]}–{ielts[-1]}, median {statistics.median(ielts)}; {sum(1 for x in ielts if x >= 7)} scored 7.0 or higher.</p>
<p><b>SAT</b> — {len(sat)} students tested: total {sat[0]}–{sat[-1]}, median {int(statistics.median(sat))}. Highest: {bs["total"]} ({bs["pct"]}th percentile; Math {bs["m"]}).</p>
</div><div>
<h2>Olympiads and awards</h2>
<p>{olymp}.</p>
<p>National subject certificates earned by graduates since 2023 include <b>{A._data()["top"]} at level A or A+</b> (the two highest levels).</p>
</div></div>

<div class="box"><b>Verify online.</b> Every figure in this profile is published, with details, at <b>kegeyliqm.uz/en/</b>: graduates (graduates/), certificates, IELTS and SAT results (achievements/), offers from abroad (achievements/offers/), school status (about/#status).</div>
<div class="foot"><span>Figures as of {_fmt_date(PD.AS_OF)}. Enrolment ≈ students tested in the Oct–Nov 2026 state diagnostic assessment.</span><span>Page 2 of 2</span></div>
</section>"""

    head = (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>School Profile {YEAR} — Kegeyli District Specialized School</title>'
            f'<meta name="description" content="School Profile {YEAR} of Kegeyli District Specialized School, Uzbekistan: curriculum, grading, graduates, test results and university offers.">'
            + ('<meta name="robots" content="noindex">' if DRAFT else "") +
            f'<link rel="canonical" href="{domain}school-profile/"><link rel="icon" href="../favicon-48.png"><style>{CSS}</style></head><body>')
    dl = f'<a class="dl noprint" href="../{PDF}" download>Download PDF</a>' if os.path.exists(os.path.join(root, PDF)) else ""
    out = head + p1 + p2 + dl + "</body></html>"
    os.makedirs(os.path.join(root, "school-profile"), exist_ok=True)
    open(os.path.join(root, "school-profile", "index.html"), "w", encoding="utf-8").write(out)
    return out
