# "Our story": the school's history 2022 -> today, in 4 languages.
# Every milestone comes from data already published on the site (news, results, graduates, offers).
# To add a milestone: copy a dict in EVENTS (date "YYYY", "YYYY-MM" or "YYYY-MM-DD"; big=True for a highlighted card).
import graduates as G
import offers as OF

SUB = "history/"
L = lambda a, b, c, d: (a, b, c, d)
NAME = L("Mektebimiz tariyxı", "Our story", "Maktabimiz tarixi", "История школы")
DESC = L("2022-jıldan búginge shekem: birinshi pitkeriwshiler, shet el universitetleri, xalıqaralıq tán alınıw.",
         "From 2022 to today: first graduates, offers from abroad and international recognition.",
         "2022-yildan bugungacha: birinchi bitiruvchilar, xorijiy universitetlar, xalqaro e’tirof.",
         "С 2022 года до сегодняшнего дня: первые выпускники, зарубежные университеты, международное признание.")
ICON = ('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>', "#0b5f78")

CAT = {  # colour, icon, label
 "school": ("#0b5f78", '<path d="M3 21h18"/><path d="M5 21V9l7-5 7 5v12"/><path d="M10 21v-5h4v5"/>', L("Mektep", "School", "Maktab", "Школа")),
 "grads": ("#047857", '<path d="M22 10L12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/>', L("Pitkeriwshiler", "Graduates", "Bitiruvchilar", "Выпускники")),
 "result": ("#d97706", '<circle cx="12" cy="15" r="6"/><path d="M8.500 10.200L5 3h4l3 6 3-6h4l-3.500 7.200"/>', L("Nátiyje", "Result", "Natija", "Результат")),
 "abroad": ("#2563eb", '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.500 2.700 3.800 5.700 3.800 9s-1.300 6.300-3.800 9c-2.500-2.700-3.800-5.700-3.800-9S9.500 5.700 12 3z"/>', L("Shet el", "Abroad", "Xorij", "За рубежом")),
 "recog": ("#7c3aed", '<path d="M12 3l2.600 5.300 5.900.900-4.300 4.100 1 5.800L12 16.300 6.800 19.100l1-5.800L3.500 9.200l5.900-.900z"/>', L("Tán alınıw", "Recognition", "E’tirof", "Признание")),
}


def _grad(y):
    n = dict(G.YEARS)[y]
    uni = sum(1 for k, f in G.PLACED[y] if G.INST[k][5] == "uni")
    return n, uni


def _gev(y, date, big=False):
    n, u = _grad(y)
    first = y == G.YEARS[0][0]
    t = (L("Birinshi pitkeriwshiler", "Our first graduates", "Birinchi bitiruvchilar", "Первые выпускники") if first else
         L(f"{y[-4:]}-jıl pitkeriwshileri", f"Class of {y[-4:]}", f"{y[-4:]}-yil bitiruvchilari", f"Выпуск {y[-4:]} года"))
    return dict(date=date, cat="grads", big=big, link="graduates/", title=t,
                text=L(f"{n} pitkeriwshi, olardıń {u} universitetke kirdi.", f"{n} graduates, {u} of them went on to university.",
                       f"{n} nafar bitiruvchi, ulardan {u} nafari universitetga kirdi.", f"{n} выпускников, {u} из них поступили в университет."))


EVENTS = [
 dict(date="2022", cat="school", big=True, link="about/",
      title=L("Mektep ashıldı", "The school opens", "Maktab ochildi", "Открытие школы"),
      text=L("Kegeyli rayonında anıq hám tábiyiy pánlerge qánigelestirilgen mektep Qánigelestirilgen bilimlendiriw mekemeleri agentligi sistemasında jumısın basladı.",
             "A school specializing in exact and natural sciences opens in Kegeyli District, as part of the Agency for Specialized Educational Institutions.",
             "Kegeli tumanida aniq va tabiiy fanlarga ixtisoslashgan maktab Ixtisoslashtirilgan ta’lim muassasalari agentligi tizimida faoliyatini boshladi.",
             "В Кегейлийском районе открылась школа, специализирующаяся на точных и естественных науках, в системе Агентства специализированных образовательных учреждений.")),
 dict(date="2023-02-07", cat="result", link="news/",
      title=L("Birinshi grantlar", "First grants", "Birinchi grantlar", "Первые гранты"),
      text=L("Artıqbay Saparniyazov hám Adilbek Jumabaev matematikadan respublika olimpiadasınıń saralaw basqıshında sıylıqlı orın alıp, hár biri PDP University-diń 12 000 000 swmlıq grantın jeńip aldı.",
             "Artıqbay Saparniyazov and Adilbek Jumabaev become prize-winners in the qualifying round of the national maths olympiad, and each wins a 12,000,000 so‘m PDP University grant.",
             "Artıqbay Saparniyazov va Adilbek Jumabaev matematika bo‘yicha respublika olimpiadasining saralash bosqichida sovrindor bo‘lib, har biri PDP Universityning 12 000 000 so‘mlik grantini qo‘lga kiritdi.",
             "Артыкбай Сапарниязов и Адилбек Жумабаев стали призёрами отборочного этапа республиканской олимпиады по математике и получили по гранту PDP University в 12 000 000 сумов.")),
 _gev("2022/2023", "2023-06"),
 dict(date="2024-03", cat="result", link="achievements/ielts/",
      title=L("Birinshi IELTS sertifikatları", "First IELTS certificates", "Birinchi IELTS sertifikatlari", "Первые сертификаты IELTS"),
      text=L("Oqıwshılarımız birinshi IELTS sertifikatların aldı.", "Our students receive their first IELTS certificates.", "O‘quvchilarimiz birinchi IELTS sertifikatlarini oldi.", "Наши ученики получают первые сертификаты IELTS.")),
 dict(date="2024-04-01", cat="school", link="clubs/young-academicians/",
      title=L("«Jas akademikler» klubı", "Young Academicians club", "«Yosh akademiklar» to‘garagi", "Клуб «Юные академики»"),
      text=L("PF-55 Pármanı tiykarında Pánler akademiyası menen birge islewshi klub jumısın basladı.", "Under Presidential Decree PF-55, a club run with the Academy of Sciences begins.", "PF-55 Farmoni asosida Fanlar akademiyasi bilan birga ishlaydigan to‘garak faoliyatini boshladi.", "По Указу УП-55 начинает работу клуб совместно с Академией наук.")),
 _gev("2023/2024", "2024-06"),
 dict(date="2024-12-07", cat="result", link="achievements/sat/",
      title=L("Birinshi SAT hám IELTS 7.5", "First SAT, and IELTS 7.5", "Birinchi SAT va IELTS 7.5", "Первый SAT и IELTS 7.5"),
      text=L("Bir kúnde: oqıwshımız birinshi márte SAT tapsırdı, Dawıtbek Arıslanbaev bolsa IELTS-ten 7.5 (C1) aldı.", "On the same day, a student sits the SAT for the first time and Dawitbek Arislanbaev scores IELTS 7.5 (C1).",
             "Bir kunda: o‘quvchimiz birinchi marta SAT topshirdi, Dawitbek Arislanbaev esa IELTSdan 7.5 (C1) oldi.", "В один день: ученик впервые сдаёт SAT, а Давитбек Арисланбаев получает IELTS 7.5 (C1).")),
 dict(date="2025-01-05", cat="abroad", big=True, link="achievements/offers/",
      title=L("Birinshi shet el universitetleri", "First offers from abroad", "Birinchi xorijiy universitetlar", "Первые зарубежные университеты"),
      text=L("Khurshida Ismailova AQSh-tıń altı universitetine qabıl etildi.", "Khurshida Ismailova is admitted to six universities in the USA.", "Khurshida Ismailova AQShning oltita universitetiga qabul qilindi.", "Хуршида Исмайлова принята в шесть университетов США.")),
 dict(date="2025-04-04", cat="abroad", big=True, link="achievements/offers/",
      title=L("Dúnyanıń top-100 universitetleri", "Two world top-100 universities", "Dunyoning top-100 universitetlari", "Два университета мирового топ-100"),
      text=L("Ayjamal Abdullaeva Glasgo (QS #78) hám Birmingem (QS #80) universitetlerinen usınıs aldı.", "Ayjamal Abdullaeva receives offers from the University of Glasgow (QS #78) and the University of Birmingham (QS #80).",
             "Ayjamal Abdullaeva Glazgo (QS #78) va Birmingem (QS #80) universitetlaridan taklif oldi.", "Айжамал Абдуллаева получает предложения от Университета Глазго (QS #78) и Бирмингемского университета (QS #80).")),
 dict(date="2025-05-17", cat="abroad", link="achievements/offers/",
      title=L("16 000 dollarlıq grant", "A $16,000 grant", "16 000 dollarlik grant", "Грант $16 000"),
      text=L("Aynura Turganbaeva Arizona universitetinen 16 000 dollarlıq grant penen usınıs aldı.", "Aynura Turganbaeva is offered a $16,000 grant by the University of Arizona.", "Aynura Turganbaeva Arizona universitetidan 16 000 dollarlik grant bilan taklif oldi.", "Айнура Турганбаева получает предложение с грантом $16 000 от Университета Аризоны.")),
 _gev("2024/2025", "2025-06"),
 dict(date="2025-2026", cat="result", link="achievements/olympiads/",
      title=L("AKHU STEM olimpiadasında bronza", "Bronze at the AKHU STEM Olympiad", "AKHU STEM olimpiadasida bronza", "Бронза на олимпиаде AKHU STEM"),
      text=L("2025/2026 oqıw jılında AKHU STEM olimpiadasında bronza medal hám 95 milliy sertifikat imtixanı (aldıńǵı jılı 32).", "A bronze medal at the AKHU STEM Olympiad, and 95 national certificate exams taken in 2025/2026 (32 a year earlier).",
             "2025/2026 o‘quv yilida AKHU STEM olimpiadasida bronza medal va 95 ta milliy sertifikat imtihoni (oldingi yili 32 ta).", "Бронзовая медаль олимпиады AKHU STEM и 95 экзаменов на национальные сертификаты в 2025/2026 году (годом ранее — 32).")),
 dict(date="2026-01-29", cat="recog", big=True, link="ielts/",
      title=L("Rásmiy IELTS dizimge alıw punkti", "Official IELTS Registration Point", "Rasmiy IELTS ro‘yxatga olish nuqtasi", "Официальный пункт регистрации IELTS"),
      text=L("Mektep British Council penen sheriklikte rásmiy IELTS dizimge alıw punkti boldı.", "The school becomes an official IELTS Registration Point in partnership with the British Council.", "Maktab British Council bilan hamkorlikda rasmiy IELTS ro‘yxatga olish nuqtasiga aylandi.", "Школа становится официальным пунктом регистрации IELTS в партнёрстве с British Council.")),
 _gev("2025/2026", "2026-06"),
 dict(date="2026-11", cat="recog", link="",
      title=L("kegeyliqm.uz — 4 tilde", "kegeyliqm.uz in four languages", "kegeyliqm.uz — 4 tilda", "kegeyliqm.uz на четырёх языках"),
      text=L("Mektep sayti qaraqalpaq, inglis, ózbek hám rus tillerinde: tekseriwge bolatuǵın nátiyjeler, mektep profili hám shet elde oqıw quralları.", "The school website goes live in Karakalpak, English, Uzbek and Russian, with results that can be checked, a School Profile and study-abroad tools.",
             "Maktab sayti qoraqalpoq, ingliz, o‘zbek va rus tillarida: tekshirish mumkin bo‘lgan natijalar, maktab profili va xorijda o‘qish vositalari.", "Сайт школы на каракалпакском, английском, узбекском и русском: проверяемые результаты, профиль школы и инструменты для учёбы за рубежом.")),
 dict(date="2026-11-07", cat="result", link="achievements/sat/",
      title=L("SAT 1440 — mektep rekordı", "SAT 1440, a school record", "SAT 1440 — maktab rekordi", "SAT 1440 — рекорд школы"),
      text=L("Dawıtbek Arıslanbaev SAT-tan 1440 ball aldı (95-procentil). Onıń bes sertifikatı bar.", "Dawitbek Arislanbaev scores 1440 on the SAT (95th percentile), one of his five certificates.", "Dawitbek Arislanbaev SATdan 1440 ball oldi (95-persentil). Uning beshta sertifikati bor.", "Давитбек Арисланбаев набирает 1440 баллов SAT (95-й процентиль) — один из пяти его сертификатов.")),
]

NEXT = [L("College Board (CEEB) kodı — soralǵan", "College Board (CEEB) code: requested", "College Board (CEEB) kodi — so‘ralgan", "Код College Board (CEEB) — запрошен"),
        L("Shet eldegi sherik mektep", "A partner school abroad", "Xorijdagi hamkor maktab", "Школа-партнёр за рубежом"),
        L("Xalıqaralıq olimpiadalarǵa qatnasıw", "International olympiads", "Xalqaro olimpiadalarda qatnashish", "Участие в международных олимпиадах"),
        L("Jáne kóbirek shet el universitetleri", "More students at universities abroad", "Yana ko‘proq xorijiy universitetlar", "Больше студентов в зарубежных университетах")]

T = dict(
 lead=L("Tórt jıl ishinde awıllıq rayondaǵı jas mektep oqıwshıları dúnyanıń top-100 universitetlerinen usınıs alatuǵın mektepke aylandı. Mine bul jol.",
        "In four years, a young school in a rural district has become one whose students receive offers from world top-100 universities. This is how it happened.",
        "To‘rt yil ichida qishloq tumanidagi yosh maktab o‘quvchilari dunyoning top-100 universitetlaridan taklif oladigan maktabga aylandi. Mana bu yo‘l.",
        "За четыре года молодая школа в сельском районе стала школой, ученики которой получают предложения от университетов мирового топ-100. Вот как это было."),
 years=L("jıl", "years", "yil", "года"),
 grads=L("pitkeriwshi", "graduates", "bitiruvchi", "выпускника"),
 offers=L("shet el usınısı", "offers from abroad", "xorijiy taklif", "предложений из-за рубежа"),
 top=L("top-100 usınısı", "top-100 offers", "top-100 taklifi", "предложения топ-100"),
 chart_h=L("Hár jılı kóbirek pitkeriwshi", "More graduates every year", "Har yili ko‘proq bitiruvchi", "С каждым годом больше выпускников"),
 chart_uni=L("universitetke kirdi", "went to university", "universitetga kirdi", "поступили в университет"),
 chart_all=L("pitkeriwshiler", "graduates", "bitiruvchilar", "выпускники"),
 more=L("Tolıǵıraq", "More", "Batafsil", "Подробнее"),
 next_h=L("Keyingi qádemler", "What’s next", "Keyingi qadamlar", "Что дальше"),
 next_p=L("Tariyxımız endi baslanıp atır.", "Our story is just beginning.", "Tariximiz endi boshlanmoqda.", "Наша история только начинается."),
 goals=L("Xalıqaralıq maqsetlerimiz", "Our international goals", "Xalqaro maqsadlarimiz", "Наши международные цели"),
 src=L("Barlıq maǵlıwmatlar bul saytta tolıq kórsetilgen.", "Every milestone is documented in full on this website.", "Barcha ma’lumotlar ushbu saytda to‘liq ko‘rsatilgan.", "Каждое событие подробно описано на этом сайте."),
)

SUMMER = L("{y}-jıl jazı", "Summer {y}", "{y}-yil yozi", "Лето {y}")
MON = [("yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentyabr", "oktyabr", "noyabr", "dekabr"),
       ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"),
       ("yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentabr", "oktabr", "noyabr", "dekabr"),
       ("января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря")]
MON_N = [("yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentyabr", "oktyabr", "noyabr", "dekabr"),
         MON[1], MON[2], ("январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь")]


def _fdate(d, i):
    if len(d) == 4:
        return d
    if len(d) == 9:  # school year "2025-2026"
        return d.replace("-", "/")
    p = d.split("-")
    if len(p) == 2:
        return f"{MON_N[i][int(p[1]) - 1].capitalize()} {p[0]}"
    return f"{int(p[2])} {MON[i][int(p[1]) - 1]} {p[0]}" if i != 1 else f"{int(p[2])} {MON[1][int(p[1]) - 1]} {p[0]}"


def _svg(p, s=22):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'


def _chart(i):
    rows = [(y, n, _grad(y)[1]) for y, n in G.YEARS]
    mx = max(n for _, n, _ in rows)
    W, H, pad, bw = 560, 250, 34, 74
    gap = (W - 2 * pad - len(rows) * bw) / max(1, len(rows) - 1)
    out = ""
    for k, (y, n, u) in enumerate(rows):
        x = pad + k * (bw + gap)
        h = (H - 70) * n / mx; hu = (H - 70) * u / mx
        top = H - 30 - h
        out += (f'<rect x="{x:.1f}" y="{top:.1f}" width="{bw}" height="{h:.1f}" rx="10" class="hcb"/>'
                f'<rect x="{x:.1f}" y="{H - 30 - hu:.1f}" width="{bw}" height="{hu:.1f}" rx="10" class="hcu" style="--k:{k}"/>'
                f'<text x="{x + bw / 2:.1f}" y="{top - 10:.1f}" class="hcn">{n}</text>'
                f'<text x="{x + bw / 2:.1f}" y="{H - 8}" class="hcy">{y[-4:]}</text>')
    leg = (f'<p class="hcleg"><span class="hcl hcl1"></span>{T["chart_all"][i]} <span class="hcl hcl2"></span>{T["chart_uni"][i]}</p>')
    return (f'<figure class="card hchart"><h3>{T["chart_h"][i]}</h3><svg viewBox="0 0 {W} {H}" role="img" aria-label="{T["chart_h"][i]}">{out}</svg>{leg}</figure>')


def body(i, up, href):
    tot = sum(n for _, n in G.YEARS)
    unis = len(OF.OFFERS)
    top = sum(1 for o in OF.OFFERS if (OF.UNI.get(o["uni"], (None, None))[1] or 999) <= 100)
    yrs = int(G.YEARS[-1][0][-4:]) - 2022
    stats = [(f"{yrs}", T["years"][i]), (str(tot), T["grads"][i]), (str(unis), T["offers"][i]), (str(top), T["top"][i])]
    hero = (f'<div class="hhero"><div class="hhy"><span>2022</span><i aria-hidden="true"></i><span>2026</span></div>'
            f'<p class="hlead">{T["lead"][i]}</p><div class="hstats">'
            + "".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in stats) + '</div></div>')
    years = sorted({e["date"][:4] for e in EVENTS})
    ynav = '<nav class="hyn" aria-label="years">' + "".join(f'<a href="#y{y}">{y}</a>' for y in years) + '</nav>'
    tl, cur, side = "", None, 0
    for e in sorted(EVENTS, key=lambda e: e["date"]):
        y = e["date"][:4]
        if y != cur:
            tl += f'<li class="hyr" id="y{y}"><span>{y}</span></li>'
            cur = y
        col, ic, lab = CAT[e["cat"]]
        link = f'<a class="hmore" href="{href(e["link"])}">{T["more"][i]} →</a>' if e.get("link") is not None else ""
        tl += (f'<li class="hev{" big" if e.get("big") else ""} {"l" if side % 2 == 0 else "r"}" style="--c:{col}"><span class="hdot">{_svg(ic, 18)}</span>'
               f'<article class="hcard"><p class="hmeta"><span class="hcat">{lab[i]}</span><time>{SUMMER[i].format(y=e["date"][:4]) if e["cat"] == "grads" else _fdate(e["date"], i)}</time></p>'
               f'<h3>{e["title"][i]}</h3><p>{e["text"][i]}</p>{link}</article></li>')
        side += 1
    nxt = "".join(f"<li>{x[i]}</li>" for x in NEXT)
    return (hero + _chart(i) + ynav + f'<ol class="htl">{tl}'
            f'<li class="hyr hnow"><span>…</span></li></ol>'
            f'<div class="hnext"><div><h2>{T["next_h"][i]}</h2><p>{T["next_p"][i]}</p><ul>{nxt}</ul></div>'
            f'<a class="btn p" href="{href("international/")}">{T["goals"][i]} →</a></div><p class="note">{T["src"][i]}</p>')
