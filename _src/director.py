# Extra sections for the director's profile. SAMPLE sections are shown only with ?preview in the URL
# (e.g. /leadership/feruza-nizamatdinova/?preview) until real content replaces them: set SAMPLE[...] = False after editing.
import json
SAMPLE = {"word": True, "career": True, "awards": True, "goals": True, "hours": True}

WORD = ("Húrmetli ata-analar hám oqıwshılar! Mektebimizdiń saytına xosh keldińiz. Bizdiń maqsetimiz — hár bir oqıwshıǵa sapalı bilim berip, olardı Ózbekstannıń hám dúnyanıń jetekshi universitetlerine tayarlaw. "
        "Tájiriybeli muǵallimlerimiz, zamanagóy klasslarımız hám xalıqaralıq hamkorlıqlarımız usı maqsetke xızmet etedi. Birge islesek, balalarımızdıń keleshegi jarqın boladı.",
        "Dear parents and students, welcome to our school’s website. Our goal is to give every student a quality education and prepare them for leading universities in Uzbekistan and around the world. "
        "Our experienced teachers, modern classrooms and international partnerships all serve this goal. Working together, we can give our children a bright future.",
        "Hurmatli ota-onalar va o‘quvchilar! Maktabimiz saytiga xush kelibsiz. Maqsadimiz — har bir o‘quvchiga sifatli ta’lim berib, ularni O‘zbekiston va dunyoning yetakchi universitetlariga tayyorlash. "
        "Tajribali o‘qituvchilarimiz, zamonaviy sinflarimiz va xalqaro hamkorliklarimiz shu maqsadga xizmat qiladi. Birgalikda ishlasak, farzandlarimizning kelajagi porloq bo‘ladi.",
        "Уважаемые родители и ученики, добро пожаловать на сайт нашей школы. Наша цель — дать каждому ученику качественное образование и подготовить его к ведущим вузам Узбекистана и мира. "
        "Этой цели служат опытные учителя, современные классы и международные партнёрства. Работая вместе, мы обеспечим нашим детям светлое будущее.")
CAREER = [  # (year, text x4) — SAMPLE placeholders
 ("20XX", ("Universitetti pitkerdi", "Graduated from university", "Universitetni tamomladi", "Окончила университет")),
 ("20XX", ("Pán muǵallimi", "Subject teacher", "Fan o‘qituvchisi", "Учитель-предметник")),
 ("20XX", ("Direktordıń oqıw isleri boyınsha orınbasarı", "Deputy Director for Academic Affairs", "Direktorning o‘quv ishlari bo‘yicha o‘rinbosari", "Заместитель директора по учебной работе")),
 ("20XX", ("Kegeyli rayonı qánigelestirilgen mektebiniń direktorı", "Director of Kegeyli District Specialized School", "Kegeyli tumani ixtisoslashtirilgan maktabi direktori", "Директор Кегейлийской районной специализированной школы")),
]
AWARDS = [  # SAMPLE placeholders
 ("20XX", ("Kókirek belgisi (atı)", "Badge of honour (name)", "Ko‘krak nishoni (nomi)", "Нагрудный знак (название)")),
 ("20XX", ("Ministrlik maqtaw jarlıǵı", "Ministry certificate of honour", "Vazirlik faxriy yorlig‘i", "Почётная грамота министерства")),
 ("20XX", ("Hákimiyat minnetdarshılıq xatı", "Letter of thanks from the district administration", "Hokimlik minnatdorchilik xati", "Благодарственное письмо хокимията")),
]
GOALS = [  # SAMPLE
 ("Xalıqaralıq hamkorlıqlardı keńeytiw", "Expand international partnerships", "Xalqaro hamkorliklarni kengaytirish", "Расширить международные партнёрства"),
 ("STEM hám zamanagóy laboratoriyalar", "STEM and modern laboratories", "STEM va zamonaviy laboratoriyalar", "STEM и современные лаборатории"),
 ("Hár jılı kóbirek grant hám sertifikat", "More scholarships and certificates every year", "Har yili ko‘proq grant va sertifikat", "Больше грантов и сертификатов каждый год"),
 ("Ata-analar menen tıǵız baylanıs", "Close partnership with parents", "Ota-onalar bilan yaqin hamkorlik", "Тесное сотрудничество с родителями"),
]
HOURS = ("Shárshembi, 14:00–16:00 (aldın ala jazılıw menen)", "Wednesday, 14:00–16:00 (by appointment)", "Chorshanba, 14:00–16:00 (oldindan yozilish bilan)", "Среда, 14:00–16:00 (по записи)")
T = {
 "sample": ("NAMUNA", "SAMPLE", "NAMUNA", "ОБРАЗЕЦ"),
 "preview": ("Kórip shıǵıw rejimi: «NAMUNA» belgisi bar bólimler tek usı siltemede kórinedi hám haqıyqıy maǵlıwmat penen almastırıladı.",
             "Preview mode: sections marked SAMPLE are visible only on this link and will be replaced with real information.",
             "Ko‘rib chiqish rejimi: «NAMUNA» belgili bo‘limlar faqat shu havolada ko‘rinadi va haqiqiy ma’lumot bilan almashtiriladi.",
             "Режим просмотра: разделы с пометкой «ОБРАЗЕЦ» видны только по этой ссылке и будут заменены реальными данными."),
 "word_h": ("Direktordıń sózi", "A word from the Director", "Direktor so‘zi", "Слово директора"),
 "career_h": ("Miynet jolı", "Career path", "Mehnat yo‘li", "Карьерный путь"),
 "awards_h": ("Sıylıqları", "Awards and honours", "Mukofotlari", "Награды"),
 "goals_h": ("Mektep ushın maqsetler", "Goals for the school", "Maktab uchun maqsadlar", "Цели для школы"),
 "ach_h": ("Basshılıǵı astında mektep jetiskenlikleri", "School achievements under her leadership", "Rahbarligi ostida maktab yutuqlari", "Достижения школы под её руководством"),
 "a_sat": ("eń joqarı SAT ballı", "best SAT score", "eng yuqori SAT bali", "лучший балл SAT"),
 "a_ielts": ("eń joqarı IELTS", "best IELTS band", "eng yuqori IELTS", "лучший IELTS"),
 "a_cert": ("milliy sertifikat imtihanı (2025/2026)", "national certificate exams (2025/2026)", "milliy sertifikat imtihoni (2025/2026)", "экзаменов на нацсертификат (2025/2026)"),
 "a_chsb": ("CHSB I-sherek ortashası", "Term I CHSB average", "CHSB I-chorak o‘rtachasi", "средний CHSB, I четверть"),
 "a_more": ("Barlıq jetiskenlikler", "All achievements", "Barcha yutuqlar", "Все достижения"),
 "hours_h": ("Qabıllaw waqtı", "Reception hours", "Qabul vaqti", "Часы приёма"),
 "form_h": ("Ushırasıwǵa jazılıw", "Request a meeting", "Uchrashuvga yozilish", "Записаться на встречу"),
 "form_p": ("Atıńızdı, telefonıńızdı hám máseleni jazıń — mektep siz benen baylanısadı.", "Leave your name, phone and topic — the school will contact you to arrange a time.",
            "Ismingiz, telefoningiz va masalani yozing — maktab siz bilan bog‘lanadi.", "Оставьте имя, телефон и тему — школа свяжется с вами."),
 "f_name": ("Atıńız", "Your name", "Ismingiz", "Ваше имя"),
 "f_phone": ("Telefon", "Phone", "Telefon", "Телефон"),
 "f_topic": ("Másele", "Topic", "Masala", "Тема"),
 "f_msg": ("Qısqasha jazıń", "Short message", "Qisqacha yozing", "Коротко опишите"),
 "f_send": ("Jiberiw", "Send request", "Yuborish", "Отправить"),
 "f_ok": ("Rahmet! Sorawıńız jiberildi.", "Thank you! Your request has been sent.", "Rahmat! So‘rovingiz yuborildi.", "Спасибо! Заявка отправлена."),
 "f_err": ("Qátelik. Telefon arqalı baylanısıń.", "Something went wrong. Please call the school.", "Xatolik. Telefon orqali bog‘laning.", "Ошибка. Пожалуйста, позвоните в школу."),
 "f_need": ("Atı hám telefondı jazıń.", "Please enter your name and phone.", "Ism va telefonni kiriting.", "Укажите имя и телефон."),
 "topics": (("Qabıllaw", "Oqıw procesi", "Usınıs", "Basqa"), ("Admission", "Studies", "Suggestion", "Other"), ("Qabul", "O‘quv jarayoni", "Taklif", "Boshqa"), ("Приём", "Учёба", "Предложение", "Другое")),
}
def _svg(p, s=20, w=2):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
I_Q = '<path d="M7 7h4v4H8c0 2 1 3 3 3M15 7h4v4h-3c0 2 1 3 3 3"/>'
I_AW = '<circle cx="12" cy="9" r="6"/><path d="M8.500 13.500L7 21l5-3 5 3-1.500-7.500"/>'
I_TG = '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>'
I_CLK = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'
I_CAL = '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>'
I_UP = '<path d="M4 15l4-4 4 3 7-7"/><path d="M15 7h4v4h-3"/>'

def _wrap(key, i, html):
    if not SAMPLE.get(key):
        return html
    return f'<div class="lpsample"><span class="lpstag">{T["sample"][i]}</span>{html}</div>'

def sections(i, href, ctx):
    word = _wrap("word", i, f'<blockquote class="card lpword"><span class="lpq">{_svg(I_Q, 30)}</span><h3>{T["word_h"][i]}</h3><p>{WORD[i]}</p><cite>— {ctx["name"]}</cite></blockquote>')
    car = "".join(f'<li><span>{y}</span><p>{t[i]}</p></li>' for y, t in CAREER)
    career = _wrap("career", i, f'<div class="card lpcar"><h3>{_svg(I_UP)} {T["career_h"][i]}</h3><ol>{car}</ol></div>')
    aw = "".join(f'<li><span>{_svg(I_AW, 22)}</span><div><b>{t[i]}</b><small>{y}</small></div></li>' for y, t in AWARDS)
    awards = _wrap("awards", i, f'<div class="card lpaw"><h3>{_svg(I_AW)} {T["awards_h"][i]}</h3><ul>{aw}</ul></div>')
    gl = "".join(f'<li><b>{n}</b><span>{g[i]}</span></li>' for n, g in enumerate(GOALS, 1))
    goals = _wrap("goals", i, f'<div class="lpgoals"><h2>{T["goals_h"][i]}</h2><ol>{gl}</ol></div>')
    A = ctx["ach"]
    tiles = "".join(f'<div class="actile" style="--ac:{c}"><b>{v}</b><span>{l}</span></div>' for v, l, c in [
        (A["sat"], T["a_sat"][i], "#2a7fd1"), (A["ielts"], T["a_ielts"][i], "#d6452f"), (A["cert"], T["a_cert"][i], "#0b7a8f"), (A["chsb"], T["a_chsb"][i], "#2f8f5b")])
    ach = (f'<h2>{T["ach_h"][i]}</h2><div class="actiles lpach">{tiles}</div>'
           f'<p><a class="btn s" href="{href("achievements/")}">{T["a_more"][i]} →</a></p>')
    hours = _wrap("hours", i, f'<div class="card lphours"><span>{_svg(I_CLK, 26)}</span><div><h3>{T["hours_h"][i]}</h3><p>{HOURS[i]}</p></div></div>')
    opts = "".join(f'<option>{o}</option>' for o in T["topics"][i])
    form = (f'<div class="card lpform"><h3>{_svg(I_CAL)} {T["form_h"][i]}</h3><p>{T["form_p"][i]}</p><form id="mf" novalidate>'
            f'<label for="mn">{T["f_name"][i]}</label><input id="mn" autocomplete="name" required>'
            f'<label for="mp">{T["f_phone"][i]}</label><input id="mp" type="tel" autocomplete="tel" placeholder="+998 90 123 45 67" required>'
            f'<label for="mt">{T["f_topic"][i]}</label><select id="mt">{opts}</select>'
            f'<label for="mm">{T["f_msg"][i]}</label><textarea id="mm" rows="3"></textarea>'
            f'<input type="checkbox" id="mbot" tabindex="-1" style="display:none" aria-hidden="true">'
            f'<button type="submit" class="btn p">{T["f_send"][i]}</button><p id="mok" role="status"></p></form></div>')
    js = ("<script>(function(){if(/[?&]preview/.test(location.search)){document.body.classList.add('lpprev')}"
          "var f=document.getElementById('mf');if(!f)return;var ok=document.getElementById('mok');"
          "f.addEventListener('submit',async function(e){e.preventDefault();if(document.getElementById('mbot').checked)return;var n=f.mn.value.trim(),p=f.mp.value.trim();"
          "if(!n||!p){ok.textContent=" + json.dumps(T["f_need"][i]) + ";return}var b=f.querySelector('button');b.disabled=true;"
          "try{var r=await fetch('https://api.web3forms.com/submit',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},"
          "body:JSON.stringify({access_key:" + json.dumps(ctx["KEY"]) + ",subject:'Meeting request (Director) — '+n,from_name:'kegeyliqm.uz',name:n,phone:p,topic:f.mt.value,message:f.mm.value})});"
          "var j=await r.json();ok.textContent=j.success?" + json.dumps(T["f_ok"][i]) + ":" + json.dumps(T["f_err"][i]) + ";if(j.success)f.reset()}catch(x){ok.textContent=" + json.dumps(T["f_err"][i]) + "}b.disabled=false})})();</script>")
    note = f'<p class="lpprevnote">{T["preview"][i]}</p>'
    return dict(top=note + word, mid=f'<div class="actwo">{career}{awards}</div>{goals}{ach}', side=hours, bottom=f'{form}{js}')
