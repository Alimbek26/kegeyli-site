# College counselling office page (4 languages): counselor, record, Grade 9-11 roadmap,
# services for students/families and for universities, principles, toolkit, contact.
# Figures come from graduates.py / offers.py, so they update with the data.
import collections
import graduates as G
import offers as OF

SUB = "counseling/"
L = lambda a, b, c, d: (a, b, c, d)
NAME = L("Universitetke kiriw boyınsha másláhát", "College counselling", "Universitetga kirish bo‘yicha maslahat", "Консультации по поступлению")
DESC = L("Mektep másláhátshisi oqıwshılarǵa 9-klasstan universitetke shekem qalay járdem beredi hám universitetlerge qanday hújjetler jiberemiz.",
         "How our school counselor guides students from Grade 9 to university, and what we send to universities: transcripts, recommendations, School Profile.",
         "Maktab maslahatchisi o‘quvchilarga 9-sinfdan universitetgacha qanday yordam beradi va universitetlarga qanday hujjatlar yuboramiz.",
         "Как школьный консультант ведёт учеников от 9 класса до университета и какие документы мы отправляем в университеты.")
ICON = ('<path d="M22 10L12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/><path d="M22 10v6"/>', "#7c3aed")

T = dict(
 eyebrow=L("Universitetke tayarlıq bólimi", "College Counselling Office", "Universitetga tayyorlov bo‘limi", "Отдел подготовки к поступлению"),
 name=L("Alimbek Jumamuratov", "Alimbek Jumamuratov", "Alimbek Jumamuratov", "Алимбек Жумамуратов"),
 role=L("Mektep másláhátshisi · IELTS dizimge alıw punktiniń juwapkeri", "School Counselor · IELTS Registration Point contact", "Maktab maslahatchisi · IELTS ro‘yxatga olish nuqtasi mas’uli", "Школьный консультант · ответственный за пункт регистрации IELTS"),
 mission=L("Bizdiń maqsetimiz — hár bir oqıwshıǵa Ózbekstanda yamasa shet elde ózi ósetuǵın universitetti tabıwǵa járdem beriw hám universitetlerge hár bir talapker haqqında ádil, tolıq maǵlıwmat beriw.",
           "Our aim is to help every student find the university where they will grow, in Uzbekistan or abroad, and to give universities an honest, complete picture of each applicant.",
           "Maqsadimiz — har bir o‘quvchiga O‘zbekistonda yoki xorijda o‘zi o‘sadigan universitetni topishga yordam berish va universitetlarga har bir abituriyent haqida halol, to‘liq ma’lumot berish.",
           "Наша цель — помочь каждому ученику найти университет, где он будет расти, в Узбекистане или за рубежом, и дать университетам честную и полную картину о каждом абитуриенте."),
 book=L("Ushırasıwǵa jazılıw", "Book a meeting", "Uchrashuvga yozilish", "Записаться на встречу"),
 profile_p=L("Másláhátshi profili", "Counselor profile", "Maslahatchi profili", "Профиль консультанта"),
 rec_h=L("Nátiyjelerimiz", "Our record", "Natijalarimiz", "Наши результаты"),
 rec_note=L("Barlıq sanlar saytta tolıq kórsetilgen hám tekseriwge boladı.", "Every figure is published in full on this website and can be checked.", "Barcha raqamlar saytda to‘liq ko‘rsatilgan va tekshirish mumkin.", "Все цифры полностью опубликованы на сайте и их можно проверить."),
 r_uni=L("pitkeriwshilerimizdiń {g} nan universitetke tústi ({y})", "of our {g} graduates went on to university ({y})", "bitiruvchilarimizdan {g} tadan universitetga kirdi ({y})", "из {g} выпускников поступили в университет ({y})"),
 r_inst=L("universitet hám kolledj — pitkeriwshilerimiz oqıp atırǵan orınlar", "universities and colleges where our graduates study", "universitet va kollej — bitiruvchilarimiz o‘qiyotgan joylar", "университетов и колледжей, где учатся наши выпускники"),
 r_off=L("shet eldegi {u} universitetten usınıs", "offers from {u} universities abroad", "xorijdagi {u} universitetdan taklif", "предложений от {u} зарубежных университетов"),
 r_top=L("dúnyanıń top-100 universitetinen usınıs (QS 2025)", "offers from world top-100 universities (QS 2025)", "dunyoning top-100 universitetidan taklif (QS 2025)", "предложения от университетов мирового топ-100 (QS 2025)"),
 road_h=L("9-klasstan universitetke shekem", "From Grade 9 to university", "9-sinfdan universitetgacha", "От 9 класса до университета"),
 road_p=L("Hár bir basqıshta oqıwshı ne isleydi hám másláhátshi qalay járdem beredi.", "What the student does at each stage, and how the counselor helps.", "Har bir bosqichda o‘quvchi nima qiladi va maslahatchi qanday yordam beradi.", "Что делает ученик на каждом этапе и как помогает консультант."),
 you=L("Oqıwshı", "Student", "O‘quvchi", "Ученик"),
 we=L("Másláhátshi", "Counselor", "Maslahatchi", "Консультант"),
 serv_h=L("Biz ne usınamız", "What we offer", "Biz nima taklif qilamiz", "Что мы предлагаем"),
 fam_h=L("Oqıwshılar hám ata-analar ushın", "For students and families", "O‘quvchilar va ota-onalar uchun", "Ученикам и родителям"),
 uni_h=L("Universitetler ushın", "For universities", "Universitetlar uchun", "Университетам"),
 uni_mail=L("Hújjetler hám tekseriw ushın:", "Documents and verification:", "Hujjatlar va tekshirish uchun:", "Документы и проверка:"),
 prin_h=L("Biziń principlerimiz", "Our principles", "Bizning tamoyillarimiz", "Наши принципы"),
 tool_h=L("Oqıwshılar ushın qurallar", "Toolkit for students", "O‘quvchilar uchun vositalar", "Инструменты для учеников"),
 tool_p=L("Bul saytta tayarlanǵan qollanbalar — óz betińshe tayarlanıw ushın.", "Step-by-step guides on this website, for preparing on your own.", "Ushbu saytdagi qo‘llanmalar — mustaqil tayyorlanish uchun.", "Пошаговые руководства на этом сайте — для самостоятельной подготовки."),
 cta_h=L("Ushırasıwǵa jazılıń", "Book a meeting", "Uchrashuvga yoziling", "Запишитесь на встречу"),
 cta_p=L("Oqıwshılar hám ata-analar: Telegram yamasa elektron pochta arqalı jazıń, yamasa qońıraw etiń. Ushırasıwlar mektepte, aldın ala kelisip ótkeriledi.",
         "Students and parents: write on Telegram or by email, or call. Meetings take place at school, by appointment.",
         "O‘quvchilar va ota-onalar: Telegram yoki elektron pochta orqali yozing yoki qo‘ng‘iroq qiling. Uchrashuvlar maktabda, oldindan kelishib o‘tkaziladi.",
         "Ученики и родители: напишите в Telegram или на почту либо позвоните. Встречи проходят в школе по предварительной договорённости."),
 offers=L("Shet el universitetleri", "Offers from abroad", "Xorijiy universitetlar", "Зарубежные университеты"),
 grads=L("Pitkeriwshiler", "Graduates", "Bitiruvchilar", "Выпускники"),
 sp=L("Mektep profili (PDF)", "School Profile (PDF)", "Maktab profili (PDF)", "Профиль школы (PDF)"),
)

STEPS = [  # (colour, stage, title, student points, counselor points)
 ("#0891b2", L("9-klass", "Grade 9", "9-sinf", "9 класс"), L("Ózińdi tanı", "Discover", "O‘zingni kashf et", "Узнай себя"),
  [L("Qızıǵıwshılıqlarıń hám kúshli pánleriń haqqında oylan", "Explore your interests and strongest subjects", "Qiziqishlaring va kuchli fanlaring haqida o‘yla", "Определи интересы и сильные предметы"),
   L("IELTS ushın inglis tilin rawajlandır", "Build your English towards IELTS", "IELTS uchun ingliz tilini rivojlantir", "Развивай английский к IELTS"),
   L("Olimpiadalarda kúshińdi sına", "Try olympiads", "Olimpiadalarda kuchingni sina", "Попробуй себя в олимпиадах")],
  [L("Birinshi jeke sáwbet", "First one-to-one conversation", "Birinchi yakkama-yakka suhbat", "Первая индивидуальная беседа"),
   L("Baǵdar tańlawǵa járdem", "Helps choose a direction", "Yo‘nalish tanlashga yordam", "Помогает выбрать направление"),
   L("Ózbekstan hám shet eldegi imkaniyatlar menen tanıstıradı", "Introduces options in Uzbekistan and abroad", "O‘zbekiston va xorijdagi imkoniyatlar bilan tanishtiradi", "Знакомит с вариантами в Узбекистане и за рубежом")]),
 ("#2563eb", L("10-klass", "Grade 10", "10-sinf", "10 класс"), L("Tayarlan", "Prepare", "Tayyorlan", "Готовься"),
  [L("IELTS tapsır — mektepte biypul dizimge alınıw", "Take IELTS: free registration at school", "IELTS topshir — maktabda bepul ro‘yxatdan o‘tish", "Сдай IELTS — бесплатная регистрация в школе"),
   L("AQSh-qa niyetlenseń, SAT-qa tayarlan", "Prepare for the SAT if aiming at the USA", "AQShni maqsad qilsang, SATga tayyorlan", "Готовься к SAT, если цель — США"),
   L("Milliy sertifikatlar, iskerlik hám jazǵı joybarlar", "National certificates, activities and summer projects", "Milliy sertifikatlar, faollik va yozgi loyihalar", "Национальные сертификаты, активности и летние проекты")],
  [L("Universitetlerdiń uzın dizimin dúzedi", "Builds a long list of universities", "Universitetlarning uzun ro‘yxatini tuzadi", "Составляет длинный список университетов"),
   L("Testler kalendarın rejelestiredi", "Plans the testing calendar", "Testlar kalendarini rejalashtiradi", "Планирует календарь тестов"),
   L("Iskerlik hám grantlar boyınsha másláhát", "Advises on activities and scholarships", "Faollik va grantlar bo‘yicha maslahat", "Советует по активностям и стипендиям")]),
 ("#7c3aed", L("11-klass · sentyabr–yanvar", "Grade 11 · Sep–Jan", "11-sinf · sentyabr–yanvar", "11 класс · сентябрь–январь"), L("Arza ber", "Apply", "Ariza topshir", "Подавай документы"),
  [L("Aqırǵı dizimdi tańla", "Finalise your list", "Yakuniy ro‘yxatni tanla", "Утверди финальный список"),
   L("Esseńdi jaz hám qayta isle", "Write and revise your essays", "Inshoingni yoz va qayta ishla", "Напиши и доработай эссе"),
   L("Common App, UCAS yamasa universitet portalları arqalı arza ber", "Apply via Common App, UCAS or university portals", "Common App, UCAS yoki universitet portallari orqali ariza ber", "Подай через Common App, UCAS или порталы университетов")],
  [L("Essege pikir aytadı (esseni oqıwshınıń ózi jazadı)", "Gives feedback on essays (the student writes them)", "Inshoga fikr bildiradi (inshoni o‘quvchining o‘zi yozadi)", "Даёт отзыв на эссе (пишет сам ученик)"),
   L("Usınıs xatın jazadı", "Writes the recommendation letter", "Tavsiyanoma yozadi", "Пишет рекомендательное письмо"),
   L("Transkript hám mektep profilin jiberedi, múddetlerdi baqlaydı", "Sends transcript and School Profile, tracks deadlines", "Transkript va maktab profilini yuboradi, muddatlarni kuzatadi", "Отправляет транскрипт и профиль школы, следит за сроками")]),
 ("#a3202c", L("11-klass · fevral–avgust", "Grade 11 · Feb–Aug", "11-sinf · fevral–avgust", "11 класс · февраль–август"), L("Sheshim qabılla", "Decide", "Qaror qabul qil", "Принимай решение"),
  [L("Usınıslar hám grantlardı salıstır", "Compare offers and grants", "Takliflar va grantlarni solishtir", "Сравни предложения и гранты"),
   L("Milliy qabıl testlerin tapsır", "Sit the national admission tests", "Milliy qabul testlarini topshir", "Сдай национальные вступительные тесты"),
   L("Shet elge barsań — viza", "Visa, if studying abroad", "Xorijga borsang — viza", "Виза, если учёба за рубежом")],
  [L("Usınıslar hám qárejetlerdi salıstırıwǵa járdem", "Helps compare offers and costs", "Takliflar va xarajatlarni solishtirishga yordam", "Помогает сравнить предложения и расходы"),
   L("Milliy qabılda qollaydı", "Supports national admission", "Milliy qabulda qo‘llab-quvvatlaydi", "Поддерживает при национальном поступлении"),
   L("Viza ushın mektep hújjetlerin tayarlaydı", "Prepares school documents for the visa", "Viza uchun maktab hujjatlarini tayyorlaydi", "Готовит школьные документы для визы")]),
 ("#047857", L("Pitkergennen keyin", "After graduation", "Bitirgandan keyin", "После выпуска"), L("Baylanısta bol", "Stay in touch", "Aloqada bo‘l", "Оставайся на связи"),
  [L("Nátiyjeńdi hám tájiriybeńdi kishi oqıwshılar menen bólis", "Share your result and story with younger students", "Natijang va tajribangni kichik o‘quvchilar bilan baham ko‘r", "Поделись результатом и опытом с младшими")],
  [L("Pitkeriwshiler haqqında maǵlıwmatlardı júrgizedi", "Keeps alumni records", "Bitiruvchilar haqidagi ma’lumotlarni yuritadi", "Ведёт данные о выпускниках"),
   L("Pitkeriwshilerdi oqıwshılar menen ushırasıwǵa shaqıradı", "Invites alumni to meet current students", "Bitiruvchilarni o‘quvchilar bilan uchrashuvga taklif qiladi", "Приглашает выпускников на встречи с учениками")]),
]

_I = {  # small stroke icons
 "tg": '<path d="M21 4L3 11l6 2 2 6 3-4 5 4z"/><path d="M9 13l8-6"/>',
 "talk": '<path d="M4 5h11a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H9l-4 3v-3H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z"/><path d="M17 9h3a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-1v3l-3.500-3H13"/>',
 "list": '<path d="M9 6h11M9 12h11M9 18h11"/><path d="M4 6h.01M4 12h.01M4 18h.01"/>',
 "pen": '<path d="M12 20h9"/><path d="M16.500 3.500a2.100 2.100 0 0 1 3 3L7 19l-4 1 1-4z"/>',
 "test": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>',
 "gift": '<rect x="3" y="8" width="18" height="13" rx="1"/><path d="M12 8v13M3 12h18"/><path d="M12 8c-2-4-6-4-6-1.500S9 8 12 8c3 0 6-1 6-1.500S14 4 12 8z"/>',
 "bell": '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10 21a2 2 0 0 0 4 0"/>',
 "doc": '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>',
 "grade": '<path d="M4 4h16v16H4z"/><path d="M8 15l2.500-6 2.500 6M9 13h3M15 10v4M13 12h4"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "check": '<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>',
 "code": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "eye": '<path d="M2 12s3.500-7 10-7 10 7 10 7-3.500 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.500 8.500l-2 5-5 2 2-5z"/>',
 "hand": '<path d="M12 21s-7-4.500-7-10a4 4 0 0 1 7-2.600A4 4 0 0 1 19 11c0 5.500-7 10-7 10z"/>',
 "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
 "users": '<circle cx="9" cy="8" r="3.500"/><path d="M2 20a7 7 0 0 1 14 0"/><circle cx="17" cy="9" r="2.500"/><path d="M17 14.500a5 5 0 0 1 5 5.500"/>',
}

FAMILY = [
 ("talk", L("Oqıwshı hám ata-analar ushın jeke ushırasıwlar", "One-to-one meetings for students and parents", "O‘quvchi va ota-onalar uchun yakkama-yakka uchrashuvlar", "Индивидуальные встречи для учеников и родителей")),
 ("list", L("Ózbekstan hám shet eldegi universitetler dizimi", "A university list in Uzbekistan and abroad", "O‘zbekiston va xorijdagi universitetlar ro‘yxati", "Список университетов в Узбекистане и за рубежом")),
 ("pen", L("Esse hám arzalarǵa pikir — biraq siz ushın jazılmaydı", "Feedback on essays and applications, never written for you", "Insho va arizalarga fikr — lekin siz uchun yozilmaydi", "Отзыв на эссе и заявки — но никогда не вместо вас")),
 ("test", L("Mektepte biypul IELTS dizimge alıw (rásmiy punkt)", "Free IELTS registration at school (official Registration Point)", "Maktabda bepul IELTS ro‘yxatdan o‘tish (rasmiy nuqta)", "Бесплатная регистрация на IELTS в школе (официальный пункт)")),
 ("gift", L("Grant hám stipendiyalardı izlew", "Scholarship and grant search", "Grant va stipendiyalarni izlash", "Поиск грантов и стипендий")),
 ("bell", L("Múddetlerdi baqlaw hám eskertiwler", "Deadline tracking and reminders", "Muddatlarni kuzatish va eslatmalar", "Контроль сроков и напоминания")),
]
UNIS = [
 ("doc", L("Mektep profili (PDF): oqıw baǵdarlaması, bahalaw, nátiyjeler", "School Profile (PDF): curriculum, grading, results", "Maktab profili (PDF): o‘quv dasturi, baholash, natijalar", "Профиль школы (PDF): программа, оценивание, результаты")),
 ("grade", L("Inglis tilindegi rásmiy transkript, 5 ballıq shkala túsindirilgen", "Official transcript in English, with the 5-point scale explained", "Ingliz tilidagi rasmiy transkript, 5 ballik shkala tushuntirilgan", "Официальный транскрипт на английском с пояснением 5-балльной шкалы")),
 ("mail", L("Másláhátshi hám muǵallimlerdiń usınıs xatları — tikkeley jiberiledi", "Counselor and teacher recommendations, sent directly", "Maslahatchi va o‘qituvchilarning tavsiyanomalari — to‘g‘ridan-to‘g‘ri yuboriladi", "Рекомендации консультанта и учителей — отправляются напрямую")),
 ("check", L("Soraw boyınsha bahalar hám hújjetlerdi tastıyıqlaw", "Verification of grades and documents on request", "So‘rov bo‘yicha baholar va hujjatlarni tasdiqlash", "Подтверждение оценок и документов по запросу")),
 ("code", L("College Board (CEEB) kodı: soralǵan; berilgenshe mektepti atı menen kórsetiń", "College Board (CEEB) code: requested; until issued, please list the school by name", "College Board (CEEB) kodi: so‘ralgan; berilgunga qadar maktabni nomi bilan ko‘rsating", "Код College Board (CEEB): запрошен; до его выдачи указывайте школу по названию")),
]
PRINCIPLES = [
 ("eye", "#0b5f78", L("Hadallıq", "Honesty", "Halollik", "Честность"),
  L("Bahalar hám jetiskenlikler qanday bolsa, sonday kórsetiledi. Saytdaǵı hár bir nátiyjeni tekseriwge boladı.", "Grades and achievements are reported exactly as they are. Every result on this website can be checked.", "Baholar va yutuqlar qanday bo‘lsa, shunday ko‘rsatiladi. Saytdagi har bir natijani tekshirish mumkin.", "Оценки и достижения указываются такими, какие они есть. Каждый результат на сайте можно проверить.")),
 ("compass", "#2563eb", L("Oqıwshınıń tańlawı", "The student’s choice", "O‘quvchining tanlovi", "Выбор ученика"),
  L("Biz másláhát beremiz, al sheshimdi oqıwshı hám shańaraǵı qabıllaydı.", "We advise; the student and family decide.", "Biz maslahat beramiz, qarorni esa o‘quvchi va oilasi qabul qiladi.", "Мы советуем, решают ученик и семья.")),
 ("pen", "#7c3aed", L("Óz miyneti", "Students’ own work", "O‘z mehnati", "Собственная работа"),
  L("Biz pikir aytamız, biraq esseni hámme waqıt oqıwshınıń ózi jazadı.", "We give feedback, but essays are always written by the student.", "Biz fikr bildiramiz, lekin inshoni har doim o‘quvchining o‘zi yozadi.", "Мы даём отзыв, но эссе всегда пишет сам ученик.")),
 ("hand", "#047857", L("Hámme ushın biypul", "Free for every student", "Hamma uchun bepul", "Бесплатно для всех"),
  L("Másláhát hám IELTS dizimge alıw oqıwshılarımız ushın biypul.", "Counselling and IELTS registration cost our students nothing.", "Maslahat va IELTS ro‘yxatdan o‘tish o‘quvchilarimiz uchun bepul.", "Консультации и регистрация на IELTS для наших учеников бесплатны.")),
 ("lock", "#b45309", L("Qupıyalıq", "Privacy", "Maxfiylik", "Конфиденциальность"),
  L("Oqıwshılardıń hújjetleri hám jeke maǵlıwmatları járiyalanbaydı.", "Students’ documents and personal details are never published.", "O‘quvchilarning hujjatlari va shaxsiy ma’lumotlari e’lon qilinmaydi.", "Документы и личные данные учеников не публикуются.")),
 ("users", "#a3202c", L("Hámmege birdey itibar", "Equal attention", "Hammaga teng e’tibor", "Равное внимание"),
  L("Tek eń kúshli oqıwshılarǵa emes, hár bir oqıwshıǵa járdem beriledi.", "Every student gets support, not only the top ones.", "Faqat eng kuchli o‘quvchilarga emas, har bir o‘quvchiga yordam beriladi.", "Поддержку получает каждый ученик, а не только лучшие.")),
]


def stats():
    tot_g = sum(n for _, n in G.YEARS)
    tot_u = sum(sum(1 for k, f in G.PLACED[y] if G.INST[k][5] == "uni") for y, _ in G.YEARS)
    inst = {k for y, _ in G.YEARS for k, f in G.PLACED[y]}
    unis = {o["uni"] for o in OF.OFFERS}
    top = sum(1 for o in OF.OFFERS if (OF.UNI.get(o["uni"], (None, None))[1] or 999) <= 100)
    yrs = f'{G.YEARS[0][0][-4:]}–{G.YEARS[-1][0][-4:]}'
    return dict(tot_g=tot_g, pct=round(tot_u / tot_g * 100), inst=len(inst), off=len(OF.OFFERS), unis=len(unis), top=top, yrs=yrs)


def _svg(p, s=22):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'


def body(i, up, href, ctx, tools):
    s = stats()
    tg = ctx["TG"]
    btns = (f'<a class="btn p" href="{tg}" rel="noopener">{_svg(_I["tg"], 18)}Telegram</a>'
            f'<a class="btn s" href="mailto:{ctx["EMAIL"]}">{_svg(_I["mail"], 18)}{ctx["EMAIL"]}</a>'
            f'<a class="btn s" href="tel:{ctx["PHONE"]}">{ctx["PHONE_TXT"]}</a>')
    hero = (f'<div class="cshero"><figure class="csph"><img src="{up}photos/leaders/alimbek-jumamuratov-p.jpg" alt="{T["name"][i]}" width="720" height="960" loading="eager"></figure>'
            f'<div class="cstx"><span class="cseb">{_svg(ICON[0], 16)}{T["eyebrow"][i]}</span><h2>{T["name"][i]}</h2><p class="csrole">{T["role"][i]}</p>'
            f'<blockquote class="csq">{T["mission"][i]}</blockquote><p class="btns">{btns}</p>'
            f'<a class="cslink" href="{href(ctx["PROFILE"])}">{T["profile_p"][i]} →</a></div></div>')
    tiles = [(f'{s["pct"]}%', T["r_uni"][i].format(g=s["tot_g"], y=s["yrs"]), href("graduates/")),
             (str(s["inst"]), T["r_inst"][i], href("graduates/")),
             (str(s["off"]), T["r_off"][i].format(u=s["unis"]), href("achievements/offers/")),
             (str(s["top"]), T["r_top"][i], href("achievements/offers/"))]
    rec = "".join(f'<a class="csst" href="{h}"><b>{n}</b><span>{l}</span></a>' for n, l, h in tiles)
    steps = "".join(
        f'<li class="csstep" style="--c:{c}"><span class="csdot">{k + 1}</span><div class="card cscard"><p class="csstage">{st[i]}</p><h3>{ti[i]}</h3>'
        f'<div class="cscols"><div><h4>{T["you"][i]}</h4><ul>' + "".join(f"<li>{x[i]}</li>" for x in a) + '</ul></div>'
        f'<div class="cswe"><h4>{T["we"][i]}</h4><ul>' + "".join(f"<li>{x[i]}</li>" for x in b) + '</ul></div></div></div></li>'
        for k, (c, st, ti, a, b) in enumerate(STEPS))
    li = lambda rows: "".join(f'<li><span class="csi">{_svg(_I[ic], 20)}</span><span>{t[i]}</span></li>' for ic, t in rows)
    serv = (f'<div class="cssv"><div class="card csfam"><h3>{T["fam_h"][i]}</h3><ul class="csul">{li(FAMILY)}</ul></div>'
            f'<div class="card csuni"><h3>{T["uni_h"][i]}</h3><ul class="csul">{li(UNIS)}</ul>'
            f'<p class="csum">{T["uni_mail"][i]} <a href="mailto:{ctx["EMAIL"]}">{ctx["EMAIL"]}</a></p>'
            f'<a class="btn p" href="{up}school-profile/">{T["sp"][i]} →</a></div></div>')
    prin = "".join(f'<div class="cspr" style="--c:{c}"><span class="csi">{_svg(_I[ic], 22)}</span><h3>{t[i]}</h3><p>{d[i]}</p></div>' for ic, c, t, d in PRINCIPLES)
    tool = "".join(f'<a class="cstl" href="{h}"><span>{n}</span><b aria-hidden="true">→</b></a>' for h, n in tools)
    return (hero
            + f'<h2>{T["rec_h"][i]}</h2><div class="csrec">{rec}</div><p class="note">{T["rec_note"][i]}</p>'
            + f'<h2>{T["road_h"][i]}</h2><p class="lead2">{T["road_p"][i]}</p><ol class="csroad">{steps}</ol>'
            + f'<h2>{T["serv_h"][i]}</h2>{serv}'
            + f'<h2>{T["prin_h"][i]}</h2><div class="csprs">{prin}</div><p class="btns" style="margin:-20px 0 36px"><a class="btn s" href="{href("policies/")}">{__import__("policies").NAME[i]} →</a></p>'
            + f'<h2>{T["tool_h"][i]}</h2><p>{T["tool_p"][i]}</p><div class="cstls">{tool}</div>'
            + f'<div class="cscta"><div><h2>{T["cta_h"][i]}</h2><p>{T["cta_p"][i]}</p></div><p class="btns">{btns}</p></div>'
            + f'<p class="btns"><a class="btn s" href="{href("achievements/offers/")}">{T["offers"][i]} →</a><a class="btn s" href="{href("graduates/")}">{T["grads"][i]} →</a></p>')
