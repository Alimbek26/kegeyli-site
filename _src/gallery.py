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

# ---- batch of 28.11.2026 (consent / dates to confirm with the school: consent=None means "not confirmed yet")
def _e(file, kaa, en, uz, ru, **kw):
    return dict(section="events", file="events/" + file, cap=(kaa, en, uz, ru), consent=kw.pop("consent", None), **kw)
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
