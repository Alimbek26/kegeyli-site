# Test results: hub + one page per grade (CHSB termly tests, 4 languages). Data in results_data.py.
import json
from results_data import TESTS as _T
import news as NW
import heads as HD
LANGS = ["kaa", "en", "uz", "ru"]

NAME = ("CHSB test nátiyjeleri", "CHSB Test Results", "CHSB test natijalari", "Результаты тестов CHSB")
TERMS = [dict(sub="results/term-1/", n=1, tests=[dict(t, sub=f'results/term-1/grade-{t["g"]}/') for t in _T])]
TNAME = ("{n}-sherek", "Term {r}", "{n}-chorak", "{n} четверть")
ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV"}
def tname(T, i):
    return TNAME[i].format(n=ROMAN[T["n"]], r=ROMAN[T["n"]])
TESTS = [t for T in TERMS for t in T["tests"]]
SUBS = ["results/"] + [x for T in TERMS for x in [T["sub"]] + [t["sub"] for t in T["tests"]]]
def term_of(sub):
    return next(T for T in TERMS if sub == T["sub"] or any(t["sub"] == sub for t in T["tests"]))
def crumbs(sub, i, href):
    if sub == "results/":
        return ""
    T = term_of(sub)
    c = f'<a href="{href("results/")}">{NAME[i]}</a> <span aria-hidden="true">›</span> '
    if sub != T["sub"]:
        c += f'<a href="{href(T["sub"])}">{tname(T, i)}</a> <span aria-hidden="true">›</span> '
    return c
GNAME = ("{g}-klass", "Grade {g}", "{g}-sinf", "{g} класс")
SUBJ = {  # key: (names kaa, en, uz, ru), colour, short label
 "ma": (("Matematika", "Mathematics", "Matematika", "Математика"), "#0b7a8f", "MA"),
 "alg": (("Algebra", "Algebra", "Algebra", "Алгебра"), "#0b7a8f", "ALG"),
 "geo": (("Geometriya", "Geometry", "Geometriya", "Геометрия"), "#2a7fd1", "GEO"),
 "fiz": (("Fizika", "Physics", "Fizika", "Физика"), "#d97706", "FIZ"),
 "bio": (("Biologiya", "Biology", "Biologiya", "Биология"), "#2f8f5b", "BIO"),
 "kim": (("Ximiya", "Chemistry", "Kimyo", "Химия"), "#b23a48", "KIM"),
 "en": (("Ingliz tili", "English", "Ingliz tili", "Английский язык"), "#7c3aed", "EN"),
}
ORDER = ["ma", "alg", "geo", "fiz", "bio", "kim", "en"]
CLSCOL = ["#2a7fd1", "#7c3aed", "#d97706"]
def names(i):
    d = {"results/": NAME[i]}
    for T in TERMS:
        d[T["sub"]] = tname(T, i)
        for t in T["tests"]:
            d[t["sub"]] = GNAME[i].format(g=t["g"])
    return d
def subjects(L):
    return [k for k in ORDER if any(k in x["s"] for x in L)]
def classes(L):
    return sorted({x["c"] for x in L})
DESC0 = ("{g}-klass oqıwshılarınıń CHSB test nátiyjeleri: {s}. Grafikler, bahalar hám hár bir oqıwshınıń nátiyjesi.",
         "Grade {g} CHSB test results ({s}): class averages, grades and every student’s score.",
         "{g}-sinf o‘quvchilarining CHSB test natijalari: {s}. Grafiklar, baholar va har bir o‘quvchi natijasi.",
         "Результаты теста CHSB {g} классов ({s}): средние баллы, оценки и результат каждого ученика.")
def descs():
    d = {"results/": ("CHSB test nátiyjeleri sherekler boyınsha: 5–11-klasslar, grafikler hám hár bir oqıwshınıń nátiyjesi.",
                      "CHSB test results by term for grades 5–11: charts, comparisons and every student’s score.",
                      "CHSB test natijalari choraklar bo‘yicha: 5–11-sinflar, grafiklar va har bir o‘quvchi natijasi.",
                      "Результаты тестов CHSB по четвертям: 5–11 классы, графики и результат каждого ученика.")}
    for T in TERMS:
        d[T["sub"]] = ("5–11-klasslardıń CHSB test nátiyjeleri: grafikler, salıstırıw hám eń jaqsı oqıwshılar.",
                      "CHSB test results for grades 5–11: charts, comparisons and top students.",
                      "5–11-sinflarning CHSB test natijalari: grafiklar, taqqoslash va eng yaxshi o‘quvchilar.",
                      "Результаты тестов CHSB 5–11 классов: графики, сравнение и лучшие ученики.")
    for t in TESTS:
        d[t["sub"]] = tuple(x.format(g=t["g"], s=", ".join(SUBJ[k][0][n] for k in subjects(t["rows"]))) for n, x in enumerate(DESC0))
    return d
AND = (" hám ", " and ", " va ", " и ")
def join(items, i):
    items = list(items)
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + AND[i] + items[-1]
X = {
 "tag": ("{g}-klass · {d}", "Grade {g} · {d}", "{g}-sinf · {d}", "{g} класс · {d}"),
 "h": ("CHSB testi", "CHSB test", "CHSB testi", "Тест CHSB"),
 "p": ("{c} klass oqıwshıları testti tapsırdı: {s}.", "Students of {c} took the test in {s}.", "{c} sinf o‘quvchilari testni topshirdi: {s}.", "Ученики {c} прошли тест: {s}."),
 "track": ("{c} klass — {s}", "{c}: {s}", "{c} sinf — {s}", "{c}: {s}"),
 "hub_h": ("CHSB nátiyjeleri", "CHSB results", "CHSB natijalari", "Результаты CHSB"),
 "hub_p": ("5–11-klasslar boyınsha testler. Klasstı tańlań — grafikler, bahalar hám hár bir oqıwshınıń nátiyjesi.",
           "Tests for grades 5–11. Pick a grade to see charts, grades and every student’s result.",
           "5–11-sinflar bo‘yicha testlar. Sinfni tanlang — grafiklar, baholar va har bir o‘quvchining natijasi.",
           "Тесты 5–11 классов. Выберите класс — графики, оценки и результат каждого ученика."),
 "open": ("Kóriw", "Open", "Ko‘rish", "Открыть"),
 "gcmp_h": ("Klasslar boyınsha ortasha nátiyje", "Average score by grade", "Sinflar bo‘yicha o‘rtacha natija", "Средний результат по классам"),
 "gcmp_p": ("Ulıwma nátiyje hám ingliz tili — barlıq klasslar tapsırǵan pán.", "Overall score and English — the subject every grade took.", "Umumiy natija va ingliz tili — barcha sinflar topshirgan fan.", "Общий результат и английский — предмет, который сдавали все."),
 "top5_h": ("Barlıq klasslar boyınsha eń jaqsı 10", "Top 10 across all grades", "Barcha sinflar bo‘yicha eng yaxshi 10", "Топ-10 по всем классам"),
 "subjavg_h": ("Pánler boyınsha mektep ortashası", "School average by subject", "Fanlar bo‘yicha maktab o‘rtachasi", "Средний балл школы по предметам"),
 "stud": ("oqıwshı", "students", "nafar o‘quvchi", "учеников"),
 "subj": ("pán", "subjects", "ta fan", "предметов"),
 "grs": ("klass", "grades", "ta sinf", "классов"),
 "q": ("soraw", "questions", "ta savol", "вопросов"),
 "avg": ("ortasha nátiyje", "average score", "o‘rtacha natija", "средний результат"),
 "best": ("eń joqarı nátiyje", "best score", "eng yuqori natija", "лучший результат"),
 "pass": ("3 hám onnan joqarı", "scored grade 3+", "3 va undan yuqori", "оценка 3 и выше"),
 "all": ("Ulıwma", "Overall", "Umumiy", "Общий"),
 "subj_h": ("Pánler boyınsha", "By subject", "Fanlar bo‘yicha", "По предметам"),
 "took": ("{n} oqıwshı tapsırdı", "{n} students took it", "{n} nafar topshirdi", "сдавали: {n}"),
 "passed": ("{p}% — 3 hám joqarı", "{p}% scored 3+", "{p}% — 3 va yuqori", "{p}% — 3 и выше"),
 "cmp_h": ("Klasslar salıstırması", "Class comparison", "Sinflar taqqoslanishi", "Сравнение классов"),
 "hist_h": ("Ulıwma ball bólistiriliwi", "How scores are spread", "Umumiy ball taqsimoti", "Распределение баллов"),
 "top_h": ("Eń jaqsı nátiyjeler", "Top results", "Eng yaxshi natijalar", "Лучшие результаты"),
 "list_h": ("Oqıwshılar dizimi", "All students", "O‘quvchilar ro‘yxati", "Все ученики"),
 "search": ("Atı boyınsha izlew", "Search by name", "Ism bo‘yicha qidirish", "Поиск по имени"),
 "cls": ("klass", "class", "sinf", "класс"),
 "terms_p": ("Shereklik summativ baholaw (CHSB) testleriniń nátiyjeleri. Sherekti tańlań — hár bir klass hám oqıwshı boyınsha tolıq maǵlıwmat.",
             "Results of the termly summative assessment (CHSB) tests. Pick a term to see full results for every grade and student.",
             "Choraklik summativ baholash (CHSB) testlari natijalari. Chorakni tanlang — har bir sinf va o‘quvchi bo‘yicha to‘liq ma’lumot.",
             "Результаты четвертных суммативных тестов (CHSB). Выберите четверть — полные результаты по каждому классу и ученику."),
 "avg_by": ("Klasslar boyınsha ortasha, %", "Average by grade, %", "Sinflar bo‘yicha o‘rtacha, %", "Средний балл по классам, %"),
 "cls_h": ("Klasslar", "Classes", "Sinflar", "Классы"),
 "allg": ("Barlıq klasslar", "All grades", "Barcha sinflar", "Все классы"),
 "both": ("Barlıǵı", "All classes", "Barchasi", "Все классы"),
 "correct": ("{n}/{q} durıs", "{n}/{q} correct", "{n}/{q} to‘g‘ri", "{n}/{q} верно"),
 "none": ("Hesh kim tabılmadı", "No one found", "Hech kim topilmadi", "Никто не найден"),
 "key": ("Bahalar: 5 — 86% hám joqarı, 4 — 70–85%, 3 — 55–69%, 2 — 55% ten tómen.",
         "Grades: 5 — 86% and above, 4 — 70–85%, 3 — 55–69%, 2 — below 55%.",
         "Baholar: 5 — 86% va yuqori, 4 — 70–85%, 3 — 55–69%, 2 — 55% dan past.",
         "Оценки: 5 — от 86%, 4 — 70–85%, 3 — 55–69%, 2 — ниже 55%."),
 "insight_h": ("Neni kórsetedi", "What it shows", "Nimani ko‘rsatadi", "Что это показывает"),
 "ins_s": ("{s} — eń kúshli pán: ortasha {a}%.", "{s} is the strongest subject: {a}% on average.", "{s} — eng kuchli fan: o‘rtacha {a}%.", "{s} — самый сильный предмет: в среднем {a}%."),
 "ins_w": ("{s} qosımsha itibar talap etedi: ortasha {a}%.", "{s} needs extra attention: {a}% on average.", "{s} qo‘shimcha e’tibor talab qiladi: o‘rtacha {a}%.", "{s} требует больше внимания: в среднем {a}%."),
 "ins_c": ("Eń joqarı ortasha nátiyje — {c} klassta: {a}%.", "The highest class average is {c}: {a}%.", "Eng yuqori o‘rtacha natija — {c} sinfda: {a}%.", "Лучший средний результат — у {c}: {a}%."),
 "ins_b": ("{n} oqıwshı 85% hám onnan joqarı nátiyje kórsetti.", "{n} students scored 85% or higher.", "{n} nafar o‘quvchi 85% va undan yuqori natija ko‘rsatdi.", "{n} учеников набрали 85% и выше."),
 "note": ("Derek: test platformasınıń rásmiy nátiyjeleri. Login hám jeke maǵlıwmatlar kórsetilmeydi. Bahalar procent boyınsha esaplanǵan.",
          "Source: official results from the testing platform. Logins and personal data are not shown. Grades are calculated from the percentages.",
          "Manba: test platformasining rasmiy natijalari. Login va shaxsiy ma’lumotlar ko‘rsatilmaydi. Baholar foiz bo‘yicha hisoblangan.",
          "Источник: официальные результаты тестовой платформы. Логины и личные данные не показываются. Оценки рассчитаны по процентам."),
}
GCOL = {5: "#2f8f5b", 4: "#2a7fd1", 3: "#d4a017", 2: "#d6452f"}
ECOL, MCOL = "#7c3aed", "#0b7a8f"

def grade(p):
    return 5 if p >= 86 else 4 if p >= 70 else 3 if p >= 55 else 2

def f1(x):
    return f"{x:.1f}".rstrip("0").rstrip(".") if abs(x - round(x)) < 0.05 else f"{x:.1f}"

def _svg(p, s=22, w=2):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'

I_USR = '<circle cx="9" cy="8" r="3"/><path d="M3 20c.5-3.500 3-5.500 6-5.500s5.500 2 6 5.500"/><path d="M16 6a3 3 0 0 1 0 5.500M18 14.500c1.700.8 2.700 2.500 3 5"/>'
I_STAR = '<path d="M12 3l2.700 5.600 6.100.9-4.400 4.300 1 6.100L12 17l-5.400 2.900 1-6.100L3.200 9.500l6.100-.9z"/>'
I_CHART = '<path d="M4 19V5M4 19h16M8 15v-4M12 15V8M16 15v-6"/>'
I_OK = '<path d="M5 12l5 5L20 7"/>'
I_SEARCH = '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>'
I_BULB = '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-4 10.500c.8.700 1 1.500 1 2.500h6c0-1 .2-1.800 1-2.500A6 6 0 0 0 12 3z"/>'

def hero_art():
    return ('<svg class="rsart" viewBox="0 0 240 200" aria-hidden="true">'
            '<circle cx="120" cy="104" r="86" fill="currentColor" opacity=".08"/>'
            '<g transform="rotate(-8 80 100)"><rect x="34" y="52" width="88" height="112" rx="10" fill="#0b7a8f"/><rect x="42" y="62" width="72" height="26" rx="5" fill="#e6f4f7"/>'
            '<text x="78" y="81" text-anchor="middle" font-family="Unbounded,Inter,sans-serif" font-weight="700" font-size="15" fill="#0b7a8f">+ − × ÷</text>'
            + "".join(f'<rect x="{42 + c * 19}" y="{96 + r * 17}" width="15" height="12" rx="3" fill="#fff" opacity=".85"/>' for r in range(4) for c in range(4)) +
            '</g><g transform="rotate(7 160 100)"><rect x="118" y="44" width="92" height="120" rx="8" fill="#7c3aed"/><rect x="118" y="44" width="14" height="120" rx="4" fill="#5b21b6"/>'
            '<text x="171" y="104" text-anchor="middle" font-family="Unbounded,Inter,sans-serif" font-weight="700" font-size="30" fill="#fff">ABC</text>'
            '<rect x="142" y="118" width="58" height="5" rx="2.500" fill="#fff" opacity=".6"/><rect x="142" y="129" width="42" height="5" rx="2.500" fill="#fff" opacity=".6"/></g>'
            '<g transform="rotate(35 196 40)"><rect x="188" y="8" width="14" height="62" rx="3" fill="#f2b134"/><path d="M188 70h14l-7 14z" fill="#f6d7a8"/><path d="M193 80h4l-2 4z" fill="#13232b"/><rect x="188" y="8" width="14" height="9" rx="3" fill="#d6452f"/></g>'
            '<path d="M30 30l3 7 7 1-5 5 1 7-6-3-6 3 1-7-5-5 7-1z" fill="#f2b134"/><circle cx="214" cy="170" r="6" fill="#2f8f5b"/><circle cx="22" cy="150" r="4" fill="#d6452f"/>'
            '</svg>')

def ring(p, col, size=110, label=""):
    C = 2 * 3.14159 * 42
    return (f'<div class="rsring" style="--ac:{col};width:{size}px;height:{size}px"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="42" class="r0"/>'
            f'<circle cx="50" cy="50" r="42" class="r1" stroke-dasharray="{C * p / 100:.1f} {C:.1f}" transform="rotate(-90 50 50)"/></svg><div><b>{f1(p)}%</b><small>{label}</small></div></div>')


def avg(L, f):
    v = [f(x) for x in L if f(x) is not None]
    return sum(v) / len(v) if v else 0

def body(sub, i, href):
    if sub == "results/":
        return terms_hub(i, href)
    TT = term_of(sub)
    if sub == TT["sub"]:
        return f'<p class="rsback"><a href="{href("results/")}">← {NAME[i]}</a></p>' + hub(TT, i, href)
    T = next(t for t in TT["tests"] if t["sub"] == sub)
    back = f'<p class="rsback"><a href="{href(TT["sub"])}">← {tname(TT, i)}</a></p>'
    return back + test_body(T, i)

def terms_hub(i, href):
    cards = ""
    for T in TERMS:
        ALL = [x for t in T["tests"] for x in t["rows"]]; a = avg(ALL, lambda x: x["t"])
        ds = sorted(t["date"] for t in T["tests"])
        chips = "".join(f'<span style="--gc:{gcol(t["g"])}">{t["g"]} <b>{f1(avg(t["rows"], lambda x: x["t"]))}</b></span>' for t in T["tests"])
        cards += (f'<a class="card rshc rsterm" href="{href(T["sub"])}" style="--ac:#0b7a8f"><div class="rssh">{ring(a, "#0b7a8f", 104)}<div><span class="cntag">{NW.fmt(ds[0], i)} – {NW.fmt(ds[-1], i)}</span>'
                  f'<h2>{tname(T, i)}</h2><p>{len(ALL)} {X["stud"][i]} · {len(T["tests"])} {X["grs"][i]}</p></div></div>'
                  f'<p class="rssmall" style="margin:12px 0 6px">{X["avg_by"][i]}</p><div class="rshs">{chips}</div><span class="btn p">{X["open"][i]} →</span></a>')
    TM = {T["n"]: T for T in TERMS}
    steps = "".join((f'<li class="on"><a href="{href(TM[n]["sub"])}">' if n in TM else '<li><span class="rsx">') + f'<b>{ROMAN[n]}</b><span>{TNAME[i].format(n=ROMAN[n], r=ROMAN[n])}</span>' + ('</a></li>' if n in TM else '</span></li>') for n in (1, 2, 3, 4))
    hero = (f'<div class="rshero"><div><span class="cntag">CHSB</span><h2>{NAME[i]}</h2><p>{X["terms_p"][i]}</p><ol class="rsterms">{steps}</ol></div>{hero_art()}</div>')
    return f'{hero}<div class="rshcs">{cards}</div>'


def tabs(sub, i, href):
    N = names(i)
    items = "".join(f'<a href="{href(k)}"' + (' aria-current="page"' if k == sub else "") + f'><span class="mi" style="--mc:{"#2a7fd1" if k == "results/" else "#0b7a8f"}">{_svg(I_CHART if k == "results/" else I_USR, 18)}</span>{N[k]}</a>' for k in SUBS)
    js = "<script>(function(){var a=document.querySelector('.abtabs [aria-current]');if(a){var n=a.parentNode;n.scrollLeft=a.offsetLeft-n.offsetLeft-16}})();</script>"
    return f'<nav class="abtabs" aria-label="{NAME[i]}">{items}</nav>{js}'

def gcol(g):
    return ["#7c3aed", "#0b7a8f", "#2a7fd1", "#d97706", "#2f8f5b", "#b23a48", "#d4a017"][(g - 5) % 7]

def hub(TT, i, href):
    TESTS = TT["tests"]
    ALL = [x for t in TESTS for x in t["rows"]]
    keys = subjects(ALL)
    hero = (f'<div class="rshero"><div><span class="cntag">{join([SUBJ[k][0][i] for k in keys], i)}</span><h2>{X["hub_h"][i]} · {tname(TT, i)}</h2><p>{X["hub_p"][i]}</p>'
            f'<div class="rschips"><span><b>{len(ALL)}</b> {X["stud"][i]}</span><span><b>{len(TESTS)}</b> {X["grs"][i]}</span><span><b>{len(keys)}</b> {X["subj"][i]}</span></div></div>{hero_art()}</div>')
    cards = ""
    for t in TESTS:
        L = t["rows"]; col = gcol(t["g"]); best = max(L, key=lambda x: x["t"])
        chips = "".join(f'<span style="--gc:{SUBJ[k][1]}">{SUBJ[k][2]} <b>{f1(avg(L, lambda x: x["s"].get(k)))}</b></span>' for k in subjects(L))
        cards += (f'<a class="card rshc" href="{href(t["sub"])}" style="--ac:{col}"><div class="rssh">{ring(avg(L, lambda x: x["t"]), col, 92)}<div><span class="cntag">{NW.fmt(t["date"], i)}</span>'
                  f'<h2>{GNAME[i].format(g=t["g"])}</h2><p>{len(L)} {X["stud"][i]} · {X["best"][i]} {f1(best["t"])}%</p></div></div>'
                  f'<div class="rshs">{chips}</div><span class="rsgo">{X["open"][i]} →</span></a>')
    # by grade: overall + English
    bars = ""
    for t in TESTS:
        L = t["rows"]; a, e = avg(L, lambda x: x["t"]), avg(L, lambda x: x["s"].get("en"))
        bars += (f'<div class="rsgb"><div class="rsgbb"><i style="height:{a:.1f}%;background:{gcol(t["g"])}"><em>{f1(a)}</em></i><i style="height:{e:.1f}%;background:{SUBJ["en"][1]};opacity:.6"><em>{f1(e)}</em></i></div><b>{t["g"]}</b></div>')
    leg = f'<div class="rsleg2"><span><i style="background:linear-gradient(90deg,#7c3aed,#0b7a8f,#2a7fd1,#d97706,#2f8f5b)"></i>{X["all"][i]}</span><span><i style="background:{SUBJ["en"][1]};opacity:.6"></i>{SUBJ["en"][0][i]}</span></div>'
    gchart = f'<div class="card rsgcard"><h3>{X["gcmp_h"][i]}</h3><p class="rssmall">{X["gcmp_p"][i]}</p><div class="rsgbars">{bars}</div>{leg}</div>'
    sa = "".join(f'<div class="iav"><span>{SUBJ[k][0][i]}</span><div class="iab"><i style="width:{avg(ALL, lambda x: x["s"].get(k)):.1f}%;background:{SUBJ[k][1]}"></i></div><b>{f1(avg(ALL, lambda x: x["s"].get(k)))}</b></div>' for k in sorted(keys, key=lambda k: -avg(ALL, lambda x: x["s"].get(k))))
    schart = f'<div class="card"><h3>{X["subjavg_h"][i]}</h3>{sa}</div>'
    top = sorted(ALL, key=lambda x: (-x["t"], -x["ok"]))[:10]
    tl = "".join(f'<li><span class="rsrk{" m" + str(r) if r < 4 else ""}">{r}</span><div class="rsnm"><b>{x["n"]}</b><small>{x["c"]}</small>'
                 f'<div class="rstb"><i style="width:{x["t"]}%;background:{GCOL[grade(x["t"])]}"></i></div></div><div class="rsscs"><span class="rst">{f1(x["t"])}%</span></div></li>' for r, x in enumerate(top, 1))
    allx = sorted(ALL, key=lambda x: (-x["t"], -x["ok"]))
    rows = "".join(stud_card(r, x, i, subjects([x]), gtag=True) for r, x in enumerate(allx, 1))
    gchips = f'<button type="button" class="cnchip" aria-pressed="true" data-c="all">{X["allg"][i]} <em>{len(ALL)}</em></button>' + "".join(
        f'<button type="button" class="cnchip" aria-pressed="false" data-c="{t["g"]}" style="--ac:{gcol(t["g"])}">{GNAME[i].format(g=t["g"])} <em>{len(t["rows"])}</em></button>' for t in TESTS)
    lsec = list_section(i, gchips, rows, "g")
    return (f'{hero}<div class="rshcs">{cards}</div><div class="actwo">{gchart}{schart}</div>'
            f'<h2>{X["top5_h"][i]}</h2><ol class="rslist rstop5">{tl}</ol>{lsec}')

def test_body(T, i):
    L = T["rows"]; n = len(L); g = T["g"]; CL = classes(L); KS = subjects(L)
    ccol = {c: CLSCOL[k % 3] for k, c in enumerate(CL)}
    at = avg(L, lambda x: x["t"]); best = max(L, key=lambda x: x["t"])
    passed = sum(1 for x in L if grade(x["t"]) >= 3)
    qn = max(set(x["qn"] for x in L), key=lambda q: sum(1 for x in L if x["qn"] == q))
    tracks = {}
    for c in CL:
        tracks.setdefault(tuple(k for k in KS if any(k in x["s"] for x in L if x["c"] == c)), []).append(c)
    tr = ""
    if len(tracks) > 1:
        tr = '<ul class="rstracks">' + "".join(f'<li>{X["track"][i].format(c=join(cs, i), s=join([SUBJ[k][0][i] for k in ks], i))}</li>' for ks, cs in tracks.items()) + "</ul>"
    hero = (f'<div class="rshero"><div><span class="cntag">{X["tag"][i].format(g=g, d=NW.fmt(T["date"], i))}</span><h2>{X["h"][i]}</h2>'
            f'<p>{X["p"][i].format(c=join(CL, i), s=join([SUBJ[k][0][i] for k in KS], i))}</p>{tr}'
            f'<div class="rschips"><span><b>{n}</b> {X["stud"][i]}</span><span><b>{len(KS)}</b> {X["subj"][i]}</span><span><b>{qn}</b> {X["q"][i]}</span></div></div>{hero_art()}</div>')
    tiles = "".join(f'<div class="actile" style="--ac:{c}"><span class="aci">{_svg(p)}</span><b>{v}</b><span>{l}</span></div>' for v, l, p, c in [
        (n, X["stud"][i], I_USR, "#2a7fd1"), (f'{f1(at)}%', X["avg"][i], I_CHART, "#0b7a8f"),
        (f'{f1(best["t"])}%', X["best"][i], I_STAR, "#d4a017"), (passed, X["pass"][i], I_OK, "#2f8f5b")])
    def subj_card(k):
        S = [x for x in L if k in x["s"]]; m = len(S); col = SUBJ[k][1]
        gc = {v: sum(1 for x in S if grade(x["s"][k]) == v) for v in (5, 4, 3, 2)}
        bar = "".join(f'<i style="width:{gc[v] / m * 100:.2f}%;background:{GCOL[v]}" title="{v}: {gc[v]}"></i>' for v in (5, 4, 3, 2) if gc[v])
        leg = "".join(f'<span><em style="background:{GCOL[v]}">{v}</em>{gc[v]}</span>' for v in (5, 4, 3, 2))
        pp = round((gc[5] + gc[4] + gc[3]) / m * 100)
        return (f'<div class="card rssub" style="--ac:{col}"><div class="rssh">{ring(avg(S, lambda x: x["s"][k]), col, 92)}<div><h3>{SUBJ[k][0][i]}</h3>'
                f'<p>{X["took"][i].format(n=m)}<br>{X["passed"][i].format(p=pp)}</p></div></div><div class="rsgbar">{bar}</div><div class="rsleg">{leg}</div></div>')
    ccards = ""
    for c in CL:
        S = [x for x in L if x["c"] == c]; a = avg(S, lambda x: x["t"]); hn = HD.name(c, LANGS[i]) if c in HD.HEAD else ""
        ccards += (f'<div class="card rscls" style="--ac:{ccol[c]}"><div class="rssh">{ring(a, ccol[c], 84)}<div><h3>{c} {X["cls"][i]}</h3>'
                   f'<p>{len(S)} {X["stud"][i]}</p>' + (f'<p class="rsht">{HD.T["one"][i]}: <b>{hn}</b></p>' if hn else '') + '</div></div></div>')
    clsec = f'<h2>{X["cls_h"][i]}</h2><div class="rssubs">{ccards}</div>'
    subs = f'<h2>{X["subj_h"][i]}</h2><div class="rssubs">{"".join(subj_card(k) for k in KS)}</div><p class="rskey">{X["key"][i]}</p>'
    rows = ""
    for k in ["t"] + KS:
        nm = X["all"][i] if k == "t" else SUBJ[k][0][i]; f = (lambda x: x["t"]) if k == "t" else (lambda x, k=k: x["s"].get(k))
        cb = ""
        for c in CL:
            S = [x for x in L if x["c"] == c and f(x) is not None]
            if S:
                a = avg(S, f); cb += f'<div class="rscb"><em>{c}</em><div><i style="width:{a:.1f}%;background:{ccol[c]}"></i></div><b>{f1(a)}%</b></div>'
        rows += f'<div class="rscmp"><span class="rscl">{nm}</span>{cb}</div>'
    cmp_ = f'<div class="card rscmpc"><h3>{X["cmp_h"][i]}</h3>{rows}</div>'
    bins = [(lo, lo + 10) for lo in range(0, 100, 10)]
    cnt = [sum(1 for x in L if lo <= x["t"] < hi or (hi == 100 and x["t"] == 100)) for lo, hi in bins]
    while cnt and cnt[0] == 0: cnt.pop(0); bins.pop(0)
    mx = max(cnt)
    hist = "".join(f'<div class="ihb"><span class="ihv">{c or ""}</span><i style="height:{max(c / mx * 100, 3):.0f}%;background:{GCOL[grade(lo + 5)]}"></i><b>{lo}</b></div>' for (lo, hi), c in zip(bins, cnt))
    histc = f'<div class="card"><h3>{X["hist_h"][i]}</h3><div class="ihist">{hist}</div></div>'
    sav = sorted(((k, avg(L, lambda x, k=k: x["s"].get(k))) for k in KS), key=lambda z: -z[1])
    cav = max(((c, avg([x for x in L if x["c"] == c], lambda x: x["t"])) for c in CL), key=lambda z: z[1])
    ins = [X["ins_s"][i].format(s=SUBJ[sav[0][0]][0][i], a=f1(sav[0][1])), X["ins_w"][i].format(s=SUBJ[sav[-1][0]][0][i], a=f1(sav[-1][1]))]
    if len(CL) > 1: ins.append(X["ins_c"][i].format(c=cav[0], a=f1(cav[1])))
    nb = sum(1 for x in L if x["t"] >= 85)
    if nb: ins.append(X["ins_b"][i].format(n=nb))
    insl = "".join(f'<li><span>{_svg(I_BULB, 18)}</span>{s}</li>' for s in ins)
    charts = f'<div class="actwo">{cmp_}{histc}</div><div class="card rsins"><h3>{X["insight_h"][i]}</h3><ul>{insl}</ul></div>'
    top = sorted(L, key=lambda x: (-x["t"], -x["ok"]))
    pod = ""
    for pos, x in ((2, top[1]), (1, top[0]), (3, top[2])):
        w = x["n"].split()
        pod += (f'<div class="rspod p{pos}"><span class="rsav">{(w[1][:1] if len(w) > 1 else "")}{w[0][:1]}</span><b>{x["n"]}</b><small>{x["c"]}</small>'
                f'<div class="rsstep"><em>{pos}</em><span>{f1(x["t"])}%</span></div></div>')
    podium = f'<h2>{X["top_h"][i]}</h2><div class="rspodium">{pod}</div>'
    rows = "".join(stud_card(r, x, i, KS) for r, x in enumerate(top, 1))
    chips = f'<button type="button" class="cnchip" aria-pressed="true" data-c="all">{X["both"][i]} <em>{n}</em></button>' + "".join(
        f'<button type="button" class="cnchip" aria-pressed="false" data-c="{c}" style="--ac:{ccol[c]}">{c} {X["cls"][i]} <em>{sum(1 for x in L if x["c"] == c)}</em></button>' for c in CL)
    lsec = list_section(i, chips, rows, "c")
    return f'{hero}<div class="actiles">{tiles}</div>{clsec}{subs}{charts}{podium}{lsec}'

def stud_card(r, x, i, KS, gtag=False):
    med = f' m{r}' if r < 4 else ''
    sc = "".join(f'<span class="rsg" style="--gc:{GCOL[grade(x["s"][k])]}">{SUBJ[k][2]} {f1(x["s"][k])}<em>{grade(x["s"][k])}</em></span>' for k in ORDER if k in x["s"])
    return (f'<li data-c="{x["c"]}" data-g="{x["c"].split("-")[0]}" data-q="{x["n"].lower()}"><span class="rsrk{med}">{r}</span><div class="rsnm"><b>{x["n"]}</b><small>{x["c"]} · {X["correct"][i].format(n=x["ok"], q=x["qn"])}</small>'
            f'<div class="rstb"><i style="width:{x["t"]}%;background:{GCOL[grade(x["t"])]}"></i></div></div>'
            f'<div class="rsscs"><span class="rst">{f1(x["t"])}%</span>{sc}</div></li>')

def list_section(i, chips, rows, attr):
    js = ("<script>(function(){var q=document.getElementById('rsq'),cur='all',ch=document.querySelectorAll('.rschips2 .cnchip'),li=[].slice.call(document.querySelectorAll('#rsl li'));"
          "function run(){var v=q.value.trim().toLowerCase(),n=0;li.forEach(function(x){var ok=(cur==='all'||x.dataset." + attr + "===cur)&&(!v||x.dataset.q.indexOf(v)>-1);x.hidden=!ok;if(ok){n++;var k=x.querySelector('.rsrk');k.textContent=n;k.className='rsrk'+(n<4?' m'+n:'')}});"
          "document.getElementById('rsnone').hidden=n>0}"
          "q.addEventListener('input',run);ch.forEach(function(b){b.addEventListener('click',function(){cur=b.dataset.c;ch.forEach(function(x){x.setAttribute('aria-pressed',x===b)});run()})})})();</script>")
    return (f'<h2 id="rslist">{X["list_h"][i]}</h2><label class="cnsearch">{_svg(I_SEARCH, 20)}<input type="search" id="rsq" placeholder="{X["search"][i]}" autocomplete="off"></label>'
            f'<div class="cnchips rschips2" style="margin-top:12px">{chips}</div><ol class="rslist" id="rsl">{rows}</ol><p class="cnnone" id="rsnone" hidden>{X["none"][i]}</p><p class="note">{X["note"][i]}</p>{js}')
