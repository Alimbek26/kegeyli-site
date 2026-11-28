# "About the school" page: official name, timeline, mission & values, quick facts, links.
# Edit TIMELINE to add milestones: (year, (kaa, en, uz, ru) title, (kaa, en, uz, ru) text)
NAME = ("Mektep haqqında", "About the school", "Maktab haqida", "О школе")
DESC = ("Kegeyli rayonı qánigelestirilgen mektebi haqqında: tariyxı, missiyası, qádiriyatları, nátiyjeleri hám baylanıs.",
        "About Kegeyli District Specialized School: history, mission, values, results and contact details.",
        "Kegeli tumani ixtisoslashtirilgan maktabi haqida: tarixi, missiyasi, qadriyatlari, natijalari va aloqa.",
        "О Кегейлийской районной специализированной школе: история, миссия, ценности, результаты и контакты.")
OFFICIAL = ("Rásmiy ataması", "Official name", "Rasmiy nomi", "Официальное название")
FULL = ("Kegeyli Qánigelestirilgen Mektebi", "Kegeyli District Specialized Educational Institution",
        "Kegeli tumani ixtisoslashtirilgan ta’lim muassasasi", "Кегейлийская районная специализированная образовательная организация")
SUB = ("Qaraqalpaqstan Respublikası, Kegeyli rayonı. Qánigelestirilgen bilimlendiriw mekemeleri agentligi sistemasında.",
       "Kegeyli District, Republic of Karakalpakstan. Part of the Agency for Specialized Educational Institutions.",
       "Qoraqalpog‘iston Respublikasi, Kegeli tumani. Ixtisoslashtirilgan ta’lim muassasalari agentligi tizimida.",
       "Республика Каракалпакстан, Кегейлийский район. Входит в систему Агентства специализированных образовательных учреждений.")
H_TL = ("Mektep tariyxı", "School history", "Maktab tarixi", "История школы")
TIMELINE = [
 ("2022", ("Mektep ashıldı", "The school opens", "Maktab ochildi", "Открытие школы"),
  ("Kegeyli rayonında anıq hám tábiyiy pánlerge qánigelestirilgen mektep jumısın basladı.", "A school specializing in exact and natural sciences starts work in Kegeyli District.", "Kegeli tumanida aniq va tabiiy fanlarga ixtisoslashgan maktab faoliyatini boshladi.", "В Кегейлийском районе начала работу школа, специализирующаяся на точных и естественных науках.")),
 ("2024", ("Xalıqaralıq imtihanlar", "International exams begin", "Xalqaro imtihonlar", "Международные экзамены"),
  ("Oqıwshılarımız birinshi IELTS sertifikatların aldı. Búgin {n} oqıwshınıń IELTS sertifikatı bar.", "Our students receive their first IELTS certificates. Today {n} students hold one.", "O‘quvchilarimiz birinchi IELTS sertifikatlarini oldi. Bugun {n} nafar o‘quvchining IELTS sertifikati bor.", "Ученики получают первые сертификаты IELTS. Сегодня сертификат IELTS есть у {n} учеников.")),
 ("2025", ("Milliy sertifikat hám olimpiada", "National certificates and olympiads", "Milliy sertifikat va olimpiada", "Нацсертификаты и олимпиады"),
  ("2025/2026 oqıw jılında 95 milliy sertifikat imtihanı tapsırıldı (aldıńǵı jılı 32). AKHU STEM olimpiadasında bronza medal.", "In 2025/2026 students took 95 national certificate exams (32 a year earlier) and won a bronze medal at the AKHU STEM Olympiad.", "2025/2026 o‘quv yilida 95 ta milliy sertifikat imtihoni topshirildi (avvalgi yili 32). AKHU STEM olimpiadasida bronza medal.", "В 2025/2026 учебном году сдано 95 нацсертификатов (годом ранее 32) и получена бронзовая медаль на олимпиаде AKHU STEM.")),
 ("2026", ("Sayt hám Study abroad orayı", "Website and Study abroad center", "Sayt va Study abroad markazi", "Сайт и центр Study abroad"),
  ("kegeyliqm.uz iske qosıldı: 4 tilde mektep haqqında maǵlıwmat hám shet elde oqıwǵa tayarlıq quralları.", "kegeyliqm.uz goes live in four languages with school information and tools for studying abroad.", "kegeyliqm.uz 4 tilda ishga tushdi: maktab haqida ma’lumot va chet elda o‘qishga tayyorlov vositalari.", "Запущен kegeyliqm.uz на четырёх языках: информация о школе и инструменты для поступления за рубеж.")),
]
H_MV = ("Maqset, missiya hám qádiriyatlar", "Goal, mission and values", "Maqsad, missiya va qadriyatlar", "Цель, миссия и ценности")
GOAL_H = ("Maqseti", "Our goal", "Maqsadi", "Цель")
MISSION_H = ("Missiyası", "Our mission", "Missiyasi", "Миссия")
OFFICIAL_NOTE = ("Mekteptiń rásmiy maqseti hám missiyası", "The school’s official goal and mission statements", "Maktabning rasmiy maqsadi va missiyasi", "Официальные цель и миссия школы")
GOAL = (("Mámleket bilimlendiriw standartlarına sáykes hár bir oqıwshınıń bilim-tárbiya alıwı, anıq hám tábiyiy pánler, Ózbekstan tariyxı hám shet tillerin tereńlestirip úyretiwge baǵdarlanǵan.",
         "Jas áwladtıń Ózbekstanda ámelge asırılıp atırǵan reformalar mazmun-mánisin tereń ańlaytuǵın hár tárepleme básekiles, erkin pikirleytuǵın intellektual, ilimiy hám dóretiwshilik qábiletlerin júzege shıǵarıw arqalı ruwxıy jaqtan kamal tabıwına járdemlesiw, átirap-álemge sanalı múnásibetin qáliplestiriw, hár tárepleme dúnyaqarası keń shaxstı tárbiyalaw bolıp tabıladı."),
        ("To give every student an education in line with the state educational standards, with in-depth teaching of the exact and natural sciences, the history of Uzbekistan and foreign languages.",
         "To help young people grow intellectually and spiritually by developing their intellectual, scientific and creative abilities, so that they become well-rounded, competitive and free-thinking people who deeply understand the reforms under way in Uzbekistan; to build a conscious attitude to the world around them; and to raise individuals with a broad outlook."),
        ("Davlat ta’lim standartlariga muvofiq har bir o‘quvchining ta’lim-tarbiya olishi, aniq va tabiiy fanlar, O‘zbekiston tarixi va xorijiy tillarni chuqurlashtirib o‘qitishga yo‘naltirilgan.",
         "Yosh avlodning O‘zbekistonda amalga oshirilayotgan islohotlar mazmun-mohiyatini chuqur anglaydigan, har tomonlama raqobatbardosh, erkin fikrlaydigan intellektual, ilmiy va ijodiy qobiliyatlarini ro‘yobga chiqarish orqali ma’naviy kamol topishiga ko‘maklashish, atrof-olamga ongli munosabatini shakllantirish, har tomonlama dunyoqarashi keng shaxsni tarbiyalashdan iborat."),
        ("Обеспечить каждому ученику обучение и воспитание в соответствии с государственными образовательными стандартами с углублённым изучением точных и естественных наук, истории Узбекистана и иностранных языков.",
         "Содействовать духовному развитию молодого поколения — всесторонне конкурентоспособных, свободно мыслящих людей, глубоко понимающих суть проводимых в Узбекистане реформ, — через раскрытие их интеллектуальных, научных и творческих способностей; формировать осознанное отношение к окружающему миру и воспитывать всесторонне развитую личность с широким кругозором."))
MISSION = ("Intalı oqıwshılarǵa olardıń potencialların maksimal dárejede qanaatlandıra alatuǵın tálim beriw múmkinshiligin jaratıw arqalı bilimlendiriw tájiriybesin asırıw, turaqlı ózgeriwsheń global jámiyette ózin-ózi basqarıwshı hám jetik sanalı shaxslar tárbiyalawda dóretiwshilik hám innovaciyalıq pikirlewdi rawajlandırıw arqalı belsendi puqaralar hám ilim alıwdan sharshamaytuǵın oqıwshılardı tárbiyalaw bolıp tabıladı.",
           "To raise active citizens and tireless learners: we strengthen our educational practice by giving motivated students an education that fully meets their potential, and we develop creative and innovative thinking so that they grow into self-directed, mature and conscious people in a constantly changing global society.",
           "Iqtidorli o‘quvchilarga ularning salohiyatini maksimal darajada qondira oladigan ta’lim berish imkoniyatini yaratish orqali ta’lim tajribasini oshirish, doimiy o‘zgaruvchan global jamiyatda o‘zini o‘zi boshqaradigan va yetuk ongli shaxslarni tarbiyalashda ijodiy va innovatsion fikrlashni rivojlantirish orqali faol fuqarolar va ilm olishdan charchamaydigan o‘quvchilarni tarbiyalashdan iborat.",
           "Воспитывать активных граждан и учеников, не устающих учиться: повышать образовательный опыт, создавая для мотивированных учеников возможность получать образование, в полной мере раскрывающее их потенциал, и развивать творческое и инновационное мышление при воспитании самостоятельных и зрелых, сознательных личностей в постоянно меняющемся глобальном обществе.")
VALUES = [
 (("Bilimde sapa", "Academic excellence", "Bilimda sifat", "Качество знаний"), ("Tereńletilgen matematika, ingliz tili hám STEM.", "Advanced mathematics, English and STEM.", "Chuqurlashtirilgan matematika, ingliz tili va STEM.", "Углублённые математика, английский и STEM."), "#0b7a8f",
  '<path d="M3 9l9-5 9 5-9 5-9-5z"/><path d="M7 11.500V16c0 1 2.500 2.500 5 2.500s5-1.500 5-2.500v-4.500"/>'),
 (("Xalıqaralıq kózqaras", "Global outlook", "Xalqaro nuqtai nazar", "Глобальный взгляд"), ("IELTS, SAT hám shet elde oqıwǵa járdem.", "IELTS, SAT and support for studying abroad.", "IELTS, SAT va chet elda o‘qishga ko‘mak.", "IELTS, SAT и поддержка поступления за рубеж."), "#2a7fd1",
  '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'),
 (("Sadıqlıq", "Integrity", "Halollik", "Честность"), ("Ashıq, ádil qabıllaw hám baha qoyıw.", "Open, fair admission and assessment.", "Ochiq, adolatli qabul va baholash.", "Открытый и честный приём и оценивание."), "#7c3aed",
  '<path d="M12 3l8 3v6c0 4.500-3.500 8-8 9-4.500-1-8-4.500-8-9V6z"/><path d="M8.500 12l2.500 2.500 4.500-5"/>'),
 (("Hámkarlıq", "Partnership", "Hamkorlik", "Сотрудничество"), ("Ata-analar, muǵallimler hám sheriklerdiń birgeliktegi isi.", "Parents, teachers and partners working together.", "Ota-onalar, o‘qituvchilar va hamkorlarning birgalikdagi ishi.", "Совместная работа родителей, учителей и партнёров."), "#d97706",
  '<circle cx="8" cy="9" r="3"/><circle cx="16.500" cy="10" r="2.500"/><path d="M2.500 19c.5-3 2.800-5 5.500-5s5 2 5.500 5M14 18.500c.4-2 1.800-3.500 3.500-3.500 2 0 3.500 1.500 4 3.500"/>'),
]
H_FACTS = ("Qısqasha maǵlıwmat", "At a glance", "Qisqacha ma’lumot", "Коротко")
H_NUM = ("Nátiyjeler", "Results", "Natijalar", "Результаты")
H_GO = ("Keyingi bólimler", "Explore more", "Keyingi bo‘limlar", "Узнать больше")
GO = [("leadership/", ("Basshılıq", "Leadership", "Rahbariyat", "Руководство")), ("teachers/", ("Muǵallimler", "Teachers", "O‘qituvchilar", "Учителя")),
      ("admission/", ("Qabıllaw", "Admission", "Qabul", "Приём")), ("abroad/", ("Shet elde oqıw", "Study abroad", "Chet elda o‘qish", "Учёба за рубежом")),
      ("partners/", ("Sheriklerimiz", "Partners", "Hamkorlar", "Партнёры")), ("documents/", ("Hújjetler", "Documents", "Hujjatlar", "Документы")),
      ("international/", ("Xalıqaralıq maqsetlerimiz", "Our international goals", "Xalqaro maqsadlarimiz", "Наши международные цели"))]

# Status and accreditation (for universities, College Board and partners abroad)
ST_H = ("Mekteptiń statusı hám akkreditaciyası", "Status and accreditation", "Maktab maqomi va akkreditatsiyasi", "Статус и аккредитация")
AGENCY_URL = "https://gov.uz/oz/ima"
STATUS = [
 (("Túri", "Type", "Turi", "Тип"),
  ("Mámleketlik qánigelestirilgen ulıwma orta bilim beriw mektebi", "State (public) specialized general secondary school", "Davlat ixtisoslashtirilgan umumiy o‘rta ta’lim maktabi", "Государственная специализированная общеобразовательная школа")),
 (("Tiykar salınǵan", "Founded", "Tashkil etilgan", "Основана"), ("2022", "2022", "2022", "2022")),
 (("Basqarıw organı", "Governing authority", "Boshqaruv organi", "Орган управления"),
  ("Ózbekstan Respublikası Bilimlendiriw hám ilim-pán ministrligi janındaǵı Qánigelestirilgen bilimlendiriw mekemeleri agentligi",
   "Agency for Specialized Educational Institutions under the Ministry of Education and Science of the Republic of Uzbekistan",
   "O‘zbekiston Respublikasi Ta’lim va ilm-fan vazirligi huzuridagi Ixtisoslashtirilgan ta’lim muassasalari agentligi",
   "Агентство специализированных образовательных учреждений при Министерстве образования и науки Республики Узбекистан")),
 (("Klasslar", "Grades", "Sinflar", "Классы"), ("5–11", "5–11", "5–11", "5–11")),
 (("Oqıtıw tili", "Language of instruction", "Ta’lim tili", "Язык обучения"), ("Qaraqalpaq tili", "Karakalpak", "Qoraqalpoq tili", "Каракалпакский")),
 (("Pitkeriwshilerge beriledi", "Graduates receive", "Bitiruvchilarga beriladi", "Выпускники получают"),
  ("Ulıwma orta bilim haqqında mámleketlik attestat", "State certificate (attestat) of complete general secondary education", "Umumiy o‘rta ta’lim to‘g‘risida davlat attestati", "Государственный аттестат о полном общем среднем образовании")),
 (("Bahalaw sisteması", "Grading scale", "Baholash tizimi", "Система оценок"),
  ("5 ballıq: 5 — ayrıqsha, 4 — jaqsı, 3 — qanaatlandırarlı, 2 — qanaatlandırarlı emes", "5-point scale: 5 = excellent, 4 = good, 3 = satisfactory, 2 = unsatisfactory",
   "5 ballik: 5 — a’lo, 4 — yaxshi, 3 — qoniqarli, 2 — qoniqarsiz", "5-балльная: 5 — отлично, 4 — хорошо, 3 — удовлетворительно, 2 — неудовлетворительно")),
]
def status_card(i):
    rows = "".join(f"<dt>{k[i]}</dt><dd>{v[i]}" + (f' <a href="{AGENCY_URL}" target="_blank" rel="noopener">gov.uz/ima ↗</a>' if k[1] == "Governing authority" else "") + "</dd>" for n, (k, v) in enumerate(STATUS))
    sp = ("Universitetler ushın: mektep profili (inglis tilinde, PDF)", "For universities: School Profile (PDF)", "Universitetlar uchun: maktab profili (ingliz tilida, PDF)", "Для университетов: профиль школы (на английском, PDF)")[i]
    return f'<section class="card astatus" id="status"><h2>{ST_H[i]}</h2><dl>{rows}</dl><p class="aspl btns"><a class="btn p" href="{{UP}}school-profile/">{sp} →</a><a class="btn s" href="{{UP}}files/kegeyli-school-profile-2026-2027.pdf" download>PDF ↓</a></p></section>'

H_CAMPUS = ("Mektebimiz", "Our campus", "Maktabimiz", "Наша школа")
CAMPUS_P = ("Jarıq klasslar, laboratoriyalar hám keń kirisiw zalı — oqıwshılarımız kúnin usı jerde ótkeredi.",
            "Bright classrooms, laboratories and a spacious entrance hall: this is where our students spend their day.",
            "Yorug‘ sinflar, laboratoriyalar va keng kirish zali — o‘quvchilarimiz kunini shu yerda o‘tkazadi.",
            "Светлые классы, лаборатории и просторный холл — здесь проходит день наших учеников.")
CAMPUS_ALL = ("Barlıq súwretler", "All campus photos", "Barcha suratlar", "Все фотографии")


def campus(i, up, gal_href):
    import gallery as G
    ps = [p for p in G.PHOTOS if G.ALBUM_OF.get(p["file"].split("/")[-1]) == "campus"]
    if not ps:
        return ""
    cells = ""
    for k, p in enumerate(ps[:5]):
        f = p["file"]; src = f"{up}photos/gallery/{f}.jpg" if k == 0 else f"{up}photos/gallery/{f}-t.jpg"
        cells += f'<a class="acp{" big" if k == 0 else ""}" href="{gal_href}#campus"><img src="{src}" alt="{p["cap"][i]}" loading="lazy"><span>{p["cap"][i]}</span></a>'
    return (f'<h2 class="ah">{H_CAMPUS[i]}</h2><p>{CAMPUS_P[i]}</p><div class="acgrid n{min(len(ps), 5)}">{cells}</div>'
            f'<p class="btns"><a class="btn s" href="{gal_href}#campus">{CAMPUS_ALL[i]} ({len(ps)}) →</a></p>')


def body(i, up, t, hrefs):
    import achieve as _A
    tl = "".join(f'<li><span class="aty">{y}</span><div class="atc card"><h3>{h[i]}</h3><p>{p[i].replace("{n}", str(len(_A.IELTS)))}</p></div></li>' for y, h, p in TIMELINE)
    vals = "".join(f'<div class="card avc" style="--mc:{c}"><span class="mi"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ic}</svg></span><h3>{h[i]}</h3><p>{p[i]}</p></div>' for h, p, c, ic in VALUES)
    facts = "".join(f"<li><b>{k}</b><span>{v}</span></li>" for k, v in t["facts"])
    nums = "".join(f'<div class="card anc"><b>{n}</b><span>{l}</span></div>' for n, l in t["results"])
    go = "".join(f'<a class="btn s" href="{hrefs[k]}">{n[i]} →</a>' for k, n in GO)
    return (f'<div class="ahero"><img src="{up}photos/school.jpg" alt="{FULL[i]}" fetchpriority="high"></div>'
            f'<div class="card aname"><small>{OFFICIAL[i]}</small><h2>{FULL[i]}</h2><p>{SUB[i]}</p></div>'
            f'<p class="lead2">{t["about1"]}</p><p>{t["about2"]}</p>{status_card(i)}' + campus(i, up, hrefs["gallery/"]) +
            f'<h2 class="ah">{H_TL[i]}</h2><ol class="atl">{tl}</ol><p class="btns"><a class="btn p" href="{hrefs["history/"]}">{__import__("history").NAME[i]} →</a></p>'
            f'<h2 class="ah">{H_MV[i]}</h2><p class="amnote">{OFFICIAL_NOTE[i]}</p><div class="amgrid">'
            f'<div class="card amc"><h3>{GOAL_H[i]}</h3>' + "".join(f"<p>{x}</p>" for x in GOAL[i]) + '</div>'
            f'<div class="card amc mis"><h3>{MISSION_H[i]}</h3><p>{MISSION[i]}</p></div></div><div class="avgrid">{vals}</div>'
            f'<h2 class="ah">{H_NUM[i]}</h2><div class="angrid">{nums}</div>'
            f'<h2 class="ah">{H_FACTS[i]}</h2><ul class="facts afacts">{facts}</ul>'
            f'<h2 class="ah">{H_GO[i]}</h2><div class="btns ago">{go}</div>')
