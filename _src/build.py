#!/usr/bin/env python3
import datetime as _dt
"""Builds the 4-language school website.
Run from the repository root:  python3 _src/build.py
Main language (site root) = Karakalpak. Others live in /en/, /uz/, /ru/.
Edit texts in _src/texts.py, then run this script again.
"""
import json, os, sys, collections
sys.path.insert(0, os.path.dirname(__file__))
from texts import T, ORDER, MAIN
import partners as PT
import about as AU
import news as NW
import study as STD
import achieve as ACH
import canteen as CN
import bell as BL
import results as RS
import heads as HD
import tprofile as TP
import seminars as SEM
import schoolcal as CAL
import gallery as GAL
import international as INTL
import support as SUP
import counseling as CSL
import policies as POL
import clubs as CLB
import lprofile as LP
import tbadges as TB
import tgfeed as TGF
import laws as LW
from teachers import TEACHERS, LEADERS, ROLES, SUBJECTS, CATS, latin, LEADER_INFO, latin_raw as _latin_raw, shown as _shown
from profiles import PROFILES, UNI, DEG, SPEC
import re as _re, html as _html
LI = {"kaa": 0, "en": 1, "uz": 2, "ru": 3}
def path(lang):            # folder of a language ("" for the main one)
    return "" if lang == MAIN else lang + "/"
TL = {
 "edu": ("Bilimi", "Education", "Ma’lumoti", "Образование"),
 "spec": ("Qánigeligi", "Specialization", "Mutaxassisligi", "Специальность"),
 "train": ("Sońǵı malaka asırıw", "Latest professional development", "So‘nggi malaka oshirish", "Последнее повышение квалификации"),
 "ach": ("Jetiskenlikleri", "Achievements", "Yutuqlari", "Достижения"),
 "all": ("Barlıǵı", "All", "Barchasi", "Все"),
 "search": ("Atı boyınsha izlew", "Search by name", "Ism bo‘yicha qidirish", "Поиск по имени"),
 "more": ("Jáne {n}", "{n} more", "Yana {n} ta", "Ещё {n}"),
 "none": ("Hesh kim tabılmadı", "No teachers found", "Hech kim topilmadi", "Никто не найден"),
 "pos": ("Lawazımı", "Position", "Lavozimi", "Должность"),
 "since": ("Mektepte", "At the school since", "Maktabda", "В школе с"),
 "since_v": ("{y}-jıldan beri", "{y}", "{y}-yildan beri", "{y} года"),
 "staff_h": ("Administraciya hám xızmetkerler", "Administration and staff", "Ma’muriyat va xodimlar", "Администрация и сотрудники"),
 "lead_page": ("Basshılıq hám xızmetkerler", "Leadership and staff", "Rahbariyat va xodimlar", "Руководство и сотрудники"),
 "all_teachers": ("Barlıq muǵallimler", "All teachers", "Barcha o‘qituvchilar", "Все учителя"),
 "all_staff": ("Basshılıq hám barlıq xızmetkerler", "Leadership and all staff", "Rahbariyat va barcha xodimlar", "Руководство и все сотрудники"),
 "prof": ("Profildi ashıw", "Open profile", "Profilni ochish", "Открыть профиль"),
 "home": ("Bas bet", "Home", "Bosh sahifa", "Главная"),
 "teach_desc": ("{b}: {n} muǵallimniń bilimi, qánigeligi hám jetiskenlikleri.", "{b}: education, specialization and achievements of our {n} teachers.", "{b}: {n} nafar o‘qituvchining ma’lumoti, mutaxassisligi va yutuqlari.", "{b}: образование, специальность и достижения {n} учителей."),
 "lead_desc": ("{b}: mektep basshılıǵı hám xızmetkerleri.", "{b}: school leadership and staff.", "{b}: maktab rahbariyati va xodimlari.", "{b}: руководство и сотрудники школы."),
}
TOP = ("director", "dep_edu", "dep_spirit", "dep_econ")
import extra as EX
import ielts as IE
import abroad as AB
PAGES = ["", "about/", "news/", "admission/", "teachers/", "leadership/", "timetable/", "study/", "graduates/", "achievements/", "achievements/olympiads/", "achievements/certificates/", "achievements/national/", "achievements/offers/", "achievements/programmes/", "achievements/sat/", "achievements/ielts/", "abroad/", "abroad/plan/", "abroad/applications/", "abroad/scholarships/", "abroad/countries/", "abroad/calendar/", "abroad/checklist/", "abroad/calculator/", "partners/", "abroad/sat/", "abroad/essay/", "abroad/top10/", "abroad/commonapp/", "abroad/ucas/", "ielts/", "parents/", "canteen/", "canteen/not-allowed/", "documents/"] + RS.SUBS + ["teachers/class-teachers/", "teachers/by-class/", SEM.SUB, CAL.SUB, GAL.SUB, INTL.SUB, SUP.SUB, CSL.SUB, POL.SUB, CLB.SUB, CLB.JSUB] + list(TP.SUB) + list(LP.SUB) + [l["sub"] for l in LW.LAWS]
import posixpath
def href(fl, fs, tl, ts):
    a = path(fl) + fs; b = path(tl) + ts
    r = posixpath.relpath(b or ".", a.rstrip("/") or ".")
    return "./" if r == "." else r + "/"
def slug_l(n):
    return _re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")
def slug(n):
    return _re.sub(r"[^a-z0-9]+", "-", _latin_raw(n).lower().replace("ǵ", "g")).strip("-")
try:
    from texts import PHOTOS   # list of (file in /photos/, caption per language dict)
except ImportError:
    PHOTOS = []

DOMAIN = "https://kegeyliqm.uz/"
SRC = os.path.dirname(__file__)
ROOT = os.path.dirname(SRC)
STYLE = open(os.path.join(SRC, "style.css"), encoding="utf-8").read()
def gal_who(c, lang):
    """Gallery: link a person in a photo to their profile."""
    import tprofile as _TP, lprofile as _LP
    for j, tch in enumerate(TEACHERS):
        if tch[0] == c: return (_TP.sub_of(j), _TP.name(j, lang))
    for n, l in enumerate(LEADERS):
        if l[0] == c: return (f"leadership/{_LP.slug(l[0])}/", _LP.name(n, lang))
    return None
def og_img(sub):
    """Sharing image: the person's photo on teacher / leader profiles, otherwise the logo."""
    import tprofile as _TP, lprofile as _LP
    for folder, subs, key in (("teachers", _TP.SUB, lambda j: _TP.slug(TEACHERS[j][0])), ("leaders", _LP.SUB, lambda n: _LP.slug(LEADERS[n][0]))):
        if sub in subs and os.path.exists(os.path.join(ROOT, "photos", folder, key(subs[sub]) + ".jpg")):
            return f"photos/{folder}/{key(subs[sub])}.jpg"
    if sub == "counseling/":
        return "photos/leaders/alimbek-jumamuratov.jpg"
    if sub == "gallery/":
        return "photos/gallery/events/karakalpak-language-day-dance.jpg"
    return "logo-512.png"
# One shared, cacheable stylesheet instead of a copy inside every page.
# The file name carries a hash of its content, so browsers always get the new version after a change.
import hashlib as _hl, re as _re
STYLE_MIN = "\n".join(l.strip() for l in _re.sub(r"/\*.*?\*/", "", STYLE, flags=_re.S).splitlines() if l.strip())
CSS_FILE = f"style.{_hl.sha1(STYLE_MIN.encode()).hexdigest()[:10]}.css"
HERO = open(os.path.join(SRC, "hero.svg"), encoding="utf-8").read()
PHONE = "+998906543398"; PHONE_TXT = "+998 90 654 33 98"
EMAIL = "ixm013@piima.uz"; TG = "https://t.me/Kegeyliqanigelestirilgenmektebi"
MAP = "https://maps.app.goo.gl/ZpG2M65NVNU99asAA"
# Contact form: paste a free Web3Forms access key here (web3forms.com, sent to EMAIL) to deliver messages by e-mail.
# While empty, the form opens the visitor's e-mail app with the message prefilled instead.
SUBJ_VIS = {  # icon path, colour
 "math": ('<path d="M5 12h14M12 5v14"/><path d="M5 19l14-14" opacity=".35"/>', "#2a7fd1"),
 "eng": ('<path d="M4 5h16v11H9l-4 4v-4H4z"/><path d="M8 9h8M8 12h5"/>', "#7c3aed"),
 "phys": ('<circle cx="12" cy="12" r="1.800"/><ellipse cx="12" cy="12" rx="9" ry="3.800"/><ellipse cx="12" cy="12" rx="9" ry="3.800" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="9" ry="3.800" transform="rotate(120 12 12)"/>', "#0b7a8f"),
 "chem": ('<path d="M9 3h6M10 3v6L4.500 19a1.500 1.500 0 0 0 1.300 2.200h12.400a1.500 1.500 0 0 0 1.300-2.200L14 9V3M7.500 15h9"/>', "#047857"),
 "bio": ('<path d="M12 21c-5-2-8-6-8-11 5 0 8 2 8 6 0-4 3-6 8-6 0 5-3 9-8 11zM12 21v-6"/>', "#2f8f5b"),
 "inf": ('<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4M9 9l-2 2 2 2M15 9l2 2-2 2"/>', "#5b5fc7"),
 "rob": ('<rect x="5" y="8" width="14" height="11" rx="3"/><path d="M12 8V4M9 13h.01M15 13h.01M9 16h6M3 12v3M21 12v3"/>', "#d6452f"),
 "kaa": ('<path d="M4 5h6a2 2 0 0 1 2 2v13a2 2 0 0 0-2-2H4zM20 5h-6a2 2 0 0 0-2 2v13a2 2 0 0 1 2-2h6z"/>', "#d97706"),
 "uzb": ('<path d="M4 5h6a2 2 0 0 1 2 2v13a2 2 0 0 0-2-2H4zM20 5h-6a2 2 0 0 0-2 2v13a2 2 0 0 1 2-2h6z"/>', "#0b7a8f"),
 "rus": ('<path d="M4 5h16v11H9l-4 4v-4H4z"/><path d="M8 9h8M8 12h5"/>', "#b23a48"),
 "hist": ('<path d="M3 21h18M5 21V10M9 21V10M15 21V10M19 21V10M3 10l9-6 9 6z"/>', "#b45309"),
 "geo": ('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>', "#2a7fd1"),
 "art": ('<path d="M12 3a9 9 0 1 0 0 18c1.500 0 2-1 1.500-2.200-.5-1.300.300-2.300 1.700-2.300H17a4 4 0 0 0 4-4c0-5-4-9.500-9-9.500z"/><circle cx="8" cy="11" r="1"/><circle cx="12" cy="7.500" r="1"/><circle cx="16" cy="11" r="1"/>', "#be185d"),
 "pe": ('<circle cx="12" cy="12" r="9"/><path d="M12 3c-3 3-3 15 0 18M12 3c3 3 3 15 0 18M3 12h18" opacity=".6"/>', "#e07a1f"),
 "cqt": ('<path d="M12 3l8 3v6c0 5-3.500 8-8 9-4.500-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>', "#4b5563"),
 "tarb": ('<path d="M12 20s-7-4.500-7-10a4 4 0 0 1 7-2.500A4 4 0 0 1 19 10c0 5.500-7 10-7 10z"/>', "#e11d48"),
}
HKICK = {"kaa": "Anıq hám tábiyiy pánlerge qánigelestirilgen mektep", "en": "School for exact and natural sciences", "uz": "Aniq va tabiiy fanlar maktabi", "ru": "Школа точных и естественных наук"}
TSTAT = {"kaa": ("muǵallim", "pán"), "en": ("teachers", "subjects"), "uz": ("o‘qituvchi", "fan"), "ru": ("учителей", "предметов")}
FOOT = {  # tagline, school, abroad, contact, top, since
 "kaa": ("2022-jıldan beri aniq hám tábiyiy pánlerge qánigelestirilgen mektep. Matematika, inglis tili hám STEM.", "Mektep", "Shet elde oqıw", "Baylanıs", "Joqarıǵa", "2022-jıldan beri", "Sayt administratorı"),
 "en": ("A specialized school for exact and natural sciences since 2022: Maths, English and STEM.", "School", "Study abroad", "Contact", "Back to top", "Since 2022", "Website administrator"),
 "uz": ("2022-yildan beri aniq va tabiiy fanlarga ixtisoslashtirilgan maktab: matematika, ingliz tili va STEM.", "Maktab", "Xorijda o‘qish", "Aloqa", "Yuqoriga", "2022-yildan beri", "Sayt administratori"),
 "ru": ("Школа с углублённым изучением точных и естественных наук с 2022 года: математика, английский язык и STEM.", "Школа", "Учёба за рубежом", "Контакты", "Наверх", "С 2022 года", "Администратор сайта"),
}
# GoatCounter page views (goatcounter.com, code "alimbek26"). The 4 language versions of a page are counted together.
GOATCOUNTER = "alimbek26"
VIEWS_TXT = {"kaa": ("Bul bet", "Sayt boyınsha jámi", "kóriw"), "en": ("This page", "Whole site", "views"),
             "uz": ("Bu sahifa", "Sayt bo‘yicha jami", "ko‘rish"), "ru": ("Эта страница", "Весь сайт", "просмотров")}
WEB3FORMS_KEY = "a9aa2bb5-5bc2-4b33-a802-1eab51f19597"
FORM_X = {  # sending, sent, failed, mail-fallback hint
 "kaa": ("Jiberilmekte…", "Raxmet! Xabarıńız jiberildi. Tez arada baylanısamız.", "Jiberiw ámelge aspadı. Telefon yamasa Telegram arqalı jazıń.", "E-pochta programması ashıldı. Xabardı usı jerden jiberiń yamasa telefon / Telegram arqalı baylanısıń."),
 "en": ("Sending…", "Thank you! Your message was sent. We will contact you soon.", "Sending failed. Please call or write on Telegram.", "Your e-mail app has opened. Send the message from there, or contact us by phone / Telegram."),
 "uz": ("Yuborilmoqda…", "Rahmat! Xabaringiz yuborildi. Tez orada bog‘lanamiz.", "Yuborib bo‘lmadi. Telefon yoki Telegram orqali yozing.", "Elektron pochta ilovasi ochildi. Xabarni o‘sha yerdan yuboring yoki telefon / Telegram orqali bog‘laning."),
 "ru": ("Отправка…", "Спасибо! Сообщение отправлено. Мы скоро свяжемся с вами.", "Не удалось отправить. Позвоните или напишите в Telegram.", "Открылось приложение почты. Отправьте сообщение оттуда или свяжитесь по телефону / в Telegram."),
}
LAT, LNG = 42.764889, 59.623139

FLAGS = {
 "en": '<svg viewBox="0 0 60 30" aria-hidden="true"><clipPath id="ukc"><path d="M30 15h30v15zv15H0zH0V0zV0h30z"/></clipPath><path d="M0 0v30h60V0z" fill="#012169"/><path d="M0 0l60 30M60 0L0 30" stroke="#fff" stroke-width="6"/><path d="M0 0l60 30M60 0L0 30" clip-path="url(#ukc)" stroke="#C8102E" stroke-width="4"/><path d="M30 0v30M0 15h60" stroke="#fff" stroke-width="10"/><path d="M30 0v30M0 15h60" stroke="#C8102E" stroke-width="6"/></svg>',
 "uz": '<svg viewBox="0 0 250 125" aria-hidden="true"><rect width="250" height="125" fill="#1eb53a"/><rect width="250" height="85" fill="#ce1126"/><rect width="250" height="83" y="0" fill="#fff"/><rect width="250" height="42" fill="#ce1126"/><rect width="250" height="40" fill="#0099b5"/><circle cx="32" cy="20" r="14" fill="#fff"/><circle cx="37" cy="20" r="12" fill="#0099b5"/><g fill="#fff"><circle cx="78" cy="9" r="2.4"/><circle cx="88" cy="9" r="2.4"/><circle cx="98" cy="9" r="2.4"/><circle cx="68" cy="20" r="2.4"/><circle cx="78" cy="20" r="2.4"/><circle cx="88" cy="20" r="2.4"/><circle cx="98" cy="20" r="2.4"/><circle cx="58" cy="31" r="2.4"/><circle cx="68" cy="31" r="2.4"/><circle cx="78" cy="31" r="2.4"/><circle cx="88" cy="31" r="2.4"/><circle cx="98" cy="31" r="2.4"/></g></svg>',
 "kaa": '<svg viewBox="0 0 250 125" aria-hidden="true"><rect width="250" height="125" fill="#1eb53a"/><rect width="250" height="85" fill="#fff"/><rect width="250" height="83" fill="#ce1126"/><rect width="250" height="81" fill="#f2c200"/><rect width="250" height="44" fill="#ce1126"/><rect width="250" height="42" fill="#fff"/><rect width="250" height="40" fill="#0099b5"/><circle cx="32" cy="20" r="14" fill="#fff"/><circle cx="37" cy="20" r="12" fill="#0099b5"/><g fill="#fff"><circle cx="66" cy="13" r="3.2"/><circle cx="80" cy="13" r="3.2"/><circle cx="59" cy="27" r="3.2"/><circle cx="73" cy="27" r="3.2"/><circle cx="87" cy="27" r="3.2"/></g></svg>',
 "ru": '<svg viewBox="0 0 9 6" aria-hidden="true"><rect width="9" height="6" fill="#d52b1e"/><rect width="9" height="4" fill="#0039a6"/><rect width="9" height="2" fill="#fff"/></svg>',
}



_I = lambda d: f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
NAV_ICON = {
 "study": (_I('<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.500 2M9 2h6"/>'), "#d97706"),
 "about": (_I('<path d="M3 21h18"/><path d="M5 21V10l7-5 7 5v11"/><path d="M9 21v-6h6v6"/><path d="M12 5V2"/>'), "#0b5f78"),
 "subjects": (_I('<path d="M9 3h6"/><path d="M10 3v6L4.5 19a1.5 1.5 0 0 0 1.3 2.2h12.4a1.5 1.5 0 0 0 1.3-2.2L14 9V3"/><path d="M7.5 15h9"/>'), "#047857"),
 "results": (_I('<path d="M8 21h8"/><path d="M12 17v4"/><path d="M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M17 5h3v2a3 3 0 0 1-3 3"/><path d="M7 5H4v2a3 3 0 0 0 3 3"/>'), "#b45309"),
 "leadership": (_I('<path d="M3 7l4 4 5-7 5 7 4-4-2 12H5z"/>'), "#7c3aed"),
 "teachers": (_I('<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8"/><path d="M12 16v4"/><path d="M7 9h6"/><path d="M7 12h4"/>'), "#1d4ed8"),
 "gallery": (_I('<rect x="3" y="5" width="18" height="15" rx="2"/><circle cx="9" cy="10" r="1.8"/><path d="M21 16l-5-5-9 9"/>'), "#db2777"),
 "calendar": (_I('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/><circle cx="12" cy="15.5" r="2"/>'), "#4f63d6"),
 "timetable": (_I('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18"/><path d="M8 3v4"/><path d="M16 3v4"/><path d="M8 14h3"/><path d="M13 14h3"/><path d="M8 17.5h3"/>'), "#0e7490"),
 "graduates": (_I('<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11.2V16c0 1.2 2.7 3 6 3s6-1.8 6-3v-4.8"/><path d="M22 9v6"/>'), "#be185d"),
 "counseling": (_I(CSL.ICON[0]), CSL.ICON[1]),
 "policies": (_I(POL.ICON[0]), POL.ICON[1]),
 "clubs": (_I(CLB.ICON[0]), CLB.ICON[1]),
 "abroad": (_I('<path d="M22 2L11 13"/><path d="M22 2l-7 20-4-9-9-4z"/>'), "#0891b2"),
 "ielts": (_I('<path d="M21 12a8 8 0 0 1-8 8H5l-2 2V12a8 8 0 0 1 8-8h2a8 8 0 0 1 8 8z"/><path d="M8.5 14.5l2-5 2 5"/><path d="M9.2 13h2.6"/><path d="M15 9.5v5"/>'), "#0891b2"),
 "parents": (_I('<circle cx="9" cy="8" r="3"/><path d="M3 20v-1a5 5 0 0 1 5-5h2a5 5 0 0 1 5 5v1"/><circle cx="17.5" cy="9.5" r="2.2"/><path d="M17 14.2a4 4 0 0 1 4 3.8v1.5"/>'), "#d97706"),
 "tests": (_I('<path d="M9 3h6v3H9zM7 5H5v16h14V5h-2"/><path d="M8 13l2.500 2.500L16 10"/>'), "#2a7fd1"),
 "canteen": (_I('<path d="M3 11h18a9 9 0 0 1-18 0z"/><path d="M8 7c0-2 2-2 2-4M13 7c0-2 2-2 2-4"/>'), "#2f8f5b"),
 "documents": (_I('<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M12 11v5"/><path d="M9.5 13.8L12 16.3l2.5-2.5"/>'), "#0369a1"),
 "admission": (_I('<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5"/><path d="M9 13h7"/><path d="M9 17h5"/>'), "#a3202c"),
 "news": (_I('<path d="M4 5h13v14H6a2 2 0 0 1-2-2z"/><path d="M17 9h3v8a2 2 0 0 1-2 2"/><path d="M8 9h5"/><path d="M8 13h5"/>'), "#92400e"),
 "partners": (_I('<path d="M8 12l3 3 5-6"/><path d="M3 12a4 4 0 0 1 4-4h2M21 12a4 4 0 0 1-4 4h-2M7 16h2M15 8h2"/>'), "#2a7fd1"),
 "contact": (_I('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>'), "#475569"),
}
FACT_ICON = {
 "pin": (_I('<path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>'), "#d6452f"),
 "focus": (_I('<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>'), "#047857"),
 "meal": (_I('<path d="M7 3v8M4 3v5a3 3 0 0 0 6 0V3M7 11v10"/><path d="M17 21V3c-2.5 1.5-3.5 4-3.5 7v3H17"/>'), "#b45309"),
 "clock": (_I('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'), "#7c3aed"),
 "cal": (_I('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>'), "#0e7490"),
 "phone": (_I('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>'), "#1d4ed8"),
 "mail": (_I('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>'), "#be185d"),
 "tg": (_I('<path d="M22 2L11 13"/><path d="M22 2l-7 20-4-9-9-4z"/>'), "#0891b2"),
 "map": (_I('<path d="M9 4l-6 2v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>'), "#047857"),
}
def fi(k): return f'<span class="mi" style="--mc:{FACT_ICON[k][1]}">{FACT_ICON[k][0]}</span>'
ROLE_ICON = {   # (icon svg, colour class)
 "director":   (_I('<path d="M12 2.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 15.9l-5.2 2.7 1-5.8L3.5 8.7l5.9-.9z"/>'), "ic-gold"),
 "dep_edu":    (_I('<path d="M2.5 5.5c3-1.3 6.2-1.3 9.5.8v13c-3.3-2.1-6.5-2.1-9.5-.8z"/><path d="M21.5 5.5c-3-1.3-6.2-1.3-9.5.8v13c3.3-2.1 6.5-2.1 9.5-.8z"/>'), "ic-teal"),
 "adviser":    (_I('<path d="M4 5h11a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H9l-4 3v-3H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z"/><path d="M17 9h3a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-1v3l-3.5-3H13"/>'), "ic-red"),
 "dep_spirit": (_I('<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.6.5 1.1 1.3 1.1 2.2h5c0-.9.5-1.7 1.1-2.2A6 6 0 0 0 12 3z"/>'), "ic-teal"),
 "psych":      (_I('<path d="M12 20s-7.5-4.6-7.5-10.2A4.3 4.3 0 0 1 12 7a4.3 4.3 0 0 1 7.5 2.8C19.5 15.4 12 20 12 20z"/><path d="M7.5 11.5h2.5l1.5-2.5 2 5 1.5-2.5h1.5"/>'), "ic-red"),
 "dep_econ":   (_I('<path d="M14.7 6.3a4 4 0 0 0-5.3 5.3L3 18l3 3 6.4-6.4a4 4 0 0 0 5.3-5.3l-2.5 2.5-2.5-.5-.5-2.5z"/>'), "ic-teal"),
 "librarian":  (_I('<rect x="3" y="4" width="4" height="16" rx="1"/><rect x="8.5" y="4" width="4" height="16" rx="1"/><path d="M14.5 5.2l3.8-1 3.2 15.3-3.8 1z"/>'), "ic-gold"),
 "accountant": (_I('<rect x="5" y="2.5" width="14" height="19" rx="2"/><rect x="8" y="5.5" width="8" height="4" rx="1"/><path d="M8.5 13h.01M12 13h.01M15.5 13h.01M8.5 16.5h.01M12 16.5h.01M15.5 16.5h.01"/>'), "ic-gold"),
 "hr":         (_I('<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.6-3.6 3.2-5.5 6.5-5.5s5.9 1.9 6.5 5.5"/><path d="M16 4.6a3.5 3.5 0 0 1 0 6.8M18.5 14.8c1.7.8 2.7 2.6 3 5.2"/>'), "ic-red"),
 "cqt_head":   (_I('<path d="M12 2.5l8 3v6c0 5-3.4 8.6-8 10-4.6-1.4-8-5-8-10v-6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>'), "ic-teal"),
}

TT = json.load(open(os.path.join(SRC, "timetable.json"), encoding="utf-8"))
TP_M = TP.tt_index(TT)
def _dir_ach():
    allr = [x for t in RS.TESTS for x in t["rows"]]
    return {"sat": ACH.BEST, "ielts": f'{max(x[6] for x in ACH.IELTS):.1f}', "cert": ACH.EXAMS[0], "chsb": f'{sum(x["t"] for x in allr) / len(allr):.1f}%'}
DIR_ACH = _dir_ach()
TT_SUBJ = {   # sheet name -> (kaa, en, uz, ru, colour)
 "Ana til": ("Ana tili", "Native language", "Ona tili", "Родной язык", "#a3202c"),
 "Ozbek til": ("Ózbek tili", "Uzbek", "O‘zbek tili", "Узбекский язык", "#c2410c"),
 "Russ til": ("Rus tili", "Russian", "Rus tili", "Русский язык", "#b45309"),
 "Inglis til": ("Ingliz tili", "English", "Ingliz tili", "Английский язык", "#7c3aed"),
 "Matematika": ("Matematika", "Mathematics", "Matematika", "Математика", "#0b5f78"),
 "Informatika": ("Informatika", "Computer science", "Informatika", "Информатика", "#0e7490"),
 "Fizika": ("Fizika", "Physics", "Fizika", "Физика", "#1d4ed8"),
 "Ximiya": ("Ximiya", "Chemistry", "Kimyo", "Химия", "#047857"),
 "Biologiya": ("Biologiya", "Biology", "Biologiya", "Биология", "#15803d"),
 "Geografiya": ("Geografiya", "Geography", "Geografiya", "География", "#4d7c0f"),
 "Tariyx": ("Tariyx", "History", "Tarix", "История", "#92400e"),
 "Tarbiya": ("Tárbiya", "Character education", "Tarbiya", "Воспитание", "#be185d"),
 "Dene tarbiya": ("Dene tárbiyası", "Physical education", "Jismoniy tarbiya", "Физкультура", "#dc2626"),
 "JSHSHT": ("Shaqırıwǵa shekemgi tayarlıq", "Pre-conscription training", "Chaqiruvga qadar tayyorgarlik", "Допризывная подготовка", "#475569"),
 "ART": ("ART", "Art", "ART", "ИЗО (ART)", "#db2777"),
 "Texnologiya": ("Texnologiya", "Technology", "Texnologiya", "Технология", "#6d28d9"),
}
TT_ICON = {  # subject sheet name -> svg inner paths (24x24, stroke)
 "Ana til": '<path d="M12 6c-2-1.500-5-2-8-1.500V18c3-.5 6 0 8 1.500 2-1.500 5-2 8-1.500V4.500C17 4 14 4.500 12 6z"/><path d="M12 6v13.500"/>',
 "Ozbek til": '<path d="M12 6c-2-1.500-5-2-8-1.500V18c3-.5 6 0 8 1.500 2-1.500 5-2 8-1.500V4.500C17 4 14 4.500 12 6z"/><path d="M12 6v13.500"/>',
 "Russ til": '<path d="M12 6c-2-1.500-5-2-8-1.500V18c3-.5 6 0 8 1.500 2-1.500 5-2 8-1.500V4.500C17 4 14 4.500 12 6z"/><path d="M12 6v13.500"/>',
 "Inglis til": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
 "Matematika": '<path d="M5 8h6M8 5v6M14 5.500l5 5M19 5.500l-5 5M5 18h6M14 18h5"/>',
 "Informatika": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 "Fizika": '<circle cx="12" cy="12" r="1.800"/><ellipse cx="12" cy="12" rx="9" ry="3.800"/><ellipse cx="12" cy="12" rx="9" ry="3.800" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="9" ry="3.800" transform="rotate(120 12 12)"/>',
 "Ximiya": '<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3"/><path d="M8 15h8"/>',
 "Biologiya": '<path d="M5 19c0-8 5-13 14-14 0 9-5 14-13 14z"/><path d="M5 19c3-5 6-8 10-10"/>',
 "Geografiya": '<path d="M12 21s-6-5.600-6-10.500a6 6 0 0 1 12 0C18 15.400 12 21 12 21z"/><circle cx="12" cy="10.500" r="2.200"/>',
 "Tariyx": '<path d="M3 21h18M5 21V10M9 21V10M15 21V10M19 21V10M3 10l9-6 9 6"/>',
 "Tarbiya": '<path d="M12 20s-7-4.500-7-10a4 4 0 0 1 7-2.500A4 4 0 0 1 19 10c0 5.500-7 10-7 10z"/>',
 "Dene tarbiya": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3v18"/>',
 "JSHSHT": '<path d="M12 3l8 3v6c0 4.500-3.500 8-8 9-4.500-1-8-4.500-8-9V6z"/>',
 "ART": '<path d="M12 3a9 9 0 1 0 0 18c1.500 0 2-1 1.500-2s0-2 1.500-2h2a3 3 0 0 0 3-3c0-5-4-11-8-11z"/><circle cx="7.500" cy="11" r="1"/><circle cx="11" cy="7" r="1"/><circle cx="16" cy="8.500" r="1"/>',
 "Texnologiya": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.200 4.200l2.100 2.100M17.700 17.700l2.100 2.100M2 12h3M19 12h3M4.200 19.800l2.100-2.100M17.700 6.300l2.100-2.100"/>',
}
BELLS = [("9:00", "9:45"), ("9:50", "10:35"), ("10:40", "11:25"), ("11:35", "12:20"),
         ("12:25", "13:10"), ("13:40", "14:25"), ("14:30", "15:15"), ("15:20", "16:05")]   # lesson 1..8
TT_TXT = {
 "now": ("Házir", "Now", "Hozir", "Сейчас"),
 "ht": ("Klass basshısı", "Class teacher", "Sinf rahbari", "Классный руководитель"),
 "tom": ("Erteń", "Tomorrow", "Ertaga", "Завтра"),
 "m_free": ("Bos muǵallimler", "Free teachers", "Bo‘sh o‘qituvchilar", "Свободные учителя"),
 "fp_h": ("Sabaqlardı tańlań", "Choose periods", "Darslarni tanlang", "Выберите уроки"),
 "fp_hint": ("Kún hám sabaqlardı tańlań — sol waqıtta sabaǵı joq muǵallimler kórsetiledi.", "Pick a day and one or more periods to see which teachers have no lesson then.", "Kun va darslarni tanlang — o‘sha vaqtda darsi yo‘q o‘qituvchilar ko‘rsatiladi.", "Выберите день и уроки — покажем учителей, у которых в это время нет урока."),
 "fsubj": ("Barlıq pánler", "All subjects", "Barcha fanlar", "Все предметы"),
 "free_n": ("{n} muǵallim bos", "{n} teachers free", "{n} nafar o‘qituvchi bo‘sh", "Свободно учителей: {n}"),
 "teach_day": ("Bul kúni sabaǵı bar", "Teaching this day", "Bu kuni darsi bor", "Ведут уроки в этот день"),
 "no_day": ("Bul kúni sabaǵı joq", "No lessons this day", "Bu kuni darsi yo‘q", "В этот день без уроков"),
 "l_day": ("bul kúni {n} sabaq", "{n} lessons this day", "bu kuni {n} ta dars", "уроков в этот день: {n}"),
 "nextl": ("keyingi: {p}-sabaq, {c}", "next: lesson {p}, {c}", "keyingi: {p}-dars, {c}", "следующий: {p}-й урок, {c}"),
 "nonef": ("Tańlanǵan waqıtta bos muǵallim joq", "No teachers are free at the selected time", "Tanlangan vaqtda bo‘sh o‘qituvchi yo‘q", "В выбранное время свободных учителей нет"),
 "pickp": ("Keminde bir sabaqtı tańlań", "Select at least one period", "Kamida bitta darsni tanlang", "Выберите хотя бы один урок"),
 "allday": ("Pútkil kún", "Whole day", "Butun kun", "Весь день"),
 "install": ("Telefonǵa ornatıw", "Install app", "Ilovani o‘rnatish", "Установить приложение"),
 "ios": ("iPhone: «Bólisiw» → «Bas ekranǵa qosıw»", "iPhone: tap Share → “Add to Home Screen”", "iPhone: «Ulashish» → «Bosh ekranga qo‘shish»", "iPhone: «Поделиться» → «На экран „Домой“»"),
 "print": ("PDF júklep alıw", "Download PDF", "PDF yuklab olish", "Скачать PDF"),
 "printhelp": ("Basıp shıǵarıw aynası ashılmasa: brauzer menyusı (⋮ yamasa «Bólisiw») → «Basıp shıǵarıw» → «PDF retinde saqlaw».", "If no print window opened: browser menu (⋮ or Share) → Print → Save as PDF.", "Chop etish oynasi ochilmasa: brauzer menyusi (⋮ yoki «Ulashish») → «Chop etish» → «PDF sifatida saqlash».", "Если окно печати не открылось: меню браузера (⋮ или «Поделиться») → «Печать» → «Сохранить как PDF»."),
 "open": ("Kesteni ashıw", "Open timetable", "Jadvalni ochish", "Открыть расписание"),
 "choose": ("Házirgi sabaqtı kóriw ushın klassıńızdı tańlań", "Choose your class to see the current lesson", "Hozirgi darsni ko‘rish uchun sinfingizni tanlang", "Выберите класс, чтобы видеть текущий урок"),
 "pickt": ("Muǵallimdi tańlań", "Choose a teacher", "O‘qituvchini tanlang", "Выберите учителя"),
 "m_cls": ("Klass", "Class", "Sinf", "Класс"),
 "m_tch": ("Muǵallim", "Teacher", "O‘qituvchi", "Учитель"),
 "nol": ("Bul kúni sabaq joq", "No lessons on this day", "Bu kuni dars yo‘q", "В этот день уроков нет"),
 "lno": ("{p}-sabaq", "Lesson {p}", "{p}-dars", "{p}-й урок"),
 "ends": ("{m} minuttan keyin tamamlanadı", "ends in {m} min", "{m} daqiqadan so‘ng tugaydi", "закончится через {m} мин"),
 "brk": ("Tánepis", "Break", "Tanaffus", "Перемена"),
 "next": ("Keyingi sabaq {t} de", "Next lesson at {t}", "Keyingi dars {t} da", "Следующий урок в {t}"),
 "done": ("Búgingi sabaqlar tamamlandı", "Today’s lessons are over", "Bugungi darslar tugadi", "Уроки на сегодня закончились"),
 "before": ("Sabaqlar {t} de baslanadı", "Lessons start at {t}", "Darslar {t} da boshlanadi", "Уроки начинаются в {t}"),
 "off": ("Búgin sabaq joq", "No lessons today", "Bugun dars yo‘q", "Сегодня уроков нет"),
 "clock": ("Mektep waqtı", "School time", "Maktab vaqti", "Время в школе"),
 "bells": ("Qońıraw kestesi", "Bell schedule", "Qo‘ng‘iroq jadvali", "Расписание звонков"),
 "brk_m": ("{m} min tánepis", "{m} min break", "{m} daq tanaffus", "перемена {m} мин"),
 "title": ("Sabaq keste", "Timetable", "Dars jadvali", "Расписание уроков"),
 "desc": ("{b}: 5–11-klasslar ushın sabaq keste.", "{b}: lesson timetable for grades 5–11.", "{b}: 5–11-sinflar uchun dars jadvali.", "{b}: расписание уроков для 5–11 классов."),
 "pick": ("Klassıńızdı tańlań", "Choose your class", "Sinfingizni tanlang", "Выберите свой класс"),
 "days": (("Dúyshembi", "Siyshembi", "Sárshembi", "Piyshembi", "Juma"), ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"),
          ("Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma"), ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница")),
 "short": (("Dú", "Si", "Sá", "Pi", "Ju"), ("Mon", "Tue", "Wed", "Thu", "Fri"), ("Du", "Se", "Ch", "Pa", "Ju"), ("Пн", "Вт", "Ср", "Чт", "Пт")),
 "today": ("Búgin", "Today", "Bugun", "Сегодня"),
 "lesson": ("sabaq", "lesson", "dars", "урок"),
 "groups": ("2 toparǵa bólinedi", "split into 2 groups", "2 guruhga bo‘linadi", "делится на 2 группы"),
 "free": ("Sabaq joq", "No lesson", "Dars yo‘q", "Нет урока"),
 "day_v": ("Kún", "Day", "Kun", "День"),
 "week_v": ("Hápte", "Week", "Hafta", "Неделя"),
 "count": ("{n} sabaq", "{n} lessons", "{n} ta dars", "уроков: {n}"),
 "upd": ("Keste {d} jaǵdayına", "Timetable as of {d}", "Jadval {d} holatiga", "Расписание на {d}"),
 "cls": ("klass", "class", "sinf", "класс"),
}
def tt_body(lang, i):
    sub = {k: [v[i], v[4]] for k, v in TT_SUBJ.items()}
    T_ = {k: (v[i] if isinstance(v, tuple) and not isinstance(v[0], tuple) else v[i]) for k, v in TT_TXT.items()}
    data = json.dumps({"c": TT["classes"], "s": sub, "t": T_, "b": BELLS, "hd": {c: HD.name(c, lang) for c in HD.HEAD}, "ic": {v[4]: TT_ICON.get(k, "") for k, v in TT_SUBJ.items()}}, ensure_ascii=False, separators=(",", ":"))
    def mins(s): h, m = s.split(":"); return int(h) * 60 + int(m)
    brows = ""
    for n, (a, e) in enumerate(BELLS, 1):
        gap = mins(BELLS[n][0]) - mins(e) if n < len(BELLS) else 0
        brows += f'<tr data-p="{n}"><th>{n}</th><td>{a} – {e}</td><td>{TT_TXT["brk_m"][i].format(m=gap) if gap else ""}</td></tr>'
    bells = f'<div class="ttbells card"><h2><span class="bic"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 17V11a6 6 0 0 1 12 0v6l2 2H4zM10 21a2 2 0 0 0 4 0"/></svg></span>{TT_TXT["bells"][i]}</h2><table class="btab"><tbody>{brows}</tbody></table></div>'
    grades = collections.OrderedDict()
    for c in TT["classes"]:
        grades.setdefault(c.split("-")[0], []).append(c)
    picker = "".join(f'<div class="grade"><span>{g}</span>' + "".join(
        f'<button type="button" class="cl" data-c="{c}">{c}</button>' for c in cs) + "</div>" for g, cs in grades.items())
    return f"""<div class="printhead"><img src="{{UP}}logo.png" alt=""><div><b>{T[lang]['brand']}</b><span>{TT_TXT['title'][i]} · {TT_TXT['upd'][i].format(d=TT['date'])}</span></div></div>
{BL.html(i, BELLS, {k: [v[i], v[4]] for k, v in TT_SUBJ.items()}, "#pickh")}
<div class="ttwrap" data-pdf="{{UP}}pdf/{lang}/">
  <div class="ttside"><div class="ttclock card" hidden><span class="ckic"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span><div><small>{TT_TXT['clock'][i]}</small><b id="clk">--:--</b></div><p id="status"></p><div class="pbar"><i id="barfill"></i></div></div>
  <div class="ttpick card"><div class="seg mode" role="group"><button type="button" class="on" data-m="class"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3"/><path d="M3 20c.5-3.500 3-5.500 6-5.500s5.500 2 6 5.500M16 6a3 3 0 0 1 0 5.500M18 14.500c1.700.8 2.700 2.500 3 5"/></svg>{TT_TXT['m_cls'][i]}</button><button type="button" data-m="teacher"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="11" rx="2"/><path d="M8 20l4-5 4 5M8 9h8"/></svg>{TT_TXT['m_tch'][i]}</button><button type="button" data-m="free"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>{TT_TXT['m_free'][i]}</button></div>
    <h2 id="pickh">{TT_TXT['pick'][i]}</h2><div class="grades" id="grades">{picker}</div>
    <div id="tpick" hidden><select id="tsel" aria-label="{TT_TXT['pickt'][i]}"></select></div><p class="note" id="fhint" hidden>{TT_TXT['fp_hint'][i]}</p></div>{bells}</div>
  <div class="ttmain card">
    <div class="tthead"><div><p class="ttcls" id="ttcls"></p><p class="note" id="ttcount"></p></div>
      <div class="seg" role="group"><button type="button" class="on" data-v="day">{TT_TXT['day_v'][i]}</button><button type="button" data-v="week">{TT_TXT['week_v'][i]}</button></div></div>
    <div class="quick" id="quick"><button type="button" data-q="today" data-d="TODAY">{TT_TXT['today'][i]}</button><button type="button" data-q="tom" data-d="TOM">{TT_TXT['tom'][i]}</button></div>
    <div class="dtabs" id="dtabs" role="tablist"></div>
    <div id="freebox" hidden><h3 class="fh">{TT_TXT['fp_h'][i]}</h3><div class="fper" id="fper"></div>
      <select id="fsub" aria-label="{TT_TXT['fsubj'][i]}"></select><div id="fres"></div></div>
    <ol class="lessons" id="lessons"></ol>
    <div class="scroll" id="week" hidden></div>
  </div>
</div>
<div class="tttools"><a class="btn s" id="ttprint" href="#" download hidden>{TT_TXT['print'][i]}</a><button type="button" class="btn p" id="ttinst" hidden>{TT_TXT['install'][i]}</button><span class="note" id="ttios" hidden>{TT_TXT['ios'][i]}</span></div>
<p class="note">{TT_TXT['upd'][i].format(d=TT['date'])}</p>
<script id="ttdata" type="application/json">{data}</script>"""

TT_JS = r"""
  const td=document.getElementById('ttdata');
  if(td){
    const D=JSON.parse(td.textContent),C=D.c,S=D.s,X=D.t,B=D.b,IC=D.ic||{},K=['mon','tue','wed','thu','fri'];
    const $=id=>document.getElementById(id),esc=s=>String(s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
    const mm=s=>{const[h,m]=s.split(':');return +h*60+ +m};
    const now=()=>{const p={};new Intl.DateTimeFormat('en-US',{timeZone:'Asia/Samarkand',weekday:'long',hour:'2-digit',minute:'2-digit',second:'2-digit',hourCycle:'h23'}).formatToParts(new Date()).forEach(x=>p[x.type]=x.value);return {wd:['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].indexOf(String(p.weekday).slice(0,3)),h:+p.hour,m:+p.minute,s:+p.second}};
    const subj=k=>S[k]||[k,'#0b5f78'];
    // teacher index
    const TI={},TS={};
    for(const c in C)for(const k of K)for(const p in (C[c][k]||{}))for(const [s,t] of C[c][k][p]){if(!t)continue;((TI[t]=TI[t]||{})[k]=TI[t][k]||{})[p]=[c,s];TS[t]=TS[t]||s}
    const tnames=Object.keys(TI).sort((a,b)=>a.localeCompare(b));
    const slug=t=>'t-'+t.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/-+$/,'');
    // select options grouped by subject
    const groups={};tnames.forEach(t=>(groups[TS[t]]=groups[TS[t]]||[]).push(t));
    $('tsel').innerHTML=`<option value="">${X.pickt}</option>`+Object.keys(groups).sort((a,b)=>subj(a)[0].localeCompare(subj(b)[0])).map(g=>`<optgroup label="${esc(subj(g)[0])}">`+groups[g].map(t=>`<option value="${esc(t)}">${esc(t)}</option>`).join('')+'</optgroup>').join('');
    const N0=now(),today=N0.wd<=4?N0.wd:-1,tomorrow=N0.wd>=4?0:N0.wd+1;
    let day=today<0?0:today,view='day',mode='class',cls=null,tch=null;
    {const qt=document.querySelector('#quick [data-q=today]'),qm=document.querySelector('#quick [data-q=tom]');qt.dataset.d=today;qt.hidden=today<0;qm.dataset.d=tomorrow;}
    try{cls=localStorage.getItem('ttcls');tch=localStorage.getItem('tttch');mode=localStorage.getItem('ttmode')||'class'}catch(e){}
    const h=(location.hash||'').slice(1);
    if(h==='free')mode='free';
    else if(C[h.toUpperCase()]){cls=h.toUpperCase();mode='class'}
    else if(h.startsWith('t-')){const f=tnames.find(t=>slug(t)===h);if(f){tch=f;mode='teacher'}}
    if(!C[cls])cls=null;if(!TI[tch])tch=null;
    const sel=()=>mode==='class'?cls:tch;
    // free-teacher state: default = current (or next) period today
    const fsel=new Set();let fsub='';
    {const n=now(),cur=n.h*60+n.m;let p0=B.findIndex(b=>cur<mm(b[1]));if(p0<0||today<0)p0=0;fsel.add(p0+1)}
    $('fper').innerHTML=B.map((b,k)=>`<button type="button" data-p="${k+1}"><b>${k+1}</b><small>${b[0]}</small></button>`).join('')+`<button type="button" data-p="all" class="fall">${X.allday}</button>`;
    $('fsub').innerHTML=`<option value="">${X.fsubj}</option>`+[...new Set(Object.values(TS))].sort((a,b)=>subj(a)[0].localeCompare(subj(b)[0])).map(s=>`<option value="${esc(s)}">${esc(subj(s)[0])}</option>`).join('');
    function renderFree(){
      const k=K[day],ps=[...fsel].sort((a,b)=>a-b);
      document.querySelectorAll('#fper button').forEach(b=>b.classList.toggle('on',b.dataset.p==='all'?fsel.size===B.length:fsel.has(+b.dataset.p)));
      $('ttcls').textContent=X.m_free;
      $('ttcount').textContent=X.days[day]+(ps.length?' · '+ps.map(p=>p).join(', ')+' ('+B[ps[0]-1][0]+' – '+B[ps[ps.length-1]-1][1]+')':'');
      if(!ps.length){$('fres').innerHTML=`<p class="note">${X.pickp}</p>`;return}
      const busy=[],off=[];
      for(const t of tnames){if(fsub&&TS[t]!==fsub)continue;const L=(TI[t][k]||{}),n=Object.keys(L).length;
        if(ps.some(p=>L[p]))continue;
        const after=Object.keys(L).map(Number).filter(p=>p>ps[ps.length-1]).sort((a,b)=>a-b)[0];
        (n?busy:off).push({t,n,nx:after?X.nextl.replace('{p}',after).replace('{c}',L[after][0]):''})}
      const card=o=>`<li style="--sc:${subj(TS[o.t])[1]}"><span class="fav">${esc(o.t.split(' ').map(w=>w[0]).join('').slice(0,2))}</span><div><b>${esc(o.t)}</b><small>${esc(subj(TS[o.t])[0])}${o.n?' · '+X.l_day.replace('{n}',o.n):''}${o.nx?' · '+esc(o.nx):''}</small></div></li>`;
      let out=`<p class="fcount">${X.free_n.replace('{n}',busy.length+off.length)}</p>`;
      if(!busy.length&&!off.length)out=`<p class="note">${X.nonef}</p>`;
      if(busy.length)out+=`<h4>${X.teach_day}</h4><ul class="flist">${busy.map(card).join('')}</ul>`;
      if(off.length)out+=`<details${busy.length?'':' open'}><summary>${X.no_day} (${off.length})</summary><ul class="flist dim">${off.map(card).join('')}</ul></details>`;
      $('fres').innerHTML=out}
    // lessons of the selected class/teacher on day index d: {p:{name,col,sub}}
    function les(d){const k=K[d],o={};
      if(mode==='class'&&cls){const L=(C[cls][k]||{});for(const p in L){const l=L[p],s=subj(l[0][0]),t=l.map(x=>x[1]).filter(Boolean);o[p]={name:s[0],col:s[1],sub:t.join(' · ')+(l.length>1?' — '+X.groups:'')}}}
      if(mode==='teacher'&&tch){const L=(TI[tch][k]||{});for(const p in L){const [c,sb]=L[p],s=subj(sb);o[p]={name:c+' '+X.cls,col:s[1],sub:s[0]}}}
      return o}
    function render(){
      document.querySelectorAll('.mode button').forEach(b=>b.classList.toggle('on',b.dataset.m===mode));
      $('grades').hidden=mode!=='class';$('tpick').hidden=mode!=='teacher';$('fhint').hidden=mode!=='free';$('pickh').textContent=mode==='class'?X.pick:mode==='teacher'?X.pickt:X.fp_h;
      const isF=mode==='free';$('freebox').hidden=!isF;$('ttprint').hidden=true;document.querySelector('.ttmain .seg').hidden=isF;
      if(isF){const main=document.querySelector('.ttmain');main.classList.remove('empty');view='day';$('quick').hidden=false;$('lessons').hidden=true;$('week').hidden=true;
        document.querySelectorAll('#quick button').forEach(b=>b.classList.toggle('on',+b.dataset.d===day&&((b.dataset.q==='today'&&day===today)||(b.dataset.q==='tom'&&day===tomorrow))));
        $('dtabs').hidden=false;$('dtabs').innerHTML=K.map((k,n)=>`<button type="button" role="tab" aria-selected="${n===day}" data-d="${n}"><b>${X.short[n]}</b><small>${n===today?X.today:n===tomorrow?X.tom:''}</small></button>`).join('');
        renderFree();tick();return}
      document.querySelectorAll('.cl').forEach(b=>b.classList.toggle('on',mode==='class'&&b.dataset.c===cls));
      $('tsel').value=tch||'';
      const main=document.querySelector('.ttmain'),cur=sel();main.classList.toggle('empty',!cur);
      if(!cur){$('ttcls').textContent=mode==='class'?X.pick:X.pickt;$('ttcount').textContent='';$('dtabs').innerHTML='';$('lessons').innerHTML='';$('week').hidden=true;$('quick').hidden=true;tick();return}
      if(mode==='class'){const h=(D.hd||{})[cls];$('ttcls').innerHTML=esc(cls+' '+X.cls)+(h?`<span class="tthd">${esc(X.ht)}: <b>${esc(h)}</b></span>`:'')}else $('ttcls').textContent=tch;
      $('quick').hidden=view!=='day';
      document.querySelectorAll('#quick button').forEach(b=>b.classList.toggle('on',+b.dataset.d===day&&((b.dataset.q==='today'&&day===today)||(b.dataset.q==='tom'&&day===tomorrow))));
      $('dtabs').innerHTML=K.map((k,n)=>{const c=Object.keys(les(n)).length;return `<button type="button" role="tab" aria-selected="${n===day}" data-d="${n}"><b>${X.short[n]}</b><small>${n===today?X.today:n===tomorrow?X.tom:X.count.replace('{n}',c)}</small></button>`}).join('');
      $('dtabs').hidden=view!=='day';
      const ls=les(day),ps=Object.keys(ls).map(Number),max=ps.length?Math.max(...ps):0,min=ps.length?Math.min(...ps):1;
      $('ttcount').textContent=view==='day'?X.days[day]+' · '+X.count.replace('{n}',ps.length):(mode==='teacher'?subj(TS[tch])[0]:'');
      let out='';
      if(!ps.length)out=`<li class="free"><span class="pn">–</span><div><b>${X.nol}</b></div></li>`;
      for(let p=min;p<=max&&ps.length;p++){const c=ls[p],tm=B[p-1]?B[p-1][0]+' – '+B[p-1][1]:'';
        if(!c){out+=`<li class="free" data-p="${p}"><span class="pn">${p}</span><div><b>${X.free}</b><small>${tm}</small></div></li>`;continue}
        out+=`<li style="--sc:${c.col}" data-p="${p}"><span class="pn">${p}</span><div><span class="tm">${tm}</span><b>${esc(c.name)}</b><small>${esc(c.sub)}</small></div><span class="si"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">${IC[c.col]||''}</svg></span></li>`}
      $('lessons').innerHTML=out;$('lessons').hidden=view!=='day';
      if(view==='week'){const W=K.map((k,n)=>les(n));let mp=0;W.forEach(o=>Object.keys(o).forEach(p=>mp=Math.max(mp,+p)));
        let tb='<table class="wk"><thead><tr><th>#</th>'+K.map((k,n)=>`<th${n===today?' class="td"':''}>${X.short[n]}</th>`).join('')+'</tr></thead><tbody>';
        for(let p=1;p<=mp;p++){tb+=`<tr><th>${p}<small>${B[p-1]?B[p-1][0]:''}</small></th>`+W.map((o,n)=>{const c=o[p],cl=n===today?' class="td"':'';if(!c)return `<td${cl}></td>`;return `<td${cl}><span style="--sc:${c.col}">${esc(mode==='teacher'?c.name.split(' ')[0]:c.name)}</span></td>`}).join('')+'</tr>'}
        $('week').innerHTML=tb+'</tbody></table>'}
      $('week').hidden=view!=='week';
      pdfLink();tick();
    }
    function tick(){
      const n=now(),cur=n.h*60+n.m+n.s/60;$('clk').textContent=String(n.h).padStart(2,'0')+':'+String(n.m).padStart(2,'0');
      let msg='',pct=0,live=0;const d=n.wd<=4?n.wd:-1;
      const L=mode!=='free'&&sel()&&d>=0?les(d):null,ps0=L?Object.keys(L).map(Number):null;
      if(d<0)msg=X.off;else{const ps=B.map((b,k)=>k+1).filter(p=>!ps0||ps0.includes(p));
        if(!ps.length)msg=X.off;
        else if(cur<mm(B[ps[0]-1][0]))msg=X.before.replace('{t}',B[ps[0]-1][0]);
        else if(cur>=mm(B[ps[ps.length-1]-1][1]))msg=X.done;
        else for(const p of ps){const a=mm(B[p-1][0]),e=mm(B[p-1][1]);
          if(cur>=a&&cur<e){live=p;pct=(cur-a)/(e-a)*100;const nm=L&&L[p]?L[p].name+' · ':'';msg=`<b>${X.now}: ${X.lno.replace('{p}',p)}</b> · ${esc(nm)}${X.ends.replace('{m}',Math.ceil(e-cur))}`;break}
          if(cur<a){const nx=L&&L[p]?' · '+esc(L[p].name):'';msg=`<b>${X.brk}</b> · ${X.next.replace('{t}',B[p-1][0])}${nx}`;break}}}
      $('status').innerHTML=msg;$('barfill').style.width=pct+'%';document.querySelector('.ttclock').classList.toggle('live',!!live);
      document.querySelectorAll('#lessons li').forEach(li=>li.classList.toggle('cur',!!live&&day===d&&+li.dataset.p===live));
      document.querySelectorAll('.btab tr').forEach(r=>r.classList.toggle('cur',!!live&&+r.dataset.p===live));
    }
    setInterval(tick,15000);
    const save=()=>{try{localStorage.setItem('ttmode',mode);cls&&localStorage.setItem('ttcls',cls);tch&&localStorage.setItem('tttch',tch)}catch(e){}
      history.replaceState(null,'','#'+(mode==='free'?'free':mode==='class'?(cls||'').toLowerCase():(tch?slug(tch):'')))};
    const jump=()=>{if(innerWidth<900)document.querySelector('.ttmain').scrollIntoView({block:'start'})};
    $('grades').addEventListener('click',e=>{const b=e.target.closest('.cl');if(!b)return;cls=b.dataset.c;save();render();jump()});
    $('tsel').addEventListener('change',()=>{tch=$('tsel').value||null;save();render();if(tch)jump()});
    document.querySelectorAll('.mode button').forEach(b=>b.addEventListener('click',()=>{mode=b.dataset.m;save();render()}));
    $('dtabs').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;day=+b.dataset.d;render()});
    $('quick').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;day=+b.dataset.d;view='day';document.querySelectorAll('.ttmain .seg button').forEach(x=>x.classList.toggle('on',x.dataset.v==='day'));render()});
    document.querySelectorAll('.ttmain .seg button').forEach(b=>b.addEventListener('click',()=>{view=b.dataset.v;document.querySelectorAll('.ttmain .seg button').forEach(x=>x.classList.toggle('on',x===b));render()}));
    const pdfBase=document.querySelector('.ttwrap').dataset.pdf;
    function pdfLink(){const a=$('ttprint'),cur=sel();a.hidden=mode==='free'||!cur;if(a.hidden)return;
      const f=mode==='class'?'c-'+cls.toLowerCase():slug(tch);a.href=pdfBase+f+'.pdf';a.setAttribute('download',(mode==='class'?cls:tch).replace(/\s+/g,'_')+'.pdf')}
    let dp=null;addEventListener('beforeinstallprompt',e=>{e.preventDefault();dp=e;$('ttinst').hidden=false});
    $('ttinst').addEventListener('click',async()=>{if(!dp)return;dp.prompt();try{await dp.userChoice}catch(e){};dp=null;$('ttinst').hidden=true});
    if(/iphone|ipad|ipod/i.test(navigator.userAgent)&&!navigator.standalone)$('ttios').hidden=false;
    $('fper').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;
      if(b.dataset.p==='all'){if(fsel.size===B.length)fsel.clear();else B.forEach((x,k)=>fsel.add(k+1))}else{const p=+b.dataset.p;fsel.has(p)?fsel.delete(p):fsel.add(p)}render()});
    $('fsub').addEventListener('change',()=>{fsub=$('fsub').value;render()});
    render();
  }"""

HOME_JS = r"""
  const lb=document.getElementById('lbdata');
  if(lb){
    const L=JSON.parse(lb.textContent),X=L.t,B=L.b,K=['mon','tue','wed','thu','fri'],bar=document.getElementById('livebar'),tx=document.getElementById('lbtxt');
    const mm=s=>{const[h,m]=s.split(':');return +h*60+ +m};
    const esc=s=>String(s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
    let mode='class',cls=null,tch=null;try{mode=localStorage.getItem('ttmode')||'class';cls=localStorage.getItem('ttcls');tch=localStorage.getItem('tttch')}catch(e){}
    const who=mode==='teacher'?tch:cls;
    if(!who){tx.textContent=X.choose;bar.hidden=false}
    else fetch(document.querySelector('link[rel=icon][href$="logo.png"]').href.replace(/logo\.png$/,'timetable.json')).then(r=>r.json()).then(D=>{
      const C=D.classes;
      function les(k){const o={};if(mode==='class'&&C[cls]){const T=C[cls][k]||{};for(const p in T)o[p]=(L.s[T[p][0][0]]||[T[p][0][0]])[0]}
        else{for(const c in C){const T=C[c][k]||{};for(const p in T)if(T[p].some(x=>x[1]===tch))o[p]=c+' '+X.cls}}return o}
      function tick(){const p={};new Intl.DateTimeFormat('en-US',{timeZone:'Asia/Samarkand',weekday:'long',hour:'2-digit',minute:'2-digit',hourCycle:'h23'}).formatToParts(new Date()).forEach(x=>p[x.type]=x.value);
        const wd=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].indexOf(String(p.weekday).slice(0,3)),cur=+p.hour*60+ +p.minute;let msg='';
        if(wd>4)msg=X.off;else{const O=les(K[wd]),ps=Object.keys(O).map(Number).sort((a,b)=>a-b);
          if(!ps.length)msg=X.off;else if(cur<mm(B[ps[0]-1][0]))msg=X.before.replace('{t}',B[ps[0]-1][0]);else if(cur>=mm(B[ps[ps.length-1]-1][1]))msg=X.done;
          else for(const q of ps){const a=mm(B[q-1][0]),e=mm(B[q-1][1]);if(cur>=a&&cur<e){msg=`<b>${X.now}: ${X.lno.replace('{p}',q)}</b> · ${esc(O[q])} · ${X.ends.replace('{m}',e-cur)}`;break}
            if(cur<a){msg=`<b>${X.brk}</b> · ${X.next.replace('{t}',B[q-1][0])} · ${esc(O[q])}`;break}}}
        tx.innerHTML=`<strong>${esc(who)}</strong> · ${msg}`;bar.hidden=false}
      tick();setInterval(tick,30000)}).catch(()=>{});
  }
  const yc=document.querySelectorAll('.ychips .chip');
  yc.forEach(b=>b.addEventListener('click',()=>{yc.forEach(x=>x.classList.toggle('on',x===b));document.querySelectorAll('.gview').forEach(v=>v.hidden=v.dataset.y!==b.dataset.y)}));
  const pcs=document.querySelectorAll('.pchips .pc');
  pcs.forEach(b=>b.addEventListener('click',()=>{pcs.forEach(x=>x.classList.toggle('on',x===b));document.querySelectorAll('.ppanel').forEach(p=>p.hidden=p.dataset.f!==b.dataset.f)}));
  const gq=document.getElementById('gq');
  if(gq){let gy=document.querySelector('.gyears .chip.on').dataset.y,gk='all';const rows=[...document.querySelectorAll('#glist tbody tr')],kc=document.querySelectorAll('.gkinds .chip');
    const run=()=>{const v=gq.value.trim().toLowerCase();let n=0;const cnt={all:0,uni:0,col:0,none:0};
      rows.forEach(r=>{const iy=v||gy==='all'||r.dataset.y===gy,iq=!v||r.dataset.q.includes(v);if(iy&&iq){cnt.all++;cnt[r.dataset.k]++}const ok=iy&&iq&&(gk==='all'||r.dataset.k===gk);r.hidden=!ok;if(ok)n++});
      kc.forEach(b=>{b.querySelector('em').textContent=cnt[b.dataset.k];b.hidden=b.dataset.k!=='all'&&!cnt[b.dataset.k]&&gk!==b.dataset.k});document.getElementById('gnone').hidden=n>0};
    document.querySelectorAll('.gyears .chip').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.gyears .chip').forEach(x=>x.classList.toggle('on',x===b));gy=b.dataset.y;gq.value='';run()}));
    kc.forEach(b=>b.addEventListener('click',()=>{kc.forEach(x=>x.classList.toggle('on',x===b));gk=b.dataset.k;run()}));
    gq.addEventListener('input',run);run()}
  if('serviceWorker' in navigator){const ic=document.querySelector('link[rel=icon][href$="logo.png"]');navigator.serviceWorker.register(ic.href.replace(/logo\.png$/,'sw.js')).catch(()=>{})}"""

import graduates as G
UZB = json.load(open(os.path.join(SRC, 'uzb_outline.json')))
UZB = [UZB] if isinstance(UZB[0][0][0], (int, float)) else UZB
from collections import Counter as _Ctr
GT = {
 "title": ("Pitkeriwshiler", "Graduates", "Bitiruvchilar", "Выпускники"),
 "desc": ("{b}: pitkeriwshilerimiz qay jerde oqıp atır — joqarı oqıw orınları, baǵdarlar hám qalalar.", "{b}: where our graduates study — universities, fields and cities.", "{b}: bitiruvchilarimiz qayerda o‘qimoqda — oliygohlar, yo‘nalishlar va shaharlar.", "{b}: где учатся наши выпускники — вузы, направления и города."),
 "lead": ("Sońǵı tórt jılda mektebimizdi {n} oqıwshı pitkerdi. Olardıń {u} joqarı oqıw orınlarında, {c} texnikumda oqıp atır.", "{n} students graduated from our school in the last four years. {u} of them study at universities and {c} at colleges (technikums).", "So‘nggi to‘rt yilda maktabimizni {n} nafar o‘quvchi bitirdi. Ulardan {u} nafari oliygohlarda, {c} nafari texnikumlarda o‘qimoqda.", "За последние четыре года школу окончили {n} учеников. {u} из них учатся в вузах, {c} — в техникумах."),
 "s_ninst": ("túrli joqarı oqıw orınında pitkeriwshilerimiz oqıp atır (+ {c} texnikum)", "different universities where our graduates study (plus {c} technikums)", "xil oliygohda bitiruvchilarimiz o‘qimoqda (yana {c} ta texnikum)", "разных вузов, где учатся наши выпускники (и ещё {c} техникума)"),
 "s_uni": ("joqarı oqıw orınlarında oqıp atır ({p} oqıwshı)", "study at universities ({p} students)", "oliygohlarda o‘qimoqda ({p} nafar)", "учатся в вузах ({p} чел.)"),
 "s_col": ("texnikumda oqıp atır ({p} oqıwshı)", "study at colleges / technikums ({p} students)", "texnikumlarda o‘qimoqda ({p} nafar)", "учатся в техникумах ({p} чел.)"),
 "k_all": ("Barlıǵı", "All", "Barchasi", "Все"),
 "k_uni": ("Joqarı oqıw orını", "University", "Oliygoh", "Вуз"),
 "k_col": ("Texnikum", "College (technikum)", "Texnikum", "Техникум"),
 "y_uni": ("{a} joqarı oqıw orınında", "{a} at university", "{a} nafari oliygohda", "{a} в вузе"),
 "y_col": ("{a} texnikumda", "{a} at college", "{a} nafari texnikumda", "{a} в техникуме"),
 "y_of": ("{b} pitkeriwshiden", "of {b} graduates", "{b} nafar bitiruvchidan", "из {b} выпускников"),
 "s_grad": ("pitkeriwshi (2023–2026)", "graduates (2023–2026)", "bitiruvchi (2023–2026)", "выпускник (2023–2026)"),
 "s_cont": ("bilimin dawam ettirip atır ({p} oqıwshı)", "continue their education ({p} students)", "ta’limni davom ettirmoqda ({p} nafar)", "продолжают обучение ({p} чел.)"),
 "s_inst": ("joqarı oqıw orını hám texnikum", "universities and colleges", "oliygoh va texnikum", "вузов и колледжей"),
 "s_city": ("qalada oqıp atır", "cities across Uzbekistan", "shaharda o‘qimoqda", "городов Узбекистана"),
 "years_h": ("Jıllar boyınsha", "Year by year", "Yillar bo‘yicha", "По годам"),
 "of": ("{a} / {b} bilimin dawam ettiredi", "{a} of {b} continue studying", "{a} / {b} ta’limni davom ettirmoqda", "{a} из {b} продолжают обучение"),
 "where_h": ("Qay jerde oqıp atır", "Where they study", "Qayerda o‘qimoqda", "Где они учатся"),
 "all": ("Barlıq {n} oqıw orını", "All {n} institutions", "Barcha {n} ta muassasa", "Все учебные заведения ({n})"),
 "field_h": ("Tańlanǵan baǵdarlar", "Fields they chose", "Tanlangan yo‘nalishlar", "Выбранные направления"),
 "city_h": ("Ózbekstan boylap", "Across Uzbekistan", "O‘zbekiston bo‘ylab", "По всему Узбекистану"),
 "city_p": ("{n} pitkeriwshi Qaraqalpaqstannan tısqarıdaǵı joqarı oqıw orınlarında oqıp atır.", "{n} graduates study at universities outside Karakalpakstan.", "{n} nafar bitiruvchi Qoraqalpog‘istondan tashqaridagi oliygohlarda o‘qimoqda.", "{n} выпускников учатся в вузах за пределами Каракалпакстана."),
 "beyond_h": ("Qaraqalpaqstannan tısqarıdaǵı oqıw orınları", "Universities beyond Karakalpakstan", "Qoraqalpog‘istondan tashqaridagi oliygohlar", "Вузы за пределами Каракалпакстана"),
 "students": ("{n} oqıwshı", "{n} students", "{n} nafar", "{n} чел."),
 "student1": ("1 oqıwshı", "1 student", "1 nafar", "1 чел."),
 "college": ("texnikum", "college", "texnikum", "техникум"),
 "note": ("Derek: mekteptiń 2022/2023–2025/2026 oqıw jılları boyınsha kórsetkishleri. Pitkeriwshilerdiń atları olardıń ruqsatı menen járiyalandı; sertifikat nátiyjeleri tek ulıwma sanda kórsetiledi.", "Source: school records for the 2022/2023–2025/2026 school years. Graduates’ names are published with their permission; certificate results are shown as totals only.", "Manba: maktabning 2022/2023–2025/2026 o‘quv yillari bo‘yicha ko‘rsatkichlari. Bitiruvchilarning ismlari ularning roziligi bilan e’lon qilindi; sertifikat natijalari faqat umumiy sonda ko‘rsatiladi.", "Источник: данные школы за 2022/2023–2025/2026 учебные годы. Имена выпускников опубликованы с их согласия; результаты сертификатов приводятся только в общем количестве."),
 "more": ("Pitkeriwshiler haqqında", "About our graduates", "Bitiruvchilar haqida", "О наших выпускниках"),
}
GT2 = {
 "cert_h": ("Pitkeriwshilerdiń sertifikatları", "Graduates’ certificates", "Bitiruvchilarning sertifikatlari", "Сертификаты выпускников"),
 "cert_p": ("Kúshli nátiyjeler — jaqsı joqarı oqıw orınlarına jol.", "Strong results open the door to good universities.", "Kuchli natijalar — yaxshi oliygohlarga yo‘l.", "Сильные результаты открывают дорогу в хорошие вузы."),
 "c_with": ("pitkeriwshide milliy yamasa xalıqaralıq sertifikat bar ({t} den)", "graduates hold a national or international certificate (of {t})", "nafar bitiruvchida milliy yoki xalqaro sertifikat bor ({t} tadan)", "выпускников имеют национальный или международный сертификат (из {t})"),
 "c_top": ("pitkeriwshi milliy sertifikatta A yamasa A+ dárejesin aldı", "graduates earned an A or A+ national certificate", "nafar bitiruvchi milliy sertifikatda A yoki A+ darajasini oldi", "выпускников получили национальный сертификат уровня A или A+"),
 "c_ielts": ("pitkeriwshi IELTS tapsırdı", "graduates took IELTS", "nafar bitiruvchi IELTS topshirdi", "выпускников сдали IELTS"),
 "c_sat": ("pitkeriwshi SAT tapsırdı (eń joqarı: {b})", "graduates took the SAT (best score: {b})", "nafar bitiruvchi SAT topshirdi (eng yuqori: {b})", "выпускника сдали SAT (лучший результат: {b})"),
 "trend_h": ("Ósiw", "Growing every year", "O‘sish", "Рост с каждым годом"),
 "t_cert": ("Sertifikatı bar pitkeriwshiler", "Graduates with a certificate", "Sertifikatli bitiruvchilar", "Выпускники с сертификатом"),
 "t_out": ("Qaraqalpaqstannan tısqarıda oqıytuǵınlar", "Studying outside Karakalpakstan", "Qoraqalpog‘istondan tashqarida o‘qiydiganlar", "Учатся за пределами Каракалпакстана"),
 "t_me": ("Medicina hám injenerlik/IT", "Medicine and engineering/IT", "Tibbiyot va muhandislik/IT", "Медицина и инженерия/IT"),
 "spot": ("{n} oqıw orınında", "at {n} institutions", "{n} ta muassasada", "в {n} учебных заведениях"),
 "explore_h": ("Jıl boyınsha kóriw", "Explore by year", "Yil bo‘yicha ko‘rish", "Смотреть по годам"),
 "allyears": ("Barlıq jıllar", "All years", "Barcha yillar", "Все годы"),
 "list_h": ("Pitkeriwshiler dizimi", "List of graduates", "Bitiruvchilar ro‘yxati", "Список выпускников"),
 "list_p": ("Barlıq pitkeriwshilerimiz hám olar bilim alıp atırǵan orınlar.", "All our graduates and where they are studying.", "Barcha bitiruvchilarimiz va ular tahsil olayotgan joylar.", "Все наши выпускники и где они учатся."),
 "search": ("Atı yamasa oqıw orını boyınsha izlew", "Search by name or university", "Ism yoki oliygoh bo‘yicha qidirish", "Поиск по имени или вузу"),
 "th": (("Atı", "Oqıw orını", "Baǵdar"), ("Name", "University / college", "Field"), ("F.I.Sh.", "Oliygoh / texnikum", "Yo‘nalish"), ("Ф.И.О.", "Вуз / колледж", "Направление")),
 "p_h": ("Óz jolıńdı tańla", "Choose your path", "Yo‘lingni tanla", "Выбери свой путь"),
 "p_p": ("Qaysı baǵdar qızıqtıradı? Pitkeriwshilerimiz qayerde oqıp atırǵanın kóriń.", "Which field interests you? See where our graduates went.", "Qaysi yo‘nalish qiziqtiradi? Bitiruvchilarimiz qayerda o‘qiyotganini ko‘ring.", "Какое направление вам интересно? Узнайте, где учатся наши выпускники."),
 "p_big": ("{n} pitkeriwshi usı baǵdardı tańladı", "{n} graduates chose this field", "{n} nafar bitiruvchi shu yo‘nalishni tanlagan", "{n} выпускников выбрали это направление"),
 "p_share": ("Oqıwın dawam etkenler ishinde {p}%", "{p}% of all graduates who continue studying", "O‘qishni davom ettirganlar orasida {p}%", "{p}% от всех, кто продолжает обучение"),
 "p_where": ("Qayerde oqıydı", "Where they study", "Qayerda o‘qiydi", "Где учатся"),
 "p_year": ("Jıllar boyınsha", "By year", "Yillar bo‘yicha", "По годам"),
 "p_city": ("Qalalar", "Cities", "Shaharlar", "Города"),
 "p_more": ("hám basqa {n} oqıw orını", "and {n} more institutions", "va yana {n} ta oliygoh/texnikum", "и ещё {n} учебных заведений"),
 "p_note": ("Sanlar mektebimiz pitkeriwshileriniń 2022–2026 jıllardaǵı haqıyqıy nátiyjelerinen alınǵan.", "Numbers come from the real results of our graduates, 2022–2026.", "Raqamlar bitiruvchilarimizning 2022–2026 yillardagi haqiqiy natijalaridan olingan.", "Цифры взяты из реальных результатов наших выпускников за 2022–2026 годы."),
 "c_h": ("Qanday sertifikatlar bar edi", "What certificates they had", "Qanday sertifikatlari bor edi", "Какие сертификаты у них были"),
 "c_sum": ("{a} / {n} pitkeriwshide keminde bir sertifikat bar edi", "{a} of {n} graduates had at least one certificate", "{n} nafar bitiruvchidan {a} tasida kamida bitta sertifikat bor edi", "У {a} из {n} выпускников был хотя бы один сертификат"),
 "c_typ": ("kóbirek: {l}", "typically {l}", "ko‘pincha: {l}", "обычно {l}"),
 "c_best": ("eń joqarı: {l}", "best: {l}", "eng yuqori: {l}", "лучший: {l}"),
 "c_none": ("Bul baǵdar boyınsha sertifikat maǵlıwmatı joq.", "No certificate data for this field.", "Bu yo‘nalish bo‘yicha sertifikat ma’lumoti yo‘q.", "Нет данных о сертификатах по этому направлению."),
 "c_note": ("Sertifikat maǵlıwmatı 2023–2026 jılı pitkeriwshileri ushın. Hár pitkeriwshi bir neshe pán boyınsha sertifikatqa iye bolıwı múmkin.", "Certificate data covers the 2023–2026 graduates. A graduate can hold certificates in several subjects.", "Sertifikat ma’lumotlari 2023–2026 yillar bitiruvchilari uchun. Bitiruvchida bir nechta fandan sertifikat bo‘lishi mumkin.", "Данные о сертификатах — за выпуски 2023–2026 годов. У одного выпускника может быть несколько предметов."),
 "subj": {"M": ("Matematika", "Mathematics", "Matematika", "Математика"), "P": ("Fizika", "Physics", "Fizika", "Физика"),
          "C": ("Ximiya", "Chemistry", "Kimyo", "Химия"), "B": ("Biologiya", "Biology", "Biologiya", "Биология"),
          "H": ("Tariyx", "History", "Tarix", "История"), "G": ("Geografiya", "Geography", "Geografiya", "География"),
          "L": ("Ana tili hám ádebiyat", "Native language and literature", "Ona tili va adabiyot", "Родной язык и литература"),
          "E": ("Ingliz tili (CEFR)", "English (CEFR)", "Ingliz tili (CEFR)", "Английский язык (CEFR)"),
          "U": ("Ózbek tili", "Uzbek language", "O‘zbek tili", "Узбекский язык"), "Q": ("Qaraqalpaq tili", "Karakalpak language", "Qoraqalpoq tili", "Каракалпакский язык"),
          "T": ("Túrk tili (CEFR)", "Turkish (CEFR)", "Turk tili (CEFR)", "Турецкий язык (CEFR)")},
 "na": ("Maǵlıwmat kiritilmegen", "Not specified", "Ko‘rsatilmagan", "Не указано"),
 "nores": ("Hesh nárse tabılmadı", "Nothing found", "Hech narsa topilmadi", "Ничего не найдено"),
 "school": ("Mektebimiz (Kegeyli)", "Our school (Kegeyli)", "Maktabimiz (Kegeyli)", "Наша школа (Кегейли)"),
 "stories": ("Pitkeriwshilerimiz sóyleydi", "Our graduates say", "Bitiruvchilarimiz so‘zlaydi", "Слово выпускникам"),
}

SEAL_COL = {"nukus": "#0b5f78", "tashkent": "#a3202c", "samarkand": "#7c3aed", "khorezm": "#047857", "andijan": "#b45309",
            "navoi": "#1d4ed8", "kashkadarya": "#be185d", "namangan": "#0e7490", "surkhandarya": "#92400e"}
def seal(k):
    logo = os.path.join(ROOT, "photos", "unis", k + ".png")
    if os.path.exists(logo):
        return f'<span class="seal img"><img src="{{UP}}photos/unis/{k}.png" alt=""></span>'
    ab = G.ABBR.get(k, k.upper()); col = SEAL_COL.get(G.INST[k][4], "#0b5f78")
    fs = 15 if len(ab) <= 3 else 12 if len(ab) <= 4 else 9.5 if len(ab) <= 5 else 8.5
    return (f'<span class="seal" style="--sc:{col}"><svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="22" class="s1"/>'
            f'<circle cx="24" cy="24" r="17.5" class="s2"/><text x="24" y="{24 + fs * .36:.1f}" text-anchor="middle" font-size="{fs}">{ab}</text></svg></span>')
def grad_body(lang, i):
    tot = sum(n for _, n in G.YEARS); allp = [x for v in G.PLACED.values() for x in v]; pl = len(allp)
    dec = lambda v: f"{v:.1f}".replace(".", "," if lang != "en" else ".")
    pct = dec(pl / tot * 100) + "%"
    stu = lambda n: GT["student1"][i] if n == 1 else GT["students"][i].format(n=n)
    inst_all = _Ctr(k for k, _ in allp); city_all = _Ctr(G.INST[k][4] for k, _ in allp)
    iscol = lambda k: G.INST[k][5] == "college"
    ncol = sum(1 for k, _ in allp if iscol(k)); nuni = pl - ncol
    stats = "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v, l in [
        (tot, GT["s_grad"][i]), (dec(nuni / tot * 100) + "%", GT["s_uni"][i].format(p=nuni)), (dec(ncol / tot * 100) + "%", GT["s_col"][i].format(p=ncol)),
        (sum(1 for k in inst_all if not iscol(k)), GT["s_ninst"][i].format(c=sum(1 for k in inst_all if iscol(k)))), (len(city_all), GT["s_city"][i])])
    mx = max(n for _, n in G.YEARS)
    def yrow(y, n):
        c = sum(1 for k, _ in G.PLACED[y] if iscol(k)); u = len(G.PLACED[y]) - c
        lab = GT["y_uni"][i].format(a=u) + (f' · <span class="ycol">{GT["y_col"][i].format(a=c)}</span>' if c else "") + " " + GT["y_of"][i].format(b=n)
        return (f'<div class="yr"><span class="yl">{y}</span><div class="ybar"><i class="tot" style="width:{n / mx * 100:.1f}%"></i>'
                f'<i class="ok" style="width:{u / mx * 100:.1f}%"></i>' + (f'<i class="col" style="left:{u / mx * 100:.1f}%;width:{c / mx * 100:.1f}%"></i>' if c else "")
                + f'</div><span class="yv"><b>{round(u / n * 100)}%</b> {lab}</span></div>')
    years = "".join(yrow(y, n) for y, n in G.YEARS)
    years += (f'<ul class="ylegend"><li><i class="ok"></i>{GT["k_uni"][i]}</li><li><i class="col"></i>{GT["k_col"][i]}</li>'
              f'<li><i class="tot"></i>{GT2["na"][i]}</li></ul>')
    # ---- certificates
    C = G.CERTS; cw = sum(c["with_"] for c in C.values()); ct = sum(c["top"] for c in C.values())
    ci = sum(c["ielts"] for c in C.values()); cs = sum(c["sat"] for c in C.values())
    cstats = "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v, l in [
        (cw, GT2["c_with"][i].format(t=tot)), (ct, GT2["c_top"][i]), (ci, GT2["c_ielts"][i]), (cs, GT2["c_sat"][i].format(b=G.BEST_SAT))])
    def mini(title, vals, fmt, col):
        m = max(max(vals), 1)
        bars = "".join(f'<div class="mb"><span class="mv">{fmt(v)}</span><i style="height:{max(v / m * 100, 2):.0f}%;background:{col}"></i><small>{y[2:4]}/{y[7:]}</small></div>' for v, (y, _) in zip(vals, G.YEARS))
        return f'<div class="mini card"><h3>{title}</h3><div class="mbars">{bars}</div></div>'
    cpct = [round(C[y]["with_"] / n * 100) for y, n in G.YEARS]
    outside = [sum(1 for k, _ in G.PLACED[y] if G.INST[k][4] not in G.HOME) for y, _ in G.YEARS]
    medeng = [sum(1 for _, f in G.PLACED[y] if f in ("med", "eng")) for y, _ in G.YEARS]
    trends = (mini(GT2["t_cert"][i], cpct, lambda v: f"{v}%", "#f2b134") + mini(GT2["t_out"][i], outside, str, "#0b5f78")
              + mini(GT2["t_me"][i], medeng, str, "#a3202c"))
    # ---- spotlight medicine & engineering
    def spot(f, col):
        L = [k for k, ff in allp if ff == f]; ins = _Ctr(L)
        rows = "".join(f'<li>{seal(k)}<span class="sn">{G.INST[k][i]}</span><b>{n}</b></li>' for k, n in ins.most_common(3))
        return (f'<div class="spot" style="--sc:{col}"><div class="stop"><b>{len(L)}</b><div><h3>{G.FIELD[f][i]}</h3>'
                f'<p>{GT2["spot"][i].format(n=len(ins))}</p></div></div><ul class="slist">{rows}</ul></div>')
    spots = spot("med", "#a3202c") + spot("eng", "#1d4ed8")
    # ---- filterable block (all years + each year)
    def block(P, key):
        inst = _Ctr(k for k, _ in P); fld = _Ctr(f for _, f in P); city = _Ctr(G.INST[k][4] for k, _ in P); n_ = len(P)
        if not n_:
            return ""
        top = inst.most_common(); m1 = top[0][1]
        def irow(k, n):
            I = G.INST[k]; tag = f' <em>{GT["college"][i]}</em>' if I[5] == "college" else ""
            return f'<li>{seal(k)}<div class="il"><b>{I[i]}</b>{tag}<small>{G.CITY[I[4]][i]}</small></div><div class="ib"><i style="width:{max(n / m1 * 100, 3):.1f}%"></i></div><span>{n}</span></li>'
        ih = f'<ol class="ilist">{"".join(irow(k, n) for k, n in top[:8])}</ol>'
        if len(top) > 8:
            ih += f'<details><summary>{GT["all"][i].format(n=len(top))}</summary><ol class="ilist" start="9">{"".join(irow(k, n) for k, n in top[8:])}</ol></details>'
        fs = fld.most_common()
        stack = "".join(f'<i style="width:{n / n_ * 100:.2f}%;background:{G.FIELD[k][4]}" title="{G.FIELD[k][i]}"></i>' for k, n in fs)
        legend = "".join(f'<li><span class="sw" style="background:{G.FIELD[k][4]}"></span><b>{G.FIELD[k][i]}</b><em>{n} · {round(n / n_ * 100)}%</em></li>' for k, n in fs)
        out = sum(n for c, n in city.items() if c not in G.HOME)
        # map: real outline of Uzbekistan (equirectangular, cos-lat scaled)
        import math
        LO0, LO1, LA0, LA1 = 55.6, 75.2, 36.9, 45.9; k_ = math.cos(math.radians(41.3))
        W = 640; H = round(W * (LA1 - LA0) / ((LO1 - LO0) * k_))
        def xy(c):
            la, lo = G.GEO[c] if isinstance(c, str) else c
            return (lo - LO0) / (LO1 - LO0) * W, (LA1 - la) / (LA1 - LA0) * H
        outline = " ".join("M" + " L".join(f"{xy((p[1], p[0]))[0]:.1f} {xy((p[1], p[0]))[1]:.1f}" for p in ring) + " Z" for poly in UZB for ring in poly)
        kx, ky = xy("kegeyli"); svg = f'<path d="{outline}" class="land"/>'
        for c, n in sorted(city.items(), key=lambda kv: kv[1]):
            if c == "kegeyli":
                continue  # same spot as the school marker
            x_, y_ = xy(c); r = min(5 + (n ** 0.5) * 2.2, 18)
            if c != "nukus":
                svg += f'<path d="M{kx:.0f} {ky:.0f} Q{(kx + x_) / 2:.0f} {min(ky, y_) - 30:.0f} {x_:.0f} {y_:.0f}" class="arc"/>'
            svg += f'<circle cx="{x_:.0f}" cy="{y_:.0f}" r="{r:.1f}" class="cdot{" home" if c == "nukus" else ""}"/>'
        for c, n in city.items():
            if c == "kegeyli":
                continue
            x_, y_ = xy(c); r = min(5 + (n ** 0.5) * 2.2, 18)
            pos = {"namangan": ("middle", 0, -r - 8), "andijan": ("start", r + 5, r + 10), "tashkent": ("end", -r - 6, -r - 2), "nukus": ("start", r + 6, 16),
                   "khorezm": ("start", r + 6, 10), "navoi": ("end", -r - 6, 4)}.get(c, ("start", r + 6, 4))
            svg += f'<text x="{x_ + pos[1]:.0f}" y="{y_ + pos[2]:.0f}" text-anchor="{pos[0]}" class="clab">{G.CITY[c][i]} <tspan>{n}</tspan></text>'
        svg += f'<circle cx="{kx:.0f}" cy="{ky:.0f}" r="5" class="school"/><text x="{kx - 6:.0f}" y="{ky - 14:.0f}" class="clab sch">{GT2["school"][i]}</text>'
        mapsvg = f'<div class="gmap"><svg viewBox="0 0 {W} {H}" role="img" aria-label="{GT["city_h"][i]}">{svg}</svg></div>'
        beyond = sorted(((k, n) for k, n in inst.items() if G.INST[k][4] not in G.HOME), key=lambda kv: (-kv[1], G.INST[kv[0]][i]))
        bcards = "".join(f'<div class="bcard">{seal(k)}<div><small>{G.CITY[G.INST[k][4]][i]}</small><b>{G.INST[k][i]}</b></div><span class="bn">{n}</span></div>' for k, n in beyond)
        return (f'<div class="gview" data-y="{key}"{"" if key == "all" else " hidden"}>'
                f'<div class="gsec two"><div><h2>{GT["where_h"][i]}</h2>{ih}</div>'
                f'<div><h2>{GT["field_h"][i]}</h2><div class="stack">{stack}</div><ul class="legend">{legend}</ul></div></div>'
                f'<div class="gsec"><h2>{GT["city_h"][i]}</h2><p>{GT["city_p"][i].format(n=out)}</p>{mapsvg}'
                + (f'<h3 class="bh">{GT["beyond_h"][i]}</h3><div class="bgrid">{bcards}</div>' if bcards else "") + '</div></div>')
    views = block(allp, "all") + "".join(block(G.PLACED[y], y) for y, _ in G.YEARS)
    ychips = f'<button type="button" class="chip on" data-y="all">{GT2["allyears"][i]}</button>' + "".join(f'<button type="button" class="chip" data-y="{y}">{y}</button>' for y, _ in G.YEARS)
    gchips = (f'<button type="button" class="chip" data-y="all">{GT2["allyears"][i]} <em>{tot}</em></button>'
              + "".join(f'<button type="button" class="chip{" on" if n_ == 0 else ""}" data-y="{y}">{y} <em>{len(G.roster(y))}</em></button>' for n_, (y, _) in enumerate(reversed(G.YEARS))))
    kchips = "".join(f'<button type="button" class="chip{" on" if k_ == "all" else ""}" data-k="{k_}">{l_} <em></em></button>'
                     for k_, l_ in [("all", GT["k_all"][i]), ("uni", GT["k_uni"][i]), ("col", GT["k_col"][i]), ("none", GT2["na"][i])])
    grows = ""
    for y, _ in G.YEARS:
        for nm_, plc in G.roster(y):
            nm = nm_ if lang == "ru" else G.latin_name(nm_)
            if plc is None:
                grows += (f'<tr data-y="{y}" data-k="none" data-q="{nm.lower()}"><td class="gn">{nm}</td>'
                          f'<td><span class="gna">{GT2["na"][i]}</span></td><td><span class="gna">—</span></td></tr>')
                continue
            k, f = plc
            ctag = f' <em class="ctag">{GT["college"][i]}</em>' if iscol(k) else ""
            grows += (f'<tr data-y="{y}" data-k="{"col" if iscol(k) else "uni"}" data-q="{(nm + " " + G.INST[k][i]).lower()}"><td class="gn">{nm}</td>'
                      f'<td><div class="gi">{seal(k)}<span>{G.INST[k][i]}{ctag}<small>{G.CITY[G.INST[k][4]][i]}</small></span></div></td>'
                      f'<td><span class="fchip" style="--sc:{G.FIELD[f][4]}">{G.FIELD[f][i]}</span></td></tr>')
    th = GT2["th"][i]
    glist = (f'<div class="gsec" id="glist"><h2>{GT2["list_h"][i]}</h2><p>{GT2["list_p"][i]}</p>'
             f'<div class="gtools"><input type="search" id="gq" placeholder="{GT2["search"][i]}" aria-label="{GT2["search"][i]}"><div class="chips gyears" role="group">{gchips}</div><div class="chips gkinds" role="group">{kchips}</div></div>'
             f'<div class="gtable card"><table><thead><tr><th>{th[0]}</th><th>{th[1]}</th><th>{th[2]}</th></tr></thead><tbody>{grows}</tbody></table>'
             f'<p class="note" id="gnone" hidden>{GT2["nores"][i]}</p></div></div>')
    fcnt = _Ctr(f for _, f in allp); order = [f for f, _ in fcnt.most_common()]
    pchips = "".join(f'<button type="button" class="chip pc{" on" if n_ == 0 else ""}" data-f="{f}" style="--sc:{G.FIELD[f][4]}">{G.FIELD[f][i]} <em>{fcnt[f]}</em></button>' for n_, f in enumerate(order))
    ppan = ""
    for n_, f in enumerate(order):
        rows = [(k, y) for y in G.PLACED for k, ff in G.PLACED[y] if ff == f]
        ic = _Ctr(k for k, _ in rows); top = ic.most_common(5); mxi = top[0][1]
        irows = "".join(f'<div class="prow">{seal(k)}<div class="pname"><b>{G.INST[k][i]}</b><small>{G.CITY[G.INST[k][4]][i]}</small>'
                        f'<div class="pbar"><i style="width:{c / mxi * 100:.0f}%"></i></div></div><span class="pn">{c}</span></div>' for k, c in top)
        rest = len(ic) - len(top)
        if rest > 0: irows += f'<p class="pmore">{GT2["p_more"][i].format(n=rest)}</p>'
        yc = _Ctr(y for _, y in rows); myc = max(yc.values())
        yrows = "".join(f'<div class="py"><span>{y}</span><div class="pbar"><i style="width:{yc[y] / myc * 100:.0f}%"></i></div><b>{yc[y]}</b></div>' for y, _ in G.YEARS)
        cc = _Ctr(G.INST[k][4] for k, _ in rows)
        cch = "".join(f'<span class="cchip">{G.CITY[c][i]} <b>{n}</b></span>' for c, n in cc.most_common())
        LV = ["B1", "B2", "C", "C+", "B", "B+", "A", "A+"]  # CEFR B1<B2 first, then national levels low->high
        rk = lambda s, l: (LV.index(l) if s not in "ET" else LV.index(l))
        certs = [(s.split(":")[0], s.split(":")[1]) for y in G.PLACED if y != "2022/2023"
                 for (k_, ff), cs_ in zip(G.PLACED[y], G.CERT_SUBJ[y]) if ff == f for s in cs_]
        nn = sum(1 for y in G.PLACED if y != "2022/2023" for (k_, ff) in G.PLACED[y] if ff == f)
        aa = sum(1 for y in G.PLACED if y != "2022/2023" for (k_, ff), cs_ in zip(G.PLACED[y], G.CERT_SUBJ[y]) if ff == f and cs_)
        if nn and aa:
            sc = {}
            for s, l in certs: sc.setdefault(s, []).append(l)
            lvl = lambda s, l: l if s in "ET" else l
            srows = ""
            for s, ls in sorted(sc.items(), key=lambda t: -len(t[1]))[:5]:
                ls2 = sorted(ls, key=lambda l: LV.index(l)); med = ls2[len(ls2) // 2]; best = ls2[-1]
                srows += (f'<div class="prow csub"><div class="pname"><b>{GT2["subj"][s][i]}</b>'
                          f'<small>{GT2["c_typ"][i].format(l=med)} · {GT2["c_best"][i].format(l=best)}</small>'
                          f'<div class="pbar"><i style="width:{len(ls) / nn * 100:.0f}%"></i></div></div><span class="pn">{len(ls)}</span></div>')
            cblock = f'<h3>{GT2["c_h"][i]}</h3><p class="csum">{GT2["c_sum"][i].format(a=aa, n=nn)}</p>{srows}<p class="pmore">{GT2["c_note"][i]}</p>'
        else:
            cblock = f'<h3>{GT2["c_h"][i]}</h3><p class="pmore">{GT2["c_none"][i]}</p>'
        ppan += (f'<div class="ppanel card" data-f="{f}" style="--sc:{G.FIELD[f][4]}"{"" if n_ == 0 else " hidden"}>'
                 f'<div class="pbig"><b>{len(rows)}</b><span>{GT2["p_big"][i].format(n=len(rows)).replace(str(len(rows)), "", 1).strip()}</span>'
                 f'<em>{GT2["p_share"][i].format(p=dec(len(rows) / pl * 100))}</em></div>'
                 f'<h3>{GT2["p_where"][i]}</h3>{irows}<h3>{GT2["p_year"][i]}</h3>{yrows}<h3>{GT2["p_city"][i]}</h3><div class="cchips">{cch}</div>{cblock}</div>')
    path = (f'<div class="gsec" id="path"><h2>{GT2["p_h"][i]}</h2><p>{GT2["p_p"][i]}</p>'
            f'<div class="chips pchips" role="group">{pchips}</div>{ppan}<p class="note">{GT2["p_note"][i]}</p></div>')
    stories = ""
    if G.STORIES:
        cards = "".join(f'<figure class="story">{f"<img src=\'{{UP}}{s_["photo"]}\' alt=\'\'>" if s_.get("photo") else ""}<blockquote>{s_["text"][i]}</blockquote>'
                        f'<figcaption><b>{s_["name"]}</b><span>{G.INST[s_["inst"]][i]} · {s_["year"]}</span></figcaption></figure>' for s_ in G.STORIES)
        stories = f'<div class="gsec"><h2>{GT2["stories"][i]}</h2><div class="stories">{cards}</div></div>'
    return f"""<p class="glead">{GT['lead'][i].format(n=tot, u=nuni, c=ncol)}</p>
<div class="stats gstats">{stats}</div>
<div class="gsec"><h2>{GT['years_h'][i]}</h2><div class="years">{years}</div></div>
<div class="gsec"><h2>{GT2['cert_h'][i]}</h2><p>{GT2['cert_p'][i]}</p><div class="stats gstats cstats">{cstats}</div></div>
<div class="gsec"><h2>{GT2['trend_h'][i]}</h2><div class="minis">{trends}</div></div>
<div class="gsec spots">{spots}</div>
{stories}
<div class="gsec gfilter"><h2>{GT2['explore_h'][i]}</h2><div class="chips ychips" role="group">{ychips}</div></div>
{views}
{path}
{glist}
<p class="note">{GT['note'][i]}</p>"""

def person_card(la, cy, r, lang):
    n = LP.full(la, cy, lang)
    ini = "".join(w[0] for w in n.split()[:2])
    top = " lead-top" if r == "director" else ""
    lines = LEADER_INFO.get(la, [])
    info = ('<ul class="linfo">' + "".join(f"<li>{l[LI[lang]]}</li>" for l in lines) + "</ul>") if lines else ""
    ph = slug_l(la)
    ic, col = ROLE_ICON.get(r, (ini, "ic-teal"))
    _s = "-s" if os.path.exists(os.path.join(ROOT, "photos", "leaders", ph + "-s.jpg")) else ""
    av = (f'<img src="{{UP}}photos/leaders/{ph}{_s}.jpg" alt="{n}" loading="lazy" decoding="async">' if os.path.exists(os.path.join(ROOT, "photos", "leaders", ph + ".jpg")) else ini)
    return (f'<div class="person card{top}"><div class="avatar" aria-hidden="true">{av}</div>'
            f'<div><h3 style="margin:0"><a class="plink" href="{LP.slug(la)}/">{n}</a></h3><p class="role"><span class="ric {col}">{ic}</span><span>{ROLES[r][lang]}</span></p>{info}'
            f'<a class="tprof" href="{LP.slug(la)}/">{TL["prof"][LI[lang]]} →</a></div></div>')

BYC = {
 "h": ("Klass boyınsha muǵallimler", "Teachers by class", "Sinf bo‘yicha o‘qituvchilar", "Учителя по классам"),
 "tab": ("Klass boyınsha", "By class", "Sinf bo‘yicha", "По классам"),
 "desc": ("Hár bir klassta qaysı muǵallimler qaysı pánnen sabaq beredi — sabaq kestesi boyınsha.", "Which teachers teach each class and which subjects — from the timetable.",
          "Har bir sinfda qaysi o‘qituvchilar qaysi fandan dars beradi — dars jadvali bo‘yicha.", "Какие учителя ведут какие предметы в каждом классе — по расписанию."),
 "p": ("Klasstı tańlań — onda sabaq beretuǵın barlıq muǵallimler hám pánler kórsetiledi.", "Pick a class to see every teacher who teaches it and their subjects.",
       "Sinfni tanlang — unda dars beradigan barcha o‘qituvchilar va fanlar ko‘rsatiladi.", "Выберите класс — покажем всех учителей и их предметы."),
 "lpw": ("{n} sabaq/hápte", "{n} lessons/week", "{n} dars/hafta", "{n} ур./нед."),
 "head": ("Klass basshısı", "Class teacher", "Sinf rahbari", "Классный руководитель"),
 "tot": ("{t} muǵallim", "{t} teachers", "{t} nafar o‘qituvchi", "{t} учителей"),
}

def staff_strip(lang):
    i = LI[lang]; st = TB.stats(); cols = {"total": "#0b7a8f", "high": "#d4a017", "ma": "#7c3aed", "cert": "#2a7fd1", "heads": "#a3202c", "subj": "#2f8f5b"}
    return '<div class="tbstats">' + "".join(f'<div style="--ac:{cols[k]}"><b>{st[k]}</b><span>{TB.ST[k][i]}</span></div>' for k in ("total", "high", "ma", "cert", "heads", "subj")) + '</div>'

def by_class(lang, up=""):
    i = LI[lang]; esc = _html.escape
    per = {c: {} for c in TT["classes"]}
    for j in range(len(TEACHERS)):
        for (d, p), xs in TP.schedule(j, TT, TP_M).items():
            for c, sname in xs:
                per[c].setdefault((j, sname), 0); per[c][(j, sname)] += 1
    order = sorted(per, key=lambda c: (int(c.split("-")[0]), c))
    chips = "".join(f'<button type="button" class="cnchip" data-c="{c}" style="--ac:{RS.gcol(int(c.split("-")[0]))}">{c}</button>' for c in order)
    panels = ""
    for c in order:
        head = HD.HEAD.get(c, (None,))[0]
        rows = sorted(per[c].items(), key=lambda kv: (TEACHERS[kv[0][0]][0] != head, -kv[1]))
        lis = ""
        for (j, sname), n in rows:
            nm = TP.name(j, lang); ini = "".join(w[0] for w in nm.split()[:2]); sj = TT_SUBJ.get(sname, (sname,) * 4 + ("#0b7a8f",))
            ish = TEACHERS[j][0] == head
            lis += (f'<li class="{"hd" if ish else ""}" style="--ac:{sj[4]}"><a href="../{TP.slug(TEACHERS[j][0])}/"><span class="bcav">{TP.small(TEACHERS[j][0], up, "", ini)}</span><div><b>{esc(nm)}</b>'
                    f'<small>{sj[i]}' + (f' · <em>{BYC["head"][i]}</em>' if ish else '') + f'</small></div>' + ("" if TP.hide_lpw(j) else f'<span class="bcn">{BYC["lpw"][i].format(n=n)}</span>') + '</a></li>')
        nt = len({j for (j, s) in per[c]}); nl = sum(per[c].values())
        panels += f'<div class="bcp" data-c="{c}" hidden><h3>{c} <small>{BYC["tot"][i].format(t=nt)}</small></h3><ul class="bclist">{lis}</ul></div>'
    js = ("<script>(function(){var ch=document.querySelectorAll('.bcchips .cnchip'),ps=document.querySelectorAll('.bcp');"
          "function show(c){ch.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.c===c)});ps.forEach(function(p){p.hidden=p.dataset.c!==c})}"
          "ch.forEach(function(b){b.addEventListener('click',function(){show(b.dataset.c);try{localStorage.setItem('ttcls',b.dataset.c)}catch(e){};history.replaceState(null,'','#'+b.dataset.c)})});"
          "var c=decodeURIComponent(location.hash.slice(1));if(!c){try{c=localStorage.getItem('ttcls')}catch(e){}}show(c&&[].some.call(ps,function(p){return p.dataset.c===c})?c:ch[0].dataset.c)})();</script>")
    return f'<p>{BYC["p"][i]}</p><div class="cnchips bcchips">{chips}</div>{panels}{js}'

NAVG = {
 "school": ("Mektep", "School", "Maktab", "Школа"),
 "students": ("Oqıwshılarǵa", "Students", "O‘quvchilarga", "Ученикам"),
 "results": ("Nátiyjeler", "Results", "Natijalar", "Результаты"),
 "abroad": ("Qabıllaw", "Admission", "Qabul", "Приём"),
 "parents": ("Ata-analar", "Parents", "Ota-onalar", "Родителям"),
}

def teach_tabs(sub, lang, h):
    i = LI[lang]
    tabs = [("teachers/", TL["all_teachers"][i], '<circle cx="9" cy="8" r="3"/><path d="M3 20c.5-3.500 3-5.500 6-5.500s5.500 2 6 5.500"/><path d="M16 6a3 3 0 0 1 0 5.500M18 14.500c1.700.8 2.700 2.500 3 5"/>', "#0b7a8f", len(TEACHERS)),
            ("teachers/class-teachers/", HD.T["h"][i], '<path d="M3 7l4 4 5-7 5 7 4-4-2 12H5z"/>', "#d4a017", len(HD.HEADS)),
            ("teachers/by-class/", BYC["tab"][i], '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>', "#2a7fd1", len(TT["classes"])),
            (SEM.SUB, SEM.TAB[i], '<rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/><path d="M8 14h3"/>', "#7c3aed", len(SEM.SEMINARS))]
    return '<nav class="abtabs">' + "".join(f'<a href="{h(k)}"' + (' aria-current="page"' if k == sub else '') + f'><span class="mi" style="--mc:{c}"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{p}</svg></span>{n} <em class="tbn">{cnt}</em></a>' for k, n, p, c, cnt in tabs) + '</nav>'

def heads_html(lang, pre=""):
    i = LI[lang]; esc = _html.escape; grades = {}
    for c, _ in HD.HEADS:
        grades.setdefault(int(c.split("-")[0]), []).append(c)
    out = ""
    for g, cs in grades.items():
        col = RS.gcol(g)
        cards = "".join(f'<a class="hdc" href="{pre}{slug(HD.HEAD[c][0])}/" style="--ac:{col}"><span class="hdcl">{c}</span><span class="hdnm"><b>{esc(HD.name(c, lang))}</b><small>{SUBJECTS[HD.HEAD[c][1]][lang]}</small></span></a>' for c in cs)
        out += f'<div class="hdg"><h3 style="--ac:{col}"><span>{g}</span>{HD.T["grade"][i].format(g=g)}</h3><div class="hdcs">{cards}</div></div>'
    return (f'<section class="hdsec" id="class-teachers"><div class="hdhead"><div><h2>{HD.T["h"][i]}</h2><p>{HD.T["p"][i].format(n=len(HD.HEADS))}</p></div>'
            f'<span class="hdtot"><b>{len(HD.HEADS)}</b>{HD.T["total"][i]}</span></div><div class="hdgs">{out}</div></section>')

def teacher_cards(lang, up):
    i = LI[lang]; esc = _html.escape
    nm = (lambda c: _shown(c, "ru")) if lang == "ru" else latin
    chips = f'<button type="button" class="chip on" data-s="all">{TL["all"][i]} <em>{len(TEACHERS)}</em></button>' + "".join(
        f'<button type="button" class="chip" data-s="{k}">{v[lang]} <em>{sum(1 for x in TEACHERS if x[1] == k)}</em></button>'
        for k, v in SUBJECTS.items() if any(x[1] == k for x in TEACHERS))
    cards = []
    order = sorted(range(len(TEACHERS)), key=lambda j: (list(SUBJECTS).index(TEACHERS[j][1]), {"high": 0, "first": 1, "second": 2, "spec": 3, None: 4}[TEACHERS[j][2]], latin(TEACHERS[j][0])))
    for j in order:
        cy, sk, ck = TEACHERS[j]; pr = PROFILES[j]; name = nm(cy); sl = slug(cy)
        photo = os.path.join(ROOT, "photos", "teachers", sl + ".jpg")
        ini = "".join(w[0] for w in name.split()[:2])
        _s = "-s" if os.path.exists(os.path.join(ROOT, "photos", "teachers", sl + "-s.jpg")) else ""
        av = f'<img src="{up}photos/teachers/{sl}{_s}.jpg" alt="{esc(name)}" width="160" height="160" loading="lazy" decoding="async">' if os.path.exists(photo) else f'<span>{ini}</span>'
        edu = "<br>".join(f'{UNI[u][i]}, {y}' + (f' ({DEG[d][i]})' if d == "ma" else "") for y, u, d in pr["edu"])
        rows = ""
        if pr.get("pos"):
            rows += f'<dt>{TL["pos"][i]}</dt><dd>{pr["pos"][i]}</dd>'
        rows += f'<dt>{TL["edu"][i]}</dt><dd>{edu}</dd>'
        if pr["spec"]:
            rows += f'<dt>{TL["spec"][i]}</dt><dd>{SPEC[pr["spec"]][i]}</dd>'
        if pr.get("since"):
            rows += f'<dt>{TL["since"][i]}</dt><dd>{TL["since_v"][i].format(y=pr["since"])}</dd>'
        if pr["train"]:
            rows += f'<dt>{TL["train"][i]}</dt><dd>{pr["train"]}</dd>'
        ach = ""
        if pr["ach"]:
            items = [f"<li>{esc(a[i])}</li>" for a in pr["ach"]]
            ach = f'<h4>{TL["ach"][i]}</h4><ul class="ach">{"".join(items[:3])}</ul>'
            if len(items) > 3:
                ach += f'<details><summary>{TL["more"][i].format(n=len(items) - 3)}</summary><ul class="ach">{"".join(items[3:])}</ul></details>'
        cards.append(f'<article class="tcard" data-s="{sk}" data-n="{esc((latin(cy) + " " + cy).lower())}" id="t-{sl}">'
            f'<header><div class="tav c-{ck}">{av}</div><div><h2 class="tname"><a href="{sl}/">{esc(name)}</a></h2><p class="tsub">{SUBJECTS[sk][lang]}</p>'
            + (f'<span class="badge c-{ck}">{CATS[ck][lang]}</span>' if ck else '') + f'</div></header>{TB.html(j, i)}<dl>{rows}</dl>{ach}<a class="tprof" href="{sl}/">{TL["prof"][i]} →</a></article>')
    return (f'<div class="tbar"><input type="search" id="tq" placeholder="{TL["search"][i]}" aria-label="{TL["search"][i]}">'
            f'<div class="chips" role="group">{chips}</div></div><div class="tcards">{"".join(cards)}</div>'
            f'<p id="tnone" class="note" hidden>{TL["none"][i]}</p>')

def page(lang, sub=""):
    t = T[lang]; i = LI[lang]; url = DOMAIN + path(lang) + sub
    here = path(lang) + sub
    up = posixpath.relpath(".", here.rstrip("/") or ".") + "/" if here else ""
    up = "" if up == "./" else up
    home = href(lang, sub, lang, "")
    alts = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{DOMAIN + path(l) + sub}">' for l in ORDER)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{DOMAIN + sub}">'
    langs = "".join(
        f'<a href="{href(lang, sub, l, sub)}" hreflang="{l}" lang="{l}" title="{T[l]["lang_name"]}"'
        + (' aria-current="page"' if l == lang else "")
        + f'>{FLAGS[l]}<span>{T[l]["lang_code"]}</span></a>' for l in ORDER)
    pre = "" if sub == "" else home
    navitems = [
        (href(lang, sub, lang, "about/"), t["nav"][0], "about/", "about"),
        (href(lang, sub, lang, "admission/"), t["nav"][2], "admission/", "admission"),
        (href(lang, sub, lang, "abroad/"), AB.NAME[i], "abroad/", "abroad"),
        (href(lang, sub, lang, CSL.SUB), CSL.NAME[i], CSL.SUB, "counseling"),
        (href(lang, sub, lang, POL.SUB), POL.NAME[i], POL.SUB, "policies"),
        (href(lang, sub, lang, CLB.SUB), CLB.NAME[i], CLB.SUB, "clubs"),
        (pre + "#subjects", t["nav"][1], "", "subjects"),
        (href(lang, sub, lang, "teachers/"), t["teach_h"], "teachers/", "teachers"),
        (href(lang, sub, lang, "leadership/"), t["lead_h"], "leadership/", "leadership"),
        (href(lang, sub, lang, "timetable/"), TT_TXT["title"][i], "timetable/", "timetable"), (href(lang, sub, lang, CAL.SUB), CAL.NAME[i], CAL.SUB, "calendar"), (href(lang, sub, lang, GAL.SUB), GAL.NAME[i], GAL.SUB, "gallery"), (href(lang, sub, lang, "study/"), STD.NAME[i], "study/", "study"),
        (href(lang, sub, lang, "achievements/"), ACH.NAME["achievements/"][i], "achievements/", "results"),
        (href(lang, sub, lang, "results/"), RS.NAME[i], "results/", "tests"),
        (href(lang, sub, lang, "graduates/"), GT["title"][i], "graduates/", "graduates"),
        (href(lang, sub, lang, "parents/"), EX.NAME["parents/"][i], "parents/", "parents"),
        (href(lang, sub, lang, "canteen/"), CN.NAME[i], "canteen/", "canteen"),
        (href(lang, sub, lang, "documents/"), EX.NAME["documents/"][i], "documents/", "documents"),
        (href(lang, sub, lang, "news/"), t["nav"][3], "news/", "news")] + ([(href(lang, sub, lang, "partners/"), PT.H[i], "partners/", "partners")] if PT.PARTNERS else []) + [(pre + "#contact", t["nav"][5], "", "contact")]
    def _cur(s_):
        return bool(s_ and (s_ == sub or (s_ == CLB.SUB and sub == CLB.JSUB) or (s_ == "abroad/" and sub in AB.GROUP) or (s_ == "achievements/" and sub in ACH.SUBS) or (s_ == "canteen/" and sub in CN.SUBS) or (s_ == "results/" and sub in RS.SUBS) or (s_ == "teachers/" and (sub in TP.SUB or sub in ("teachers/class-teachers/", "teachers/by-class/", SEM.SUB))) or (s_ == "leadership/" and sub in LP.SUB) or (s_ == "documents/" and sub.startswith("documents/"))))
    NI = {x[3]: x for x in navitems}
    groups = [("school", NAVG["school"][i], "about", ["about", "leadership", "teachers", "subjects", "news", "partners"]),
              ("students", NAVG["students"][i], "timetable", ["timetable", "calendar", "clubs", "study", "canteen"]),
              ("results", NAVG["results"][i], "results", ["results", "tests", "graduates"]),
              ("abroad", NAVG["abroad"][i], "abroad", ["admission", "abroad", "counseling"]),
              ("parents", NAVG["parents"][i], "parents", ["parents", "documents", "policies", "contact"])]
    nav = ""
    for gk, gl, gi, keys in groups:
        its = [NI[k] for k in keys if k in NI]
        on = any(_cur(s_) for h, n, s_, k in its)
        links = "".join(f'<a href="{h}"' + (' aria-current="page"' if _cur(s_) else "") + f'><span class="mi" style="--mc:{NAV_ICON[k][1]}">{NAV_ICON[k][0]}</span><span>{n}</span></a>' for h, n, s_, k in its)
        nav += (f'<li class="ng{" on" if on else ""}"><button type="button" class="ngb" aria-expanded="false" aria-controls="ng-{gk}"><span class="mi" style="--mc:{NAV_ICON[gi][1]}">{NAV_ICON[gi][0]}</span><span>{gl}</span>'
                f'<svg class="ngc" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.500" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>'
                f'<div class="ngp" id="ng-{gk}" hidden>{links}</div></li>')
    def _pi(p):
        inner = (f'<img src="{up}photos/partners/{p["logo"]}" alt="{p["name"]}" height="52">' if p["logo"] else f'<span class="pbadge">{p["name"][:2].upper()}</span><span class="pname">{p["name"]}</span>')
        return f'<a class="pitem{" pinv" if p.get("dark") else ""}" href="{p["url"]}" target="_blank" rel="noopener" aria-label="{p["name"]}" title="{p["name"]}">{inner}</a>'
    _pl = [_pi(p) for p in PT.PARTNERS]
    _rep = max(2, -(-8 // max(1, len(_pl))))
    partners_html = (f'<section id="partners" class="band pstrip"><div class="wrap"><h2>{PT.H[i]}</h2><p>{PT.P[i]} <a href="{href(lang, sub, lang, "partners/")}" class="pall">{PT.X["all"][i]} →</a></p></div>'
                     f'<div class="pmar" role="list"><div class="ptrack">{"".join(_pl * _rep)}</div><div class="ptrack" aria-hidden="true">{"".join(x.replace("<a ", "<a tabindex=-1 ") for x in _pl * _rep)}</div></div></section>') if (_pl and sub != "partners/") else ""
    SOC = {"tg": _I('<path d="M21 4L3 11l6 2 2 6 3-4 5 4z"/><path d="M9 13l8-6"/>'), "ph": _I('<path d="M6 3h3l2 5-2 1.500a11 11 0 0 0 6 6L16.500 14l5 2v3a2 2 0 0 1-2 2A16 16 0 0 1 4 5a2 2 0 0 1 2-2z"/>'), "ml": _I('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>'), "pin": _I('<path d="M12 21s-6-5.600-6-10.500a6 6 0 0 1 12 0C18 15.400 12 21 12 21z"/><circle cx="12" cy="10.500" r="2.200"/>'), "clk": _I('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')}
    _fl = lambda L: "".join(f'<li><a href="{h}">{n}</a></li>' for h, n in L)
    SPN = {"kaa": "Mektep profili (EN, PDF)", "en": "School Profile (PDF)", "uz": "Maktab profili (EN, PDF)", "ru": "Профиль школы (EN, PDF)"}[lang]
    foot_school = _fl([(href(lang, sub, lang, "about/"), t["nav"][0]), (href(lang, sub, lang, INTL.SUB), INTL.NAME[i]), (href(lang, sub, lang, SUP.SUB), SUP.NAME[i]), (f"{up}school-profile/", SPN), (href(lang, sub, lang, POL.SUB), POL.NAME[i]), (href(lang, sub, lang, "leadership/"), t["lead_h"]), (href(lang, sub, lang, "teachers/"), t["teach_h"]), (href(lang, sub, lang, "timetable/"), TT_TXT["title"][i]), (href(lang, sub, lang, CAL.SUB), CAL.NAME[i]), (href(lang, sub, lang, GAL.SUB), GAL.NAME[i]), (href(lang, sub, lang, CLB.SUB), CLB.NAME[i]), (href(lang, sub, lang, "study/"), STD.NAME[i]), (href(lang, sub, lang, "graduates/"), GT["title"][i]), (href(lang, sub, lang, "achievements/"), ACH.NAME["achievements/"][i]), (href(lang, sub, lang, "results/"), RS.NAME[i]), (href(lang, sub, lang, "admission/"), t["nav"][2]), (href(lang, sub, lang, "parents/"), EX.NAME["parents/"][i]), (href(lang, sub, lang, "canteen/"), CN.NAME[i])])
    foot_abroad = _fl([(href(lang, sub, lang, CSL.SUB), CSL.NAME[i])] + [(href(lang, sub, lang, k), AB.SUBNAME[k][i]) for k in ("abroad/", "abroad/plan/", "abroad/scholarships/", "abroad/calendar/", "abroad/checklist/", "abroad/calculator/", "abroad/sat/", "ielts/")])
    school = {
      "@context": "https://schema.org", "@type": "School", "name": t["brand"],
      "alternateName": [T[l]["brand"] for l in ORDER if l != lang] + ["Kegeyli QM", "Kegeyli IM"],
      "url": DOMAIN + path(lang), "telephone": PHONE, "email": EMAIL, "sameAs": [TG, MAP], "logo": DOMAIN + "logo-512.png",
      "openingHours": "Mo-Sa 08:30-17:00", "hasMap": MAP,
      "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LNG}, "inLanguage": t["html_lang"],
      "address": {"@type": "PostalAddress", "streetAddress": t["street"], "addressLocality": t["town"],
                  "addressRegion": t["region"], "addressCountry": "UZ"},
      "employee": [{"@type": "Person", "name": (cy if lang == "ru" else la), "jobTitle": ROLES[r][lang]} for la, cy, r in LEADERS]}
    ld = [school]
    if sub == "":
        title, desc = t["title"], t["desc"]
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]})
        body = home_body(lang, t, i, up)
    else:
        name = {"abroad/": AB.NAME[i], "abroad/applications/": AB.SUBNAME["abroad/applications/"][i], "abroad/scholarships/": AB.SUBNAME["abroad/scholarships/"][i], "abroad/top10/": AB.TP.NAME[i], "abroad/countries/": AB.CO.NAME[i], "abroad/calendar/": AB.DLN.NAME[i], "abroad/checklist/": AB.CKL.NAME[i], "abroad/calculator/": AB.CAL.NAME[i], "abroad/sat/": AB.SAT.NAME[i], "abroad/plan/": AB.PL.TITLE[i], "abroad/essay/": AB.ESS.NAME[i], "abroad/commonapp/": AB.AP.NAME["abroad/commonapp/"][i], "abroad/ucas/": AB.AP.NAME["abroad/ucas/"][i], "ielts/": IE.NAME[i], "partners/": PT.H[i], CAL.SUB: CAL.NAME[i], GAL.SUB: GAL.NAME[i], INTL.SUB: INTL.NAME[i], SUP.SUB: SUP.NAME[i], CSL.SUB: CSL.NAME[i], POL.SUB: POL.NAME[i], CLB.SUB: CLB.NAME[i], CLB.JSUB: CLB.JNAME[i], "about/": AU.NAME[i], "news/": NW.NAME[i], "study/": STD.NAME[i], "admission/": t["nav"][2], "parents/": EX.NAME["parents/"][i], "documents/": EX.NAME["documents/"][i], "teachers/": t["teach_h"], "leadership/": t["lead_h"], "timetable/": TT_TXT["title"][i], "graduates/": GT["title"][i], **{k: CN.NAMES[k][i] for k in CN.SUBS}, **RS.names(i), **LW.names(i), "teachers/class-teachers/": HD.T["h"][i], "teachers/by-class/": BYC["h"][i], SEM.SUB: SEM.NAME[i], **{k: TP.name(j, lang) for k, j in TP.SUB.items()}, **{k: LP.name(n, lang) for k, n in LP.SUB.items()}, **{k: ACH.NAME[k][i] for k in ACH.SUBS}}[sub]
        title = f"{name} — {t['brand']}"
        desc = {"abroad/": AB.DESC["abroad/"], "abroad/applications/": AB.DESC["abroad/applications/"], "abroad/scholarships/": AB.DESC["abroad/scholarships/"], "abroad/top10/": AB.DESC["abroad/top10/"], "abroad/countries/": AB.DESC["abroad/countries/"], "abroad/calendar/": AB.DESC["abroad/calendar/"], "abroad/checklist/": AB.DESC["abroad/checklist/"], "abroad/calculator/": AB.DESC["abroad/calculator/"], "abroad/sat/": AB.DESC["abroad/sat/"], "abroad/plan/": AB.DESC["abroad/plan/"], "abroad/essay/": AB.DESC["abroad/essay/"], "abroad/commonapp/": AB.DESC["abroad/commonapp/"], "abroad/ucas/": AB.DESC["abroad/ucas/"], "ielts/": IE.DESC, "partners/": PT.PAGE_DESC, CAL.SUB: CAL.DESC, GAL.SUB: GAL.DESC, INTL.SUB: INTL.DESC, SUP.SUB: SUP.DESC, CSL.SUB: CSL.DESC, POL.SUB: POL.DESC, CLB.SUB: CLB.DESC, CLB.JSUB: CLB.JDESC, "about/": AU.DESC, "news/": NW.DESC, "study/": STD.DESC, "admission/": EX.DESC["admission/"], "parents/": EX.DESC["parents/"], "documents/": EX.DESC["documents/"], "teachers/": TL["teach_desc"], "leadership/": TL["lead_desc"], "timetable/": TT_TXT["desc"], "graduates/": GT["desc"], **CN.DESCS, **RS.descs(), **LW.descs(), "teachers/class-teachers/": HD.DESC, "teachers/by-class/": BYC["desc"], SEM.SUB: SEM.DESC, **{k: TP.desc(j) for k, j in TP.SUB.items()}, **{k: LP.desc(n) for k, n in LP.SUB.items()}, **ACH.DESC}[sub][i].format(b=t["brand"], n=len(TEACHERS))
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": TL["home"][i], "item": DOMAIN + path(lang)},
            {"@type": "ListItem", "position": 2, "name": name, "item": url}]})
        if sub in TP.SUB or sub in LP.SUB:
            _j = TP.SUB.get(sub); _role = SUBJECTS[TEACHERS[_j][1]][lang] if _j is not None else LP.ROLES[LP.LEADERS[LP.SUB[sub]][2]][lang]
            ld.append({"@context": "https://schema.org", "@type": "ProfilePage", "url": url, "mainEntity": {"@type": "Person", "name": name, "jobTitle": _role,
                       "worksFor": {"@type": "School", "name": t["brand"], "url": DOMAIN + path(lang)}}})
        if sub == "timetable/":
            inner = tt_body(lang, i)
        elif sub == "graduates/":
            inner = grad_body(lang, i)
        elif sub in [l["sub"] for l in LW.LAWS]:
            inner = LW.body(sub, i, "{UP}", lambda k: href(lang, sub, lang, k), NW.fmt)
        elif sub in LP.SUB:
            inner = LP.body(sub, lang, "{UP}", lambda k: href(lang, sub, lang, k), {"ROOT": ROOT, "PHONE": PHONE, "PHONE_TXT": PHONE_TXT, "TG": TG, "KEY": WEB3FORMS_KEY, "ach": DIR_ACH})
        elif sub in TP.SUB:
            inner = TP.body(sub, lang, "{UP}", lambda k: href(lang, sub, lang, k), {"tt": TT, "M": TP_M, "TT_SUBJ": TT_SUBJ, "BELLS": BELLS, "ROOT": ROOT})
        elif sub in RS.SUBS:
            inner = RS.body(sub, i, lambda k: href(lang, sub, lang, k))
        elif sub in CN.SUBS:
            inner = CN.body(sub, i, "{UP}", lambda k: href(lang, sub, lang, k))
        elif sub in ACH.SUBS:
            inner = ACH.body(sub, i, lambda k: href(lang, sub, lang, k), GT2["subj"])
        elif sub in AB.GROUP and sub != "ielts/":
            inner = AB.body(sub, lang, i, t, lambda k: href(lang, sub, lang, k), {"PHONE": PHONE, "PHONE_TXT": PHONE_TXT, "TG": TG})
        elif sub == "ielts/":
            inner = AB.tabs(sub, lang, i, lambda k: href(lang, sub, lang, k)) + ACH.ielts_banner(i, href(lang, sub, lang, "achievements/ielts/")) + IE.body(lang, i)
        elif sub in ("admission/", "parents/", "documents/"):
            inner = EX.body(sub, lang, i, t, ROOT, {"BELLS": BELLS, "href_tt": href(lang, sub, lang, "timetable/"), "href_cn": href(lang, sub, lang, "canteen/not-allowed/"), "cn": CN.NAMES["canteen/not-allowed/"][i], "cnd": CN.X["hero_h"][i], "tt": TT_TXT["title"][i], "href_gr": href(lang, sub, lang, "graduates/"), "gr": GT["title"][i],
                                                    "TG": TG, "PHONE": PHONE, "PHONE_TXT": PHONE_TXT, "EMAIL": EMAIL, "MAP": MAP, "KEY": WEB3FORMS_KEY, "FX": FORM_X[lang]})
        elif sub == "about/":
            inner = AU.body(i, up, t, {k: href(lang, sub, lang, k) for k, _ in AU.GO})
        elif sub == "study/":
            inner = STD.body(i, up, [(v_[:4], v_[4]) for v_ in TT_SUBJ.values()])
        elif sub == "news/":
            inner = NW.body(i, up, TG)
        elif sub == CAL.SUB:
            inner = CAL.body(lang, lambda k: href(lang, sub, lang, k), up)
        elif sub == CLB.JSUB:
            inner = CLB.join_body(i, up, lambda k: href(lang, sub, lang, k), list(TT["classes"]), {"EMAIL": EMAIL, "TG": "https://t.me/mr_successor"})
        elif sub == CLB.SUB:
            inner = CLB.body(i, up, lambda k: href(lang, sub, lang, k))
        elif sub == POL.SUB:
            inner = POL.body(i, up, lambda k: href(lang, sub, lang, k), lambda nm: href(lang, sub, lang, f"leadership/{LP.slug(nm)}/"))
        elif sub == CSL.SUB:
            _h = lambda k: href(lang, sub, lang, k)
            _tools = [(_h("abroad/plan/"), AB.PL.TITLE[i]), (_h("abroad/calendar/"), AB.DLN.NAME[i]), (_h("abroad/checklist/"), AB.CKL.NAME[i]), (_h("abroad/scholarships/"), AB.SUBNAME["abroad/scholarships/"][i]),
                      (_h("ielts/"), IE.NAME[i]), (_h("abroad/sat/"), AB.SAT.NAME[i]), (_h("abroad/essay/"), AB.ESS.NAME[i]), (_h("abroad/commonapp/"), AB.AP.NAME["abroad/commonapp/"][i]),
                      (_h("abroad/ucas/"), AB.AP.NAME["abroad/ucas/"][i]), (_h("abroad/calculator/"), AB.CAL.NAME[i])]
            inner = CSL.body(i, up, _h, {"PHONE": PHONE, "PHONE_TXT": PHONE_TXT, "EMAIL": EMAIL, "TG": "https://t.me/mr_successor", "PROFILE": "leadership/alimbek-jumamuratov/"}, _tools)
        elif sub == SUP.SUB:
            inner = SUP.body(i, up, lambda k: href(lang, sub, lang, k), {"PHONE": PHONE, "PHONE_TXT": PHONE_TXT, "EMAIL": EMAIL, "TG": TG})
        elif sub == INTL.SUB:
            inner = INTL.body(i, up, lambda k: href(lang, sub, lang, k), EMAIL)
        elif sub == GAL.SUB:
            inner = GAL.body(lang, lambda k: href(lang, sub, lang, k), up, lambda c: gal_who(c, lang))
        elif sub == "partners/":
            inner = PT.body(i, up, {"EMAIL": EMAIL, "TG": "https://t.me/mr_successor", "PHONE": PHONE, "PHONE_TXT": PHONE_TXT, "SUP_HREF": href(lang, sub, lang, SUP.SUB)})
        elif sub == "teachers/":
            inner = f'{teach_tabs(sub, lang, lambda k: href(lang, sub, lang, k))}{staff_strip(lang)}<p>{t["teach_p"].format(n=len(TEACHERS))}</p>{teacher_cards(lang, up)}'
        elif sub == "teachers/by-class/":
            inner = f'{teach_tabs(sub, lang, lambda k: href(lang, sub, lang, k))}{by_class(lang, up)}'
        elif sub == SEM.SUB:
            _h = lambda k: href(lang, sub, lang, k)
            inner = f'{teach_tabs(sub, lang, _h)}{SEM.body(lang, _h, TP.sub_of, LP.sub_of)}'
        elif sub == "teachers/class-teachers/":
            inner = f'{teach_tabs(sub, lang, lambda k: href(lang, sub, lang, k))}{heads_html(lang, "../")}'
        else:
            inner = f'<div class="grid">{"".join(person_card(*x, lang) for x in LEADERS)}</div>'
        mid = (f'<a href="{href(lang, sub, lang, CLB.SUB)}">{CLB.NAME[i]}</a> <span aria-hidden="true">›</span> ' if sub == CLB.JSUB else f'<a href="{href(lang, sub, lang, "achievements/")}">{ACH.NAME["achievements/"][i]}</a> <span aria-hidden="true">›</span> ' if sub in ACH.SUBS[1:] else f'<a href="{href(lang, sub, lang, "canteen/")}">{CN.NAME[i]}</a> <span aria-hidden="true">›</span> ' if sub in CN.SUBS[1:] else RS.crumbs(sub, i, lambda k: href(lang, sub, lang, k)) if sub in RS.SUBS[1:] else f'<a href="{href(lang, sub, lang, "teachers/")}">{t["teach_h"]}</a> <span aria-hidden="true">›</span> ' if sub in TP.SUB or sub in ("teachers/class-teachers/", "teachers/by-class/", SEM.SUB) else f'<a href="{href(lang, sub, lang, "leadership/")}">{t["lead_h"]}</a> <span aria-hidden="true">›</span> ' if sub in LP.SUB else f'<a href="{href(lang, sub, lang, "documents/")}">{EX.NAME["documents/"][i]}</a> <span aria-hidden="true">›</span> ' if sub.startswith("documents/") and sub != "documents/" else "")
        body = (f'<section class="pagehead"><div class="wrap"><nav class="crumbs" aria-label="breadcrumb"><a href="{home}">{TL["home"][i]}</a> <span aria-hidden="true">›</span> {mid}<span>{name}</span></nav>'
                f'<h1>{name}</h1></div></section><div class="orn"></div>'
                f'<section class="band" id="{sub.strip("/")}"><div class="wrap">{inner}</div></section>')
    body = body.replace("{UP}", up)
    ldjs = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False, indent=1)}</script>' for x in ld)
    return f"""<!DOCTYPE html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{t['keywords']}">
<meta name="google-site-verification" content="_ZceBwu3dQ0Ez7WnYUB7kfIozHncBke8m_cyXPJIzLg" />
<link rel="canonical" href="{url}">
{alts}
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:locale" content="{t['og_locale']}">
<meta property="og:site_name" content="{t['brand']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}{og_img(sub)}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0b5f78">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="48x48" href="{up}favicon-48.png">
<link rel="icon" type="image/png" sizes="96x96" href="{up}favicon-96.png">
<link rel="icon" type="image/png" href="{up}logo.png">
<link rel="apple-touch-icon" href="{up}logo-512.png">
<link rel="manifest" href="{up}{path(lang)}manifest.webmanifest">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Kegeyli QM">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700&family=Inter:wght@400;600&display=swap&subset=cyrillic,latin-ext" rel="stylesheet">
{ldjs}
<script>try{{var m=localStorage.getItem("theme");if(m)document.documentElement.dataset.theme=m}}catch(e){{}}</script>
<link rel="stylesheet" href="{up}{CSS_FILE}">
</head>
<body>
<header class="top">
  <div class="bar">
    <a class="brand" href="{home}" aria-label="{t['brand']}">
      <img src="{up}logo.png" width="36" height="36" alt="">
      <span>{t['brand']}</span>
    </a>
    <nav class="langs" aria-label="{t['lang_label']}">{langs}<button type="button" id="themebtn" class="tbtn" aria-label="Theme"><svg class="ti-moon" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.800A9 9 0 1 1 11.200 3a7 7 0 0 0 9.800 9.800z"/></svg><svg class="ti-sun" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.900 4.900l1.400 1.400M17.700 17.700l1.400 1.400M2 12h2M20 12h2M4.900 19.100l1.400-1.400M17.700 6.300l1.400-1.400"/></svg></button></nav>
    <nav class="menu" aria-label="{t['menu_label']}"><ul>{nav}</ul></nav>
    <script>(function(){{var bs=document.querySelectorAll('.ngb');function close(x){{bs.forEach(function(b){{if(b!==x){{b.setAttribute('aria-expanded','false');b.nextElementSibling.hidden=true}}}})}}
    bs.forEach(function(b){{b.addEventListener('click',function(e){{e.stopPropagation();var o=b.getAttribute('aria-expanded')==='true';close(b);b.setAttribute('aria-expanded',!o);b.nextElementSibling.hidden=o}})}});
    document.addEventListener('click',function(e){{if(!e.target.closest('.ng'))close()}});document.addEventListener('keydown',function(e){{if(e.key==='Escape')close()}})}})();</script>
  </div>
</header>
<main>
{body}
</main>

{partners_html}
<div class="orn"></div>
<footer class="sf">
  <div class="wrap sfgrid">
    <div class="sfbrand">
      <a class="sflogo" href="{home}"><img src="{up}logo.png" width="48" height="48" alt=""><span><strong>{t['brand']}</strong><em>{FOOT[lang][5]}</em></span></a>
      <p>{FOOT[lang][0]}</p>
      <div class="sfsoc"><a href="{TG}" rel="noopener" aria-label="Telegram">{SOC['tg']}</a><a href="tel:{PHONE}" aria-label="{PHONE_TXT}">{SOC['ph']}</a><a href="mailto:{EMAIL}" aria-label="{EMAIL}">{SOC['ml']}</a></div>
    </div>
    <nav class="sfcol" aria-label="{FOOT[lang][1]}"><h4>{FOOT[lang][1]}</h4><ul>{foot_school}</ul></nav>
    <nav class="sfcol" aria-label="{FOOT[lang][2]}"><h4>{FOOT[lang][2]}</h4><ul>{foot_abroad}</ul></nav>
    <div class="sfcol sfcontact"><h4>{FOOT[lang][3]}</h4><ul>
      <li>{SOC['pin']}<span>{t['addr_full']}</span></li>
      <li>{SOC['ph']}<a href="tel:{PHONE}">{PHONE_TXT}</a></li>
      <li>{SOC['ml']}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>{SOC['clk']}<span>{t['hours']}</span></li>
    </ul></div>
  </div>
  <div class="sfbar"><div class="wrap"><span>© 2022–2026 {t['brand']}. {t['rights'].replace('© 2026 ','')}</span><span>{t['footer_dir']}</span><span>{FOOT[lang][6]}: Alimbek Jumamuratov</span><span class="gcv" id="gcv" hidden><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3.500-7 10-7 10 7 10 7-3.500 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg><span>{VIEWS_TXT[lang][0]}: <b id="gcp">…</b></span><span>{VIEWS_TXT[lang][1]}: <b id="gct">…</b></span></span><a href="#top" class="sftop">{FOOT[lang][4]} ↑</a></div></div>
</footer>

<script>
{{
  const q=document.getElementById('tq');
  if(q){{
    const cs=[...document.querySelectorAll('.tcard')],none=document.getElementById('tnone');let sub='all';
    const run=()=>{{const v=(q.value||'').trim().toLowerCase();let n=0;for(const c of cs){{const ok=(sub==='all'||c.dataset.s===sub)&&(!v||c.dataset.n.includes(v));c.hidden=!ok;if(ok)n++}}none.hidden=n>0}};
    document.querySelectorAll('.chip').forEach(b=>b.addEventListener('click',()=>{{document.querySelectorAll('.chip').forEach(x=>x.classList.toggle('on',x===b));sub=b.dataset.s;run()}}));
    q.addEventListener('input',run);
  }}

{TT_JS}
{HOME_JS}{BL.JS}
  const f=document.getElementById('f'),ok=document.getElementById('ok');
  if(f)f.addEventListener('submit',async e=>{{
    e.preventDefault();
    if(f.botcheck&&f.botcheck.checked)return;
    if(!f.n.value.trim()||!f.m.value.trim()){{ok.textContent={json.dumps(t['form'][5], ensure_ascii=False)};return}}
    const FX={json.dumps(FORM_X[lang], ensure_ascii=False)},KEY={json.dumps(WEB3FORMS_KEY)},btn=f.querySelector('button');
    if(!KEY){{
      const body=f.m.value.trim()+'\\n\\n'+f.n.value.trim()+(f.ph.value.trim()?'\\n'+f.ph.value.trim():'');
      ok.textContent=FX[3];
      location.href='mailto:{EMAIL}?subject='+encodeURIComponent('kegeyliqm.uz — '+f.n.value.trim())+'&body='+encodeURIComponent(body);
      return}}
    btn.disabled=true;ok.textContent=FX[0];
    try{{
      const r=await fetch('https://api.web3forms.com/submit',{{method:'POST',headers:{{'Content-Type':'application/json',Accept:'application/json'}},body:JSON.stringify({{access_key:KEY,subject:'kegeyliqm.uz — '+f.n.value.trim(),from_name:'kegeyliqm.uz',name:f.n.value.trim(),phone:f.ph.value.trim(),message:f.m.value.trim(),botcheck:''}})}});
      const j=await r.json();
      if(j.success){{ok.textContent=FX[1];f.reset()}}else{{ok.textContent=FX[2]}}
    }}catch(x){{ok.textContent=FX[2]}}
    btn.disabled=false;
  }});
}}
</script>
<script>(function(){{var b=document.getElementById("themebtn");if(!b)return;var r=document.documentElement;function cur(){{return r.dataset.theme||(matchMedia("(prefers-color-scheme:dark)").matches?"dark":"light")}}function sync(){{b.setAttribute("aria-pressed",cur()==="dark")}}sync();b.addEventListener("click",function(){{var n=cur()==="dark"?"light":"dark";r.dataset.theme=n;try{{localStorage.setItem("theme",n)}}catch(e){{}}sync()}})}})();</script>
<script>window.goatcounter={{path:function(p){{return p.replace(/^\\/(en|uz|ru)(\\/|$)/,"/")||"/"}}}};
(function(){{var C="{GOATCOUNTER}";if(!C)return;var p=location.pathname.replace(/index\\.html$/,"").replace(/^\\/(en|uz|ru)(\\/|$)/,"/")||"/";
function get(x,id){{return fetch("https://"+C+".goatcounter.com/counter/"+encodeURIComponent(x)+".json").then(function(r){{if(!r.ok)throw 0;return r.json()}}).then(function(j){{document.getElementById(id).textContent=j.count;return 1}})}}
if(!/^(localhost|127\\.)/.test(location.hostname))Promise.all([get(p,"gcp").catch(function(){{document.getElementById("gcp").textContent="—";return 0}}),get("TOTAL","gct").catch(function(){{return 0}})]).then(function(r){{if(r[0]||r[1])document.getElementById("gcv").hidden=false}})}})();</script>
<script data-goatcounter="https://{GOATCOUNTER}.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
"""

def home_body(lang, t, i, up):
    _mx = max(sum(1 for x in TEACHERS if x[1] == k) for k in SUBJECTS)
    subj_tags = "".join(
        f'<li class="subc" style="--mc:{SUBJ_VIS[k][1]};--w:{max(8, round(100*sum(1 for x in TEACHERS if x[1] == k)/_mx))}%"><span class="mi">{_I(SUBJ_VIS[k][0])}</span><span class="sn">{v[lang]}</span><b>{sum(1 for x in TEACHERS if x[1] == k)}</b><i class="sbar"></i></li>'
        for k, v in SUBJECTS.items() if any(x[1] == k for x in TEACHERS))
    _hi = sum(1 for x in TEACHERS if x[2] == "high"); _ns = len({x[1] for x in TEACHERS})
    teach_stats = (f'<div class="tstats"><div><b>{len(TEACHERS)}</b><span>{TSTAT[lang][0]}</span></div><div><b>{_ns}</b><span>{TSTAT[lang][1]}</span></div><div><b>{_hi}</b><span>{CATS["high"][lang]}</span></div></div>')
    high = sum(1 for x in TEACHERS if x[2] == "high")
    _RI = [(_I('<path d="M12 4l9 4-9 4-9-4z"/><path d="M7 10.500v4.500c0 1.400 2.200 3 5 3s5-1.600 5-3v-4.500M21 8v6"/>'), "#e8b94a"), (_I('<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>'), "#7dd3a8"), (_I('<rect x="4" y="3.500" width="16" height="14" rx="2"/><path d="M8 8h8M8 11.500h5"/><circle cx="16" cy="18" r="3"/><path d="M14.500 20.500L14 23l2-1 2 1-.5-2.500"/>'), "#f0a07a"),
           (_I('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'), "#8cc8f0"), (_I('<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.500 2.700-6 6-6s6 2.500 6 6M16 5.500a3 3 0 0 1 0 5.500M18 14.500c2 .8 3 2.800 3 5.500"/>'), "#c4a6f5"), (_I('<circle cx="12" cy="9" r="5.500"/><path d="M8.500 13.500L7 21l5-3 5 3-1.500-7.500"/>'), "#e0a15a")]
    def _rs(k, n, l):
        m = _re.match(r"^(\d+(?:[.,]\d+)?)%$", n)
        ring = ""
        if m:
            p = float(m.group(1).replace(",", "."))
            ring = f'<svg class="rsring" viewBox="0 0 44 44"><circle cx="22" cy="22" r="18" class="rb"/><circle cx="22" cy="22" r="18" class="rf" stroke-dasharray="{p*1.131:.1f} 113.1" transform="rotate(-90 22 22)"/></svg>'
        ic, col = _RI[k % len(_RI)]
        return f'<div class="stat rsc" style="--rc:{col}"><span class="rsi">{ic}</span><div class="rsn"><b>{n}</b>{ring}</div><span class="rsl">{l}</span></div>'
    stats = "".join(_rs(k, n, l) for k, (n, l) in enumerate(t["results"]))
    _fk = ["pin", "focus", "meal", "clock", "cal"]
    facts = "".join(f"<li>{fi(_fk[n] if n < len(_fk) else 'cal')}<b>{k}</b><span>{v}</span></li>" for n, (k, v) in enumerate(t["facts"]))
    _SC = [(_I('<path d="M5 8h6M8 5v6M14 5.500l5 5M19 5.500l-5 5M5 18h6M14 18h5M16.500 15.500v5"/>'), "#2a7fd1", None), (_I('<path d="M4 5h16v11H9l-4 4v-4H4z"/><path d="M8 9h8M8 12h5"/>'), "#7c3aed", "ielts/"),
           (_I('<circle cx="12" cy="12" r="1.800"/><ellipse cx="12" cy="12" rx="9" ry="3.800"/><ellipse cx="12" cy="12" rx="9" ry="3.800" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="9" ry="3.800" transform="rotate(120 12 12)"/>'), "#0b7a8f", None),
           (_I('<path d="M12 21s-6-5.600-6-10.500a6 6 0 0 1 12 0C18 15.400 12 21 12 21z"/><circle cx="12" cy="10.500" r="2.200"/>'), "#d97706", "abroad/")]
    cards = "".join(
        f'<{"a href=%s" % chr(34) + _SC[k][2] + chr(34) if _SC[k][2] else "div"} class="card sjc" style="--mc:{_SC[k][1]}"><span class="sji">{_SC[k][0]}</span><h3>{h}</h3><p>{p}</p>'
        + (f'<span class="sjgo">→</span></a>' if _SC[k][2] else '</div>')
        for k, (h, p) in enumerate(t["cards"]))
    links = {"mygov": '<a href="https://my.gov.uz" rel="noopener">my.gov.uz</a>',
             "ariza": '<a href="https://ariza.piima.uz" rel="noopener">ariza.piima.uz</a>'}
    steps = "".join(f"<li><div><h3>{h}</h3><p>{p.format(**links)}</p></div></li>" for h, p in t["steps"])
    docs = "".join(f"<li>{d}</li>" for d in t["docs"])
    news = "".join(f'<article class="card"><time datetime="{dt}">{d}</time><h3>{h}</h3><p>{p}</p></article>'
                   for dt, d, h, p in t["news"])
    gallery = GAL.teaser(lang, up, href(lang, "", lang, GAL.SUB))
    if PHOTOS:
        figs = "".join(f'<figure><img src="{up}photos/{f}" alt="{cap.get(lang, "")}" loading="lazy"><figcaption>{cap.get(lang, "")}</figcaption></figure>' for f, cap in PHOTOS)
        gallery = f'<section id="gallery" class="band"><div class="wrap"><h2>{t["gallery_h"]}</h2><div class="gal">{figs}</div></div></section>'
    faqs = EX.faq_html(t)
    c = t["contact_labels"]
    return f"""<section class="hero hero2" aria-labelledby="t">
  <div class="hpic"><img src="{up}photos/school.jpg" alt="{t['brand']}" width="1206" height="1180" fetchpriority="high"></div>
  <div class="htxt">
    <p class="hkick">{HKICK[lang]}</p>
    <h1 id="t">{t['brand']}</h1>
    <p class="lead">{t['lead']}</p>
    <div class="hbtns">
      <a class="hb1 t-adm" href="admission/">{NAV_ICON['admission'][0]}{t['btn_adm']}</a>
      <a class="hb1 alt t-tt" href="timetable/">{NAV_ICON['timetable'][0]}{TT_TXT['title'][i]}</a>
      <a class="hb2 t-ab" href="abroad/">{NAV_ICON['abroad'][0]}{AB.NAME[i]}</a>
      <a class="hb2 t-ct" href="#contact">{NAV_ICON['contact'][0]}{t['btn_contact']}</a>
    </div>
  </div>
</section>

<section id="about" class="band hab">
  <div class="wrap two">
    <div>
      <span class="kick">{fi('cal')}{FOOT[lang][5]}</span>
      <h2>{t['nav'][0]}</h2>
      <p class="hlead">{t['about1']}</p>
      <div class="hnote"><span class="mi" style="--mc:#d97706">{FACT_ICON['meal'][0]}</span><p>{t['about2']}</p></div>
      <p><a class="btn s" href="about/">{AU.NAME[i]} →</a></p>
    </div>
    <ul class="facts tiles">{facts}</ul>
  </div>
</section>

<section id="subjects" class="band alt">
  <div class="wrap">
    <h2>{t['nav'][1]}</h2>
    <p>{t['subj_p']}</p>
    <div class="grid">{cards}</div>
  </div>
</section>

<section id="results" class="band results">
  <div class="wrap">
    <h2>{t['results_h']}</h2>
    <div class="stats">{stats}</div>
    <p class="note">{t['results_note']}</p>
    <p class="btns" style="margin-top:18px"><a class="btn p" href="achievements/">{ACH.NAME['achievements/'][i]} →</a><a class="btn s" href="graduates/">{GT['more'][i]} →</a></p>
  </div>
</section>

<section id="teachers" class="band alt">
  <div class="wrap">
    <h2>{t['teach_h']}</h2>
    <p>{t['teach_p'].format(n=len(TEACHERS))}</p>
    {teach_stats}
    <ul class="subgrid">{subj_tags}</ul>
    <p style="margin-top:20px"><a class="btn p" href="teachers/">{TL['all_teachers'][i]} ({len(TEACHERS)}) →</a></p>
  </div>
</section>

<section id="admission" class="band">
  <div class="wrap">
    <h2>{t['nav'][2]}</h2>
    <p>{t['adm_p']}</p>
    <div class="astrip">{"".join(f'<div class="astat"><b>{a}</b><span>{b}</span></div>' for a, b in EX.AX["strip"][i])}</div>
    <div class="btns"><a class="btn p" href="admission/">{t['btn_adm']} →</a><a class="btn s" href="https://ariza.piima.uz" rel="noopener">{EX.X["a_apply"][i]}</a></div>
  </div>
</section>

<section id="news" class="band alt news">
  <div class="wrap">
    <h2>{t['nav'][3]}</h2>
    <div class="ngrid">{NW.cards(i, 3, up)}</div>
    <p class="btns" style="margin-top:20px"><a class="btn p" href="news/">{NW.ALL[i]} →</a><a class="btn s" href="{TG}" rel="noopener">{t['news_btn']}</a></p>
  </div>
</section>

{gallery}
<section id="faq" class="band">
  <div class="wrap" style="max-width:820px">
    <h2>{t['faq_h']}</h2>
    {faqs}
  </div>
</section>

<section id="contact" class="band alt">
  <div class="wrap two">
    <div>
      <h2>{t['nav'][5]}</h2>
      <ul class="facts">
        <li>{fi('pin')}<b>{c[0]}</b><span>{t['addr_full']}</span></li>
        <li>{fi('phone')}<b>{c[1]}</b><span><a href="tel:{PHONE}">{PHONE_TXT}</a></span></li>
        <li>{fi('mail')}<b>{c[2]}</b><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></li>
        <li>{fi('tg')}<b>{c[3]}</b><span><a href="{TG}" rel="noopener">@Kegeyliqanigelestirilgenmektebi</a></span></li>
        <li>{fi('clock')}<b>{c[4]}</b><span>{t['hours']}</span></li>
        <li>{fi('map')}<b>{c[5]}</b><span><a href="{MAP}" rel="noopener">{t['map']}</a></span></li>
      </ul>
    </div>
    <form id="f" class="card" novalidate>
      <h3>{t['form'][0]}</h3>
      <label for="n">{t['form'][1]}</label><input id="n" name="n" autocomplete="name" required>
      <label for="ph">{t['form'][2]}</label><input id="ph" name="ph" type="tel" autocomplete="tel">
      <label for="m">{t['form'][3]}</label><textarea id="m" name="m" rows="4" required></textarea>
      <input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off" style="display:none" aria-hidden="true">
      <button type="submit">{t['form'][4]}</button>
      <p id="ok" role="status"></p>
    </form>
  </div>
  <div class="wrap map"><iframe title="{t['map_title']}" src="https://maps.google.com/maps?q={LAT},{LNG}&amp;z=17&amp;hl={ {'kaa':'uz'}.get(t['html_lang'],t['html_lang']) }&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</section>"""

def sitemap():
    rows = []
    for sub in PAGES:
        for l in ORDER:
            alts = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{a}" href="{DOMAIN + path(a) + sub}"/>' for a in ORDER)
            rows.append(f"  <url>\n    <loc>{DOMAIN + path(l) + sub}</loc>{alts}\n    <lastmod>{_dt.date.today().isoformat()}</lastmod>\n  </url>")
    rows.append(f"  <url>\n    <loc>{DOMAIN}school-profile/</loc>\n    <lastmod>{_dt.date.today().isoformat()}</lastmod>\n  </url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")

for l in ORDER:
    for sub in PAGES:
        out = os.path.join(ROOT, path(l), sub, "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(page(l, sub))
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(sitemap())
open(os.path.join(ROOT, CAL.ICS), "w", encoding="utf-8", newline="").write(CAL.ics())
import school_profile as SP
SP.build(ROOT, DOMAIN)
for l in ORDER:
    man = {"name": T[l]["brand"], "short_name": "Kegeyli QM", "lang": T[l]["html_lang"], "start_url": "timetable/", "scope": "/",
           "display": "standalone", "background_color": "#ffffff", "theme_color": "#0b5f78",
           "icons": [{"src": "/logo.png", "sizes": "192x192", "type": "image/png"}, {"src": "/logo-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}]}
    open(os.path.join(ROOT, path(l), "manifest.webmanifest"), "w", encoding="utf-8").write(json.dumps(man, ensure_ascii=False, indent=1))
json.dump(TT, open(os.path.join(ROOT, "timetable.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
for _f in os.listdir(ROOT):
    if _re.fullmatch(r"style\.[0-9a-f]{10}\.css", _f) and _f != CSS_FILE:
        os.remove(os.path.join(ROOT, _f))
open(os.path.join(ROOT, CSS_FILE), "w", encoding="utf-8").write(STYLE_MIN)
open(os.path.join(ROOT, "sw.js"), "w", encoding="utf-8").write(open(os.path.join(SRC, "sw.js"), encoding="utf-8").read())
print("built:", ", ".join(ORDER), "x", len(PAGES), "pages")
