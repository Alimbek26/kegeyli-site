# News posts, newest first. To add a post: copy one block, set date (YYYY-MM-DD) and write the title/text in
# the order Karakalpak, English, Uzbek, Russian. Optional: photo="news/file.jpg" (file in photos/news/), tag="olympiad".
# tag is one of: event, result, project, announce
MONTHS = [
 ("Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"),
 ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"),
 ("yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentabr", "oktabr", "noyabr", "dekabr"),
 ("января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"),
]
NAME = ("Jańalıqlar", "News", "Yangiliklar", "Новости")
DESC = ("Kegeyli rayonı qánigelestirilgen mektebiniń jańalıqları: ushırasıwlar, nátiyjeler, joybarlar.",
        "News from Kegeyli District Specialized School: events, results and projects.",
        "Kegeli tumani ixtisoslashtirilgan maktabi yangiliklari: uchrashuvlar, natijalar, loyihalar.",
        "Новости Кегейлийской районной специализированной школы: события, результаты, проекты.")
TAGS = {"event": ("Waqıya", "Event", "Tadbir", "Событие"), "result": ("Nátiyje", "Result", "Natija", "Результат"),
        "project": ("Joybar", "Project", "Loyiha", "Проект"), "announce": ("Xabarlama", "Announcement", "E’lon", "Объявление")}
TAGCOL = {"event": "#2a7fd1", "result": "#d97706", "project": "#7c3aed", "announce": "#0b7a8f"}
TAGICON = {"event": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
           "result": '<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0zM17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>',
           "project": '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.600 10.800c.6.500 1.100 1.300 1.100 2.200h5c0-.9.5-1.700 1.100-2.200A6 6 0 0 0 12 3z"/>',
           "announce": '<path d="M4 10v4h3l7 4V6l-7 4zM17 9a4 4 0 0 1 0 6"/>'}
READ = ("Tolıq oqıw", "Read more", "Batafsil", "Читать далее")
EMPTY = ("Jańalıqlar tez arada.", "News coming soon.", "Yangiliklar tez orada.", "Новости скоро появятся.")
TG_BTN = ("Telegram kanalımız", "Our Telegram channel", "Telegram kanalimiz", "Наш Telegram-канал")
ALL = ("Barlıq jańalıqlar", "All news", "Barcha yangiliklar", "Все новости")
NEWS = [
 dict(date="2026-11-20", tag="event",
  title=('Belsendi oqıwshılar ushırasıwı', 'Meeting of active students', 'Faol o‘quvchilar uchrashuvi', 'Встреча активных учеников'),
  text=('Qaraqalpaqstan Respublikası jaslar isleri basqarması hám Balalar shólkemi shólkemlestirgen 10–18 jastaǵı belsendi oqıwshılar ushırasıwına mektebimiz oqıwshıları da qatnastı.', "Our students took part in a meeting of active young people aged 10–18, organized by the Youth Affairs Department of the Republic of Karakalpakstan and the Children's Organization.", 'Qoraqalpog‘iston Respublikasi yoshlar ishlari boshqarmasi va Bolalar tashkiloti tashkil etgan 10–18 yoshdagi faol o‘quvchilar uchrashuvida maktabimiz o‘quvchilari ham qatnashdi.', 'Наши ученики приняли участие во встрече активной молодёжи 10–18 лет, организованной Управлением по делам молодёжи Республики Каракалпакстан и Детской организацией.')),
 dict(date="2026-11", tag="result",
  title=('Xalıqaralıq sertifikat nátiyjeleri', 'International certificate results', 'Xalqaro sertifikat natijalari', 'Результаты международных сертификатов'),
  text=('11-b klass oqıwshımız fizika, matematika, IELTS, SAT hám rus tili boyınsha xalıqaralıq sertifikat nátiyjelerin qolǵa kirgizdi.', 'A student of class 11-B achieved international certificate results in physics, mathematics, IELTS, SAT and Russian.', '11-b sinf o‘quvchimiz fizika, matematika, IELTS, SAT va rus tili bo‘yicha xalqaro sertifikat natijalarini qo‘lga kiritdi.', 'Ученик 11-Б класса получил результаты международных сертификатов по физике, математике, IELTS, SAT и русскому языку.')),
 dict(date="2026-11", tag="project",
  title=('Ingliz tili joybarları', 'English language projects', 'Ingliz tili loyihalari', 'Проекты по английскому языку'),
  text=('9-c klass oqıwshıları ingliz tili páninen joybar jumısların usınıs etti.', 'Students of class 9-C presented their English language project work.', '9-c sinf o‘quvchilari ingliz tili fanidan loyiha ishlarini taqdim etishdi.', 'Ученики 9-C класса представили проектные работы по английскому языку.')),
]
def fmt(date, i):
    p = date.split("-")
    m = MONTHS[i][int(p[1]) - 1]
    return (f"{int(p[2])} {m} {p[0]}" if len(p) > 2 else f"{m} {p[0]}") if i else (f"{int(p[2])}-{m.lower()}, {p[0]}" if len(p) > 2 else f"{m}, {p[0]}")

ORIG = ("Telegramdaǵı original", "Original on Telegram", "Telegramdagi asl post", "Оригинал в Telegram")

def _src(n, i):
    return f'<a class="nsrc" href="{n["url"]}" rel="noopener" target="_blank">{ORIG[i]} →</a>' if n.get("url") else ""

def cards(i, limit=None, up=""):
    items = sorted(NEWS, key=lambda n: n["date"], reverse=True)[:limit]
    out = ""
    for n in items:
        tg = n.get("tag", "announce")
        ph = f'<img class="nph" src="{up}photos/{n["photo"]}" alt="" loading="lazy">' if n.get("photo") else ""
        out += (f'<article class="card ncard" style="--mc:{TAGCOL[tg]}">{ph}<div class="nbody"><div class="nmeta"><span class="ntag"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{TAGICON[tg]}</svg>{TAGS[tg][i]}</span>'
                f'<time datetime="{n["date"]}">{fmt(n["date"], i)}</time></div><h3>{n["title"][i]}</h3><p>{n["text"][i]}</p>{_src(n, i)}</div></article>')
    return out or f'<p>{EMPTY[i]}</p>'

def body(i, up, tg):
    import tgfeed as TGF
    return (f'{TGF.html(i, len(TGF.POSTS))}<div class="ngrid">{cards(i, None, up)}</div>'
            f'<p style="margin-top:22px"><a class="btn p" href="{tg}" rel="noopener">{TG_BTN[i]} →</a></p>')
