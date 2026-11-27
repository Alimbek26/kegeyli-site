# "International goals 2026–2027": the public version of the school's 12-month plan for international recognition.
SUB = "international/"
NAME = ("Xalıqaralıq maqsetlerimiz", "Our international goals", "Xalqaro maqsadlarimiz", "Наши международные цели")
DESC = ("2027-jıl noyabrge shekem: shet elde oqıytuǵın pitkeriwshiler, sherik mektep, xalıqaralıq jarıslar hám College Board kodı.",
        "By November 2027: graduates studying abroad, a partner school, international competitions and a College Board code.",
        "2027-yil noyabrgacha: xorijda o‘qiydigan bitiruvchilar, hamkor maktab, xalqaro musobaqalar va College Board kodi.",
        "К ноябрю 2027 года: выпускники за рубежом, школа-партнёр, международные конкурсы и код College Board.")
L = lambda a, b, c, d: (a, b, c, d)
T = dict(
 lead=L("Maqsetimiz: 2027-jıl noyabrge shekem shet eldegi universitetler hám sheriklerimiz mektebimizdi atı menen tanıwı. Bul — 12 aylıq jobamız.",
        "Our goal: by November 2027, universities and partners abroad know our school by name. This is our 12-month plan.",
        "Maqsadimiz: 2027-yil noyabrgacha xorijdagi universitetlar va hamkorlar maktabimizni nomidan tanishi. Bu — 12 oylik rejamiz.",
        "Наша цель: к ноябрю 2027 года университеты и партнёры за рубежом знают нашу школу по имени. Это наш план на 12 месяцев."),
 now_h=L("Biz qay jerdemiz", "Where we are now", "Biz qayerdamiz", "Где мы сейчас"),
 dir_h=L("Bes baǵdar", "Five directions", "Besh yo‘nalish", "Пять направлений"),
 plan_h=L("Jıl boyınsha jobası", "The year, phase by phase", "Yil davomida reja", "План по этапам"),
 tgt_h=L("2027-jıl noyabrge maqsetler", "Targets for November 2027", "2027-yil noyabrga maqsadlar", "Цели к ноябрю 2027 года"),
 measure=L("Kórsetkish", "Measure", "Ko‘rsatkich", "Показатель"), now=L("Házir", "Now", "Hozir", "Сейчас"), target=L("Maqset", "Target", "Maqsad", "Цель"),
 part_h=L("Shet eldegi mektepler hám universitetler ushın", "For schools and universities abroad", "Xorijdagi maktab va universitetlar uchun", "Для школ и университетов за рубежом"),
 part_p=L("Sheriklik, onlayn sabaqlar, almasıw yamasa oqıwshılarımız haqqında sorawlar ushın mektep konsultantına jazıń.",
          "For partnerships, online lessons, exchanges or questions about our students, write to the school counselor.",
          "Hamkorlik, onlayn darslar, almashinuv yoki o‘quvchilarimiz haqida savollar uchun maktab maslahatchisiga yozing.",
          "По вопросам партнёрства, онлайн-уроков, обменов или о наших учениках пишите школьному консультанту."),
 counselor=L("Alimbek Jumamuratov, mektep konsultantı", "Alimbek Jumamuratov, School Counselor", "Alimbek Jumamuratov, maktab maslahatchisi", "Алимбек Жумамуратов, школьный консультант"),
 profile=L("Mektep profili (PDF)", "School Profile (PDF)", "Maktab profili (PDF)", "Профиль школы (PDF)"),
 offers=L("Shet el universitetleriniń usınısları", "Offers from universities abroad", "Xorijiy universitetlar takliflari", "Предложения зарубежных университетов"),
)
NOW = [  # (number, label)
 ("10", L("shet el universitetleriniń qabıl usınısı (2025)", "offers from universities abroad (2025)", "ta xorijiy universitet taklifi (2025)", "предложений от зарубежных университетов (2025)")),
 ("2", L("dúnyanıń top-100 universiteti (QS)", "world top-100 universities (QS)", "ta dunyo top-100 universiteti (QS)", "университета из топ-100 мира (QS)")),
 ("1440", L("eń joqarı SAT ballı", "best SAT score", "eng yuqori SAT bali", "лучший балл SAT")),
 ("97%", L("pitkeriwshi oqıwın dawam etedi (2023–2026)", "of graduates continue studying (2023–2026)", "bitiruvchi o‘qishni davom ettiradi (2023–2026)", "выпускников продолжают учёбу (2023–2026)")),
]
DIRS = [  # (colour, title, three points)
 ("#0b5f78", L("College Board", "College Board", "College Board", "College Board"),
  [L("CEEB kodı", "CEEB school code", "CEEB kodi", "Код CEEB"), L("Mektep profili hár arzada", "School Profile with every application", "Har arizada maktab profili", "Профиль школы в каждой заявке"), L("Jıl sayın jańalanadı", "Updated every year", "Har yili yangilanadi", "Обновляется каждый год")]),
 ("#2563eb", L("Shet elde oqıw", "Study abroad", "Xorijda o‘qish", "Учёба за рубежом"),
  [L("10-klasstan tayarlıq", "Preparation from Grade 10", "10-sinfdan tayyorgarlik", "Подготовка с 10 класса"), L("Grantlı usınıslar", "Offers with full or large grants", "Grantli takliflar", "Предложения с грантами"), L("Shet eldegi birinshi studentlerimiz", "Our first graduates studying abroad", "Xorijdagi birinchi talabalarimiz", "Первые выпускники за рубежом")]),
 ("#d97706", L("Jarıslar", "Competitions", "Musobaqalar", "Конкурсы"),
  [L("Xalıqaralıq olimpiadalar", "International olympiads", "Xalqaro olimpiadalar", "Международные олимпиады"), L("Ilim jármeńkeleri", "Science fairs", "Ilmiy ko‘rgazmalar", "Научные ярмарки"), L("Komandalıq jarıslar", "Team competitions", "Jamoaviy musobaqalar", "Командные конкурсы")]),
 ("#16a34a", L("Baylanıslar", "Connections", "Aloqalar", "Связи"),
  [L("Shet eldegi sherik mektep", "A partner school abroad", "Xorijdagi hamkor maktab", "Школа-партнёр за рубежом"), L("Almasıw programmaları", "Exchange programmes", "Almashinuv dasturlari", "Программы обмена"), L("Jazǵı mektepler", "Summer schools", "Yozgi maktablar", "Летние школы")]),
 ("#7c3aed", L("Kóriniw", "Visibility", "Ko‘rinish", "Видимость"),
  [L("Hár ay jańalıqlar", "News every month", "Har oy yangiliklar", "Новости каждый месяц"), L("Inglis tilinde LinkedIn betı", "LinkedIn page in English", "Ingliz tilida LinkedIn sahifasi", "Страница в LinkedIn на английском"), L("Google profili", "Google Business Profile", "Google profili", "Профиль в Google")]),
]
PHASES = [  # (months, title, points)
 (L("Dekabr – fevral", "December – February", "Dekabr – fevral", "Декабрь – февраль"), L("Tiykar", "Foundations", "Poydevor", "Основа"),
  [L("CEEB kodı saytta hám profilde", "CEEB code on the website and profile", "CEEB kodi saytda va profilda", "Код CEEB на сайте и в профиле"),
   L("10-klass oqıwshıları menen ata-analar ushırasıwı", "Grade 10 applicants chosen; parents informed", "10-sinf nomzodlari tanlanadi; ota-onalar bilan uchrashuv", "Выбор кандидатов из 10 класса; встреча с родителями"),
   L("5 shet el mektebine sheriklik usınısı", "Partnership letters to 5 schools abroad", "5 ta xorijiy maktabga hamkorlik taklifi", "Письма о партнёрстве в 5 школ за рубежом")]),
 (L("Mart – may", "March – May", "Mart – may", "Март – май"), L("Tayarlıq", "Preparation", "Tayyorgarlik", "Подготовка"),
  [L("SAT hám IELTS toparı, háptesine 2 ret", "SAT and IELTS group, twice a week", "SAT va IELTS guruhi, haftasiga 2 marta", "Группа SAT и IELTS дважды в неделю"),
   L("Jazǵı mekteplerge arzalar", "Applications to summer schools", "Yozgi maktablarga arizalar", "Заявки в летние школы"),
   L("Bir xalıqaralıq jarısqa qatnasıw; sherik mektep", "One international competition; a partner school", "Bitta xalqaro musobaqa; hamkor maktab", "Один международный конкурс; школа-партнёр")]),
 (L("Iyun – avgust", "June – August", "Iyun – avgust", "Июнь – август"), L("Testler", "Tests", "Testlar", "Тесты"),
  [L("2027–2028 ushın mektep profili", "School Profile for 2027–2028", "2027–2028 uchun maktab profili", "Профиль школы на 2027–2028"),
   L("IELTS hám SAT; universitetler dizimi", "IELTS and SAT; a university list for each student", "IELTS va SAT; har bir o‘quvchiga universitetlar ro‘yxati", "IELTS и SAT; список университетов для каждого"),
   L("Sherik mektep penen birinshi joybar", "First project with the partner school", "Hamkor maktab bilan birinchi loyiha", "Первый проект со школой-партнёром")]),
 (L("Sentyabr – noyabr", "September – November", "Sentabr – noyabr", "Сентябрь – ноябрь"), L("Arzalar", "Applications", "Arizalar", "Заявки"),
  [L("Esseler hám usınıs xatları", "Essays and recommendation letters", "Esselar va tavsiyanomalar", "Эссе и рекомендательные письма"),
   L("Erte arzalar mektep profili menen", "Early applications, each with the School Profile", "Erta arizalar maktab profili bilan", "Ранние заявки с профилем школы"),
   L("Nátiyjelerdi bahalaw, 2028 jobası", "Review results; plan for 2028", "Natijalarni baholash, 2028 rejasi", "Итоги и план на 2028 год")]),
]
TARGETS = [
 (L("Grant penen shet elde oqıytuǵın pitkeriwshiler", "Graduates studying abroad with a grant", "Grant bilan xorijda o‘qiydigan bitiruvchilar", "Выпускники за рубежом с грантом"), "0", "1–3"),
 (L("Shet elge arza beretuǵın oqıwshılar", "Students applying abroad", "Xorijga ariza beradigan o‘quvchilar", "Учеников подают заявки за рубеж"), "3", "8–10"),
 (L("SAT tapsırǵan pitkeriwshiler (jılına)", "Graduates with an SAT score (per year)", "SAT topshirgan bitiruvchilar (yiliga)", "Выпускников с баллом SAT (в год)"), "2", "8"),
 (L("IELTS sertifikatı bar pitkeriwshiler (jılına)", "Graduates with IELTS (per year)", "IELTS sertifikatli bitiruvchilar (yiliga)", "Выпускников с IELTS (в год)"), "4", "10"),
 (L("Xalıqaralıq jarıslar", "International competitions entered", "Xalqaro musobaqalar", "Международных конкурсов"), "0", "2"),
 (L("Shet eldegi sherik mektepler", "Partner schools abroad", "Xorijdagi hamkor maktablar", "Школ-партнёров за рубежом"), "0", "1"),
 (L("College Board kodı", "College Board code", "College Board kodi", "Код College Board"),
  L("Arza berildi", "Applied for", "Ariza berildi", "Подана заявка"), L("Saytta", "On the website", "Saytda", "На сайте")),
]


def body(i, up, href, email):
    v = lambda x: x[i] if isinstance(x, tuple) else x
    now = "".join(f'<div class="card ianow"><b>{n}</b><span>{l[i]}</span></div>' for n, l in NOW)
    dirs = "".join(f'<div class="card iadir" style="--dc:{c}"><h3>{t[i]}</h3><ul>' + "".join(f"<li>{p[i]}</li>" for p in ps) + "</ul></div>" for c, t, ps in DIRS)
    phases = "".join(f'<li class="card iaph"><span class="iam">{m[i]}</span><h3><b>{k + 1}</b> {t[i]}</h3><ul>' + "".join(f"<li>{p[i]}</li>" for p in ps) + "</ul></li>"
                     for k, (m, t, ps) in enumerate(PHASES))
    rows = "".join(f"<tr><td>{m[i]}</td><td>{v(a)}</td><td><b>{v(b)}</b></td></tr>" for m, a, b in TARGETS)
    return (f'<p class="lead2">{T["lead"][i]}</p>'
            f'<h2>{T["now_h"][i]}</h2><div class="ianows">{now}</div>'
            f'<p class="btns" style="margin-bottom:30px"><a class="btn s" href="{href("achievements/offers/")}">{T["offers"][i]} →</a></p>'
            f'<h2>{T["dir_h"][i]}</h2><div class="iadirs">{dirs}</div>'
            f'<h2>{T["plan_h"][i]}</h2><ol class="iaphs">{phases}</ol>'
            f'<h2>{T["tgt_h"][i]}</h2><div class="tablewrap"><table class="iatgt"><thead><tr><th>{T["measure"][i]}</th><th>{T["now"][i]}</th><th>{T["target"][i]}</th></tr></thead><tbody>{rows}</tbody></table></div>'
            f'<div class="card ofcta iapart"><div><h3>{T["part_h"][i]}</h3><p>{T["part_p"][i]}</p><p><b>{T["counselor"][i]}</b> · <a href="mailto:{email}">{email}</a></p></div>'
            f'<a class="btn p" href="{up}school-profile/">{T["profile"][i]} →</a></div>')
