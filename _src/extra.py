# Extra pages: admission/, parents/, documents/  (texts in kaa, en, uz, ru order)
import os, re

NAME = {
 "parents/": ("Ata-analar ushın", "For parents", "Ota-onalar uchun", "Родителям"),
 "documents/": ("Hújjetler", "Documents", "Hujjatlar", "Документы"),
}
DESC = {
 "admission/": ("Kegeyli qánigelestirilgen mektebine qabıllaw: 5- hám 7-klass, onlayn arza, kiriw imtihanı hám kerekli hújjetler.",
                "Admission to Kegeyli specialized school: grades 5 and 7, online application, entrance test and required documents.",
                "Kegeyli ixtisoslashtirilgan maktabiga qabul: 5- va 7-sinf, onlayn ariza, kirish imtihoni va kerakli hujjatlar.",
                "Приём в Кегейлийскую специализированную школу: 5 и 7 классы, онлайн-заявление, вступительный тест и документы."),
 "parents/": ("Ata-analar ushın kerekli maǵlıwmat: sabaq hám jumıs waqtı, qońıraw kestesi, asxana hám baylanıs.",
              "Useful information for parents: school days and hours, bell schedule, canteen and contacts.",
              "Ota-onalar uchun kerakli ma’lumot: dars va ish vaqti, qo‘ng‘iroq jadvali, oshxona va aloqa.",
              "Полезная информация для родителей: учебные дни и часы работы, расписание звонков, столовая, контакты."),
 "documents/": ("Sabaq kesteleri (PDF), rásmiy siltemeler hám mektep hújjetleri.",
                "Timetables (PDF), official links and school documents.",
                "Dars jadvallari (PDF), rasmiy havolalar va maktab hujjatlari.",
                "Расписание (PDF), официальные ссылки и документы школы."),
}
X = {
 "a_cards": (
  (("5-klass", "Anıq pánler baǵdarı"), ("7-klass", "Tábiyiy pánler baǵdarı"), ("Bos orınlar", "Test tiykarında")),
  (("Grade 5", "Exact sciences track"), ("Grade 7", "Natural sciences track"), ("Vacancies", "Based on a test")),
  (("5-sinf", "Aniq fanlar yo‘nalishi"), ("7-sinf", "Tabiiy fanlar yo‘nalishi"), ("Bo‘sh o‘rinlar", "Test asosida")),
  (("5 класс", "Направление точных наук"), ("7 класс", "Направление естественных наук"), ("Вакантные места", "По результатам теста"))),
 "a_steps": ("Qalay arza tapsırıladı", "How to apply", "Qanday ariza topshiriladi", "Как подать заявление"),
 "a_apply": ("Onlayn arza tapsırıw", "Apply online", "Onlayn ariza topshirish", "Подать заявление"),
 "a_faq": ("Sorawlar", "Questions", "Savollar", "Вопросы"),
 "p_cards": (
  (("Sabaq kúnleri", "Dúyshembi–juma"), ("Mektep jumıs waqtı", "Dúyshembi–shembi, 08:30–17:00"), ("Awqatlanıw", "Mektepte óz asxanası bar"), ("Jataqxana", "Joq — mektep internat emes")),
  (("School days", "Monday–Friday"), ("Office hours", "Monday–Saturday, 08:30–17:00"), ("Meals", "The school has its own canteen"), ("Dormitory", "None — not a boarding school")),
  (("Dars kunlari", "Dushanba–juma"), ("Maktab ish vaqti", "Dushanba–shanba, 08:30–17:00"), ("Ovqatlanish", "Maktabning o‘z oshxonasi bor"), ("Yotoqxona", "Yo‘q — maktab-internat emas")),
  (("Учебные дни", "Понедельник–пятница"), ("Часы работы школы", "Понедельник–суббота, 08:30–17:00"), ("Питание", "В школе есть собственная столовая"), ("Общежитие", "Нет — школа не является интернатом"))),
 "bells_h": ("Qońıraw kestesi", "Bell schedule", "Qo‘ng‘iroq jadvali", "Расписание звонков"),
 "lesson": ("{n}-sabaq", "Lesson {n}", "{n}-dars", "{n}-й урок"),
 "links_h": ("Paydalı siltemeler", "Quick links", "Foydali havolalar", "Полезные ссылки"),
 "tg": ("Telegram kanalı", "Telegram channel", "Telegram kanali", "Telegram-канал"),
 "touch_h": ("Baylanısıw", "Get in touch", "Bog‘lanish", "Связаться"),
 "call": ("Qońıraw qılıw", "Call", "Qo‘ng‘iroq qilish", "Позвонить"),
 "d_h1": ("Sabaq kesteleri (PDF)", "Timetables (PDF)", "Dars jadvallari (PDF)", "Расписание (PDF)"),
 "d_p1": ("Klass yamasa muǵallim kestesin júklep alıp, chop etiń.", "Download and print a class or teacher timetable.", "Sinf yoki o‘qituvchi jadvalini yuklab oling va chop eting.", "Скачайте и распечатайте расписание класса или учителя."),
 "d_cls": ("Klasslar", "Classes", "Sinflar", "Классы"),
 "d_tch": ("Muǵallimler", "Teachers", "O‘qituvchilar", "Учителя"),
 "d_h2": ("Rásmiy siltemeler", "Official links", "Rasmiy havolalar", "Официальные ссылки"),
 "d_gov": ("Mámleketlik xızmetler portalı", "Public services portal", "Davlat xizmatlari portali", "Портал госуслуг"),
 "d_ariza": ("Onlayn arza tapsırıw", "Online application", "Onlayn ariza topshirish", "Подача онлайн-заявления"),
 "d_hot": ("PIIMA isenim telefonı", "PIIMA hotline", "PIIMA ishonch telefoni", "Телефон доверия PIIMA"),
 "d_h3": ("Mektep hújjetleri", "School documents", "Maktab hujjatlari", "Документы школы"),
 "d_p3": ("Mektep nızamı, qaǵıydalar hám esabatlar usı jerde járiyalanadı.", "The school charter, rules and reports will be published here.", "Maktab nizomi, qoidalar va hisobotlar shu yerda e’lon qilinadi.", "Устав школы, правила и отчёты будут опубликованы здесь."),
}
HOT = "+998 71 207 40 48"

def _pdf_label(f):
    s = f[:-4]
    if s.startswith("c-"):
        a = s[2:].split("-"); return f"{a[0]}-{a[1].upper()}"
    a = s[2:].split("-"); return a[0].capitalize() + " " + a[1].upper()

_DI = lambda d: f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
DOC_ICONS = [  # photo, birth certificate, parent ID, phone
 (_DI('<rect x="3" y="5" width="18" height="14" rx="2.500"/><circle cx="9" cy="11" r="2.200"/><path d="M4.500 18c1-2.500 3-3.500 4.500-3.500s3.500 1 4.500 3.500M15 10h3M15 13.500h2.500"/>'), "#2a7fd1"),
 (_DI('<path d="M7 3h8l4 4v14H7z"/><path d="M15 3v4h4M10 12h6M10 16h6"/><circle cx="9" cy="9" r=".6"/>'), "#d97706"),
 (_DI('<rect x="3" y="5" width="18" height="14" rx="2.500"/><circle cx="8.500" cy="11" r="2"/><path d="M5.500 16c.6-1.500 1.700-2 3-2s2.400.5 3 2M14 10h4M14 13.500h3"/>'), "#7c3aed"),
 (_DI('<rect x="7" y="2.500" width="10" height="19" rx="2.500"/><path d="M11 18.500h2"/>'), "#2f8f5b"),
]
_INFO = _DI('<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/>')
_LIST = _DI('<rect x="5" y="3.500" width="14" height="17" rx="2"/><path d="M8.500 9l1.500 1.500L12.500 8M8.500 15l1.500 1.500 2.500-2.500M15 9.500h1.500M15 15.500h1.500"/>')
AX = {
 "strip": [  # (big, small) per language
  [("5", "klass · Anıq pánler"), ("7", "klass · Tábiyiy pánler"), ("May–Iyun", "onlayn arza"), ("Iyun–Iyul", "jazba test")],
  [("5", "grade · Exact sciences"), ("7", "grade · Natural sciences"), ("May–Jun", "online application"), ("Jun–Jul", "written test")],
  [("5", "sinf · Aniq fanlar"), ("7", "sinf · Tabiiy fanlar"), ("May–Iyun", "onlayn ariza"), ("Iyun–Iyul", "yozma test")],
  [("5", "класс · Точные науки"), ("7", "класс · Естественные науки"), ("Май–Июнь", "онлайн-заявка"), ("Июнь–Июль", "письменный тест")],
 ],
 "cta_h": ("Qabıllawǵa tayarsız ba?", "Ready to apply?", "Qabulga tayyormisiz?", "Готовы подать заявку?"),
 "cta_p": ("Arzanı rásmiy portal arqalı tapsırıń. Sorawıńız bolsa, bizge jazıń yamasa qońıraw qılıń.", "Submit your application on the official portal. If you have questions, message or call us.", "Arizani rasmiy portal orqali topshiring. Savollaringiz bo‘lsa, bizga yozing yoki qo‘ng‘iroq qiling.", "Подайте заявку на официальном портале. Если есть вопросы, напишите или позвоните нам."),
}

AF = {
 "h": ("Onlayn qabıllaw arzası", "Online admission request", "Onlayn qabul arizasi", "Онлайн-заявка на приём"),
 "p": ("Perzentińizdi mektepke jazdırıw ushın tómendegi formanı toltırıń. Administraciya siz benen baylanısadı.", "Fill in the form below to register your child's interest. The school administration will contact you.", "Farzandingizni maktabimizga yozdirish uchun quyidagi shaklni to‘ldiring. Ma’muriyat siz bilan bog‘lanadi.", "Заполните форму ниже, чтобы записать ребёнка. Администрация школы свяжется с вами."),
 "note": ("Bul — dáslepki jazılıw. Rásmiy arza {a} arqalı tapsırıladı.", "This is a pre-registration. The official application is submitted via {a}.", "Bu — dastlabki yozilish. Rasmiy ariza {a} orqali topshiriladi.", "Это предварительная запись. Официальная заявка подаётся через {a}."),
 "name": ("Oqıwshınıń tolıq atı-jóni", "Student's full name", "O‘quvchining to‘liq ismi", "ФИО ученика"),
 "phone": ("Telefon nomeri", "Phone number", "Telefon raqami", "Номер телефона"),
 "grade": ("Qabıl etiletuǵın klass", "Grade applying for", "Qabul qilinadigan sinf", "Класс поступления"),
 "pick": ("Klassıńdı tańlań", "Select grade", "Sinfni tanlang", "Выберите класс"),
 "msg": ("Qosımsha xabar (ixtiyariy)", "Additional message (optional)", "Qo‘shimcha xabar (ixtiyoriy)", "Дополнительное сообщение (необязательно)"),
 "send": ("Arzanı jiberiw", "Send request", "Arizani yuborish", "Отправить заявку"),
 "need": ("Atı-jóni hám telefon nomerin hám klassın kiritiń.", "Please enter the name, phone number and grade.", "Ism, telefon raqami va sinfni kiriting.", "Укажите ФИО, телефон и класс."),
}
def apply_form(i, ctx):
    opts = "".join(f'<option value="{g}">{g}</option>' for g in range(5, 12))
    note = AF["note"][i].format(a='<a href="https://ariza.piima.uz" rel="noopener">ariza.piima.uz</a>')
    import json
    fx = json.dumps(ctx["FX"], ensure_ascii=False); need = json.dumps(AF["need"][i], ensure_ascii=False)
    return (f'<form id="af" class="card aform" novalidate><h2>{AF["h"][i]}</h2><p>{AF["p"][i]}</p><p class="anote">{note}</p>'
            f'<label for="an">{AF["name"][i]}</label><input id="an" autocomplete="name" required>'
            f'<label for="ap">{AF["phone"][i]}</label><input id="ap" type="tel" autocomplete="tel" placeholder="+998 90 123 45 67" required>'
            f'<label for="ag">{AF["grade"][i]}</label><select id="ag" required><option value="">{AF["pick"][i]}</option>{opts}</select>'
            f'<label for="am">{AF["msg"][i]}</label><textarea id="am" rows="4"></textarea>'
            f'<input type="checkbox" id="abot" tabindex="-1" autocomplete="off" style="display:none" aria-hidden="true">'
            f'<button type="submit" class="btn p">{AF["send"][i]}</button><p id="aok" role="status"></p></form>'
            f'<script>(function(){{var f=document.getElementById("af");if(!f)return;var FX={fx},KEY={json.dumps(ctx["KEY"])},ok=document.getElementById("aok");'
            f'f.addEventListener("submit",async function(e){{e.preventDefault();if(document.getElementById("abot").checked)return;'
            f'var n=f.an.value.trim(),p=f.ap.value.trim(),g=f.ag.value,m=f.am.value.trim();if(!n||!p||!g){{ok.textContent={need};return}}'
            f'var msg="Grade: "+g+(m?"\\n\\n"+m:"");var b=f.querySelector("button");'
            f'if(!KEY){{ok.textContent=FX[3];location.href="mailto:{ctx["EMAIL"]}?subject="+encodeURIComponent("Admission — "+n)+"&body="+encodeURIComponent(msg+"\\n\\n"+n+"\\n"+p);return}}'
            f'b.disabled=true;ok.textContent=FX[0];try{{var r=await fetch("https://api.web3forms.com/submit",{{method:"POST",headers:{{"Content-Type":"application/json",Accept:"application/json"}},body:JSON.stringify({{access_key:KEY,subject:"Admission request — "+n+" (grade "+g+")",from_name:"kegeyliqm.uz admission",name:n,phone:p,grade:g,message:msg,botcheck:""}})}});var j=await r.json();if(j.success){{ok.textContent=FX[1];f.reset()}}else{{ok.textContent=FX[2]}}}}catch(x){{ok.textContent=FX[2]}}b.disabled=false}})}})();</script>')

def docs_html(t):
    n = len(t["docs"])
    rows = "".join(f'<li><span class="mi" style="--mc:{DOC_ICONS[k][1]}">{DOC_ICONS[k][0]}</span><span class="dtx">{d}</span><span class="dn">{k+1}</span></li>' for k, d in enumerate(t["docs"]))
    return (f'<div class="card docscard"><div class="dhead"><span class="dbig">{_LIST}</span><h3>{t["docs_h"]}</h3><span class="dcount">{n}</span></div>'
            f'<ul class="dlist">{rows}</ul><div class="dnote">{_INFO}<p>{t["docs_note"]}</p></div></div>')

FAQ_ICONS = [  # dorm, admission, location, abroad, hours, spare
 (_DI('<path d="M3 18v-7a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v7M3 15h18M3 21v-3M21 21v-3M7 9V6h10v3"/>'), "#7c3aed"),
 (_DI('<path d="M4 20l4-1 11-11-3-3L5 16zM14 6l3 3"/>'), "#d97706"),
 (_DI('<path d="M12 21s-6-5.600-6-10.500a6 6 0 0 1 12 0C18 15.400 12 21 12 21z"/><circle cx="12" cy="10.500" r="2.200"/>'), "#d6452f"),
 (_DI('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'), "#2a7fd1"),
 (_DI('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'), "#2f8f5b"),
 (_DI('<circle cx="12" cy="12" r="9"/><path d="M9.500 9.500a2.500 2.500 0 1 1 3.500 2.300c-.7.400-1 .9-1 1.700M12 17h.01"/>'), "#0b7a8f"),
]
_CHEV = _DI('<path d="M6 9l6 6 6-6"/>')
def faq_html(t, n=None):
    L = t["faq"][:n] if n else t["faq"]
    return '<div class="faqs">' + "".join(
        f'<details class="faqi"><summary><span class="mi" style="--mc:{FAQ_ICONS[min(k,5)][1]}">{FAQ_ICONS[min(k,5)][0]}</span><span class="fq">{q}</span><span class="fchev">{_CHEV}</span></summary><p>{a}</p></details>'
        for k, (q, a) in enumerate(L)) + "</div>"

def body(sub, lang, i, t, root, ctx):
    UP = "{UP}"
    if sub == "admission/":
        cards = "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in X["a_cards"][i])
        links = {"mygov": '<a href="https://my.gov.uz" rel="noopener">my.gov.uz</a>', "ariza": '<a href="https://ariza.piima.uz" rel="noopener">ariza.piima.uz</a>'}
        steps = "".join(f"<li><div><h3>{h}</h3><p>{p.format(**links)}</p></div></li>" for h, p in t["steps"])
        docs = "".join(f"<li>{d}</li>" for d in t["docs"])
        strip = "".join(f'<div class="astat"><b>{a}</b><span>{b}</span></div>' for a, b in AX["strip"][i])
        cta = (f'<div class="card acta"><h3>{AX["cta_h"][i]}</h3><p>{AX["cta_p"][i]}</p><div class="btns"><a class="btn p" href="https://ariza.piima.uz" rel="noopener">{X["a_apply"][i]} →</a>'
               f'<a class="btn s" href="tel:{ctx["PHONE"]}">{ctx["PHONE_TXT"]}</a><a class="btn s" href="{ctx["TG"]}" rel="noopener">Telegram</a></div></div>')
        return (f'<p class="lead2">{t["adm_p"]}</p><div class="astrip">{strip}</div>'
                f'<div class="two" style="margin-top:28px"><div><h2>{X["a_steps"][i]}</h2><ol class="steps">{steps}</ol>'
                f'<div class="btns"><a class="btn p" href="https://ariza.piima.uz" rel="noopener">{X["a_apply"][i]} →</a>'
                f'<a class="btn s" href="https://my.gov.uz" rel="noopener">my.gov.uz</a></div></div>'
                f'{docs_html(t)}</div>'
                f'<h2 style="margin-top:34px">{X["a_faq"][i]}</h2>{faq_html(t, 2)}<div style="margin-top:34px">{apply_form(i, ctx)}</div>{cta}')
    if sub == "parents/":
        cards = "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in X["p_cards"][i])
        bells = "".join(f'<tr><td>{X["lesson"][i].format(n=n)}</td><td><b>{a}</b> – {b}</td></tr>' for n, (a, b) in enumerate(ctx["BELLS"], 1))
        c = t["contact_labels"]
        return (f'<div class="grid2">{cards}</div>'
                f'<div class="two" style="margin-top:28px"><div><h2>{X["bells_h"][i]}</h2><div class="card bells"><table><tbody>{bells}</tbody></table></div></div>'
                f'<div><h2>{X["links_h"][i]}</h2><div class="linklist">'
                f'<a href="{ctx["href_cn"]}">{ctx["cn"]} →</a><a href="{ctx["href_tt"]}">{ctx["tt"]} →</a><a href="{ctx["href_gr"]}">{ctx["gr"]} →</a>'
                f'<a href="{ctx["TG"]}" rel="noopener">{X["tg"][i]} →</a></div></div></div>'
                f'<h2 style="margin-top:34px">{t["faq_h"]}</h2>{faq_html(t)}'
                f'<h2 style="margin-top:34px">{X["touch_h"][i]}</h2><div class="btns"><a class="btn p" href="tel:{ctx["PHONE"]}">{X["call"][i]} {ctx["PHONE_TXT"]}</a>'
                f'<a class="btn s" href="{ctx["TG"]}" rel="noopener">Telegram</a><a class="btn s" href="mailto:{ctx["EMAIL"]}">{ctx["EMAIL"]}</a>'
                f'<a class="btn s" href="{ctx["MAP"]}" rel="noopener">{t["map"]}</a></div>')
    # documents
    files = sorted(os.listdir(os.path.join(root, "pdf", lang)))
    cl = [f for f in files if f.startswith("c-")]; tc = [f for f in files if f.startswith("t-")]
    key = lambda f: (int(f[2:].split("-")[0]), f) if f.startswith("c-") else (0, f)
    cl.sort(key=key)
    chips = "".join(f'<a class="dchip" href="{UP}pdf/{lang}/{f}" download>PDF · {_pdf_label(f)}</a>' for f in cl)
    tch = "".join(f'<a class="dchip" href="{UP}pdf/{lang}/{f}" download>{_pdf_label(f)}</a>' for f in tc)
    return (f'<h2>{X["d_h1"][i]}</h2><p>{X["d_p1"][i]}</p><h3 class="subh">{X["d_cls"][i]}</h3><div class="dchips">{chips}</div>'
            f'<details class="dtch"><summary>{X["d_tch"][i]} ({len(tc)})</summary><div class="dchips">{tch}</div></details>'
            f'<h2 style="margin-top:34px">{X["d_h2"][i]}</h2><div class="linklist">'
            f'<a href="{UP}files/taqiqlangan-mahsulotlar.pdf" download><b>PDF</b> — {ctx.get("cnd", "")} →</a>'
            f'<a href="https://my.gov.uz" rel="noopener"><b>my.gov.uz</b> — {X["d_gov"][i]} →</a>'
            f'<a href="https://ariza.piima.uz" rel="noopener"><b>ariza.piima.uz</b> — {X["d_ariza"][i]} →</a>'
            f'<a href="tel:+998712074048"><b>{HOT}</b> — {X["d_hot"][i]} →</a></div>'
            + __import__("laws").doc_cards(i, UP) +
            f'<h2 style="margin-top:34px">{X["d_h3"][i]}</h2><div class="card"><p>{X["d_p3"][i]}</p></div>')
