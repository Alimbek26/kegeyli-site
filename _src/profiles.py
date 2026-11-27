# Teacher profiles, same order as TEACHERS in teachers.py (from table 5 of "Kegeyli IM ko'rsatgich").
# Not published on purpose: birth year, salary bonuses (70% ustama), "did not take training".
# Each profile: edu = [(year, university key, "ba"/"ma")], spec = specialization key, train = last training year or None,
# ach = list of achievements, each as (kaa, en, uz, ru).

UNI = {
 "ksu": ("Qaraqalpaq mámleketlik universiteti", "Karakalpak State University", "Qoraqalpoq davlat universiteti", "Каракалпакский государственный университет"),
 "nspi": ("Nókis mámleketlik pedagogikalıq institutı", "Nukus State Pedagogical Institute", "Nukus davlat pedagogika instituti", "Нукусский государственный педагогический институт"),
 "nuu": ("Ózbekstan milliy universiteti", "National University of Uzbekistan", "O‘zbekiston milliy universiteti", "Национальный университет Узбекистана"),
 "uzswlu": ("Ózbekstan mámleketlik jáhán tilleri universiteti", "Uzbekistan State World Languages University", "O‘zbekiston davlat jahon tillari universiteti", "Узбекский государственный университет мировых языков"),
}
DEG = {"ba": ("bakalavriat", "Bachelor's", "bakalavriat", "бакалавриат"), "ma": ("magistratura", "Master's", "magistratura", "магистратура")}

SPEC = {
 "math": ("Matematika", "Mathematics", "Matematika", "Математика"),
 "eng_lit": ("Ingliz tili hám ádebiyatı", "English language and literature", "Ingliz tili va adabiyoti", "Английский язык и литература"),
 "foreign_eng": ("Shet tili hám ádebiyatı (ingliz tili)", "Foreign language and literature (English)", "Xorijiy til va adabiyoti (ingliz tili)", "Иностранный язык и литература (английский)"),
 "art_eng": ("Súwretlew óneri hám injenerlik grafikası", "Fine arts and engineering graphics", "Tasviriy san’at va muhandislik grafikasi", "Изобразительное искусство и инженерная графика"),
 "phys": ("Fizika", "Physics", "Fizika", "Физика"),
 "bioorg": ("Bioorganikalıq ximiya, tábiyiy hám fiziologiyalıq aktiv birikpeler ximiyası", "Bioorganic chemistry and chemistry of natural and physiologically active compounds", "Bioorganik kimyo, tabiiy va fiziologik faol birikmalar kimyosi", "Биоорганическая химия, химия природных и физиологически активных соединений"),
 "phil_kaa": ("Filologiya hám tillerdi oqıtıw: qaraqalpaq tili", "Philology and language teaching: Karakalpak", "Filologiya va tillarni o‘qitish: qoraqalpoq tili", "Филология и преподавание языков: каракалпакский язык"),
 "math_inf": ("Matematika hám informatika", "Mathematics and computer science", "Matematika va informatika", "Математика и информатика"),
 "method_sci": ("Anıq hám tábiyiy pánlerdi oqıtıw metodikası", "Methods of teaching exact and natural sciences", "Aniq va tabiiy fanlarni o‘qitish metodikasi", "Методика преподавания точных и естественных наук"),
 "bio": ("Biologiya", "Biology", "Biologiya", "Биология"),
 "pe": ("Dene tárbiyası", "Physical education", "Jismoniy madaniyat", "Физическая культура"),
 "edu_theory": ("Tálim hám tárbiya teoriyası hám metodikası", "Theory and methods of education", "Ta’lim va tarbiya nazariyasi va metodikasi", "Теория и методика обучения и воспитания"),
 "hist": ("Tariyx", "History", "Tarix", "История"),
 "inf_method": ("Informatika oqıtıw metodikası", "Methods of teaching computer science", "Informatika o‘qitish metodikasi", "Методика преподавания информатики"),
 "uzb_lit": ("Ózbek tili hám ádebiyatı", "Uzbek language and literature", "O‘zbek tili va adabiyoti", "Узбекский язык и литература"),
 "phil_eng": ("Filologiya: ingliz tili", "Philology: English", "Filologiya: ingliz tili", "Филология: английский язык"),
 "appl_math": ("Ámeliy matematika hám informatika", "Applied mathematics and computer science", "Amaliy matematika va informatika", "Прикладная математика и информатика"),
 "kaa_lit": ("Qaraqalpaq tili hám ádebiyatı", "Karakalpak language and literature", "Qoraqalpoq tili va adabiyoti", "Каракалпакский язык и литература"),
 "chem": ("Ximiya", "Chemistry", "Kimyo", "Химия"),
 "guide_eng": ("Gid-awdarmashılıq iskerligi (ingliz tili)", "Tour guiding and translation (English)", "Gid hamrohligi va tarjimonlik faoliyati (ingliz tili)", "Сопровождение гида и переводческая деятельность (английский)"),
 "phil_rus": ("Filologiya hám tillerdi oqıtıw: rus tili", "Philology and language teaching: Russian", "Filologiya va tillarni o‘qitish: rus tili", "Филология и преподавание языков: русский язык"),
 "bio_method": ("Biologiya oqıtıw metodikası", "Methods of teaching biology", "Biologiya o‘qitish metodikasi", "Методика преподавания биологии"),
 "nat_idea": ("Milliy ideya, ruwxıylıq tiykarları hám huqıq tálimi", "National idea, spirituality and law education", "Milliy g‘oya, ma’naviyat asoslari va huquq ta’limi", "Национальная идея, основы духовности и правовое образование"),
 "math_method": ("Matematika oqıtıw metodikası", "Methods of teaching mathematics", "Matematika o‘qitish metodikasi", "Методика преподавания математики"),
 "it_edu": ("Tálimde informaciyalıq texnologiyalar", "Information technology in education", "Ta’limda axborot texnologiyalari", "Информационные технологии в образовании"),
 "geo": ("Geografiya", "Geography", "Geografiya", "География"),
 "ling_uzb": ("Lingvistika (ózbek tili)", "Linguistics (Uzbek)", "Lingvistika (o‘zbek tili)", "Лингвистика (узбекский язык)"),
}

def nc(level, subj=None):
    """National certificate line."""
    s = {"math": ("matematika", "mathematics", "matematika", "математика"),
         "kaa": ("qaraqalpaq tili hám ádebiyatı", "Karakalpak language and literature", "qoraqalpoq tili va adabiyoti", "каракалпакский язык и литература"),
         "uzb": ("ózbek tili hám ádebiyatı", "Uzbek language and literature", "o‘zbek tili va adabiyoti", "узбекский язык и литература"),
         "native": ("ana tili hám ádebiyatı", "native language and literature", "ona tili va adabiyoti", "родной язык и литература"),
         "hist": ("tariyx", "history", "tarix", "история"),
         "eng": ("ingliz tili", "English", "ingliz tili", "английский язык"),
         "turk": ("túrk tili", "Turkish", "turk tili", "турецкий язык")}.get(subj)
    lv = f" {level}" if level else ""
    if s:
        return (f"Milliy sertifikat{lv} ({s[0]})", f"National certificate{lv} ({s[1]})", f"Milliy sertifikat{lv} ({s[2]})", f"Национальный сертификат{lv} ({s[3]})")
    return (f"Milliy sertifikat{lv}", f"National certificate{lv}", f"Milliy sertifikat{lv}", f"Национальный сертификат{lv}")

SAT = ("Xalıqaralıq SAT sertifikatı", "International SAT certificate", "Xalqaro SAT sertifikati", "Международный сертификат SAT")
HONOR = ("Agentliktiń Húrmet jarlıǵı", "Honorary Certificate of the Agency for Specialized Educational Institutions", "Agentlik Faxriy yorlig‘i", "Почётная грамота Агентства")
EXCEL_RK = ("Qaraqalpaqstan Respublikası Xalıq bilimlendiriw aǵlashısı", "Excellence in Public Education badge of the Republic of Karakalpakstan", "QR Xalq ta’limi a’lochisi", "Отличник народного образования Республики Каракалпакстан")
EXCEL_UZ = ("Ózbekstan Xalıq bilimlendiriw aǵlashısı", "Excellence in Public Education badge of Uzbekistan", "O‘zbekiston Xalq ta’limi a’lochisi", "Отличник народного образования Узбекистана")

PROFILES = [
 # 1 Aynazarov Ajiniyaz
 dict(edu=[(2018, "ksu", "ba")], spec="math", train=2022, ach=[SAT, nc("")]),
 # 2 Aynazarov Qurbanazar
 dict(edu=[(2015, "nspi", "ba"), (2022, "ksu", "ma")], spec="math", train=None, ach=[SAT, nc("A+", "math"), HONOR]),
 # 3 Aytmuratova Dilfuza
 dict(edu=[(2017, "nspi", "ba")], spec="eng_lit", train=2023, ach=[
   ("Xalıqaralıq TKT sertifikatı (1, 2, 3-modul, Band 3)", "International TKT certificate (modules 1–3, Band 3)", "Xalqaro TKT sertifikati (1, 2, 3-modul, Band 3)", "Международный сертификат TKT (модули 1–3, Band 3)"),
   ("Multilevel B2 sertifikatı", "Multilevel B2 certificate", "Multilevel B2 sertifikati", "Сертификат Multilevel B2")]),
 # 4 Amanbaeva Quralay
 dict(edu=[(2025, "nspi", "ba")], spec="foreign_eng", train=None, ach=[
   ("«Classroom management structures» maqalası «Лучшие интеллектуальные исследования» jurnalında jarıq kórdi (2025)", "Article “Classroom management structures” published in the journal «Лучшие интеллектуальные исследования» (2025)", "«Classroom management structures» maqolasi «Лучшие интеллектуальные исследования» jurnalida chop etilgan (2025)", "Статья «Classroom management structures» опубликована в журнале «Лучшие интеллектуальные исследования» (2025)"),
   ("Milliy B2 hám xalıqaralıq EF SET B2 sertifikatları", "National B2 and international EF SET B2 certificates", "Milliy B2 va xalqaro EF SET B2 sertifikatlari", "Национальный B2 и международный EF SET B2")]),
 # 5 Arzibaev Tolisbay
 dict(edu=[(2022, "nspi", "ba")], spec="art_eng", train=2026, ach=[]),
 # 6 Artikova Shaxnoza
 dict(edu=[(2018, "ksu", "ba")], spec="phys", train=2023, ach=[nc("B+")]),
 # 7 Atashov Aziz
 dict(edu=[(2010, "ksu", "ba"), (2012, "ksu", "ma")], spec="bioorg", train=None, ach=[
   ("Ximiya pánleri boyınsha filosofiya doktorı (PhD)", "Doctor of Philosophy (PhD) in Chemistry", "Kimyo fanlari bo‘yicha falsafa doktori (PhD)", "Доктор философии (PhD) по химическим наукам")]),
 # 8 Begalieva Jarqin
 dict(edu=[(2016, "ksu", "ba")], spec="phil_kaa", train=2022, ach=[nc("A", "kaa"),
   ("Eki xalıqaralıq ilimiy-ámeliy konferenciya toplamında maqalaları jarıq kórgen", "Articles published in two international research conference proceedings", "Ikki xalqaro ilmiy-amaliy konferensiya to‘plamida maqolalari chop etilgan", "Статьи в сборниках двух международных научно-практических конференций")]),
 # 9 Berdibaev Salamat
 dict(edu=[(2026, "nspi", "ba")], spec="math_inf", train=None, ach=[SAT,
   ("CEFR B2 sertifikatı", "CEFR B2 certificate", "CEFR B2 sertifikati", "Сертификат CEFR B2"),
   ("«Ulıǵbek» atındaǵı mámleketlik stipendiya iyesi (2025/2026)", "“Ulugbek” State Scholarship holder (2025/2026)", "«Ulug‘bek» nomidagi davlat stipendiyasi sohibi (2025/2026)", "Обладатель государственной стипендии имени Улугбека (2025/2026)")]),
 # 10 Dáwirxanov Jeńisbay
 dict(edu=[(2021, "nspi", "ba"), (2023, "nspi", "ma")], spec="method_sci", train=2026,
      pos=("Kásiplik awqam baslıǵı", "Chair of the trade union committee", "Kasaba uyushmasi raisi", "Председатель профсоюзного комитета"), ach=[
   ("«Eurasian Journal of Academic Research» xalıqaralıq jurnalında 1 hám respublikalıq konferenciyalarda 2 maqala", "1 article in the international “Eurasian Journal of Academic Research” and 2 at national conferences", "«Eurasian Journal of Academic Research» xalqaro jurnalida 1 ta va respublika konferensiyalarida 2 ta maqola", "1 статья в международном журнале «Eurasian Journal of Academic Research» и 2 на республиканских конференциях"),
   ("Ilimiy maqalaǵa avtorlıq gúwalıǵı", "Copyright certificate for a research article", "Ilmiy maqolaga mualliflik guvohnomasi", "Авторское свидетельство на научную статью")]),
 # 11 Dilmuratov Damir
 dict(edu=[(2026, "ksu", "ba")], spec="math", train=None, ach=[
   ("Al-Xorezmiy atındaǵı Xalıqaralıq matematika olimpiadasınıń altın medalı", "Gold medal, Al-Khwarizmi International Mathematical Olympiad", "Al-Xorazmiy nomidagi Xalqaro matematika olimpiadasi oltin medali", "Золотая медаль Международной математической олимпиады имени аль-Хорезми"),
   ("Xalıqaralıq hám respublikalıq matematika olimpiadalarında 6 altın, 9 gúmis, 5 bronza medal", "6 gold, 9 silver and 5 bronze medals at international and national maths olympiads", "Xalqaro va respublika matematika olimpiadalarida 6 oltin, 9 kumush, 5 bronza medal", "6 золотых, 9 серебряных и 5 бронзовых медалей на международных и республиканских олимпиадах по математике"),
   ("Prezident, Berdaq hám T. Sarımsaqov stipendiyalarınıń iyesi", "President’s, Berdakh and T. Sarimsakov scholarships", "Prezident, Berdaq va T. Sarimsoqov stipendiyalari sohibi", "Стипендиат Президента, стипендий имени Бердаха и Т. Саримсакова"),
   ("Scopus Q2 jurnalında birge avtorlıqta maqala, jáne 12 maqala hám 3 oqıw-metodikalıq qollanba", "Co-authored article in a Scopus Q2 journal, plus 12 articles and 3 teaching manuals", "Scopus Q2 jurnalida hammualliflikda maqola, yana 12 ta maqola va 3 ta o‘quv-metodik qo‘llanma", "Статья в соавторстве в журнале Scopus Q2, ещё 12 статей и 3 учебно-методических пособия"),
   ("SAT, Milliy sertifikat A+ hám IELTS 5.5", "SAT, National certificate A+ and IELTS 5.5", "SAT, Milliy sertifikat A+ va IELTS 5.5", "SAT, национальный сертификат A+ и IELTS 5.5"),
   ("«Úmit ushqını» kókirek belgisi", "“Umid uchquni” badge of honour", "«Umid uchquni» ko‘krak nishoni", "Нагрудный знак «Умид учкуни»"),
   ("EEM ushın programmanıń mámleketlik dizimnen ótkeriliwi haqqında gúwalıq (DGU 33417, 2024, birge avtor)", "State registration certificate for computer software (DGU 33417, 2024, co-author)", "EHM uchun dasturning davlat ro‘yxatidan o‘tkazilganligi to‘g‘risida guvohnoma (DGU 33417, 2024, hammuallif)", "Свидетельство о государственной регистрации программы для ЭВМ (DGU 33417, 2024, соавтор)")]),
 # 12 Elmuratova Toti
 dict(edu=[(2005, "ksu", "ba")], spec="bio", train=2026, ach=[]),
 # 13 Erejepov Zuxratdin
 dict(edu=[(2025, "nspi", "ba")], spec="pe", train=None, ach=[
   ("Oqıwshıları «Basshı kubogı» jarısınıń respublikalıq basqıshında mini-futbol boyınsha 2-orın aldı", "His students took 2nd place in mini-football at the national stage of the “Rahbar kubogi” competition", "O‘quvchilari «Rahbar kubogi» musobaqasining respublika bosqichida mini-futbol bo‘yicha 2-o‘rinni egalladi", "Его ученики заняли 2-е место по мини-футболу на республиканском этапе соревнований «Рахбар кубоги»")]),
 # 14 Esbergenov Atabek
 dict(edu=[(2021, "nspi", "ba"), (2023, "nspi", "ma")], spec="method_sci", train=None, ach=[SAT,
   ("Respublikalıq ilimiy-ámeliy konferenciyada maqalası jarıq kórgen (NMPI, 2023)", "Article published at a national research conference (NSPI, 2023)", "Respublika ilmiy-amaliy konferensiyasida maqolasi chop etilgan (NDPI, 2023)", "Статья на республиканской научно-практической конференции (НГПИ, 2023)")]),
 # 15 Jalgasova Orkenay
 dict(edu=[(2023, "nspi", "ba")], spec="foreign_eng", train=2023, ach=[
   ("Slovakiya Milliy stipendiyası grantı menen Pavol Jozef Šafárik universitetinde 1 semestr almasıw baǵdarlaması (2023)", "Slovak National Scholarship: one-semester exchange at Pavol Jozef Šafárik University (2023)", "Slovakiya Milliy stipendiyasi granti bilan Pavol Jozef Šafárik universitetida 1 semestr almashinuv dasturi (2023)", "Национальная стипендия Словакии: семестр по обмену в Университете Павла Йозефа Шафарика (2023)"),
   ("Italiyadaǵı Bolonya universitetinde magistraturada oqıǵan (2024–2026)", "Master’s studies at the University of Bologna, Italy (2024–2026)", "Italiyadagi Boloniya universitetida magistraturada o‘qigan (2024–2026)", "Магистратура Болонского университета, Италия (2024–2026)"),
   ("IELTS 6.5 hám milliy C1 (ingliz tili)", "IELTS 6.5 and national C1 (English)", "IELTS 6.5 va milliy C1 (ingliz tili)", "IELTS 6.5 и национальный C1 (английский)")]),
 # 16 Jangabaeva Nargiza
 dict(edu=[(2021, "nspi", "ba"), (2023, "nspi", "ma")], spec="edu_theory", train=2026, ach=[
   ("IT center «Fundamentals of Robotics» kursınıń sertifikatı", "“Fundamentals of Robotics” course certificate (IT Center)", "IT center «Fundamentals of Robotics» kursi sertifikati", "Сертификат курса «Fundamentals of Robotics» (IT Center)"),
   ("«ART, robototexnika hám jasalma intellekt» boyınsha sertifikat", "Certificate in “ART, robotics and artificial intelligence”", "«ART, robototexnika va sun’iy intellekt» bo‘yicha sertifikat", "Сертификат «ART, робототехника и искусственный интеллект»")]),
 # 17 Jarilqasinov Aynazar
 dict(edu=[(2024, "ksu", "ba"), (2026, "ksu", "ma")], spec="hist", train=None, ach=[nc("")]),
 # 18 Joldasbaev Bazarbay
 dict(edu=[(2020, "ksu", "ba"), (2022, "ksu", "ma")], spec="phil_kaa", train=2025, ach=[
   ("«Oyanıw» jaslar ádebiy tańlawınıń respublikalıq basqıshında húrmetli 3-orın", "Honourable 3rd place at the national stage of the “Uyg‘onish” youth literary contest", "«Uyg‘onish» yoshlar adabiy tanlovining respublika bosqichida faxrli 3-o‘rin", "Почётное 3-е место на республиканском этапе молодёжного литературного конкурса «Уйгониш»"),
   nc("", "native")]),
 # 19 Zaripbaev Ajinyaz
 dict(edu=[(2021, "nspi", "ba")], spec="inf_method", train=2026, ach=[
   ("Microsoft Certified Educator sertifikatı", "Microsoft Certified Educator", "Microsoft Certified Educator sertifikati", "Сертификат Microsoft Certified Educator")]),
 # 20 Ismaylova Gulmira
 dict(edu=[(2013, "nspi", "ba")], spec="uzb_lit", train=2022, ach=[
   ("Xalıq bilimlendiriw aǵlashısı", "Excellence in Public Education badge", "Xalq ta’limi a’lochisi", "Отличник народного образования"),
   ("«Ilm-pán iftixarı» kókirek belgisi", "“Ilm-fan iftixori” badge of honour", "«Ilm-fan iftixori» ko‘krak nishoni", "Нагрудный знак «Илм-фан ифтихори»"),
   ("«Jıldıń eń jaqsı ózbek tili muǵallimi» tańlawınıń Qaraqalpaqstan basqıshında 2-orın", "2nd place, Karakalpakstan stage of the “Best Uzbek Language Teacher of the Year” contest", "«Yilning eng yaxshi o‘zbek tili o‘qituvchisi» tanlovining Qoraqalpog‘iston bosqichida 2-o‘rin", "2-е место на этапе Каракалпакстана конкурса «Лучший учитель узбекского языка года»"),
   ("«Nutqimizda so‘zlar jilosi» respublikalıq tańlawınıń I dárejeli diplomı (2020)", "1st-degree diploma, national contest “Nutqimizda so‘zlar jilosi” (2020)", "«Nutqimizda so‘zlar jilosi» respublika ko‘rik-tanlovining I darajali diplomi (2020)", "Диплом I степени республиканского конкурса «Нуткимизда сўзлар жилоси» (2020)"),
   HONOR, nc("", "uzb")]),
 # 21 Keunimjaev Abdug'aniy
 dict(edu=[(2023, "nuu", "ba")], spec="phys", train=2026, ach=[nc("A+"),
   ("TMU olimpiadasınıń sıylıq iyesi", "Prize-winner of the TSU olympiad", "TDU olimpiadasi sovrindori", "Призёр олимпиады ТГУ")]),
 # 22 Mamutova Zinexan
 dict(edu=[(2014, "ksu", "ba")], spec="phil_eng", train=2023, ach=[
   ("Britaniya Keńesiniń «School Champions» joybarınıń aǵzası", "Member of the British Council “School Champions” project", "Britaniya Kengashi «School Champions» loyihasi a’zosi", "Участник проекта Британского совета «School Champions»"),
   ("TESOL Core Certificate Program sertifikatı", "TESOL Core Certificate Program", "TESOL Core Certificate Program sertifikati", "Сертификат TESOL Core Certificate Program"),
   ("«English Speaking Nation: Silk Road» konferenciyasınıń bayanatshısı (2023)", "Speaker at the “English Speaking Nation: Silk Road” conference (2023)", "«English Speaking Nation: Silk Road» konferensiyasi ma’ruzachisi (2023)", "Докладчик конференции «English Speaking Nation: Silk Road» (2023)"),
   ("Is tájiriybesi Qaraqalpaqstan kóleminde keń tarqatılǵan", "Teaching practice shared across Karakalpakstan as best practice", "Ish tajribasi Qoraqalpog‘iston miqyosida ommalashtirilgan", "Опыт работы распространён в масштабах Каракалпакстана")]),
 # 23 Nazbergenova Ziyada
 dict(edu=[(2010, "nspi", "ba")], spec="eng_lit", train=2022, ach=[EXCEL_RK,
   ("2022-jılı American Councils ESN joybarında ingliz tili muǵallimleriniń treneri", "Trainer of English teachers in the American Councils ESN project (2022)", "2022-yil American Councils ESN loyihasida ingliz tili o‘qituvchilari treneri", "Тренер учителей английского языка в проекте American Councils ESN (2022)"),
   ("TQUK Level 5 TEFL sertifikatı", "TQUK Level 5 TEFL certificate", "TQUK Level 5 TEFL sertifikati", "Сертификат TQUK Level 5 TEFL"),
   ("TESOL xalıqaralıq konferenciyasınıń qatnasıwshısı", "Participant of the international TESOL conference", "TESOL xalqaro konferensiyasi ishtirokchisi", "Участник международной конференции TESOL")]),
 # 24 Orazalieva Risgul
 dict(edu=[(2016, "ksu", "ba")], spec="appl_math", train=None, ach=[
   ("Oqıwshısı AKHU STEM olimpiadasınıń finalına shıqtı (MAAB akademiyasınıń 25 mln sumlıq vaucheri)", "Her student reached the final of the AKHU STEM Olympiad (25 million so‘m MAAB academy voucher)", "O‘quvchisi AKHU STEM olimpiadasining finalida qatnashdi (MAAB akademiyasining 25 mln so‘mlik vaucheri)", "Её ученик вышел в финал олимпиады AKHU STEM (ваучер академии MAAB на 25 млн сумов)"),
   ("Oqıwshısı pán olimpiadasınıń rayon basqıshında 3-orın aldı", "Her student took 3rd place at the district stage of the subject olympiad", "O‘quvchisi fan olimpiadasining tuman bosqichida 3-o‘rinni egalladi", "Её ученик занял 3-е место на районном этапе предметной олимпиады"),
   ("Xalıqaralıq GRE hám milliy B1 (ingliz tili) sertifikatları", "International GRE and national B1 (English) certificates", "Xalqaro GRE va milliy B1 (ingliz tili) sertifikatlari", "Международный GRE и национальный B1 (английский)")]),
 # 25 Oserbaeva Zulfiya
 dict(edu=[(2019, "ksu", "ba")], spec="foreign_eng", train=None, ach=[
   ("Xalıqaralıq Highfield Level 5 TEFL hám milliy C1 sertifikatları", "International Highfield Level 5 TEFL and national C1 certificates", "Xalqaro Highfield Level 5 TEFL va milliy C1 sertifikatlari", "Международный Highfield Level 5 TEFL и национальный C1"),
   ("Ilǵar is tájiriybesi rayon kóleminde tarqatılǵan (2026)", "Best practice shared at district level (2026)", "Ilg‘or ish tajribasi tuman miqyosida ommalashtirilgan (2026)", "Передовой опыт распространён на районном уровне (2026)")]),
 # 26 Pirimbetov Alpisbay
 dict(edu=[(1999, "ksu", "ba")], spec="math", train=2025, ach=[
   ("Qánigelestirilgen mektepler ushın matematika sabaqlıqlarınıń qaraqalpaq tiline awdarmasınıń redaktorı", "Editor of the Karakalpak translation of maths textbooks for specialized schools", "Ixtisoslashtirilgan maktablar uchun matematika darsliklarining qoraqalpoq tiliga tarjima muharriri", "Редактор перевода учебников математики для специализированных школ на каракалпакский язык"),
   ("SAT 1140", "SAT 1140", "SAT 1140", "SAT 1140")]),
 # 27 Salieva Elmira
 dict(edu=[(2019, "nspi", "ba")], spec="kaa_lit", train=None, ach=[
   ("«Óz kásibiniń pidayısı» kókirek belgisi", "“Devoted to the Profession” badge of honour", "«O‘z kasbining fidoyisi» ko‘krak nishoni", "Нагрудный знак «Преданный своей профессии»"),
   nc("A", "kaa")]),
 # 28 Saparov Mansur
 dict(edu=[(2019, "nspi", "ba"), (2023, "nspi", "ma")], spec="math", train=None, ach=[SAT, nc("A"),
   ("Ilimiy maqala avtorı", "Author of a research article", "Ilmiy maqola muallifi", "Автор научной статьи")]),
 # 29 Sarsenbaev Daniyar
 dict(edu=[(2016, "ksu", "ba")], spec="phys", train=2020, ach=[nc("")]),
 # 30 Seytnazarov Temirbek
 dict(edu=[(2006, "ksu", "ba")], spec="hist", train=2026, ach=[
   ("«Jaslardı watansúyiwshilik ruwxında tárbiyalaǵanı ushın» medalı", "Medal “For Raising Youth in the Spirit of Patriotism”", "«Yoshlarni vatanparvarlik ruhida tarbiyalash uchun» medali", "Медаль «За воспитание молодёжи в духе патриотизма»"),
   ("«Pidayı watansúyer» kókirek belgisi", "“Devoted Patriot” badge of honour", "«Fidoyi vatanparvar» ko‘krak nishoni", "Нагрудный знак «Фидойи ватанпарвар»"),
   ("Milliy gvardiyanıń alǵıs xatı", "Letter of gratitude from the National Guard", "Milliy gvardiya tashakkurnomasi", "Благодарственное письмо Национальной гвардии")]),
 # 31 Tajimuratova Ziyada
 dict(edu=[(1997, "ksu", "ba")], spec="chem", train=2025, ach=[nc("B")]),
 # 32 Temirxanova Aynura
 dict(edu=[(2025, "ksu", "ba")], spec="guide_eng", train=None, ach=[
   ("Webster universitetiniń magistraturasın pitkergen (MA TESOL, 2026)", "Master’s degree from Webster University (MA TESOL, 2026)", "Vebster universiteti magistraturasini tamomlagan (MA TESOL, 2026)", "Магистратура Университета Вебстера (MA TESOL, 2026)"),
   ("IELTS 6.5 hám milliy C1", "IELTS 6.5 and national C1", "IELTS 6.5 va milliy C1", "IELTS 6.5 и национальный C1")]),
 # 33 Tulepov Sultan
 dict(edu=[(2016, "ksu", "ba"), (2023, "nspi", "ma")], spec="hist", train=None, ach=[nc("A+", "hist"), nc("B1", "turk"),
   ("Ilimiy maqalalar avtorı", "Author of research articles", "Ilmiy maqolalar muallifi", "Автор научных статей")]),
 # 34 Uzaqbaeva Aysanem
 dict(edu=[(2023, "uzswlu", "ba")], spec="phil_rus", train=None, ach=[
   ("Milliy C1 hám IELTS sertifikatları", "National C1 and IELTS certificates", "Milliy C1 va IELTS sertifikatlari", "Национальный C1 и сертификат IELTS"),
   ("TRKI III xalıqaralıq rus tili sertifikatı", "TRKI III international Russian language certificate", "TRKI III xalqaro rus tili sertifikati", "Международный сертификат ТРКИ III"),
   ("Xalıqaralıq jaslar festivali-2026 qatnasıwshısı (Ekaterinburg)", "Participant of the International Youth Festival 2026 (Yekaterinburg)", "Xalqaro yoshlar festivali-2026 ishtirokchisi (Yekaterinburg)", "Участник Международного молодёжного фестиваля 2026 (Екатеринбург)")]),
 # 35 Umirbekova Fatima
 dict(edu=[(2022, "nspi", "ba")], spec="bio_method", train=None, ach=[]),
 # 36 Uteniyazova Abadan
 dict(edu=[(2016, "ksu", "ba")], spec="chem", train=2025, ach=[nc("B+")]),
 # 37 Uteshova Gulbaxar
 dict(edu=[(2025, "ksu", "ba")], spec="nat_idea", train=None, ach=[
   ("Coursera platformasındaǵı ámeliy kurs sertifikatı", "Coursera course certificate", "Coursera platformasidagi amaliy kurs sertifikati", "Сертификат практического курса Coursera")]),
 # 38 Xudaybergenova Qumar
 dict(edu=[(2019, "nspi", "ba")], spec="math_method", train=None, ach=[nc("B+"), SAT]),
 # 39 Shukirillaev Naurizbay
 dict(edu=[(2021, "nspi", "ba"), (2023, "nspi", "ma")], spec="it_edu", train=2025, ach=[
   ("IC3 Digital Literacy Master sertifikatı", "IC3 Digital Literacy Master certificate", "IC3 Digital Literacy Master sertifikati", "Сертификат IC3 Digital Literacy Master")]),
 # 40 Qarlibaeva Gulshaxra
 dict(edu=[(2015, "ksu", "ba")], spec="phil_kaa", train=2022, ach=[EXCEL_UZ, nc("B+", "kaa")]),
 # 41 Qudaybergenov Maxmut
 dict(edu=[(2022, "ksu", "ba")], spec="geo", train=2025, ach=[nc("B+")]),
 # 42 Qurbanbaeva Malika
 dict(edu=[(2020, "ksu", "ba"), (2022, "ksu", "ma")], spec="phys", train=None, ach=[nc("B+"), nc("B1", "eng")]),
 # 43 Qutlimuratov Sarmanbek
 dict(edu=[(2021, "ksu", "ba"), (2023, "ksu", "ma")], spec="ling_uzb", train=2023, ach=[nc("B+", "uzb"),
   ("Bir neshe xalıqaralıq ilimiy-ámeliy konferenciyalardıń qatnasıwshısı", "Participant of several international research conferences", "Bir nechta xalqaro ilmiy-amaliy anjumanlar ishtirokchisi", "Участник нескольких международных научно-практических конференций")]),
]
