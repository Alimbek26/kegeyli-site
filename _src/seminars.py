# "Kásiplik rawajlanıw kúni" (Professional Development Day): every Saturday at 10:00 one teacher runs a seminar for colleagues.
# Source: Google Sheet "Kásiplik rawajlanıw seminar waqıtları 2026-2027".
#
# To add or change a seminar, edit SEMINARS below and run: python3 _src/build.py
#   date    : "YYYY-MM-DD"
#   who     : list of trainers - a teacher's name exactly as in teachers.TEACHERS (Cyrillic),
#             or "lead:<Latin name>" for someone in teachers.LEADERS. Empty list = name not published.
#   subj    : a key of teachers.SUBJECTS, or "lead" for school leadership
#   topic   : the seminar topic as written (leave "" if not decided yet - shown as "topic to be announced")
# Past/upcoming is worked out from today's date automatically (also in the visitor's browser).
import datetime as _dt, html as _html, json
from teachers import TEACHERS, LEADERS, SUBJECTS, ROLES, latin

TIME = "10:00"
SEMINARS = [
 dict(date="2026-09-19", who=["Давирханов Женисбай"], subj="math", topic="Anıq pánlerdi oqıtıwda gamifikaciya elementlerinen paydalanıw"),
 dict(date="2026-09-26", who=["Арзибаев Толисбай"], subj="art", topic="Xudojnik Leonardo da Vinci ómiri hám dóretiwshiligi"),
 dict(date="2026-10-03", who=["Жангабаева Наргиза"], subj="rob", topic="VARK modeli hám robotlar haqqında"),
 dict(date="2026-10-10", who=["Исмайлова Гулмира", "Қутлимуратов Сарманбек"], subj="uzb", topic="«Ózbek tiline mámleketlik til biyligi berilgenine 32 jıl» tolıwı múnásibeti menen"),
 dict(date="2026-10-17", who=["Қудайбергенов Махмут"], subj="geo", topic="Racional awqatlanıw"),
 dict(date="2026-10-24", who=["Жарилқасинов Айназар"], subj="hist", topic="Tariyx pániniń rawajlanıw basqıshları: dáslepki jazıwdan jasalma intellektke shekem"),
 dict(date="2026-10-31", who=["Елмуратова Тоти"], subj="bio", topic="Qızıqlı biologiya"),
 dict(date="2026-11-07", who=["Сейтназаров Темирбек"], subj="cqt", topic="АК-47 автоматы, Ф-1 ҳәм РГД-5 қол гранаталары"),
 dict(date="2026-11-14", who=["lead:Islam Pirniyazov"], subj="lead", topic="«Pedagog maqomi»: qaror va hujjatlar bilan tanishtiruv"),
 dict(date="2026-11-28", who=["Қарлибаева Гулшахра"], subj="kaa", topic="Ana tilimiz imkaniyatları"),
 dict(date="2026-12-05", who=["Дилмуратов Дамир"], subj="math", topic=""),
 dict(date="2026-12-12", who=["Жалғасова Оркенай"], subj="eng", topic=""),
 dict(date="2026-12-19", who=["Узақбаева Айсанем"], subj="rus", topic=""),
 dict(date="2026-12-26", who=["Айназаров Қурбаназар"], subj="math", topic=""),
 dict(date="2027-01-02", who=["Бегалиева Жарқин"], subj="kaa", topic=""),
 dict(date="2027-01-09", who=["Тулепов Султан"], subj="hist", topic=""),
 dict(date="2027-01-16", who=["Умирбекова Фатима"], subj="bio", topic=""),
 dict(date="2027-01-23", who=["Артикова Шахноза"], subj="phys", topic=""),
 dict(date="2027-01-30", who=["Зарипбаев Ажиняз"], subj="inf", topic=""),
 dict(date="2027-02-06", who=["Айтмуратова Дилфуза"], subj="eng", topic=""),
 dict(date="2027-02-13", who=["Тажимуратова Зияда"], subj="chem", topic=""),
 dict(date="2027-02-20", who=["Жолдасбаев Базарбай"], subj="kaa", topic=""),
 dict(date="2027-02-27", who=["Кеунимжаев Абдуғаний"], subj="phys", topic=""),
 dict(date="2027-03-06", who=["Есбергенов Атабек"], subj="math", topic=""),
 dict(date="2027-03-13", who=["Мамутова Зинехан"], subj="eng", topic=""),
 dict(date="2027-03-20", who=["Шукириллаев Науризбай"], subj="inf", topic=""),
 dict(date="2027-03-27", who=["Сарсенбаев Данияр"], subj="phys", topic=""),
 dict(date="2027-04-03", who=["Худайбергенова Қумар"], subj="math", topic=""),
 dict(date="2027-04-10", who=["Темирханова Айнура"], subj="eng", topic=""),
 dict(date="2027-04-17", who=["Сапаров Мансур"], subj="math", topic=""),
 dict(date="2027-04-24", who=["Салиева Элмира"], subj="kaa", topic=""),
 dict(date="2027-05-01", who=["Айназаров Ажинияз"], subj="math", topic="Zamanagóy muǵallimniń 7 sırı"),
 dict(date="2027-05-08", who=["Аманбаева Қуралай"], subj="eng", topic=""),
 dict(date="2027-05-15", who=["Оразалиева Рисгул"], subj="math", topic=""),
 dict(date="2027-05-22", who=["Назбергенова Зияда"], subj="eng", topic=""),
 dict(date="2027-05-29", who=["Пиримбетов Алписбай"], subj="math", topic=""),
 dict(date="2027-06-05", who=["Осербаева Зулфия"], subj="eng", topic=""),
]

LANGS = ["kaa", "en", "uz", "ru"]
SUB = "teachers/seminars/"
NAME = ("Kásiplik rawajlanıw kúni", "Professional Development Day", "Kasbiy rivojlanish kuni", "День профессионального развития")
TAB = ("Seminarlar", "Seminars", "Seminarlar", "Семинары")
DESC = ("Hár shembi saat 10:00 de bir muǵallim kásipleslerine seminar ótkeredi: sabaq ótiw metodları hám paydalı usıllar. Seminarlar dizimi hám sáneleri.",
        "Every Saturday at 10:00 one of our teachers runs a seminar for colleagues on teaching methods and useful techniques. Schedule and topics.",
        "Har shanba soat 10:00 da bir o‘qituvchi hamkasblariga seminar o‘tkazadi: dars o‘tish metodlari va foydali usullar. Seminarlar jadvali va mavzulari.",
        "Каждую субботу в 10:00 один из учителей проводит семинар для коллег о методиках преподавания и полезных приёмах. Расписание и темы.")
T = {
 "lead": ("Hár shembi kúni saat 10:00 de mektebimizde Kásiplik rawajlanıw kúni ótkeriledi. Hár hápte bir muǵallim seminar-trener bolıp, kásipleslerine sabaq ótiw metodların, paydalı usılların hám jańa ideyaların úyretedi.",
          "Every Saturday at 10:00 our school holds a Professional Development Day. Each week one teacher leads a seminar and shares teaching methods, useful techniques and new ideas with colleagues.",
          "Har shanba kuni soat 10:00 da maktabimizda Kasbiy rivojlanish kuni o‘tkaziladi. Har hafta bir o‘qituvchi seminar-trener bo‘lib, hamkasblariga dars o‘tish metodlari, foydali usullar va yangi g‘oyalarni o‘rgatadi.",
          "Каждую субботу в 10:00 в нашей школе проходит День профессионального развития. Каждую неделю один учитель проводит семинар и делится с коллегами методиками преподавания, полезными приёмами и новыми идеями."),
 "s_held": ("seminar ótkerildi (2026/2027)", "seminars held (2026/2027)", "seminar o‘tkazildi (2026/2027)", "семинаров проведено (2026/2027)"),
 "s_next": ("seminar rejelestirilgen", "seminars planned", "seminar rejalashtirilgan", "семинаров запланировано"),
 "s_who": ("seminar-trener usı oqıw jılında", "seminar trainers this school year", "seminar-trener shu o‘quv yilida", "ведущих семинаров в этом учебном году"),
 "s_when": ("hár shembi", "every Saturday", "har shanba", "каждую субботу"),
 "next_h": ("Keyingi seminar", "Next seminar", "Navbatdagi seminar", "Следующий семинар"),
 "today": ("Búgin", "Today", "Bugun", "Сегодня"),
 "tba": ("Tema keyinirek belgilenedi", "Topic to be announced", "Mavzu keyinroq e’lon qilinadi", "Тема будет объявлена позже"),
 "up_h": ("Aldaǵı seminarlar", "Upcoming seminars", "Kelgusi seminarlar", "Предстоящие семинары"),
 "past_h": ("Ótkerilgen seminarlar", "Seminars held", "O‘tkazilgan seminarlar", "Проведённые семинары"),
 "all": ("Barlıǵı", "All", "Barchasi", "Все"),
 "lead_s": ("Basshılıq", "Leadership", "Rahbariyat", "Руководство"),
 "nobody": ("Muǵallim", "Teacher", "O‘qituvchi", "Учитель"),
 "none": ("Bul pán boyınsha seminar joq", "No seminars for this subject", "Bu fan bo‘yicha seminar yo‘q", "По этому предмету семинаров нет"),
 "lang_note": ("Seminar temaları seminar ótkerilgen tilde berilgen.", "Seminar topics are given in the language the seminar was held in.", "Seminar mavzulari seminar o‘tkazilgan tilda berilgan.", "Темы семинаров приведены на языке, на котором проходил семинар."),
 "prof_h": ("Kásiplik rawajlanıw kúni seminarları", "Professional Development Day seminars", "Kasbiy rivojlanish kuni seminarlari", "Семинары Дня профессионального развития"),
 "all_link": ("Barlıq seminarlar", "All seminars", "Barcha seminarlar", "Все семинары"),
}
MON = {"kaa": ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentyabr", "oktyabr", "noyabr", "dekabr"],
       "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
       "uz": ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentabr", "oktabr", "noyabr", "dekabr"],
       "ru": ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]}
MON_S = {"kaa": ["yan", "fev", "mar", "apr", "may", "iyun", "iyul", "avg", "sen", "okt", "noy", "dek"],
         "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
         "uz": ["yan", "fev", "mar", "apr", "may", "iyun", "iyul", "avg", "sen", "okt", "noy", "dek"],
         "ru": ["янв", "фев", "мар", "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]}
SAT = ("shembi", "Saturday", "shanba", "суббота")
SUBJ_COL = {"math": "#0b5f78", "eng": "#7c3aed", "phys": "#1d4ed8", "chem": "#0e7490", "bio": "#047857", "inf": "#2a7fd1", "rob": "#b45309",
            "kaa": "#a3202c", "uzb": "#be185d", "rus": "#92400e", "hist": "#7c2d12", "geo": "#15803d", "art": "#d97706", "pe": "#0b7a8f",
            "cqt": "#475569", "tarb": "#b23a48", "lead": "#5b6472"}

_TIDX = {t[0]: j for j, t in enumerate(TEACHERS)}
_LIDX = {l[0]: n for n, l in enumerate(LEADERS)}
for _s in SEMINARS:  # catch typos early
    for _w in _s["who"]:
        assert (_w[5:] in _LIDX) if _w.startswith("lead:") else (_w in _TIDX), "unknown trainer in seminars.py: " + _w
    assert _s["subj"] in SUBJECTS or _s["subj"] == "lead", "unknown subject in seminars.py: " + _s["subj"]

def _date(s):
    return _dt.date.fromisoformat(s)
def fmt_long(s, lang):
    d = _date(s); i = LANGS.index(lang)
    if lang == "en":
        return f"{SAT[i]}, {d.day} {MON[lang][d.month - 1]} {d.year}"
    if lang == "ru":
        return f"{d.day} {MON[lang][d.month - 1]} {d.year}, {SAT[i]}"
    return f"{d.day}-{MON[lang][d.month - 1]}, {d.year}, {SAT[i]}"
def subj_name(k, i):
    return T["lead_s"][i] if k == "lead" else SUBJECTS[k][LANGS[i]]
def person(w, lang, href, tp_sub, lp_sub):
    """(display name, link or None)"""
    if w.startswith("lead:"):
        n = _LIDX[w[5:]]; la, cy, r = LEADERS[n]
        return (cy if lang == "ru" else la), href(lp_sub(n))
    j = _TIDX[w]
    return (w if lang == "ru" else latin(w)), href(tp_sub(j))
def today():
    return _dt.date.today().isoformat()
def counts():
    t = today(); held = [s for s in SEMINARS if s["date"] < t]
    who = {w for s in SEMINARS for w in s["who"]}
    return len(held), len(SEMINARS) - len(held), len(who)

def _row(s, lang, href, tp, lp, cls=""):
    i = LANGS.index(lang); esc = _html.escape; d = _date(s["date"])
    names = []
    for w in s["who"]:
        nm, link = person(w, lang, href, tp, lp)
        names.append(f'<a href="{link}">{esc(nm)}</a>')
    who = ", ".join(names) or f'<span class="smuted">{T["nobody"][i]}</span>'
    col = SUBJ_COL.get(s["subj"], "#5b6472")
    topic = f'<p class="smtopic">{esc(s["topic"])}</p>' if s["topic"] else f'<p class="smtopic tba">{T["tba"][i]}</p>'
    return (f'<li class="smrow{cls}" data-d="{s["date"]}" data-s="{s["subj"]}" style="--sc:{col}">'
            f'<time class="smdate" datetime="{s["date"]}T{TIME}"><b>{d.day}</b><span>{MON_S[lang][d.month - 1]}</span><small>{d.year}</small></time>'
            f'<div class="smbody"><div class="smmeta"><span class="smsubj">{esc(subj_name(s["subj"], i))}</span>'
            f'<span class="smtoday" hidden>{T["today"][i]}</span></div>{topic}<p class="smwho">{who}</p></div></li>')

def _next_card(s, lang, href, tp, lp, shown):
    i = LANGS.index(lang); esc = _html.escape
    names = ", ".join(f'<a href="{l}">{esc(n)}</a>' for n, l in (person(w, lang, href, tp, lp) for w in s["who"])) or T["nobody"][i]
    topic = esc(s["topic"]) if s["topic"] else f'<span class="tba">{T["tba"][i]}</span>'
    col = SUBJ_COL.get(s["subj"], "#5b6472")
    return (f'<div class="smnext card" data-d="{s["date"]}" style="--sc:{col}"{"" if shown else " hidden"}>'
            f'<p class="smkick">{T["next_h"][i]} · <span class="smtoday" hidden>{T["today"][i]} · </span>{fmt_long(s["date"], lang)}, {TIME}</p>'
            f'<h2>{topic}</h2><p class="smwho"><span class="smsubj">{esc(subj_name(s["subj"], i))}</span> {names}</p></div>')

def body(lang, href, tp, lp):
    """Page body. href(sub) -> relative link; tp(j) / lp(n) -> sub of teacher / leader profile."""
    i = LANGS.index(lang); t = today()
    held, up, who = counts()
    past = sorted((s for s in SEMINARS if s["date"] < t), key=lambda s: s["date"], reverse=True)
    fut = sorted((s for s in SEMINARS if s["date"] >= t), key=lambda s: s["date"])
    stats = "".join(f'<div class="stat"><b{(" id=" + q) if q else ""}>{v}</b><span>{l}</span></div>' for v, l, q in [
        (held, T["s_held"][i], "smh"), (up, T["s_next"][i], "smu"), (who, T["s_who"][i], ""), (TIME, T["s_when"][i], "")])
    nexts = "".join(_next_card(s, lang, href, tp, lp, k == 0) for k, s in enumerate(fut))
    used = [k for k in list(SUBJECTS) + ["lead"] if any(s["subj"] == k for s in SEMINARS)]
    chips = (f'<button type="button" class="chip on" data-s="all">{T["all"][i]}</button>'
             + "".join(f'<button type="button" class="chip" data-s="{k}" style="--sc:{SUBJ_COL.get(k, "#5b6472")}">{_html.escape(subj_name(k, i))}</button>' for k in used))
    js = """<script>(function(){var t=new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Tashkent'}).format(new Date());
var up=document.getElementById('smup'),pa=document.getElementById('smpast');
[].slice.call(up.children).forEach(function(r){if(r.dataset.d<t){pa.insertBefore(r,pa.firstChild)}});
document.querySelectorAll('.smrow,.smnext').forEach(function(r){if(r.dataset.d===t)r.querySelectorAll('.smtoday').forEach(function(x){x.hidden=false})});
var n=null;document.querySelectorAll('.smnext').forEach(function(c){var ok=!n&&c.dataset.d>=t;if(ok)n=c;c.hidden=!ok});
document.getElementById('smh').textContent=pa.children.length;document.getElementById('smu').textContent=up.children.length;
document.getElementById('smuph').hidden=!up.children.length;document.getElementById('smpasth').hidden=!pa.children.length;
var cs=document.querySelectorAll('.smchips .chip'),run=function(k){var v=0;document.querySelectorAll('.smrow').forEach(function(r){var ok=k==='all'||r.dataset.s===k;r.hidden=!ok;if(ok)v++});document.getElementById('smnone').hidden=v>0};
cs.forEach(function(b){b.addEventListener('click',function(){cs.forEach(function(x){x.classList.toggle('on',x===b)});run(b.dataset.s)})})})();</script>"""
    return (f'<p class="lead2">{T["lead"][i]}</p><div class="stats gstats smstats">{stats}</div>{nexts}'
            f'<div class="chips smchips" role="group">{chips}</div><p class="note" id="smnone" hidden>{T["none"][i]}</p>'
            f'<h2 id="smuph"{"" if fut else " hidden"}>{T["up_h"][i]}</h2><ol class="smlist" id="smup">{"".join(_row(s, lang, href, tp, lp) for s in fut)}</ol>'
            f'<h2 id="smpasth"{"" if past else " hidden"}>{T["past_h"][i]}</h2><ol class="smlist past" id="smpast">{"".join(_row(s, lang, href, tp, lp) for s in past)}</ol>'
            f'<p class="note">{T["lang_note"][i]}</p>{js}')

def for_person(key, lang, href, tp, lp):
    """Section for a teacher / leader profile. key = Cyrillic teacher name or 'lead:<Latin name>'."""
    i = LANGS.index(lang)
    mine = sorted((s for s in SEMINARS if key in s["who"]), key=lambda s: s["date"], reverse=True)
    if not mine:
        return ""
    rows = "".join(_row(s, lang, href, tp, lp, " past" if s["date"] < today() else "") for s in mine)
    return (f'<h2>{T["prof_h"][i]}</h2><ol class="smlist">{rows}</ol>'
            f'<p><a class="btn s" href="{href(SUB)}">{T["all_link"][i]} →</a></p>')
