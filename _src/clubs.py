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
      when=L("Eki háptede bir ret, siyshembi kúni", "Every other Tuesday", "Ikki haftada bir marta, seshanba kuni", "Раз в две недели, по вторникам"),
      where=None, members=None,
      since=L("2024-jıl 1-aprel", "1 April 2024", "2024-yil 1-aprel", "1 апреля 2024 г."),
      done=[], photo=None, join=True),
]


DOC_I = '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>'


def _svg(p, s=22):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'


def _card(c, i, up, href):
    facts = [(T[k][i], c[k][i] if isinstance(c[k], tuple) else c[k]) for k in ("teacher", "when", "where", "members", "since") if c.get(k)]
    fx = ("<dl class=\"clfacts\">" + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in facts) + "</dl>") if facts else ""
    if c.get("leader"):
        nm, sl, rl = c["leader"]
        fx = (f'<a class="cllead" href="{href("teachers/" + sl + "/")}"><img src="{up}photos/teachers/{sl}-s.jpg" alt="" width="56" height="56" loading="lazy">'
              f'<span><small>{T["leader"][i]}</small><b>{nm}</b><em>{rl[i]}</em></span><i aria-hidden="true">→</i></a>') + fx
    done = (f'<h3>{T["done"][i]}</h3><ul class="cldone">' + "".join(f"<li>{d[i]}</li>" for d in c["done"]) + "</ul>") if c.get("done") else ""
    ph = f'<img class="clph" src="{up}photos/clubs/{c["photo"]}" alt="{c["name"][i]}" loading="lazy">' if c.get("photo") else ""
    law = (f'<a class="cllaw" href="{href(c["law"])}"><span class="clli">{_svg(DOC_I, 20)}</span>'
           f'<span><small>{T["basis"][i]}</small><b>{c["basis"][i]}</b></span><em>{T["decree"][i]} →</em></a>') if c.get("law") else ""
    return (f'<article class="clcard" id="{c["key"]}" style="--c:{c["colour"]}">'
            f'<div class="clhead"><span class="clic">{_svg(c["icon"], 34)}</span><div><span class="cltag">{c["tag"][i]}</span><h2>{c["name"][i]}</h2></div></div>'
            f'{ph}<p class="clintro">{c["intro"][i]}</p>{fx}'
            f'<h3>{T["what"][i]}</h3><ul class="clwhat">' + "".join(f'<li><span>{n + 1}</span>{w[i]}</li>' for n, w in enumerate(c["what"])) + '</ul>'
            f'{done}{law}'
            + (f'<a class="btn p cljbtn" href="{href(JSUB)}?club={c["key"]}">{T["join_btn"][i]} →</a>' if c.get("join") else "")
            + '</article>')


def body(i, up, href):
    cards = "".join(_card(c, i, up, href) for c in CLUBS)
    return (f'<p class="lead2">{T["lead"][i]}</p><div class="clubs">{cards}</div>'
            f'<div class="card cljoin"><h3>{T["join_h"][i]}</h3><p>{T["join_p"][i]}</p>'
            f'<p class="btns"><a class="btn s" href="{href("counseling/")}">{__import__("counseling").NAME[i]} →</a></p></div>'
            f'<p class="note">{T["more"][i]}</p>')


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
