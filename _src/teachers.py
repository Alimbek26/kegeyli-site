# Teachers (from table 5 of "Kegeyli IM ko'rsatgich"). Only surname + first name, subject and category are published.
# Format: (Surname Firstname in Cyrillic, subject key, category key)
# subject keys: see SUBJECTS below; category keys: high, first, second, spec
TEACHERS = [
 ("Айназаров Ажинияз", "math", "high"), ("Айназаров Қурбаназар", "math", "high"),
 ("Айтмуратова Дилфуза", "eng", "high"), ("Аманбаева Қуралай", "eng", "spec"),
 ("Арзибаев Толисбай", "art", "spec"), ("Артикова Шахноза", "phys", "first"),
 ("Аташов Азиз", "chem", "spec"), ("Бегалиева Жарқин", "kaa", "high"),
 ("Бердибаев Саламат", "math", "spec"), ("Давирханов Женисбай", "math", "first"),
 ("Дилмуратов Дамир", "math", "spec"), ("Елмуратова Тоти", "bio", "second"),
 ("Ережепов Зухратдин", "pe", "second"), ("Есбергенов Атабек", "math", "first"),
 ("Жалғасова Оркенай", "eng", "second"), ("Жангабаева Наргиза", "rob", "second"),
 ("Жарилқасинов Айназар", "hist", "high"), ("Жолдасбаев Базарбай", "kaa", "first"),
 ("Зарипбаев Ажиняз", "inf", "second"), ("Исмайлова Гулмира", "uzb", "high"),
 ("Кеунимжаев Абдуғаний", "phys", "first"), ("Мамутова Зинехан", "eng", "high"),
 ("Назбергенова Зияда", "eng", "first"), ("Оразалиева Рисгул", "math", "high"),
 ("Осербаева Зулфия", "eng", "first"), ("Пиримбетов Алписбай", "math", "high"),
 ("Салиева Элмира", "kaa", "high"), ("Сапаров Мансур", "math", "first"),
 ("Сарсенбаев Данияр", "phys", "high"), ("Сейтназаров Темирбек", "cqt", "spec"),
 ("Тажимуратова Зияда", "chem", "first"), ("Темирханова Айнура", "eng", "second"),
 ("Тулепов Султан", "hist", "high"), ("Узақбаева Айсанем", "rus", "first"),
 ("Умирбекова Фатима", "bio", "first"), ("Утениязова Абадан", "chem", "first"),
 ("Утешова Гулбахар", "tarb", "spec"), ("Худайбергенова Қумар", "math", "high"),
 ("Шукириллаев Науризбай", "inf", "first"), ("Қарлибаева Гулшахра", "kaa", "high"),
 ("Қудайбергенов Махмут", "geo", "first"), ("Қурбанбаева Малика", "phys", "first"),
 ("Қутлимуратов Сарманбек", "uzb", "high"),
]

# Leadership: (Latin name, Cyrillic name, role key). Add deputies here.
LEADERS = [   # shown in this order
 ("Feruza Nizamatdinova", "Феруза Низаматдинова", "director"),
 ("Nurnazar Uteniyazov", "Нурназар Утениязов", "dep_edu"),
 ("Alimbek Jumamuratov", "Алимбек Жумамуратов", "adviser"),
 ("Islam Pirniyazov", "Ислам Пирниязов", "dep_spirit"),
 ("Baxtiyar Perdebaev", "Бахтияр Пердебаев", "psych"),
 ("Azat Utepbergenov", "Азат Утепбергенов", "dep_econ"),
 ("Feruza Seytnazarova", "Феруза Сейтназарова", "librarian"),
 ("Qabil Orazbaev", "Кабыл Оразбаев", "accountant"),
 ("Gulziba Temirxanova", "Гулзиба Темирханова", "hr"),
 ("Temirbek Seytnazarov", "Темирбек Сейтназаров", "cqt_head"),
]

# Extra details shown on a leadership card (Latin name -> list of lines (kaa, en, uz, ru)).
# Alimbek Jumamuratov: from his portfolio (erp.maktab.uz). Not published: birth date, nationality, document numbers.
LEADER_INFO = {
 "Alimbek Jumamuratov": [
  ("Nókis mámleketlik pedagogikalıq institutı, 2022", "Nukus State Pedagogical Institute, 2022", "Nukus davlat pedagogika instituti, 2022", "Нукусский государственный педагогический институт, 2022"),
  ("Mektepte 2023-jıldan beri", "At the school since 2023", "Maktabda 2023-yildan beri", "В школе с 2023 года"),
  ("British Council ingliz tili sertifikatı", "British Council English language certificate", "British Council ingliz tili sertifikati", "Сертификат British Council по английскому языку"),
 ],
}

ROLES = {
 "director": {"kaa": "Mektep direktorı", "en": "School Director", "uz": "Maktab direktori", "ru": "Директор школы"},
 "dep_edu": {"kaa": "Direktordıń oqıw isleri boyınsha orınbasarı", "en": "Deputy Director for Academic Affairs", "uz": "Direktorning o‘quv ishlari bo‘yicha o‘rinbosari", "ru": "Заместитель директора по учебной работе"},
 "dep_econ": {"kaa": "Direktordıń xojalıq isleri boyınsha orınbasarı", "en": "Deputy Director for Facilities", "uz": "Direktorning xo‘jalik ishlari bo‘yicha o‘rinbosari", "ru": "Заместитель директора по хозяйственной части"},
 "adviser": {"kaa": "Mektep másláhátshisi", "en": "School Counselor", "uz": "Maktab maslahatchisi", "ru": "Школьный консультант"},
 "psych": {"kaa": "Psixolog", "en": "Psychologist", "uz": "Psixolog", "ru": "Психолог"},
 "cqt_head": {"kaa": "Shaqırıwǵa shekemgi baslanǵısh tayarlıq basshısı", "en": "Head of Pre-conscription Training", "uz": "Chaqiruvga qadar boshlang‘ich tayyorgarlik rahbari", "ru": "Руководитель допризывной подготовки"},
 "librarian": {"kaa": "Kitapxanashı", "en": "Librarian", "uz": "Kutubxonachi", "ru": "Библиотекарь"},
 "accountant": {"kaa": "Buxgalter", "en": "Accountant", "uz": "Buxgalter", "ru": "Бухгалтер"},
 "hr": {"kaa": "Kadrlar boyınsha qánige", "en": "HR Specialist", "uz": "Kadrlar bo‘yicha mutaxassis", "ru": "Специалист по кадрам"},
 "dep_spirit": {"kaa": "Direktordıń ruwxıylıq hám aǵartıwshılıq isleri boyınsha orınbasarı", "en": "Deputy Director for Spiritual and Educational Affairs", "uz": "Direktorning ma’naviy-ma’rifiy ishlar bo‘yicha o‘rinbosari", "ru": "Заместитель директора по духовно-просветительской работе"},
}

SUBJECTS = {  # order = display order
 "math": {"kaa": "Matematika", "en": "Mathematics", "uz": "Matematika", "ru": "Математика"},
 "eng": {"kaa": "Ingliz tili", "en": "English", "uz": "Ingliz tili", "ru": "Английский язык"},
 "phys": {"kaa": "Fizika", "en": "Physics", "uz": "Fizika", "ru": "Физика"},
 "chem": {"kaa": "Ximiya", "en": "Chemistry", "uz": "Kimyo", "ru": "Химия"},
 "bio": {"kaa": "Biologiya", "en": "Biology", "uz": "Biologiya", "ru": "Биология"},
 "inf": {"kaa": "Informatika", "en": "Computer science", "uz": "Informatika", "ru": "Информатика"},
 "rob": {"kaa": "Robototexnika", "en": "Robotics", "uz": "Robototexnika", "ru": "Робототехника"},
 "kaa": {"kaa": "Qaraqalpaq tili hám ádebiyatı", "en": "Karakalpak language and literature", "uz": "Qoraqalpoq tili va adabiyoti", "ru": "Каракалпакский язык и литература"},
 "uzb": {"kaa": "Ózbek tili (mámleketlik til)", "en": "Uzbek (state language)", "uz": "O‘zbek tili (davlat tili)", "ru": "Узбекский язык (государственный)"},
 "rus": {"kaa": "Rus tili", "en": "Russian", "uz": "Rus tili", "ru": "Русский язык"},
 "hist": {"kaa": "Tariyx", "en": "History", "uz": "Tarix", "ru": "История"},
 "geo": {"kaa": "Geografiya", "en": "Geography", "uz": "Geografiya", "ru": "География"},
 "art": {"kaa": "Súwretlew óneri (ART)", "en": "Art", "uz": "Tasviriy san’at (ART)", "ru": "Изобразительное искусство (ART)"},
 "pe": {"kaa": "Dene tárbiyası", "en": "Physical education", "uz": "Jismoniy tarbiya", "ru": "Физическая культура"},
 "cqt": {"kaa": "Shaqırıwǵa shekemgi baslanǵısh tayarlıq", "en": "Pre-conscription training", "uz": "Chaqiruvga qadar boshlang‘ich tayyorgarlik", "ru": "Допризывная подготовка"},
 "tarb": {"kaa": "Tárbiya", "en": "Character education", "uz": "Tarbiya", "ru": "Воспитание"},
}

CATS = {
 "high": {"kaa": "Joqarı kategoriya", "en": "Highest category", "uz": "Oliy toifa", "ru": "Высшая категория"},
 "first": {"kaa": "Birinshi kategoriya", "en": "First category", "uz": "1-toifa", "ru": "Первая категория"},
 "second": {"kaa": "Ekinshi kategoriya", "en": "Second category", "uz": "2-toifa", "ru": "Вторая категория"},
 "spec": {"kaa": "Qánige", "en": "Specialist", "uz": "Mutaxassis", "ru": "Специалист"},
}

_MAP = {"а":"a","б":"b","в":"v","г":"g","д":"d","е":"e","ё":"yo","ж":"j","з":"z","и":"i","й":"y","к":"k","л":"l","м":"m",
 "н":"n","о":"o","п":"p","р":"r","с":"s","т":"t","у":"u","ф":"f","х":"x","ц":"ts","ч":"ch","ш":"sh","ъ":"’","ь":"",
 "э":"e","ю":"yu","я":"ya","ў":"w","қ":"q","ғ":"ǵ","ҳ":"h"}  # Karakalpak-style Latin spelling of names

def latin(name):
    out = []
    for w in name.split():
        r = ""
        for i, ch in enumerate(w):
            lo = ch.lower(); v = _MAP.get(lo, ch)
            r += v.capitalize() if ch.isupper() and v else v
        out.append(r)
    return " ".join(out)
