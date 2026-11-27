# Leadership & staff profile pages: leadership/<slug>/ (4 languages). Built from teachers.LEADERS / LEADER_INFO / ROLES.
import html as _html, json, os, re
from teachers import LEADERS, LEADER_INFO, ROLES, TEACHERS, latin
import tprofile as TP
import director as DIR
import seminars as _SEM

LANGS = ["kaa", "en", "uz", "ru"]
def slug(la):
    return re.sub(r"[^a-z0-9]+", "-", la.lower()).strip("-")
SUB = {f"leadership/{slug(l[0])}/": n for n, l in enumerate(LEADERS)}
def sub_of(n):
    return f"leadership/{slug(LEADERS[n][0])}/"
FULL = {"Feruza Nizamatdinova": ("Feruza Nizamatdinova Usnatdinovna", "Феруза Низаматдинова Уснатдиновна")}
def full(la, cy, lang):
    f = FULL.get(la)
    return (f[1] if lang == "ru" else f[0]) if f else (cy if lang == "ru" else la)
def name(n, lang):
    la, cy, r = LEADERS[n]
    return full(la, cy, lang)
def teacher_of(n):
    """index in TEACHERS if this person also teaches"""
    la = LEADERS[n][0]; f, s = la.split()[0], la.split()[-1]
    m = [j for j, t in enumerate(TEACHERS) if latin(t[0]).split()[0] == s and latin(t[0]).split()[1] == f]
    return m[0] if m else None

ROLECOL = {"director": "#a3202c", "dep_edu": "#0b5f78", "dep_spirit": "#7c3aed", "dep_econ": "#b45309", "adviser": "#2a7fd1",
           "psych": "#2f8f5b", "cqt_head": "#5b6472", "librarian": "#d97706", "accountant": "#0b7a8f", "hr": "#b23a48"}
GROUP = {"director": 0, "dep_edu": 1, "dep_spirit": 1, "dep_econ": 1}
# What each role is responsible for (general description of the position) and when to contact them.
DUTY = {
 "director": [("Mekteptiń ulıwma basqarıwı hám rawajlanıw strategiyası", "Overall management and development of the school", "Maktabni umumiy boshqarish va rivojlantirish strategiyasi", "Общее руководство и стратегия развития школы"),
              ("Qabıllaw, xızmetkerler hám hamkorlıq máseleleri", "Admission, staff and partnership decisions", "Qabul, xodimlar va hamkorlik masalalari", "Приём, кадры и партнёрства"),
              ("Ata-analar hám mámleketlik shólkemler menen baylanıs", "Relations with parents and government bodies", "Ota-onalar va davlat tashkilotlari bilan aloqa", "Связь с родителями и госорганами")],
 "dep_edu": [("Oqıw procesi hám sabaq kestesi", "Teaching process and the timetable", "O‘quv jarayoni va dars jadvali", "Учебный процесс и расписание"),
             ("Bahalaw, CHSB testleri hám olimpiadalar", "Assessment, CHSB tests and olympiads", "Baholash, CHSB testlari va olimpiadalar", "Оценивание, тесты CHSB и олимпиады"),
             ("Muǵallimlerdiń metodikalıq jumısı", "Teachers’ methodological work", "O‘qituvchilarning metodik ishi", "Методическая работа учителей")],
 "dep_spirit": [("Tárbiya hám ruwxıy-aǵartıwshılıq ilajlar", "Upbringing and educational events", "Tarbiya va ma’naviy-ma’rifiy tadbirlar", "Воспитательная работа и мероприятия"),
                ("Oqıwshılardıń bos waqtı, dógerekler hám bayramlar", "Clubs, celebrations and students’ free time", "To‘garaklar, bayramlar va o‘quvchilar bo‘sh vaqti", "Кружки, праздники и досуг учеников"),
                ("Ata-analar menen tárbiyalıq jumıs", "Working with parents on student behaviour", "Ota-onalar bilan tarbiyaviy ish", "Работа с родителями по воспитанию")],
 "dep_econ": [("Mektep imaratı, klasslar hám úskeneler", "School building, classrooms and equipment", "Maktab binosi, sinflar va jihozlar", "Здание, классы и оборудование"),
              ("Asxana, tazalıq hám qáwipsizlik", "Canteen, cleanliness and safety", "Oshxona, tozalik va xavfsizlik", "Столовая, чистота и безопасность"),
              ("Xojalıq támiynatı hám remont jumısları", "Supplies and repairs", "Xo‘jalik ta’minoti va ta’mirlash", "Снабжение и ремонт")],
 "adviser": [("Shet elde hám Ózbekstanda oqıwǵa túsiw boyınsha másláhát", "Guidance on university admission abroad and in Uzbekistan", "Xorijda va O‘zbekistonda o‘qishga kirish bo‘yicha maslahat", "Консультации по поступлению за рубежом и в Узбекистане"),
             ("IELTS, SAT hám grantlarǵa tayarlıq", "IELTS, SAT and scholarship preparation", "IELTS, SAT va grantlarga tayyorgarlik", "Подготовка к IELTS, SAT и грантам"),
             ("Kásip tańlaw hám xalıqaralıq hamkorlıq", "Career guidance and international partnerships", "Kasb tanlash va xalqaro hamkorlik", "Профориентация и международное сотрудничество")],
 "psych": [("Oqıwshılardıń psixologiyalıq jaǵdayı hám qollap-quwatlaw", "Students’ wellbeing and psychological support", "O‘quvchilarning psixologik holati va qo‘llab-quvvatlash", "Психологическое благополучие и поддержка учеников"),
           ("Imtihanlar aldınan stress penen islesiw", "Help with exam stress", "Imtihon oldidan stress bilan ishlash", "Помощь со стрессом перед экзаменами"),
           ("Ata-analar ushın jeke másláhátler", "Private consultations for parents", "Ota-onalar uchun shaxsiy maslahatlar", "Личные консультации для родителей")],
 "cqt_head": [("Shaqırıwǵa shekemgi baslanǵısh tayarlıq sabaqları", "Pre-conscription training lessons", "Chaqiruvga qadar boshlang‘ich tayyorgarlik darslari", "Уроки допризывной подготовки"),
              ("Puqaralıq qorǵanıw hám qáwipsizlik", "Civil defence and safety drills", "Fuqaro muhofazasi va xavfsizlik", "Гражданская оборона и безопасность"),
              ("Watanparwarlıq tárbiyası", "Patriotic education", "Vatanparvarlik tarbiyasi", "Патриотическое воспитание")],
 "librarian": [("Mektep kitapxanası hám sabaqlıqlar", "School library and textbooks", "Maktab kutubxonasi va darsliklar", "Школьная библиотека и учебники"),
               ("Kitap oqıw ilajları", "Reading events", "Kitobxonlik tadbirlari", "Читательские мероприятия"),
               ("Elektron resurslar", "Digital resources", "Elektron resurslar", "Электронные ресурсы")],
 "accountant": [("Mekteptiń qarjı esabı", "School finances and accounting", "Maktabning moliyaviy hisobi", "Финансовый учёт школы"),
                ("Is haqı hám tólemler", "Salaries and payments", "Ish haqi va to‘lovlar", "Зарплаты и платежи")],
 "hr": [("Xızmetkerlerdi jumısqa qabıllaw hám hújjetler", "Hiring and staff documents", "Xodimlarni ishga qabul qilish va hujjatlar", "Приём на работу и кадровые документы"),
        ("Malaka asırıw hám attestaciya", "Training and certification of staff", "Malaka oshirish va attestatsiya", "Повышение квалификации и аттестация"),
        ("Bos jumıs orınları", "Job vacancies", "Bo‘sh ish o‘rinlari", "Вакансии")],
}
X = {
 "back": ("Basshılıq hám xızmetkerler", "Leadership and staff", "Rahbariyat va xodimlar", "Руководство и сотрудники"),
 "duty_h": ("Juwapkershiligi", "Responsibilities", "Mas’uliyati", "Обязанности"),
 "about_h": ("Maǵlıwmat", "About", "Ma’lumot", "Сведения"),
 "contact_h": ("Baylanıs", "Contact", "Bog‘lanish", "Связаться"),
 "contact_p": ("Mektep arqalı baylanısıń: telefon yamasa Telegram. Jeke másláhát ushın aldın ala waqıt belgileń.",
               "Contact through the school by phone or Telegram. For a personal meeting, please book a time in advance.",
               "Maktab orqali bog‘laning: telefon yoki Telegram. Shaxsiy uchrashuv uchun oldindan vaqt belgilang.",
               "Свяжитесь через школу по телефону или в Telegram. Для личной встречи договоритесь о времени заранее."),
 "call": ("Qońıraw etiw", "Call the school", "Qo‘ng‘iroq qilish", "Позвонить"),
 "teaches": ("Muǵallim sıpatında da sabaq beredi", "Also teaches", "O‘qituvchi sifatida ham dars beradi", "Также преподаёт"),
 "tprof": ("Muǵallim profilin ashıw", "Open teacher profile", "O‘qituvchi profilini ochish", "Открыть профиль учителя"),
 "team_h": ("Komanda", "The team", "Jamoa", "Команда"),
 "share": ("Bólisiw", "Share", "Ulashish", "Поделиться"),
 "copied": ("Silteme kóshirildi", "Link copied", "Havola nusxalandi", "Ссылка скопирована"),
 "open": ("Profil", "Profile", "Profil", "Профиль"),
 "desc": ("{n} — {r}, Kegeyli rayonı qánigelestirilgen mektebi.", "{n}, {r} at Kegeyli District Specialized School.",
          "{n} — {r}, Kegeyli tumani ixtisoslashtirilgan maktabi.", "{n} — {r}, Кегейлийская районная специализированная школа."),
}
def _svg(p, s=22, w=2):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
I_OK = '<path d="M5 12l5 5L20 7"/>'
I_INFO = '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.500h.01"/>'
I_PHONE = '<path d="M5 4h4l2 5-2.500 1.500a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>'
I_TG = '<path d="M21 4L3 11l6 2 2 6 3-4 5 4z"/><path d="M9 13l8-6"/>'
I_SHARE = '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.600 13.500l6.800 4M15.400 6.500l-6.800 4"/>'
I_BOOK = '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 21V5M9 7h6"/>'

def body(sub, lang, up, href, ctx):
    i = LANGS.index(lang); esc = _html.escape; n = SUB[sub]
    la, cy, r = LEADERS[n]; nm = name(n, lang); col = ROLECOL.get(r, "#0b7a8f")
    ph = slug(la); photo = os.path.exists(os.path.join(ctx["ROOT"], "photos", "leaders", ph + ".jpg"))
    ini = "".join(w[0] for w in nm.split()[:2])
    av = f'<img src="{up}photos/leaders/{ph}.jpg" alt="{esc(nm)}">' if photo else f'<span>{ini}</span>'
    share = (f'<div class="tpshare"><button type="button" class="btn s" id="tpsh">{_svg(I_SHARE, 18)} {X["share"][i]}</button>'
             f'<a class="btn s" id="tptg" href="#" rel="noopener">{_svg(I_TG, 18)} Telegram</a><span id="tpok" role="status"></span></div>')
    hero = (f'<p class="rsback"><a href="{href("leadership/")}">← {X["back"][i]}</a></p>'
            f'<div class="tphero" style="--ac:{col}"><div class="tpav">{av}</div><div class="tpht"><h2>{esc(nm)}</h2>'
            f'<div class="tpchips"><span class="tpchip lead">{ROLES[r][lang]}</span></div>{share}</div></div>')
    full = ""
    if os.path.exists(os.path.join(ctx["ROOT"], "photos", "leaders", ph + "-full.jpg")):
        full = (f'<figure class="lpfull"><img src="{up}photos/leaders/{ph}-full.jpg" alt="{esc(nm)} — {ROLES[r][lang]}" width="1400" height="1050" loading="lazy">'
                f'<figcaption><b>{esc(nm)}</b><span>{ROLES[r][lang]}</span></figcaption></figure>')
    duties = "".join(f'<li><span>{_svg(I_OK, 16, 3)}</span>{d[i]}</li>' for d in DUTY.get(r, []))
    info = LEADER_INFO.get(la, [])
    about = ""
    if info:
        about = f'<div class="card lpabout"><h3>{_svg(I_INFO, 20)} {X["about_h"][i]}</h3><ul>' + "".join(f'<li>{esc(l[i])}</li>' for l in info) + '</ul></div>'
    tj = teacher_of(n)
    tlink = ""
    if tj is not None:
        tlink = (f'<a class="card lpteach" href="{href(TP.sub_of(tj))}"><span>{_svg(I_BOOK, 22)}</span><div><b>{X["teaches"][i]}</b>'
                 f'<small>{X["tprof"][i]} →</small></div></a>')
    contact = (f'<div class="card lpcontact"><h3>{_svg(I_PHONE, 20)} {X["contact_h"][i]}</h3><p>{X["contact_p"][i]}</p>'
               f'<div class="btns"><a class="btn p" href="tel:{ctx["PHONE"]}">{_svg(I_PHONE, 18)} {ctx["PHONE_TXT"]}</a><a class="btn s" href="{ctx["TG"]}" rel="noopener">Telegram</a></div></div>')
    duty = f'<div class="card lpduty" style="--ac:{col}"><h3>{X["duty_h"][i]}</h3><ul>{duties}</ul></div>' if duties else ""
    team = "".join(f'<a href="{href(sub_of(k))}" style="--ac:{ROLECOL.get(l[2], "#0b7a8f")}"><span>{"".join(w[0] for w in name(k, lang).split()[:2])}</span><div><b>{esc(name(k, lang))}</b><small>{ROLES[l[2]][lang]}</small></div></a>'
                   for k, l in enumerate(LEADERS) if k != n)
    js = ("<script>(function(){var u=location.href,t=document.title,ok=document.getElementById('tpok');"
          "document.getElementById('tptg').href='https://t.me/share/url?url='+encodeURIComponent(u)+'&text='+encodeURIComponent(t);"
          "document.getElementById('tpsh').addEventListener('click',function(){if(navigator.share){navigator.share({title:t,url:u}).catch(function(){})}"
          "else if(navigator.clipboard){navigator.clipboard.writeText(u).then(function(){ok.textContent=" + json.dumps(X["copied"][i]) + "})}})})();</script>")
    D = DIR.sections(i, href, dict(ctx, name=esc(nm))) if r == "director" else dict(top="", mid="", side="", bottom="")
    return (f'{hero}{full}{D["top"]}<div class="actwo">{duty}<div class="lpside">{about}{tlink}{D["side"]}{contact}</div></div>{D["mid"]}{D["bottom"]}'
            + _SEM.for_person("lead:" + LEADERS[n][0], lang, href, TP.sub_of, sub_of) +
            f'<h2>{X["team_h"][i]}</h2><div class="lpteam">{team}</div>{js}')

def desc(n):
    la, cy, r = LEADERS[n]
    return tuple(X["desc"][k].format(n=name(n, l), r=ROLES[r][l]) for k, l in enumerate(LANGS))
