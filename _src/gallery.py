# Photo gallery (Gallery page is being prepared). Photos live in photos/gallery/<section>/:
#   <name>.jpg (max 1600 px, for the large view) and <name>-t.jpg (600 px thumbnail).
# Sections: building, classrooms, labs, library, canteen, sports, events.
# consent: True once the people shown (and parents, for students) agreed to publication.
# who: teachers shown (Cyrillic names exactly as in teachers.TEACHERS) - links the photo to their profiles.
SECTIONS = ["building", "classrooms", "labs", "library", "canteen", "sports", "events"]
PHOTOS = [
 dict(section="events", file="events/uzbek-language-teachers", who=["Исмайлова Гулмира", "Қутлимуратов Сарманбек"], consent=True,
      cap=("Ózbek tili hám ádebiyatı muǵallimleri Ismaylova Gulmira hám Qutlimuratov Sarmanbek",
           "Uzbek language and literature teachers Ismaylova Gulmira and Qutlimuratov Sarmanbek",
           "O‘zbek tili va adabiyoti o‘qituvchilari Ismaylova Gulmira va Qutlimuratov Sarmanbek",
           "Учителя узбекского языка и литературы Исмайлова Гулмира и Қутлимуратов Сарманбек")),
 dict(section="events", file="events/olympiad-diploma", leader="Islam Pirniyazov", consent=True,   # student and parents agreed
      todo="add student name, class, olympiad name/subject and date",
      cap=("Islam Pirniyazov olimpiada jeńimpazına 1-dárejeli diplom tapsırmaqta",
           "Islam Pirniyazov presents a 1st-degree olympiad diploma",
           "Islam Pirniyazov olimpiada g‘olibiga 1-darajali diplom topshirmoqda",
           "Ислам Пирниязов вручает диплом I степени победителю олимпиады")),
]

# ---- batch of 28.11.2026 (consent confirmed by the school 28.11.2026)
def _e(file, kaa, en, uz, ru, **kw):
    return dict(section="events", file="events/" + file, cap=(kaa, en, uz, ru), consent=kw.pop("consent", True), **kw)
PHOTOS += [
 _e("navruz-teachers", "Mektebimiz jámáátı Náwrız bayramında", "Our school staff at the Navruz celebration", "Maktabimiz jamoasi Navro‘z bayramida", "Коллектив школы на празднике Навруз", tag="navruz"),
 _e("navruz-girls-costumes", "Oqıwshılar qaraqalpaq milliy kiyimlerinde — Náwrız bayramı", "Students in Karakalpak national dress at Navruz", "O‘quvchilar qoraqalpoq milliy liboslarida — Navro‘z bayrami", "Ученицы в каракалпакских национальных костюмах на Наврузе", tag="navruz"),
 _e("navruz-national-table", "Náwrız: milliy taǵamlar, kiyimler hám saz ásbapları kórgizbesi", "Navruz: a display of national dishes, costumes and instruments", "Navro‘z: milliy taomlar, liboslar va cholg‘u asboblari ko‘rgazmasi", "Навруз: выставка национальных блюд, костюмов и музыкальных инструментов", tag="navruz"),
 _e("navruz-audience", "Náwrız bayramındaǵı oqıwshılar", "Students at the Navruz celebration", "Navro‘z bayramida o‘quvchilar", "Ученики на празднике Навруз", tag="navruz"),
 _e("outdoor-lesson", "Ashıq hawadaǵı sabaq", "A lesson outdoors", "Ochiq havodagi dars", "Урок на свежем воздухе"),
 _e("bake-sale", "Oqıwshılar tayarlaǵan taǵamlar jármeńkesi", "A fair of food baked by students", "O‘quvchilar tayyorlagan pishiriqlar yarmarkasi", "Ярмарка выпечки, приготовленной учениками"),
 _e("staff-group", "Mektebimiz jámáátı", "Our school team", "Maktabimiz jamoasi", "Коллектив школы"),
 _e("hakim-cup-ceremony", "«Kegeyli rayonı hákim kubogı» olimpiadası jeńimpazların sıylaw", "Awarding the winners of the “Kegeyli District Governor’s Cup” olympiad", "«Kegeyli tumani hokim kubogi» olimpiadasi g‘oliblarini taqdirlash", "Награждение победителей олимпиады «Кубок хокима Кегейлийского района»", tag="hakim-cup",
    note="diplomas: science subjects, 6th-grade students, held at our school; add date and winners"),
 _e("hakim-cup-winners", "«Kegeyli rayonı hákim kubogı» olimpiadasınıń jeńimpazları", "Winners of the “Kegeyli District Governor’s Cup” olympiad", "«Kegeyli tumani hokim kubogi» olimpiadasi g‘oliblari", "Победители олимпиады «Кубок хокима Кегейлийского района»", tag="hakim-cup"),
 _e("trip-presidential-school", "Oqıwshılarımız Prezident mektebinde", "Our students at the Presidential School", "O‘quvchilarimiz Prezident maktabida", "Наши ученики в Президентской школе", date="2025-04-30", tag="trip"),
 _e("trip-youth-centre", "Jaslar orayına sapar", "Visit to the Youth Centre", "Yoshlar markaziga tashrif", "Посещение Молодёжного центра", date="2025-04-30", tag="trip"),
 _e("trip-savitsky-museum", "I. V. Savickiy atındaǵı mámleketlik kórkem óner muzeyine sapar", "Visit to the Savitsky State Museum of Art", "I. V. Savitskiy nomidagi davlat san’at muzeyiga sayohat", "Экскурсия в Государственный музей искусств им. И. В. Савицкого", tag="trip"),
 _e("yosh-contest-winner", "«YOSH» tańlawınıń jeńimpazı: diplom hám jeńimpaz komandaǵa biypul sayaxat jollaması", "Winner of the “YOSH” contest: a diploma and a free-trip voucher for the winning team", "«YOSH» tanlovi g‘olibi: diplom va g‘olib jamoaga bepul sayohat yo‘llanmasi", "Победитель конкурса «YOSH»: диплом и путёвка на бесплатную поездку для команды-победителя", date="2025-05-22",
    note="poster: team 'Mind-Masters'; diploma looks like 1st place; add student name/class, who the adult is, and consent"),
]

# ---- batch 2 of 28.11.2026 (drafts: consent, dates and event names to confirm)
PHOTOS += [
 _e("welcome-balloons", "Oqıwshılar ustazlardı sharlar menen kútip almaqta", "Students welcome teachers with balloons", "O‘quvchilar ustozlarni sharlar bilan kutib olmoqda", "Ученики встречают учителей с шарами", date="2025", note="event not recorded"),
 _e("teacher-nominations", "Ustazlardı nominaciyalar boyınsha sıylaw: «Eń quwnaq ustaz», «Eń talabshań ustaz» hám basqalar", "Teachers honoured in nominations such as “Most cheerful teacher” and “Most demanding teacher”", "Ustozlarni nominatsiyalar bo‘yicha taqdirlash: «Eng quvnoq ustoz», «Eng talabchan ustoz» va boshqalar", "Награждение учителей в номинациях «Самый весёлый учитель», «Самый требовательный учитель» и др.", date="2025", note="one certificate shows 'Ismailova Gúlmira'; confirm names, event and date"),
 _e("english-day-guests", "Mehmanlar «Tuesday — English Day» múyeshinde", "Guests at our “Tuesday — English Day” corner", "Mehmonlar «Tuesday — English Day» burchagida", "Гости у уголка «Tuesday — English Day»", date="2025", note="who are the guests? date?"),
 _e("autumn-costumes", "Gúz bayramı: oqıwshılar óz qolı menen tayarlaǵan kiyimler", "Autumn festival: costumes the students made themselves", "Kuz bayrami: o‘quvchilar o‘z qo‘llari bilan tayyorlagan liboslar", "Осенний праздник: костюмы, сделанные учениками своими руками", date="2025", note="event name?"),
 _e("karakalpak-language-day-dance", "1-dekabr — Qaraqalpaq tiline mámleketlik til mártebesi berilgen kún: milliy biy", "1 December, Karakalpak Language Day: a national dance", "1-dekabr — Qoraqalpoq tiliga davlat tili maqomi berilgan kun: milliy raqs", "1 декабря — День придания каракалпакскому языку статуса государственного: национальный танец", date="2025-12-01", tag="language-day"),
 _e("new-year-staff-gifts", "Jańa jıl bayramında ayal xızmetkerlerimizge sawǵalar", "New Year gifts for our female staff", "Yangi yil bayramida xodimalarimizga sovg‘alar", "Новогодние подарки нашим сотрудницам", date="2025-12", tag="new-year"),
 _e("new-year-group", "Jańa jıl bayramı: oqıwshılar hám ustazlar birge", "New Year celebration: students and teachers together", "Yangi yil bayrami: o‘quvchilar va ustozlar birga", "Новогодний праздник: ученики и учителя вместе", date="2025-12", tag="new-year"),
 _e("staff-celebration-stage", "Mektebimiz jámáátı bayram keshesinde", "Our school staff at a celebration", "Maktabimiz jamoasi bayram kechasida", "Коллектив школы на праздничном вечере", date="2025", tag="staff-event", note="cropped table/coats at bottom; which celebration?"),
 _e("staff-game-men", "Muǵallimler arasındaǵı oyın", "A game among the teachers", "O‘qituvchilar o‘rtasidagi o‘yin", "Игра среди учителей", date="2025", tag="staff-event"),
 _e("staff-game-women", "Muǵallimler arasındaǵı tańlaw", "A contest among the teachers", "O‘qituvchilar o‘rtasidagi tanlov", "Конкурс среди учителей", date="2025", tag="staff-event", note="cropped audience heads at bottom"),
]

PHOTOS += [
 _e("turganbaeva-arizona", "Aynura Turǵanbaeva — University of Arizona-nıń 16 000 dollarlıq grantınıń iyesi", "Aynura Turganbaeva, winner of a $16,000 grant from the University of Arizona", "Aynura Turg‘anbayeva — University of Arizona’ning 16 000 dollarlik granti sohibi", "Айнура Турганбаева — обладательница гранта University of Arizona на $16 000", date="2025-05-17"),
 _e("ismailova-cambridge-programme", "Khurshida Ismailova Kembridj universitetiniń programmasında", "Khurshida Ismailova at a University of Cambridge programme", "Khurshida Ismailova Kembrij universiteti dasturida", "Хуршида Исмайлова на программе Кембриджского университета"),
 _e("pdp-grant-jumabaev", "Ádilbek Jumabaev — PDP University-diń 12 mln swmlıq grantınıń iyesi", "Adilbek Jumabaev won a 12 million so‘m grant from PDP University", "Adilbek Jumabaev — PDP Universityning 12 mln so‘mlik granti sohibi", "Адилбек Жумабаев — обладатель гранта PDP University на 12 млн сумов", date="2023-02-07"),
 _e("pdp-grant-saparniyazov", "Artıqbay Saparniyazov — PDP University-diń 12 mln swmlıq grantınıń iyesi", "Artıqbay Saparniyazov won a 12 million so‘m grant from PDP University", "Artiqbay Saparniyazov — PDP Universityning 12 mln so‘mlik granti sohibi", "Артыкбай Сапарниязов — обладатель гранта PDP University на 12 млн сумов", date="2023-02-07"),
]

# ======================= Gallery page =======================
import html as _html, json as _json, os as _os
SUB = "gallery/"
NAME = ("Fotogalereya", "Photo gallery", "Fotogalereya", "Фотогалерея")
DESC = ("Mektep turmısınan fotosúwretler: bayramlar, ustazlar jámáátı, olimpiada jeńimpazları, saparlar hám oqıwshılar ómiri.",
        "Photos from school life: holidays, our teachers, olympiad winners, trips and everyday student life.",
        "Maktab hayotidan suratlar: bayramlar, ustozlar jamoasi, olimpiada g‘oliblari, sayohatlar va o‘quvchilar hayoti.",
        "Фотографии из жизни школы: праздники, учителя, победители олимпиад, экскурсии и жизнь учеников.")

# albums: key -> (title x4, one-line description x4, colour)
ALBUMS = {
 "holidays": (("Bayramlar", "Holidays", "Bayramlar", "Праздники"),
              ("Náwrız, Jańa jıl hám Qaraqalpaq tili kúni", "Navruz, New Year and Karakalpak Language Day", "Navro‘z, Yangi yil va Qoraqalpoq tili kuni", "Навруз, Новый год и День каракалпакского языка"), "#a3202c"),
 "staff": (("Ustazlar jámáátı", "Our teachers", "Ustozlar jamoasi", "Наши учителя"),
           ("Muǵallimlerimiz, olardıń sıylıqları hám bayram keshleri", "Our teachers, their awards and staff celebrations", "O‘qituvchilarimiz, ularning mukofotlari va bayram kechalari", "Наши учителя, их награды и праздничные вечера"), "#0b5f78"),
 "awards": (("Olimpiada hám tańlawlar", "Olympiads and contests", "Olimpiada va tanlovlar", "Олимпиады и конкурсы"),
            ("Jeńimpazlarımızdı sıylaw", "Celebrating our winners", "G‘oliblarimizni taqdirlash", "Награждение наших победителей"), "#d97706"),
 "trips": (("Saparlar", "Trips", "Sayohatlar", "Экскурсии"),
           ("Muzeyler, Prezident mektebi hám Jaslar orayı", "Museums, the Presidential School and the Youth Centre", "Muzeylar, Prezident maktabi va Yoshlar markazi", "Музеи, Президентская школа и Молодёжный центр"), "#0891b2"),
 "life": (("Mektep turmısı", "School life", "Maktab hayoti", "Школьная жизнь"),
          ("Sabaqlar, jármeńkeler, ińglis tili kúni hám basqa da kúnlerimiz", "Lessons, fairs, English Day and our everyday", "Darslar, yarmarkalar, ingliz tili kuni va kundalik hayotimiz", "Уроки, ярмарки, День английского и наши будни"), "#16a34a"),
}
ALBUM_OF = {
 "navruz-teachers": "holidays", "navruz-girls-costumes": "holidays", "navruz-national-table": "holidays", "navruz-audience": "holidays",
 "karakalpak-language-day-dance": "holidays", "new-year-staff-gifts": "holidays", "new-year-group": "holidays",
 "uzbek-language-teachers": "staff", "staff-group": "staff", "teacher-nominations": "staff", "welcome-balloons": "staff",
 "staff-celebration-stage": "staff", "staff-game-men": "staff", "staff-game-women": "staff",
 "olympiad-diploma": "awards", "pdp-grant-saparniyazov": "awards", "pdp-grant-jumabaev": "awards", "ismailova-cambridge-programme": "awards", "turganbaeva-arizona": "awards", "hakim-cup-ceremony": "awards", "hakim-cup-winners": "awards", "yosh-contest-winner": "awards",
 "trip-presidential-school": "trips", "trip-youth-centre": "trips", "trip-savitsky-museum": "trips",
 "outdoor-lesson": "life", "bake-sale": "life", "autumn-costumes": "life", "english-day-guests": "life",
}
COVER = {"holidays": "karakalpak-language-day-dance", "staff": "teacher-nominations", "awards": "hakim-cup-winners", "trips": "trip-savitsky-museum", "life": "autumn-costumes"}
TAGS = {"navruz": ("Náwrız", "Navruz", "Navro‘z", "Навруз"), "new-year": ("Jańa jıl", "New Year", "Yangi yil", "Новый год"),
        "language-day": ("Til kúni", "Language Day", "Til kuni", "День языка"), "hakim-cup": ("Hákim kubogı", "Governor’s Cup", "Hokim kubogi", "Кубок хокима"),
        "trip": None, "staff-event": None}
MON = (["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentyabr", "oktyabr", "noyabr", "dekabr"],
       ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
       ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentabr", "oktabr", "noyabr", "dekabr"],
       ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"])
MON_NOM = ["dekabr", "December", "dekabr", "декабрь"]  # only month-only date used so far is December
T = dict(
 lead=("Mektebimizdiń ómirinen kórinisler. Albomdı tańlań yamasa fotonı basıp úlken etip kóriń.",
       "Moments from the life of our school. Pick an album, or tap any photo to see it large.",
       "Maktabimiz hayotidan lavhalar. Albomni tanlang yoki suratni bosib kattalashtiring.",
       "Моменты из жизни нашей школы. Выберите альбом или нажмите на фото, чтобы увеличить."),
 photos=("foto", "photos", "ta surat", "фото"), albums=("albom", "albums", "ta albom", "альбомов"),
 all=("Barlıǵı", "All photos", "Barchasi", "Все фото"),
 teachers=("Fotoda:", "In the photo:", "Suratda:", "На фото:"),
 prev=("Aldıńǵı", "Previous", "Oldingi", "Предыдущее"), next=("Keyingi", "Next", "Keyingi", "Следующее"), close=("Jabıw", "Close", "Yopish", "Закрыть"),
 soon_h=("Mektebimiz: imarat hám klasslar", "Our school: building and classrooms", "Maktabimiz: bino va sinflar", "Наша школа: здание и классы"),
 soon_p=("Imarat, klasslar, laboratoriyalar, kitapxana, asxana hám sport zalınıń fotoları jaqın arada qosıladı.",
         "Photos of the building, classrooms, labs, library, canteen and sports hall are coming soon.",
         "Bino, sinflar, laboratoriyalar, kutubxona, oshxona va sport zali suratlari tez orada qo‘shiladi.",
         "Фото здания, классов, лабораторий, библиотеки, столовой и спортзала скоро появятся."),
 open=("Ashıw", "Open", "Ochish", "Открыть"),
 home_more=("Barlıq fotolar", "See all photos", "Barcha suratlar", "Все фото"),
)
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
def _size(path):
    try:
        from PIL import Image
        with Image.open(_os.path.join(_ROOT, path)) as im: return im.size
    except Exception: return (600, 450)
def _slug(p): return p["file"].split("/")[-1]
def fmt_date(d, i):
    if not d: return ""
    y, *r = d.split("-")
    if not r: return y
    m = int(r[0]) - 1
    if len(r) == 1: return f"{MON_NOM[i] if m == 11 else MON[i][m]} {y}"
    dd = int(r[1])
    return f"{MON[i][m]} {dd}, {y}" if i == 1 else f"{dd}-{MON[i][m]} {y}" if i in (0, 2) else f"{dd} {MON[i][m]} {y}"
def shown():
    """Photos that can be published, newest first inside each album (undated last)."""
    ps = [p for p in PHOTOS if p.get("consent") is True and _slug(p) in ALBUM_OF]
    return sorted(ps, key=lambda p: (list(ALBUMS).index(ALBUM_OF[_slug(p)]), -(int((p.get("date") or "0").replace("-", "").ljust(8, "0")))))

_LANGI = {"kaa": 0, "en": 1, "uz": 2, "ru": 3}
def body(lang, href, up, who_link):
    """who_link(cyr_name_or_leader) -> (href, shown_name) or None"""
    i = _LANGI[lang]; ps = shown(); e = _html.escape
    counts = {a: sum(ALBUM_OF[_slug(p)] == a for p in ps) for a in ALBUMS}
    alb_cards = []
    for a, (tt, dd, col) in ALBUMS.items():
        if not counts[a]: continue
        cv = f"{up}photos/gallery/events/{COVER[a]}-t.jpg"
        alb_cards.append(f'<button type="button" class="galb" data-a="{a}" style="--ac:{col}" aria-pressed="false"><img src="{cv}" alt="" loading="lazy" width="600" height="450"><span class="galbt"><b>{tt[i]}</b><small>{dd[i]}</small><em>{counts[a]} {T["photos"][i]}</em></span></button>')
    chips = f'<button type="button" class="chip on" data-a="">{T["all"][i]} <em>{len(ps)}</em></button>' + "".join(
        f'<button type="button" class="chip" data-a="{a}" style="--ac:{v[2]}">{v[0][i]} <em>{counts[a]}</em></button>' for a, v in ALBUMS.items() if counts[a])
    figs, data = [], []
    for n, p in enumerate(ps):
        s = _slug(p); a = ALBUM_OF[s]; cap = p["cap"][i]; dt = fmt_date(p.get("date"), i)
        w, h = _size(f"photos/{'gallery/' + p['file']}-t.jpg")
        tag = TAGS.get(p.get("tag") or "") or None
        people = []
        for c in (p.get("who") or []) + ([p["leader"]] if p.get("leader") else []):
            r = who_link(c)
            if r: people.append({"h": href(r[0]), "n": r[1]})
        data.append({"src": f"{up}photos/gallery/{p['file']}.jpg", "cap": cap, "d": dt, "a": ALBUMS[a][0][i], "p": people})
        meta = " · ".join(x for x in (tag[i] if tag else "", dt) if x)
        figs.append(f'<figure class="gfig" data-a="{a}" style="--ac:{ALBUMS[a][2]}"><button type="button" data-n="{n}" aria-label="{e(cap)}">'
                    f'<img src="{up}photos/gallery/{p["file"]}-t.jpg" alt="{e(cap)}" width="{w}" height="{h}" loading="lazy" decoding="async"></button>'
                    f'<figcaption>{e(cap)}{f"<small>{e(meta)}</small>" if meta else ""}</figcaption></figure>')
    nalb = sum(1 for a in ALBUMS if counts[a])
    js = ("<script>(function(){var D=" + _json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + ",L=" + _json.dumps({"t": T["teachers"][i]}, ensure_ascii=False) + ";"
          "var figs=[].slice.call(document.querySelectorAll('.gfig')),chips=[].slice.call(document.querySelectorAll('.galchips .chip')),albs=[].slice.call(document.querySelectorAll('.galb')),cur='';"
          "function setA(a,push){cur=a;figs.forEach(function(f){f.hidden=!!a&&f.dataset.a!==a});chips.forEach(function(c){c.classList.toggle('on',c.dataset.a===a);c.setAttribute('aria-pressed',c.dataset.a===a)});"
          "albs.forEach(function(b){b.classList.toggle('on',b.dataset.a===a);b.setAttribute('aria-pressed',b.dataset.a===a)});if(push!==false)history.replaceState(null,'',a?'#'+a:location.pathname+location.search)}"
          "chips.forEach(function(c){c.onclick=function(){setA(c.dataset.a)}});albs.forEach(function(b){b.onclick=function(){setA(cur===b.dataset.a?'':b.dataset.a);document.getElementById('galgrid').scrollIntoView({behavior:'smooth',block:'start'})}});"
          "var h=location.hash.slice(1);if(h&&albs.some(function(b){return b.dataset.a===h}))setA(h,false);"
          "var d=document.getElementById('gallb');if(!d||!d.showModal)return;var im=d.querySelector('img'),cp=d.querySelector('.glcap'),ct=d.querySelector('.glct'),i=0;"
          "function vis(){return figs.filter(function(f){return !f.hidden}).map(function(f){return +f.querySelector('button').dataset.n})}"
          "function show(n){i=n;var x=D[n],v=vis(),k=v.indexOf(n);im.src=x.src;im.alt=x.cap;cp.innerHTML='';var b=document.createElement('b');b.textContent=x.cap;cp.appendChild(b);"
          "var m=document.createElement('small');m.textContent=[x.a,x.d].filter(Boolean).join(' · ');cp.appendChild(m);"
          "if(x.p.length){var q=document.createElement('span');q.className='glwho';q.append(L.t+' ');x.p.forEach(function(p,j){var a=document.createElement('a');a.href=p.h;a.textContent=p.n;q.appendChild(a);if(j<x.p.length-1)q.append(', ')});cp.appendChild(q)}"
          "ct.textContent=(k+1)+' / '+v.length;[v[k-1],v[k+1]].forEach(function(z){if(z!=null){var p=new Image();p.src=D[z].src}})}"
          "function step(s){var v=vis(),k=v.indexOf(i);show(v[(k+s+v.length)%v.length])}"
          "figs.forEach(function(f){var b=f.querySelector('button');b.onclick=function(){show(+b.dataset.n);d.showModal()}});"
          "d.querySelector('.glp').onclick=function(){step(-1)};d.querySelector('.gln').onclick=function(){step(1)};d.querySelector('.glx').onclick=function(){d.close()};"
          "d.addEventListener('click',function(e){if(e.target===d)d.close()});"
          "d.addEventListener('keydown',function(e){if(e.key==='ArrowLeft')step(-1);else if(e.key==='ArrowRight')step(1)});"
          "var sx=null;d.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});d.addEventListener('touchend',function(e){if(sx==null)return;var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>50)step(dx<0?1:-1);sx=null})"
          "})();</script>")
    lb = (f'<dialog class="gallb" id="gallb" aria-label="{NAME[i]}"><button type="button" class="glx" aria-label="{T["close"][i]}">×</button>'
          f'<button type="button" class="glnav glp" aria-label="{T["prev"][i]}">‹</button><figure><img alt=""><figcaption class="glcap"></figcaption></figure>'
          f'<button type="button" class="glnav gln" aria-label="{T["next"][i]}">›</button><span class="glct"></span></dialog>')
    return (f'<p class="lead2">{T["lead"][i]}</p>'
            f'<div class="galstats"><span><b>{len(ps)}</b> {T["photos"][i]}</span><span><b>{nalb}</b> {T["albums"][i]}</span></div>'
            f'<div class="galbs">{"".join(alb_cards)}</div>'
            f'<div class="chips galchips" id="galgrid" role="group">{chips}</div>'
            f'<div class="galgrid">{"".join(figs)}</div>'
            f'<div class="card galsoon"><span aria-hidden="true">📷</span><div><h3>{T["soon_h"][i]}</h3><p>{T["soon_p"][i]}</p></div></div>'
            + lb + js)

def teaser(lang, up, link):
    """Home-page strip: 6 photos, one per album first."""
    i = _LANGI[lang]; ps = shown()
    if not ps: return ""
    pick = [p for p in ps if _slug(p) in COVER.values()] + [p for p in ps if _slug(p) not in COVER.values()]
    figs = "".join(f'<a class="gtz" href="{link}#{ALBUM_OF[_slug(p)]}"><img src="{up}photos/gallery/{p["file"]}-t.jpg" alt="{_html.escape(p["cap"][i])}" loading="lazy" width="600" height="450"></a>' for p in pick[:6])
    return (f'<section id="gallery" class="band"><div class="wrap"><h2>{NAME[i]}</h2><p>{T["lead"][i]}</p>'
            f'<div class="gtzs">{figs}</div><p><a class="btn p" href="{link}">{T["home_more"][i]} ({len(ps)}) →</a></p></div></section>')
