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
 dict(date="2025-01-20", tag="result",
  title=("Ayjamal Abdullaeva Colorado State University-ge qabıl etildi", "Ayjamal Abdullaeva admitted to Colorado State University", "Ayjamal Abdullayeva Colorado State University’ga qabul qilindi", "Айжамал Абдуллаева принята в Colorado State University"),
  text=("Mektebimizdiń 11-«a» klass oqıwshısı Ayjamal Abdullaeva AQShtıń Colorado State University-diń Economics (ekonomika) baǵdarına oqıwǵa qabıl etildi. Ayjamalǵa áwmet tileymiz hám basqa pitkeriwshilerimizden de jaqsı jańalıqlar kútemiz!",
        "Ayjamal Abdullaeva, a Grade 11-A student at our school, has been admitted to Colorado State University in the USA to study Economics. We wish Ayjamal every success and look forward to more good news from our graduates!",
        "Maktabimizning 11-«a» sinf o‘quvchisi Ayjamal Abdullayeva AQShning Colorado State University’dagi Economics (iqtisodiyot) yo‘nalishiga o‘qishga qabul qilindi. Ayjamalga omad tilaymiz va boshqa bitiruvchilarimizdan ham yaxshi xabarlar kutamiz!",
        "Ученица 11 «А» класса нашей школы Айжамал Абдуллаева принята в Colorado State University (США) на направление Economics (экономика). Желаем Айжамал успехов и ждём хороших новостей от других выпускников!")),
 dict(date="2025-01-05", tag="result", photo="gallery/events/ismailova-cambridge-programme.jpg",
  title=("Oqıwshımız úsh AQSh universitetine qabıl etildi", "Our student admitted to three US universities", "O‘quvchimiz AQShning uchta universitetiga qabul qilindi", "Наша ученица принята в три университета США"),
  text=("Kegeyli rayonı qánigelestirilgen mektebiniń 11-«a» klass oqıwshısı Húrshida Ismailova AQSh universitetlerinen biri — Pennsylvania Western University-ge oqıwǵa qabıl etildi hám oǵan 7000 dollar muǵdarında grant ajıratıldı. Sonday-aq ol Colorado State University-diń Computer Science (kompyuter ilimleri) baǵdarına 2025-jıl gúzgi semestrine qabıl etildi. 8-yanvarda ol Caldwell University-diń Computer Science baǵdarına da qabıl etilip, Honors Program stipendiyasına ılayıq dep tabıldı. Fotoda: Húrshida Kembridj universitetiniń programmasında.",
        "Húrshida Ismailova, a Grade 11-A student at Kegeyli District Specialized School, was admitted to Pennsylvania Western University in the USA and awarded a $7,000 grant. She was also admitted to Colorado State University to study Computer Science, starting in fall 2025. On 8 January she was also admitted to Caldwell University’s Computer Science programme and qualified for its Honors Program scholarship. Photo: Húrshida at a University of Cambridge programme.",
        "Kegeyli tumani ixtisoslashtirilgan maktabining 11-«a» sinf o‘quvchisi Xurshida Ismailova AQSh universitetlaridan biri — Pennsylvania Western University’ga o‘qishga qabul qilindi va unga 7000 dollar miqdorida grant ajratildi. Shuningdek, u Colorado State University’ning Computer Science (kompyuter fanlari) yo‘nalishiga 2025-yil kuzgi semestriga qabul qilindi. 8-yanvarda u Caldwell University’ning Computer Science yo‘nalishiga ham qabul qilinib, Honors Program stipendiyasiga loyiq deb topildi. Suratda: Xurshida Kembrij universiteti dasturida.",
        "Ученица 11 «А» класса Кегейлийской районной специализированной школы Хуршида Исмайлова принята в Pennsylvania Western University (США) и получила грант в размере $7000. Также она принята в Colorado State University на направление Computer Science (компьютерные науки) с осеннего семестра 2025 года. 8 января она также была принята в Caldwell University на направление Computer Science и получила право на стипендию Honors Program. На фото: Хуршида на программе Кембриджского университета.")),
 dict(date="2023-02-07", tag="result", photo="gallery/events/pdp-grant-saparniyazov.jpg",
  title=("Eki oqıwshımız PDP University grantın jeńip aldı", "Two of our students win PDP University grants", "Ikki o‘quvchimiz PDP University grantini yutdi", "Двое наших учеников выиграли гранты PDP University"),
  text=("Kegeyli rayonı qánigelestirilgen mektebiniń oqıwshıları Artıqbay Saparniyazov (10-klass) hám Ádilbek Jumabaev (11-klass) matematikadan Respublika pán olimpiadasınıń saralaw basqıshında joqarı ball alıp, hár biri PDP University tárepinen 12 000 000 swmlıq granttıń iyesi boldı.",
        "Artıqbay Saparniyazov (Grade 10) and Adilbek Jumabaev (Grade 11), students at Kegeyli District Specialized School, scored highly in the qualifying round of the Republican Mathematics Olympiad, and each was awarded a grant of 12,000,000 so‘m by PDP University.",
        "Kegeyli tumani ixtisoslashtirilgan maktabi o‘quvchilari Artiqbay Saparniyazov (10-sinf) va Adilbek Jumabaev (11-sinf) matematika bo‘yicha Respublika fan olimpiadasining saralash bosqichida yuqori ball to‘plab, har biri PDP University tomonidan 12 000 000 so‘mlik grant sohibi bo‘ldi.",
        "Ученики Кегейлийской районной специализированной школы Артыкбай Сапарниязов (10 класс) и Адилбек Жумабаев (11 класс) набрали высокие баллы на отборочном этапе Республиканской олимпиады по математике, и каждый получил грант PDP University на 12 000 000 сумов.")),
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
    return (f'<div class="ngrid">{cards(i, None, up)}</div>'
            f'<p style="margin-top:22px"><a class="btn p" href="{tg}" rel="noopener">{TG_BTN[i]} →</a></p>')
