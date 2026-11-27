# "Study abroad" hub: roadmap, applications tracker, scholarships (+ IELTS as a tab)
import json
import top10 as TP
import apps as AP
import countries as CO
import deadlines as DLN
import checklist as CKL
import calculator as CAL
import sat as SAT
import plan as PL
import essay as ESS
NAME = ("Shet elde oqıw", "Study abroad", "Xorijda o‘qish", "Учёба за рубежом")
TABS = {  # key: (url sub, labels)
 "abroad/": ("abroad/", ("Jol kartası", "Roadmap", "Yo‘l xaritasi", "Дорожная карта")),
 "abroad/plan/": ("abroad/plan/", PL.NAME),
 "abroad/applications/": ("abroad/applications/", ("Meniń arzalarım", "My applications", "Mening arizalarim", "Мои заявки")),
 "abroad/scholarships/": ("abroad/scholarships/", ("Stipendiyalar", "Scholarships", "Stipendiyalar", "Стипендии")),
 "abroad/countries/": ("abroad/countries/", CO.TAB),
 "abroad/calendar/": ("abroad/calendar/", DLN.TAB),
 "abroad/checklist/": ("abroad/checklist/", CKL.TAB),
 "abroad/calculator/": ("abroad/calculator/", CAL.TAB),
 "abroad/sat/": ("abroad/sat/", SAT.TAB),
 "abroad/essay/": ("abroad/essay/", ESS.TAB),
 "abroad/top10/": ("abroad/top10/", TP.TAB),
 "abroad/commonapp/": ("abroad/commonapp/", AP.NAME["abroad/commonapp/"]),
 "abroad/ucas/": ("abroad/ucas/", AP.NAME["abroad/ucas/"]),
 "ielts/": ("ielts/", ("IELTS", "IELTS", "IELTS", "IELTS")),
}
GROUP = tuple(TABS)
_I = lambda d: f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
TAB_ICON = {  # (svg, colour)
 "abroad/": (_I('<path d="M12 21s-6-5.6-6-10.5a6 6 0 0 1 12 0C18 15.4 12 21 12 21z"/><circle cx="12" cy="10.5" r="2.2"/>'), "#0b7a8f"),
 "abroad/applications/": (_I('<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4h6v3H9zM9 12l2 2 4-4M9 17h6"/>'), "#2f8f5b"),
 "abroad/scholarships/": (_I('<path d="M12 3l2.7 5.5 6 .9-4.4 4.2 1 6L12 16.7 6.7 19.6l1-6L3.3 9.4l6-.9z"/>'), "#d99a00"),
 "abroad/plan/": (_I('<path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/>'), "#d97706"),
 "abroad/sat/": (_I('<rect x="4" y="3" width="16" height="18" rx="2"/><circle cx="8.500" cy="8" r="1"/><circle cx="8.500" cy="12" r="1"/><circle cx="8.500" cy="16" r="1"/><path d="M12 8h5M12 12h5M12 16h3"/>'), "#7c3aed"),
 "abroad/essay/": (_I('<path d="M4 20l1-4L16 5a2.100 2.100 0 0 1 3 3L8 19z"/><path d="M14 7l3 3M4 20h6"/>'), "#be185d"),
 "abroad/calculator/": (_I('<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 11h2M12 11h2M8 15h2M12 15h2M8 18h2M12 18h4"/>'), "#b45309"),
 "abroad/checklist/": (_I('<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8l1.5 1.5L12 7M8 14l1.5 1.5L12 13M14 9h3M14 15h3"/>'), "#047857"),
 "abroad/calendar/": (_I('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4M8 14h3M13 14h3M8 18h3"/>'), "#d6452f"),
 "abroad/countries/": (_I('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'), "#2a7fd1"),
 "abroad/top10/": (_I('<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0zM7 6H4a3 3 0 0 0 3 4M17 6h3a3 3 0 0 1-3 4"/>'), "#e07a1f"),
 "abroad/commonapp/": (_I('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M8 14h8M8 17h5"/>'), "#5b5fc7"),
 "abroad/ucas/": (_I('<path d="M12 4l9 4-9 4-9-4z"/><path d="M7 10.5v4.5c0 1.4 2.2 3 5 3s5-1.600 5-3v-4.500M21 8v6"/>'), "#b23a48"),
 "ielts/": (_I('<path d="M4 5h9a3 3 0 0 1 3 3v12a2 2 0 0 0-2-2H4zM20 5h-4M10 9v4M8 11h4"/><path d="M17 12h3v7h-3"/>'), "#0f8f7a"),
}
SUBNAME = {k: v[1] for k, v in TABS.items()}
DESC = {
 "abroad/plan/": PL.DESC, "abroad/top10/": TP.DESC, "abroad/countries/": CO.DESC, "abroad/calendar/": DLN.DESC, "abroad/checklist/": CKL.DESC, "abroad/calculator/": CAL.DESC, "abroad/sat/": SAT.DESC, "abroad/essay/": ESS.DESC, **AP.DESC,
 "abroad/": ("Shet elde oqıw: 9–11-klass boyınsha jol kartası, universitetke arza tayarlaw hám keńes. Kegeyli qánigelestirilgen mektebi.",
             "Studying abroad: a roadmap for grades 9–11, how to prepare university applications, and counselling. Kegeyli specialized school.",
             "Xorijda o‘qish: 9–11-sinflar uchun yo‘l xaritasi, universitetga ariza tayyorlash va maslahat. Kegeyli ixtisoslashtirilgan maktabi.",
             "Учёба за рубежом: дорожная карта для 9–11 классов, подготовка заявок в университеты и консультации. Кегейлийская специализированная школа."),
 "abroad/applications/": ("Universitetlerge arzalarıńızdı, múddetlerdi hám hújjetlerdi qadaǵalań. Maǵlıwmatlar telefonıńızda saqlanadı.",
                          "Track your university applications, deadlines and documents. Your data stays on your own phone.",
                          "Universitetlarga arizalaringiz, muddatlar va hujjatlarni kuzating. Ma’lumotlar telefoningizda saqlanadi.",
                          "Отслеживайте заявки в университеты, сроки и документы. Данные хранятся только на вашем телефоне."),
 "abroad/scholarships/": ("Shet elde oqıw ushın stipendiyalar: Túrkiya, Vengriya, Qıtay, Yaponiya, Koreya. Rásmiy siltemeler menen.",
                          "Scholarships for studying abroad: Turkey, Hungary, China, Japan, Korea. With official links.",
                          "Xorijda o‘qish uchun stipendiyalar: Turkiya, Vengriya, Xitoy, Yaponiya, Koreya. Rasmiy havolalar bilan.",
                          "Стипендии для учёбы за рубежом: Турция, Венгрия, Китай, Япония, Корея. С официальными ссылками."),
}
T = {
 "intro": ("Shet elde oqıwdı qálegen oqıwshılar ushın: ne waqıtta ne islew kerek, arzalardı qalay qadaǵalaw hám qaysı stipendiyalar bar. Sorawıńız bolsa, mektep másláhátshisine jazıń.",
           "For students who want to study abroad: what to do and when, how to track applications, and which scholarships exist. If you have questions, write to the school counsellor.",
           "Xorijda o‘qishni xohlagan o‘quvchilar uchun: qachon nima qilish kerak, arizalarni qanday kuzatish va qaysi stipendiyalar bor. Savol bo‘lsa, maktab maslahatchisiga yozing.",
           "Для тех, кто хочет учиться за рубежом: что и когда делать, как отслеживать заявки и какие есть стипендии. Если есть вопросы, напишите школьному консультанту."),
 "stages": (
  (("9-klass", ("Qaysı mámleketler hám baǵdarlar qızıqtıratuǵının úyreniń.", "Ingliz tilin hár kúni rawajlandırıń; maqset universitetler talap etetuǵın dárejeni anıqlań.", "Bahalarıńızdı jaqsı uslań hám jumıslardı baslań: olimpiadalar, joybarlar, volonterlik.")),
   ("10-klass", ("Dárejeńizdi bilip alıw ushın dáslepki IELTS yamasa SAT sınaq testin tapsırıń.", "1–2 uzaq múddetli iske kóbirek dıqqat berip, nátiyje kórsetiń (jarıs, joybar).", "Universitetler hám stipendiyalar dizimin dúziń: kerekli testler hám múddetlerdi jazıp barıń.", "Jazǵı baǵdarlamalar hám onlayn kurslardı izleń.")),
   ("11-klass, gúz", ("IELTS/SAT tapsırıń (kerek bolsa) — qayta tapsırıwǵa waqıt qaldırıń.", "8–10 universitet tańlań: biri júdá básekili, biri real, biri isenimli.", "Muǵallimlerden usınıs xatların aldınan sorań, olarǵa jetiskenlikler dizimin beriń.", "Jeke esse qaralamasın jazıp, tekseriwge beriń.", "Kóp universitetlerde múddetler gúz benen qıs basında bolıwı múmkin, stipendiyalar tezirek jabılıwı múmkin — hárbirin házir tekseriń.")),
   ("Arzadan keyin", ("Nátiyjelerdi «Meniń arzalarım» bóliminde qadaǵalań.", "Hújjetlerdi tayarlań: pasport, awdarılǵan hám tastıyıqlanǵan attestat, finanslıq hújjetler.", "Qabıl etilgennen keyin: viza, jaylasıw, saqlandırıw hám sapar.")))
  ,
  (("Grade 9", ("Explore which countries and fields interest you.", "Build your English every day; find out the level your target universities require.", "Keep your grades strong and start activities: olympiads, projects, volunteering.")),
   ("Grade 10", ("Take a first IELTS or SAT practice test to see your level.", "Pick 1–2 long-term activities and aim for results (competitions, projects).", "Start a list of universities and scholarships; note required tests and deadlines.", "Look for summer programs and online courses.")),
   ("Grade 11, autumn", ("Take IELTS/SAT if required — leave time to retake.", "Make a list of 8–10 universities: some very competitive, some realistic, some safe.", "Ask teachers for recommendation letters early and give them your list of achievements.", "Write personal statement drafts and have them reviewed.", "Many deadlines fall between autumn and early winter, and some scholarships close earlier — check each one now.")),
   ("After applying", ("Track decisions and scholarship results in “My applications”.", "Prepare documents: passport, translated and certified transcripts, financial documents.", "After acceptance: visa, housing, insurance and travel.")))
  ,
  (("9-sinf", ("Qaysi davlatlar va yo‘nalishlar qiziqtirishini o‘rganing.", "Ingliz tilini har kuni rivojlantiring; maqsad universitetlar talab qiladigan darajani aniqlang.", "Baholaringizni yaxshi saqlang va faoliyatni boshlang: olimpiadalar, loyihalar, volontyorlik.")),
   ("10-sinf", ("Darajangizni bilish uchun dastlabki IELTS yoki SAT sinov testini topshiring.", "1–2 uzoq muddatli faoliyatga e’tibor bering va natija ko‘rsating (musobaqa, loyiha).", "Universitetlar va stipendiyalar ro‘yxatini tuzing: kerakli testlar va muddatlarni yozib boring.", "Yozgi dasturlar va onlayn kurslarni qidiring.")),
   ("11-sinf, kuz", ("IELTS/SAT topshiring (kerak bo‘lsa) — qayta topshirishga vaqt qoldiring.", "8–10 ta universitet tanlang: biri juda raqobatli, biri real, biri ishonchli.", "O‘qituvchilardan tavsiya xatlarini oldindan so‘rang, yutuqlar ro‘yxatini bering.", "Shaxsiy esse qoralamasini yozib, tekshirtiring.", "Ko‘p universitetlarda muddatlar kuz va qish boshiga to‘g‘ri kelishi mumkin, ba’zi stipendiyalar tezroq yopiladi — hozir har birini tekshiring.")),
   ("Ariza topshirgandan keyin", ("Natijalarni «Mening arizalarim» bo‘limida kuzating.", "Hujjatlarni tayyorlang: pasport, tarjima qilingan va tasdiqlangan attestat, moliyaviy hujjatlar.", "Qabul qilingach: viza, turar joy, sug‘urta va sayohat.")))
  ,
  (("9 класс", ("Узнайте, какие страны и направления вам интересны.", "Развивайте английский каждый день; выясните уровень, который требуют нужные университеты.", "Держите хорошие оценки и начните внеучебную деятельность: олимпиады, проекты, волонтёрство.")),
   ("10 класс", ("Пройдите пробный IELTS или SAT, чтобы узнать свой уровень.", "Выберите 1–2 долгосрочных занятия и добивайтесь результатов (конкурсы, проекты).", "Составьте список университетов и стипендий; записывайте нужные тесты и сроки.", "Ищите летние программы и онлайн-курсы.")),
   ("11 класс, осень", ("Сдайте IELTS/SAT, если требуется, — оставьте время на пересдачу.", "Составьте список из 8–10 университетов: очень конкурентные, реалистичные и надёжные.", "Заранее попросите учителей о рекомендательных письмах и дайте им список достижений.", "Напишите черновик личного эссе и покажите его на проверку.", "Многие дедлайны приходятся на осень и начало зимы, а некоторые стипендии закрываются раньше — проверьте каждый уже сейчас.")),
   ("После подачи", ("Отслеживайте решения и результаты стипендий в разделе «Мои заявки».", "Подготовьте документы: паспорт, переведённый и заверенный аттестат, финансовые документы.", "После зачисления: виза, жильё, страховка и поездка.")))),
 "road_h": ("Jol kartası", "Roadmap", "Yo‘l xaritasi", "Дорожная карта"),
 "road_note": ("Bul — ulıwma jol kartası. Hár universitettiń talapları hám múddetleri ózgeshe, sonlıqtan ol saytında tekserip barıń.",
               "This is a general roadmap. Every university has its own requirements and deadlines, so always check its website.",
               "Bu umumiy yo‘l xaritasi. Har bir universitetning talablari va muddatlari o‘ziga xos, shuning uchun uning saytini tekshirib boring.",
               "Это общая дорожная карта. У каждого университета свои требования и сроки, поэтому всегда проверяйте его сайт."),
 "touch_h": ("Keńes alıw", "Get advice", "Maslahat olish", "Получить консультацию"),
 "touch_p": ("Universitet saylaw, hújjetler yamasa arza boyınsha sorawıńız bolsa, mektep másláhátshisine jazıń.",
             "Questions about choosing a university, documents or applying? Write to the school counsellor.",
             "Universitet tanlash, hujjatlar yoki ariza bo‘yicha savolingiz bo‘lsa, maktab maslahatchisiga yozing.",
             "Вопросы о выборе университета, документах или подаче заявки? Напишите школьному консультанту."),
 "call": ("Qońıraw qılıw", "Call", "Qo‘ng‘iroq qilish", "Позвонить"),
 "go_tracker": ("Arzalardı qadaǵalaw →", "Track applications →", "Arizalarni kuzatish →", "Отслеживать заявки →"),
 "go_schol": ("Stipendiyalar →", "Scholarships →", "Stipendiyalar →", "Стипендии →"),
 # tracker
 "t_p": ("Universitet, mámleket hám múddetti kiritiń, soń hújjetlerdi belgilep barıń. Maǵlıwmatlar tek sizdiń telefonıńızda saqlanadı hám basqa hesh kimge kórinbeydi.",
         "Add a university, country and deadline, then tick off documents as you prepare them. Your data stays only on your phone and is not visible to anyone else.",
         "Universitet, davlat va muddatni kiriting, so‘ng hujjatlarni belgilab boring. Ma’lumotlar faqat telefoningizda saqlanadi va boshqa hech kimga ko‘rinmaydi.",
         "Добавьте университет, страну и срок, затем отмечайте готовые документы. Данные хранятся только на вашем телефоне и никому не видны."),
 "t_uni": ("Universitet", "University", "Universitet", "Университет"),
 "t_country": ("Mámleket", "Country", "Davlat", "Страна"),
 "t_dl": ("Múddeti", "Deadline", "Muddati", "Срок"),
 "t_add": ("Qosıw", "Add", "Qo‘shish", "Добавить"),
 "t_del": ("Óshiriw", "Delete", "O‘chirish", "Удалить"),
 "t_empty": ("Házirshe arza joq. Joqarıda birinshi universitetti qosıń.", "No applications yet. Add your first university above.", "Hozircha ariza yo‘q. Yuqorida birinchi universitetni qo‘shing.", "Пока нет заявок. Добавьте первый университет выше."),
 "t_days": ("{n} kún qaldı", "{n} days left", "{n} kun qoldi", "осталось дней: {n}"),
 "t_today": ("Búgin!", "Today!", "Bugun!", "Сегодня!"),
 "t_past": ("Múddet ótken", "Deadline passed", "Muddat o‘tgan", "Срок прошёл"),
 "t_done": ("tayın", "ready", "tayyor", "готово"),
 "docs": (("Pasport", "Attestat hám bahalar (awdarılǵan)", "Ingliz tili testi (IELTS/TOEFL)", "SAT (kerek bolsa)", "Usınıs xatları", "Jeke esse (personal statement)", "Jetiskenlikler dizimi (CV)", "Finanslıq hújjetler"),
          ("Passport", "Transcript (translated)", "English test (IELTS/TOEFL)", "SAT (if required)", "Recommendation letters", "Personal statement", "CV / activities list", "Financial documents"),
          ("Pasport", "Attestat va baholar (tarjima)", "Ingliz tili testi (IELTS/TOEFL)", "SAT (kerak bo‘lsa)", "Tavsiya xatlari", "Shaxsiy esse", "CV / yutuqlar ro‘yxati", "Moliyaviy hujjatlar"),
          ("Паспорт", "Аттестат и оценки (перевод)", "Тест по английскому (IELTS/TOEFL)", "SAT (если требуется)", "Рекомендательные письма", "Личное эссе", "CV / список достижений", "Финансовые документы")),
 # scholarships
 "s_p": ("Төмендегi stipendiyalar boyınsha maǵlıwmat rásmiy saytlardan alındı. Qaǵıydalar, summa hám múddetler hár jılı ózgeredi — arza beriwden aldın rásmiy saytta tekserip alıń.",
         "The information below comes from the official websites. Rules, amounts and deadlines change every year — always confirm on the official site before you apply.",
         "Quyidagi ma’lumotlar rasmiy saytlardan olindi. Qoidalar, summa va muddatlar har yili o‘zgaradi — ariza topshirishdan oldin rasmiy saytda tekshiring.",
         "Информация ниже взята с официальных сайтов. Правила, суммы и сроки меняются каждый год — перед подачей всегда проверяйте официальный сайт."),
 "s_site": ("Rásmiy sayt →", "Official site →", "Rasmiy sayt →", "Официальный сайт →"),
 "s_checked": ("Sońǵı tekseriw: 2026-jıl noyabr", "Last checked: November 2026", "Oxirgi tekshiruv: 2026-yil noyabr", "Последняя проверка: ноябрь 2026"),
 "s_more": ("Basqa imkaniyatlar: universitetlerdiń óz stipendiyaları hám finanslıq járdemi (AQSh, Uлken Britaniya, Evropa). Hár universitettiń «financial aid» bólimin tekseriń.",
            "Other options: universities’ own scholarships and financial aid (USA, UK, Europe). Check each university’s “financial aid” page.",
            "Boshqa imkoniyatlar: universitetlarning o‘z stipendiyalari va moliyaviy yordami (AQSh, Buyuk Britaniya, Yevropa). Har bir universitetning «financial aid» bo‘limini tekshiring.",
            "Другие возможности: собственные стипендии и финансовая помощь университетов (США, Великобритания, Европа). Проверяйте раздел «financial aid» каждого университета."),
}
T["s_p"] = tuple(x.replace("Төмендегi", "Tómendegi") for x in T["s_p"])
T["s_more"] = tuple(x.replace("Uлken", "Ullı") for x in T["s_more"])
SCHOL = [  # url, (country x4), (level x4), (covers x4), (note x4)
 ("https://turkiyeburslari.gov.tr/en",
  ("Túrkiya", "Turkey", "Turkiya", "Турция"), "Türkiye Bursları",
  ("Bakalavr, magistr, PhD", "Bachelor’s, master’s, PhD", "Bakalavr, magistratura, PhD", "Бакалавриат, магистратура, PhD"),
  ("Universitet hám qánigelik tańlaw, aylıq stipendiya, oqıw haqı, densawlıqtı saqlandırıw, jataqxana, túrk tili kursı, bir mártelik awıa bilet", "University placement, monthly stipend, tuition, health insurance, accommodation, Turkish language course, one-time flight ticket",
   "Universitet va mutaxassislik tanlash, oylik stipendiya, o‘qish to‘lovi, tibbiy sug‘urta, yotoqxona, turk tili kursi, bir martalik aviachipta", "Подбор университета и специальности, ежемесячная стипендия, оплата обучения, мед. страховка, жильё, курс турецкого языка, один авиабилет"),
  ("Arzalar onlayn hám biypul tapsırıladı. Múddetlerdi rásmiy kalendarda tekseriń.", "Applications are online and free. Check dates in the official calendar.", "Arizalar onlayn va bepul topshiriladi. Muddatlarni rasmiy kalendarda tekshiring.", "Заявки подаются онлайн и бесплатно. Сроки смотрите в официальном календаре.")),
 ("https://stipendiumhungaricum.hu/",
  ("Vengriya", "Hungary", "Vengriya", "Венгрия"), "Stipendium Hungaricum",
  ("Bakalavr hám basqa dárejeler (qatnasıwshı universitetlerde)", "Bachelor’s and other degrees (at participating universities)", "Bakalavr va boshqa darajalar (ishtirokchi universitetlarda)", "Бакалавриат и другие уровни (в участвующих университетах)"),
  ("Oqıw haqı toliq jabıladı, jataqxana bólek qollap-quwatlanadı", "Tuition fully covered, accommodation partly supported", "O‘qish to‘lovi to‘liq qoplanadi, yotoqxona qisman qo‘llab-quvvatlanadi", "Обучение оплачивается полностью, жильё частично"),
  ("Qabıllaw jılına bir ret ashıladı. Rásmiy saytta házirgi jıl jabıq dep kórsetilgen bolıwı múmkin — keler jıl shaqırıwın baqlań.", "Applications open once a year. The site may show the current year as closed — watch for next year’s call.",
   "Qabul yiliga bir marta ochiladi. Rasmiy saytda joriy yil yopiq deb ko‘rsatilgan bo‘lishi mumkin — keyingi yil e’lonini kuzating.", "Приём открывается раз в год. На сайте текущий год может быть закрыт — следите за объявлением на следующий год.")),
 ("https://www.campuschina.org",
  ("Qıtay", "China", "Xitoy", "Китай"), "Chinese Government Scholarship (CSC)",
  ("Bakalavr hám joqarı dárejeler", "Bachelor’s and higher", "Bakalavr va yuqori darajalar", "Бакалавриат и выше"),
  ("Oqıw haqınan azat etiw, jataqxana yamasa kompensaciya, aylıq stipendiya, densawlıqtı saqlandırıw", "Tuition waiver, dormitory or housing subsidy, monthly stipend, medical insurance",
   "O‘qish to‘lovidan ozod qilish, yotoqxona yoki kompensatsiya, oylik stipendiya, tibbiy sug‘urta", "Освобождение от платы за обучение, общежитие или компенсация, ежемесячная стипендия, мед. страховка"),
  ("Xabarlarǵa qaraǵanda, 2026/2027 oqıw jılınan bakalavr talapkerleri CSCA testin tapsırıwı kerek. Aniqlıq ushın rásmiy saytqa qarań.", "Reports say undergraduate applicants must take the CSCA test starting with 2026/2027. Confirm on the official site.",
   "Xabarlarga ko‘ra, 2026/2027 o‘quv yilidan bakalavr abituriyentlari CSCA testini topshirishi kerak. Aniqlik uchun rasmiy saytga qarang.", "По сообщениям, с 2026/2027 учебного года абитуриенты бакалавриата должны сдавать тест CSCA. Уточняйте на официальном сайте.")),
 ("https://www.studyinjapan.go.jp/en/planning/about-scholarship/",
  ("Yaponiya", "Japan", "Yaponiya", "Япония"), "MEXT (Japanese Government Scholarship)",
  ("Bakalavr bóleginde bar", "Undergraduate track available", "Bakalavr yo‘nalishi mavjud", "Есть программа для бакалавриата"),
  ("Tolıq shártler rásmiy derekte kórsetilmegen; stipendiyalar kóbinese bólekshe qollap-quwatlaw boladı", "Details are on the official sources; scholarships are often partial support",
   "Batafsil shartlar rasmiy manbalarda; stipendiyalar ko‘pincha qisman yordam bo‘ladi", "Подробности в официальных источниках; стипендии часто покрывают лишь часть расходов"),
  ("Eki jol bar: Yaponiya elshixanası arqalı yamasa universitet arqalı. Talaplar hám múddetler ushın elshixanadan sorań.", "There are two routes: through the Japanese embassy or through a university. Ask the embassy for requirements and dates.",
   "Ikki yo‘l bor: Yaponiya elchixonasi orqali yoki universitet orqali. Talablar va muddatlar uchun elchixonadan so‘rang.", "Есть два пути: через посольство Японии или через университет. Требования и сроки уточняйте в посольстве.")),
 ("https://www.studyinkorea.go.kr",
  ("Koreya", "South Korea", "Janubiy Koreya", "Южная Корея"), "Global Korea Scholarship (GKS)",
  ("Rásmiy saytta tekseriń", "See the official site", "Rasmiy saytda tekshiring", "См. официальный сайт"),
  ("Koreya húkimeti stipendiyası; sharayatlar hám dárejeler rásmiy saytta", "Korean government scholarship; terms and degree levels are on the official site", "Koreya hukumati stipendiyasi; shartlar va darajalar rasmiy saytda", "Стипендия правительства Кореи; условия и уровни — на официальном сайте"),
  ("Jas sheklewi, orta ball hám múddetler jıl sayın ózgeredi — rásmiy saytta tekseriń.", "Age limits, GPA and dates change every year — check the official site.", "Yosh chegarasi, o‘rtacha ball va muddatlar yil sayin o‘zgaradi — rasmiy saytda tekshiring.", "Возрастные ограничения, средний балл и сроки меняются каждый год — смотрите на официальном сайте."))
]
JS = r"""
(function(){
 var $=function(i){return document.getElementById(i)},K='abroadApps',D=JSON.parse($('abdata').textContent);
 var apps=[];try{apps=JSON.parse(localStorage.getItem(K)||'[]')}catch(e){}
 var save=function(){try{localStorage.setItem(K,JSON.stringify(apps))}catch(e){}};
 var esc=function(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
 function days(d){var t=new Date();t.setHours(0,0,0,0);return Math.round((new Date(d+'T00:00:00')-t)/864e5)}
 function draw(){
  $('ablist').innerHTML=apps.length?apps.map(function(a,i){
   var n=days(a.d),cls=n<0?'past':n<=14?'soon':'',txt=isNaN(n)?'':(n<0?D.past:n===0?D.today:D.days.replace('{n}',n));
   var done=a.c.filter(Boolean).length;
   return '<div class="card abapp '+cls+'"><div class="abtop"><div><b>'+esc(a.u)+'</b><small>'+esc(a.k||'')+(a.d?' · '+a.d:'')+'</small></div><span class="abdays">'+txt+'</span></div>'
    +'<div class="pbar" style="--sc:#0b5f78"><i style="width:'+Math.round(done/D.docs.length*100)+'%"></i></div><small>'+done+'/'+D.docs.length+' '+D.done+'</small>'
    +'<div class="abdocs">'+D.docs.map(function(x,j){return '<label><input type="checkbox" data-i="'+i+'" data-j="'+j+'"'+(a.c[j]?' checked':'')+'> '+esc(x)+'</label>'}).join('')+'</div>'
    +'<button type="button" class="abdel" data-i="'+i+'">'+D.del+'</button></div>'}).join(''):'<p class="note">'+D.empty+'</p>';
 }
 $('ablist').addEventListener('change',function(e){var t=e.target;if(t.type==='checkbox'){apps[+t.dataset.i].c[+t.dataset.j]=t.checked;save();draw()}});
 $('ablist').addEventListener('click',function(e){var t=e.target;if(t.classList.contains('abdel')){apps.splice(+t.dataset.i,1);save();draw()}});
 $('abform').addEventListener('submit',function(e){e.preventDefault();var u=$('abu').value.trim();if(!u)return;
  apps.push({u:u,k:$('abk').value.trim(),d:$('abd').value,c:D.docs.map(function(){return false})});apps.sort(function(a,b){return (a.d||'9')<(b.d||'9')?-1:1});save();this.reset();draw()});
 draw();
})();
"""

def tabs(sub, lang, i, href):
    items = "".join(f'<a href="{href(k)}"' + (' aria-current="page"' if k == sub else "") + f'><span class="mi" style="--mc:{TAB_ICON[k][1]}">{TAB_ICON[k][0]}</span>{v[1][i]}</a>' for k, v in TABS.items())
    return f'<nav class="abtabs" aria-label="{NAME[i]}">{items}</nav>'

def body(sub, lang, i, t, href, ctx):
    tb = tabs(sub, lang, i, href)
    if sub == "abroad/":
        stages = "".join(f'<li class="stage"><h3>{h}</h3><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul></li>' for h, xs in T["stages"][i])
        return (f'{tb}{PL.banner(i, href("abroad/plan/"))}<p class="lead2">{T["intro"][i]}</p><h2>{T["road_h"][i]}</h2><ol class="road">{stages}</ol><p class="note">{T["road_note"][i]}</p>'
                f'<div class="btns"><a class="btn p" href="{href("abroad/applications/")}">{T["go_tracker"][i]}</a><a class="btn s" href="{href("abroad/scholarships/")}">{T["go_schol"][i]}</a></div>'
                f'<h2 style="margin-top:34px">{T["touch_h"][i]}</h2><p>{T["touch_p"][i]}</p><div class="btns"><a class="btn p" href="tel:{ctx["PHONE"]}">{T["call"][i]} {ctx["PHONE_TXT"]}</a>'
                f'<a class="btn s" href="{ctx["TG"]}" rel="noopener">Telegram</a></div>')
    if sub == "abroad/plan/":
        return PL.body(i, tb, href)
    if sub == "abroad/sat/":
        import achieve as ACH
        return SAT.body(i, tb + ACH.sat_banner(i, href("achievements/sat/")))
    if sub == "abroad/essay/":
        return ESS.body(i, tb, href)
    if sub == "abroad/calculator/":
        return CAL.body(i, tb)
    if sub == "abroad/checklist/":
        return CKL.body(i, tb)
    if sub == "abroad/calendar/":
        return DLN.body(i, tb)
    if sub == "abroad/countries/":
        nxt = "".join(f'<a class="uofficial" style="margin-right:18px" href="{href(k)}">{TABS[k][1][i]} →</a>' for k in ("abroad/scholarships/", "abroad/top10/", "ielts/"))
        return CO.body(i, tb, f'<div class="card gapp"><h3>{CO.X["next"][i]}</h3>{nxt}</div>')
    if sub in AP.NAME:
        return AP.body(sub, i, tb)
    if sub == "abroad/top10/":
        return TP.body(i, tb)
    if sub == "abroad/applications/":
        data = {"docs": list(T["docs"][i]), "days": T["t_days"][i], "today": T["t_today"][i], "past": T["t_past"][i], "done": T["t_done"][i], "del": T["t_del"][i], "empty": T["t_empty"][i]}
        return (f'{tb}<p class="lead2">{T["t_p"][i]}</p><form id="abform" class="card abform"><label>{T["t_uni"][i]}<input id="abu" required maxlength="80"></label>'
                f'<label>{T["t_country"][i]}<input id="abk" maxlength="40"></label><label>{T["t_dl"][i]}<input id="abd" type="date"></label>'
                f'<button class="btn p" type="submit">{T["t_add"][i]}</button></form><div id="ablist" class="ablist"></div>'
                f'<script id="abdata" type="application/json">{json.dumps(data, ensure_ascii=False)}</script><script>{JS}</script>')
    # scholarships
    cards = ""
    for url, ctry, name, lvl, cov, note in SCHOL:
        cards += (f'<article class="card sch"><div class="schtop"><span class="cchip">{ctry[i]}</span><h3>{name}</h3></div>'
                  f'<p><b>{lvl[i]}</b></p><p>{cov[i]}</p><p class="note">{note[i]}</p><a href="{url}" rel="noopener">{T["s_site"][i]}</a></article>')
    return f'{tb}<p class="lead2">{T["s_p"][i]}</p><div class="grid2">{cards}</div><p style="margin-top:18px">{T["s_more"][i]}</p><p class="note">{T["s_checked"][i]}</p>'
