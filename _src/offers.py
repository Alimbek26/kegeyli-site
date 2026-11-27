# University offers abroad: admission offers our students received from foreign universities,
# plus international programmes they took part in. An offer counts even if the student chose to study elsewhere.
# To add an offer: copy one dict in OFFERS. Names only with the student's permission.
#   student: name in 4 languages; cls: class at the time; grad: graduating year
#   uni: university name (as the university writes it); country: key in COUNTRY; city: city/state (English)
#   prog: programme in 4 languages or None; term: e.g. "2025-fall" or None; grant: amount in USD as stated in the offer, or None
#   date: "YYYY-MM-DD" / "YYYY-MM" / "YYYY" (when the offer came); news: True if there is a news post
import html as _html

SUB = "achievements/offers/"
NAME = ("Shet el universitetleri", "Offers from abroad", "Xorijiy universitetlar", "Зарубежные университеты")
DESC = ("Oqıwshılarımız qabıl etilgen shet el universitetleri: universitet, mámleket, baǵdar hám grantlar.",
        "Universities abroad that admitted our students: university, country, programme and grants.",
        "O‘quvchilarimiz qabul qilingan xorijiy universitetlar: universitet, davlat, yo‘nalish va grantlar.",
        "Зарубежные университеты, принявшие наших учеников: университет, страна, направление и гранты.")
ICON = ('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.800 5.700 3.800 9s-1.300 6.300-3.800 9c-2.500-2.700-3.800-5.700-3.800-9S9.500 5.700 12 3z"/>', "#2563eb")

COUNTRY = {
 "us": ("🇺🇸", ("AQSh", "USA", "AQSh", "США")),
 "uk": ("🇬🇧", ("Ullı Britaniya", "United Kingdom", "Buyuk Britaniya", "Великобритания")),
}
_XH = ("Húrshida Ismailova", "Húrshida Ismailova", "Xurshida Ismailova", "Хуршида Исмайлова")
OFFERS = [
 dict(student=_XH, cls="11-A", grad="2024/2025", uni="Colorado State University", country="us", city="Fort Collins, Colorado",
      prog=("Computer Science (kompyuter ilimleri)", "Computer Science", "Computer Science (kompyuter fanlari)", "Computer Science (компьютерные науки)"),
      term="2025-fall", grant=None, date="2025", news=True),
 dict(student=_XH, cls="11-A", grad="2024/2025", uni="Pennsylvania Western University", country="us", city="Pennsylvania",
      prog=None, term=None, grant=7000, date="2025-01-05", news=True),
]
OFFERS.append(
 dict(student=_XH, cls="11-A", grad="2024/2025", uni="University of Cincinnati — Clermont College", country="us", city="Batavia, Ohio",
      prog=("Computer Aided Design (sertifikat programması)", "Computer Aided Design (certificate programme)", "Computer Aided Design (sertifikat dasturi)", "Computer Aided Design (сертификатная программа)"),
      term="2025-fall", grant=None, date="2025", news=True,
      award=("Grant penen qabıl etildi", "Admitted with a grant", "Grant bilan qabul qilindi", "Принята с грантом")))
OFFERS.append(
 dict(student=_XH, cls="11-A", grad="2024/2025", uni="University of Minnesota Twin Cities", country="us", city="Minneapolis–Saint Paul, Minnesota",
      prog=("College of Science and Engineering (Ilim hám injeneriya kolledji)", "College of Science and Engineering", "College of Science and Engineering (Fan va muhandislik kolleji)", "College of Science and Engineering (Колледж науки и инженерии)"),
      term="2025-fall", grant=None, date="2025", news=True))
OFFERS.append(
 dict(student=_XH, cls="11-A", grad="2024/2025", uni="Iowa State University", country="us", city="Ames, Iowa",
      prog=None, term=None, grant=None, date="2025-01-21", news=True,
      award=("Grant penen qabıl etildi", "Admitted with a grant", "Grant bilan qabul qilindi", "Принята с грантом")))
OFFERS.append(
 dict(student=_XH, cls="11-A", grad="2024/2025", uni="Caldwell University", country="us", city="Caldwell, New Jersey",
      prog=("Computer Science (kompyuter ilimleri)", "Computer Science", "Computer Science (kompyuter fanlari)", "Computer Science (компьютерные науки)"),
      term="2025-fall", grant=None, date="2025-01-08", news=True,
      award=("Honors Program stipendiyasına ılayıq dep tabıldı", "Qualified for the Honors Program scholarship", "Honors Program stipendiyasiga loyiq deb topildi", "Получила право на стипендию Honors Program")))
OFFERS.append(
 dict(student=("Ayjamal Abdullaeva", "Ayjamal Abdullaeva", "Ayjamal Abdullayeva", "Айжамал Абдуллаева"), cls="11-A", grad="2024/2025",
      uni="Colorado State University", country="us", city="Fort Collins, Colorado",
      prog=("Economics (ekonomika)", "Economics", "Economics (iqtisodiyot)", "Economics (экономика)"),
      term="2025-fall", grant=None, date="2025-01-20", news=True))
OFFERS.append(
 dict(student=("Ayjamal Abdullaeva", "Ayjamal Abdullaeva", "Ayjamal Abdullayeva", "Айжамал Абдуллаева"), cls="11-A", grad="2024/2025",
      uni="University of Glasgow", country="uk", city="Glasgow, Scotland", news=True,
      rank="QS 2025: #78",
      via=("Glasgow International College (Kaplan) arqalı: 2 semestrlik foundation, keyin universitet", "Through Glasgow International College (Kaplan): a two-term foundation year, then the university",
           "Glasgow International College (Kaplan) orqali: 2 semestrlik foundation, so‘ng universitet", "Через Glasgow International College (Kaplan): подготовительный год (2 семестра), затем университет"),
      prog=("Foundation (Business and Social Sciences) → MA (Hons) Economics", "Foundation (Business and Social Sciences) → MA (Hons) Economics",
            "Foundation (Business and Social Sciences) → MA (Hons) Economics", "Foundation (Business and Social Sciences) → MA (Hons) Economics"),
      term="2025-fall", grant=None, date="2025-04-04",
      award=None, status=("Shártli usınıs", "Conditional offer", "Shartli taklif", "Условное предложение")))
OFFERS.append(
 dict(student=("Ayjamal Abdullaeva", "Ayjamal Abdullaeva", "Ayjamal Abdullayeva", "Айжамал Абдуллаева"), cls="11-A", grad="2024/2025",
      uni="University of Birmingham", country="uk", city="Birmingham, England", news=True,
      rank="QS 2025: #80",
      via=("University of Birmingham Foundation Pathways (Kaplan) arqalı: foundation jılı qosılǵan 4 jıllıq bakalavriat", "Through University of Birmingham Foundation Pathways (Kaplan): a four-year bachelor’s degree with an integrated foundation year",
           "University of Birmingham Foundation Pathways (Kaplan) orqali: foundation yili qo‘shilgan 4 yillik bakalavriat", "Через University of Birmingham Foundation Pathways (Kaplan): 4-летний бакалавриат с подготовительным годом"),
      prog=("BSc (Hons) Economics", "BSc (Hons) Economics", "BSc (Hons) Economics", "BSc (Hons) Economics"),
      term="2025-fall", grant=None, date="2025-04-04",
      award=None, status=("Shártli usınıs", "Conditional offer", "Shartli taklif", "Условное предложение")))
OFFERS.append(
 dict(student=("Aynura Turǵanbaeva", "Aynura Turganbaeva", "Aynura Turg‘anbayeva", "Айнура Турганбаева"), cls="11-A", grad="2024/2025",
      uni="University of Arizona", country="us", city="Tucson, Arizona", prog=None, term=None, grant=16000, date="2025-05-17", news=True))
PROGRAMMES = [
 dict(student=_XH, name=("Kembridj universitetiniń programması", "University of Cambridge programme", "Kembrij universiteti dasturi", "Программа Кембриджского университета"),
      country="uk", year=None, photo="gallery/events/ismailova-cambridge-programme-t.jpg"),
]

X = dict(
 lead=("Oqıwshılarımız qabıl etilgen shet el universitetleri. Oqıwshı basqa jerde oqıwdı tańlasa da, usınıs esapqa alınadı.",
       "Universities abroad that have offered places to our students. An offer counts even if the student chose to study elsewhere.",
       "O‘quvchilarimizga o‘rin taklif qilgan xorijiy universitetlar. O‘quvchi boshqa joyda o‘qishni tanlagan bo‘lsa ham, taklif hisobga olinadi.",
       "Зарубежные университеты, предложившие место нашим ученикам. Предложение учитывается, даже если ученик выбрал учёбу в другом месте."),
 t_off=("qabıl usınısı", "offers of admission", "ta qabul taklifi", "предложений о зачислении"),
 t_uni=("universitet", "universities", "ta universitet", "университетов"),
 t_cty=("mámleket", "countries", "ta davlat", "стран"),
 t_grant=("grantlar", "in grants", "grantlar", "в грантах"),
 admitted=("Qabıl etildi", "Admitted", "Qabul qilindi", "Принят(а)"),
 offered=("Usınıs alındı", "Offer received", "Taklif olindi", "Получено предложение"),
 via=("Jol", "Route", "Yo‘l", "Путь"),
 status=("Túri", "Type", "Turi", "Тип"),
 rank=("Dúnya reytingi", "World ranking", "Jahon reytingi", "Мировой рейтинг"),
 prog=("Baǵdar", "Programme", "Yo‘nalish", "Направление"),
 start=("Baslanıwı", "Start", "Boshlanishi", "Начало"),
 grant=("Grant", "Grant", "Grant", "Грант"),
 per_year=("jılına", "per year", "yiliga", "в год"),
 student=("Oqıwshı", "Student", "O‘quvchi", "Ученик"),
 cls=("klass", "Grade", "sinf", "класс"),
 grad=("pitkeriwshi", "graduate", "bitiruvchi", "выпуск"),
 news=("Jańalıqtı oqıw", "Read the news", "Yangilikni o‘qish", "Читать новость"),
 fall=("gúzgi semestr", "Fall", "kuzgi semestr", "осенний семестр"),
 prog_h=("Xalıqaralıq programmalar", "International programmes", "Xalqaro dasturlar", "Международные программы"),
 prog_p=("Oqıwshılarımız qatnasqan shet el universitetleriniń programmaları (bul qabıl usınısı emes).",
         "Programmes at universities abroad that our students took part in (these are not offers of admission).",
         "O‘quvchilarimiz qatnashgan xorijiy universitetlar dasturlari (bu qabul taklifi emas).",
         "Программы зарубежных университетов, в которых участвовали наши ученики (это не предложения о зачислении)."),
 cta_h=("Shet elde oqıwdı joybarlap atırsız ba?", "Planning to study abroad?", "Xorijda o‘qishni rejalashtiryapsizmi?", "Планируете учиться за рубежом?"),
 cta_p=("Basqıshpa-basqısh jol kórsetkish, mámleketler, stipendiyalar hám múddetler — barlıǵı bir jerde.",
        "Step-by-step guide, countries, scholarships and deadlines — all in one place.",
        "Bosqichma-bosqich yo‘riqnoma, davlatlar, stipendiyalar va muddatlar — hammasi bir joyda.",
        "Пошаговое руководство, страны, стипендии и сроки — всё в одном месте."),
 cta_b=("Shet elde oqıw", "Study abroad guide", "Xorijda o‘qish", "Учёба за рубежом"),
 note=("Atlar oqıwshılardıń ruxsatı menen jariyalanadı. Jańa usınıs alǵan bolsańız, mektep basshılıǵına xabar beriń.",
       "Names are published with the students’ permission. If you have received an offer, please let the school know.",
       "Ismlar o‘quvchilarning roziligi bilan e’lon qilinadi. Yangi taklif olgan bo‘lsangiz, maktab rahbariyatiga xabar bering.",
       "Имена публикуются с согласия учеников. Если вы получили предложение, сообщите об этом школе."),
 hub=("AQSh hám Ullı Britaniya universitetleriniń usınısları, sonıń ishinde dúnyanıń top-100 universitetleri — barlıǵı bir betde.",
      "Offers from universities in the USA and the UK, including world top-100 universities — all on one page.",
      "AQSh va Buyuk Britaniya universitetlari takliflari, jumladan dunyoning top-100 universitetlari — barchasi bir sahifada.",
      "Предложения университетов США и Великобритании, включая топ-100 мира, — всё на одной странице."),
)
MON = (["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentyabr", "oktyabr", "noyabr", "dekabr"],
       ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
       ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentabr", "oktabr", "noyabr", "dekabr"],
       ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"])

def _date(d, i):
    p = d.split("-")
    if len(p) < 3: return p[0]
    m = MON[i][int(p[1]) - 1]; dd = int(p[2])
    return f"{m} {dd}, {p[0]}" if i == 1 else f"{dd} {m} {p[0]}" if i == 3 else f"{dd}-{m}, {p[0]}"
def _term(t, i):
    y, s = t.split("-")
    return f'{X["fall"][i]} {y}' if i == 1 else f'{y}-jıl {X["fall"][i]}' if i == 0 else f'{y}-yil {X["fall"][i]}' if i == 2 else f'{X["fall"][i]} {y} г.'
def _cls(c, i):
    return f'{X["cls"][i]} {c}' if i == 1 else f'{c} {X["cls"][i]}'

def stats():
    return dict(n=len(OFFERS), students=len({o["student"][1] for o in OFFERS}), uni=len({o["uni"] for o in OFFERS}), cty=len({o["country"] for o in OFFERS}),
                grant=sum(o["grant"] or 0 for o in OFFERS))

def page(i, href, tabs):
    e = _html.escape; st = stats()
    tiles = "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v, l in [
        (st["n"], X["t_off"][i]), (st["uni"], X["t_uni"][i]), (st["cty"], X["t_cty"][i]), (f'${st["grant"]:,}', X["t_grant"][i])])
    cards = []
    for o in sorted(OFFERS, key=lambda o: o["date"], reverse=True):
        fl, cn = COUNTRY[o["country"]]
        rows = []
        if o.get("prog"): rows.append((X["prog"][i], o["prog"][i]))
        if o.get("term"): rows.append((X["start"][i], _term(o["term"], i)))
        if o.get("grant"): rows.append((X["grant"][i], f'<b class="ofgr">${o["grant"]:,}</b>'))
        if o.get("via"): rows.insert(0, (X["via"][i], o["via"][i]))
        if o.get("status"): rows.append((X["status"][i], o["status"][i]))
        if o.get("award"): rows.append((X["grant"][i], f'<b class="ofgr">{o["award"][i]}</b>'))
        rows.append((X["student"][i], f'{e(o["student"][i])} · {(_cls(o["cls"], i) + " · ") if o.get("cls") else ""}{(X["grad"][i] + " " + o["grad"]) if i == 3 else (o["grad"] + " " + X["grad"][i])}'))
        dl = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in rows)
        nl = f'<a class="oflink" href="{href("news/")}">{X["news"][i]} →</a>' if o.get("news") else ""
        cards.append(f'<article class="card ofcard"><div class="ofhead"><span class="offlag" aria-hidden="true">{fl}</span>'
                     f'<div><span class="ofok">✓ {X["offered" if o.get("status") else "admitted"][i]} · {_date(o["date"], i)}</span><h3>{e(o["uni"])}</h3><p class="ofloc">{e(o["city"])}, {cn[i]}{f' · <span class="ofrank">{o["rank"]}</span>' if o.get("rank") else ""}</p></div></div>'
                     f'<dl class="ofdl">{dl}</dl>{nl}</article>')
    progs = "".join(f'<article class="card ofprog">' + (f'<img src="{{UP}}photos/{p["photo"]}" alt="" loading="lazy">' if p.get("photo") else "")
                    + f'<div><span class="offlag sm" aria-hidden="true">{COUNTRY[p["country"]][0]}</span><h3>{p["name"][i]}</h3><p>{e(p["student"][i])}' + (f' · {p["year"]}' if p.get("year") else "") + '</p></div></article>'
                    for p in PROGRAMMES)
    return (f'{tabs(SUB, i, href)}<p class="lead2">{X["lead"][i]}</p><div class="stats ofstats">{tiles}</div>'
            f'<div class="ofgrid">{"".join(cards)}</div>'
            + (f'<h2 class="ofh2">{X["prog_h"][i]}</h2><p>{X["prog_p"][i]}</p><div class="ofprogs">{progs}</div>' if PROGRAMMES else "")
            + f'<div class="card ofcta"><div><h3>{X["cta_h"][i]}</h3><p>{X["cta_p"][i]}</p></div><a class="btn p" href="{href("abroad/")}">{X["cta_b"][i]} →</a></div>'
            f'<p class="note">{X["note"][i]}</p>')
