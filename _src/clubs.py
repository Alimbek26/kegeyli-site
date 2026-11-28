# Clubs and activities (4 languages). To add a club: copy a dict in CLUBS.
# Optional fields are shown only when filled: leader, teacher, when, where, members, done (list), photo, since.
SUB = "clubs/"
L = lambda a, b, c, d: (a, b, c, d)
NAME = L("Mektep klubları", "Clubs and activities", "Maktab to‘garaklari", "Клубы и кружки")
DESC = L("Oqıwshılarımız sabaqtan tıs shuǵıllanatuǵın klublar: «Jas akademikler» hám basqalar.",
         "Clubs where our students go beyond lessons: Young Academicians and more.",
         "O‘quvchilarimiz darsdan tashqari shug‘ullanadigan to‘garaklar: «Yosh akademiklar» va boshqalar.",
         "Клубы, где наши ученики занимаются за рамками уроков: «Юные академики» и другие.")
ICON = ('<path d="M9 3h6"/><path d="M10 3v6L4.500 19a1.500 1.500 0 0 0 1.300 2.200h12.400a1.500 1.500 0 0 0 1.300-2.200L14 9V3"/><path d="M7.500 14h9"/>', "#7c3aed")

T = dict(
 lead=L("Klublarda oqıwshılar sabaqta úyrengenin ámelde qollanadı: joybarlar isleydi, ilimpazlar menen ushırasadı hám jarıslarǵa tayarlanadı.",
        "In our clubs, students put what they learn in class into practice: they work on projects, meet scientists and prepare for competitions.",
        "To‘garaklarda o‘quvchilar darsda o‘rganganini amalda qo‘llaydi: loyihalar ustida ishlaydi, olimlar bilan uchrashadi va musobaqalarga tayyorlanadi.",
        "В клубах ученики применяют знания с уроков на практике: работают над проектами, встречаются с учёными и готовятся к конкурсам."),
 basis=L("Huqıqıy tiykar", "Official basis", "Huquqiy asos", "Правовая основа"),
 what=L("Klubta ne isleydi", "What the club does", "To‘garakda nima qilinadi", "Чем занимается клуб"),
 leader=L("Basshısı", "Led by", "Rahbari", "Руководитель"),
 teacher=L("Mekteptegi juwapker", "Teacher in charge", "Maktabdagi mas’ul", "Ответственный учитель"),
 when=L("Waqtı", "When", "Vaqti", "Когда"),
 where=L("Orın", "Where", "Joyi", "Где"),
 members=L("Aǵzalar", "Members", "A’zolar", "Участники"),
 since=L("Baslanǵan", "Since", "Boshlangan", "С"),
 done=L("Jetiskenlikler", "Highlights", "Yutuqlar", "Достижения"),
 join_h=L("Klubqa qalay qosılıw múmkin?", "How to join", "To‘garakka qanday qo‘shilish mumkin?", "Как вступить"),
 join_p=L("Klass basshıńızǵa yamasa mektep másláhátshisine aytıń — sizge kerekli maǵlıwmattı beredi.",
          "Ask your class teacher or the school counselor, and they will tell you how.",
          "Sinf rahbaringizga yoki maktab maslahatchisiga ayting — sizga kerakli ma’lumotni beradi.",
          "Спросите классного руководителя или школьного консультанта — они подскажут."),
 more=L("Basqa klublar tez arada qosıladı.", "More clubs will be added soon.", "Boshqa to‘garaklar tez orada qo‘shiladi.", "Скоро добавим другие клубы."),
 join_btn=L("Klubqa arza beriw", "Apply to join", "To‘garakka ariza berish", "Подать заявку"),
 more_btn=L("Klub haqqında tolıǵıraq", "More about the club", "To‘garak haqida batafsil", "Подробнее о клубе"),
 about_h=L("Klub haqqında", "About", "To‘garak haqida", "О клубе"),
 log_h=L("Ushırasıwlar", "Meeting log", "Mashg‘ulotlar", "Занятия"),
 proj_h=L("Joybarlar", "Projects", "Loyihalar", "Проекты"),
 mem_h=L("Aǵzalar", "Members", "A’zolar", "Участники"),
 log_empty=L("Ushırasıwlar haqqında maǵlıwmatlar tez arada qosıladı.", "Reports from club meetings will appear here soon.", "Mashg‘ulotlar haqida ma’lumotlar tez orada qo‘shiladi.", "Отчёты о занятиях скоро появятся здесь."),
 proj_empty=L("Oqıwshılar joybarları tez arada qosıladı.", "Student projects will appear here soon.", "O‘quvchilar loyihalari tez orada qo‘shiladi.", "Проекты учеников скоро появятся здесь."),
 mem_empty=L("Aǵzalar dizimi tez arada qosıladı.", "The members list will be added soon.", "A’zolar ro‘yxati tez orada qo‘shiladi.", "Список участников скоро будет добавлен."),
 done_empty=L("Házirshe jetiskenlikler joq — birinshi nátiyjeler aldıda.", "No results yet: the first ones are ahead.", "Hozircha yutuqlar yo‘q — birinchi natijalar oldinda.", "Пока достижений нет — первые результаты впереди."),
 join_cta=L("Arzanı toltırıń hám Telegram yamasa pochta arqalı jiberiń.", "Fill in a short application and send it by Telegram or email.", "Qisqa arizani to‘ldiring va Telegram yoki pochta orqali yuboring.", "Заполните короткую заявку и отправьте в Telegram или по почте."),
 all=L("Barlıq klublar", "All clubs", "Barcha to‘garaklar", "Все клубы"),
 club_lead=L("{c} basshısı", "Leads the {c}", "{c} rahbari", "Руководитель: {c}"),
 clubs_h=L("Klublar", "Clubs", "To‘garaklar", "Клубы"),
 why_h=L("Nege qosılıw kerek", "Why join", "Nega qo‘shilish kerak", "Зачем вступать"),
 faq_h=L("Kóp beriletuǵın sorawlar", "Questions and answers", "Ko‘p beriladigan savollar", "Вопросы и ответы"),
 next=L("Keyingi ushırasıw", "Next meeting", "Keyingi mashg‘ulot", "Следующее занятие"),
 today=L("búgin", "today", "bugun", "сегодня"), tomorrow=L("erteń", "tomorrow", "ertaga", "завтра"),
 indays=L("{n} kúnnen keyin", "in {n} days", "{n} kundan keyin", "через {n} дн."),
 groups_h=L("Pánler boyınsha toparlar", "Subject groups", "Fanlar bo‘yicha guruhlar", "Группы по предметам"),
 tbc=L("Muǵallim hám waqıt tez arada kórsetiledi", "Teacher and schedule coming soon", "O‘qituvchi va vaqt tez orada ko‘rsatiladi", "Учитель и расписание скоро"),
 steps_h=L("Qalay qabıl etiledi", "How students are selected", "Qanday qabul qilinadi", "Как проходит отбор"),
 stages_h=L("Olimpiada basqıshları", "Olympiad stages", "Olimpiada bosqichlari", "Этапы олимпиад"),
 decree=L("PF-55 Pármanın oqıw", "Read Decree PF-55", "PF-55 Farmonini o‘qish", "Читать Указ УП-55"),
)

CLUBS = [
 dict(key="young-academicians", colour="#7c3aed",
      icon='<path d="M22 10L12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/><path d="M22 10v6"/>',
      name=L("«Jas akademikler» klubı", "Young Academicians club", "«Yosh akademiklar» to‘garagi", "Клуб «Юные академики»"),
      tag=L("Pánler akademiyası menen birge", "With the Academy of Sciences", "Fanlar akademiyasi bilan birga", "Вместе с Академией наук"),
      intro=L("Ózbekstan Respublikası Pánler akademiyasınıń akademikleri menen birge isleytuǵın klub. Ol qánigelestirilgen mektep oqıwshılarınıń ilimge qızıǵıwshılıǵın hám dóretiwshilik qábiletin rawajlandırıw ushın dúzilgen.",
              "A club run together with academicians of the Academy of Sciences of Uzbekistan. It was created to develop specialized-school students’ interest in science and their creative thinking.",
              "O‘zbekiston Respublikasi Fanlar akademiyasi akademiklari bilan birga ishlaydigan to‘garak. U ixtisoslashtirilgan maktab o‘quvchilarining ilmga qiziqishi va ijodiy qobiliyatini rivojlantirish uchun tashkil etilgan.",
              "Клуб, работающий вместе с академиками Академии наук Узбекистана. Создан, чтобы развивать у учеников специализированных школ интерес к науке и творческое мышление."),
      what=[L("Akademikler menen dóretiwshilik sabaqları", "Creativity lessons with academicians", "Akademiklar bilan ijodkorlik darslari", "Уроки творчества с академиками"),
            L("Ámeliy ilimiy joybarlar", "Hands-on science projects", "Amaliy ilmiy loyihalar", "Практические научные проекты"),
            L("Ilimiy laboratoriyalarǵa sayaxatlar", "Visits to research laboratories", "Ilmiy laboratoriyalarga tashriflar", "Посещение научных лабораторий"),
            L("Ilimiy jarıslarǵa tayarlıq", "Preparation for science competitions", "Ilmiy tanlovlarga tayyorgarlik", "Подготовка к научным конкурсам")],
      basis=L("Prezident Pármanı PF-55, 2024-jıl 1-aprel", "Presidential Decree PF-55, 1 April 2024", "Prezident Farmoni PF-55, 2024-yil 1-aprel", "Указ Президента УП-55 от 1 апреля 2024 г."),
      law="documents/pf-55/",
      leader=("Toti Elmuratova", "elmuratova-toti",
              L("biologiya muǵallimi", "Biology teacher", "biologiya o‘qituvchisi", "учитель биологии")),
      teacher=None,
      when=L("Eki háptede bir ret, siyshembi kúni, 15:00", "Every other Tuesday, 15:00", "Ikki haftada bir marta, seshanba kuni, 15:00", "Раз в две недели, по вторникам, 15:00"),
      where=L("Akademik kelgende — konferenc-zal; basqa waqıtta — bos klass yamasa laboratoriya", "Conference room when an academician visits; otherwise a free classroom or laboratory",
              "Akademik kelganda — konferens-zal; boshqa paytda — bo‘sh sinf yoki laboratoriya", "Конференц-зал, когда приходит академик; в остальное время — свободный класс или лаборатория"),
      anchor="2026-12-01",   # date of one real meeting "YYYY-MM-DD" (a Tuesday); turns on the next-meeting countdown
      every=14, mtime="15:00",  # cycle in days; start time e.g. "15:00"
      why=[("lab", L("Haqıyqıy ilimpazlar menen islew", "Work with real scientists", "Haqiqiy olimlar bilan ishlash", "Работа с настоящими учёными"),
             L("Pánler akademiyasınıń akademikleri menen ushırasıw hám olardan tikkeley úyreniw.", "Meet academicians of the Academy of Sciences and learn from them directly.", "Fanlar akademiyasi akademiklari bilan uchrashish va ulardan bevosita o‘rganish.", "Встречи с академиками Академии наук и обучение у них напрямую.")),
           ("bulb", L("Óz joybarıń", "Your own project", "O‘z loyihang", "Свой проект"),
             L("Ideyadan nátiyjege shekem ilimiy joybar islew — bul bilimińdi ámelde kórsetedi.", "Take a science project from idea to result, and put what you learn into practice.", "G‘oyadan natijagacha ilmiy loyiha qilish — bu bilimingni amalda ko‘rsatadi.", "Довести научный проект от идеи до результата и применить знания на практике.")),
           ("cap", L("Universitetke arza ushın", "Stronger university applications", "Universitetga ariza uchun", "Сильнее заявка в университет"),
             L("Ilimiy iskerlik hám joybarlar shet el hám Ózbekstan universitetleri ushın arzanıń kúshli tárepi boladı.", "Research activity and projects are a strong point in applications to universities abroad and in Uzbekistan.", "Ilmiy faoliyat va loyihalar xorijiy va O‘zbekiston universitetlariga arizada kuchli tomon bo‘ladi.", "Научная деятельность и проекты — сильная сторона заявки в зарубежные и узбекские университеты.")),
           ("trophy", L("Jarıslarǵa tayarlıq", "Ready for competitions", "Musobaqalarga tayyorgarlik", "Подготовка к конкурсам"),
             L("«Ixtirochilikka qadam» hám basqa ilimiy tańlawlarǵa joybar menen qatnasıw.", "Enter “Ixtirochilikka qadam” and other science contests with your project.", "«Ixtirochilikka qadam» va boshqa ilmiy tanlovlarda loyiha bilan qatnashish.", "Участие с проектом в конкурсе «Ixtirochilikka qadam» и других научных конкурсах."))],
      faq=[(L("Kim qosıla aladı?", "Who can join?", "Kim qo‘shilishi mumkin?", "Кто может вступить?"),
            L("5-klasstan 11-klassqa shekemgi barlıq oqıwshılar.", "Students of any grade, from 5 to 11.", "5-sinfdan 11-sinfgacha barcha o‘quvchilar.", "Ученики любого класса, с 5 по 11.")),
           (L("Tólem bar ma?", "Does it cost anything?", "To‘lov bormi?", "Это платно?"),
            L("Yaq, klub tolıq biypul.", "No, the club is completely free.", "Yo‘q, to‘garak butunlay bepul.", "Нет, клуб полностью бесплатный.")),
           (L("Qashan ótkeriledi?", "When does it meet?", "Qachon o‘tkaziladi?", "Когда проходят занятия?"),
            L("Eki háptede bir ret, siyshembi kúni saat 15:00 de.", "Every other Tuesday at 15:00.", "Ikki haftada bir marta, seshanba kuni soat 15:00 da.", "Раз в две недели, по вторникам в 15:00.")),
           (L("Qay jerde?", "Where?", "Qayerda?", "Где?"),
            L("Akademik kelgende — konferenc-zalda; basqa waqıtlarda — bos klassta yamasa laboratoriyada.", "In the conference room when an academician visits; otherwise in a free classroom or laboratory.", "Akademik kelganda — konferens-zalda; boshqa paytda — bo‘sh sinfda yoki laboratoriyada.", "В конференц-зале, когда приходит академик; в остальное время — в свободном классе или лаборатории.")),
           (L("Ózim menen ne alıp keliwim kerek?", "What should I bring?", "O‘zim bilan nima olib kelishim kerak?", "Что взять с собой?"),
            L("Dápter. Noutbuk bolsa, alıp keliw usınıladı.", "A notebook. A laptop is recommended if you have one.", "Daftar. Noutbuk bo‘lsa, olib kelish tavsiya etiladi.", "Тетрадь. Если есть ноутбук, его рекомендуется взять.")),
           (L("Qalay qosılaman?", "How do I join?", "Qanday qo‘shilaman?", "Как вступить?"),
            L("Usı saytta qısqa arzanı toltırıp, Telegram yamasa pochta arqalı jiberiń.", "Fill in the short application on this website and send it by Telegram or email.", "Ushbu saytda qisqa arizani to‘ldirib, Telegram yoki pochta orqali yuboring.", "Заполните короткую заявку на этом сайте и отправьте в Telegram или по почте."), "join")],
      since=L("2024-jıl 1-aprel", "1 April 2024", "2024-yil 1-aprel", "1 апреля 2024 г."),
      done=[], photo=None, join=True, log=[], projects=[], members=[]),
]

CLUBS.append(dict(key="olympiad-groups", colour="#d97706",
      icon='<circle cx="12" cy="15" r="6"/><path d="M8.500 10.200L5 3h4l3 6 3-6h4l-3.500 7.200"/>',
      name=L("Olimpiada toparları", "Olympiad groups", "Olimpiada guruhlari", "Олимпиадные группы"),
      tag=L("Matematika · Fizika · Ximiya · Biologiya · Informatika", "Maths · Physics · Chemistry · Biology · Computer science", "Matematika · Fizika · Kimyo · Biologiya · Informatika", "Математика · Физика · Химия · Биология · Информатика"),
      intro=L("Pánler boyınsha olimpiadalarǵa tereń tayarlıq: mektep basqıshınan baslap respublikalıq hám xalıqaralıq olimpiadalarǵa shekem.",
              "In-depth preparation for subject olympiads, from the school stage up to national and international olympiads.",
              "Fanlar bo‘yicha olimpiadalarga chuqur tayyorgarlik: maktab bosqichidan boshlab respublika va xalqaro olimpiadalargacha.",
              "Углублённая подготовка к предметным олимпиадам: от школьного этапа до республиканских и международных олимпиад."),
      what=[L("Programmadan tıs qıyın máseleler", "Hard problems beyond the curriculum", "Dasturdan tashqari murakkab masalalar", "Сложные задачи сверх программы"),
            L("Ótken jıllardıń olimpiada tapsırmaları", "Past olympiad papers", "O‘tgan yillar olimpiada topshiriqlari", "Задания олимпиад прошлых лет"),
            L("Waqıtqa qarap sınaq olimpiadalar", "Timed practice olympiads", "Vaqtli sinov olimpiadalari", "Пробные олимпиады на время"),
            L("Hár bir basqıshqa jeke tayarlıq", "Individual preparation for each stage", "Har bir bosqichga individual tayyorgarlik", "Индивидуальная подготовка к каждому этапу")],
      groups=[("math", "#2563eb", L("Matematika", "Maths", "Matematika", "Математика")),
              ("phys", "#0b7a8f", L("Fizika", "Physics", "Fizika", "Физика")),
              ("chem", "#047857", L("Ximiya", "Chemistry", "Kimyo", "Химия")),
              ("bio", "#2f8f5b", L("Biologiya", "Biology", "Biologiya", "Биология")),
              ("it", "#7c3aed", L("Informatika", "Computer science", "Informatika", "Информатика"))],
      group_info={},   # e.g. "math": dict(teacher=("Name", "slug"), when=L(...), where=L(...))
      steps=[L("Arza beriw", "Apply", "Ariza berish", "Подача заявки"),
             L("Tańlaw (sınaq yamasa mektep olimpiadası nátiyjesi)", "Selection (test or school olympiad result)", "Saralash (sinov yoki maktab olimpiadasi natijasi)", "Отбор (тест или результат школьной олимпиады)"),
             L("Toparda tayarlıq", "Training in the group", "Guruhda tayyorgarlik", "Подготовка в группе")],
      stages=["school", "district", "region", "republic", "intl"],
      leader=None, teacher=None, when=None, where=None, since=None,
      done=[], photo=None, join=True, log=[], projects=[], members=[],
      faq=[(L("Kim qosıla aladı?", "Who can join?", "Kim qo‘shilishi mumkin?", "Кто может вступить?"),
            L("Qálegen oqıwshı arza bere aladı. Keyin tańlaw ótkeriledi hám eń tayar oqıwshılar toparlarǵa alınadı.", "Any student can apply. A selection follows, and the best-prepared students join the groups.", "Istalgan o‘quvchi ariza berishi mumkin. So‘ng saralash o‘tkaziladi va eng tayyor o‘quvchilar guruhlarga olinadi.", "Подать заявку может любой ученик. Затем проходит отбор, и лучше подготовленные ученики попадают в группы.")),
           (L("Bir neshe pánge arza beriwge bola ma?", "Can I apply for more than one subject?", "Bir nechta fanga ariza berish mumkinmi?", "Можно подать заявку на несколько предметов?"),
            L("Awa, arzada qızıǵatuǵın barlıq pánlerdi belgileń.", "Yes: tick every subject you are interested in on the application.", "Ha, arizada qiziqqan barcha fanlarni belgilang.", "Да, отметьте в заявке все интересующие предметы.")),
           (L("Qaysı olimpiadalarǵa tayarlanadı?", "Which olympiads do the groups prepare for?", "Qaysi olimpiadalarga tayyorlanadi?", "К каким олимпиадам готовят?"),
            L("Mektep, rayon, Qaraqalpaqstan hám respublika basqıshlarına, sonday-aq múmkinshilik bolǵanda xalıqaralıq olimpiadalarǵa.", "The school, district, Karakalpakstan and national stages, and international olympiads whenever possible.", "Maktab, tuman, Qoraqalpog‘iston va respublika bosqichlariga, shuningdek imkon bo‘lganda xalqaro olimpiadalarga.", "К школьному, районному, каракалпакстанскому и республиканскому этапам, а при возможности — к международным олимпиадам.")),
           (L("Qalay qosılaman?", "How do I join?", "Qanday qo‘shilaman?", "Как вступить?"),
            L("Usı saytta arzanı toltırıp, pánlerdi belgileń hám Telegram yamasa pochta arqalı jiberiń.", "Fill in the application on this website, tick your subjects and send it by Telegram or email.", "Ushbu saytda arizani to‘ldirib, fanlarni belgilang va Telegram yoki pochta orqali yuboring.", "Заполните заявку на сайте, отметьте предметы и отправьте в Telegram или по почте."), "join")]))


WHY_I = {"lab": '<path d="M9 3h6"/><path d="M10 3v6L4.500 19a1.500 1.500 0 0 0 1.300 2.200h12.400a1.500 1.500 0 0 0 1.300-2.200L14 9V3"/><path d="M7.500 14h9"/>',
         "bulb": '<path d="M9 18h6M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.700V17h8v-2.300A7 7 0 0 0 12 2z"/>',
         "cap": '<path d="M22 10L12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/>',
         "trophy": '<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>'}
CAL_I = '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18"/>'
TBC = "<span class=\"clgw\">{}</span>"
DOC_I = '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>'


def _svg(p, s=22):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'


def _parts(c, i, up, href):
    facts = [(T[k][i], c[k][i] if isinstance(c[k], tuple) else c[k]) for k in ("teacher", "when", "where", "since") if c.get(k)]
    if c.get("members"):
        facts.append((T["members"][i], str(len(c["members"]))))
    fx = ("<dl class=\"clfacts\">" + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in facts) + "</dl>") if facts else ""
    lead = ""
    if c.get("leader"):
        nm, sl, rl = c["leader"]
        lead = (f'<a class="cllead" href="{href("teachers/" + sl + "/")}"><img src="{up}photos/teachers/{sl}-s.jpg" alt="" width="56" height="56" loading="lazy">'
                f'<span><small>{T["leader"][i]}</small><b>{nm}</b><em>{rl[i]}</em></span><i aria-hidden="true">→</i></a>')
    law = (f'<a class="cllaw" href="{href(c["law"])}"><span class="clli">{_svg(DOC_I, 20)}</span>'
           f'<span><small>{T["basis"][i]}</small><b>{c["basis"][i]}</b></span><em>{T["decree"][i]} →</em></a>') if c.get("law") else ""
    head = (f'<div class="clhead"><span class="clic">{_svg(c["icon"], 34)}</span><div><span class="cltag">{c["tag"][i]}</span>'
            f'<h2>{c["name"][i]}</h2></div></div>')
    join = f'<a class="btn p" href="{href(JSUB)}?club={c["key"]}">{T["join_btn"][i]} →</a>' if c.get("join") else ""
    return fx, lead, law, head, join


def csub(c):
    return f"clubs/{c['key']}/"


def _card(c, i, up, href):
    """Summary card on the Clubs page; the title and button open the club's own page."""
    fx, lead, law, head, join = _parts(c, i, up, href)
    head = head.replace(f'<h2>{c["name"][i]}</h2>', f'<h2><a class="clh" href="{href(csub(c))}">{c["name"][i]}</a></h2>')
    return (f'<article class="clcard" id="{c["key"]}" style="--c:{c["colour"]}">{head}'
            f'<p class="clintro">{c["intro"][i]}</p>{lead}{fx}'
            f'<p class="btns clbtns"><a class="btn s clmore" href="{href(csub(c))}">{T["more_btn"][i]} →</a>{join}</p></article>')


def body(i, up, href):
    cards = "".join(_card(c, i, up, href) for c in CLUBS)
    return (f'<p class="lead2">{T["lead"][i]}</p><div class="clubs">{cards}</div>'
            f'<div class="card cljoin"><h3>{T["join_h"][i]}</h3><p>{T["join_p"][i]}</p>'
            f'<p class="btns"><a class="btn p" href="{href(JSUB)}">{T["join_btn"][i]} →</a><a class="btn s" href="{href("counseling/")}">{__import__("counseling").NAME[i]} →</a></p></div>'
            f'<p class="note">{T["more"][i]}</p>')


# ---------- One page per club: clubs/<key>/
# Content lists, each shown only when it has entries (an "empty" note otherwise):
#   log:      [dict(date="2026-11-25", topic=L(...), text=L(...) or None, photo="file.jpg" or None)]   (photos in photos/clubs/)
#   projects: [dict(title=L(...), who="names" or None, text=L(...), photo=None)]
#   members:  [("Name Surname", "9-B")]   only students who agreed to be shown
CSUBS = {csub(c): n for n, c in enumerate(CLUBS)}


def cname(sub, i):
    return CLUBS[CSUBS[sub]]["name"][i]


def cdesc(sub):
    return CLUBS[CSUBS[sub]]["intro"]


def _date(d, i):
    y, m, dd = (d.split("-") + ["", ""])[:3]
    M = [("yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentyabr", "oktyabr", "noyabr", "dekabr"),
         ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"),
         ("yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentabr", "oktabr", "noyabr", "dekabr"),
         ("января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря")]
    if not dd:
        return y
    return f"{int(dd)} {M[i][int(m) - 1]} {y}" if i != 1 else f"{int(dd)} {M[1][int(m) - 1]} {y}"


def club_body(sub, i, up, href):
    c = CLUBS[CSUBS[sub]]
    fx, lead, law, head, join = _parts(c, i, up, href)
    what = "".join(f'<li><span>{n + 1}</span>{w[i]}</li>' for n, w in enumerate(c["what"]))
    log = sorted(c.get("log", []), key=lambda e: e["date"], reverse=True)
    logh = ("<ol class=\"cllog\">" + "".join(
        f'<li><time>{_date(e["date"], i)}</time><div class="card"><h3>{e["topic"][i]}</h3>'
        + (f'<p>{e["text"][i]}</p>' if e.get("text") else "")
        + (f'<img src="{up}photos/clubs/{e["photo"]}" alt="{e["topic"][i]}" loading="lazy">' if e.get("photo") else "")
        + "</div></li>" for e in log) + "</ol>") if log else f'<p class="clempty">{T["log_empty"][i]}</p>'
    pr = c.get("projects", [])
    prh = ("<div class=\"clprs\">" + "".join(
        f'<div class="card clpr">' + (f'<img src="{up}photos/clubs/{p["photo"]}" alt="" loading="lazy">' if p.get("photo") else "")
        + f'<h3>{p["title"][i]}</h3>' + (f'<p class="clwho">{p["who"]}</p>' if p.get("who") else "") + f'<p>{p["text"][i]}</p></div>' for p in pr) + "</div>") \
        if pr else f'<p class="clempty">{T["proj_empty"][i]}</p>'
    mem = c.get("members", [])
    memh = ("<ul class=\"clmem\">" + "".join(f"<li><b>{n}</b><span>{k}</span></li>" for n, k in mem) + "</ul>") if mem else f'<p class="clempty">{T["mem_empty"][i]}</p>'
    done = ("<ul class=\"cldone\">" + "".join(f"<li>{d[i]}</li>" for d in c["done"]) + "</ul>") if c.get("done") else f'<p class="clempty">{T["done_empty"][i]}</p>'
    ph = f'<img class="clph" src="{up}photos/clubs/{c["photo"]}" alt="{c["name"][i]}">' if c.get("photo") else ""
    why = "".join(f'<div class="clwhy"><span class="clic">{_svg(WHY_I[k], 24)}</span><h3>{t[i]}</h3><p>{d[i]}</p></div>' for k, t, d in c.get("why", []))
    whyh = f'<section class="clsec" id="why" style="--c:{c["colour"]}"><h2>{T["why_h"][i]}</h2><div class="clwhys">{why}</div></section>' if why else ""
    faq = "".join(f'<details class="clfaq"><summary>{q[0][i]}</summary><p>{q[1][i]}' + (f' <a href="{href(JSUB)}?club={c["key"]}">{T["join_btn"][i]} →</a>' if len(q) > 2 else "") + '</p></details>' for q in c.get("faq", []))
    faqh = f'<section class="clsec" id="faq" style="--c:{c["colour"]}"><h2>{T["faq_h"][i]}</h2><div class="clfaqs">{faq}</div></section>' if faq else ""
    nxt = ""
    if c.get("anchor"):
        import json as _j
        nd = _j.dumps({"a": c["anchor"], "e": c.get("every", 14), "t": c.get("mtime") or "", "l": i, "lab": {k: T[k][i] for k in ("today", "tomorrow", "indays")}}, ensure_ascii=False)
        nxt = (f'<div class="clnext" id="clnext" hidden><span class="clic">{_svg(CAL_I, 24)}</span><div><small>{T["next"][i]}</small><b id="clnd"></b><em id="clnin"></em></div></div>'
               f'<script>var CN={nd};' + NEXT_JS + '</script>')
    import achieve as _A
    grp = ""
    if c.get("groups"):
        gi = c.get("group_info", {})
        cells = ""
        for k, col, nm in c["groups"]:
            info = gi.get(k, {})
            det = ""
            if info.get("teacher"):
                tn, ts = info["teacher"]
                det += f'<a class="clgt" href="{href("teachers/" + ts + "/")}"><img src="{up}photos/teachers/{ts}-s.jpg" alt="" width="36" height="36" loading="lazy">{tn}</a>'
            if info.get("when"):
                det += f'<span class="clgw">{info["when"][i]}</span>'
            if info.get("where"):
                det += f'<span class="clgw">{info["where"][i]}</span>'
            cells += f'<div class="clg" style="--g:{col}"><h3>{nm[i]}</h3>{det or TBC.format(T["tbc"][i])}</div>'
        grp = f'<section class="clsec" id="groups" style="--c:{c["colour"]}"><h2>{T["groups_h"][i]}</h2><div class="clgs">{cells}</div></section>'
    if c.get("steps"):
        grp += (f'<section class="clsec" id="steps" style="--c:{c["colour"]}"><h2>{T["steps_h"][i]}</h2><ol class="clsteps">'
                + "".join(f'<li><b>{n + 1}</b><span>{x[i]}</span></li>' for n, x in enumerate(c["steps"])) + '</ol></section>')
    if c.get("stages"):
        grp += (f'<section class="clsec" id="stages" style="--c:{c["colour"]}"><h2>{T["stages_h"][i]}</h2><ol class="clstages">'
                + "".join(f'<li style="--n:{n}"><span>{n + 1}</span>{_A.STAGE[k][i]}</li>' for n, k in enumerate(c["stages"])) + '</ol></section>')
    nav = "".join(f'<a href="#{k}">{T[h][i]}</a>' for k, h in (("about", "about_h"), ("groups", "groups_h"), ("why", "why_h"), ("log", "log_h"), ("projects", "proj_h"), ("members", "mem_h"), ("faq", "faq_h")) if (k != "why" or whyh) and (k != "faq" or faqh) and (k != "groups" or c.get("groups")))
    return (f'<article class="clcard clpage" style="--c:{c["colour"]}">{head}{ph}<p class="clintro">{c["intro"][i]}</p>{lead}{fx}'
            f'{nxt}<p class="btns clbtns">{join}</p></article>'
            f'<nav class="clnav" style="--c:{c["colour"]}">{nav}</nav>'
            f'<section class="clsec" id="about" style="--c:{c["colour"]}"><h2>{T["what"][i]}</h2><ul class="clwhat">{what}</ul>{law}</section>'
            f'{grp}{whyh}<section class="clsec" id="log" style="--c:{c["colour"]}"><h2>{T["log_h"][i]}</h2>{logh}</section>'
            f'<section class="clsec" id="projects" style="--c:{c["colour"]}"><h2>{T["proj_h"][i]}</h2>{prh}</section>'
            f'<section class="clsec" id="members" style="--c:{c["colour"]}"><h2>{T["mem_h"][i]}</h2>{memh}</section>'
            f'<section class="clsec" id="results" style="--c:{c["colour"]}"><h2>{T["done"][i]}</h2>{done}</section>{faqh}'
            + (f'<div class="cscta clcta"><div><h2>{T["join_h"][i]}</h2><p>{T["join_cta"][i]}</p></div><p class="btns">{join}</p></div>' if join else "")
            + f'<p class="btns"><a class="btn s" href="{href(SUB)}">← {T["all"][i]}</a></p>')


# ---------- Join page: the student fills in a short application in the browser, then sends it
# themselves by Telegram or email. Nothing is sent to or stored by the website.
JSUB = "clubs/join/"
JNAME = L("Klubqa arza beriw", "Apply to join a club", "To‘garakka ariza berish", "Заявка в клуб")
JDESC = L("«Jas akademikler» hám basqa mektep klublarına arza beriw.", "Apply to join the Young Academicians club or another school club.",
          "«Yosh akademiklar» va boshqa maktab to‘garaklariga ariza berish.", "Заявка в клуб «Юные академики» и другие школьные клубы.")
J = dict(
 lead=L("Arzanı toltırıń, keyin onı Telegram yamasa elektron pochta arqalı jiberiń. Klub basshısı yamasa mektep másláhátshisi siz benen baylanısadı.",
        "Fill in the application, then send it by Telegram or email. The club leader or the school counselor will get back to you.",
        "Arizani to‘ldiring, so‘ng uni Telegram yoki elektron pochta orqali yuboring. To‘garak rahbari yoki maktab maslahatchisi siz bilan bog‘lanadi.",
        "Заполните заявку и отправьте её через Telegram или по почте. Руководитель клуба или школьный консультант свяжется с вами."),
 s1=L("Toltırıń", "Fill in", "To‘ldiring", "Заполните"), s2=L("Jiberiń", "Send", "Yuboring", "Отправьте"), s3=L("Juwap kútiń", "Get a reply", "Javob kuting", "Ждите ответа"),
 club=L("Klub", "Club", "To‘garak", "Клуб"),
 name=L("Atıńız hám familiyańız", "Your full name", "Ism va familiyangiz", "Ваши имя и фамилия"),
 cls=L("Klassıńız", "Your class", "Sinfingiz", "Ваш класс"),
 pick=L("Tańlań", "Choose", "Tanlang", "Выберите"),
 int=L("Qaysı pánler qızıqtıradı?", "Which subjects interest you?", "Qaysi fanlar qiziqtiradi?", "Какие предметы вам интересны?"),
 why=L("Nege qosılǵıńız keledi? (májbúriy emes)", "Why do you want to join? (optional)", "Nega qo‘shilmoqchisiz? (ixtiyoriy)", "Почему хотите вступить? (необязательно)"),
 why_ph=L("Mısalı: óz joybarımdı islegim keledi…", "For example: I want to work on my own project…", "Masalan: o‘z loyihamni qilmoqchiman…", "Например: хочу сделать свой проект…"),
 parent=L("Ata-anam bul arza haqqında biledi", "My parent or guardian knows I am applying", "Ota-onam bu ariza haqida biladi", "Мои родители знают об этой заявке"),
 preview=L("Siziń arzańız", "Your application", "Sizning arizangiz", "Ваша заявка"),
 tg=L("Telegram arqalı jiberiw", "Send by Telegram", "Telegram orqali yuborish", "Отправить в Telegram"),
 mail=L("Pochta arqalı jiberiw", "Send by email", "Pochta orqali yuborish", "Отправить по почте"),
 copied=L("Arza tekstı kóshirildi. Telegramda «Qoyıw» (Paste) basıń hám jiberiń.", "Application text copied. In Telegram, tap Paste and send.", "Ariza matni nusxalandi. Telegramda «Qo‘yish» (Paste) ni bosing va yuboring.", "Текст заявки скопирован. В Telegram нажмите «Вставить» и отправьте."),
 need=L("Atıńızdı, klassıńızdı kiritiń hám ata-ana belgisin qoyıń.", "Please enter your name and class, and tick the parent box.", "Ismingiz, sinfingizni kiriting va ota-ona belgisini qo‘ying.", "Укажите имя, класс и отметьте согласие родителей."),
 hello=L("Assalawma áleykum! Klubqa qosılǵım keledi.", "Hello! I would like to join a club.", "Assalomu alaykum! To‘garakka qo‘shilmoqchiman.", "Здравствуйте! Хочу вступить в клуб."),
 privacy=L("Sayt bul maǵlıwmatlardı saqlamaydı: arza tek siz jibergen waqıtta bizge keledi.", "The website does not store this information: the application reaches us only when you send it.", "Sayt bu ma’lumotlarni saqlamaydi: ariza faqat siz yuborganingizda bizga keladi.", "Сайт не сохраняет эти данные: заявка попадёт к нам, только когда вы её отправите."),
 back=L("Barlıq klublar", "All clubs", "Barcha to‘garaklar", "Все клубы"),
)
MSG = dict(club=L("Klub", "Club", "To‘garak", "Клуб"), name=L("Atı-familiyası", "Name", "Ism-familiya", "Имя и фамилия"), cls=L("Klassı", "Class", "Sinf", "Класс"),
           int=L("Qızıǵıwshılıǵı:", "Interests:", "Qiziqishlari:", "Интересы:"), why=L("Sebebi", "Reason", "Sababi", "Причина"))
SUBJ = [L("Matematika", "Maths", "Matematika", "Математика"), L("Fizika", "Physics", "Fizika", "Физика"), L("Ximiya", "Chemistry", "Kimyo", "Химия"),
        L("Biologiya", "Biology", "Biologiya", "Биология"), L("Informatika", "Computer science", "Informatika", "Информатика"), L("Geografiya", "Geography", "Geografiya", "География"),
        L("Ekologiya", "Ecology", "Ekologiya", "Экология")]


def join_body(i, up, href, classes, ctx):
    import json as _j
    clubs = [c for c in CLUBS if c.get("join")]
    opts = "".join(f'<option value="{c["key"]}">{c["name"][i]}</option>' for c in clubs)
    copts = "".join(f'<option>{c}</option>' for c in classes)
    chips = "".join(f'<label class="jchip"><input type="checkbox" name="s" value="{s_[i]}"><span>{s_[i]}</span></label>' for s_ in SUBJ)
    steps = "".join(f'<li><b>{n + 1}</b>{s_[i]}</li>' for n, s_ in enumerate((J["s1"], J["s2"], J["s3"])))
    data = _j.dumps({"lab": {k: v[i] for k, v in MSG.items()},
                     "hello": J["hello"][i], "need": J["need"][i], "copied": J["copied"][i], "mail": ctx["EMAIL"], "tg": ctx["TG"], "subj": JNAME[i]}, ensure_ascii=False)
    return (f'<p class="lead2">{J["lead"][i]}</p><ol class="jsteps">{steps}</ol>'
            f'<div class="jgrid"><form class="card jform" id="jf" onsubmit="return false">'
            f'<label class="jl">{J["club"][i]}<select id="jclub">{opts}</select></label>'
            f'<label class="jl">{J["name"][i]}<input id="jname" autocomplete="name" maxlength="80"></label>'
            f'<label class="jl">{J["cls"][i]}<select id="jcls"><option value="">{J["pick"][i]}</option>{copts}</select></label>'
            f'<fieldset class="jl"><legend>{J["int"][i]}</legend><div class="jchips">{chips}</div></fieldset>'
            f'<label class="jl">{J["why"][i]}<textarea id="jwhy" rows="3" maxlength="400" placeholder="{J["why_ph"][i]}"></textarea></label>'
            f'<label class="jchk"><input type="checkbox" id="jpar"><span>{J["parent"][i]}</span></label></form>'
            f'<div class="card jprev"><h3>{J["preview"][i]}</h3><pre id="jtext"></pre><p class="jerr" id="jerr" hidden>{J["need"][i]}</p>'
            f'<div class="jbtns"><a class="btn p" id="jtg" href="{ctx["TG"]}" rel="noopener">{J["tg"][i]}</a><a class="btn s" id="jmail" href="mailto:{ctx["EMAIL"]}">{J["mail"][i]}</a></div>'
            f'<p class="jok" id="jok" hidden>{J["copied"][i]}</p><p class="note">{J["privacy"][i]}</p></div></div>'
            f'<p class="btns"><a class="btn s" href="{href(SUB)}">← {J["back"][i]}</a></p>'
            f'<script>var JD={data};' + JOIN_JS + '</script>')


JOIN_JS = r"""(function(){var $=function(i){return document.getElementById(i)},D=JD;
var q=new URLSearchParams(location.search).get('club');if(q&&$('jclub').querySelector('option[value="'+q+'"]'))$('jclub').value=q;
function text(){var s=[].map.call(document.querySelectorAll('.jchip input:checked'),function(x){return x.value}).join(', ');
var c=$('jclub');var t=D.hello+'\n\n'+D.lab.club+': '+c.options[c.selectedIndex].text+'\n'+D.lab.name+': '+($('jname').value.trim()||'—')+'\n'+D.lab.cls+': '+($('jcls').value||'—');
if(s)t+='\n'+D.lab.int+' '+s;var w=$('jwhy').value.trim();if(w)t+='\n'+D.lab.why+': '+w;return t}
function ok(){return $('jname').value.trim().length>1&&$('jcls').value&&$('jpar').checked}
function upd(){var t=text();$('jtext').textContent=t;$('jmail').href='mailto:'+D.mail+'?subject='+encodeURIComponent(D.subj)+'&body='+encodeURIComponent(t);
document.querySelector('.jbtns').classList.toggle('off',!ok());if(ok())$('jerr').hidden=true}
$('jf').addEventListener('input',upd);$('jf').addEventListener('change',upd);upd();
function guard(e){if(!ok()){e.preventDefault();$('jerr').hidden=false;return false}return true}
$('jmail').addEventListener('click',guard);
$('jtg').addEventListener('click',function(e){if(!guard(e))return;var t=text();try{navigator.clipboard.writeText(t).then(function(){$('jok').hidden=false})}catch(x){}});
})();"""


NEXT_JS = r"""(function(){var D=CN,M=[["yanvar","fevral","mart","aprel","may","iyun","iyul","avgust","sentyabr","oktyabr","noyabr","dekabr"],["January","February","March","April","May","June","July","August","September","October","November","December"],["yanvar","fevral","mart","aprel","may","iyun","iyul","avgust","sentabr","oktabr","noyabr","dekabr"],["января","февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря"]],
W=[["Siyshembi"],["Tuesday"],["Seshanba"],["Вторник"]];
var p=D.a.split('-'),a=new Date(+p[0],p[1]-1,+p[2]),n=new Date();n.setHours(0,0,0,0);
var d=Math.round((n-a)/864e5),k=d<=0?0:Math.ceil(d/D.e),x=new Date(a.getTime()+k*D.e*864e5);x.setHours(0,0,0,0);
var g=Math.round((x-n)/864e5),L=D.l,s=(L==1?W[1][0]+', '+x.getDate()+' '+M[1][x.getMonth()]:W[L][0]+', '+x.getDate()+' '+M[L][x.getMonth()])+(D.t?' · '+D.t:'');
document.getElementById('clnd').textContent=s;document.getElementById('clnin').textContent=g==0?D.lab.today:g==1?D.lab.tomorrow:D.lab.indays.replace('{n}',g);
document.getElementById('clnext').hidden=false})();"""
