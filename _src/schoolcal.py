# School-year calendar (Oqıw jılı kalendarı): terms, holidays, days off, teachers' seminars.
# Source: the school's official calendar for 2026-2027 (screenshots of the "Kalendar" page).
# Each new school year: change YEAR, TERMS, BREAKS and DAYS_OFF below and run  python3 _src/build.py
import datetime as _dt, html as _html, json
import seminars as SEM
from teachers import latin, shown

YEAR = "2026/2027"
SUB = "calendar/"
ICS = "kegeyli-oqiw-jili-2026-2027.ics"
# (key, first day, last day) - lessons
TERMS = [("1", "2026-09-02", "2026-11-03"), ("2", "2026-11-10", "2026-12-27"),
         ("3", "2027-01-11", "2027-03-19"), ("4", "2027-03-29", "2027-05-25")]
# (key, first day, last day) - pupils' holidays (kanikul)
BREAKS = [("autumn", "2026-11-04", "2026-11-09"), ("winter", "2026-12-28", "2027-01-10"),
          ("spring", "2027-03-20", "2027-03-28"), ("summer", "2027-05-26", "2027-08-31")]
# Non-working days for everyone (pupils and teachers): public holidays on weekdays and decreed extra days off.
# 31.12.2026 - 02.01.2027: New Year days off under the presidential decree of 24.12.2025 on 2026 holidays.
# Navruz, Ramadan Hayit, Kurban Hayit and other 2027 days off: add when the 2027 decree is published.
DAYS_OFF = [("2026-10-01", "teachers"), ("2026-12-08", "constitution"), ("2026-12-31", "ny_extra"),
            ("2027-01-01", "newyear"), ("2027-01-02", "ny_off"), ("2027-03-08", "women")]
MONTHS = [(2026, m) for m in range(9, 13)] + [(2027, m) for m in range(1, 6)]   # September - May

LANGS = ["kaa", "en", "uz", "ru"]
NAME = ("Oqıw jılı kalendarı", "School year calendar", "O‘quv yili kalendari", "Календарь учебного года")
DESC = ("2026/2027 oqıw jılı: sherekler, kanikullar, dem alıs hám bayram kúnleri. Búgin qaysı sherek hám kanikulǵa neshe kún qalǵanın kóriń.",
        "The 2026/2027 school year: terms, holidays and days off. See which term it is today and how many days are left until the holidays.",
        "2026/2027 o‘quv yili: choraklar, ta’tillar, dam olish va bayram kunlari. Bugun qaysi chorak va ta’tilgacha necha kun qolganini ko‘ring.",
        "2026/2027 учебный год: четверти, каникулы, выходные и праздники. Узнайте, какая сейчас четверть и сколько дней до каникул.")
TERM = {"1": ("I sherek", "Term I", "I chorak", "I четверть"), "2": ("II sherek", "Term II", "II chorak", "II четверть"),
        "3": ("III sherek", "Term III", "III chorak", "III четверть"), "4": ("IV sherek", "Term IV", "IV chorak", "IV четверть")}
BREAK = {"autumn": ("Gúzgi kanikul", "Autumn holiday", "Kuzgi ta’til", "Осенние каникулы"),
         "winter": ("Qısqı kanikul", "Winter holiday", "Qishki ta’til", "Зимние каникулы"),
         "spring": ("Báhárgi kanikul", "Spring holiday", "Bahorgi ta’til", "Весенние каникулы"),
         "summer": ("Jazǵı kanikul", "Summer holiday", "Yozgi ta’til", "Летние каникулы")}
UNTIL = {"autumn": ("Gúzgi kanikulǵa shekem", "until the autumn holiday", "Kuzgi ta’tilgacha", "до осенних каникул"),
         "winter": ("Qısqı kanikulǵa shekem", "until the winter holiday", "Qishki ta’tilgacha", "до зимних каникул"),
         "spring": ("Báhárgi kanikulǵa shekem", "until the spring holiday", "Bahorgi ta’tilgacha", "до весенних каникул"),
         "summer": ("Jazǵı kanikulǵa shekem", "until the summer holiday", "Yozgi ta’tilgacha", "до летних каникул")}
OFF = {"teachers": ("Muǵallimler hám ustazlar kúni", "Teachers’ and Mentors’ Day", "O‘qituvchi va murabbiylar kuni", "День учителей и наставников"),
       "constitution": ("Konstituciya kúni", "Constitution Day", "Konstitutsiya kuni", "День Конституции"),
       "ny_extra": ("Qosımsha dem alıs kúni (Jańa jıl)", "Extra day off (New Year)", "Qo‘shimcha dam olish kuni (Yangi yil)", "Дополнительный выходной (Новый год)"),
       "newyear": ("Jańa jıl", "New Year", "Yangi yil", "Новый год"),
       "ny_off": ("Jańa jıl dem alısı", "New Year day off", "Yangi yil dam olish kuni", "Новогодний выходной"),
       "women": ("Xalıqaralıq hayal-qızlar kúni", "International Women’s Day", "Xalqaro xotin-qizlar kuni", "Международный женский день")}
TCOL = {"1": "#d99a1e", "2": "#3b6fd8", "3": "#2f9e5b", "4": "#b04ac9"}
MON = {"kaa": ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"],
       "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
       "uz": ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"],
       "ru": ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]}
WD = {"kaa": ["Dú", "Si", "Sá", "Pi", "Ju", "Sh", "Ek"], "en": ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"],
      "uz": ["Du", "Se", "Ch", "Pa", "Ju", "Sh", "Ya"], "ru": ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]}
WDF = {"kaa": ["Dúyshembi", "Siyshembi", "Sárshembi", "Piyshembi", "Juma", "Shembi", "Ekshembi"],
       "en": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
       "uz": ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"],
       "ru": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]}
T = {
 "lead": ("Mektebimizdiń {y} oqıw jılı kalendarı: sherekler, kanikullar, dem alıs hám bayram kúnleri. Sabaqlar dúyshembiden jumaǵa shekem ótedi.",
          "Our school’s calendar for the {y} school year: terms, holidays and days off. Lessons run Monday to Friday.",
          "Maktabimizning {y} o‘quv yili kalendari: choraklar, ta’tillar, dam olish va bayram kunlari. Darslar dushanbadan jumagacha o‘tadi.",
          "Календарь нашей школы на {y} учебный год: четверти, каникулы, выходные и праздники. Уроки проходят с понедельника по пятницу."),
 "today": ("Búgin", "Today", "Bugun", "Сегодня"),
 "now": ("Házir", "Now", "Hozir", "Сейчас"),
 "dayoff": ("dem alıs kúni", "day off", "dam olish kuni", "выходной"),
 "dl": ("kún qaldı", "days left", "kun qoldi", "дн. осталось"),
 "until": ("{b} baslanıwına shekem", "until the {b}", "{b}gacha", "до начала: {b}"),
 "left_l": ("{n} oqıw kúni", "{n} school days", "{n} o‘quv kuni", "{n} учебных дн."),
 "lastday": ("Búgin sherektiń sońǵı oqıw kúni", "Today is the last school day of the term", "Bugun chorakning oxirgi o‘quv kuni", "Сегодня последний учебный день четверти"),
 "resume": ("Sabaqlar {d} kúni baslanadı", "Lessons start again on {d}", "Darslar {d} kuni boshlanadi", "Уроки начнутся {d}"),
 "prog": ("{a} / {b} oqıw kúni ótti", "{a} of {b} school days done", "{a} / {b} o‘quv kuni o‘tdi", "Прошло {a} из {b} учебных дней"),
 "before": ("Oqıw jılı {d} kúni baslanadı", "The school year starts on {d}", "O‘quv yili {d} kuni boshlanadi", "Учебный год начнётся {d}"),
 "over": ("Oqıw jılı juwmaqlandı. Jaqsı dem alıń!", "The school year is over. Have a good summer!", "O‘quv yili yakunlandi. Yaxshi dam oling!", "Учебный год завершён. Хорошего лета!"),
 "year_done": ("Oqıw jılınıń {p}% ótti", "{p}% of the school year done", "O‘quv yilining {p}% o‘tdi", "Пройдено {p}% учебного года"),
 "terms_h": ("Sherekler", "Terms", "Choraklar", "Четверти"),
 "days": ("{n} oqıw kúni", "{n} school days", "{n} o‘quv kuni", "{n} учебных дней"),
 "weeks": ("{n} hápte", "{n} weeks", "{n} hafta", "{n} нед."),
 "st_done": ("Juwmaqlandı", "Finished", "Yakunlandi", "Завершена"),
 "st_now": ("Házir", "Now", "Hozir", "Сейчас"),
 "st_next": ("Aldaǵı", "Coming", "Kelgusi", "Впереди"),
 "all": ("Pútkil jıl", "Whole year", "Butun yil", "Весь год"),
 "months_h": ("Aylar boyınsha", "Month by month", "Oylar bo‘yicha", "По месяцам"),
 "hint": ("Kún haqqında bilip alıw ushın onı basıń.", "Tap a day to see what happens on it.", "Kun haqida bilish uchun uni bosing.", "Нажмите на день, чтобы узнать подробности."),
 "lg_kan": ("Kanikul", "Holiday", "Ta’til", "Каникулы"),
 "lg_off": ("Dem alıs hám bayram kúnleri", "Weekends and public holidays", "Dam olish va bayram kunlari", "Выходные и праздники"),
 "lg_sem": ("Muǵallimler seminarı (10:00)", "Teachers’ seminar (10:00)", "O‘qituvchilar seminari (10:00)", "Семинар учителей (10:00)"),
 "tw": ("oqıwshılar ushın kanikul, muǵallimler ushın jumıs kúni", "pupils’ holiday, a working day for teachers", "o‘quvchilar uchun ta’til, o‘qituvchilar uchun ish kuni", "каникулы для учеников, рабочий день для учителей"),
 "lg_today": ("Búgingi kún", "Today", "Bugungi sana", "Сегодня"),
 "sem_t": ("Seminar kúnlerin kórsetiw", "Show seminar days", "Seminar kunlarini ko‘rsatish", "Показать дни семинаров"),
 "lesson": ("sabaq kúni", "school day", "dars kuni", "учебный день"),
 "weekend": ("dem alıs kúni", "weekend", "dam olish kuni", "выходной"),
 "out": ("oqıw jılınan tısqarı", "outside the school year", "o‘quv yilidan tashqari", "вне учебного года"),
 "sem": ("Kásiplik rawajlanıw kúni: {w}, {t}", "Professional Development Day: {w}, {t}", "Kasbiy rivojlanish kuni: {w}, {t}", "День профессионального развития: {w}, {t}"),
 "breaks_h": ("Kanikullar hám bayram kúnleri", "Holidays and days off", "Ta’tillar va bayram kunlari", "Каникулы и праздники"),
 "n_days": ("{n} kún", "{n} days", "{n} kun", "{n} дн."),
 "one_day": ("1 kún", "1 day", "1 kun", "1 день"),
 "from": ("{d} kúninen", "from {d}", "{d} dan", "с {d}"),
 "ics": ("Telefon kalendarına qosıw (.ics)", "Add to phone calendar (.ics)", "Telefon kalendariga qo‘shish (.ics)", "Добавить в календарь телефона (.ics)"),
 "ics_p": ("Sherekler hám kanikullar telefonıńız yamasa Google Calendar-ǵa túsedi.", "Terms and holidays go straight into your phone or Google Calendar.", "Choraklar va ta’tillar telefoningiz yoki Google Calendar’ga tushadi.", "Четверти и каникулы попадут в календарь телефона или Google Calendar."),
 "print": ("Basıp shıǵarıw", "Print", "Chop etish", "Печать"),
 "sum_days": ("oqıw kúni", "school days", "o‘quv kuni", "учебных дней"),
 "sum_terms": ("sherek", "terms", "chorak", "четверти"),
 "sum_hol": ("kún kanikul (jazdan tısqarı)", "holiday days (not counting summer)", "kun ta’til (yozgidan tashqari)", "дней каникул (кроме летних)"),
 "sum_end": ("oqıw jılınıń sońǵı kúni", "last day of the school year", "o‘quv yilining oxirgi kuni", "последний учебный день"),
 "source": ("Derek: mekteptiń rásmiy oqıw jılı kalendarı.", "Source: the school’s official calendar for the school year.", "Manba: maktabning rasmiy o‘quv yili kalendari.", "Источник: официальный календарь учебного года школы."),
}

D = _dt.date.fromisoformat
def _rng(a, b):
    d = D(a)
    while d <= D(b):
        yield d; d += _dt.timedelta(1)
OFFSET = {D(d): k for d, k in DAYS_OFF}
def school_days(a, b):
    return [d for d in _rng(a, b) if d.weekday() < 5 and d not in OFFSET]
def classify(d):
    """('term', key) | ('break', key) | (None, None)"""
    for k, a, b in TERMS:
        if D(a) <= d <= D(b):
            return "term", k
    for k, a, b in BREAKS:
        if D(a) <= d <= D(b):
            return "break", k
    return None, None
def fdate(d, lang, wd=False, year=False):
    from seminars import MON as GEN
    i = LANGS.index(lang); m = GEN[lang][d.month - 1]
    s = f"{d.day} {m}" if lang in ("en", "ru") else f"{d.day}-{m}"
    if year:
        s += f" {d.year}" if lang in ("en", "ru") else f", {d.year}"
    if wd:
        w = WDF[lang][d.weekday()]
        s = f"{w}, {s}" if lang == "en" else f"{s}, {w.lower() if lang != 'en' else w}"
    return s

def _sem_map(lang):
    out = {}
    for s in SEM.SEMINARS:
        who = ", ".join((w[5:] if w.startswith("lead:") else shown(w, lang)) for w in s["who"]) or SEM.T["nobody"][LANGS.index(lang)]
        out[s["date"]] = (who, SEM.subj_name(s["subj"], LANGS.index(lang)), s["topic"])
    return out

def _info(d, lang, sem):
    i = LANGS.index(lang); kind, k = classify(d)
    parts = [fdate(d, lang, wd=True)]
    if d in OFFSET:
        parts += [OFF[OFFSET[d]][i]]
    elif kind == "term":
        parts += [TERM[k][i], T["lesson"][i] if d.weekday() < 5 else T["weekend"][i]]
    elif kind == "break":
        parts += [BREAK[k][i]] + ([T["tw"][i]] if k != "summer" and d.weekday() < 6 else [])
    else:
        parts += [T["out"][i]]
    s = sem.get(d.isoformat())
    if s:
        parts += [T["sem"][i].format(w=s[0], t=SEM.TIME) + (f" — {s[2]}" if s[2] else "")]
    return " · ".join(parts)

def _month(y, m, lang, sem):
    i = LANGS.index(lang); first = _dt.date(y, m, 1)
    nxt = _dt.date(y + (m == 12), m % 12 + 1, 1); n = (nxt - first).days
    terms = sorted({classify(_dt.date(y, m, dd))[1] for dd in range(1, n + 1) if classify(_dt.date(y, m, dd))[0] == "term"})
    cells = '<span class="ce"></span>' * first.weekday()
    for dd in range(1, n + 1):
        d = _dt.date(y, m, dd); kind, k = classify(d); cls = []
        if kind == "term":
            cls.append(f"t{k}")
        elif kind == "break":
            cls.append("kan")
        if d.weekday() >= 5 or d in OFFSET:
            cls.append("off")
        if d in OFFSET:
            cls.append("hol")
        iso = d.isoformat(); s = sem.get(iso)
        if s:
            cls.append("sem")
        cells += (f'<button type="button" class="cd {" ".join(cls)}" data-d="{iso}" data-i="{_html.escape(_info(d, lang, sem))}"'
                  f' aria-label="{_html.escape(_info(d, lang, sem))}">{dd}</button>')
    head = "".join(f"<span>{w}</span>" for w in WD[lang])
    return (f'<section class="cmon card" data-t="{" ".join(terms)}" data-m="{y}-{m:02d}"><h3>{MON[lang][m - 1]} <small>{y}</small></h3>'
            f'<div class="cwd">{head}</div><div class="cgrid">{cells}</div></section>')

def _timeline(lang):
    i = LANGS.index(lang); a = D(TERMS[0][1]).replace(day=1); b = _dt.date(2027, 5, 31); tot = (b - a).days + 1
    pos = lambda d: (D(d) - a).days / tot * 100
    segs = ""
    for k, s, e in TERMS:
        segs += f'<i class="tl t{k}" data-t="{k}" style="left:{pos(s):.2f}%;width:{(D(e) - D(s)).days / tot * 100 + 100 / tot:.2f}%" title="{TERM[k][i]}"><b>{TERM[k][i].split()[0] if lang != "en" else TERM[k][i].split()[1]}</b></i>'
    for k, s, e in BREAKS:
        e2 = min(D(e), b).isoformat()
        segs += f'<i class="tl kan" style="left:{pos(s):.2f}%;width:{(D(e2) - D(s)).days / tot * 100 + 100 / tot:.2f}%" title="{BREAK[k][i]}"></i>'
    ticks = "".join(f'<span style="left:{pos(f"{y}-{m:02d}-01"):.2f}%">{MON[lang][m - 1][:3]}</span>' for y, m in MONTHS)
    return (f'<div class="ctl" data-a="{a.isoformat()}" data-n="{tot}"><div class="ctlbar">{segs}<em class="ctlnow" hidden></em></div>'
            f'<div class="ctlm">{ticks}</div></div>')

def ics():
    """iCalendar file with terms, holidays and days off."""
    now = "20260901T000000Z"; ev = []
    def add(uid, a, b, title):
        e = D(b) + _dt.timedelta(1)
        ev.append(f"BEGIN:VEVENT\r\nUID:{uid}@kegeyliqm.uz\r\nDTSTAMP:{now}\r\nDTSTART;VALUE=DATE:{D(a):%Y%m%d}\r\nDTEND;VALUE=DATE:{e:%Y%m%d}\r\n"
                  f"SUMMARY:{title}\r\nTRANSP:TRANSPARENT\r\nEND:VEVENT")
    for k, a, b in TERMS:
        add(f"term{k}-{YEAR.replace('/', '-')}", a, b, f"{TERM[k][0]} ({D(a):%d.%m}–{D(b):%d.%m})")
    for k, a, b in BREAKS:
        add(f"break-{k}-{YEAR.replace('/', '-')}", a, b, BREAK[k][0])
    for d, k in DAYS_OFF:
        add(f"off-{d}", d, d, OFF[k][0])
    return ("BEGIN:VCALENDAR\r\nVERSION:2.0\r\nPRODID:-//kegeyliqm.uz//Oqiw jili kalendari//KAA\r\nCALSCALE:GREGORIAN\r\nMETHOD:PUBLISH\r\n"
            f"X-WR-CALNAME:Kegeyli mektebi — {YEAR}\r\nX-WR-TIMEZONE:Asia/Tashkent\r\n" + "\r\n".join(ev) + "\r\nEND:VCALENDAR\r\n")

def body(lang, href, up):
    i = LANGS.index(lang); esc = _html.escape; sem = _sem_map(lang)
    tdays = {k: school_days(a, b) for k, a, b in TERMS}
    total = sum(len(v) for v in tdays.values())
    holdays = sum((D(b) - D(a)).days + 1 for k, a, b in BREAKS if k != "summer")
    # ---- data for the live status (all wording prepared here, JS only picks)
    cfg = {"terms": [[k, a, b, TERM[k][i], len(tdays[k]), TCOL[k]] for k, a, b in TERMS],
           "breaks": [[k, a, b, BREAK[k][i], UNTIL[k][i]] for k, a, b in BREAKS],
           "school": sorted(d.isoformat() for v in tdays.values() for d in v),
           "dates": {d.isoformat(): fdate(d, lang, wd=True) for a in [TERMS[0][1]] for d in _rng("2026-08-01", "2027-09-05")},
           "t": {k: T[k][i] for k in ("now", "dayoff", "dl", "lastday", "left_l", "resume", "prog", "before", "over", "year_done", "today", "st_done", "st_now", "st_next")},
           "lang": lang}
    # ---- status card (filled by JS, with a build-time fallback)
    kd, kk = classify(_dt.date.today())
    now_name = TERM[kk][i] if kd == "term" else BREAK[kk][i] if kd == "break" else ""
    status = (f'<div class="cnow card" id="cnow"><div class="cnowl"><p class="cnowk" id="cnk">{T["today"][i]}</p>'
              f'<h2 id="cnh">{now_name}</h2></div>'
              f'<div class="cnowr"><div class="cnowp"><div class="cbar"><i id="cnb"></i></div><p id="cnp"></p></div>'
              f'<div class="cnowc" id="cnc"></div></div><div class="cyear"><div class="cbar thin"><i id="cny"></i></div><p id="cnd"></p></div></div>')
    summary = "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v, l in [
        (total, T["sum_days"][i]), (4, T["sum_terms"][i]), (holdays, T["sum_hol"][i]), (fdate(D(TERMS[-1][2]), lang), T["sum_end"][i])])
    # ---- term cards = filter
    tcards = f'<button type="button" class="cterm all on" data-t="all"><span class="ctn">∑</span><b>{T["all"][i]}</b><small>{YEAR}</small><em>{T["days"][i].format(n=total)}</em></button>'
    for k, a, b in TERMS:
        wk = round(((D(b) - D(a)).days + 1) / 7)
        tcards += (f'<button type="button" class="cterm" data-t="{k}" data-a="{a}" data-b="{b}" style="--tc:{TCOL[k]}"><span class="ctn">{["I", "II", "III", "IV"][int(k) - 1]}</span>'
                   f'<b>{TERM[k][i]}</b><small>{D(a):%d.%m.%Y} – {D(b):%d.%m.%Y}</small><em>{T["days"][i].format(n=len(tdays[k]))} · {T["weeks"][i].format(n=wk)}</em>'
                   f'<span class="cst" hidden></span></button>')
    months = "".join(_month(y, m, lang, sem) for y, m in MONTHS)
    legend = (f'<ul class="clegend">' + "".join(f'<li><i class="cd t{k}"></i>{TERM[k][i]}</li>' for k, a, b in TERMS)
              + f'<li><i class="cd kan"></i>{T["lg_kan"][i]}</li><li><i class="cd off"></i>{T["lg_off"][i]}</li>'
              f'<li><i class="cd sem t2"></i>{T["lg_sem"][i]}</li><li><i class="cd today"></i>{T["lg_today"][i]}</li></ul>')
    tools = (f'<div class="ctools"><label class="cswitch"><input type="checkbox" id="csem" checked> <span>{T["sem_t"][i]}</span></label>'
             f'<a class="btn s" href="{up}{ICS}" download>{T["ics"][i]}</a><button type="button" class="btn s" onclick="window.print()">{T["print"][i]}</button></div>')
    # ---- holidays list
    rows = ""
    for k, a, b in BREAKS:
        n = (D(b) - D(a)).days + 1
        when = T["from"][i].format(d=fdate(D(a), lang)) if k == "summer" else f'{fdate(D(a), lang)} – {fdate(D(b), lang, year=True)}'
        rows += (f'<li class="cbr" data-a="{a}" data-b="{b}"><span class="cbi kan"></span><div><b>{BREAK[k][i]}</b><small>{when}</small></div>'
                 + ("" if k == "summer" else f'<em>{T["n_days"][i].format(n=n)}</em>') + '</li>')
    for d, k in DAYS_OFF:
        rows += (f'<li class="cbr" data-a="{d}" data-b="{d}"><span class="cbi off"></span><div><b>{OFF[k][i]}</b><small>{fdate(D(d), lang, wd=True, year=True)}</small></div>'
                 f'<em>{T["one_day"][i]}</em></li>')
    js = "<script>window.CAL=" + json.dumps(cfg, ensure_ascii=False) + ";</script>" + _JS
    return (f'<p class="lead2">{T["lead"][i].format(y=YEAR)}</p>{status}{_timeline(lang)}'
            f'<div class="stats gstats cstats2">{summary}</div>'
            f'<h2>{T["terms_h"][i]}</h2><div class="cterms" role="group">{tcards}</div>'
            f'<h2 id="cmh">{T["months_h"][i]}</h2><p class="note">{T["hint"][i]}</p>{tools}{legend}'
            f'<div class="cinfo" id="cinfo" role="status" aria-live="polite" hidden><span></span><button type="button" aria-label="×">×</button></div>'
            f'<div class="cmonths" id="cmonths">{months}</div>'
            f'<h2>{T["breaks_h"][i]}</h2><ul class="cbreaks">{rows}</ul>'
            f'<div class="card cics"><div><b>{T["ics"][i]}</b><p>{T["ics_p"][i]}</p></div><a class="btn p" href="{up}{ICS}" download>.ics ↓</a></div>'
            f'<p class="note">{T["source"][i]}</p>{js}')

_JS = r"""<script>(function(){var C=window.CAL,t=C.t,P=new URLSearchParams(location.search).get('d'),
today=/^\d{4}-\d\d-\d\d$/.test(P||'')?P:new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Tashkent'}).format(new Date());
function dd(a,b){return Math.round((Date.parse(b)-Date.parse(a))/864e5)}
function f(s,o){return s.replace(/\{(\w)\}/g,function(m,k){return o[k]})}
var $=function(i){return document.getElementById(i)},S=C.school,first=C.terms[0][1],last=C.terms[3][2],card=$('cnow');
var cur=null,brk=null,nextT=null;C.terms.forEach(function(x){if(today>=x[1]&&today<=x[2])cur=x;if(!nextT&&x[1]>today)nextT=x});
C.breaks.forEach(function(x){if(today>=x[1]&&today<=x[2])brk=x});
var isLesson=S.indexOf(today)>=0,done=S.filter(function(d){return d<=today}).length;
function big(n,small){$('cnc').innerHTML='<b>'+n+'</b><span>'+t.dl+'</span><small>'+small+'</small>'}
$('cnk').textContent=t.today+' · '+(C.dates[today]||today)+(cur&&!isLesson?' · '+t.dayoff:'');
if(cur){card.style.setProperty('--tc',cur[5]);$('cnh').textContent=cur[3];
 var n=S.filter(function(d){return d>=cur[1]&&d<=today}).length;$('cnb').style.width=(n/cur[4]*100)+'%';$('cnp').textContent=f(t.prog,{a:n,b:cur[4]});
 var nb=C.breaks.filter(function(x){return x[1]>today})[0];
 if(nb){var lft=S.filter(function(d){return d>today&&d<nb[1]}).length;big(dd(today,nb[1]),nb[4]+' · '+(lft||!isLesson?f(t.left_l,{n:lft}):t.lastday))}}
else if(today<first){$('cnh').textContent=C.terms[0][3];big(dd(today,first),f(t.before,{d:C.dates[first]}));$('cnb').style.width='0';}
else if(brk&&nextT){card.classList.add('onbreak');$('cnh').textContent=brk[3];big(dd(today,nextT[1]),f(t.resume,{d:C.dates[nextT[1]]}));
 $('cnb').style.width=(dd(brk[1],today)+1)/(dd(brk[1],brk[2])+1)*100+'%';$('cnp').textContent=nextT[3]+' · '+C.dates[nextT[1]];}
else{card.classList.add('onbreak');$('cnh').textContent=brk?brk[3]:'';$('cnc').innerHTML='<span class="cover">'+t.over+'</span>';$('cnb').style.width='100%';$('cnp').textContent='';}
$('cnd').textContent=f(t.year_done,{p:Math.min(100,Math.round(done/S.length*100))});$('cny').style.width=Math.min(100,done/S.length*100)+'%';
var tl=document.querySelector('.ctl'),k=dd(tl.dataset.a,today)/(+tl.dataset.n)*100;if(k>=0&&k<=100){var m=document.querySelector('.ctlnow');m.style.left=k+'%';m.hidden=false}
document.querySelectorAll('.cterm[data-a]').forEach(function(b){var s=b.querySelector('.cst');s.hidden=false;
 if(today>b.dataset.b){s.textContent='✓ '+t.st_done;b.classList.add('done')}else if(today>=b.dataset.a){s.textContent=t.st_now;b.classList.add('now')}else{s.textContent=t.st_next}});
document.querySelectorAll('.cbr').forEach(function(r){if(today>r.dataset.b)r.classList.add('past');else if(today>=r.dataset.a)r.classList.add('now')});
var tc=document.querySelector('.cd[data-d="'+today+'"]');if(tc){tc.classList.add('today');tc.setAttribute('aria-current','date')}
var info=$('cinfo'),sel=null;function close(){if(sel)sel.classList.remove('sel');sel=null;info.hidden=true}
document.querySelectorAll('.cgrid .cd').forEach(function(c){c.addEventListener('click',function(e){e.stopPropagation();if(sel===c){close();return}
 if(sel)sel.classList.remove('sel');sel=c;c.classList.add('sel');info.querySelector('span').textContent=c.dataset.i;info.hidden=false})});
info.querySelector('button').addEventListener('click',close);document.addEventListener('keydown',function(e){if(e.key==='Escape')close()});
document.addEventListener('click',function(e){if(sel&&!info.contains(e.target))close()});
var bs=document.querySelectorAll('.cterm');function filt(v,scroll){bs.forEach(function(x){x.classList.toggle('on',x.dataset.t===v)});
 document.querySelectorAll('.cmon').forEach(function(m){m.hidden=v!=='all'&&m.dataset.t.split(' ').indexOf(v)<0});close();
 if(scroll)$('cmh').scrollIntoView({behavior:'smooth',block:'start'})}
bs.forEach(function(b){b.addEventListener('click',function(){filt(b.dataset.t,b.dataset.t!=='all')})});
document.querySelectorAll('.ctl .tl[data-t]').forEach(function(x){x.addEventListener('click',function(){filt(x.dataset.t,true)})});
$('csem').addEventListener('change',function(e){$('cmonths').classList.toggle('nosem',!e.target.checked)});
})();</script>"""
