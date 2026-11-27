# Achievements: hub page + Olympiads + Certificates (4 languages: kaa, en, uz, ru).
# Certificate numbers are counted automatically from graduates.py (CERT_SUBJ, CERTS, BEST_SAT).
# To add an olympiad result: copy one dict in OLYMP and fill it in.
#   year:  "2025/2026" (or None if unknown)
#   stage: "school" | "district" | "region" | "republic" | "intl"
#   award: "gold" | "silver" | "bronze" | "p1" | "p2" | "p3" | "final" | "prize"
#   subj:  subject key from SUBJ below (or None)
#   name:  olympiad name in 4 languages; who: optional student/class text in 4 languages (only with permission)
import collections
import graduates as G
import natcert as NC
import offers as OF

T4 = lambda a, b, c, d: (a, b, c, d)
SUBS = ["achievements/", "achievements/olympiads/", "achievements/certificates/", NC.SUB, OF.SUB, "achievements/sat/", "achievements/ielts/"]
NAME = {
 "achievements/": ("Jetiskenlikler", "Achievements", "Yutuqlar", "Достижения"),
 "achievements/olympiads/": ("Olimpiadalar", "Olympiads", "Olimpiadalar", "Олимпиады"),
 "achievements/certificates/": ("Sertifikatlar", "Certificates", "Sertifikatlar", "Сертификаты"),
 NC.SUB: NC.NAME,
 OF.SUB: OF.NAME,
 "achievements/sat/": ("SAT nátiyjeleri", "SAT results", "SAT natijalari", "Результаты SAT"),
 "achievements/ielts/": ("IELTS nátiyjeleri", "IELTS results", "IELTS natijalari", "Результаты IELTS"),
}
DESC = {
 "achievements/": ("Kegeyli rayonı qánigelestirilgen mektebi oqıwshılarınıń olimpiada hám sertifikat jetiskenlikleri.",
                   "Olympiad results and certificates earned by students of Kegeyli District Specialized School.",
                   "Kegeli tumani ixtisoslashtirilgan maktabi o‘quvchilarining olimpiada va sertifikat yutuqlari.",
                   "Олимпиадные результаты и сертификаты учеников Кегейлийской районной специализированной школы."),
 "achievements/olympiads/": ("Mektep oqıwshılarınıń pán olimpiadaları hám STEM jarıslarındaǵı nátiyjeleri.",
                             "Our students’ results at subject olympiads and STEM competitions.",
                             "O‘quvchilarimizning fan olimpiadalari va STEM musobaqalaridagi natijalari.",
                             "Результаты наших учеников на предметных олимпиадах и STEM-конкурсах."),
 "achievements/certificates/": ("Pitkeriwshilerdiń milliy, CEFR, IELTS hám SAT sertifikatları: pánler, dárejeler hám ósiw.",
                                "National, CEFR, IELTS and SAT certificates of our graduates: subjects, levels and growth.",
                                "Bitiruvchilarning milliy, CEFR, IELTS va SAT sertifikatlari: fanlar, darajalar va o‘sish.",
                                "Национальные, CEFR, IELTS и SAT сертификаты выпускников: предметы, уровни и рост."),
 NC.SUB: NC.DESC,
 OF.SUB: OF.DESC,
 "achievements/sat/": ("Oqıwshılarımızdıń rásmiy SAT nátiyjeleri: jalpı ball, bólimler, procentiller hám 8 bilim tarawı.",
                       "Our students’ official SAT results: total scores, sections, percentiles and the 8 skill areas.",
                       "O‘quvchilarimizning rasmiy SAT natijalari: umumiy ball, bo‘limlar, persentillar va 8 ta bilim sohasi.",
                       "Официальные результаты SAT наших учеников: общий балл, разделы, процентили и 8 областей знаний."),
 "achievements/ielts/": ("Oqıwshılarımızdıń rásmiy IELTS Academic nátiyjeleri: ulıwma ball, 4 bólim hám CEFR dárejesi.",
                         "Our students’ official IELTS Academic results: overall band, the 4 sections and CEFR level.",
                         "O‘quvchilarimizning rasmiy IELTS Academic natijalari: umumiy ball, 4 ta bo‘lim va CEFR darajasi.",
                         "Официальные результаты IELTS Academic наших учеников: общий балл, 4 раздела и уровень CEFR."),
}
ICON = {
 "achievements/": ('<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0zM17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>', "#b45309"),
 "achievements/olympiads/": ('<circle cx="12" cy="15" r="6"/><path d="M8.500 10.200L5 3h4l3 6 3-6h4l-3.500 7.200"/><path d="M12 12.500v5M10.500 13.500l1.500-1"/>', "#d97706"),
 OF.SUB: OF.ICON,
 NC.SUB: ('<circle cx="12" cy="9" r="6"/><path d="M9 14.5L7.5 22l4.500-2.500L16.500 22 15 14.500"/><path d="M10 9l1.500 1.500L14.500 7.500"/>', "#a3202c"),
 "achievements/sat/": ('<path d="M4 19V5M4 19h16M8 15l3-4 3 2 5-6"/>', "#7c3aed"),
 "achievements/ielts/": ('<path d="M4 5h16v11H9l-4 4v-4H4z"/><path d="M8 9h8M8 12h5"/>', "#d6452f"),
 "achievements/certificates/": ('<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M7 9h10M7 12h6"/><circle cx="16" cy="17" r="3"/><path d="M14.500 19.500L14 22l2-1 2 1-.5-2.500"/>', "#0b7a8f"),
}
SUBJ = {
 "math": ("Matematika", "Mathematics", "Matematika", "Математика"),
 "phys": ("Fizika", "Physics", "Fizika", "Физика"),
 "chem": ("Ximiya", "Chemistry", "Kimyo", "Химия"),
 "bio": ("Biologiya", "Biology", "Biologiya", "Биология"),
 "inf": ("Informatika", "Computer science", "Informatika", "Информатика"),
 "eng": ("Ingliz tili", "English", "Ingliz tili", "Английский язык"),
 "stem": ("STEM", "STEM", "STEM", "STEM"),
}
STAGE = {  # order = ladder from bottom to top
 "school": ("Mektep basqıshı", "School stage", "Maktab bosqichi", "Школьный этап"),
 "district": ("Rayon basqıshı", "District stage", "Tuman bosqichi", "Районный этап"),
 "region": ("Respublika (Qaraqalpaqstan) basqıshı", "Karakalpakstan stage", "Qoraqalpog‘iston bosqichi", "Этап Каракалпакстана"),
 "republic": ("Respublikalıq", "National (Uzbekistan)", "Respublika", "Республиканский"),
 "intl": ("Xalıqaralıq", "International", "Xalqaro", "Международный"),
}
AWARD = {  # text, colour
 "gold": (("Altın medal", "Gold medal", "Oltin medal", "Золотая медаль"), "#d4a017"),
 "silver": (("Gúmis medal", "Silver medal", "Kumush medal", "Серебряная медаль"), "#8a97a3"),
 "bronze": (("Bronza medal", "Bronze medal", "Bronza medal", "Бронзовая медаль"), "#b4693a"),
 "p1": (("1-orın", "1st place", "1-o‘rin", "1-е место"), "#d4a017"),
 "p2": (("2-orın", "2nd place", "2-o‘rin", "2-е место"), "#8a97a3"),
 "p3": (("3-orın", "3rd place", "3-o‘rin", "3-е место"), "#b4693a"),
 "final": (("Finalist", "Finalist", "Finalchi", "Финалист"), "#0b7a8f"),
 "prize": (("Sıylıq iyesi", "Prize-winner", "Sovrindor", "Призёр"), "#7c3aed"),
}
OLYMP = [
 dict(year="2022/2023", stage="republic", award="prize", subj="math",
      name=("Matematikadan Respublika pán olimpiadası, saralaw basqıshı", "Republican Mathematics Olympiad, qualifying round", "Matematika bo‘yicha Respublika fan olimpiadasi, saralash bosqichi", "Республиканская олимпиада по математике, отборочный этап"),
      who=("Artıqbay Saparniyazov (10-klass) hám Ádilbek Jumabaev (11-klass)", "Artıqbay Saparniyazov (Grade 10) and Adilbek Jumabaev (Grade 11)", "Artiqbay Saparniyazov (10-sinf) va Adilbek Jumabaev (11-sinf)", "Артыкбай Сапарниязов (10 класс) и Адилбек Жумабаев (11 класс)"),
      extra=("Ekewine de PDP University-diń 12 000 000 swmlıq grantı", "A 12,000,000 so‘m PDP University grant for each of them", "Ikkalasiga ham PDP Universityning 12 000 000 so‘mlik granti", "Каждому — грант PDP University на 12 000 000 сумов")),
 dict(year="2025/2026", stage="republic", award="bronze", subj="stem",
      name=("AKHU STEM olimpiadası", "AKHU STEM Olympiad", "AKHU STEM olimpiadasi", "Олимпиада AKHU STEM")),
 dict(year=None, stage="republic", award="final", subj="stem",
      name=("AKHU STEM olimpiadası", "AKHU STEM Olympiad", "AKHU STEM olimpiadasi", "Олимпиада AKHU STEM"),
      extra=("MAAB akademiyasınıń 25 mln sumlıq vaucheri", "25 million so‘m voucher from MAAB academy", "MAAB akademiyasining 25 mln so‘mlik vaucheri", "Ваучер академии MAAB на 25 млн сумов")),
 dict(year=None, stage="district", award="p3", subj=None,
      name=("Pán olimpiadası", "Subject olympiad", "Fan olimpiadasi", "Предметная олимпиада")),
]

X = {
 "tag": ("Mektep maqtanıshı", "Our pride", "Maktab faxri", "Гордость школы"),
 "lead": ("Oqıwshılarımızdıń olimpiadalardaǵı hám sertifikat imtihanlarındaǵı nátiyjeleri — bir orında.",
          "Our students’ olympiad results and certificate exam results — all in one place.",
          "O‘quvchilarimizning olimpiadalar va sertifikat imtihonlaridagi natijalari — bir joyda.",
          "Результаты наших учеников на олимпиадах и сертификационных экзаменах — в одном месте."),
 "h_cert": ("sertifikat (milliy hám CEFR)", "national and CEFR certificates", "ta sertifikat (milliy va CEFR)", "национальных и CEFR сертификатов"),
 "h_grad": ("pitkeriwshide sertifikat bar", "graduates with a certificate", "nafar bitiruvchida sertifikat bor", "выпускников с сертификатом"),
 "h_top": ("A hám A+ nátiyje", "A and A+ results", "ta A va A+ natija", "результатов A и A+"),
 "h_sat": ("eń joqarı SAT ballı", "best SAT score", "eng yuqori SAT bali", "лучший балл SAT"),
 "h_ol": ("olimpiada nátiyjesi", "olympiad results", "ta olimpiada natijasi", "олимпиадных результатов"),
 "h_med": ("medal", "medals", "ta medal", "медалей"),
 "open": ("Ashıw", "Open", "Ochish", "Открыть"),
 "hl_h": ("Eń jaqsı nátiyjeler", "Highlights", "Eng yaxshi natijalar", "Лучшие результаты"),
 "hl_sat": ("SAT ballı — mektebimizdiń eń joqarı nátiyjesi", "SAT — the best score in our school", "SAT bali — maktabimizning eng yuqori natijasi", "SAT — лучший результат школы"),
 "hl_ap": ("A+ milliy sertifikat", "A+ national certificates", "ta A+ milliy sertifikat", "национальных сертификатов A+"),
 "hl_ex": ("milliy sertifikat imtihanı 2025/2026 jılı ({p} aldıńǵı jılı)", "national certificate exams taken in 2025/2026 ({p} a year earlier)", "ta milliy sertifikat imtihoni 2025/2026 yilda ({p} avvalgi yili)", "экзаменов на нацсертификат в 2025/2026 ({p} годом ранее)"),
 "grad_link": ("Pitkeriwshiler qayerde oqıp atır", "Where our graduates study", "Bitiruvchilar qayerda o‘qimoqda", "Где учатся выпускники"),
 # olympiads
 "o_ladder": ("Olimpiada basqıshları", "Olympiad stages", "Olimpiada bosqichlari", "Этапы олимпиад"),
 "o_ladder_p": ("Hár basqıshta qansha nátiyje alǵanımız.", "How many results we have at each stage.", "Har bosqichda nechta natijamiz bor.", "Сколько у нас результатов на каждом этапе."),
 "o_list": ("Nátiyjeler", "Results", "Natijalar", "Результаты"),
 "o_all": ("Barlıǵı", "All", "Barchasi", "Все"),
 "o_noyear": ("Jılı kórsetilmegen", "Year not specified", "Yili ko‘rsatilmagan", "Год не указан"),
 "o_join_h": ("Olimpiadaǵa qatnasıwdı qálesez", "Want to take part?", "Olimpiadada qatnashmoqchimisiz?", "Хотите участвовать?"),
 "o_join": (("Pán muǵallimińizge aytıń — mektep basqıshı hár jılı ótkeriledi.", "Kúnine 25–45 minut tayarlanıń: ótken jıllardıń máseleleri eń jaqsı trenajer.", "Mektep basqıshında jeńgenler rayon, keyin Qaraqalpaqstan hám respublika basqıshına shıǵadı."),
            ("Tell your subject teacher — the school stage is held every year.", "Practise 25–45 minutes a day: past years’ problems are the best training.", "School-stage winners go on to the district, then Karakalpakstan and national stages."),
            ("Fan o‘qituvchingizga ayting — maktab bosqichi har yili o‘tkaziladi.", "Kuniga 25–45 daqiqa tayyorlaning: o‘tgan yillar masalalari eng yaxshi mashq.", "Maktab bosqichi g‘oliblari tuman, so‘ng Qoraqalpog‘iston va respublika bosqichiga chiqadi."),
            ("Скажите учителю по предмету — школьный этап проводится каждый год.", "Готовьтесь 25–45 минут в день: задачи прошлых лет — лучшая тренировка.", "Победители школьного этапа выходят на районный, затем на этап Каракалпакстана и республиканский.")),
 "o_timer": ("Oqıw taymerin ashıw", "Open the study timer", "O‘qish taymerini ochish", "Открыть таймер учёбы"),
 "o_note": ("Jańa nátiyjeler qosılıp baradı. Oqıwshılardıń atları tek olardıń ruqsatı menen járiyalanadı.",
            "New results are added as they come. Students’ names are published only with their permission.",
            "Yangi natijalar qo‘shib boriladi. O‘quvchilarning ismlari faqat ularning roziligi bilan e’lon qilinadi.",
            "Новые результаты добавляются по мере поступления. Имена учеников публикуются только с их согласия."),
 # certificates
 "c_grow": ("Jıldan jılǵa ósiw", "Growing every year", "Yildan yilga o‘sish", "Рост из года в год"),
 "c_grow_p": ("Hár bir pitkeriwshiler klasında alınǵan milliy hám CEFR sertifikatları sanı.", "Number of national and CEFR certificates held by each graduating class.", "Har bir bitiruvchilar sinfidagi milliy va CEFR sertifikatlari soni.", "Число национальных и CEFR сертификатов у каждого выпуска."),
 "c_grads": ("{a} / {n} pitkeriwshi", "{a} of {n} graduates", "{a} / {n} bitiruvchi", "{a} из {n} выпускников"),
 "c_subj": ("Pánler boyınsha", "By subject", "Fanlar bo‘yicha", "По предметам"),
 "c_subj_p": ("Hár pánnen alınǵan sertifikatlar hám olardıń dárejeleri.", "Certificates in each subject and their levels.", "Har bir fandan olingan sertifikatlar va ularning darajalari.", "Сертификаты по каждому предмету и их уровни."),
 "c_lvl": ("Milliy sertifikat dárejeleri", "National certificate levels", "Milliy sertifikat darajalari", "Уровни национальных сертификатов"),
 "c_cefr": ("Til sertifikatları (CEFR)", "Language certificates (CEFR)", "Til sertifikatlari (CEFR)", "Языковые сертификаты (CEFR)"),
 "c_intl": ("Xalıqaralıq imtihanlar", "International exams", "Xalqaro imtihonlar", "Международные экзамены"),
 "c_ielts": ("pitkeriwshi IELTS tapsırdı", "graduates took IELTS", "nafar bitiruvchi IELTS topshirdi", "выпускников сдали IELTS"),
 "c_satn": ("pitkeriwshi SAT tapsırdı", "graduates took the SAT", "nafar bitiruvchi SAT topshirdi", "выпускника сдали SAT"),
 "c_best": ("eń joqarı SAT ballı", "best SAT score", "eng yuqori SAT bali", "лучший балл SAT"),
 "c_prep": ("IELTS hám SAT tayarlıǵı", "Prepare for IELTS and SAT", "IELTS va SAT tayyorlovi", "Подготовка к IELTS и SAT"),
 "c_note": ("Derek: 2022/2023–2025/2026 jılları pitkeriwshileriniń maǵlıwmatları. Tek ulıwma sanlar kórsetiledi; bir pitkeriwshide bir neshe pán boyınsha sertifikat bolıwı múmkin.",
            "Source: records of the 2022/2023–2025/2026 graduates. Only totals are shown; one graduate can hold certificates in several subjects.",
            "Manba: 2022/2023–2025/2026 yillar bitiruvchilari ma’lumotlari. Faqat umumiy sonlar ko‘rsatiladi; bitta bitiruvchida bir nechta fandan sertifikat bo‘lishi mumkin.",
            "Источник: данные выпусков 2022/2023–2025/2026. Показаны только общие числа; у одного выпускника может быть несколько сертификатов."),
}

# SAT score reports (College Board). Domains: R&W = Information & Ideas, Craft & Structure, Expression of Ideas,
# Standard English Conventions; Math = Algebra, Advanced Math, Problem-Solving & Data Analysis, Geometry & Trigonometry.
# Domain value = performance band 1..7 (1: 200-360, 2: 370-410, 3: 420-480, 4: 490-540, 5: 550-600, 6: 610-670, 7: 680-800).
# Record locators from the reports are NOT published.
SHOW_NAMES = True
SAT = [
 dict(name="Dawitbek Arislanbaev", date="2026-11-07", total=1440, pct="95", rw=670, rwp="88", m=770, mp="97", dom=(5, 7, 7, 7, 7, 7, 7, 7)),
 dict(name="Gulbanu Ubaydullaeva", date="2025-09-13", total=1310, pct="87", rw=550, rwp="61", m=760, mp="96", dom=(4, 3, 5, 5, 7, 7, 7, 7)),
 dict(name="Sag‘inbay To‘rebaev", date="2025-03-08", total=1270, pct="84", rw=470, rwp="35", m=800, mp=">99", dom=(3, 2, 4, 2, 7, 7, 7, 7)),
 dict(name="Ayjamal Abdullaeva", date="2024-12-07", total=1100, pct="63", rw=410, rwp="17", m=690, mp="90", dom=(3, 2, 4, 1, 7, 7, 4, 5)),
 dict(name="Gulnura Jalgasbaeva", date="2025-10-04", total=1040, pct="54", rw=370, rwp="9", m=670, mp="88", dom=(3, 1, 3, 1, 5, 7, 7, 7)),
 dict(name="Ulasbek Xabibullaev", date="2026-03-14", total=990, pct="47", rw=380, rwp="11", m=610, mp="79", dom=(3, 1, 2, 1, 7, 5, 5, 4)),
 dict(name="Xurliman Paraxatova", date="2025-06-07", total=970, pct="43", rw=360, rwp="6", m=610, mp="79", dom=(1, 1, 3, 2, 6, 6, 4, 5)),
]
SAT_AVG = 1037   # 3-year average of all testers (College Board)
BEST = max([G.BEST_SAT] + [x["total"] for x in SAT])
BANDS = ["200–360", "370–410", "420–480", "490–540", "550–600", "610–670", "680–800"]
DOMS = [("Maǵlıwmat hám ideyalar", "Information and Ideas", "Ma’lumot va g‘oyalar", "Информация и идеи"),
        ("Dúzilis hám stil", "Craft and Structure", "Tuzilish va uslub", "Структура и стиль"),
        ("Pikirdi bildiriw", "Expression of Ideas", "Fikrni ifodalash", "Выражение идей"),
        ("Grammatika normaları", "Standard English Conventions", "Grammatika qoidalari", "Нормы английского языка"),
        ("Algebra", "Algebra", "Algebra", "Алгебра"),
        ("Joqarı matematika", "Advanced Math", "Murakkab matematika", "Продвинутая математика"),
        ("Másele sheshiw hám maǵlıwmat", "Problem-Solving and Data Analysis", "Masala yechish va ma’lumotlar tahlili", "Решение задач и анализ данных"),
        ("Geometriya hám trigonometriya", "Geometry and Trigonometry", "Geometriya va trigonometriya", "Геометрия и тригонометрия")]
SX = {
 "h": ("SAT nátiyjelerimiz", "Our SAT results", "SAT natijalarimiz", "Наши результаты SAT"),
 "p": ("Oqıwshılarımızdıń rásmiy College Board esabatlarınan alınǵan ballar. Tolıq maǵlıwmat ushın kartanı basıń.",
       "Scores from our students’ official College Board score reports. Tap a card to see the details.",
       "O‘quvchilarimizning rasmiy College Board hisobotlaridan olingan ballar. Batafsil ko‘rish uchun kartani bosing.",
       "Баллы из официальных отчётов College Board наших учеников. Нажмите на карточку, чтобы увидеть подробности."),
 "n": ("SAT nátiyjesi", "SAT results", "ta SAT natijasi", "результатов SAT"),
 "best": ("eń joqarı jalpı ball", "best total score", "eng yuqori umumiy ball", "лучший общий балл"),
 "bm": ("eń joqarı Matematika", "best Math score", "eng yuqori matematika", "лучший балл Math"),
 "o1k": ("1000+ ball alǵanlar", "scored 1000+", "nafari 1000+ ball olgan", "набрали 1000+"),
 "dist": ("400–1600 shkalasında", "On the 400–1600 scale", "400–1600 shkalasida", "На шкале 400–1600"),
 "avg": ("Dúnya boyınsha ortasha {a}", "World average {a}", "Dunyo bo‘yicha o‘rtacha {a}", "Среднее в мире {a}"),
 "total": ("Jalpı ball", "Total score", "Umumiy ball", "Общий балл"),
 "pct": ("{p}-procentil", "{p}th percentile", "{p}-persentil", "{p}-й процентиль"),
 "top": ("Top {t}%", "Top {t}%", "Top {t}%", "Топ {t}%"),
 "rw": ("Oqıw hám jazıw", "Reading and Writing", "O‘qish va yozish", "Чтение и письмо"),
 "math": ("Matematika", "Math", "Matematika", "Математика"),
 "perfect": ("Matematikadan 800/800", "Perfect Math 800/800", "Matematikadan 800/800", "Математика 800/800"),
 "more": ("Tolıǵıraq", "Details", "Batafsil", "Подробнее"),
 "skills": ("8 bilim tarawı boyınsha nátiyje", "Performance in the 8 skill areas", "8 ta bilim sohasi bo‘yicha natija", "Результаты по 8 областям знаний"),
 "date": ("Tapsırǵan sánesi", "Test date", "Topshirilgan sana", "Дата экзамена"),
 "prev_h": ("SAT nátiyjeleri", "SAT results", "SAT natijalari", "Результаты SAT"),
 "prev_p": ("{n} rásmiy nátiyje · eń joqarı {b}", "{n} official results · best {b}", "{n} ta rasmiy natija · eng yuqori {b}", "{n} официальных результатов · лучший {b}"),
 "all": ("Barlıq SAT nátiyjeleri", "See all SAT results", "Barcha SAT natijalari", "Все результаты SAT"),
 "prep": ("Siz de tayarlanıń: SAT tayarlıq betine ótiw", "Prepare too: open the SAT prep page", "Siz ham tayyorlaning: SAT tayyorlov sahifasi", "Готовьтесь и вы: страница подготовки к SAT"),
 "school_h": ("Mektep oqıwshılarınıń SAT nátiyjeleri", "SAT results of our students", "Maktab o‘quvchilarining SAT natijalari", "Результаты SAT наших учеников"),
 "school_p": ("Eń joqarı ball {b}. Mektep oqıwshıları SAT-tı tabıslı tapsırmaqta — siz de qosılıń.", "Best score {b}. Our students are already doing well on the SAT — you can too.", "Eng yuqori ball {b}. Maktab o‘quvchilari SATni muvaffaqiyatli topshirmoqda — siz ham qo‘shiling.", "Лучший балл {b}. Наши ученики уже успешно сдают SAT — присоединяйтесь."),
 "note": ("Derek: College Board rásmiy esabatları. Procentil — sońǵı 3 jılda tapsırǵan 12-klass oqıwshıları arasında. Ballar oqıwshılardıń ruqsatı menen járiyalandı.",
          "Source: official College Board score reports. Percentiles compare with 12th-grade test takers of the past 3 years. Scores are published with the students’ permission.",
          "Manba: rasmiy College Board hisobotlari. Persentil — so‘nggi 3 yilda topshirgan 12-sinf o‘quvchilari orasida. Ballar o‘quvchilarning roziligi bilan e’lon qilindi.",
          "Источник: официальные отчёты College Board. Процентиль — среди сдававших 12-классников за последние 3 года. Баллы опубликованы с согласия учеников."),
}
# IELTS Academic Test Report Forms. (name, test date, Listening, Reading, Writing, Speaking, Overall, CEFR)
# Candidate IDs, dates of birth and photos from the forms are NOT published.
IELTS = [
 ("Aynura Janabaeva", "2026-11-24", 9.0, 7.5, 6.5, 6.0, 7.5, "C1"),
 ("Dawitbek Arislanbaev", "2024-12-07", 9.0, 9.0, 7.0, 5.5, 7.5, "C1"),
 ("Dilnaz Kurbanbaeva", "2026-03-01", 7.5, 8.0, 6.5, 6.0, 7.0, "C1"),
 ("Aynura Turganbaeva", "2024-03-16", 7.0, 6.5, 6.0, 6.0, 6.5, "B2"),
 ("Gulbanu Ubaydullaeva", "2025-02-01", 6.5, 7.0, 6.0, 5.0, 6.0, "B2"),
 ("Xurshida Ismailova", "2024-09-07", 6.5, 6.0, 6.0, 5.5, 6.0, "B2"),
 ("Gulzar Bazarbaeva", "2024-08-08", 6.5, 6.0, 6.0, 5.5, 6.0, "B2"),
 ("Artiq Saparniyazov", "2024-03-07", 6.5, 5.5, 5.5, 5.5, 6.0, "B2"),
 ("Nargiza Seytekova", "2025-09-14", 5.5, 5.5, 5.5, 6.5, 6.0, "B2"),
 ("Ayjamal Abdullaeva", "2025-04-12", 5.5, 6.0, 6.0, 5.5, 6.0, "B2"),
 ("Muxammeddin Allambergenov", "2024-04-13", 7.0, 5.5, 5.0, 4.5, 5.5, "B2"),
 ("Dilafruz Kaldibaeva", "2024-12-07", 6.5, 5.5, 5.5, 5.0, 5.5, "B2"),
 ("Zuxratdin Muratbeav", "2024-10-26", 6.0, 5.0, 5.5, 6.0, 5.5, "B2"),
 ("Alfiya Dauletbaeva", "2024-10-26", 5.5, 5.5, 6.0, 5.5, 5.5, "B2"),
 ("Tursinay Tlepbaeva", "2024-10-26", 5.0, 5.0, 5.5, 5.5, 5.5, "B2"),
 ("Gulnur Abdullaeva", "2026-01-31", 4.5, 5.5, 6.0, 5.5, 5.5, "B2"),
]
SKILLS = [("Tıńlaw", "Listening", "Tinglash", "Аудирование", "#2a7fd1"), ("Oqıw", "Reading", "O‘qish", "Чтение", "#0b7a8f"),
          ("Jazıw", "Writing", "Yozish", "Письмо", "#7c3aed"), ("Sóylew", "Speaking", "Gapirish", "Говорение", "#d6452f")]
IX = {
 "h": ("IELTS nátiyjeleri", "IELTS results", "IELTS natijalari", "Результаты IELTS"),
 "p": ("Oqıwshılarımızdıń rásmiy IELTS Academic nátiyjeleri (Test Report Form).", "Our students’ official IELTS Academic results (Test Report Forms).",
       "O‘quvchilarimizning rasmiy IELTS Academic natijalari (Test Report Form).", "Официальные результаты IELTS Academic наших учеников (Test Report Form)."),
 "n": ("IELTS nátiyjesi", "IELTS results", "ta IELTS natijasi", "результатов IELTS"),
 "best": ("eń joqarı ulıwma ball", "best overall band", "eng yuqori umumiy ball", "лучший общий балл"),
 "c1": ("C1 dárejesi", "reached C1 level", "nafari C1 darajasi", "уровень C1"),
 "nine": ("bólimde 9.0 — maksimal ball", "sections scored a perfect 9.0", "ta bo‘limda 9.0 — maksimal ball", "разделов на максимальные 9.0"),
 "dist": ("Ulıwma ball boyınsha bólistiriliw", "How the overall bands are spread", "Umumiy ball bo‘yicha taqsimot", "Распределение общих баллов"),
 "avg_h": ("Ortasha ball — bólimler boyınsha", "Average score by section", "Bo‘limlar bo‘yicha o‘rtacha ball", "Средний балл по разделам"),
 "avg_p": ("Eń kúshli tárepimiz — {s}.", "Our strongest section is {s}.", "Eng kuchli tomonimiz — {s}.", "Наша сильная сторона — {s}."),
 "overall": ("Ulıwma", "Overall", "Umumiy", "Общий"),
 "perfect": ("{s}: 9.0", "Perfect {s} 9.0", "{s}: 9.0", "{s}: 9.0"),
 "stud": ("oqıwshı", "students", "nafar", "чел."),
 "note": ("Derek: rásmiy IELTS Test Report Form hújjetleri. Ballar oqıwshılardıń ruqsatı menen járiyalandı; jeke maǵlıwmatlar (ID, tuwılǵan sáne, súwret) kórsetilmeydi.",
          "Source: official IELTS Test Report Forms. Scores are published with the students’ permission; personal details (ID, date of birth, photo) are not shown.",
          "Manba: rasmiy IELTS Test Report Form hujjatlari. Ballar o‘quvchilarning roziligi bilan e’lon qilindi; shaxsiy ma’lumotlar (ID, tug‘ilgan sana, rasm) ko‘rsatilmaydi.",
          "Источник: официальные IELTS Test Report Form. Баллы опубликованы с согласия учеников; личные данные (ID, дата рождения, фото) не показываются."),
 "prev_p": ("{n} rásmiy nátiyje · eń joqarı {b}", "{n} official results · best {b}", "{n} ta rasmiy natija · eng yuqori {b}", "{n} официальных результатов · лучший {b}"),
 "all": ("Barlıq IELTS nátiyjeleri", "See all IELTS results", "Barcha IELTS natijalari", "Все результаты IELTS"),
 "prep": ("Siz de tayarlanıń: IELTS tayarlıq betine ótiw", "Prepare too: open the IELTS prep page", "Siz ham tayyorlaning: IELTS tayyorlov sahifasi", "Готовьтесь и вы: страница подготовки к IELTS"),
 "school_h": ("Mektep oqıwshılarınıń IELTS nátiyjeleri", "IELTS results of our students", "Maktab o‘quvchilarining IELTS natijalari", "Результаты IELTS наших учеников"),
 "school_p": ("Eń joqarı ball {b}, {c} oqıwshı C1 dárejesine jetti — siz de qosılıń.", "Best band {b}; {c} students reached C1 — you can too.", "Eng yuqori ball {b}, {c} nafar o‘quvchi C1 darajasiga erishdi — siz ham qo‘shiling.", "Лучший балл {b}, {c} ученика достигли C1 — присоединяйтесь."),
}

NAT_LV = ["A+", "A", "B+", "B", "C+", "C"]
CEFR_LV = ["C1", "B2", "B1"]
LVCOL = {"A+": "#a3202c", "A": "#d6452f", "B+": "#e07a1f", "B": "#f2b134", "C+": "#5aa3b8", "C": "#9cc3cf",
         "C1": "#4c1d95", "B2": "#7c3aed", "B1": "#b8a3f0"}
SCOL = {"M": "#2a7fd1", "P": "#0b7a8f", "C": "#047857", "B": "#2f8f5b", "H": "#b45309", "G": "#2a7fd1", "L": "#d97706",
        "E": "#7c3aed", "U": "#0b7a8f", "Q": "#d97706", "T": "#b23a48"}
EXAMS = (95, 32)   # national certificate exams taken in 2025/2026 and 2024/2025 (about page)

def _svg(p, s=22):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'

def _data():
    lv = collections.Counter(); bys = collections.defaultdict(collections.Counter); per = []
    for y, _ in G.YEARS:
        L = G.CERT_SUBJ.get(y, []); n = 0
        for g in L:
            for x in g:
                if x:
                    s, l = x.split(":"); lv[l] += 1; bys[s][l] += 1; n += 1
        per.append((y, n, G.CERTS[y]["with_"], len(G.PLACED[y]) if y in G.PLACED else 0))
    tot = sum(lv.values()); top = lv["A"] + lv["A+"]
    grads = sum(c["with_"] for c in G.CERTS.values())
    ielts = sum(c["ielts"] for c in G.CERTS.values()); sat = sum(c["sat"] for c in G.CERTS.values())
    return dict(lv=lv, bys=bys, per=per, tot=tot, top=top, grads=grads, ielts=ielts, sat=sat)

def _medals():
    return sum(1 for o in OLYMP if o["award"] in ("gold", "silver", "bronze"))

def tabs(sub, i, href):
    items = "".join(f'<a href="{href(k)}"' + (' aria-current="page"' if k == sub else "") + f'><span class="mi" style="--mc:{ICON[k][1]}">{_svg(ICON[k][0], 18)}</span>{NAME[k][i]}</a>' for k in SUBS)
    js = "<script>(function(){var a=document.querySelector('.abtabs [aria-current]');if(a){var n=a.parentNode;n.scrollLeft=a.offsetLeft-n.offsetLeft-16}})();</script>"
    return f'<nav class="abtabs" aria-label="{NAME["achievements/"][i]}">{items}</nav>{js}'

def _tiles(rows):
    return '<div class="actiles">' + "".join(f'<div class="actile" style="--ac:{c}"><span class="aci">{_svg(p)}</span><b>{v}</b><span>{l}</span></div>' for v, l, p, c in rows) + '</div>'

P_CERT = ICON["achievements/certificates/"][0]; P_OL = ICON["achievements/olympiads/"][0]
P_STAR = '<path d="M12 3l2.700 5.600 6.100.9-4.400 4.300 1 6.100L12 17l-5.400 2.900 1-6.100L3.200 9.500l6.100-.9z"/>'
P_USR = '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>'
P_SAT = '<path d="M4 19V5M4 19h16M8 15l3-4 3 2 5-6"/>'

def hub(i, href):
    d = _data(); y_last = G.YEARS[-1][0]
    tiles = _tiles([(d["tot"], X["h_cert"][i], P_CERT, "#0b7a8f"), (d["grads"], X["h_grad"][i], P_USR, "#2a7fd1"),
                    (d["top"], X["h_top"][i], P_STAR, "#a3202c"), (len(OLYMP), X["h_ol"][i], P_OL, "#d97706")])
    big = lambda k, stats, col: (f'<a class="acbig card" href="{href(k)}" style="--ac:{col}"><span class="acbi">{_svg(ICON[k][0], 30)}</span>'
                                 f'<div><h2>{NAME[k][i]}</h2><p>{DESC[k][i]}</p><div class="acbs">{stats}</div></div><span class="acgo">{X["open"][i]} →</span></a>')
    s_ol = f'<span><b>{len(OLYMP)}</b> {X["h_ol"][i]}</span><span><b>{_medals()}</b> {X["h_med"][i]}</span>'
    s_ce = f'<span><b>{d["tot"]}</b> {X["h_cert"][i]}</span><span><b>{BEST}</b> {X["h_sat"][i]}</span>'
    hl = [(str(BEST), X["hl_sat"][i], "#2a7fd1"), (str(d["lv"]["A+"]), X["hl_ap"][i], "#a3202c"),
          (_f(_isorted()[0][6], i), "IELTS — " + IX["best"][i], "#d6452f"), (str(EXAMS[0]), X["hl_ex"][i].format(p=EXAMS[1]), "#0b7a8f")]
    b0 = next((o for o in OLYMP if o["award"] in ("gold", "silver", "bronze")), None)
    if b0:
        hl.insert(0, ("🥉" if b0["award"] == "bronze" else "🥈" if b0["award"] == "silver" else "🥇", f'{AWARD[b0["award"]][0][i]} — {b0["name"][i]}' + (f' ({b0["year"]})' if b0["year"] else ""), AWARD[b0["award"]][1]))
    hls = "".join(f'<li style="--ac:{c}"><b>{v}</b><span>{t}</span></li>' for v, t, c in hl)
    return (f'{tabs("achievements/", i, href)}<p class="lead2">{X["lead"][i]}</p>{tiles}'
            f'<div class="acbigs">{big("achievements/olympiads/", s_ol, "#d97706")}{big("achievements/certificates/", s_ce, "#0b7a8f")}</div>'
            f'<a class="card satprev satban ofban" href="{href(OF.SUB)}"><div class="sph"><span class="acbi" style="--ac:{OF.ICON[1]}">{_svg(OF.ICON[0], 26)}</span><div><h3>{OF.NAME[i]} · {OF.stats()["n"]}</h3><p>{OF.X["hub"][i]}</p></div><span class="acgo2">→</span></div></a>'
            f'<h2>{X["hl_h"][i]}</h2><ul class="achl">{hls}</ul>'
            f'<div class="btns"><a class="btn s" href="{href("graduates/")}">{X["grad_link"][i]} →</a></div>')

def olympiads(i, href):
    keys = list(STAGE); cnt = collections.Counter(o["stage"] for o in OLYMP)
    tiles = _tiles([(len(OLYMP), X["h_ol"][i], P_OL, "#d97706"), (_medals(), X["h_med"][i], P_STAR, "#b4693a")])
    ladder = "".join(f'<li class="{"on" if cnt[k] else ""}" style="--w:{58 + n * 10}%"><span>{STAGE[k][i]}</span><b>{cnt[k] or "—"}</b></li>' for n, k in reversed(list(enumerate(keys))))
    years = []
    for o in OLYMP:
        if o["year"] not in years:
            years.append(o["year"])
    years.sort(key=lambda y: (y is None, -(int(y[:4]) if y else 0)))
    chips = f'<button type="button" class="acchip" aria-pressed="true" data-st="all">{X["o_all"][i]}</button>' + "".join(
        f'<button type="button" class="acchip" aria-pressed="false" data-st="{k}">{STAGE[k][i]}</button>' for k in keys if cnt[k])
    out = ""
    for y in years:
        cards = ""
        for o in [o for o in OLYMP if o["year"] == y]:
            at, col = AWARD[o["award"]]
            sj = f'<span class="acsj">{SUBJ[o["subj"]][i]}</span>' if o.get("subj") else ""
            ex = f'<p>{o["extra"][i]}</p>' if o.get("extra") else ""
            who = f'<p class="acwho">{o["who"][i]}</p>' if o.get("who") else ""
            cards += (f'<article class="acol card" data-st="{o["stage"]}" style="--ac:{col}"><span class="acmed">{_svg(P_OL, 26)}</span>'
                      f'<div><b class="acaw">{at[i]}</b><h3>{o["name"][i]}</h3><div class="acmeta"><span>{STAGE[o["stage"]][i]}</span>{sj}</div>{ex}{who}</div></article>')
        out += f'<div class="acyr" data-yr><h3 class="acyh">{y or X["o_noyear"][i]}</h3><div class="acols">{cards}</div></div>'
    tips = "".join(f'<li>{x}</li>' for x in X["o_join"][i])
    js = ("<script>(function(){var b=document.querySelectorAll('.acchip');b.forEach(function(x){x.addEventListener('click',function(){var s=x.dataset.st;"
          "b.forEach(function(y){y.setAttribute('aria-pressed',y===x)});document.querySelectorAll('.acol').forEach(function(c){c.hidden=!(s==='all'||c.dataset.st===s)});"
          "document.querySelectorAll('[data-yr]').forEach(function(g){g.hidden=!g.querySelector('.acol:not([hidden])')})})})})();</script>")
    return (f'{tabs("achievements/olympiads/", i, href)}{tiles}'
            f'<div class="acsplit"><div><h2>{X["o_list"][i]}</h2><div class="acchips">{chips}</div>{out}</div>'
            f'<aside><div class="card acladder"><h3>{X["o_ladder"][i]}</h3><p>{X["o_ladder_p"][i]}</p><ol>{ladder}</ol></div>'
            f'<div class="card acjoin"><h3>{X["o_join_h"][i]}</h3><ol>{tips}</ol><a class="btn p" href="{href("study/")}">{X["o_timer"][i]}</a></div></aside></div>'
            f'<p class="note">{X["o_note"][i]}</p>{js}')

def _nm(n):
    return n if SHOW_NAMES else " ".join(w[0] + "." for w in n.split())

def sat_block(i):
    import news as NW
    L = sorted(SAT, key=lambda x: (-x["total"], -x["m"]))
    if not L:
        return ""
    tier = lambda t: "#d4a017" if t >= 1400 else "#2a7fd1" if t >= 1200 else "#0b7a8f" if t >= 1000 else "#7c3aed"
    bm = max(x["m"] for x in L); o1k = sum(1 for x in L if x["total"] >= 1000)
    head = _tiles([(len(L), SX["n"][i], P_SAT, "#7c3aed"), (L[0]["total"], SX["best"][i], P_STAR, "#d4a017"),
                   (bm, SX["bm"][i], '<path d="M5 12h14M12 5v14"/>', "#2a7fd1"), (o1k, SX["o1k"][i], P_USR, "#0b7a8f")])
    # distribution strip
    X0 = lambda v: (v - 400) / 1200 * 100
    lv_last = []; dots = ""
    for x in sorted(L, key=lambda x: x["total"]):
        px = X0(x["total"]); lv = next((k for k, v in enumerate(lv_last) if px - v >= 11), len(lv_last))
        if lv == len(lv_last):
            lv_last.append(px)
        lv_last[lv] = px
        dots += f'<span class="sdot" style="left:{px:.2f}%;--ac:{tier(x["total"])}" title="{_nm(x["name"])}: {x["total"]}"><b style="bottom:{20 + lv * 18}px">{x["total"]}</b><s style="height:{14 + lv * 18}px"></s></span>'
    axh = 46 + len(lv_last) * 18
    strip = (f'<div class="card sdist"><h3>{SX["dist"][i]}</h3><div class="saxis" style="height:{axh}px"><i class="savg" style="left:{X0(SAT_AVG):.2f}%"><em>{SX["avg"][i].format(a=SAT_AVG)}</em></i>{dots}</div>'
             f'<div class="sticks">' + "".join(f'<span style="left:{X0(v):.2f}%">{v}</span>' for v in (400, 800, 1200, 1600)) + '</div></div>')
    cards = ""
    for r, x in enumerate(L, 1):
        col = tier(x["total"]); frac = (x["total"] - 400) / 1200; C = 2 * 3.14159 * 40
        ring = (f'<svg class="sring" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="40" class="r0"/>'
                f'<circle cx="50" cy="50" r="40" class="r1" style="stroke:{col}" stroke-dasharray="{C * frac:.1f} {C:.1f}" transform="rotate(-90 50 50)"/></svg>')
        pv = x["pct"].lstrip(">"); topv = 1 if x["pct"].startswith(">") else 100 - int(pv)
        badges = f'<span class="sbadge" style="--ac:{col}">{SX["top"][i].format(t=topv)}</span>'
        if x["m"] == 800:
            badges += f'<span class="sbadge gold">★ {SX["perfect"][i]}</span>'
        sec = lambda lab, v, pc, c: (f'<div class="ssec"><div class="ssl"><span>{lab}</span><b>{v}<small>/800</small></b></div>'
                                      f'<div class="ssb"><i style="width:{(v - 200) / 600 * 100:.1f}%;background:{c}"></i></div><small class="ssp">{SX["pct"][i].format(p=pc)}</small></div>')
        def dom(k, c):
            v = x["dom"][k]
            seg = "".join(f'<i class="{"on" if j < v else ""}"></i>' for j in range(7))
            return f'<li><span>{DOMS[k][i]}</span><div class="smeter" style="--ac:{c}">{seg}</div><small>{BANDS[v - 1]}</small></li>'
        rwc, mc = "#7c3aed", "#2a7fd1"
        det = (f'<div class="sdet"><h4>{SX["skills"][i]}</h4><div class="sdom"><div><h5 style="color:{rwc}">{SX["rw"][i]}</h5><ul>{"".join(dom(k, rwc) for k in range(4))}</ul></div>'
               f'<div><h5 style="color:{mc}">{SX["math"][i]}</h5><ul>{"".join(dom(k, mc) for k in range(4, 8))}</ul></div></div></div>')
        cards += (f'<details class="satcard card" style="--ac:{col}"><summary><span class="srank">{r}</span>'
                  f'<div class="sgauge">{ring}<div><b>{x["total"]}</b><small>/1600</small></div></div>'
                  f'<div class="sinfo"><h3>{_nm(x["name"])}</h3><p class="sdate">{SX["date"][i]}: {NW.fmt(x["date"], i)}</p><div class="sbadges">{badges}</div>'
                  f'{sec(SX["rw"][i], x["rw"], x["rwp"], rwc)}{sec(SX["math"][i], x["m"], x["mp"], mc)}<span class="smore">{SX["more"][i]}</span></div></summary>{det}</details>')
    return (f'<section class="satwall"><p>{SX["p"][i]}</p>{head}{strip}<div class="satgrid">{cards}</div>'
            f'<p class="note">{SX["note"][i]}</p></section>')

def sat_preview(i, href):
    L = sorted(SAT, key=lambda x: (-x["total"], -x["m"]))[:3]
    tier = lambda t: "#d4a017" if t >= 1400 else "#2a7fd1" if t >= 1200 else "#0b7a8f" if t >= 1000 else "#7c3aed"
    rows = "".join(f'<li style="--ac:{tier(x["total"])}"><span class="srank">{r}</span><b>{_nm(x["name"])}</b><em>{x["total"]}</em></li>' for r, x in enumerate(L, 1))
    return (f'<a class="card satprev" href="{href("achievements/sat/")}"><div class="sph"><span class="acbi" style="--ac:#7c3aed">{_svg(P_SAT, 28)}</span>'
            f'<div><h2>{SX["prev_h"][i]}</h2><p>{SX["prev_p"][i].format(n=len(SAT), b=BEST)}</p></div></div><ol>{rows}</ol><span class="btn p">{SX["all"][i]} →</span></a>')

def sat_page(i, href):
    return f'{tabs("achievements/sat/", i, href)}{sat_block(i)}<div class="btns"><a class="btn s" href="{href("abroad/sat/")}">{SX["prep"][i]} →</a></div>'

def sat_banner(i, href):
    return (f'<a class="card satprev satban" href="{href}"><div class="sph"><span class="acbi" style="--ac:#d4a017">{_svg(P_STAR, 26)}</span>'
            f'<div><h3>{SX["school_h"][i]}</h3><p>{SX["school_p"][i].format(b=BEST)}</p></div><span class="acgo2">→</span></div></a>')

def _f(v, i):
    return f"{v:.1f}" if i == 1 else f"{v:.1f}".replace(".", ",") if i == 3 else f"{v:.1f}"

def _itier(b):
    return "#d4a017" if b >= 7.5 else "#d6452f" if b >= 7 else "#2a7fd1" if b >= 6.5 else "#0b7a8f" if b >= 6 else "#7c3aed"

def _isorted():
    return sorted(IELTS, key=lambda x: (-x[6], -sum(x[2:6]), x[1]))

def ielts_block(i):
    import news as NW
    L = _isorted(); best = L[0][6]; c1 = sum(1 for x in L if x[7] == "C1")
    nines = sum(1 for x in L for v in x[2:6] if v == 9.0)
    head = _tiles([(len(L), IX["n"][i], ICON["achievements/ielts/"][0], "#d6452f"), (_f(best, i), IX["best"][i], P_STAR, "#d4a017"),
                   (c1, IX["c1"][i], P_USR, "#7c3aed"), (nines, IX["nine"][i], '<path d="M5 12l5 5L20 7"/>', "#2a7fd1")])
    # histogram of overall bands
    bands = [b / 2 for b in range(int(min(x[6] for x in L) * 2), int(max(x[6] for x in L) * 2) + 1)]
    cnt = collections.Counter(x[6] for x in L); mx = max(cnt.values())
    hist = "".join(f'<div class="ihb"><span class="ihv">{cnt[b] or ""}</span><i style="height:{max(cnt[b] / mx * 100, 3):.0f}%;background:{_itier(b)}"></i><b>{_f(b, i)}</b></div>' for b in bands)
    # averages per skill
    av = [sum(x[2 + k] for x in L) / len(L) for k in range(4)]; top = max(range(4), key=lambda k: av[k])
    avg = "".join(f'<div class="iav"><span>{SKILLS[k][i]}</span><div class="iab"><i style="width:{av[k] / 9 * 100:.1f}%;background:{SKILLS[k][4]}"></i></div><b>{_f(round(av[k], 1), i)}</b></div>' for k in range(4))
    charts = (f'<div class="actwo"><div class="card"><h3>{IX["dist"][i]}</h3><div class="ihist">{hist}</div></div>'
              f'<div class="card"><h3>{IX["avg_h"][i]}</h3>{avg}<p class="iavp">{IX["avg_p"][i].format(s=SKILLS[top][i])}</p></div></div>')
    cards = ""; C = 2 * 3.14159 * 40
    for r, x in enumerate(L, 1):
        col = _itier(x[6])
        ring = (f'<svg class="sring" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="40" class="r0"/>'
                f'<circle cx="50" cy="50" r="40" class="r1" style="stroke:{col}" stroke-dasharray="{C * x[6] / 9:.1f} {C:.1f}" transform="rotate(-90 50 50)"/></svg>')
        badges = f'<span class="sbadge" style="--ac:{"#7c3aed" if x[7] == "C1" else "#0b7a8f"}">CEFR {x[7]}</span>'
        for k in range(4):
            if x[2 + k] == 9.0:
                badges += f'<span class="sbadge gold">★ {IX["perfect"][i].format(s=SKILLS[k][i])}</span>'
        rows = "".join(f'<div class="isk"><span>{SKILLS[k][i]}</span><div class="iskb" style="--ac:{SKILLS[k][4]}">' + "".join(f'<i class="{"on" if j < x[2 + k] * 2 else ""}"></i>' for j in range(18)) +
                       f'</div><b style="color:{SKILLS[k][4]}">{_f(x[2 + k], i)}</b></div>' for k in range(4))
        cards += (f'<article class="ilcard card" style="--ac:{col}"><span class="srank">{r}</span><div class="ilt">'
                  f'<div class="sgauge">{ring}<div><b>{_f(x[6], i)}</b><small>/9</small></div></div>'
                  f'<div class="sinfo"><h3>{_nm(x[0])}</h3><p class="sdate">{SX["date"][i]}: {NW.fmt(x[1], i)}</p><div class="sbadges">{badges}</div></div></div>'
                  f'<div class="isks">{rows}</div></article>')
    return f'<section class="satwall"><p>{IX["p"][i]}</p>{head}{charts}<div class="satgrid">{cards}</div><p class="note">{IX["note"][i]}</p></section>'

def ielts_page(i, href):
    return f'{tabs("achievements/ielts/", i, href)}{ielts_block(i)}<div class="btns"><a class="btn s" href="{href("ielts/")}">{IX["prep"][i]} →</a></div>'

def ielts_preview(i, href):
    L = _isorted()[:3]
    rows = "".join(f'<li style="--ac:{_itier(x[6])}"><span class="srank">{r}</span><b>{_nm(x[0])}</b><em>{_f(x[6], i)}</em></li>' for r, x in enumerate(L, 1))
    return (f'<a class="card satprev ielprev" href="{href("achievements/ielts/")}"><div class="sph"><span class="acbi" style="--ac:#d6452f">{_svg(ICON["achievements/ielts/"][0], 28)}</span>'
            f'<div><h2>{IX["h"][i]}</h2><p>{IX["prev_p"][i].format(n=len(IELTS), b=_f(_isorted()[0][6], i))}</p></div></div><ol>{rows}</ol><span class="btn p">{IX["all"][i]} →</span></a>')

def ielts_banner(i, href):
    L = _isorted()
    return (f'<a class="card satprev satban" href="{href}"><div class="sph"><span class="acbi" style="--ac:#d4a017">{_svg(P_STAR, 26)}</span>'
            f'<div><h3>{IX["school_h"][i]}</h3><p>{IX["school_p"][i].format(b=_f(L[0][6], i), c=sum(1 for x in L if x[7] == "C1"))}</p></div><span class="acgo2">→</span></div></a>')

def certificates(i, href):
    d = _data()
    tiles = _tiles([(d["tot"], X["h_cert"][i], P_CERT, "#0b7a8f"), (d["grads"], X["h_grad"][i], P_USR, "#2a7fd1"),
                    (d["top"], X["h_top"][i], P_STAR, "#a3202c"), (BEST, X["h_sat"][i], P_SAT, "#7c3aed")])
    mx = max(n for _, n, _, _ in d["per"]) or 1
    grow = "".join(f'<div class="acgb"><span class="acgv">{n}</span><i style="height:{max(n / mx * 100, 2):.0f}%"></i><b>{y}</b><small>{X["c_grads"][i].format(a=w, n=t)}</small></div>'
                   for y, n, w, t in [(y, n, w, dict(G.YEARS)[y]) for y, n, w, _ in d["per"]])
    subs = sorted(d["bys"].items(), key=lambda kv: -sum(kv[1].values())); m1 = max(sum(c.values()) for _, c in subs)
    def row(s, c):
        n = sum(c.values()); order = CEFR_LV if s in ("E", "T") else NAT_LV
        segs = "".join(f'<i style="width:{c[l] / n * 100:.2f}%;background:{LVCOL[l]}" title="{l}: {c[l]}"></i>' for l in order if c[l])
        lab = " · ".join(f'{l} {c[l]}' for l in order if c[l])
        return (f'<li><div class="acsl"><span class="acdot" style="background:{SCOL.get(s, "#0b5f78")}"></span><b>{SUBJN[s][i]}</b><em>{n}</em></div>'
                f'<div class="acbar" style="width:{max(n / m1 * 100, 8):.1f}%">{segs}</div><small>{lab}</small></li>')
    srows = "".join(row(s, c) for s, c in subs)
    def levels(order):
        m = max(d["lv"][l] for l in order) or 1
        return "".join(f'<div class="aclv"><span class="aclt" style="background:{LVCOL[l]}">{l}</span><div class="aclb"><i style="width:{d["lv"][l] / m * 100:.0f}%;background:{LVCOL[l]}"></i></div><b>{d["lv"][l]}</b></div>' for l in order if d["lv"][l])
    intl = (f'<div class="acintl"><div><b>{d["ielts"]}</b><span>{X["c_ielts"][i]}</span></div><div><b>{d["sat"]}</b><span>{X["c_satn"][i]}</span></div>'
            f'<div><b>{BEST}</b><span>{X["c_best"][i]}</span></div></div>')
    nst = NC.stats()
    ncb = (f'<a class="card satprev satban ncban" href="{href(NC.SUB)}"><div class="sph"><span class="acbi" style="--ac:#a3202c">{_svg(ICON[NC.SUB][0], 26)}</span>'
           f'<div><h3>{NC.NAME[i]}</h3><p>{NC.X["prof_p"][i].format(s=NC.SUBJ["kaa"][i], n=nst["n"], t=nst["top"])}</p></div><span class="acgo2">→</span></div></a>') if nst else ""
    return (f'{tabs("achievements/certificates/", i, href)}{tiles}{ncb}<div class="prevs">{sat_preview(i, href)}{ielts_preview(i, href)}</div>'
            f'<div class="card acgrow"><h2>{X["c_grow"][i]}</h2><p>{X["c_grow_p"][i]}</p><div class="acgbars">{grow}</div>'
            f'<p class="acex"><b>{EXAMS[0]}</b> {X["hl_ex"][i].format(p=EXAMS[1])}</p></div>'
            f'<h2>{X["c_subj"][i]}</h2><p>{X["c_subj_p"][i]}</p><ul class="acsubj">{srows}</ul>'
            f'<div class="actwo"><div class="card"><h3>{X["c_lvl"][i]}</h3>{levels(NAT_LV)}</div><div class="card"><h3>{X["c_cefr"][i]}</h3>{levels(CEFR_LV)}</div></div>'
            f'<div class="card acintlc"><h3>{X["c_intl"][i]}</h3>{intl}<div class="btns"><a class="btn p" href="{href("ielts/")}">IELTS →</a><a class="btn s" href="{href("abroad/sat/")}">SAT →</a></div></div>'
            f'<p class="note">{X["c_note"][i]}</p>')

SUBJN = {}
def body(sub, i, href, subjn=None):
    if subjn:
        SUBJN.update(subjn)
    return {"achievements/": hub, "achievements/olympiads/": olympiads, "achievements/certificates/": certificates, "achievements/sat/": sat_page, "achievements/ielts/": ielts_page,
            NC.SUB: lambda i, href: NC.page(i, href, tabs), OF.SUB: lambda i, href: OF.page(i, href, tabs)}[sub](i, href)
