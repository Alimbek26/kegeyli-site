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
 "uz": ("🇺🇿", ("Nókis, Ózbekstan", "Nukus, Uzbekistan", "Nukus, O‘zbekiston", "Нукус, Узбекистан")),
}
_XH = ("Khurshida Ismailova", "Khurshida Ismailova", "Khurshida Ismailova", "Хуршида Исмайлова")
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
      via=("Glasgow International College (Kaplan) arqalı: 2 semestrlik foundation, keyin universitet", "Through Glasgow International College (Kaplan): a two-term foundation year, then the university",
           "Glasgow International College (Kaplan) orqali: 2 semestrlik foundation, so‘ng universitet", "Через Glasgow International College (Kaplan): подготовительный год (2 семестра), затем университет"),
      prog=("Foundation (Business and Social Sciences) → MA (Hons) Economics", "Foundation (Business and Social Sciences) → MA (Hons) Economics",
            "Foundation (Business and Social Sciences) → MA (Hons) Economics", "Foundation (Business and Social Sciences) → MA (Hons) Economics"),
      term="2025-fall", grant=None, date="2025-04-04",
      award=None, status=("Shártli usınıs", "Conditional offer", "Shartli taklif", "Условное предложение")))
OFFERS.append(
 dict(student=("Ayjamal Abdullaeva", "Ayjamal Abdullaeva", "Ayjamal Abdullayeva", "Айжамал Абдуллаева"), cls="11-A", grad="2024/2025",
      uni="University of Birmingham", country="uk", city="Birmingham, England", news=True,
      via=("University of Birmingham Foundation Pathways (Kaplan) arqalı: foundation jılı qosılǵan 4 jıllıq bakalavriat", "Through University of Birmingham Foundation Pathways (Kaplan): a four-year bachelor’s degree with an integrated foundation year",
           "University of Birmingham Foundation Pathways (Kaplan) orqali: foundation yili qo‘shilgan 4 yillik bakalavriat", "Через University of Birmingham Foundation Pathways (Kaplan): 4-летний бакалавриат с подготовительным годом"),
      prog=("BSc (Hons) Economics", "BSc (Hons) Economics", "BSc (Hons) Economics", "BSc (Hons) Economics"),
      term="2025-fall", grant=None, date="2025-04-04",
      award=None, status=("Shártli usınıs", "Conditional offer", "Shartli taklif", "Условное предложение")))
OFFERS.append(
 dict(student=("Aynura Turǵanbaeva", "Aynura Turganbaeva", "Aynura Turg‘anbayeva", "Айнура Турганбаева"), cls="11-A", grad="2024/2025",
      uni="University of Arizona", country="us", city="Tucson, Arizona", prog=None, term=None, grant=16000, date="2025-05-17", news=True))
# Official website and QS World University Rankings 2025 position (the edition current when the offers were made).
# qs: number for sorting, text as shown; None = not in the QS ranking. note: shown after the rank.
UNI = {
 "University of Glasgow": ("https://www.gla.ac.uk", 78, "78"),
 "University of Birmingham": ("https://www.birmingham.ac.uk", 80, "80"),
 "University of Minnesota Twin Cities": ("https://twin-cities.umn.edu", 203, "=203"),
 "University of Arizona": ("https://www.arizona.edu", 293, "=293"),
 "Colorado State University": ("https://www.colostate.edu", 442, "=442"),
 "Iowa State University": ("https://www.iastate.edu", 470, "470"),
 "University of Cincinnati — Clermont College": ("https://ucclermont.edu", 761, "761–770"),
 "Pennsylvania Western University": ("https://www.pennwest.edu", None, None),
 "Caldwell University": ("https://www.caldwell.edu", None, None),
}
UNI_NOTE = {"University of Cincinnati — Clermont College": ("University of Cincinnati reytingi", "University of Cincinnati as a whole", "University of Cincinnati reytingi", "рейтинг University of Cincinnati в целом")}
PSUB = "achievements/programmes/"
PNAME = ("Xalıqaralıq programmalar", "International programmes", "Xalqaro dasturlar", "Международные программы")
PDESC = ("Oqıwshılarımız qatnasqan shet el universitetleriniń hám xalıqaralıq shólkemlerdiń programmaları.",
         "Programmes at universities and organisations abroad that our students have taken part in.",
         "O‘quvchilarimiz qatnashgan xorijiy universitetlar va xalqaro tashkilotlar dasturlari.",
         "Программы зарубежных университетов и международных организаций, в которых участвовали наши ученики.")
PICON = ('<path d="M12 3l9 4.500-9 4.500-9-4.500z"/><path d="M7 9.700V15c0 1.300 2.200 3 5 3s5-1.700 5-3V9.700"/><path d="M21 7.500v6"/>', "#0d9488")
PROGRAMMES = [
 dict(student=("Gulnur Abdullaeva", "Gulnur Abdullaeva", "Gulnur Abdullaeva", "Гульнур Абдуллаева"),
      name=("«English for IT» jazǵı lageri", "English for IT Summer Camp", "«English for IT» yozgi lageri", "Летний лагерь English for IT"),
      country="uz", year="2025", photo="gallery/events/english-for-it-camp-with-cert.jpg", cls="11-B", grad="2025/2026",
      note=("AQSh húkimeti tárepinen AQSh-tıń Ózbekstandaǵı elshixanası arqalı qarjılandırılǵan 3 háptelik programma. Ámelge asırıwshılar: American Councils hám IT Park University. 2025-jıl 28-iyul – 15-avgust, Nókis.",
            "A 3-week programme funded by the U.S. Government through the U.S. Embassy in Uzbekistan, run by American Councils and IT Park University. 28 July – 15 August 2025, Nukus.",
            "AQSh hukumati tomonidan AQShning O‘zbekistondagi elchixonasi orqali moliyalashtirilgan 3 haftalik dastur. Amalga oshiruvchilar: American Councils va IT Park University. 2025-yil 28-iyul – 15-avgust, Nukus.",
            "Трёхнедельная программа, финансируемая правительством США через посольство США в Узбекистане; организаторы — American Councils и IT Park University. 28 июля – 15 августа 2025 г., Нукус.")),
 dict(student=_XH, name=("Kembridj universitetiniń programması", "University of Cambridge programme", "Kembrij universiteti dasturi", "Программа Кембриджского университета"),
      country="uk", year=None, photo="gallery/events/ismailova-cambridge-programme.jpg", cls="11-A", grad="2024/2025"),
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
 site=("Rásmiy sayt", "Official website", "Rasmiy sayt", "Официальный сайт"),
 noqs=("QS reytinginde joq", "Not in the QS ranking", "QS reytingida yo‘q", "Нет в рейтинге QS"),
 t_top=("dúnyanıń top-100 universiteti", "world top-100 universities", "ta dunyo top-100 universiteti", "университета из мирового топ-100"),
 qs_src=("Reyting: QS World University Rankings 2025 (usınıslar alınǵan waqıttaǵı basılım), topuniversities.com.",
         "Rankings: QS World University Rankings 2025 (the edition current when the offers were made), topuniversities.com.",
         "Reyting: QS World University Rankings 2025 (takliflar olingan paytdagi nashr), topuniversities.com.",
         "Рейтинг: QS World University Rankings 2025 (издание, действовавшее на момент предложений), topuniversities.com."),
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

def _rank(uni, i):
    u = UNI.get(uni)
    if not u: return ""
    if u[1] is None:
        return f'<p class="ofqs none">{X["noqs"][i]}</p>'
    top = ' top' if u[1] <= 100 else ''
    note = f' <small>({UNI_NOTE[uni][i]})</small>' if uni in UNI_NOTE else ""
    return f'<p class="ofqs{top}"><b>QS 2025: #{u[2]}</b>{note}</p>'

def stats():
    return dict(n=len(OFFERS), students=len({o["student"][1] for o in OFFERS}), uni=len({o["uni"] for o in OFFERS}), cty=len({o["country"] for o in OFFERS}),
                grant=sum(o["grant"] or 0 for o in OFFERS),
                top=len({o["uni"] for o in OFFERS if (UNI.get(o["uni"], (0, None))[1] or 9999) <= 100}))

def page(i, href, tabs):
    e = _html.escape; st = stats()
    tiles = "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v, l in [
        (st["n"], X["t_off"][i]), (st["uni"], X["t_uni"][i]), (st["top"], X["t_top"][i]), (st["cty"], X["t_cty"][i]), (f'${st["grant"]:,}', X["t_grant"][i])])
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
        site = UNI.get(o["uni"], (None,))[0]
        sl = f'<a class="oflink ofsite" href="{site}" target="_blank" rel="noopener">{X["site"][i]}: {site.split("//")[1]} ↗</a>' if site else ""
        nl = sl + (f'<a class="oflink" href="{href("news/")}">{X["news"][i]} →</a>' if o.get("news") else "")
        nl = f'<div class="oflinks">{nl}</div>'
        cards.append(f'<article class="card ofcard"><div class="ofhead"><span class="offlag" aria-hidden="true">{fl}</span>'
                     f'<div><span class="ofok">✓ {X["offered" if o.get("status") else "admitted"][i]} · {_date(o["date"], i)}</span><h3>{e(o["uni"])}</h3><p class="ofloc">{e(o["city"])}, {cn[i]}</p>{_rank(o["uni"], i)}</div></div>'
                     f'<dl class="ofdl">{dl}</dl>{nl}</article>')
    return (f'{tabs(SUB, i, href)}<p class="lead2">{X["lead"][i]}</p><div class="stats ofstats">{tiles}</div>'
            f'<div class="ofgrid">{"".join(cards)}</div>'
            + f'<div class="card ofcta"><div><h3>{X["cta_h"][i]}</h3><p>{X["cta_p"][i]}</p></div><a class="btn p" href="{href("abroad/")}">{X["cta_b"][i]} →</a></div>'
            f'<p class="note">{X["qs_src"][i]} {X["note"][i]} <a href="{{UP}}school-profile/">School Profile (PDF) →</a> · <a href="{href("international/")}">{__import__("international").NAME[i]} →</a></p>')


PX = dict(
 lead=("Shet el universitetleriniń hám xalıqaralıq shólkemlerdiń jazǵı mektepleri, kursları hám programmaları — oqıwshılarımız qatnasqan.",
       "Summer schools, courses and programmes run by universities abroad and international organisations that our students have taken part in.",
       "O‘quvchilarimiz qatnashgan xorijiy universitetlar va xalqaro tashkilotlarning yozgi maktablari, kurslari va dasturlari.",
       "Летние школы, курсы и программы зарубежных университетов и международных организаций, в которых участвовали наши ученики."),
 t_prog=("programma", "programmes", "ta dastur", "программ"), t_stud=("oqıwshı", "students", "nafar o‘quvchi", "учеников"), t_cty=("mámleket", "countries", "ta davlat", "стран"),
 not_offer=("Bul qabıl usınısı emes — programmaǵa qatnasıw.", "This is participation in a programme, not an offer of admission.", "Bu qabul taklifi emas — dasturda ishtirok.", "Это участие в программе, а не предложение о зачислении."),
 offers=("Shet el universitetleriniń qabıl usınısları", "Offers of admission from universities abroad", "Xorijiy universitetlarning qabul takliflari", "Предложения о зачислении от зарубежных университетов"),
 tell_h=("Xalıqaralıq programmaǵa qatnastıńız ba?", "Taken part in an international programme?", "Xalqaro dasturda qatnashdingizmi?", "Участвовали в международной программе?"),
 tell_p=("Programmanıń atın, shólkemlestiriwshisin, sánesin hám fotonı mektep basshılıǵına jiberiń — bul betke qosamız.",
         "Send the programme name, organiser, dates and a photo to the school — we will add it to this page.",
         "Dastur nomi, tashkilotchisi, sanalari va suratni maktab rahbariyatiga yuboring — ushbu sahifaga qo‘shamiz.",
         "Пришлите в школу название программы, организатора, даты и фото — мы добавим её на эту страницу."),
)

def ppage(i, href, tabs):
    e = _html.escape
    n_st = len({p["student"][1] for p in PROGRAMMES}); n_c = len({p["country"] for p in PROGRAMMES})
    tiles = "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v, l in [
        (len(PROGRAMMES), PX["t_prog"][i]), (n_st, PX["t_stud"][i]), (n_c, PX["t_cty"][i])])
    cards = []
    for p in PROGRAMMES:
        fl, cn = COUNTRY[p["country"]]
        who = e(p["student"][i]) + (f' · {_cls(p["cls"], i)}' if p.get("cls") else "") + (f' · {(X["grad"][i] + " " + p["grad"]) if i == 3 else (p["grad"] + " " + X["grad"][i])}' if p.get("grad") else "")
        img = f'<img src="{{UP}}photos/{p["photo"]}" alt="{e(p["name"][i])}" loading="lazy">' if p.get("photo") else ""
        cards.append(f'<article class="card prcard">{img}<div class="prbody"><span class="offlag sm" aria-hidden="true">{fl}</span>'
                     f'<h3>{p["name"][i]}</h3><p class="ofloc">{cn[i]}' + (f' · {p["year"]}' if p.get("year") else "") + '</p>'
                     + (f'<p class="prdesc">{p["note"][i]}</p>' if p.get("note") else "") + f'<dl class="ofdl"><dt>{X["student"][i]}</dt><dd>{who}</dd></dl><p class="prnote">{PX["not_offer"][i]}</p></div></article>')
    return (f'{tabs(PSUB, i, href)}<p class="lead2">{PX["lead"][i]}</p><div class="stats ofstats prstats">{tiles}</div>'
            f'<div class="prgrid">{"".join(cards)}</div>'
            f'<a class="card satprev satban ofban" href="{href(SUB)}"><div class="sph"><span class="acbi" style="--ac:{ICON[1]}"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICON[0]}</svg></span><div><h3>{NAME[i]} · {len(OFFERS)}</h3><p>{PX["offers"][i]}</p></div><span class="acgo2">→</span></div></a>'
            f'<div class="card ofcta"><div><h3>{PX["tell_h"][i]}</h3><p>{PX["tell_p"][i]}</p></div><a class="btn p" href="{href("abroad/")}">{X["cta_b"][i]} →</a></div>')
