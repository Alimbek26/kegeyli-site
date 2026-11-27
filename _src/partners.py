# Partner organisations shown in the scrolling strip above the footer.
# To add one: append a line below. "logo" is a file inside photos/partners/ (PNG/SVG/JPG, ideally with a transparent or white background);
# leave logo="" to show the name as a badge instead. "url" must be the partner's official website.
DESCR = {
 "PIIMA": [
  "Ixtisoslashtirilgan ta’lim muassasalari agentligi: Ózbekstanda ixtisoslashtirilgan mektepler isin basqaradı. Mektepke qabıllaw arzaları usı agentlik arqalı beriledi.",
  "Agency for Specialized Educational Institutions: it oversees specialized schools in Uzbekistan. Applications to our school are submitted through the agency.",
  "Ixtisoslashtirilgan ta’lim muassasalari agentligi: O‘zbekistondagi ixtisoslashtirilgan maktablar faoliyatini boshqaradi. Maktabga qabul uchun arizalar shu agentlik orqali topshiriladi.",
  "Агентство специализированных образовательных учреждений: курирует специализированные школы Узбекистана. Заявки на поступление в нашу школу подаются через агентство."
 ],
 "Ájiniyaz atındaǵı NMPI": [
  "Ájiniyaz atındaǵı Nókis mámleketlik pedagogikalıq instituti (1934). Qaraqalpaqstandaǵı eń úlken pedagogikalıq joqarı oqıw orınlarınan biri.",
  "Nukus State Pedagogical Institute named after Ajiniyaz, founded in 1934. A leading teacher-training university in Karakalpakstan.",
  "Ajiniyoz nomidagi Nukus davlat pedagogika instituti (1934). Qoraqalpog‘istondagi yetakchi pedagogika oliy o‘quv yurtlaridan biri.",
  "Нукусский государственный педагогический институт имени Ажинияза (1934). Один из ведущих педагогических вузов Каракалпакстана."
 ],
 "Nukus Prezident maktabi": [
  "Nókistegi Ózbekstan Respublikası Prezident mektebi: oqıwshılar ushın xalıqaralıq dárejedegi bilim beretuǵın mámleketlik mektep.",
  "The Presidential School of the Republic of Uzbekistan in Nukus, a state school offering education to international standards.",
  "Nukusdagi O‘zbekiston Respublikasi Prezident maktabi: xalqaro darajadagi ta’lim beradigan davlat maktabi.",
  "Президентская школа Республики Узбекистан в Нукусе: государственная школа с образованием международного уровня."
 ],
 "New Uzbekistan University": [
  "Jańa Ózbekstan universiteti (Tashkent, 2021): injeneriya, kompyuter ilimleri, jasalma intellekt hám basqa da STEM baǵdarları boyınsha inglis tilindegi programmalar.",
  "New Uzbekistan University (Tashkent, opened in 2021): English-taught programmes in engineering, computer science, AI and other STEM fields.",
  "Yangi O‘zbekiston universiteti (Toshkent, 2021): muhandislik, kompyuter fanlari, sun’iy intellekt va boshqa STEM yo‘nalishlarida ingliz tilidagi dasturlar.",
  "Университет Новый Узбекистан (Ташкент, открыт в 2021 году): программы на английском языке по инженерии, компьютерным наукам, ИИ и другим STEM-направлениям."
 ],
 "British Council": [
  "Birlesken Korollik xalıqaralıq mádeniy qatnaslar hám bilim beriw shólkemi. Inglis tili, IELTS hám oqıw imkaniyatları boyınsha járdem beredi. 2026-jıl yanvardan mektebimiz British Council-dıń rásmiy IELTS dizimge alıw punkti.",
  "The UK’s international organisation for cultural relations and educational opportunities. Supports English-language learning, IELTS and study opportunities. Since January 2026 our school is an official IELTS Registration Point in partnership with the British Council.",
  "Buyuk Britaniyaning xalqaro madaniy aloqalar va ta’lim imkoniyatlari tashkiloti. Ingliz tili, IELTS va o‘qish imkoniyatlari bo‘yicha yordam beradi. 2026-yil yanvaridan maktabimiz British Council bilan hamkorlikda rasmiy IELTS ro‘yxatga olish nuqtasi.",
  "Международная организация Великобритании по культурным связям и образовательным возможностям. Поддерживает изучение английского, IELTS и учёбу за рубежом. С января 2026 года наша школа — официальный пункт регистрации на IELTS в партнёрстве с British Council."
 ]
}
PARTNERS = [
 dict(name="Nukus Prezident maktabi", url="https://nukusps.uz", logo="nukusps.png"),
 dict(name="British Council", url="https://www.britishcouncil.uz/en", logo="britishcouncil.png", dark=True),
 dict(name="PIIMA", url="https://piima.uz", logo="piima.png", dark=True),
 dict(name="Ájiniyaz atındaǵı NMPI", url="https://ndpi.uz", logo="nmpi.png"),
 dict(name="New Uzbekistan University", url="https://newuu.uz", logo="newuu.png"),
]
H = ("Hámkarlarımız", "Our partners", "Hamkorlarimiz", "Наши партнёры")
P = ("Biz menen birge islesetuǵın shólkemler. Logotipti basıp, olardıń saytına ótiń.",
     "Organizations we work with. Tap a logo to visit their website.",
     "Biz bilan hamkorlik qiluvchi tashkilotlar. Logotipni bosib, ularning saytiga o‘ting.",
     "Организации, с которыми мы сотрудничаем. Нажмите на логотип, чтобы перейти на их сайт.")

PAGE_DESC = ("Mektepimizdiń hámkarları: PIIMA, Ájiniyaz atındaǵı NMPI, Prezident mektebi, Jańa Ózbekstan universiteti hám British Council.",
             "The partners of Kegeyli specialized school: PIIMA, Nukus State Pedagogical Institute, the Presidential School, New Uzbekistan University and the British Council.",
             "Kegeyli ixtisoslashtirilgan maktabining hamkorlari: PIIMA, Nukus davlat pedagogika instituti, Prezident maktabi, Yangi O‘zbekiston universiteti va British Council.",
             "Партнёры Кегейлийской специализированной школы: PIIMA, Нукусский педагогический институт, Президентская школа, Университет Новый Узбекистан и British Council.")
X = {"visit": ("Saytqa ótiw", "Visit website", "Saytga o‘tish", "Перейти на сайт"),
     "join_h": ("Hámkar bolǵıńız keledi me?", "Want to partner with us?", "Hamkor bo‘lmoqchimisiz?", "Хотите стать партнёром?"),
     "join_p": ("Birgelikte oqıw, ótkeriletuǵın ilajlar yamasa ǵárezsiz jobalar boyınsha usınısıńız bolsa, bizge jazıń.", "If you have an idea for joint lessons, events or projects, write to us.", "Qo‘shma darslar, tadbirlar yoki loyihalar bo‘yicha taklifingiz bo‘lsa, bizga yozing.", "Если у вас есть идея совместных занятий, мероприятий или проектов, напишите нам."),
     "all": ("Barlıq hámkarlar", "All partners", "Barcha hamkorlar", "Все партнёры")}
def body(i, up, ctx):
    cards = ""
    for p in PARTNERS:
        logo = (f'<img src="{up}photos/partners/{p["logo"]}" alt="{p["name"]}" height="72">' if p["logo"] else f'<span class="pbadge">{p["name"][:2].upper()}</span>')
        d = DESCR.get(p["name"], ("", "", "", ""))[i]
        cards += (f'<article class="card pcard"><div class="plogo{" pinv" if p.get("dark") else ""}">{logo}</div><h3>{p["name"]}</h3><p>{d}</p>'
                  f'<a class="btn s" href="{p["url"]}" target="_blank" rel="noopener">{X["visit"][i]} →</a></article>')
    return (f'<p class="lead2">{P[i]}</p><div class="pgrid">{cards}</div>'
            f'<div class="card pjoin"><h3>{X["join_h"][i]}</h3><p>{X["join_p"][i]}</p><div class="btns"><a class="btn p" href="{ctx.get("SUP_HREF", "")}">{__import__("support").NAME[i]} →</a><a class="btn p" href="mailto:{ctx["EMAIL"]}">{ctx["EMAIL"]}</a><a class="btn s" href="{ctx["TG"]}" rel="noopener">Telegram</a><a class="btn s" href="tel:{ctx["PHONE"]}">{ctx["PHONE_TXT"]}</a></div></div>')
