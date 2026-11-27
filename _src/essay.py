import json
NAME = ("Esse jazıw sheberxanası", "Essay workshop", "Esse yozish ustaxonasi", "Мастерская эссе")
TAB = ("Esse", "Essay", "Esse", "Эссе")
DESC = ("Jeke esse jazıwǵa qádem-qádem járdem: oy tabıw, dúzilis, sóz sanawıshı, tekseriw dizimi hám tayın bolmaǵan basllamalar. Tek ózińiz jazıń.",
        "Step-by-step help for your personal essay: finding your story, structure, a live word counter, a self-review checklist and openings to avoid. You write it yourself.",
        "Shaxsiy esse yozishga bosqichma-bosqich yordam: hikoyani topish, tuzilma, jonli so‘z hisoblagich, tekshiruv ro‘yxati va undan qochiladigan boshlanishlar. Faqat o‘zingiz yozing.",
        "Пошаговая помощь с личным эссе: поиск своей истории, структура, счётчик слов, чек-лист самопроверки и штампы, которых стоит избегать. Пишете вы сами.")
def T(a, b, c, d): return (a, b, c, d)
UI = {
 "intro": T("Esse — komissiya sizdi tanıytuǵın birden-bir orın. Oqıw bahaları hám testler sizdiń ne islegenińizdi aytadı, al esse sizdiń kim ekenińizdi aytadı. Tómendegi qádemler arqalı óz hikayańızdı tabıń.",
            "The essay is the one place where the admissions reader hears your voice. Grades and tests show what you did; the essay shows who you are. Use the steps below to find your own story.",
            "Esse — komissiya sizni tanishi mumkin bo‘lgan yagona joy. Baholar va testlar nima qilganingizni, esse esa kimligingizni ko‘rsatadi. Quyidagi qadamlar bilan o‘z hikoyangizni toping.",
            "Эссе — единственное место, где комиссия слышит ваш голос. Оценки и тесты показывают, что вы сделали; эссе — кто вы. Пройдите шаги ниже и найдите свою историю."),
 "own": T("Esseni tek ózińiz jazıń. Basqa birew (yamasa jasalma intellekt) jazǵan esse universitetler tárepinen tabılıwı hám arzańızdı biykarlawı múmkin. Ózińizdiń sózlerińiz, ózińizdiń awazıńız — eń jaqsı esse sol.",
          "Write the essay yourself. An essay written by someone else, or by an AI tool, can be spotted and can get your application rejected. Your own words and voice make the best essay.",
          "Esseni faqat o‘zingiz yozing. Boshqa odam yoki sun’iy intellekt yozgan esse universitetlar tomonidan aniqlanishi va arizangiz rad etilishiga olib kelishi mumkin. O‘z so‘zlaringiz va ovozingiz — eng yaxshi esse.",
          "Пишите эссе сами. Эссе, написанное другим человеком или ИИ, могут распознать, и заявку могут отклонить. Ваши слова и ваш голос — лучшее эссе."),
 "h_steps": T("5 qádemde hikayańızdı tabıń", "Find your story in 5 steps", "5 qadamda hikoyangizni toping", "Найдите свою историю за 5 шагов"),
 "steps_p": T("Hár qádemge qısqasha jawap jazıń. Jazǵanlarıńız usı telefonda saqlanadı hám hesh kimge jiberilmeydi.", "Write short answers to each step. What you type is saved on this phone only and is not sent anywhere.", "Har bir qadamga qisqa javob yozing. Yozganlaringiz faqat shu telefonda saqlanadi va hech kimga yuborilmaydi.", "Напишите короткие ответы на каждый шаг. Всё, что вы вводите, хранится только на этом телефоне и никуда не отправляется."),
 "S": (
  (T("1. Bir lahza", "1. A single moment", "1. Bitta lahza", "1. Один момент"),
   T("Eslep qalǵan bir ǵana waqıya: bir kún, bir sóylesiw, bir qáte yamasa sheshim. Kishkene hám anıq bolsın.", "Pick one small, specific moment: a day, a conversation, a mistake, a decision. Small and concrete beats big and vague.", "Bitta aniq lahza: bir kun, suhbat, xato yoki qaror. Kichik va aniq bo‘lsin.", "Выберите один конкретный момент: день, разговор, ошибку или решение. Маленький и точный лучше большого и расплывчатого."),
   T("Kim? Qayerde? Ne bolıp atır edi?", "Who was there? Where? What was happening?", "Kim bor edi? Qayerda? Nima bo‘layotgan edi?", "Кто был рядом? Где? Что происходило?")),
  (T("2. Ne ózgerdi", "2. What changed", "2. Nima o‘zgardi", "2. Что изменилось"),
   T("Sol lahzadan keyin ózińizdi yamasa kóz-qarasıńızdı ne ózgertti? Dáslep ne oyladıńız, keyin ne túsindińiz?", "What did that moment change in you or in how you see things? What did you think before, and what do you understand now?", "Shu lahzadan keyin o‘zingizda yoki qarashlaringizda nima o‘zgardi? Avval nima deb o‘ylagansiz, endi nimani tushundingiz?", "Что этот момент изменил в вас или во взглядах? Что вы думали раньше и что понимаете теперь?"),
   T("Ilgeri men … dep oylaytuǵın edim, endi bolsa …", "I used to think …, now I know …", "Avval men … deb o‘ylardim, endi esa …", "Раньше я думал …, теперь понимаю …")),
  (T("3. Anıq detallar", "3. Concrete details", "3. Aniq detallar", "3. Конкретные детали"),
   T("Sezim emes, anıq detallar: at, san, iyis, sóz, nárse. Olar esseńizdi tiriltedi.", "Not feelings but facts you can see: names, numbers, smells, words, objects. Details make an essay come alive.", "His-tuyg‘u emas, aniq detallar: ism, son, hid, so‘z, narsa. Detallar esseni jonlantiradi.", "Не чувства, а видимые детали: имена, числа, запахи, слова, предметы. Детали оживляют эссе."),
   T("3 anıq detal jazıń (san, at, nárse).", "Write 3 concrete details (a number, a name, an object).", "3 ta aniq detal yozing (son, ism, narsa).", "Запишите 3 конкретные детали (число, имя, предмет).")),
  (T("4. Maqsetke baylanıs", "4. Link to your goal", "4. Maqsadga bog‘lanish", "4. Связь с целью"),
   T("Bul hikaya sizdi tańlaǵan baǵdarıńızǵa hám keleshekke qalay alıp baradı? Zorlap baylamań; haqıyqıy baylanıs bolsa jetkilikli.", "How does this story lead toward the field you chose and the person you want to become? Do not force it; one honest link is enough.", "Bu hikoya sizni tanlagan yo‘nalishingiz va kelajagingizga qanday olib boradi? Majburlab bog‘lamang; bitta samimiy bog‘lanish yetarli.", "Как эта история ведёт к выбранной специальности и к тому, кем вы хотите стать? Не тяните за уши — достаточно одной честной связи."),
   T("Sol sebepli men … oqıǵım keledi.", "That is why I want to study …", "Shuning uchun men … o‘qishni xohlayman.", "Поэтому я хочу изучать …")),
  (T("5. Birinshi nusqa", "5. First draft", "5. Birinchi nusxa", "5. Черновик"),
   T("Mukemmel bolıwdı oylamań. Birinshi nusqanı tez jazıń, keyin qayta islep shıǵıń. Tómende sóz sanawıshı bar.", "Do not aim for perfect. Write a fast first draft, then rewrite. A live counter is below.", "Mukammal bo‘lishini o‘ylamang. Birinchi nusxani tez yozing, keyin qayta ishlang. Quyida so‘z hisoblagich bor.", "Не стремитесь к идеалу. Быстро напишите черновик, потом перепишите. Ниже есть счётчик слов."),
   T("", "", "", ""))),
 "h_draft": T("Esse jazıw hám sanawısh", "Draft and counter", "Esse va hisoblagich", "Черновик и счётчик"),
 "lim": T("Shegara", "Limit", "Chegara", "Лимит"), "L1": T("Common App: 650 sóz", "Common App: 650 words", "Common App: 650 so‘z", "Common App: 650 слов"), "L2": T("UCAS: 4 000 belgi", "UCAS: 4,000 characters", "UCAS: 4 000 belgi", "UCAS: 4 000 знаков"), "L3": T("Qosımsha: 250 sóz", "Supplement: 250 words", "Qo‘shimcha: 250 so‘z", "Дополнительное: 250 слов"),
 "words": T("sóz", "words", "so‘z", "слов"), "chars": T("belgi", "characters", "belgi", "знаков"), "sent": T("gáp", "sentences", "gap", "предл."), "avg": T("gáptiń ortasha uzınlıǵı", "average sentence", "o‘rtacha gap uzunligi", "средняя длина предложения"),
 "over": T("Shegaradan asıp ketti", "Over the limit", "Chegaradan oshdi", "Превышен лимит"), "ok": T("Shegara ishinde", "Within the limit", "Chegara ichida", "В пределах лимита"),
 "ph": T("Esseńizdi usı jerge jazıń yamasa qoyıń…", "Write or paste your draft here…", "Esseni shu yerga yozing yoki qo‘ying…", "Пишите или вставляйте черновик здесь…"),
 "clich": T("Qaytalanatuǵın klishe tabıldı", "Clichés found", "Klishelar topildi", "Найдены штампы"), "clean": T("Belgili klishe tabılmadı. Jaqsı!", "No common clichés found. Good!", "Mashhur klishelar topilmadi. Yaxshi!", "Распространённых штампов не найдено. Отлично!"),
 "long": T("Uzın gáplerdi qısqartıp kóriń", "Try shortening the long sentences", "Uzun gaplarni qisqartirib ko‘ring", "Попробуйте сократить длинные предложения"),
 "h_rev": T("Óz-ózińizdi tekseriw dizimi", "Self-review checklist", "O‘z-o‘zini tekshirish ro‘yxati", "Чек-лист самопроверки"),
 "rev": (T("Birinshi 2–3 gápte anıq waqıya yamasa sahna bar", "The first 2–3 sentences open with a specific scene or moment", "Dastlabki 2–3 gapda aniq voqea yoki sahna bor", "В первых 2–3 предложениях есть конкретная сцена"),
         T("Esse bir bas oyǵa iye (bir neshe temanı aralastırmaǵan)", "The essay has one main idea, not five", "Esse bitta asosiy g‘oyaga ega", "У эссе одна главная мысль, а не пять"),
         T("«Aytıp beriw» emes, «kórsetiw»: sezimlerdi detallar menen kórsettim", "I show rather than tell: feelings are carried by details", "«Aytish» emas, «ko‘rsatish»: his-tuyg‘ularni detallar bilan ko‘rsatdim", "Я показываю, а не рассказываю: чувства переданы деталями"),
         T("Ózgeris hám sabaq anıq kórinedi", "The change in me and the lesson are clear", "O‘zgarish va saboq aniq ko‘rinadi", "Изменение и вывод хорошо видны"),
         T("Maqsetime hám baǵdarıma haqıyqıy baylanıs bar", "There is an honest link to my goal and field", "Maqsad va yo‘nalishimga samimiy bog‘lanish bor", "Есть честная связь с моей целью и специальностью"),
         T("Tek ózimniń awazım: sózler tábiyiy, jasalma uzın emes", "It sounds like me: natural words, no fake fancy ones", "Faqat o‘z ovozim: tabiiy so‘zlar, soxta murakkab emas", "Звучит как я: естественные слова, без искусственной вычурности"),
         T("Resume (CV) dizimin qaytalamaydı", "It does not just repeat my CV", "CV ro‘yxatini takrorlamaydi", "Не повторяет резюме"),
         T("Keminde 2 adam oqıdı (muǵallim, másláhátshi) hám kerekli ózgerisler kirgizildi", "At least two people read it (teacher, counsellor) and I made changes", "Kamida 2 kishi o‘qidi (o‘qituvchi, maslahatchi) va o‘zgarishlar kiritildi", "Минимум два человека прочитали (учитель, консультант), и я внёс правки"),
         T("Imla hám grammatika qátelerin tekserdim, daýıslap oqıdım", "I proofread for spelling and grammar and read it aloud", "Imlo va grammatikani tekshirdim, ovoz chiqarib o‘qidim", "Проверил орфографию и грамматику, прочитал вслух")),
 "h_avoid": T("Belgili klishelerden qashıń", "Openings and phrases to avoid", "Mashhur klishelardan qoching", "Каких штампов избегать"),
 "avoid_p": T("Komissiya mıńlaǵan esse oqıydı. Tómendegilerdi kóp ret kórgen, sonlıqtan esseńiz unamsız bolıp qaladı.", "Readers see thousands of essays. These lines show up constantly, so they make yours blend in.", "Komissiya minglab esse o‘qiydi. Quyidagilarni ko‘p marta ko‘rgan, shuning uchun esseyingiz ko‘zga tashlanmaydi.", "Комиссия читает тысячи эссе. Эти фразы встречаются постоянно, поэтому ваше сливается с остальными."),
 "bad": ("since childhood", "I have always been passionate", "in today’s world", "Webster’s dictionary defines", "ever since I was young", "my dream is to help people", "this experience taught me", "I learned that hard work", "changed my life forever", "make the world a better place"),
 "h_ex": T("Basllama mısalları", "Opening examples", "Boshlanish misollari", "Примеры начал"),
 "weak": T("Ázzi basllama", "Weak opening", "Zaif boshlanish", "Слабое начало"), "strong": T("Kúshli basllama", "Stronger opening", "Kuchli boshlanish", "Сильное начало"),
 "EX": (("Since childhood I have been passionate about science.", "The first time the lab’s only microscope broke, I fixed it with a hairpin and a borrowed screwdriver."),
        ("I want to become an engineer to help my country.", "My grandfather’s water pump stopped every August, and every August I stood beside him, handing him the wrong wrench."),
        ("Hard work is the key to success.", "I failed the maths olympiad twice. The third time, I brought a notebook of every mistake I had made.")),
 "ex_n": T("Mısallar oyda shıǵarılǵan: óz hikayańızdı jazıń.", "These examples are invented: write your own story.", "Misollar o‘ylab topilgan: o‘z hikoyangizni yozing.", "Примеры вымышлены: пишите свою историю."),
 "h_time": T("8 hápte rejesi", "8-week plan", "8 haftalik reja", "План на 8 недель"),
 "time": (T("1–2: oy, 5 qádem, 2–3 hikaya variantı", "Weeks 1–2: brainstorm, the 5 steps, 2–3 story options", "1–2-hafta: fikr, 5 qadam, 2–3 hikoya varianti", "Недели 1–2: идеи, 5 шагов, 2–3 варианта истории"),
          T("3–4: birinshi nusqa (shegarasız)", "Weeks 3–4: first draft, ignore the word limit", "3–4-hafta: birinchi nusxa (chegarasiz)", "Недели 3–4: черновик без оглядки на лимит"),
          T("5–6: qayta jazıw, qısqartıw, 2 adamǵa oqıtıw", "Weeks 5–6: rewrite, cut, show it to 2 readers", "5–6-hafta: qayta yozish, qisqartirish, 2 kishiga o‘qitish", "Недели 5–6: переписать, сократить, дать прочитать двоим"),
          T("7: sońǵı tekseriw, daýıslap oqıw", "Week 7: final polish, read aloud", "7-hafta: yakuniy tekshiruv, ovoz chiqarib o‘qish", "Неделя 7: финальная вычитка, чтение вслух"),
          T("8: jiberiw (múddetten keminde 1 hápte aldın)", "Week 8: submit, at least a week before the deadline", "8-hafta: yuborish (muddatdan kamida 1 hafta oldin)", "Неделя 8: отправка минимум за неделю до дедлайна")),
 "go": T("Common App sorawları", "Common App prompts", "Common App mavzulari", "Темы Common App"), "go2": T("UCAS jeke bayanat", "UCAS personal statement", "UCAS shaxsiy bayonot", "Личное заявление UCAS"),
 "help": T("Másláhátshige oqıtıp kóriń", "Show a draft to the counsellor", "Maslahatchiga o‘qitib ko‘ring", "Покажите черновик консультанту"),
 "share": T("Nusqanı kóshiriw", "Copy draft", "Nusxa olish", "Скопировать черновик"), "copied": T("Kóshirildi", "Copied", "Nusxalandi", "Скопировано"), "reset": T("Tazalaw", "Clear all", "Tozalash", "Очистить"), "resetq": T("Barlıq jazıwlar óshiriledi. Dawam etemiz be?", "This clears everything you wrote. Continue?", "Barcha yozuvlar o‘chiriladi. Davom etamizmi?", "Всё написанное будет удалено. Продолжить?"),
 "foot": T("Esse haqqındaǵı keńesler ulıwma. Common App esse sheklewi 650 sóz, UCAS jeke bayanatı 4 000 belgi; ayırım universitetlerdiń qosımsha esseleri ózgeshe bolıwı múmkin — hár bir universitettiń betin tekseriń.",
           "These tips are general. The Common App essay limit is 650 words and the UCAS personal statement is 4,000 characters; supplemental essays differ by university, so check each one’s page.",
           "Bu maslahatlar umumiy. Common App esse chegarasi 650 so‘z, UCAS shaxsiy bayonoti 4 000 belgi; qo‘shimcha esselar universitetga qarab farq qiladi — har birining sahifasini tekshiring.",
           "Советы общие. Лимит эссе Common App — 650 слов, личного заявления UCAS — 4 000 знаков; дополнительные эссе у вузов отличаются, проверяйте страницу каждого."),
}
def body(i, tabs_html, href):
    S = [dict(t=s[0][i], p=s[1][i], h=s[2][i]) for s in UI["S"]]
    data = {"ui": {k: v[i] for k, v in UI.items() if isinstance(v, tuple) and len(v) == 4 and all(isinstance(x, str) for x in v)}}
    data.update(S=S, rev=[r[i] for r in UI["rev"]], bad=list(UI["bad"]), ex=[list(e) for e in UI["EX"]], time=[t[i] for t in UI["time"]])
    js = ES_JS.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    links = f'<div class="btns"><a class="btn p" href="{href("abroad/commonapp/")}">{UI["go"][i]}</a><a class="btn s" href="{href("abroad/ucas/")}">{UI["go2"][i]}</a></div>'
    return (f'{tabs_html}<p class="lead2">{UI["intro"][i]}</p><div class="card esown">{UI["own"][i]}</div><section id="es"></section>{links}<p class="note">{UI["foot"][i]}</p><script>{js}</script>')
ES_JS = r"""(function(){var D=__DATA__,U=D.ui,$=function(i){return document.getElementById(i)},root=$('es');
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;')}
var st={n:['','','','',''],d:'',lim:0,rv:{}};try{var o=JSON.parse(localStorage.getItem('esS')||'{}');for(var k in o)st[k]=o[k]}catch(e){}
function save(){try{localStorage.setItem('esS',JSON.stringify(st))}catch(e){}}
var LIM=[{w:650},{c:4000},{w:250}];
function stats(t){var w=(t.trim().match(/\S+/g)||[]).length,c=t.length,s=(t.match(/[^.!?]+[.!?]+/g)||[]).length;return{w:w,c:c,s:s,a:s?Math.round(w/s):0}}
function cl(t){var l=t.toLowerCase().replace(/\u2019/g,"'"),r=[];D.bad.forEach(function(b){var n=l.split(b.toLowerCase().replace(/\u2019/g,"'")).length-1;if(n)r.push(b+(n>1?' ×'+n:''))});return r}
function steps(){return D.S.map(function(s,ix){return '<div class="esstep card"><h3><span class="esn">'+(ix+1)+'</span>'+esc(s.t.replace(/^\d\.\s*/,''))+'</h3><p>'+esc(s.p)+'</p>'+(ix<4?'<textarea data-s="'+ix+'" rows="3" placeholder="'+esc(s.h)+'">'+esc(st.n[ix]||'')+'</textarea>':'')+'</div>'}).join('')}
function meter(){var t=st.d,s=stats(t),L=LIM[st.lim],use=L.w?s.w:s.c,max=L.w||L.c,p=Math.min(100,use/max*100),over=use>max,cs=cl(t);
var h='<div class="esmeter"><div class="esbar"><i class="'+(over?'over':'')+'" style="width:'+p+'%"></i></div><p><b>'+use+' / '+max+'</b> '+(L.w?U.words:U.chars)+' · <span class="'+(over?'bad':'good')+'">'+(over?U.over:U.ok)+'</span></p><p class="note">'+s.w+' '+U.words+' · '+s.c+' '+U.chars+' · '+s.s+' '+U.sent+(s.a?' · '+U.avg+': '+s.a:'')+'</p>';
if(s.a>28)h+='<p class="note">⚠ '+esc(U.long)+'</p>';
if(t.trim())h+=cs.length?'<p class="esbadl">⚠ '+esc(U.clich)+': <b>'+cs.map(esc).join(', ')+'</b></p>':'<p class="esgood">✓ '+esc(U.clean)+'</p>';
return h+'</div>'}
function rev(){var n=D.rev.length,d=D.rev.filter(function(_,ix){return st.rv[ix]}).length;
return '<div class="satprog"><i style="width:'+(d/n*100)+'%"></i></div><p class="note">'+d+' / '+n+'</p><ul class="satck">'+D.rev.map(function(t,ix){return '<li class="'+(st.rv[ix]?'on':'')+'"><label><input type="checkbox" data-r="'+ix+'"'+(st.rv[ix]?' checked':'')+'><span class="ckbx"></span><span>'+esc(t)+'</span></label></li>'}).join('')+'</ul>'}
function render(){root.innerHTML='<h2>'+U.h_steps+'</h2><p>'+U.steps_p+'</p>'+steps()
+'<h2>'+U.h_draft+'</h2><div class="esl">'+[U.L1,U.L2,U.L3].map(function(l,ix){return '<button type="button" class="satc'+(st.lim==ix?' on':'')+'" data-l="'+ix+'">'+esc(l)+'</button>'}).join('')+'</div>'
+'<textarea id="esdraft" class="esdraft" rows="12" placeholder="'+esc(U.ph)+'">'+esc(st.d)+'</textarea><div id="esmeter">'+meter()+'</div>'
+'<div class="ckbtn"><button type="button" class="fc" data-a="copy">'+U.share+'</button><button type="button" class="fc" data-a="reset">'+U.reset+'</button><span class="cktoast" id="estoast" hidden>'+U.copied+'</span></div>'
+'<h2>'+U.h_rev+'</h2><div id="esrev">'+rev()+'</div>'
+'<h2>'+U.h_avoid+'</h2><p>'+U.avoid_p+'</p><div class="esbad">'+D.bad.map(function(b){return '<span>'+esc(b)+'</span>'}).join('')+'</div>'
+'<h2>'+U.h_ex+'</h2>'+D.ex.map(function(e){return '<div class="esex"><div class="w"><small>'+U.weak+'</small><p>'+esc(e[0])+'</p></div><div class="s"><small>'+U.strong+'</small><p>'+esc(e[1])+'</p></div></div>'}).join('')+'<p class="note">'+U.ex_n+'</p>'
+'<h2>'+U.h_time+'</h2><ol class="satplan">'+D.time.map(function(t,ix){var p=t.split(':');return '<li><span class="satpw">'+(ix+1)+'</span><div><b>'+esc(p[0])+'</b><p>'+esc(p.slice(1).join(':').trim())+'</p></div></li>'}).join('')+'</ol>'
+'<div class="card esown">'+U.help+'</div>'}
root.addEventListener('input',function(e){var t=e.target;if(t.id=='esdraft'){st.d=t.value;save();$('esmeter').innerHTML=meter()}else if(t.dataset&&t.dataset.s!=null){st.n[+t.dataset.s]=t.value;save()}});
root.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
if(b.dataset.l!=null){st.lim=+b.dataset.l;save();var c=root.querySelectorAll('[data-l]');for(var i=0;i<c.length;i++)c[i].classList.toggle('on',i==st.lim);$('esmeter').innerHTML=meter()}
else if(b.dataset.a=='copy'){var t=st.d;if(navigator.clipboard)navigator.clipboard.writeText(t).then(function(){var x=$('estoast');x.hidden=false;setTimeout(function(){x.hidden=true},1600)})}
else if(b.dataset.a=='reset'){if(confirm(U.resetq)){st={n:['','','','',''],d:'',lim:0,rv:{}};save();render()}}});
root.addEventListener('change',function(e){var c=e.target;if(c.dataset&&c.dataset.r!=null){if(c.checked)st.rv[c.dataset.r]=1;else delete st.rv[c.dataset.r];save();$('esrev').innerHTML=rev()}});
render()})();"""
