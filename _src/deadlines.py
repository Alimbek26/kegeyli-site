import json
NAME = ("Múddetler kalendarı", "Deadline calendar", "Muddatlar kalendari", "Календарь дедлайнов")
TAB = ("Kalendar", "Calendar", "Kalendar", "Календарь")
DESC = ("Universitetler, stipendiyalar hám visa qaǵıydaları boyınsha barlıq muddetler bir kalendarda: qansha kún qaldı, telefonıńızǵa eskertiw qosıw.",
        "Every deadline for universities, scholarships and visa rules in one calendar: days left, save your own list and add reminders to your phone.",
        "Universitetlar, stipendiyalar va viza qoidalari bo‘yicha barcha muddatlar bitta kalendarda: necha kun qoldi, o‘z ro‘yxatingizni saqlang va telefonga eslatma qo‘shing.",
        "Все дедлайны по университетам, стипендиям и визовым правилам в одном календаре: сколько дней осталось, свой список и напоминания в телефон.")
UI = {
 "intro": ("Bul kalendarda tiykarǵı muddetler jıynalǵan. “Tastıyıqlanǵan” — usı dáwir ushın rásmiy bette kórsetilgen sana; “Kútilmekte” — aldınǵı jıl tiykarında shama menen. Ózińizge kerekli muddetlerdi juldızsha menen saqlań hám telefonıńızǵa eskertiw qosıń.",
           "The main deadlines are gathered here. “Confirmed” means the date comes from an official page for this cycle; “Expected” is based on last year’s cycle, so check it. Star the ones you need and add reminders to your phone.",
           "Bu kalendarda asosiy muddatlar jamlangan. “Tasdiqlangan” — shu davr uchun rasmiy sahifada ko‘rsatilgan sana; “Kutilmoqda” — o‘tgan yil asosida taxminiy. Kerakli muddatlarni yulduzcha bilan saqlang va telefonga eslatma qo‘shing.",
           "Здесь собраны главные дедлайны. «Подтверждено» — дата с официальной страницы на этот цикл; «Ожидается» — по прошлому году, её нужно проверить. Отмечайте нужные звёздочкой и добавляйте напоминания в телефон."),
 "next": ("Eń jaqın muddetler", "Coming up next", "Eng yaqin muddatlar", "Ближайшие сроки"),
 "all": ("Hámmesi", "All", "Hammasi", "Все"), "uni": ("Universitetler", "Universities", "Universitetlar", "Университеты"),
 "schol": ("Stipendiyalar", "Scholarships", "Stipendiyalar", "Стипендии"), "rules": ("Visa hám qaǵıydalar", "Visa and rules", "Viza va qoidalar", "Виза и правила"),
 "mine": ("Meniń dizimim", "My list", "Mening ro‘yxatim", "Мой список"), "past": ("Ótkenlerdi kórsetiw", "Show past", "O‘tganlarni ko‘rsatish", "Показать прошедшие"),
 "conf": ("Tastıyıqlanǵan", "Confirmed", "Tasdiqlangan", "Подтверждено"), "est": ("Kútilmekte", "Expected", "Kutilmoqda", "Ожидается"),
 "today": ("Búgin", "Today", "Bugun", "Сегодня"), "tomorrow": ("Erteń", "Tomorrow", "Ertaga", "Завтра"),
 "in": ("{n} kúnnen keyin", "in {n} days", "{n} kundan keyin", "через {n} дн."), "ago": ("{n} kún aldın ótti", "{n} days ago", "{n} kun oldin o‘tdi", "{n} дн. назад"),
 "left": ("kún qaldı", "days left", "kun qoldi", "дн. осталось"), "cal": ("Kalendarǵa qosıw", "Add to calendar", "Kalendarga qo‘shish", "В календарь"),
 "calall": ("Saqlanǵanlardı kalendarǵa júklew", "Download saved as calendar", "Saqlanganlarni kalendarga yuklash", "Скачать сохранённые в календарь"),
 "save": ("Saqlaw", "Save", "Saqlash", "Сохранить"), "official": ("Rásmiy bet →", "Official page →", "Rasmiy sahifa →", "Официальная страница →"),
 "empty": ("Bul filtr boyınsha muddet joq.", "No deadlines for this filter.", "Bu filtr bo‘yicha muddat yo‘q.", "По этому фильтру сроков нет."),
 "emptymine": ("Dizim bos. Muddettiń janındaǵı juldızshanı basıń.", "Your list is empty. Tap the star next to a deadline.", "Ro‘yxat bo‘sh. Muddat yonidagi yulduzchani bosing.", "Список пуст. Нажмите звёздочку рядом с дедлайном."),
 "nodate": ("Anıq sanası joq — házir tekseriń", "No fixed date — check now", "Aniq sanasi yo‘q — hozir tekshiring", "Без точной даты — проверьте сейчас"),
 "range": ("{a} – {b}", "{a} – {b}", "{a} – {b}", "{a} – {b}"),
 "foot": ("Sanalar hár jılı ózgeredi. Arza beriwden aldın rásmiy bette tekseriń. Waqıt ádette universitettiń óz waqıt zonasında (mısalı UK 18:00).", "Dates change every year. Always confirm on the official page before you apply. Times are usually in the university’s own time zone (for example 18:00 UK time).", "Sanalar har yili o‘zgaradi. Ariza topshirishdan oldin rasmiy sahifada tasdiqlang. Vaqt odatda universitetning o‘z vaqt mintaqasida (masalan, UK 18:00).", "Даты меняются каждый год. Перед подачей всегда проверяйте официальную страницу. Время обычно по часовому поясу вуза (например, 18:00 по Великобритании)."),
 "months": (["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"], ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
            ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"], ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]),
 "mon3": (["yan", "fev", "mar", "apr", "may", "iyn", "iyl", "avg", "sen", "okt", "noy", "dek"], ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
          ["yan", "fev", "mar", "apr", "may", "iyn", "iyl", "avg", "sen", "okt", "noy", "dek"], ["янв", "фев", "мар", "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]),
}
def T(a, b, c, d): return (a, b, c, d)
# d = start date, e = optional end date, c = cat (uni/schol/rules), s = c(onfirmed)/e(xpected)
E = [
 dict(d="2026-10-15", c="uni", f="🇬🇧", s="c", t=T("UCAS: Oxford, Cambridge hám medicina muddeti", "UCAS: Oxford, Cambridge and medicine deadline", "UCAS: Oxford, Cambridge va tibbiyot muddati", "UCAS: дедлайн Oxford, Cambridge и медицины"),
      n=T("18:00 UK waqtı. Cambridge ushın qosımsha forma 22.10 ǵa shekem.", "18:00 UK time. Cambridge also needs the My Cambridge Application by 22 Oct.", "18:00 UK vaqti. Cambridge uchun qo‘shimcha forma 22.10 gacha.", "18:00 по Великобритании. Для Cambridge также нужна форма My Cambridge Application до 22.10."), u="https://www.undergraduate.study.cam.ac.uk/apply/how/ucas-application"),
 dict(d="2026-11-01", c="uni", f="🇺🇸", s="c", t=T("Erte raund: MIT, Stanford, Caltech", "Early round: MIT, Stanford, Caltech", "Erta bosqich: MIT, Stanford, Caltech", "Ранний раунд: MIT, Stanford, Caltech"),
      n=T("Early/Restrictive Early Action; qarar dekabr ortasında.", "Early / Restrictive Early Action; decisions in mid-December.", "Early/Restrictive Early Action; qaror dekabr o‘rtasida.", "Early / Restrictive Early Action; решения в середине декабря."), u="https://www.admissions.caltech.edu/apply/first-year-applicants/international-applicants"),
 dict(d="2026-11-30", c="rules", f="🇬🇧", s="c", t=T("UK visa: jańa jasaw qarjısı summaları", "UK visa: new living-cost amounts start", "UK viza: yangi yashash mablag‘i summalari", "Виза UK: новые суммы на проживание"),
      n=T("30.11 den keyingi arzalar ushın: Londonnan tısqarı ayına £1 203, Londonda £1 570 (eń kóbi 9 ay).", "For applications from this date: £1,203 a month outside London and £1,570 in London (up to 9 months).", "Shu sanadan keyingi arizalar uchun: Londondan tashqarida oyiga £1 203, Londonda £1 570 (9 oygacha).", "Для заявок с этой даты: £1 203 в месяц вне Лондона и £1 570 в Лондоне (до 9 месяцев)."), u="https://www.ukcisa.org.uk/news/student-update-changes-to-the-immigration-rules-september-2026/"),
 dict(d="2026-12-03", c="uni", f="🇸🇬", s="e", t=T("NUS: arza dáwiri baslanadı (shama menen)", "NUS: application window opens (expected)", "NUS: ariza davri boshlanadi (taxminan)", "NUS: открывается приём заявок (ожидается)"),
      n=T("Aldınǵı jıl 03.12.2025–23.02.2026 bolǵan; arza tólemi S$20.", "Last cycle ran 3 Dec 2025 – 23 Feb 2026; application fee S$20.", "O‘tgan yil 03.12.2025–23.02.2026 bo‘lgan; ariza to‘lovi S$20.", "Прошлый цикл: 03.12.2025–23.02.2026; сбор S$20."), u="https://www.nus.edu.sg/oam/admissions"),
 dict(d="2027-01-01", c="uni", f="🇺🇸", s="c", t=T("Harvard: Regular Decision muddeti", "Harvard: Regular Decision deadline", "Harvard: Regular Decision muddati", "Harvard: дедлайн Regular Decision"),
      n=T("Common App; sheshim mart sońına shekem. SAT yamasa ACT májbúriy.", "Common App; decisions by end of March. SAT or ACT required.", "Common App; qaror mart oxirigacha. SAT yoki ACT majburiy.", "Common App; решения до конца марта. SAT или ACT обязательны."), u="https://college.harvard.edu/admissions/apply/international-applicants"),
 dict(d="2027-01-01", c="rules", f="🇬🇧", s="c", t=T("UK Graduate route 18 ayǵa qısqaradı", "UK Graduate route shortens to 18 months", "UK Graduate route 18 oyga qisqaradi", "Graduate route в UK сокращается до 18 месяцев"),
      n=T("01.01.2027 ten keyingi arzalar ushın bakalavr pitkeriwshileri 2 jıl ornına 18 ay qaladı.", "For applications from 1 Jan 2027, bachelor’s graduates get 18 months instead of 2 years.", "01.01.2027 dan keyingi arizalar uchun bakalavr bitiruvchilari 2 yil o‘rniga 18 oy qoladi.", "Для заявок с 01.01.2027 выпускники бакалавриата получают 18 месяцев вместо 2 лет."), u="https://www.ukcisa.org.uk/news/student-update-changes-to-the-student-and-graduate-rules/"),
 dict(d="2027-01-04", c="uni", f="🇺🇸", s="c", t=T("MIT: Regular Action muddeti", "MIT: Regular Action deadline", "MIT: Regular Action muddati", "MIT: дедлайн Regular Action"),
      n=T("MIT óz portalı; arza tólemi $75. Sheshim mart ortasında.", "MIT’s own portal; $75 fee. Decisions in mid-March.", "MIT o‘z portali; ariza to‘lovi $75. Qaror mart o‘rtasida.", "Собственный портал MIT; сбор $75. Решения в середине марта."), u="https://mitadmissions.org/apply/firstyear/deadlines-requirements/"),
 dict(d="2027-01-04", c="uni", f="🇺🇸", s="c", t=T("Caltech: Regular Decision muddeti", "Caltech: Regular Decision deadline", "Caltech: Regular Decision muddati", "Caltech: дедлайн Regular Decision"),
      n=T("IELTS 7 (hár bólimde 7) kerek bolıwı múmkin; sheshim mart ortasında.", "IELTS 7 in every part may be needed; decisions in mid-March.", "IELTS 7 (har bo‘limda 7) kerak bo‘lishi mumkin; qaror mart o‘rtasida.", "Может понадобиться IELTS 7 в каждом разделе; решения в середине марта."), u="https://www.admissions.caltech.edu/apply/first-year-applicants/international-applicants"),
 dict(d="2027-01-05", c="uni", f="🇺🇸", s="c", t=T("Stanford: Regular Decision muddeti", "Stanford: Regular Decision deadline", "Stanford: Regular Decision muddati", "Stanford: дедлайн Regular Decision"),
      n=T("Common App, $100; sheshim aprel basında.", "Common App, $100 fee; decisions in early April.", "Common App, $100; qaror aprel boshida.", "Common App, $100; решения в начале апреля."), u="https://admission.stanford.edu/apply/first-year/index.html"),
 dict(d="2027-01-10", e="2027-02-20", c="schol", f="🇹🇷", s="e", t=T("Türkiye Burslari: arza dáwiri (shama menen)", "Türkiye Burslari: application window (expected)", "Türkiye Burslari: ariza davri (taxminan)", "Türkiye Burslari: приём заявок (ожидается)"),
      n=T("2026-jılı 10.01–20.02 bolǵan. Onlayn, tólemsiz, jılına bir ret.", "In 2026 it ran 10 Jan – 20 Feb. Online, free, once a year.", "2026 yilda 10.01–20.02 bo‘lgan. Onlayn, bepul, yiliga bir marta.", "В 2026: 10.01–20.02. Онлайн, бесплатно, раз в год."), u="https://turkiyeburslari.gov.tr"),
 dict(d="2027-01-13", c="uni", f="🇬🇧", s="c", t=T("UCAS: tiykarǵı muddet (teń qaraw sanası)", "UCAS: main deadline (equal consideration)", "UCAS: asosiy muddat (teng ko‘rib chiqish sanasi)", "UCAS: основной срок (равное рассмотрение)"),
      n=T("18:00 UK waqtı; keyin de 30.06 ǵa shekem arza beriw múmkin. Arza tólemi £34,50.", "18:00 UK time; applications are accepted until 30 June. Fee £34.50.", "18:00 UK vaqti; keyin ham 30.06 gacha ariza topshirish mumkin. To‘lov £34,50.", "18:00 по Великобритании; заявки принимают до 30.06. Сбор £34,50."), u="https://www.ucas.com/undergraduate"),
 dict(d="2027-01-15", c="schol", f="🇭🇺", s="e", t=T("Stipendium Hungaricum: arza muddeti (shama menen)", "Stipendium Hungaricum: application deadline (expected)", "Stipendium Hungaricum: ariza muddati (taxminan)", "Stipendium Hungaricum: срок подачи (ожидается)"),
      n=T("Aldınǵı jıl 15.01 14:00 CET edi; sistema ádette noyabrde ashıladı. Ózbekstannan 110 oqıwshı.", "Last year it was 15 Jan, 14:00 CET; the system usually opens in November. 110 Uzbek students were awarded in 2026/27.", "O‘tgan yil 15.01 14:00 CET edi; tizim odatda noyabrda ochiladi. O‘zbekistondan 110 o‘quvchi.", "В прошлом году — 15.01, 14:00 CET; система обычно открывается в ноябре. В 2026/27 получили 110 студентов из Узбекистана."), u="https://stipendiumhungaricum.hu"),
 dict(d="2027-02-15", c="uni", f="🇺🇸", s="c", t=T("Stanford: yarım jıllıq transkript; MIT járdem arzası", "Stanford midyear transcript; MIT aid application", "Stanford: yarim yillik transkript; MIT yordam arizasi", "Stanford: полугодовой транскрипт; заявка на помощь MIT"),
      n=T("Stanford ushın 15.02, MIT Regular Action járdem arzası 15.02.", "Stanford midyear transcript due 15 Feb; MIT Regular Action aid application also 15 Feb.", "Stanford uchun 15.02, MIT Regular Action yordam arizasi 15.02.", "Транскрипт Stanford до 15.02; заявка на помощь MIT (Regular Action) тоже 15.02."), u="https://mitadmissions.org/apply/firstyear/deadlines-requirements/"),
 dict(d="2027-02-23", c="uni", f="🇸🇬", s="e", t=T("NUS: arza dáwiri jabıladı (shama menen)", "NUS: application window closes (expected)", "NUS: ariza davri yopiladi (taxminan)", "NUS: приём заявок закрывается (ожидается)"),
      n=T("Aldınǵı jıl 23.02.2026 edi.", "Last year it closed on 23 Feb 2026.", "O‘tgan yil 23.02.2026 edi.", "В прошлом году — 23.02.2026."), u="https://www.nus.edu.sg/oam/admissions"),
 dict(d="2027-02-25", c="uni", f="🇬🇧", s="c", t=T("UCAS Extra ashıladı", "UCAS Extra opens", "UCAS Extra ochiladi", "Открывается UCAS Extra"),
      n=T("5 tańlaw da bar, biraq usınıs joq bolsa qosımsha tańlaw qosıw múmkinligi.", "A chance to add one more choice if you used all five and have no offers.", "5 ta tanlov ishlatilgan, ammo taklif bo‘lmasa, qo‘shimcha tanlov qo‘shish imkoniyati.", "Возможность добавить ещё один выбор, если использованы все пять и нет предложений."), u="https://www.ucas.com/undergraduate"),
 dict(d="2027-03-31", c="uni", f="🇨🇭", s="c", t=T("ETH Zurich: bakalavrǵa arza muddeti", "ETH Zurich: bachelor’s application deadline", "ETH Zurich: bakalavrga ariza muddati", "ETH Zurich: срок подачи на бакалавриат"),
      n=T("Nemis tili talapları usı sanaǵa shekem orınlanıwı kerek. Oqıw tek gúzde baslanadı.", "German language requirements must be met by this date. Studies start in autumn only.", "Nemis tili talablari shu sanagacha bajarilishi kerak. O‘qish faqat kuzda boshlanadi.", "Требования к немецкому нужно выполнить к этой дате. Учёба начинается только осенью."), u="https://ethz.ch/en/studies/registration-application/bachelor/other-certificates/application.html"),
 dict(d="2027-05-01", c="uni", f="🇺🇸", s="c", t=T("Qabıl etilgenler ushın juwap muddeti: Stanford, Caltech", "Reply deadline for admitted students: Stanford, Caltech", "Qabul qilinganlar uchun javob muddati: Stanford, Caltech", "Срок ответа для принятых: Stanford, Caltech"),
      n=T("Orındı tastıyıqlaw ushın 1-may.", "1 May is the day to confirm your place.", "O‘rinni tasdiqlash uchun 1-may.", "1 мая — день подтверждения места."), u="https://admission.stanford.edu/apply/first-year/index.html"),
 dict(d="2027-05-17", c="schol", f="🇯🇵", s="e", t=T("MEXT bakalavr stipendiyası: arza muddeti (shama menen)", "MEXT undergraduate scholarship: embassy deadline (expected)", "MEXT bakalavr stipendiyasi: ariza muddati (taxminan)", "Стипендия MEXT (бакалавриат): срок в посольстве (ожидается)"),
      n=T("2026-jılı basqa elshixanalarda 18–22-may; Ózbekstandaǵı elshixanadan anıq sanasın sorań.", "In 2026 other embassies set 18–22 May; ask the Embassy of Japan in Uzbekistan for exact dates.", "2026 yilda boshqa elchixonalarda 18–22-may; O‘zbekistondagi elchixonadan aniq sanani so‘rang.", "В 2026 в других посольствах — 18–22 мая; уточните даты в посольстве Японии в Узбекистане."), u="https://www.studyinjapan.go.jp"),
 dict(d="2027-06-30", c="uni", f="🇬🇧", s="c", t=T("UCAS: arza beriwdiń sońǵı kúni", "UCAS: last date to apply", "UCAS: ariza topshirishning oxirgi kuni", "UCAS: последний день подачи"),
      n=T("2 iyulde Clearing ashıladı.", "Clearing opens on 2 July.", "2-iyulda Clearing ochiladi.", "2 июля открывается Clearing."), u="https://www.ucas.com/undergraduate"),
]
UNDATED = [
 dict(f="🇰🇷", t=T("GKS-U (Koreya): 2027 qabıllawı ushın elshixana joli", "GKS-U (Korea): embassy track for the 2027 intake", "GKS-U (Koreya): 2027 qabul uchun elchixona yo‘li", "GKS-U (Корея): набор 2027 через посольство"),
      n=T("Arzalar ashılǵan. Anıq múddetti Koreya elshixanasınan hám studyinkorea.go.kr saytınan házir tekseriń.", "Applications have opened. Check the exact deadline with the Korean embassy and studyinkorea.go.kr now.", "Arizalar ochilgan. Aniq muddatni Koreya elchixonasi va studyinkorea.go.kr saytidan hozir tekshiring.", "Приём открыт. Точный срок сразу уточните в посольстве Кореи и на studyinkorea.go.kr."), u="https://www.studyinkorea.go.kr"),
 dict(f="🇺🇸", t=T("Common App fee waiver", "Common App fee waiver", "Common App fee waiver", "Common App fee waiver"),
      n=T("Másláhátshi tastıyıqlawı kerek; arza beriwden aldın sorań.", "Your counselor must confirm it, so ask before you submit.", "Maslahatchi tasdiqlashi kerak; ariza topshirishdan oldin so‘rang.", "Его должен подтвердить консультант, поэтому просите до подачи."), u="https://www.commonapp.org/apply/first-year-students"),
]
def body(i, tabs_html):
    data = {"ui": {k: (v[i] if not isinstance(v[0], list) else v[i]) for k, v in UI.items() if k not in ("intro", "foot")},
            "ev": [dict(d=e["d"], e=e.get("e"), c=e["c"], f=e["f"], s=e["s"], t=e["t"][i], n=e["n"][i], u=e["u"], id=n) for n, e in enumerate(E)],
            "un": [dict(f=e["f"], t=e["t"][i], n=e["n"][i], u=e["u"]) for e in UNDATED]}
    js = DL_JS.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    return (f'{tabs_html}<p class="lead2">{UI["intro"][i]}</p><section id="dl"><div id="dltop" class="dltop"></div>'
            f'<div class="dlbar"><div class="fchips" id="dlcat"></div><div class="dlact"><label class="dlpast"><input type="checkbox" id="dlpast"> <span id="dlpastl"></span></label>'
            f'<button type="button" class="fc" id="dlall"></button></div></div><div id="dllist"></div><div id="dlun" class="card gapp"></div></section>'
            f'<p class="note">{UI["foot"][i]}</p><script>{js}</script>')
DL_JS = r"""(function(){var D=__DATA__,U=D.ui,$=function(i){return document.getElementById(i)};
var cat='all',showPast=false,saved=[];try{saved=JSON.parse(localStorage.getItem('dlSaved')||'[]')}catch(e){}
function save(){try{localStorage.setItem('dlSaved',JSON.stringify(saved))}catch(e){}}
function P(s){var a=s.split('-');return new Date(+a[0],a[1]-1,+a[2])}
var now=new Date(),today=new Date(now.getFullYear(),now.getMonth(),now.getDate());
function diff(d){return Math.round((P(d)-today)/864e5)}
function rel(n){return n==0?U.today:n==1?U.tomorrow:n>0?U['in'].replace('{n}',n):U.ago.replace('{n}',-n)}
function fmt(d){var x=P(d);return x.getDate()+' '+U.months[x.getMonth()]}
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function ics(list){var p=function(n){return(n<10?'0':'')+n},d8=function(s){return s.replace(/-/g,'')},nx=function(s){var x=P(s);x.setDate(x.getDate()+1);return x.getFullYear()+p(x.getMonth()+1)+p(x.getDate())};
var o=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//kegeyliqm.uz//deadlines//EN','CALSCALE:GREGORIAN'];
list.forEach(function(e){var t=(e.s=='e'?'('+U.est+') ':'')+e.t;o.push('BEGIN:VEVENT','UID:dl'+e.id+'@kegeyliqm.uz','DTSTAMP:'+now.getFullYear()+p(now.getMonth()+1)+p(now.getDate())+'T000000Z','DTSTART;VALUE=DATE:'+d8(e.d),'DTEND;VALUE=DATE:'+nx(e.e||e.d),'SUMMARY:'+t.replace(/[,;]/g,' '),'DESCRIPTION:'+e.n.replace(/[,;]/g,' ')+' '+e.u,'URL:'+e.u,
'BEGIN:VALARM','TRIGGER:-P7D','ACTION:DISPLAY','DESCRIPTION:'+t.replace(/[,;]/g,' ')+' 7','END:VALARM','BEGIN:VALARM','TRIGGER:-P1D','ACTION:DISPLAY','DESCRIPTION:'+t.replace(/[,;]/g,' ')+' 1','END:VALARM','END:VEVENT')});o.push('END:VCALENDAR');
var a=document.createElement('a');a.href=URL.createObjectURL(new Blob([o.join('\r\n')],{type:'text/calendar'}));a.download='kegeyli-deadlines.ics';document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove()},500)}
function vis(e){if(cat=='mine')return saved.indexOf(e.id)>-1;return cat=='all'||e.c==cat}
function badge(e){return '<span class="dlb '+(e.s=='c'?'ok':'es')+'">'+(e.s=='c'?U.conf:U.est)+'</span>'}
function item(e){var n=diff(e.e||e.d),st=saved.indexOf(e.id)>-1,dt=P(e.d),dd=e.e?U.range.replace('{a}',fmt(e.d)).replace('{b}',fmt(e.e)):fmt(e.d)+' '+dt.getFullYear();
var cls=n<0?' past':n<=14?' soon':'';
return '<article class="dli c-'+e.c+cls+'" data-id="'+e.id+'"><div class="dld"><b>'+dt.getDate()+'</b><span>'+U.mon3[dt.getMonth()]+'</span></div><div class="dlb2"><div class="dlh"><h4>'+e.f+' '+esc(e.t)+'</h4>'+badge(e)+'</div><p>'+esc(e.n)+'</p>'
+'<div class="dlm"><span class="dlr">'+dd+' · <b>'+rel(n)+'</b></span><span class="dla"><button type="button" class="dlst'+(st?' on':'')+'" data-a="s" aria-label="'+U.save+'" aria-pressed="'+st+'">'+(st?'★':'☆')+'</button><button type="button" class="dlcal" data-a="c">'+U.cal+'</button><a href="'+e.u+'" rel="noopener">'+U.official+'</a></span></div></div></article>'}
function render(){var L=D.ev.filter(vis).sort(function(a,b){return a.d<b.d?-1:a.d>b.d?1:0}),up=D.ev.filter(function(e){return diff(e.e||e.d)>=0}).sort(function(a,b){return a.d<b.d?-1:1}).slice(0,3);
$('dltop').innerHTML='<h3>'+U.next+'</h3><div class="dlcards">'+up.map(function(e){var n=Math.max(0,diff(e.d)),late=e.e&&diff(e.d)<0;return '<div class="dlc c-'+e.c+'"><div class="dln"><b>'+(late?'•':n)+'</b><span>'+U.left+'</span></div><div><p class="dlct">'+e.f+' '+esc(e.t)+'</p><small>'+fmt(e.d)+' '+P(e.d).getFullYear()+' · '+(e.s=='c'?U.conf:U.est)+'</small></div></div>'}).join('')+'</div>';
var h='',last='';L.forEach(function(e){if(!showPast&&diff(e.e||e.d)<0)return;var x=P(e.d),m=U.months[x.getMonth()]+' '+x.getFullYear();if(m!=last){h+='<h3 class="dlmon">'+m+'</h3>';last=m}h+=item(e)});
$('dllist').innerHTML=h||'<p class="dlempty">'+(cat=='mine'?U.emptymine:U.empty)+'</p>';
$('dlun').innerHTML='<h3>'+U.nodate+'</h3><ul>'+D.un.map(function(e){return '<li>'+e.f+' <b>'+esc(e.t)+'</b> — '+esc(e.n)+' <a href="'+e.u+'" rel="noopener">'+U.official+'</a></li>'}).join('')+'</ul>'}
var cats=[['all',U.all],['uni',U.uni],['schol',U.schol],['rules',U.rules],['mine','★ '+U.mine]];
function chips(){$('dlcat').innerHTML=cats.map(function(c){return '<button type="button" class="fc'+(c[0]==cat?' on':'')+'" data-v="'+c[0]+'">'+c[1]+'</button>'}).join('')}
$('dlcat').addEventListener('click',function(e){var b=e.target.closest('.fc');if(!b)return;cat=b.dataset.v;chips();render()});
$('dlpast').addEventListener('change',function(){showPast=this.checked;render()});$('dlpastl').textContent=U.past;$('dlall').textContent=U.calall;
$('dlall').addEventListener('click',function(){var l=D.ev.filter(function(e){return saved.indexOf(e.id)>-1&&diff(e.e||e.d)>=0});if(!l.length){alert(U.emptymine);return}ics(l)});
$('dllist').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var id=+b.closest('.dli').dataset.id,ev=D.ev.filter(function(x){return x.id==id})[0];
if(b.dataset.a=='c')ics([ev]);else if(b.dataset.a=='s'){var k=saved.indexOf(id);k>-1?saved.splice(k,1):saved.push(id);save();render()}});
chips();render()})();"""
