# National certificates (Milliy sertifikat) of our students, published with the students' consent.
# Source: the certificate PDFs issued by the Knowledge and Skills Assessment Agency (Bilim va malakalarni baholash agentligi).
# Personal ID codes (JShShIR), certificate numbers, photos and the PDFs themselves are NOT published.
#
# To add a certificate: copy one line in CERTS and fill it in, then run  python3 _src/build.py
#   subj     : subject key (see SUBJ below; add a new subject there first)
#   name     : "Surname Firstname" as written on the certificate (Latin)
#   level    : A+ | A | B+ | B | C+ | C           total / pct : "Umumiy to'plagan bali" and the % next to it
#   test     : test result      written : written-work result (Jazba jumıs / Jazba sawatxanlıq)
#   sec      : optional - test sections from older certificates (4 numbers, see SEC below)
#   issued / valid : "YYYY-MM-DD"
#   grad + cy: for graduates - graduation year and the Cyrillic name exactly as in graduates.NAMES (links them to the graduates page)
#   cls      : optional - class for current students, e.g. "11-A"
import datetime as _dt, html as _html, json
import graduates as G

SUB = "achievements/national/"
CERTS = [
 dict(subj="kaa", name="Ubaydullaeva Gulbanu", level="A+", total=72.08, pct=100, test=72.16, written=72, issued="2026-06-15", valid="2029-06-14", grad="2025/2026", cy="Убайдуллаева Гүлбаныў Исметулла қызы"),
 dict(subj="kaa", name="Dawrxanova Gulmira", level="A", total=66.34, pct=100, test=62.17, written=70.5, sec=(16.457, 5.486, 23.771, 16.457), issued="2025-05-27", valid="2028-05-26", grad="2024/2025", cy="Даурханова Гулмира"),
 dict(subj="kaa", name="Buxarbaeva Barshınay", level="A", total=66.12, pct=100, test=69.23, written=63, issued="2026-03-10", valid="2029-03-09"),
 dict(subj="kaa", name="Rzambetova Perijamal", level="B+", total=62.36, pct=95.94, test=61.73, written=63, sec=(16.245, 6.498, 22.743, 16.245), issued="2025-05-27", valid="2028-05-26", grad="2025/2026", cy="Рзамбетова Перижамал Боранбай қызы"),
 dict(subj="kaa", name="Jumambetova Gulsima", level="B+", total=61.76, pct=95.02, test=55.02, written=68.5, sec=(10.581, 4.232, 25.394, 14.813), issued="2025-12-09", valid="2028-12-08", grad="2025/2026", cy="Жумамбетова Гүлсима Зийнатдин қызы"),
 dict(subj="kaa", name="Janabaeva Elmira", level="B+", total=61.49, pct=94.6, test=56.48, written=66.5, issued="2026-03-10", valid="2029-03-09", grad="2025/2026", cy="Жаңабаева Элмира Сәлменовна"),
 dict(subj="kaa", name="Tolıbaeva Hurlixa", level="B+", total=61.47, pct=94.57, test=52.44, written=70.5, issued="2026-03-10", valid="2029-03-09", grad="2025/2026", cy="Толыбаева Хурлиха Батырбай қызы"),
 dict(subj="kaa", name="Kenesbaeva Gulsevar", level="B+", total=60.88, pct=93.66, test=53.25, written=68.5, issued="2026-03-10", valid="2029-03-09", grad="2025/2026", cy="Кеңесбаева Гүлсевар Алийшер қызы"),
 dict(subj="kaa", name="Niyetbayeva Gulnura", level="B+", total=60.45, pct=93, test=51.89, written=69, issued="2026-11-20", valid="2029-11-19"),
 dict(subj="kaa", name="Tlepbaeva Tursınay", level="B", total=58.83, pct=90.51, test=50.16, written=67.5, sec=(16.051, 2.006, 26.083, 6.019), issued="2025-12-09", valid="2028-12-08", grad="2025/2026", cy="Тлепбаева Турсынай Саламат қызы"),
 dict(subj="kaa", name="Tolebaev Muxammed", level="B", total=58.73, pct=90.35, test=50.95, written=66.5, sec=(11.58, 4.632, 23.159, 11.58), issued="2025-12-09", valid="2028-12-08", grad="2025/2026", cy="Толебаев Мухаммед Асанбекович"),
 dict(subj="kaa", name="Maxsetova Dilbar", level="B", total=58.5, pct=90, test=51.49, written=65.5, issued="2026-06-15", valid="2029-06-14"),
 dict(subj="kaa", name="Ubaydullaeva Dilafruz", level="B", total=57.6, pct=88.62, test=55.69, written=59.5, issued="2026-11-20", valid="2029-11-19"),
 dict(subj="kaa", name="Tleubaeva Ayziya", level="B", total=57.26, pct=88.09, test=52.01, written=62.5, issued="2026-11-20", valid="2029-11-19"),
 dict(subj="kaa", name="Seytekova Nargiza", level="B", total=56.8, pct=87.38, test=52.09, written=61.5, issued="2026-03-10", valid="2029-03-09", grad="2025/2026", cy="Сейтекова Наргиза Халықназар қызы"),
 dict(subj="kaa", name="Muratbaeva Gulbahar", level="B", total=56, pct=86.15, test=54, written=58, issued="2026-03-10", valid="2029-03-09", grad="2025/2026", cy="Муратбаева Гүлбәҳәр Досназар қызы"),
 dict(subj="kaa", name="Nietbaeva Dilnaza", level="B", total=55.83, pct=85.89, test=53.66, written=58, issued="2026-06-15", valid="2029-06-14"),
 dict(subj="kaa", name="Jadigerova Zarina", level="B", total=55.54, pct=85.45, test=56.57, written=54.5, sec=(12.122, 6.061, 18.183, 20.204), issued="2025-05-27", valid="2028-05-26", grad="2024/2025", cy="Жадигерова Зарина Амангелди қизи"),
 dict(subj="kaa", name="Balǵabaeva Nurzada", level="B", total=55.36, pct=85.17, test=49.21, written=61.5, issued="2026-06-15", valid="2029-06-14", grad="2025/2026", cy="Балғабаева Нурзада Дарябай қызы"),
 dict(subj="kaa", name="Maratov Bekpolat", level="B", total=55.34, pct=85.14, test=47.67, written=63, issued="2026-06-15", valid="2029-06-14", grad="2025/2026", cy="Маратов Бекполат Илхаматдин улы"),
 dict(subj="kaa", name="Dauletbaeva Sayyora", level="C+", total=54.58, pct=83.97, test=48.66, written=60.5, sec=(10.813, 5.407, 18.022, 14.418), issued="2025-05-27", valid="2028-05-26", grad="2024/2025", cy="Даўлетбаева Сайёра Сағийдулла қизи"),
 dict(subj="kaa", name="Torambetov Beksultan", level="C+", total=54.06, pct=83.17, test=44.12, written=64, issued="2026-11-20", valid="2029-11-19"),
 dict(subj="kaa", name="Dalibaeva Ziyba", level="C+", total=54.02, pct=83.11, test=47.53, written=60.5, issued="2026-03-10", valid="2029-03-09", grad="2025/2026", cy="Далибаева Зийба Рүстем қызы"),
 dict(subj="kaa", name="Kuanıshbaeva Naǵıyma", level="C+", total=53.46, pct=82.25, test=41.41, written=65.5, issued="2026-03-10", valid="2029-03-09", grad="2025/2026", cy="Қуўанышбаева Нағийма Бахтияровна"),
 dict(subj="kaa", name="Tolıbaeva Aydınay", level="C+", total=53.36, pct=82.09, test=49.21, written=57.5, issued="2026-06-15", valid="2029-06-14", grad="2025/2026", cy="Толыбаева Айдынай Жалалатдин қызы"),
 dict(subj="kaa", name="Muratbaeva Zulayxa", level="C+", total=52.68, pct=81.05, test=45.35, written=60, sec=(11.83, 3.943, 21.689, 7.887), issued="2025-01-22", valid="2028-01-21", grad="2024/2025", cy="Муратбаева Зулайха Қурбанбай қызы"),
 dict(subj="kaa", name="Ongarbaeva Nilufar", level="C+", total=52.13, pct=80.2, test=50.25, written=54, sec=(15.075, 7.538, 15.075, 12.562), issued="2025-12-09", valid="2028-12-08", grad="2025/2026", cy="Оңғарбаева Нилуфар Ерполатовна"),
 dict(subj="kaa", name="Jumabaev Berdiniyaz", level="C+", total=50.96, pct=78.4, test=54.92, written=47, issued="2026-06-15", valid="2029-06-14"),
 dict(subj="kaa", name="Mnajatdinov Salauatdin", level="C+", total=50.95, pct=78.38, test=38.4, written=63.5, sec=(9.6, 3.2, 16, 9.6), issued="2025-12-09", valid="2028-12-08", grad="2025/2026", cy="Мнажатдинов Салауатдин Махмутдин улы"),
 dict(subj="kaa", name="Alibaeva Ilmira", level="C+", total=50.17, pct=77.18, test=43.33, written=57, issued="2026-11-20", valid="2029-11-19"),
 dict(subj="kaa", name="Begmuratova Guldana", level="C", total=49.97, pct=76.88, test=40.94, written=59, issued="2026-03-10", valid="2029-03-09", grad="2025/2026", cy="Бегмуратова Гүлдана Азамат қызы"),
 dict(subj="kaa", name="Sarsenbaeva Biybiruza", level="C", total=48.18, pct=74.12, test=46.35, written=50, issued="2026-06-15", valid="2029-06-14"),
 dict(subj="kaa", name="Usenov Kaxraman", level="C", total=47.58, pct=73.2, test=38.66, written=56.5, issued="2026-06-15", valid="2029-06-14", grad="2025/2026", cy="Усенов Қахраман Куанишбай ули"),
 # Russian language and literature
 dict(subj="rus", name="Matyakupova Alina", level="A", total=66.85, pct=100, test=70.7, written=63, issued="2026-06-15", valid="2029-06-14", cls="11-B"),
 dict(subj="rus", name="Esemuratov Javohir", level="B+", total=63.27, pct=97.34, test=72.54, written=54, issued="2026-11-20", valid="2029-11-19", cls="10-B"),
 dict(subj="rus", name="Arıslanbaev Dawıtbek", level="B+", total=60.24, pct=92.68, test=64.48, written=56, issued="2026-11-20", valid="2029-11-19", cls="11-B"),
 dict(subj="rus", name="Menlimuratov Asadbek", level="B", total=59.05, pct=90.85, test=62.59, written=55.5, issued="2026-11-20", valid="2029-11-19", cls="11-A"),
 dict(subj="rus", name="Sharibaeva Ulmeken", level="B", total=57.29, pct=88.14, test=62.08, written=52.5, issued="2026-11-20", valid="2029-11-19", cls="11-B"),
 dict(subj="rus", name="Menlimuratova Shaxzoda", level="B", total=56.41, pct=86.78, test=62.31, written=50.5, issued="2026-11-20", valid="2029-11-19", cls="10-B"),
 dict(subj="rus", name="Jumabaev Begzad", level="B", total=56.2, pct=86.46, test=52.89, written=59.5, issued="2026-06-15", valid="2029-06-14", cls="11-A"),
 dict(subj="rus", name="Abdullaeva Gulnur", level="C+", total=51.41, pct=79.09, test=53.81, written=49, issued="2026-06-15", valid="2029-06-14", cls="11-B"),
 dict(subj="rus", name="Aybarov Ǵayrat", level="C", total=48.95, pct=75.31, test=46.4, written=51.5, issued="2026-06-15", valid="2029-06-14", grad="2025/2026", cy="Айбаров Ғайрат Бахтияр улы"),
]

SUBJ = {"kaa": ("Qaraqalpaq tili hám ádebiyatı", "Karakalpak language and literature", "Qoraqalpoq tili va adabiyoti", "Каракалпакский язык и литература", "#a3202c"),
        "rus": ("Rus tili hám ádebiyatı", "Russian language and literature", "Rus tili va adabiyoti", "Русский язык и литература", "#1d4ed8")}
# Lower bound of each level (national certificate scale)
SCALE = [("A+", 70), ("A", 65), ("B+", 60), ("B", 55), ("C+", 50), ("C", 46)]
LVCOL = {"A+": "#a3202c", "A": "#d6452f", "B+": "#e07a1f", "B": "#d4a017", "C+": "#3e95ad", "C": "#7fb3c4"}
SEC = [("Til bilimi", "Language knowledge", "Til bilimi", "Языкознание"),
       ("Ádebiyat teoriyası hám tariyxı", "Literary theory and history", "Adabiyot nazariyasi va tarixi", "Теория и история литературы"),
       ("Oqıw sawatxanlıǵı", "Reading literacy", "O‘qish savodxonligi", "Читательская грамотность"),
       ("Lingvistikalıq hám kórkem analiz", "Linguistic and literary analysis", "Lingvistik va badiiy tahlil", "Лингвистический и художественный анализ")]
NAME = ("Milliy sertifikatlar", "National certificates", "Milliy sertifikatlar", "Национальные сертификаты")
DESC = ("Oqıwshılarımızdıń milliy sertifikatları: hár bir sertifikat — dáreje, ball, test hám jazba jumıs nátiyjeleri, berilgen sánesi.",
        "Our students’ national certificates: each certificate with level, score, test and written-work results and date issued.",
        "O‘quvchilarimizning milliy sertifikatlari: har bir sertifikat — daraja, ball, test va yozma ish natijalari, berilgan sanasi.",
        "Национальные сертификаты наших учеников: уровень, балл, результаты теста и письменной работы, дата выдачи.")
LANGS = ["kaa", "en", "uz", "ru"]
X = {
 "lead": ("Bilim hám malakalardı bahalaw agentligi bergen milliy sertifikatlar. Hár bir sertifikat oqıwshınıń ruqsatı menen járiyalandı.",
          "National certificates issued by the Knowledge and Skills Assessment Agency. Every certificate is published with the student’s consent.",
          "Bilim va malakalarni baholash agentligi bergan milliy sertifikatlar. Har bir sertifikat o‘quvchining roziligi bilan e’lon qilindi.",
          "Национальные сертификаты, выданные Агентством по оценке знаний и навыков. Каждый сертификат опубликован с согласия ученика."),
 "t_all": ("sertifikat", "certificates", "sertifikat", "сертификатов"),
 "t_top": ("A+ hám A dárejesi", "A+ and A level", "A+ va A darajasi", "уровня A+ и A"),
 "t_bplus": ("B+ hám joqarı", "B+ or higher", "B+ va yuqori", "B+ и выше"),
 "t_avg": ("ortasha ball", "average score", "o‘rtacha ball", "средний балл"),
 "t_best": ("eń joqarı ball", "best score", "eng yuqori ball", "лучший балл"),
 "ladder_h": ("Dárejeler", "Levels", "Darajalar", "Уровни"),
 "ladder_p": ("Dárejeni basıp, tek sol sertifikatlardı kóriń.", "Tap a level to show only those certificates.", "Darajani bosib, faqat o‘sha sertifikatlarni ko‘ring.", "Нажмите на уровень, чтобы показать только его."),
 "chart_h": ("Ballar shkalada", "Scores on the scale", "Ballar shkalada", "Баллы на шкале"),
 "chart_p": ("Hár bir noqat — bir sertifikat. Noqattı basıń.", "Each dot is one certificate. Tap a dot.", "Har bir nuqta — bitta sertifikat. Nuqtani bosing.", "Каждая точка — один сертификат. Нажмите на точку."),
 "list_h": ("Barlıq sertifikatlar", "All certificates", "Barcha sertifikatlar", "Все сертификаты"),
 "search": ("Atı boyınsha izlew", "Search by name", "Ism bo‘yicha qidirish", "Поиск по имени"),
 "all": ("Barlıǵı", "All", "Barchasi", "Все"),
 "g_grad": ("Pitkeriwshiler", "Graduates", "Bitiruvchilar", "Выпускники"),
 "g_cur": ("Házirgi oqıwshılar", "Current students", "Hozirgi o‘quvchilar", "Нынешние ученики"),
 "sort": ("Tártip", "Sort", "Tartib", "Сортировка"),
 "s_score": ("Ball boyınsha", "Highest score", "Ball bo‘yicha", "По баллу"),
 "s_new": ("Eń jańaları", "Newest first", "Eng yangilari", "Сначала новые"),
 "s_name": ("Atı boyınsha (A–Z)", "Name (A–Z)", "Ism bo‘yicha (A–Z)", "По имени (А–Я)"),
 "shown": ("{n} sertifikat kórsetilgen", "{n} certificates shown", "{n} ta sertifikat ko‘rsatilgan", "Показано: {n}"),
 "none": ("Hesh nárse tabılmadı", "Nothing found", "Hech narsa topilmadi", "Ничего не найдено"),
 "reset": ("Filtrlerdi tazalaw", "Clear filters", "Filtrlarni tozalash", "Сбросить фильтры"),
 "grad": ("{y} pitkeriwshisi", "{y} graduate", "{y} bitiruvchisi", "Выпускник {y}"),
 "cur": ("Mektep oqıwshısı", "Current student", "Maktab o‘quvchisi", "Ученик школы"),
 "total": ("ulıwma ball", "total score", "umumiy ball", "общий балл"),
 "test": ("Test", "Test", "Test", "Тест"),
 "written": ("Jazba jumıs", "Written work", "Yozma ish", "Письменная работа"),
 "secs": ("Test bólimleri", "Test sections", "Test bo‘limlari", "Разделы теста"),
 "issued": ("Berilgen", "Issued", "Berilgan", "Выдан"),
 "valid": ("Ámel etiw múddeti", "Valid until", "Amal qilish muddati", "Действует до"),
 "ok": ("Ámelde", "Valid", "Amalda", "Действует"),
 "exp": ("Múddeti ótken", "Expired", "Muddati o‘tgan", "Истёк"),
 "studies": ("Házir: {u}", "Now at: {u}", "Hozir: {u}", "Сейчас: {u}"),
 "how_h": ("Ball qalay esaplanadı?", "How is the score worked out?", "Ball qanday hisoblanadi?", "Как считается балл?"),
 "how_1": ("Ulıwma ball — test nátiyjesi menen jazba jumıs nátiyjesiniń ortashası.", "The total score is the average of the test result and the written-work result.", "Umumiy ball — test natijasi va yozma ish natijasining o‘rtachasi.", "Общий балл — среднее результатов теста и письменной работы."),
 "how_2": ("Sertifikat 3 jıl ámel etedi.", "A certificate is valid for 3 years.", "Sertifikat 3 yil amal qiladi.", "Сертификат действует 3 года."),
 "how_3": ("Dáreje ulıwma ball boyınsha beriledi:", "The level depends on the total score:", "Daraja umumiy ball bo‘yicha beriladi:", "Уровень зависит от общего балла:"),
 "from": ("{n} balldan", "from {n}", "{n} balldan", "от {n}"),
 "note": ("Derek: oqıwshılardıń milliy sertifikatları. Jeke kodlar, sertifikat nomerleri hám súwretler járiyalanbaydı.",
          "Source: the students’ national certificates. Personal ID codes, certificate numbers and photos are not published.",
          "Manba: o‘quvchilarning milliy sertifikatlari. Shaxsiy kodlar, sertifikat raqamlari va suratlar e’lon qilinmaydi.",
          "Источник: национальные сертификаты учеников. Личные коды, номера сертификатов и фотографии не публикуются."),
 "prof_h": ("Oqıwshılardıń milliy sertifikatları", "Students’ national certificates", "O‘quvchilarning milliy sertifikatlari", "Национальные сертификаты учеников"),
 "prof_p": ("{s} boyınsha {n} sertifikat, olardıń {t} — A+ yamasa A.", "{n} certificates in {s}, {t} of them at A+ or A.", "{s} bo‘yicha {n} ta sertifikat, ulardan {t} tasi — A+ yoki A.", "{n} сертификатов по предмету «{s}», из них {t} — уровня A+ или A."),
 "open": ("Sertifikatlardı kóriw", "See the certificates", "Sertifikatlarni ko‘rish", "Смотреть сертификаты"),
}
MON = {"kaa": ["yan", "fev", "mar", "apr", "may", "iyun", "iyul", "avg", "sen", "okt", "noy", "dek"],
       "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
       "uz": ["yan", "fev", "mar", "apr", "may", "iyun", "iyul", "avg", "sen", "okt", "noy", "dek"],
       "ru": ["янв", "фев", "мар", "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]}

def _num(v, i, d=2):
    s = f"{v:.{d}f}".rstrip("0").rstrip(".") if d else str(v)
    return s if i == 1 else s.replace(".", ",")
def _date(s, lang):
    d = _dt.date.fromisoformat(s)
    return f"{d.day} {MON[lang][d.month - 1]} {d.year}"
def _where(c):
    """University/college of a graduate, from graduates.py"""
    y, cy = c.get("grad"), c.get("cy")
    if not y or cy not in G.NAMES.get(y, []):
        return None
    k, f = G.PLACED[y][G.NAMES[y].index(cy)]
    return k
def stats(subj=None):
    L = [c for c in CERTS if subj in (None, c["subj"])]
    if not L:
        return None
    return dict(n=len(L), top=sum(c["level"] in ("A+", "A") for c in L), bplus=sum(c["level"] in ("A+", "A", "B+") for c in L),
                avg=sum(c["total"] for c in L) / len(L), best=max(L, key=lambda c: c["total"]))

def _card(c, k, i, lang, href):
    esc = _html.escape; col = LVCOL[c["level"]]; sc = SUBJ[c["subj"]]
    who = X["grad"][i].format(y=c["grad"]) if c.get("grad") else X["cur"][i] + (f' · {esc(c["cls"])}' if c.get("cls") else "")
    w = _where(c)
    where = f'<p class="ncwhere">{X["studies"][i].format(u=esc(G.INST[w][i]))}</p>' if w else ""
    bar = lambda lab, v: (f'<div class="ncbar"><span>{lab}</span><div><i style="width:{min(v, 75) / 75 * 100:.1f}%"></i></div><b>{_num(v, i)}</b></div>')
    secs = ""
    if c.get("sec"):
        tot = sum(c["sec"])
        rows = "".join(f'<li><span>{SEC[j][i]}</span><b>{_num(v, i, 3)}</b></li>' for j, v in enumerate(c["sec"]))
        stack = "".join(f'<i style="width:{v / tot * 100:.1f}%" class="s{j}"></i>' for j, v in enumerate(c["sec"]))
        secs = f'<details class="ncsec"><summary>{X["secs"][i]}</summary><div class="ncstack">{stack}</div><ul>{rows}</ul></details>'
    return (f'<article class="nccard card" id="nc{k}" data-k="{k}" data-l="{c["level"]}" data-s="{c["subj"]}" data-g="{"g" if c.get("grad") else "c"}" '
            f'data-t="{c["total"]}" data-d="{c["issued"]}" data-n="{esc(c["name"].lower())}" data-v="{c["valid"]}" style="--lc:{col}">'
            f'<div class="nchead"><span class="nclv">{c["level"]}</span><div class="nchd"><h3>{esc(c["name"])}</h3><p>{who}</p></div>'
            f'<div class="ncsc"><b>{_num(c["total"], i)}</b><small>{X["total"][i]} · {_num(c["pct"], i)}%</small></div></div>'
            f'<p class="ncsubj" style="--sc:{sc[4]}">{sc[i]}</p>{where}'
            f'<div class="ncbars">{bar(X["test"][i], c["test"])}{bar(X["written"][i], c["written"])}</div>{secs}'
            f'<div class="ncfoot"><span>{X["issued"][i]}: <b>{_date(c["issued"], lang)}</b></span><span>{X["valid"][i]}: <b>{_date(c["valid"], lang)}</b> '
            f'<em class="ncst" hidden></em></span></div></article>')

def page(i, href, tabs):
    lang = LANGS[i]; esc = _html.escape; st = stats()
    order = sorted(range(len(CERTS)), key=lambda k: (-CERTS[k]["total"], CERTS[k]["name"]))
    tiles = "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v, l in [
        (st["n"], X["t_all"][i]), (st["top"], X["t_top"][i]), (f'{round(st["bplus"] / st["n"] * 100)}%', X["t_bplus"][i]),
        (_num(st["avg"], i, 1), X["t_avg"][i]), (_num(st["best"]["total"], i), X["t_best"][i] + f' — {esc(st["best"]["name"])}')])
    # subject chips
    subs = sorted({c["subj"] for c in CERTS}, key=lambda s: list(SUBJ).index(s))
    schips = (f'<button type="button" class="chip on" data-s="all">{X["all"][i]} <em>{len(CERTS)}</em></button>' if len(subs) > 1 else "") + "".join(
        f'<button type="button" class="chip{"" if len(subs) > 1 else " on"}" data-s="{s}" style="--sc:{SUBJ[s][4]}">{SUBJ[s][i]} <em>{sum(c["subj"] == s for c in CERTS)}</em></button>' for s in subs)
    # level ladder
    cnt = {l: sum(c["level"] == l for c in CERTS) for l, _ in SCALE}; m = max(cnt.values()) or 1
    ladder = "".join(f'<button type="button" class="ncrung" data-l="{l}" style="--lc:{LVCOL[l]}"><span class="nclv">{l}</span>'
                     f'<span class="ncrb"><i style="width:{cnt[l] / m * 100:.0f}%"></i></span><b>{cnt[l]}</b><small>{X["from"][i].format(n=lo)}</small></button>'
                     for l, lo in SCALE)
    # score strip chart (45 - 75)
    lo_, hi_ = 45, 75; pos = lambda v: (min(max(v, lo_), hi_) - lo_) / (hi_ - lo_) * 100
    bands = ""; prev = hi_
    for l, lo in SCALE:
        bands += f'<i class="ncband" style="left:{pos(lo):.2f}%;width:{pos(prev) - pos(lo):.2f}%;--lc:{LVCOL[l]}"><span>{l}</span></i>'; prev = lo
    lanes = []; dots = ""
    for k in sorted(range(len(CERTS)), key=lambda k: CERTS[k]["total"]):
        c = CERTS[k]; x = pos(c["total"]); lane = 0
        while lane < len(lanes) and x - lanes[lane] < 2.2:
            lane += 1
        if lane == len(lanes):
            lanes.append(x)
        else:
            lanes[lane] = x
        dots += (f'<button type="button" class="ncdot{" r" if x > 72 else " l" if x < 22 else ""}" data-k="{k}" data-l="{c["level"]}" data-s="{c["subj"]}" data-g="{"g" if c.get("grad") else "c"}" '
                 f'style="left:{x:.2f}%;bottom:{10 + lane * 15}px;--lc:{LVCOL[c["level"]]}" aria-label="{esc(c["name"])}: {_num(c["total"], i)} ({c["level"]})">'
                 f'<span class="nctip">{esc(c["name"])} · <b>{_num(c["total"], i)}</b></span></button>')
    ticks = "".join(f'<span style="left:{pos(v):.2f}%">{v}</span>' for v in range(45, 76, 5))
    chart = (f'<div class="ncchart card"><div class="ncplot" style="height:{30 + len(lanes) * 15}px">{bands}{dots}</div>'
             f'<div class="ncticks">{ticks}</div></div>')
    cards = "".join(_card(CERTS[k], k, i, lang, href) for k in order)
    tools = (f'<div class="nctools"><input type="search" id="ncq" placeholder="{X["search"][i]}" aria-label="{X["search"][i]}">'
             f'<div class="chips ncg" role="group"><button type="button" class="chip on" data-g="all">{X["all"][i]}</button>'
             f'<button type="button" class="chip" data-g="g">{X["g_grad"][i]} <em>{sum(1 for c in CERTS if c.get("grad"))}</em></button>'
             f'<button type="button" class="chip" data-g="c">{X["g_cur"][i]} <em>{sum(1 for c in CERTS if not c.get("grad"))}</em></button></div>'
             f'<label class="ncsort">{X["sort"][i]} <select id="ncsort"><option value="t">{X["s_score"][i]}</option><option value="d">{X["s_new"][i]}</option>'
             f'<option value="n">{X["s_name"][i]}</option></select></label></div>'
             f'<p class="ncshown"><span id="ncn"></span> <button type="button" class="ncreset" id="ncr" hidden>{X["reset"][i]} ×</button></p>')
    how = (f'<div class="card nchow"><h2>{X["how_h"][i]}</h2><ul><li>{X["how_1"][i]}</li><li>{X["how_2"][i]}</li><li>{X["how_3"][i]}</li></ul>'
           f'<div class="ncscale">' + "".join(f'<span style="--lc:{LVCOL[l]}"><b>{l}</b>{lo}+</span>' for l, lo in SCALE) + '</div></div>')
    T = {"shown": X["shown"][i], "ok": X["ok"][i], "exp": X["exp"][i]}
    js = ("<script>(function(){var T=" + json.dumps(T, ensure_ascii=False) + r""",today=new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Tashkent'}).format(new Date());
var grid=document.getElementById('ncgrid'),cards=[].slice.call(grid.children),q=document.getElementById('ncq'),F={l:'all',g:'all',s:document.querySelector('.ncsubjs .chip.on').dataset.s};
cards.forEach(function(c){var e=c.querySelector('.ncst');e.hidden=false;var ok=c.dataset.v>=today;e.textContent=ok?T.ok:T.exp;e.className='ncst '+(ok?'ok':'exp')});
function run(){var v=q.value.trim().toLowerCase(),n=0;cards.forEach(function(c){var ok=(F.l==='all'||c.dataset.l===F.l)&&(F.g==='all'||c.dataset.g===F.g)&&(F.s==='all'||c.dataset.s===F.s)&&(!v||c.dataset.n.indexOf(v)>=0);c.hidden=!ok;if(ok)n++});
 document.querySelectorAll('.ncdot').forEach(function(d){var c=document.getElementById('nc'+d.dataset.k);d.classList.toggle('dim',c.hidden)});
 document.querySelectorAll('.ncrung').forEach(function(r){r.classList.toggle('on',r.dataset.l===F.l);r.classList.toggle('dim',F.l!=='all'&&r.dataset.l!==F.l)});
 document.getElementById('ncn').textContent=T.shown.replace('{n}',n);document.getElementById('ncnone').hidden=n>0;
 document.getElementById('ncr').hidden=!(F.l!=='all'||F.g!=='all'||v)}
function chips(sel,key){var bs=document.querySelectorAll(sel+' .chip');bs.forEach(function(b){b.addEventListener('click',function(){bs.forEach(function(x){x.classList.toggle('on',x===b)});F[key]=b.dataset[key];run()})})}
chips('.ncg','g');chips('.ncsubjs','s');
document.querySelectorAll('.ncrung').forEach(function(r){r.addEventListener('click',function(){F.l=F.l===r.dataset.l?'all':r.dataset.l;run();document.getElementById('nclist').scrollIntoView({behavior:'smooth',block:'start'})})});
document.querySelectorAll('.ncdot').forEach(function(d){d.addEventListener('click',function(){var c=document.getElementById('nc'+d.dataset.k);if(c.hidden){F.l='all';F.g='all';q.value='';document.querySelectorAll('.ncg .chip').forEach(function(x){x.classList.toggle('on',x.dataset.g==='all')});run()}
 c.scrollIntoView({behavior:'smooth',block:'center'});c.classList.remove('flash');void c.offsetWidth;c.classList.add('flash')})});
document.getElementById('ncsort').addEventListener('change',function(e){var k=e.target.value;cards.sort(function(a,b){return k==='t'?b.dataset.t-a.dataset.t:k==='d'?(a.dataset.d<b.dataset.d?1:a.dataset.d>b.dataset.d?-1:b.dataset.t-a.dataset.t):a.dataset.n.localeCompare(b.dataset.n)});cards.forEach(function(c){grid.appendChild(c)})});
document.getElementById('ncr').addEventListener('click',function(){F.l='all';F.g='all';q.value='';document.querySelectorAll('.ncg .chip').forEach(function(x){x.classList.toggle('on',x.dataset.g==='all')});run()});
q.addEventListener('input',run);run()})();</script>""")
    return (f'{tabs(SUB, i, href)}<p class="lead2">{X["lead"][i]}</p><div class="chips ncsubjs" role="group">{schips}</div>'
            f'<div class="stats gstats ncstats">{tiles}</div>'
            f'<div class="nctwo"><div class="card ncladder"><h2>{X["ladder_h"][i]}</h2><p class="note">{X["ladder_p"][i]}</p>{ladder}</div>'
            f'<div><h2>{X["chart_h"][i]}</h2><p class="note">{X["chart_p"][i]}</p>{chart}{how}</div></div>'
            f'<h2 id="nclist">{X["list_h"][i]}</h2>{tools}<div class="ncgrid" id="ncgrid">{cards}</div>'
            f'<p class="note" id="ncnone" hidden>{X["none"][i]}</p><p class="note">{X["note"][i]}</p>{js}')

def teaser(subj, i, href):
    """Block for a subject teacher's profile."""
    st = stats(subj)
    if not st:
        return ""
    return (f'<h2>{X["prof_h"][i]}</h2><a class="card ncteaser" href="{href(SUB)}"><span class="nclv" style="--lc:{LVCOL["A+"]}">{st["n"]}</span>'
            f'<div><b>{SUBJ[subj][i]}</b><p>{X["prof_p"][i].format(s=SUBJ[subj][i], n=st["n"], t=st["top"])}</p></div><span class="acgo2">{X["open"][i]} →</span></a>')
