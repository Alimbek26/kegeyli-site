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
      leader=None, teacher=None, when=None, where=None, members=None, since=None, done=[], photo=None),
]


DOC_I = '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>'


def _svg(p, s=22):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'


def _card(c, i, up, href):
    facts = [(T[k][i], c[k][i] if isinstance(c[k], tuple) else c[k]) for k in ("leader", "teacher", "when", "where", "members", "since") if c.get(k)]
    fx = ("<dl class=\"clfacts\">" + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in facts) + "</dl>") if facts else ""
    done = (f'<h3>{T["done"][i]}</h3><ul class="cldone">' + "".join(f"<li>{d[i]}</li>" for d in c["done"]) + "</ul>") if c.get("done") else ""
    ph = f'<img class="clph" src="{up}photos/clubs/{c["photo"]}" alt="{c["name"][i]}" loading="lazy">' if c.get("photo") else ""
    law = (f'<a class="cllaw" href="{href(c["law"])}"><span class="clli">{_svg(DOC_I, 20)}</span>'
           f'<span><small>{T["basis"][i]}</small><b>{c["basis"][i]}</b></span><em>{T["decree"][i]} →</em></a>') if c.get("law") else ""
    return (f'<article class="clcard" id="{c["key"]}" style="--c:{c["colour"]}">'
            f'<div class="clhead"><span class="clic">{_svg(c["icon"], 34)}</span><div><span class="cltag">{c["tag"][i]}</span><h2>{c["name"][i]}</h2></div></div>'
            f'{ph}<p class="clintro">{c["intro"][i]}</p>{fx}'
            f'<h3>{T["what"][i]}</h3><ul class="clwhat">' + "".join(f'<li><span>{n + 1}</span>{w[i]}</li>' for n, w in enumerate(c["what"])) + '</ul>'
            f'{done}{law}</article>')


def body(i, up, href):
    cards = "".join(_card(c, i, up, href) for c in CLUBS)
    return (f'<p class="lead2">{T["lead"][i]}</p><div class="clubs">{cards}</div>'
            f'<div class="card cljoin"><h3>{T["join_h"][i]}</h3><p>{T["join_p"][i]}</p>'
            f'<p class="btns"><a class="btn s" href="{href("counseling/")}">{__import__("counseling").NAME[i]} →</a></p></div>'
            f'<p class="note">{T["more"][i]}</p>')
