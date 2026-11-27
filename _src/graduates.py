# Graduates data (from tables 8.1–8.4 and 9 of "Kegeyli IM ko'rsatgich"). Only totals are published — no names, no scores.
# For each graduating year: number of graduates, and (institution key, field category) for those continuing education.

YEARS = [  # (label, graduates)
 ("2022/2023", 14), ("2023/2024", 31), ("2024/2025", 40), ("2025/2026", 56),
]

# (institution, field category) per graduate who continues studying
PLACED = {
 "2022/2023": [("art_nukus","soc"),("nstu","eng"),("ksu","econ"),("ksu","eng"),("nstu","econ"),("navoiu","edu"),("coll_health2","med"),("ksu","sci"),
               ("ksu","eng"),("art","soc"),("nstu","eng"),("nspi","sci"),("nstu","econ"),("ksu","lang")],
 "2023/2024": [("nii","edu"),("kaai","econ"),("ksu","sci"),("tsue","econ"),("kaai","eng"),("ksu","econ"),("ksu","eng"),("nspi","sci"),("nspi","edu"),
               ("nspi","edu"),("mil","mil"),("ksu","econ"),("nii","edu"),("uzswlu","lang"),("nspi","sci"),("ksu","soc"),("nii","edu"),("urgmi","med"),
               ("ksu","sci"),("nspi","sci"),("nii","edu"),("ksu","eng"),("ksu","econ"),("ksu","soc"),("ksu","lang"),("ubs","med"),("navoiu","med"),
               ("ksu","sci"),("ksu","soc"),("nstu","eng"),("keg3","eng")],
 "2024/2025": [("mephi","eng"),("tsue","econ"),("ksu","econ"),("ksu","lang"),("kmi","med"),("tsmu_ch","med"),("uzswlu","lang"),("ksu","soc"),
               ("ksu","lang"),("tuit","eng"),("ksu","econ"),("ksu","sci"),("nuu","sci"),("ksu","soc"),("ksu","lang"),("ksu","soc"),("samsmu","med"),
               ("nspi","edu"),("ksu","lang"),("ksu","sci"),("ksu","sci"),("ksu","eng"),("mil","mil"),("ksu","edu"),("ksu","sci"),("kmi","med"),
               ("nuu_new","econ"),("ksu","lang"),("ksu","econ"),("kaai","econ"),("coll_aral","med"),("uit","soc"),("coll_aral","med"),("ksu","lang"),
               ("ksu","econ"),("coll_health1","med"),("ksu","edu"),("coll_health2","med"),("mil","mil")],
 "2025/2026": [("ksu","econ"),("cyber","eng"),("karshi","soc"),("asmi","med"),("kmi","med"),("ksu","sci"),("ksu","econ"),("kmi","med"),("uzswlu","lang"),
               ("ksu","econ"),("ksu","econ"),("ksu","sci"),("ksu","econ"),("uzswlu","lang"),("ksu","lang"),("samvet_nukus","econ"),("nstu","eng"),
               ("ksu","sci"),("ksu","lang"),("samspi","lang"),("ksu","econ"),("namangan","soc"),("ksu","lang"),("nspi","lang"),("ksu","econ"),
               ("urgu","soc"),("art_nukus","soc"),("nstu","eng"),("nspi","edu"),("tsmu_ch","med"),("ksu","econ"),("ranch","econ"),("ksu","sci"),
               ("nstu","econ"),("uit","eng"),("nspi","lang"),("nstu","econ"),("urgmi","med"),("ksu","sci"),("nspi","lang"),("ksu","lang"),("uit","edu"),
               ("ksu","lang"),("ksu","soc"),("ksu","sci"),("ksu","econ"),("ksu","sci"),("nspi","edu"),("ksu","econ"),("ksu","lang"),("ksu","lang"),
               ("nstu","econ"),("termiz","soc")]
}

# key: (kaa, en, uz, ru, city key, kind) kind: "uni" or "college"
INST = {
 "ksu": ("Berdaq atındaǵı Qaraqalpaq mámleketlik universiteti", "Karakalpak State University", "Berdaq nomidagi Qoraqalpoq davlat universiteti", "Каракалпакский государственный университет им. Бердаха", "nukus", "uni"),
 "nspi": ("Ájiniyaz atındaǵı Nókis mámleketlik pedagogikalıq institutı", "Nukus State Pedagogical Institute", "Ajiniyoz nomidagi Nukus davlat pedagogika instituti", "Нукусский государственный педагогический институт", "nukus", "uni"),
 "nstu": ("Nókis mámleketlik texnika universiteti", "Nukus State Technical University", "Nukus davlat texnika universiteti", "Нукусский государственный технический университет", "nukus", "uni"),
 "nii": ("Nókis innovaciyalıq institutı", "Nukus Innovation Institute", "Nukus innovatsion instituti", "Нукусский инновационный институт", "nukus", "uni"),
 "kmi": ("Qaraqalpaqstan medicina institutı", "Karakalpakstan Medical Institute", "Qoraqalpog‘iston tibbiyot instituti", "Каракалпакский медицинский институт", "nukus", "uni"),
 "kaai": ("Qaraqalpaqstan awıl xojalıǵı hám agrotexnologiyalar institutı", "Karakalpakstan Institute of Agriculture and Agrotechnologies", "Qoraqalpog‘iston qishloq xo‘jaligi va agrotexnologiyalar instituti", "Каракалпакский институт сельского хозяйства и агротехнологий", "nukus", "uni"),
 "art_nukus": ("Ózbekstan mámleketlik óner hám mádeniyat institutı Nókis filialı", "Uzbekistan State Institute of Arts and Culture, Nukus branch", "O‘zbekiston davlat san’at va madaniyat instituti Nukus filiali", "Государственный институт искусств и культуры Узбекистана, Нукусский филиал", "nukus", "uni"),
 "samvet_nukus": ("Samarqand veterinariya medicinası, sharwashılıq hám biotexnologiyalar universiteti Nókis filialı", "Samarkand University of Veterinary Medicine, Livestock and Biotechnologies, Nukus branch", "Samarqand veterinariya meditsinasi, chorvachilik va biotexnologiyalar universiteti Nukus filiali", "Самаркандский университет ветеринарной медицины, животноводства и биотехнологий, Нукусский филиал", "nukus", "uni"),
 "ranch": ("RANCH texnologiya universiteti Nókis kampusı", "RANCH University of Technology, Nukus campus", "RANCH texnologiya universiteti Nukus kampusi", "Технологический университет RANCH, Нукусский кампус", "nukus", "uni"),
 "uit": ("Innovaciyalıq texnologiyalar universiteti", "University of Innovation Technologies", "Innovatsion texnologiyalar universiteti", "Университет инновационных технологий", "nukus", "uni"),
 "cyber": ("«Cyber University» mámleketlik universiteti", "Cyber University", "«Cyber University» davlat universiteti", "Государственный университет «Cyber University»", "tashkent", "uni"),
 "tsue": ("Tashkent mámleketlik ekonomika universiteti", "Tashkent State University of Economics", "Toshkent davlat iqtisodiyot universiteti", "Ташкентский государственный экономический университет", "tashkent", "uni"),
 "tuit": ("Muhammad al-Xorezmiy atındaǵı Tashkent informaciyalıq texnologiyalar universiteti", "Tashkent University of Information Technologies", "Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti", "Ташкентский университет информационных технологий им. аль-Хорезми", "tashkent", "uni"),
 "nuu": ("Mirzo Ulıǵbek atındaǵı Ózbekstan milliy universiteti", "National University of Uzbekistan", "Mirzo Ulug‘bek nomidagi O‘zbekiston Milliy universiteti", "Национальный университет Узбекистана им. Мирзо Улугбека", "tashkent", "uni"),
 "mephi": ("MIFI milliy izertlew yadro universitetiniń Tashkent filialı", "MEPhI National Research Nuclear University, Tashkent branch", "MIFI milliy tadqiqot yadro universiteti Toshkent filiali", "Ташкентский филиал НИЯУ МИФИ", "tashkent", "uni"),
 "nuu_new": ("Jańa Ózbekstan universiteti", "New Uzbekistan University", "Yangi O‘zbekiston universiteti", "Университет «Новый Узбекистан»", "tashkent", "uni"),
 "uzswlu": ("Ózbekstan mámleketlik jáhán tilleri universiteti", "Uzbekistan State World Languages University", "O‘zbekiston davlat jahon tillari universiteti", "Узбекский государственный университет мировых языков", "tashkent", "uni"),
 "mil": ("Áskeriy qáwipsizlik hám qorǵanıw universiteti", "University of Military Security and Defense", "Harbiy xavfsizlik va mudofaa universiteti", "Университет военной безопасности и обороны", "tashkent", "uni"),
 "art": ("Ózbekstan mámleketlik óner hám mádeniyat institutı", "Uzbekistan State Institute of Arts and Culture", "O‘zbekiston davlat san’at va madaniyat instituti", "Государственный институт искусств и культуры Узбекистана", "tashkent", "uni"),
 "tsmu_ch": ("Tashkent mámleketlik medicina universiteti Shirshıq filialı", "Tashkent State Medical University, Chirchik branch", "Toshkent davlat tibbiyot universiteti Chirchiq filiali", "Ташкентский государственный медицинский университет, Чирчикский филиал", "tashkent", "uni"),
 "samsmu": ("Samarqand mámleketlik medicina universiteti", "Samarkand State Medical University", "Samarqand davlat tibbiyot universiteti", "Самаркандский государственный медицинский университет", "samarkand", "uni"),
 "samspi": ("Samarqand mámleketlik pedagogikalıq institutı", "Samarkand State Pedagogical Institute", "Samarqand davlat pedagogika instituti", "Самаркандский государственный педагогический институт", "samarkand", "uni"),
 "urgmi": ("Urgench mámleketlik medicina institutı", "Urgench State Medical Institute", "Urganch davlat tibbiyot instituti", "Ургенчский государственный медицинский институт", "khorezm", "uni"),
 "urgu": ("Abu Rayxan Beruniy atındaǵı Urgench mámleketlik universiteti", "Urgench State University", "Abu Rayhon Beruniy nomidagi Urganch davlat universiteti", "Ургенчский государственный университет им. Беруни", "khorezm", "uni"),
 "asmi": ("Andijan mámleketlik medicina institutı", "Andijan State Medical Institute", "Andijon davlat tibbiyot instituti", "Андижанский государственный медицинский институт", "andijan", "uni"),
 "navoiu": ("Nawayı mámleketlik universiteti", "Navoi State University", "Navoiy davlat universiteti", "Навоийский государственный университет", "navoi", "uni"),
 "karshi": ("Qarshı mámleketlik universiteti", "Karshi State University", "Qarshi davlat universiteti", "Каршинский государственный университет", "kashkadarya", "uni"),
 "namangan": ("Namangan mámleketlik universiteti", "Namangan State University", "Namangan davlat universiteti", "Наманганский государственный университет", "namangan", "uni"),
 "termiz": ("Termiz mámleketlik universiteti", "Termez State University", "Termiz davlat universiteti", "Термезский государственный университет", "surkhandarya", "uni"),
 "coll_health1": ("Abu Áli ibn Sina atındaǵı Nókis 1-sanlı jámiyet salamatlıǵı texnikumı", "Nukus Public Health College No. 1 named after Ibn Sina", "Abu Ali ibn Sino nomidagi 1-son Nukus jamoat salomatligi texnikumi", "Нукусский техникум общественного здоровья № 1 им. Ибн Сины", "nukus", "college"),
 "coll_health2": ("Abu Áli ibn Sina atındaǵı Nókis 2-sanlı jámiyet salamatlıǵı texnikumı", "Nukus Public Health College No. 2 named after Ibn Sina", "Abu Ali ibn Sino nomidagi 2-son Nukus jamoat salomatligi texnikumi", "Нукусский техникум общественного здоровья № 2 им. Ибн Сины", "nukus", "college"),
 "ubs": ("University of Business and Science Tashkent filialı", "University of Business and Science, Tashkent branch", "University of Business and Science Toshkent filiali", "University of Business and Science, Ташкентский филиал", "tashkent", "uni"),
 "keg3": ("Kegeyli rayonı 3-sanlı texnikumı", "Kegeyli District College No. 3", "Kegeyli tumani 3-sonli texnikumi", "Техникум №3 Кегейлийского района", "kegeyli", "college"),
 "coll_aral": ("Aralboyı medicina hám transport texnikumı", "Aralboyi Medical and Transport College", "Orolbo‘yi tibbiyot va transport texnikumi", "Приаральский медицинский и транспортный техникум", "nukus", "college"),
}

CITY = {
 "nukus": ("Nókis", "Nukus", "Nukus", "Нукус"),
 "kegeyli": ("Kegeyli", "Kegeyli", "Kegeyli", "Кегейли"),
 "tashkent": ("Tashkent", "Tashkent", "Toshkent", "Ташкент"),
 "samarkand": ("Samarqand", "Samarkand", "Samarqand", "Самарканд"),
 "khorezm": ("Urgench", "Urgench", "Urganch", "Ургенч"),
 "andijan": ("Andijan", "Andijan", "Andijon", "Андижан"),
 "navoi": ("Nawayı", "Navoi", "Navoiy", "Навои"),
 "kashkadarya": ("Qarshı", "Karshi", "Qarshi", "Карши"),
 "namangan": ("Namangan", "Namangan", "Namangan", "Наманган"),
 "surkhandarya": ("Termiz", "Termez", "Termiz", "Термез"),
}

FIELD = {  # (kaa, en, uz, ru, colour)
 "econ": ("Ekonomika hám biznes", "Economics and business", "Iqtisodiyot va biznes", "Экономика и бизнес", "#0b5f78"),
 "sci": ("Matematika hám tábiyiy pánler", "Mathematics and natural sciences", "Matematika va tabiiy fanlar", "Математика и естественные науки", "#047857"),
 "lang": ("Tiller hám filologiya", "Languages and philology", "Tillar va filologiya", "Языки и филология", "#7c3aed"),
 "eng": ("Injenerlik hám IT", "Engineering and IT", "Muhandislik va IT", "Инженерия и IT", "#1d4ed8"),
 "med": ("Medicina", "Medicine and healthcare", "Tibbiyot", "Медицина", "#a3202c"),
 "edu": ("Pedagogika hám psixologiya", "Education and psychology", "Pedagogika va psixologiya", "Педагогика и психология", "#be185d"),
 "soc": ("Huqıq, tariyx hám social pánler", "Law, history and social sciences", "Huquq, tarix va ijtimoiy fanlar", "Право, история и социальные науки", "#92400e"),
 "mil": ("Áskeriy", "Military", "Harbiy", "Военное дело", "#475569"),
}

# Certificate results of each graduating class (counted from tables 8.1–8.4; totals only)
#   with: graduates holding at least one national / CEFR certificate or IELTS
#   top:  graduates with an A or A+ national certificate in at least one subject
CERTS = {
 "2022/2023": dict(with_=0, top=0, ielts=0, sat=0),
 "2023/2024": dict(with_=7, top=0, ielts=1, sat=0),
 "2024/2025": dict(with_=28, top=5, ielts=5, sat=2),
 "2025/2026": dict(with_=53, top=8, ielts=4, sat=2),
}
BEST_SAT = 1310

# Cities counted as "home" (in Karakalpakstan, not "outside")
HOME = ("nukus", "kegeyli")

# Map positions (latitude, longitude) of the cities
GEO = {"kegeyli": (42.78, 59.62), "nukus": (42.46, 59.60), "tashkent": (41.31, 69.24), "samarkand": (39.65, 66.96),
       "khorezm": (41.55, 60.63), "andijan": (40.78, 72.34), "navoi": (40.10, 65.37), "kashkadarya": (38.86, 65.79),
       "namangan": (41.00, 71.67), "surkhandarya": (37.22, 67.28)}

# Graduate stories — add only with the graduate's permission:
# dict(name="Name Surname", year="2025", inst="mephi", photo="photos/graduates/x.jpg" or None,
#      text=("kaa quote", "en quote", "uz quote", "ru quote"))
STORIES = []

# Short names shown in the round university badges (until real logo files are added as photos/unis/<key>.png)
ABBR = {"ksu": "QMU", "nspi": "NMPI", "nstu": "NMTU", "nii": "NII", "kmi": "QMI", "kaai": "QAXI", "art_nukus": "ÓMI", "samvet_nukus": "SVMU",
        "ranch": "RANCH", "uit": "UIT", "cyber": "CYBER", "tsue": "TSUE", "tuit": "TUIT", "nuu": "NUUz", "mephi": "MEPhI", "nuu_new": "NewUU",
        "uzswlu": "UzSWLU", "mil": "HXMU", "art": "ÓMI", "tsmu_ch": "TSMU", "samsmu": "SamMU", "samspi": "SamPI", "urgmi": "UrMI",
        "urgu": "UrDU", "asmi": "ADTI", "navoiu": "NavDU", "karshi": "QarDU", "namangan": "NamDU", "termiz": "TerDU", "coll_health1": "JST1", "coll_health2": "JST2", "coll_aral": "AMTT", "ubs": "UBS", "keg3": "KT3"}

# Full names of graduates who continue their education (published with permission), same order as PLACED.
NAMES = {
 "2022/2023": ["Аманбаева Қанзада Жубандық қызы", "Атаханова Назира Назирбай қызы", "Бахтыбаева Шахноза Махмуд қызы", "Инятов Азизбек Рафатдин улы",
   "Жалғасбаева Жулдыз Абатбай қызы", "Жарылқасинова Диана Елмурза қызы", "Жолдасбаева Дилназ Мухаматдин қызы", "Жумабаев Адилбек Азат улы",
   "Жумахметов Жаңабай Пердебай улы", "Қайпбаева Диларам Артықбай қызы", "Шалабаева Феруза Бахтияр қызы", "Шерниязова Салтанат Қуўат қызы",
   "Умирбаев Елбрус Ерназар улы", "Уразбаева Шахноза Оралбай қызы"],
 "2023/2024": ["Алламбергенова Айсара Адилбай қызы", "Аманбаева Мерўерт Бахтияр қызы", "Ахназарова Алтинай Қалхназар қизи", "Айбарова Зарина Бахтияр қызы",
   "Айтмуратов Шамшет", "Азаматова Арайлым Азамат қызы", "Базарбаев Жасурбек Байрамбай улы", "Бекбергенова Шахнозабану Анибек қизи",
   "Ерназарова Нилуфар Еркинбай қызы", "Ешмуратова Гулферуз Жеңисбаевна", "Иқласбаев Аллаяр Алпамисович", "Жалгасбаева Гулхумар Кеунимжай қызы",
   "Жолдасбаева Айсулиў", "Жолдасбаева Дилянора Медетбай қызы", "Жолдасбаева Зулфия Даўлетбай қызы", "Жумабаева Гулбаныў Болысбай қызы",
   "Кайратдинов Пахратдин Асематдийин ули", "Муратбаева Жузимгул Даўлетбай қизи", "Ниетуллаева Шахнозабану Нажиматдин қизи", "Нуратдинов Сайыпбек Махсетбай улы",
   "Пирданова Бегзада", "Сапарбаева Гулайда Махсетбай қызы", "Сапарниязов Артықбай Азирбаевич", "Сарсенбаева Дилфуза Бахадир қызы",
   "Сметуллаева Феруза Насир қызы", "Тажетдинова Нурзада Жақсимбай қизи", "Төлепбергенова Айсулыў Жалғасбай қызы", "Торениязова Нурсулиў Тенелбай қизи",
   "Турғанбаева Зияда Бахадыр қызы", "Узакбаева Айжамал Музапбар қызы",
   "Юсупова Умида Бахтияр қизи"],
 "2024/2025": ["Абатов Едилбек Адилбекович", "Абдуллаева Айжамал Саламат қизи", "Алламбергенов Мухаммеддин Қадирбай ўғли", "Алланиязова Гулзада Жанибек қызы",
   "Аймуратов Тазабай Байрамбай улы", "Бабаханова Риана Матимурат қизи", "Базарбаева Гулзар Муратбай қизи", "Бердимуратова Алима Исмайил қизи",
   "Даўлетбаева Сайёра Сағийдулла қизи", "Дуйсенбаев Турсинбай Есенбай ули", "Ембергенов Нурполат Адилбай ули", "Ешимбетова Малика Арепбай қизи",
   "Хамидуллаева Феруза Даулетовна", "Иқласбаев Назарбек Оралбай ўғли", "Исмайлова Хуршида Юсупбек қызы", "Жаксиликова Нилуфар Дарменбай қызы",
   "Махсудова Дилноза Азамат қизи", "Муратбаева Зулайха Қурбанбай қызы", "Назаримбетова Гәўхар Садатдин қызы", "Қалбаева Бахитгул Рашид қизи",
   "Қайпбаева Айжамал Артықбай қызы", "Қидирбаева Айсара Турсынбай қызы", "Рахметдинов Салаўатдин Бахрам ўғли", "Шерниязова Манзура Тоқтарбай қызы",
   "Ширазова Гулдана Зиуатдин қызы", "Тлегенова Феруза Аллабай қызы", "Туребаев Сагинбай Жангаберген ули", "Турғанбаева Айнура Муратбай қызы",
   "Турсинбаев Жасурбек Ахмед ўғли", "Хожалепесова Дилафруз Кайратдин қизи", "Ерниязова Малика Айнияз қызы", "Жолдасбаева Парўаз Азамат қизи",
   "Едилова Зухра Торемурат қизи", "Даурханова Гулмира", "Алланазарова Райхан", "Юсупбаева Улдана Саламат қизи",
   "Жадигерова Зарина Амангелди қизи", "Караматдинова Гулқумар Садатдин қизи", "Каримбаев Асадбек Данияр улы"],
 "2025/2026": ["Абдуллаева Сабрина Сипатдин қызы", "Әдилбаев Әрман Нурлыбай улы", "Аяпбергенов Шахрухбек Бекберген улы", "Айбаров Ғайрат Бахтияр улы",
   "Базарбаев Батыр Саламат улы", "Бегмуратова Гүлдана Азамат қызы", "Бекбаўлиев Мырзабек Байрамович", "Даулетбаева Шахсанем Азамат қызы",
   "Дәўлетбаева Алфия Палуанбай қызы", "Досназаров Ақылбек Жумағали улы", "Есемуратов Жахангир Албертович", "Хамидуллаева Айнур Дәўлетовна",
   "Исакова Гүлдана Қошқарбай қызы", "Жалғасбаева Гулнура Камалатдин қызы", "Жаңабаева Элмира Сәлменовна", "Жаңабаева Гүлзада Иляс қызы",
   "Жиемуратов Султанбек Тошкентбай улы", "Жумамбетова Гүлсима Зийнатдин қызы", "Жумамуратова Мехрибан Бегжан қызы", "Жумамуратова Рамила Хожамуратовна",
   "Калдибаева Дилафруз Айболсын қызы", "Камалатдинов Даулетияр Илхам улы", "Кеңесбаева Гүлсевар Алийшер қызы", "Кеңесбаева Динара Парахат қызы",
   "Кеунимжаева Бийбиназ Саламат қызы", "Мамбеткаримов Рамазан Шәмшетдин улы", "Маратов Бекполат Илхаматдин улы", "Махсетбаев Уснатдин Айдосович",
   "Мнажатдинов Салауатдин Махмутдин улы", "Мнажатдинова Шахноза Азамат қызы", "Муратбаева Диана Байрамбай қызы", "Муратбаева Гүлбәҳәр Досназар қызы",
   "Муратов Әлишер Дәўлет улы", "Муханов Мийрас Жалғасбай улы", "Нурниязов Абзал", "Оңғарбаева Нилуфар Ерполатовна",
   "Полатов Марат Фурхат улы", "Қудиярова Зарина Хожабай қызы", "Қуўанышбаева Нағийма Бахтияровна", "Рзамбетова Перижамал Боранбай қызы",
   "Сейтекова Наргиза Халықназар қызы", "Шамшиева Сапарай Рахат қызы", "Таңатарова Гулмира Қалбай қызы", "Тлепбаева Турсынай Саламат қызы",
   "Толебаев Мухаммед Асанбекович", "Толыбаева Айдынай Жалалатдин қызы", "Толыбаева Хурлиха Батырбай қызы", "Турғанбаева Айзада Ерполат қызы",
   "Турғанбаева Улбосын Оңғарбай қызы", "Убайдуллаева Гүлбаныў Исметулла қызы", "Умарбаева Мадина Давлеткелди қызы", "Уразбаева Хансулыў Өскинбай қызы",
   "Усенов Қахраман Куанишбай ули"],
}
# Note: the 2025/2026 list follows table 8.4 minus the three graduates without a university/college entry.
_KAA = {"а":"a","ә":"á","б":"b","в":"v","г":"g","ғ":"ǵ","д":"d","е":"e","ё":"yo","ж":"j","з":"z","и":"i","й":"y","к":"k","қ":"q","л":"l","м":"m",
 "н":"n","ң":"ń","о":"o","ө":"ó","п":"p","р":"r","с":"s","т":"t","у":"u","ү":"ú","ў":"w","ф":"f","х":"x","ҳ":"h","ц":"ts","ч":"ch","ш":"sh",
 "щ":"sh","ъ":"","ы":"ı","ь":"","э":"e","ю":"yu","я":"ya"}
_SUF = {"улы": "ulı", "ули": "uli", "ўғли": "o‘g‘li", "қызы": "qızı", "қизи": "qizi"}
def latin_name(s):
    out = ""
    for w in s.split():
        if w.lower() in _SUF:
            out += " " + _SUF[w.lower()]; continue
        r = "".join(_KAA.get(ch.lower(), ch) for ch in w)
        out += (" " if out else "") + (r[:1].upper() + r[1:] if r else r)
    return out

# Graduates with no university/college listed in the school records (index = position in the year's list)
UNPLACED = {
    "2024/2025": [(39, "Муратбаева Согдиана Артуровна")],
    "2025/2026": [(1, "Абеков Рашид Балтабай улы"), (5, "Балғабаева Нурзада Дарябай қызы"), (9, "Далибаева Зийба Рүстем қызы")],
}
def roster(y):
    rows = [(n, p) for n, p in zip(NAMES[y], PLACED[y])]
    for idx, n in UNPLACED.get(y, []):
        rows.insert(idx, (n, None))
    return rows

# National certificates per graduate (subject code:level), same order as PLACED. 2022/2023 graduates had none.
# M maths, P physics, C chemistry, B biology, H history, G geography, L native language & literature,
# E English (CEFR), U Uzbek, Q Karakalpak, T Turkish (CEFR)
_C = lambda s: [x.split(";") if x else [] for x in s.split("|")]
CERT_SUBJ = {
 "2022/2023": [[] for _ in range(14)],
 "2023/2024": _C("|||E:B2||E:B1||||||M:B|E:B2||E:B2||||||||||||E:B2||||".replace("||||", "||||")),
 "2024/2025": _C("M:C+;P:C+|M:B|M:B;E:B1|E:B2;U:C+|C:C+;B:A|B:C|E:B2;U:B|H:B+|E:B2;Q:C+|M:A+;P:B|E:B1||P:C+;M:C+|H:C;G:C|E:B2;U:B|E:B2;H:A+|C:C;B:C|Q:C+;B:C+|E:B2|C:C+|||M:B;P:C+||||M:A;E:B2|E:B2;U:B|E:B2;M:C|E:B1||||E:B2;Q:A|E:B1||Q:B||M:B;P:C"),
 "2025/2026": _C("M:B;T:B2|M:C+;P:C+|L:C|B:C+;H:B|C:C+;B:C+;L:B;H:C|C:C+;B:B;L:C|M:C+;H:A;E:B2|C:C;B:B+|M:C;L:A;H:C|M:C+;E:B2|M:C;E:B1|M:A;P:A;H:C+|M:C+;T:B2|M:C;L:C+;E:B2|L:B+;E:B2|E:B1|M:B;P:C+|C:C+;B:B+;L:B+;H:A|L:C;H:C;E:B1|L:B;E:B2|L:B;H:A+;E:B1|H:C;E:B1|M:B;L:B+;H:C+;E:B2|E:B2|M:B;T:B1|E:B1|H:C;L:B|M:B+;P:C+|L:C+|C:B;B:C+|M:C+|L:B;H:C+||M:B;E:B2||L:C+;H:B|M:C+;E:B1|B:C;L:C+;H:C|C:C+;B:B;L:C+;H:C|L:B+;H:B;E:B2|L:B;H:C;E:B2||E:B2|M:C;L:B;H:C+|C:A;B:B+;L:B;H:C+|M:B;L:C+;T:B2|M:A+;P:A;L:B+;H:B|B:C;L:C+|M:C+;E:B1|M:B;H:B;L:A+|L:B;H:C+;E:B2|M:B|L:C;H:C"),
}
_C23 = ["", "", "", "E:B2", "", "E:B1", "", "", "", "", "M:B", "E:B2", "", "E:B2", "", "", "", "", "", "", "", "", "", "", "E:B2", "", "", "", "", "", ""]
CERT_SUBJ["2023/2024"] = [x.split(";") if x else [] for x in _C23]
