# School policies page (4 languages): child protection, academic honesty, anti-bullying,
# photo & media consent, website privacy, fair admission. Each policy: summary, commitments, how to report.
SUB = "policies/"
L = lambda a, b, c, d: (a, b, c, d)
NAME = L("Mektep qaǵıydaları", "School policies", "Maktab qoidalari", "Правила и политики школы")
DESC = L("Balalardı qorǵaw, akademiyalıq hadallıq, zorlıqqa qarsı gúres, foto razılıǵı, sayt qupıyalıǵı hám ádil qabıl qaǵıydaları.",
         "Child protection, academic honesty, anti-bullying, photo consent, website privacy and fair admission.",
         "Bolalarni himoya qilish, akademik halollik, zo‘ravonlikka qarshi kurash, surat roziligi, sayt maxfiyligi va adolatli qabul qoidalari.",
         "Защита детей, академическая честность, борьба с травлей, согласие на фото, конфиденциальность сайта и честный приём.")
ICON = ('<path d="M12 3l8 3v6c0 4.500-3.400 8.300-8 9-4.600-.700-8-4.500-8-9V6z"/><path d="M9 12l2 2 4-4"/>', "#047857")
REVIEWED = L("2026-jıl noyabr", "November 2026", "2026-yil noyabr", "Ноябрь 2026")
NEXT = L("2027-jıl sentyabr", "September 2027", "2027-yil sentyabr", "Сентябрь 2027")

T = dict(
 lead=L("Bul qaǵıydalar oqıwshılarımızdıń qáwipsizligin, hadal oqıwın hám jeke maǵlıwmatlarınıń qorǵalıwın támiyinleydi. Olar Ózbekstan Respublikası nızamlarına tiykarlanǵan hám mektep xızmetkerleri, oqıwshılar hám ata-analar ushın birdey ámel etedi.",
        "These policies keep our students safe, make sure their work is honest and protect their personal information. They are based on the laws of the Republic of Uzbekistan and apply equally to staff, students and parents.",
        "Ushbu qoidalar o‘quvchilarimiz xavfsizligini, halol o‘qishini va shaxsiy ma’lumotlari himoyasini ta’minlaydi. Ular O‘zbekiston Respublikasi qonunlariga asoslangan va maktab xodimlari, o‘quvchilar va ota-onalar uchun birdek amal qiladi.",
        "Эти правила обеспечивают безопасность наших учеников, честность их работы и защиту личных данных. Они основаны на законах Республики Узбекистан и одинаково действуют для сотрудников, учеников и родителей."),
 rev=L("Kórip shıǵılǵan", "Last reviewed", "Ko‘rib chiqilgan", "Пересмотрено"),
 nxt=L("Keyingi kóriw", "Next review", "Keyingi ko‘rib chiqish", "Следующий пересмотр"),
 law=L("Huqıqıy tiykar", "Legal basis", "Huquqiy asos", "Правовая основа"),
 we=L("Biz neni támiyinleymiz", "Our commitments", "Biz nimani ta’minlaymiz", "Наши обязательства"),
 rep=L("Másele bolsa", "If there is a problem", "Muammo bo‘lsa", "Если возникла проблема"),
 toc=L("Mazmunı", "Contents", "Mundarija", "Содержание"),
 print=L("Basıp shıǵarıw", "Print", "Chop etish", "Распечатать"),
 contact_h=L("Kimge múrájat etiw kerek", "Who to contact", "Kimga murojaat qilish kerak", "К кому обращаться"),
 contact_p=L("Kez kelgen máseleni tómendegi xızmetkerlerdiń birine aytıwǵa boladı. Barlıq múrájatlar itibar menen hám qupıya kórip shıǵıladı.",
             "Any concern can be raised with any of the staff below. Every report is taken seriously and handled confidentially.",
             "Har qanday muammoni quyidagi xodimlardan biriga aytish mumkin. Barcha murojaatlar e’tibor bilan va maxfiy ko‘rib chiqiladi.",
             "О любой проблеме можно сообщить любому из сотрудников ниже. Каждое обращение рассматривается внимательно и конфиденциально."),
 hot=L("Agentlik isenim telefonı", "Agency helpline", "Agentlik ishonch telefoni", "Телефон доверия Агентства"),
 child=L("Balalardı qorǵaw isenim telefonı (Sociallıq qorǵaw milliy agentligi)", "Child protection helpline (National Agency for Social Protection)", "Bolalarni himoya qilish ishonch telefoni (Ijtimoiy himoya milliy agentligi)", "Телефон доверия по защите детей (Национальное агентство социальной защиты)"),
 approved=L("Qaǵıydalar mektep direktorı Feruza Nizamatdinova tárepinen 2026-jıl 28-noyabrde tastıyıqlanǵan hám hár jılı kórip shıǵıladı.", "These policies were approved by the school director, Feruza Nizamatdinova, on 28 November 2026 and are reviewed every year.", "Qoidalar maktab direktori Feruza Nizamatdinova tomonidan 2026-yil 28-noyabrda tasdiqlangan va har yili ko‘rib chiqiladi.", "Правила утверждены директором школы Ферузой Низаматдиновой 28 ноября 2026 года и пересматриваются ежегодно."),
 apr=L("Direktor tastıyıqlaǵan", "Approved by the director", "Direktor tasdiqlagan", "Утверждено директором"),
 apr_d=L("2026-jıl 28-noyabr", "28 November 2026", "2026-yil 28-noyabr", "28 ноября 2026"),
)

CONTACTS = [  # (name, role) - public on the Leadership page
 ("Feruza Nizamatdinova", L("Mektep direktorı", "Director", "Maktab direktori", "Директор школы")),
 ("Islam Pirniyazov", L("Direktordıń ruwxıy-aǵartıwshılıq isler boyınsha orınbasarı", "Deputy Director for upbringing and pastoral care", "Direktorning ma’naviy-ma’rifiy ishlar bo‘yicha o‘rinbosari", "Заместитель директора по духовно-просветительской работе")),
 ("Baxtiyar Perdebaev", L("Mektep psixologı", "School psychologist", "Maktab psixologi", "Школьный психолог")),
 ("Alimbek Jumamuratov", L("Mektep másláhátshisi", "School Counselor", "Maktab maslahatchisi", "Школьный консультант")),
]

POLICIES = [  # (id, colour, icon, title, summary, commitments, report, legal basis)
 ("child", "#a3202c", '<path d="M12 3l8 3v6c0 4.500-3.400 8.300-8 9-4.600-.700-8-4.500-8-9V6z"/><circle cx="12" cy="10" r="2.500"/><path d="M8 16a4 4 0 0 1 8 0"/>',
  L("Balalardı qorǵaw", "Child protection", "Bolalarni himoya qilish", "Защита детей"),
  L("Hár bir oqıwshı mektepte qáwipsiz sezinip, húrmet kóriwi kerek. Fizikalıq, psixologiyalıq jazalaw hám kemsitiw qadaǵan.", "Every student must feel safe and respected at school. Physical or psychological punishment and humiliation are forbidden.", "Har bir o‘quvchi maktabda o‘zini xavfsiz his qilishi va hurmat ko‘rishi kerak. Jismoniy, psixologik jazo va kamsitish taqiqlangan.", "Каждый ученик должен чувствовать себя в школе в безопасности и с уважением. Физические и психологические наказания и унижение запрещены."),
  [L("Xızmetkerler oqıwshılar menen tek kásiplik qatnasta boladı", "Staff keep their relationships with students strictly professional", "Xodimlar o‘quvchilar bilan faqat kasbiy munosabatda bo‘ladi", "Сотрудники поддерживают с учениками только профессиональные отношения"),
   L("Oqıwshı hám xızmetker jeke messenjerde tek oqıw máseleleri boyınsha jazısadı", "Messages between staff and students are about school matters only", "O‘quvchi va xodim messenjerda faqat o‘qish masalalari bo‘yicha yozishadi", "Переписка сотрудников с учениками — только по учебным вопросам"),
   L("Qáwip belgisin kórgen xızmetker sol kúni direktorǵa xabar beredi", "Any staff member who sees a sign of harm tells the director the same day", "Xavf belgisini ko‘rgan xodim o‘sha kuni direktorga xabar beradi", "Сотрудник, заметивший признаки опасности, в тот же день сообщает директору"),
   L("Oqıwshı psixologtan qupıya járdem ala aladı", "Students can get confidential help from the school psychologist", "O‘quvchi psixologdan maxfiy yordam olishi mumkin", "Ученик может получить конфиденциальную помощь психолога"),
   L("Mekteptegi qonaqlar xızmetker menen birge júredi", "Visitors to the school are accompanied by a staff member", "Maktabdagi mehmonlar xodim bilan birga yuradi", "Посетителей школы сопровождает сотрудник")],
  L("Oqıwshı yamasa ata-ana tómendegi xızmetkerlerdiń qálegen birine aytıwı múmkin. Shuǵıl qáwip bolsa — 102.", "A student or parent can tell any of the staff listed below. In an emergency, call 102.", "O‘quvchi yoki ota-ona quyidagi xodimlardan istalganiga aytishi mumkin. Shoshilinch xavf bo‘lsa — 102.", "Ученик или родитель может сообщить любому из сотрудников ниже. При срочной опасности — 102."),
  L("«Bala huqıqlarınıń kepillikleri haqqında»ǵı Nızam (2008)", "Law “On guarantees of the rights of the child” (2008)", "«Bola huquqlarining kafolatlari to‘g‘risida»gi Qonun (2008)", "Закон «О гарантиях прав ребёнка» (2008)")),
 ("honesty", "#2563eb", '<path d="M12 20h9"/><path d="M16.500 3.500a2.100 2.100 0 0 1 3 3L7 19l-4 1 1-4z"/>',
  L("Akademiyalıq hadallıq", "Academic honesty", "Akademik halollik", "Академическая честность"),
  L("Oqıwshınıń jumısı — onıń óz jumısı. Bahalar, sertifikatlar hám nátiyjeler qanday bolsa, sonday kórsetiledi.", "A student’s work is their own. Grades, certificates and results are reported exactly as they are.", "O‘quvchining ishi — uning o‘z ishi. Baholar, sertifikatlar va natijalar qanday bo‘lsa, shunday ko‘rsatiladi.", "Работа ученика — это его собственная работа. Оценки, сертификаты и результаты указываются такими, какие они есть."),
  [L("Imtixan hám olimpiadada kóshiriw, basqa birewdiń ornına tapsırıw qadaǵan", "No copying in tests or olympiads, and no sitting a test for someone else", "Imtihon va olimpiadada ko‘chirish, boshqa birovning o‘rniga topshirish taqiqlanadi", "Списывание и сдача теста за другого запрещены"),
   L("Universitetke esseni oqıwshınıń ózi jazadı; muǵallim tek pikir aytadı", "University essays are written by the student; teachers only give feedback", "Universitet inshosini o‘quvchining o‘zi yozadi; o‘qituvchi faqat fikr bildiradi", "Эссе в университет пишет сам ученик; учитель только даёт отзыв"),
   L("Jasalma intellekt (AI) qurallarınan paydalanılsa, bul ashıq aytıladı", "If AI tools are used, this is stated openly", "Sun’iy intellekt (AI) vositalaridan foydalanilsa, bu ochiq aytiladi", "Если используются инструменты ИИ, это указывается открыто"),
   L("Mektep usınıs xatları hám transkriptlerde bahalardı kóterip kórsetpeydi", "The school never inflates grades in transcripts or recommendation letters", "Maktab transkript va tavsiyanomalarda baholarni oshirib ko‘rsatmaydi", "Школа не завышает оценки в транскриптах и рекомендациях"),
   L("Saytta járiyalanǵan hár bir nátiyjeni tekseriwge boladı", "Every result published on this website can be checked", "Saytda e’lon qilingan har bir natijani tekshirish mumkin", "Каждый результат на сайте можно проверить")],
  L("Buzıwshılıq birinshi ret bolsa — sáwbet hám jumıstı qayta orınlaw; qaytalansa — ata-analar shaqırıladı.", "A first breach leads to a conversation and redoing the work; repeated breaches involve the parents.", "Birinchi marta buzilsa — suhbat va ishni qayta bajarish; takrorlansa — ota-onalar chaqiriladi.", "При первом нарушении — беседа и повторное выполнение работы; при повторном — вызов родителей."),
  L("«Bilimlendiriw haqqında»ǵı Nızam (2020)", "Law “On Education” (2020)", "«Ta’lim to‘g‘risida»gi Qonun (2020)", "Закон «Об образовании» (2020)")),
 ("bullying", "#d97706", '<circle cx="9" cy="8" r="3.500"/><path d="M2 20a7 7 0 0 1 14 0"/><path d="M17 8l4 4M21 8l-4 4"/>',
  L("Zorlıq hám qorlawǵa qarsı", "Anti-bullying", "Zo‘ravonlik va haqoratga qarshi", "Против травли"),
  L("Mektepte, internette hám Telegram toparlarında qorlaw, qorqıtıw hám shetlestiriw qabıl etilmeydi.", "Bullying, threats and exclusion are not accepted at school, online or in Telegram groups.", "Maktabda, internetda va Telegram guruhlarida haqorat, qo‘rqitish va chetlashtirish qabul qilinmaydi.", "Оскорбления, угрозы и изоляция недопустимы в школе, в интернете и в Telegram-группах."),
  [L("Hár bir xabar sol hápte kórip shıǵıladı", "Every report is looked into within the same week", "Har bir xabar o‘sha hafta ko‘rib chiqiladi", "Каждое сообщение рассматривается в течение той же недели"),
   L("Xabar bergen oqıwshınıń atı qorǵaladı", "The student who reports is protected", "Xabar bergan o‘quvchining ismi himoya qilinadi", "Ученик, сообщивший о травле, защищён"),
   L("Zıyan kórgen oqıwshıǵa psixolog járdem beredi", "The psychologist supports the student who was harmed", "Zarar ko‘rgan o‘quvchiga psixolog yordam beradi", "Психолог поддерживает пострадавшего ученика"),
   L("Eki tárep penen hám ata-anaları menen sáwbet ótkeriledi", "Both sides and their parents are spoken to", "Ikki tomon va ularning ota-onalari bilan suhbat o‘tkaziladi", "Проводится беседа с обеими сторонами и их родителями")],
  L("Klass basshısına, psixologqa yamasa direktorǵa aytıń — awızeki yamasa jazba túrde.", "Tell the class teacher, the psychologist or the director, in person or in writing.", "Sinf rahbariga, psixologga yoki direktorga ayting — og‘zaki yoki yozma.", "Сообщите классному руководителю, психологу или директору — устно или письменно."),
  L("«Bilimlendiriw haqqında»ǵı Nızam (2020)", "Law “On Education” (2020)", "«Ta’lim to‘g‘risida»gi Qonun (2020)", "Закон «Об образовании» (2020)")),
 ("photos", "#7c3aed", '<rect x="3" y="6" width="18" height="14" rx="2"/><circle cx="12" cy="13" r="3.500"/><path d="M8 6l1.500-2h5L16 6"/>',
  L("Foto hám media razılıǵı", "Photo and media consent", "Surat va media roziligi", "Согласие на фото и медиа"),
  L("Oqıwshılardıń súwretleri hám atları tek razılıǵı menen járiyalanadı.", "Students’ photos and names are published only with consent.", "O‘quvchilarning suratlari va ismlari faqat roziligi bilan e’lon qilinadi.", "Фото и имена учеников публикуются только с согласия."),
  [L("Súwret járiyalanıwdan aldın oqıwshınıń hám ata-anasınıń razılıǵı alınadı", "Consent from the student and a parent is obtained before a photo is published", "Surat e’lon qilinishidan oldin o‘quvchi va ota-onasining roziligi olinadi", "До публикации фото получается согласие ученика и родителя"),
   L("JShShIR, sertifikat nomerleri, úy mánzilleri hám pasport maǵlıwmatları hesh qashan járiyalanbaydı", "Personal ID numbers, certificate numbers, home addresses and passport details are never published", "JShShIR, sertifikat raqamlari, uy manzillari va pasport ma’lumotlari hech qachon e’lon qilinmaydi", "ПИНФЛ, номера сертификатов, домашние адреса и паспортные данные никогда не публикуются"),
   L("Universitet xatlarınan tek universitet atı, baǵdar hám grant kórsetiledi", "From university letters we show only the university, programme and grant", "Universitet xatlaridan faqat universitet nomi, yo‘nalish va grant ko‘rsatiladi", "Из писем университетов показываются только университет, программа и грант"),
   L("Soraw boyınsha súwret yamasa at tez arada alıp taslanadı", "A photo or name is removed promptly on request", "So‘rov bo‘yicha surat yoki ism tezda olib tashlanadi", "Фото или имя удаляются по запросу в кратчайший срок")],
  L("Súwretti alıp taslaw ushın sayt administratorına jazıń: ixm013@piima.uz", "To remove a photo, write to the website administrator: ixm013@piima.uz", "Suratni olib tashlash uchun sayt administratoriga yozing: ixm013@piima.uz", "Чтобы удалить фото, напишите администратору сайта: ixm013@piima.uz"),
  L("«Jeke maǵlıwmatlar haqqında»ǵı Nızam (2019)", "Law “On Personal Data” (2019)", "«Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonun (2019)", "Закон «О персональных данных» (2019)")),
 ("privacy", "#0b5f78", '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
  L("Sayt qupıyalıǵı", "Website privacy", "Sayt maxfiyligi", "Конфиденциальность сайта"),
  L("Bul sayt sizden jeke maǵlıwmat jıynamaydı hám reklama kórsetpeydi.", "This website does not collect your personal information and shows no advertising.", "Ushbu sayt sizdan shaxsiy ma’lumot to‘plamaydi va reklama ko‘rsatmaydi.", "Этот сайт не собирает ваши личные данные и не показывает рекламу."),
  [L("Kirisler sanı GoatCounter arqalı esaplanadı: cookie-siz, adamdı anıqlamaydı", "Visits are counted with GoatCounter, without cookies and without identifying anyone", "Tashriflar soni GoatCounter orqali hisoblanadi: cookie-siz, shaxsni aniqlamaydi", "Посещения считаются через GoatCounter — без cookie и без идентификации"),
   L("Sabaq kestesi, joba hám kalkulyator sazlamaları tek óz qurılmańızda saqlanadı", "Timetable, plan and calculator settings are saved only on your own device", "Dars jadvali, reja va kalkulyator sozlamalari faqat o‘z qurilmangizda saqlanadi", "Настройки расписания, плана и калькулятора хранятся только на вашем устройстве"),
   L("Sayt maǵlıwmat jıynamaydı: klub arzası da siz ózińiz Telegram yamasa pochta arqalı jibergende ǵana bizge keledi", "The site collects nothing: even a club application reaches us only when you send it yourself by Telegram or email", "Sayt ma’lumot to‘plamaydi: to‘garak arizasi ham faqat o‘zingiz Telegram yoki pochta orqali yuborganingizda bizga keladi", "Сайт ничего не собирает: даже заявка в клуб попадает к нам, только когда вы сами отправите её в Telegram или по почте"),
   L("Brauzer maǵlıwmatların óshirip, saqlanǵan sazlamalardı alıp taslaw múmkin", "You can delete saved settings by clearing your browser data", "Brauzer ma’lumotlarini tozalab, saqlangan sozlamalarni o‘chirish mumkin", "Сохранённые настройки можно удалить, очистив данные браузера")],
  L("Sorawlarıńız bolsa: ixm013@piima.uz", "Questions: ixm013@piima.uz", "Savollar bo‘lsa: ixm013@piima.uz", "Вопросы: ixm013@piima.uz"),
  L("«Jeke maǵlıwmatlar haqqında»ǵı Nızam (2019)", "Law “On Personal Data” (2019)", "«Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonun (2019)", "Закон «О персональных данных» (2019)")),
 ("admission", "#047857", '<path d="M3 21h18"/><path d="M5 21V9l7-5 7 5v12"/><path d="M10 21v-5h4v5"/>',
  L("Ádil qabıl", "Fair admission", "Adolatli qabul", "Честный приём"),
  L("Mektepke qabıl tek Agentlik ótkeretuǵın kiriw imtixanları nátiyjesi boyınsha boladı.", "Admission is decided only by the entrance exams run by the Agency.", "Maktabga qabul faqat Agentlik o‘tkazadigan kirish imtihonlari natijasi bo‘yicha bo‘ladi.", "Приём решается только по результатам вступительных экзаменов, которые проводит Агентство."),
  [L("Kiriw imtixanları 5- hám 7-klassqa ótkeriledi", "Entrance exams are held for Grades 5 and 7", "Kirish imtihonlari 5- va 7-sinflarga o‘tkaziladi", "Вступительные экзамены проводятся в 5 и 7 классы"),
   L("Qabıl hám oqıw biypul; mektep heshqanday tólem almaydı", "Admission and study are free; the school takes no payments", "Qabul va o‘qish bepul; maktab hech qanday to‘lov olmaydi", "Приём и обучение бесплатны; школа не берёт никаких платежей"),
   L("Hújjetler rásmiy ariza.piima.uz portalı arqalı qabıl etiledi", "Applications are made through the official portal ariza.piima.uz", "Hujjatlar rasmiy ariza.piima.uz portali orqali qabul qilinadi", "Заявления подаются через официальный портал ariza.piima.uz"),
   L("Jınısı, milleti, tili yamasa shańaraqtıń jaǵdayı boyınsha kemsitiw joq", "No discrimination by gender, ethnicity, language or family background", "Jinsi, millati, tili yoki oilaviy ahvoli bo‘yicha kamsitish yo‘q", "Никакой дискриминации по полу, национальности, языку или положению семьи")],
  L("Kimdur tólem sorasa, Agentlik isenim telefonına xabar beriń: +998 71 207 40 48.", "If anyone asks for payment, report it to the Agency helpline: +998 71 207 40 48.", "Kimdir to‘lov so‘rasa, Agentlik ishonch telefoniga xabar bering: +998 71 207 40 48.", "Если кто-то просит деньги, сообщите на телефон доверия Агентства: +998 71 207 40 48."),
  L("«Bilimlendiriw haqqında»ǵı Nızam (2020)", "Law “On Education” (2020)", "«Ta’lim to‘g‘risida»gi Qonun (2020)", "Закон «Об образовании» (2020)")),
]


PRINT_I = '<path d="M6 9V3h12v6M6 18H4v-7h16v7h-2M8 14h8v7H8z"/>'
APR_I = '<path d="M12 3l2.4 1.8 3 .2.9 2.9 2.2 2-1 2.8.4 3-2.6 1.5-1.4 2.6-3-.4L12 21l-2.4-1.8-3 .4-1.4-2.6-2.6-1.5.4-3-1-2.8 2.2-2 .9-2.9 3-.2z"/><path d="M8.5 12l2.4 2.4 4.6-4.8"/>'
WHO_I = '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>'


def _svg(p, s=22):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'


def body(i, up, href, lead_href):
    toc = "".join(f'<a href="#{k}" style="--c:{c}"><span class="poi">{_svg(ic, 18)}</span>{t[i]}</a>' for k, c, ic, t, *_ in POLICIES)
    cards = "".join(
        f'<article class="card pocard" id="{k}" style="--c:{c}"><header><span class="poi">{_svg(ic, 26)}</span><div><span class="pon">{n + 1:02d}</span><h2>{t[i]}</h2></div></header>'
        f'<p class="posum">{s[i]}</p><h3>{T["we"][i]}</h3><ul class="pocm">' + "".join(f"<li>{x[i]}</li>" for x in cm) + '</ul>'
        f'<div class="porep"><b>{T["rep"][i]}</b><span>{r[i]}</span></div><p class="polaw">{T["law"][i]}: {lw[i]}</p></article>'
        for n, (k, c, ic, t, s, cm, r, lw) in enumerate(POLICIES))
    who = "".join(f'<li><a href="{lead_href(nm)}"><b>{nm}</b></a><span>{rl[i]}</span></li>' for nm, rl in CONTACTS)
    return (f'<p class="lead2">{T["lead"][i]}</p>'
            f'<div class="pometa"><span class="poapr">{_svg(APR_I, 18)}{T["apr"][i]}: <b>{T["apr_d"][i]}</b></span><span>{T["rev"][i]}: <b>{REVIEWED[i]}</b></span><span>{T["nxt"][i]}: <b>{NEXT[i]}</b></span>'
            f'<button type="button" class="poprint" onclick="window.print()">{_svg(PRINT_I, 18)}{T["print"][i]}</button></div>'
            f'<div class="polay"><nav class="potoc" aria-label="{T["toc"][i]}"><p>{T["toc"][i]}</p>{toc}<a href="#who" style="--c:#4b5d65"><span class="poi">{_svg(WHO_I, 18)}</span>{T["contact_h"][i]}</a></nav>'
            f'<div class="pomain">{cards}'
            f'<section class="card powho" id="who"><h2>{T["contact_h"][i]}</h2><p>{T["contact_p"][i]}</p><ul>{who}</ul>'
            f'<div class="pohot"><a href="tel:1246"><b>1246</b><span>{T["child"][i]}</span></a><a href="tel:+998712074048"><b>+998 71 207 40 48</b><span>{T["hot"][i]}</span></a><a href="tel:102"><b>102</b><span>{L("Policiya", "Police", "Politsiya", "Полиция")[i]}</span></a></div></section>'
            f'<p class="note">{T["approved"][i]}</p></div></div>')
