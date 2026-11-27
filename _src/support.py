# "Support our students": how local businesses and organisations can help (4 languages).
SUB = "support/"
L = lambda a, b, c, d: (a, b, c, d)
NAME = L("Oqıwshılarımızǵa qollaw", "Support our students", "O‘quvchilarimizni qo‘llab-quvvatlang", "Поддержите наших учеников")
DESC = L("Kárxanalar hám shólkemler mektebimiz oqıwshılarına qalay járdem bere aladı: test tólemleri, sayaxatlar, kásip haqqında sáwbetler, sıylıqlar.",
         "How businesses and organisations can help our students: test fees, visits, career talks, prizes and equipment.",
         "Korxona va tashkilotlar o‘quvchilarimizga qanday yordam bera oladi: test to‘lovlari, tashriflar, kasb suhbatlari, sovrinlar.",
         "Как компании и организации могут помочь нашим ученикам: оплата тестов, визиты, беседы о профессиях, призы и оборудование.")
T = dict(
 lead=L("Kegeyli rayonı qánigelestirilgen mektebinde 380-ge jaqın talantlı oqıwshı aniq hám tábiyiy pánlerdi tereń úyrenedi. Pitkeriwshilerimiz AQSh hám Ullı Britaniya universitetlerinen, sonıń ishinde dúnyanıń top-100 universitetlerinen usınıslar aldı. Siziń járdemińiz olarǵa jáne de úlken imkaniyatlar ashadı.",
        "About 380 talented students study exact and natural sciences in depth at Kegeyli District Specialized School. Our graduates have received offers from universities in the USA and the UK, including two in the world top 100. Your support opens even bigger doors for them.",
        "Kegeyli tumani ixtisoslashtirilgan maktabida 380 ga yaqin iqtidorli o‘quvchi aniq va tabiiy fanlarni chuqur o‘rganadi. Bitiruvchilarimiz AQSh va Buyuk Britaniya universitetlaridan, jumladan dunyoning top-100 universitetlaridan takliflar oldi. Sizning yordamingiz ularga yanada katta imkoniyatlar ochadi.",
        "В Кегейлийской районной специализированной школе около 380 талантливых учеников углублённо изучают точные и естественные науки. Наши выпускники получили предложения от университетов США и Великобритании, в том числе двух из мирового топ-100. Ваша поддержка откроет им ещё больше возможностей."),
 ways_h=L("Qalay járdem beriw múmkin", "How you can help", "Qanday yordam berish mumkin", "Чем можно помочь"),
 get_h=L("Sheriklerimiz ne aladı", "What partners receive", "Hamkorlarimiz nima oladi", "Что получают партнёры"),
 how_h=L("Qalay islenedi", "How it works", "Qanday ishlaydi", "Как это работает"),
 note=L("Barlıq qollaw mekteptiń rásmiy tártibi arqalı rásmiylestiriledi hám tek kelisilgen maqsetke jumsaladı (mısalı, test tólemi tikkeley test orayına tólenedi).",
        "All support is arranged through the school’s official procedures and used only for the agreed purpose (for example, a test fee is paid directly to the test centre).",
        "Barcha yordam maktabning rasmiy tartibi orqali rasmiylashtiriladi va faqat kelishilgan maqsadga sarflanadi (masalan, test to‘lovi to‘g‘ridan-to‘g‘ri test markaziga to‘lanadi).",
        "Вся поддержка оформляется через официальные процедуры школы и идёт только на согласованную цель (например, оплата теста перечисляется напрямую в тестовый центр)."),
 contact_h=L("Baylanıs", "Get in touch", "Bog‘lanish", "Связаться"),
 counselor=L("Alimbek Jumamuratov, mektep konsultantı", "Alimbek Jumamuratov, School Counselor", "Alimbek Jumamuratov, maktab maslahatchisi", "Алимбек Жумамуратов, школьный консультант"),
 partners=L("Házirgi sheriklerimiz", "Our current partners", "Hozirgi hamkorlarimiz", "Наши партнёры"),
 profile=L("Mektep profili (PDF)", "School Profile (PDF)", "Maktab profili (PDF)", "Профиль школы (PDF)"),
)
WAYS = [  # (icon path, colour, title, text)
 ('<path d="M4 4h16v16H4z"/><path d="M8 9h8M8 13h5"/><circle cx="17" cy="17" r="3"/>', "#2563eb",
  L("SAT hám IELTS tólemleri", "SAT and IELTS fees", "SAT va IELTS to‘lovlari", "Оплата SAT и IELTS"),
  L("Eń kúshli oqıwshılardıń xalıqaralıq test tólemin qaplań — bul shet el universitetlerine jol ashatuǵın birinshi qádem.",
    "Cover the international test fee of a top student: the first step towards universities abroad.",
    "Eng kuchli o‘quvchilarning xalqaro test to‘lovini qoplang — bu xorijiy universitetlarga yo‘l ochuvchi birinchi qadam.",
    "Оплатите международный тест сильному ученику — первый шаг к зарубежным университетам.")),
 ('<path d="M3 21h18"/><path d="M5 21V9l7-5 7 5v12"/><path d="M10 21v-5h4v5"/>', "#16a34a",
  L("Kárxanaǵa sayaxat", "Host a student visit", "Korxonaga tashrif", "Экскурсия на предприятие"),
  L("Oqıwshılarǵa óndiristi, laboratoriyanı yamasa IT-komandanı kórsetiń: pán turmısta qalay islewin óz kózi menen kórsin.",
    "Show students your production line, lab or IT team, so they see how science works in real life.",
    "O‘quvchilarga ishlab chiqarish, laboratoriya yoki IT-jamoangizni ko‘rsating: fan hayotda qanday ishlashini o‘z ko‘zi bilan ko‘rsin.",
    "Покажите ученикам производство, лабораторию или IT-команду — пусть увидят, как наука работает в жизни.")),
 ('<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>', "#d97706",
  L("Kásip haqqında sáwbet", "Career talk or mentoring", "Kasb haqida suhbat", "Беседа о профессии"),
  L("Óz kásibińiz hám jolıńız haqqında 10–11-klass oqıwshılarına aytıp beriń yamasa bir oqıwshıǵa mentor bolıń.",
    "Tell Grade 10–11 students about your profession and path, or mentor one student through the year.",
    "Kasbingiz va yo‘lingiz haqida 10–11-sinf o‘quvchilariga so‘zlab bering yoki bir o‘quvchiga murabbiy bo‘ling.",
    "Расскажите ученикам 10–11 классов о своей профессии и пути или станьте наставником для одного ученика.")),
 ('<circle cx="12" cy="15" r="6"/><path d="M8.5 10.2L5 3h4l3 6 3-6h4l-3.5 7.2"/>', "#a3202c",
  L("Olimpiada sıylıqları hám saparlar", "Olympiad prizes and travel", "Olimpiada sovrinlari va safarlar", "Призы олимпиад и поездки"),
  L("Olimpiada jeńimpazlarına sıylıq yamasa xalıqaralıq jarısqa, sherik mektepke barıw jol qárejetlerin qollań.",
    "Fund prizes for olympiad winners, or travel to international competitions and our partner school.",
    "Olimpiada g‘oliblariga sovrin yoki xalqaro musobaqa va hamkor maktabga borish yo‘l xarajatlarini qo‘llab-quvvatlang.",
    "Поддержите призы победителям олимпиад или поездки на международные конкурсы и в школу-партнёр.")),
 ('<path d="M9 3h6"/><path d="M10 3v6L4.5 19a1.5 1.5 0 0 0 1.3 2.2h12.4a1.5 1.5 0 0 0 1.3-2.2L14 9V3"/>', "#7c3aed",
  L("Úskeneler hám kitaplar", "Equipment and books", "Jihozlar va kitoblar", "Оборудование и книги"),
  L("Laboratoriya, robototexnika yamasa kitapxana ushın úskene hám kitaplar menen járdem beriń.",
    "Help with lab or robotics equipment, or books for the school library.",
    "Laboratoriya, robototexnika yoki kutubxona uchun jihoz va kitoblar bilan yordam bering.",
    "Помогите оборудованием для лабораторий и робототехники или книгами для библиотеки.")),
 ('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>', "#0b5f78",
  L("Jazǵı praktika", "Summer project or internship", "Yozgi amaliyot", "Летняя практика"),
  L("10–11-klass oqıwshılarına jazda qısqa joybar yamasa praktika usınıń — bul olardıń universitet arzalarında kúshli tárep boladı.",
    "Offer Grade 10–11 students a short summer project or internship: a strong point in their university applications.",
    "10–11-sinf o‘quvchilariga yozda qisqa loyiha yoki amaliyot taklif qiling — bu ularning universitet arizalarida kuchli tomon bo‘ladi.",
    "Предложите ученикам 10–11 классов короткий летний проект или практику — сильный пункт в их заявках в университеты.")),
]
GET = [
 L("Logotipińiz saytımızdaǵı sheriklerimiz qatarında (ruxsatıńız benen)", "Your logo among our partners on the website (with your permission)", "Logotipingiz saytimizdagi hamkorlarimiz qatorida (ruxsatingiz bilan)", "Ваш логотип среди партнёров на сайте (с вашего согласия)"),
 L("Jańalıqlarda hám Telegram kanalımızda alǵıs", "A thank-you in our news and on our Telegram channel", "Yangiliklarimiz va Telegram kanalimizda minnatdorchilik", "Благодарность в новостях и в нашем Telegram-канале"),
 L("Nátiyje haqqında esabat: fotolar hám oqıwshılardıń jetiskenlikleri", "A short report on the result: photos and what students achieved", "Natija haqida hisobot: suratlar va o‘quvchilar yutuqlari", "Короткий отчёт о результате: фото и достижения учеников"),
 L("Mektep atınan alǵıs xatı", "A letter of thanks from the school", "Maktab nomidan minnatdorchilik xati", "Благодарственное письмо от школы"),
]
HOW = [
 L("Bizge jazıń yamasa qońıraw etiń — ne usınıwıńız múmkin ekenin aytıń.", "Write or call us and tell us what you could offer.", "Bizga yozing yoki qo‘ng‘iroq qiling — nima taklif qila olishingizni ayting.", "Напишите или позвоните нам и расскажите, что вы могли бы предложить."),
 L("Bizler birge maqset, waqıt hám kólemdi kelisemiz.", "Together we agree the purpose, timing and scale.", "Birgalikda maqsad, vaqt va hajmni kelishamiz.", "Вместе согласуем цель, сроки и объём."),
 L("Nátiyjesi haqqında fotolar hám qısqa esabat jiberemiz.", "We send you photos and a short report on the result.", "Natijasi haqida suratlar va qisqa hisobot yuboramiz.", "Мы присылаем фото и короткий отчёт о результате."),
]


def body(i, up, href, ctx):
    svg = lambda p: f'<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
    ways = "".join(f'<div class="card spway" style="--sc:{c}"><span class="spic">{svg(p)}</span><h3>{t[i]}</h3><p>{d[i]}</p></div>' for p, c, t, d in WAYS)
    get = "".join(f"<li>{g[i]}</li>" for g in GET)
    how = "".join(f'<li><b>{n + 1}</b><span>{h[i]}</span></li>' for n, h in enumerate(HOW))
    return (f'<p class="lead2">{T["lead"][i]}</p>'
            f'<h2>{T["ways_h"][i]}</h2><div class="spways">{ways}</div>'
            f'<div class="sptwo"><div class="card"><h2>{T["get_h"][i]}</h2><ul class="spget">{get}</ul></div>'
            f'<div class="card"><h2>{T["how_h"][i]}</h2><ol class="sphow">{how}</ol></div></div>'
            f'<p class="note">{T["note"][i]}</p>'
            f'<div class="card ofcta spcta"><div><h3>{T["contact_h"][i]}</h3><p><b>{T["counselor"][i]}</b></p>'
            f'<p class="btns"><a class="btn p" href="tel:{ctx["PHONE"]}">{ctx["PHONE_TXT"]}</a><a class="btn s" href="mailto:{ctx["EMAIL"]}">{ctx["EMAIL"]}</a><a class="btn s" href="{ctx["TG"]}" rel="noopener">Telegram</a></p></div></div>'
            f'<p class="btns"><a class="btn s" href="{href("partners/")}">{T["partners"][i]} →</a><a class="btn s" href="{up}school-profile/">{T["profile"][i]} →</a></p>')
