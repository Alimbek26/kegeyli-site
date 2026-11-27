# IELTS page (kaa, en, uz, ru)
NAME = ("IELTS", "IELTS", "IELTS", "IELTS")
DESC = ("IELTS tayarlıǵı: ball esaplaw kalkulyatorı, oqıw rejesi, keńesler hám kúnlik sózler. Kegeyli qánigelestirilgen mektebi.",
        "IELTS preparation: band score calculator, study planner, tips and a daily word. Kegeyli specialized school.",
        "IELTS tayyorgarligi: ball hisoblash kalkulyatori, o‘quv reja, maslahatlar va kunlik so‘z. Kegeyli ixtisoslashtirilgan maktabi.",
        "Подготовка к IELTS: калькулятор баллов, план занятий, советы и слово дня. Кегейлийская специализированная школа.")
BANDS = {5.5: 4, 6.0: 5, 6.5: 1}   # IELTS results of our graduates (totals only)
S = {
 "intro": ("IELTS — ingliz tili dárejesin xalıqaralıq tastıyıqlaytuǵın imtihan. Bul bet imtihanǵa tayarlanıw ushın: ball kalkulyatorı, oqıw rejesi, keńesler hám kúnlik sózler.",
           "IELTS is an international test of English. This page helps you prepare: a band calculator, a study planner, tips and a word of the day.",
           "IELTS — ingliz tili darajasini xalqaro miqyosda tasdiqlovchi imtihon. Bu sahifa tayyorgarlik uchun: ball kalkulyatori, o‘quv reja, maslahatlar va kunlik so‘z.",
           "IELTS — международный экзамен по английскому языку. Эта страница поможет подготовиться: калькулятор баллов, план занятий, советы и слово дня."),
 "parts_h": ("Imtihan dúzilisi", "What is in the test", "Imtihon tuzilishi", "Структура экзамена"),
 "parts": (
   (("Listening", "40 soraw, hár durıs juwap — 1 ball"), ("Reading", "40 soraw, hár durıs juwap — 1 ball"), ("Writing", "2 tapsırma; 2-tapsırma kóbirek ball beredi"), ("Speaking", "Imtihanshı menen sóylesiw")),
   (("Listening", "40 questions, 1 mark per correct answer"), ("Reading", "40 questions, 1 mark per correct answer"), ("Writing", "2 tasks; Task 2 counts for more"), ("Speaking", "A conversation with an examiner")),
   (("Listening", "40 ta savol, har bir to‘g‘ri javob — 1 ball"), ("Reading", "40 ta savol, har bir to‘g‘ri javob — 1 ball"), ("Writing", "2 ta topshiriq; 2-topshiriq ko‘proq ball beradi"), ("Speaking", "Imtihonchi bilan suhbat")),
   (("Listening", "40 вопросов, 1 балл за верный ответ"), ("Reading", "40 вопросов, 1 балл за верный ответ"), ("Writing", "2 задания; задание 2 весит больше"), ("Speaking", "Беседа с экзаменатором"))),
 "scale": ("Ball 0 den 9 ge shekem. Ulıwma ball — tórt bólimniń ortasha mánisi, eń jaqın 0,5 ge jumalaqlanadı. Nátiyje ádette 2 jıl dawamında jaramlı dep esaplanadı; qosımsha maǵlıwmat ushın kerekli oqıw ornınan sorań.",
           "Scores run from 0 to 9. The overall band is the average of the four sections, rounded to the nearest half band. IELTS recommends treating a result as valid for two years; check with your university.",
           "Ball 0 dan 9 gacha. Umumiy ball — to‘rt bo‘lim o‘rtachasi, eng yaqin 0,5 gacha yaxlitlanadi. Natija odatda 2 yil davomida amal qiladi deb hisoblanadi; aniqlik uchun o‘z oliygohingizdan so‘rang.",
           "Баллы от 0 до 9. Общий балл — среднее по четырём разделам, округлённое до ближайших 0,5. Результат принято считать действительным 2 года; уточняйте в своём вузе."),
 "calc_h": ("Ball kalkulyatorı", "Band calculator", "Ball kalkulyatori", "Калькулятор баллов"),
 "calc_p": ("Listening hám Reading boyınsha durıs juwaplar sanın kiritiń, Writing hám Speaking ushın ball tańlań. Nátiyje shama menen esaplanadı.",
            "Enter your correct answers for Listening and Reading and choose a band for Writing and Speaking. The result is an estimate.",
            "Listening va Reading bo‘yicha to‘g‘ri javoblar sonini kiriting, Writing va Speaking uchun ball tanlang. Natija taxminiy.",
            "Введите число верных ответов по Listening и Reading и выберите балл за Writing и Speaking. Результат приблизительный."),
 "f_l": ("Listening (durıs juwap / 40)", "Listening (correct / 40)", "Listening (to‘g‘ri / 40)", "Listening (верных / 40)"),
 "f_r": ("Reading, Academic (durıs juwap / 40)", "Reading, Academic (correct / 40)", "Reading, Academic (to‘g‘ri / 40)", "Reading, Academic (верных / 40)"),
 "f_w": ("Writing balı", "Writing band", "Writing bali", "Балл Writing"),
 "f_s": ("Speaking balı", "Speaking band", "Speaking bali", "Балл Speaking"),
 "f_t": ("Maqsetli ball", "Target band", "Maqsad ball", "Целевой балл"),
 "overall": ("Ulıwma ball", "Overall band", "Umumiy ball", "Общий балл"),
 "reached": ("Maqsetke jettińiz!", "Target reached!", "Maqsadga erishdingiz!", "Цель достигнута!"),
 "below": ("Maqsetke jetiw ushın {d} ball jetispeydi", "{d} below your target", "Maqsadga {d} ball yetmaydi", "До цели не хватает {d}"),
 "focus": ("Kóbirek dıqqat: {s}", "Focus on: {s}", "Ko‘proq e’tibor: {s}", "Обратите внимание: {s}"),
 "calc_note": ("Listening hám Reading ushın kerekli durıs juwap sanı hár imtihan variantında azmaz ózgeredi, sonlıqtan haqıyqıy nátiyje basqasha bolıwı múmkin.",
               "The number of correct answers needed for each band varies slightly between test versions, so your real result may differ.",
               "Har bir band uchun kerakli to‘g‘ri javoblar soni imtihon variantiga qarab biroz farq qiladi, shuning uchun haqiqiy natija boshqacha bo‘lishi mumkin.",
               "Число верных ответов для каждого балла немного меняется от варианта к варианту, поэтому реальный результат может отличаться."),
 "plan_h": ("Háptelik oqıw rejesi", "Weekly study plan", "Haftalik o‘quv reja", "Недельный план занятий"),
 "plan_p": ("Hár kúni 45–60 minut. Kalkulyatorda eń álsiz bólim anıqlansa, oǵan kúnine qosımsha 15 minut berin.",
            "45–60 minutes a day. If the calculator shows a weakest section, give it an extra 15 minutes daily.",
            "Har kuni 45–60 daqiqa. Kalkulyator eng zaif bo‘limni ko‘rsatsa, unga har kuni qo‘shimcha 15 daqiqa ajrating.",
            "По 45–60 минут в день. Если калькулятор показал слабый раздел, уделяйте ему ещё 15 минут ежедневно."),
 "days": (("Dúy", "Sey", "Sár", "Piy", "Juma", "Shem", "Jek"), ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"),
          ("Du", "Se", "Chor", "Pay", "Ju", "Sha", "Yak"), ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")),
 "plan": (
   ("Listening: 1 bólim, keyin qátelerdi tekseriw", "Reading: 1 tekst waqıt penen, qátelerdi analiz", "Writing: 1 tapsırma, muǵallimge kórsetiw", "Speaking: 10 minut ózińizdi jazıp alıp tıńlań", "Sózler hám grammatika", "Mini-test (bir bólim tolıq)", "Dem alıs yamasa jeńil oqıw"),
   ("Listening: 1 section, then review mistakes", "Reading: 1 timed passage, analyse mistakes", "Writing: 1 task, show it to your teacher", "Speaking: record yourself for 10 minutes and listen", "Vocabulary and grammar", "Mini-test (one full section)", "Rest or light reading"),
   ("Listening: 1 bo‘lim, so‘ng xatolarni tahlil qiling", "Reading: 1 matn vaqt bilan, xatolarni tahlil", "Writing: 1 topshiriq, o‘qituvchiga ko‘rsating", "Speaking: 10 daqiqa o‘zingizni yozib eshiting", "Lug‘at va grammatika", "Mini-test (bitta bo‘lim to‘liq)", "Dam olish yoki yengil o‘qish"),
   ("Listening: 1 раздел, затем разбор ошибок", "Reading: 1 текст на время, разбор ошибок", "Writing: 1 задание, покажите учителю", "Speaking: запишите себя 10 минут и прослушайте", "Слова и грамматика", "Мини-тест (один раздел целиком)", "Отдых или лёгкое чтение")),
 "tips_h": ("Bólimler boyınsha keńesler", "Tips by section", "Bo‘limlar bo‘yicha maslahatlar", "Советы по разделам"),
 "tips": (
   (("Listening", ("Audio baslanbastan aldın sorawlardı oqıp shıǵıń.", "Juwaplardı tıńlap atırıp jazıń, aqırǵı minutta dıqqat penen kóshirip jazıń.", "Orfografiya hám kóplik formasına dıqqat qılıń — qáte jazıw ballǵa tásir etedi.")),
    ("Reading", ("Aldın tekstti tez kóz jiberip shıǵıń, soń sorawlarǵa juwap izleń.", "Bir tekstke shama menen 20 minuttan artıq waqıt jumsamań.", "Hesh qanday juwapti bos qaldırmań — qáte juwap ushın jazalaw joq.")),
    ("Writing", ("Task 2 ballı kóbirek, sonlıqtan oǵan jetkilikli waqıt qaldırıń.", "3–5 minut rejelestirip, soń jazıń; aqırında grammatikanı tekseriń.", "Sózlerdiń minimal sanın saqlań: Task 1 — 150, Task 2 — 250.")),
    ("Speaking", ("Toliq gápler menen juwap berip, sebep yamasa mısal qosıń.", "Juwaplardı jattap alıwdan qashıń — imtihanshılar buni biledi.", "Túsinbesen, imtihanshıdan qaytalawın sorań.")))
   ,
   (("Listening", ("Read the questions before the audio starts.", "Write answers as you listen; use the last minute to copy carefully.", "Watch spelling and plurals — a spelling mistake loses the mark.")),
    ("Reading", ("Skim the passage first, then look for answers question by question.", "Don’t spend much more than about 20 minutes on one passage.", "Never leave an answer blank — wrong answers are not penalised.")),
    ("Writing", ("Task 2 counts for more, so keep enough time for it.", "Plan for 3–5 minutes, then write; check grammar at the end.", "Respect the minimum length: 150 words for Task 1, 250 for Task 2.")),
    ("Speaking", ("Answer in full sentences and add a reason or an example.", "Don’t memorise answers — examiners notice.", "If you don’t understand, ask the examiner to repeat.")))
   ,
   (("Listening", ("Audio boshlanishidan oldin savollarni o‘qib chiqing.", "Javoblarni tinglab turib yozing, oxirgi daqiqada ehtiyotkorlik bilan ko‘chiring.", "Imlo va ko‘plik shakliga e’tibor bering — imlo xatosi ballni yo‘qotadi.")),
    ("Reading", ("Avval matnni tez ko‘zdan kechiring, so‘ng savollarga javob qidiring.", "Bitta matnga taxminan 20 daqiqadan ko‘p vaqt sarflamang.", "Hech bir javobni bo‘sh qoldirmang — xato javob uchun jarima yo‘q.")),
    ("Writing", ("2-topshiriq ko‘proq ball beradi, unga yetarli vaqt qoldiring.", "3–5 daqiqa reja tuzing, so‘ng yozing; oxirida grammatikani tekshiring.", "Minimal hajmga rioya qiling: 1-topshiriq — 150, 2-topshiriq — 250 so‘z.")),
    ("Speaking", ("To‘liq gaplar bilan javob bering, sabab yoki misol qo‘shing.", "Javoblarni yodlamang — imtihonchilar buni sezadi.", "Tushunmasangiz, imtihonchidan takrorlashni so‘rang.")))
   ,
   (("Listening", ("Прочитайте вопросы до начала записи.", "Записывайте ответы по ходу, последнюю минуту используйте для аккуратного переписывания.", "Следите за орфографией и множественным числом — ошибка в написании стоит балла.")),
    ("Reading", ("Сначала бегло просмотрите текст, затем ищите ответы на вопросы.", "Не тратьте на один текст заметно больше 20 минут.", "Не оставляйте ответы пустыми — за неверные ответы баллы не снимают.")),
    ("Writing", ("Задание 2 весит больше, оставьте на него достаточно времени.", "Потратьте 3–5 минут на план, затем пишите; в конце проверьте грамматику.", "Соблюдайте минимальный объём: 150 слов в задании 1, 250 — в задании 2.")),
    ("Speaking", ("Отвечайте полными предложениями, добавляйте причину или пример.", "Не заучивайте ответы наизусть — экзаменаторы это замечают.", "Если не поняли вопрос, попросите экзаменатора повторить.")))),
 "word_h": ("Kúnnıń sózi", "Word of the day", "Kunning so‘zi", "Слово дня"),
 "res_h": ("Mektebimizdiń nátiyjeleri", "Our results", "Maktabimiz natijalari", "Результаты нашей школы"),
 "res_p": ("2022–2026 jıllarındaǵı pitkeriwshilerimizden {n} nafarı IELTS tapsırdı. Nátiyjeler (tek ulıwma sanlar):", "{n} of our 2022–2026 graduates took IELTS. Results (totals only):",
           "2022–2026 yillardagi bitiruvchilarimizdan {n} nafari IELTS topshirdi. Natijalar (faqat umumiy sonlar):", "{n} наших выпускников 2022–2026 годов сдали IELTS. Результаты (только общие числа):"),
 "grads": ("pitkeriwshi", "graduates", "nafar", "чел."),
 "links_h": ("Rásmiy derekler", "Official sources", "Rasmiy manbalar", "Официальные источники"),
 "link1": ("Rásmiy IELTS veb-saytı", "Official IELTS website", "Rasmiy IELTS veb-sayti", "Официальный сайт IELTS"),
 "link2": ("British Council — IELTS", "British Council — IELTS", "British Council — IELTS", "British Council — IELTS"),
 "links_note": ("Imtihan kúnleri hám bahası ózgerip turadı, sonlıqtan registraciya aldınan rásmiy saytlardan tekseriń.",
                "Test dates and fees change, so check the official sites before you register.",
                "Imtihon sanalari va narxlari o‘zgarib turadi, shuning uchun ro‘yxatdan o‘tishdan oldin rasmiy saytlarni tekshiring.",
                "Даты и стоимость экзамена меняются, поэтому перед регистрацией проверьте официальные сайты."),
}
WORDS = [  # en, uz, ru, kaa, example
 ("analyse", "tahlil qilmoq", "анализировать", "analiz qılıw", "Scientists analyse data to find patterns."),
 ("approach", "yondashuv", "подход", "usıl", "A new approach to teaching maths helped students."),
 ("benefit", "foyda", "польза", "payda", "Regular reading has many benefits."),
 ("consequence", "oqibat", "последствие", "aqıbet", "Pollution has serious consequences for health."),
 ("contribute", "hissa qo‘shmoq", "вносить вклад", "úles qosıw", "Exercise contributes to better sleep."),
 ("evidence", "dalil", "доказательство", "dálil", "There is strong evidence that sleep improves memory."),
 ("factor", "omil", "фактор", "faktor", "Cost is an important factor when choosing a university."),
 ("impact", "ta’sir", "влияние", "tásir", "Technology has a big impact on education."),
 ("significant", "sezilarli", "значительный", "áhmiyetli", "There was a significant rise in prices."),
 ("environment", "atrof-muhit", "окружающая среда", "átirap-ortalıq", "We must protect the environment."),
 ("resource", "resurs", "ресурс", "resurs", "Water is a vital natural resource."),
 ("trend", "tendensiya", "тенденция", "tendenciya", "The graph shows a downward trend."),
 ("issue", "muammo", "проблема", "másele", "Climate change is a global issue."),
 ("maintain", "saqlab turmoq", "поддерживать", "saqlap turıw", "It is hard to maintain concentration for hours."),
 ("global", "global", "глобальный", "global", "English is a global language."),
 ("society", "jamiyat", "общество", "jámiyet", "Education benefits the whole society."),
 ("require", "talab qilmoq", "требовать", "talap etiw", "This course requires hard work."),
 ("challenge", "qiyinchilik", "трудность", "qıyınshılıq", "Learning a language is a challenge."),
 ("achieve", "erishmoq", "достигать", "erisiw", "She worked hard to achieve her goal."),
 ("decline", "pasayish", "снижение", "tómenlew", "There was a sharp decline in sales."),
]

JS = r"""
(function(){
 var $=function(id){return document.getElementById(id)};
 var LT=[[39,9],[37,8.5],[35,8],[32,7.5],[30,7],[26,6.5],[23,6],[18,5.5],[16,5],[13,4.5],[10,4],[8,3.5],[6,3],[4,2.5],[0,2]];
 var RT=[[39,9],[37,8.5],[35,8],[33,7.5],[30,7],[27,6.5],[23,6],[19,5.5],[15,5],[13,4.5],[10,4],[8,3.5],[6,3],[4,2.5],[0,2]];
 var band=function(n,t){for(var i=0;i<t.length;i++)if(n>=t[i][0])return t[i][1];return 0};
 var D=JSON.parse($('ieltsdata').textContent);
 var fmt=function(x){return (Math.round(x*2)/2).toFixed(1).replace('.',D.dec)};
 function calc(){
  var l=Math.max(0,Math.min(40,+$('il').value||0)),r=Math.max(0,Math.min(40,+$('ir').value||0));
  var w=+$('iw').value,s=+$('is').value,t=+$('it').value;
  var b=[['L',band(l,LT)],['R',band(r,RT)],['W',w],['S',s]];
  var avg=(b[0][1]+b[1][1]+b[2][1]+b[3][1])/4,ov=Math.floor(avg*2+0.5)/2;
  $('ibands').innerHTML=b.map(function(x){return '<div class="ibt'+(x[1]<t?' low':'')+'"><span>'+D.n[x[0]]+'</span><b>'+fmt(x[1])+'</b></div>'}).join('');
  $('iov').textContent=fmt(ov);
  var low=b.filter(function(x){return x[1]<t}).sort(function(a,c){return a[1]-c[1]});
  $('imsg').textContent=ov>=t?D.reached:D.below.replace('{d}',fmt(t-ov))+(low.length?' · '+D.focus.replace('{s}',low.map(function(x){return D.n[x[0]]}).join(', ')):'');
  $('iresult').className='iresult '+(ov>=t?'ok':'');
  try{localStorage.setItem('ielts',JSON.stringify({l:l,r:r,w:w,s:s,t:t}))}catch(e){}
 }
 try{var sv=JSON.parse(localStorage.getItem('ielts')||'null');if(sv){$('il').value=sv.l;$('ir').value=sv.r;$('iw').value=sv.w;$('is').value=sv.s;$('it').value=sv.t}}catch(e){}
 ['il','ir','iw','is','it'].forEach(function(id){$(id).addEventListener('input',calc);$(id).addEventListener('change',calc)});
 calc();
 var d=new Date(),k=Math.floor((d-new Date(d.getFullYear(),0,0))/864e5)%D.w;
 document.querySelectorAll('.iword').forEach(function(e){e.hidden=+e.dataset.k!==k});
})();
"""

REG = dict(
 h=("Rásmiy IELTS dizimge alıw punkti", "Official IELTS Registration Point", "Rasmiy IELTS ro‘yxatga olish nuqtasi", "Официальный пункт регистрации на IELTS"),
 p=("2026-jıl 29-yanvardan baslap mektebimiz British Council menen sheriklikte rásmiy IELTS dizimge alıw punkti bolıp islemekte. Barlıq xızmetler biypul.",
    "Since 29 January 2026 our school has been an official IELTS Registration Point in partnership with the British Council. All services are free.",
    "2026-yil 29-yanvardan maktabimiz British Council bilan hamkorlikda rasmiy IELTS ro‘yxatga olish nuqtasi sifatida faoliyat yuritmoqda. Barcha xizmatlar bepul.",
    "С 29 января 2026 года наша школа — официальный пункт регистрации на IELTS в партнёрстве с British Council. Все услуги бесплатные."),
 items=(("IELTS Academic hám General Training imtixanlarına rásmiy dizimge alıw", "Imtixan sánesi, orınları hám tártibi haqqında isenimli maǵlıwmat", "Hújjetlerdi tayarlaw hám tapsırıwda másláhát"),
        ("Official registration for IELTS Academic and IELTS General Training", "Reliable information on test dates, venues and procedures", "Advice on preparing and submitting your documents"),
        ("IELTS Academic va IELTS General Training imtihonlariga rasmiy ro‘yxatdan o‘tkazish", "Imtihon sanalari, joylashuvi va topshirish tartibi bo‘yicha ishonchli ma’lumot", "Hujjatlarni tayyorlash va topshirishda maslahat"),
        ("Официальная регистрация на IELTS Academic и IELTS General Training", "Надёжная информация о датах, местах и порядке сдачи", "Консультации по подготовке и подаче документов")),
 who=("Juwapker: Alimbek Jumamuratov", "Contact: Alimbek Jumamuratov", "Mas’ul shaxs: Alimbek Jumamuratov", "Ответственный: Алимбек Жумамуратов"),
 free=("Biypul", "Free", "Bepul", "Бесплатно"),
)
def reg_point(i):
    li = "".join(f"<li>{x}</li>" for x in REG["items"][i])
    return (f'<div class="card iereg"><span class="iefree">{REG["free"][i]}</span><h2>{REG["h"][i]}</h2><p>{REG["p"][i]}</p><ul>{li}</ul>'
            f'<p class="iewho"><b>{REG["who"][i]}</b> · <a href="tel:+998906543398">+998 90 654 33 98</a> · <a href="mailto:ixm013@piima.uz">ixm013@piima.uz</a></p></div>')

def body(lang, i):
    import json, html
    bsel = lambda sel, lo=3.0: "".join(f'<option value="{v / 2}"{" selected" if v / 2 == sel else ""}>{str(v / 2).replace(".", "," if lang != "en" else ".")}</option>' for v in range(int(lo * 2), 19))
    parts = "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in S["parts"][i])
    tips = "".join(f'<div class="card"><h3>{n}</h3><ul>{"".join(f"<li>{t}</li>" for t in ts)}</ul></div>' for n, ts in S["tips"][i])
    days = "".join(f'<li><b>{d}</b><span>{p}</span></li>' for d, p in zip(S["days"][i], S["plan"][i]))
    wcol = {"kaa": 3, "en": 0, "uz": 1, "ru": 2}[lang]
    def wtr(w):
        if lang == "en": return " · ".join(w[x] for x in (1, 2, 3)), ""
        own = {"uz": 1, "ru": 2, "kaa": 3}[lang]
        return w[own], " · ".join(w[x] for x in (1, 2, 3) if x != own)
    words = "".join(f'<div class="iword card" data-k="{k}" hidden><div class="wbig">{w[0]}</div><div class="wtr">{wtr(w)[0]}</div>'
                    f'<div class="wtr2">{wtr(w)[1]}</div><p class="wex">“{w[4]}”</p></div>' for k, w in enumerate(WORDS))
    total = sum(BANDS.values())
    bars = "".join(f'<div class="py"><span>{str(b).replace(".", "," if lang != "en" else ".")}</span><div class="pbar"><i style="width:{n / max(BANDS.values()) * 100:.0f}%"></i></div><b>{n}</b></div>' for b, n in sorted(BANDS.items()))
    data = {"n": {"L": "Listening", "R": "Reading", "W": "Writing", "S": "Speaking"}, "reached": S["reached"][i], "below": S["below"][i], "focus": S["focus"][i], "w": len(WORDS), "dec": "." if lang == "en" else ","}
    return (f'<p class="lead2">{S["intro"][i]}</p>{reg_point(i)}'
            f'<h2>{S["parts_h"][i]}</h2><div class="grid2">{parts}</div><p class="note" style="margin-top:12px">{S["scale"][i]}</p>'
            f'<h2 style="margin-top:34px">{S["calc_h"][i]}</h2><p>{S["calc_p"][i]}</p>'
            f'<div class="two"><div class="card icalc">'
            f'<label>{S["f_l"][i]}<input id="il" type="number" inputmode="numeric" min="0" max="40" value="28"></label>'
            f'<label>{S["f_r"][i]}<input id="ir" type="number" inputmode="numeric" min="0" max="40" value="27"></label>'
            f'<label>{S["f_w"][i]}<select id="iw">{bsel(6.0)}</select></label>'
            f'<label>{S["f_s"][i]}<select id="is">{bsel(6.0)}</select></label>'
            f'<label>{S["f_t"][i]}<select id="it">{bsel(6.5, 5.0)}</select></label></div>'
            f'<div id="iresult" class="card iresult"><div id="ibands" class="ibands"></div><div class="iov"><span>{S["overall"][i]}</span><b id="iov">–</b></div><p id="imsg" class="imsg"></p>'
            f'<p class="note">{S["calc_note"][i]}</p></div></div>'
            f'<h2 style="margin-top:34px">{S["plan_h"][i]}</h2><p>{S["plan_p"][i]}</p><ul class="iplan card">{days}</ul>'
            f'<h2 style="margin-top:34px">{S["tips_h"][i]}</h2><div class="grid2">{tips}</div>'
            f'<h2 style="margin-top:34px">{S["word_h"][i]}</h2>{words}'
            f'<h2 style="margin-top:34px">{S["res_h"][i]}</h2><p>{S["res_p"][i].format(n=total)}</p><div class="card" style="--sc:#0b5f78">{bars}</div>'
            f'<h2 style="margin-top:34px">{S["links_h"][i]}</h2><div class="linklist"><a href="https://ielts.org" rel="noopener">ielts.org — {S["link1"][i]} →</a>'
            f'<a href="https://www.britishcouncil.org/exam/ielts" rel="noopener">britishcouncil.org — {S["link2"][i]} →</a></div><p class="note">{S["links_note"][i]}</p>'
            f'<script id="ieltsdata" type="application/json">{json.dumps(data, ensure_ascii=False)}</script><script>{JS}</script>')
