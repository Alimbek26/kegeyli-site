# "My study abroad plan" builder: 8-question wizard -> personal plan (readiness, country fit, exams,
# dated timeline with checkboxes, money vs budget, scholarships, reach universities). Everything runs in
# the browser and is saved on the device (localStorage "abroadPlan"). Data is reused from the other
# Study abroad modules so there is one source of truth.
import json
import countries as CO, calculator as CAL, deadlines as DL, sat as SAT, top10 as TP

def T(a, b, c, d): return (a, b, c, d)

NAME = T("Meniń jobam", "My plan", "Mening rejam", "Мой план")
TITLE = T("Shet elde oqıw jobası", "My study abroad plan", "Xorijda o‘qish rejam", "Мой план учёбы за рубежом")
DESC = T("8 sorawǵa juwap beriń hám jeke jobańızdı alıń: tayarlıq dárejesi, mámleketler, testler, kún-kún kalendar, qárejet hám stipendiyalar.",
         "Answer 8 questions and get a personal plan: readiness score, best-fit countries, exams, a dated timeline, costs and scholarships.",
         "8 ta savolga javob bering va shaxsiy rejangizni oling: tayyorgarlik darajasi, davlatlar, testlar, sanali reja, xarajat va stipendiyalar.",
         "Ответьте на 8 вопросов и получите личный план: готовность, подходящие страны, экзамены, план по датам, расходы и стипендии.")

UI = {
 "intro": T("Bir neshe minutta jeke jobańızdı dúziń. Juwaplar tek usı telefonda saqlanadı.", "Build your personal plan in a few minutes. Your answers stay only on this phone.",
            "Bir necha daqiqada shaxsiy rejangizni tuzing. Javoblar faqat shu telefonda saqlanadi.", "Составьте личный план за несколько минут. Ответы хранятся только на этом телефоне."),
 "step": T("{n}-qádem / {t}", "Step {n} of {t}", "{n}-qadam / {t}", "Шаг {n} из {t}"),
 "back": T("Artqa", "Back", "Orqaga", "Назад"), "next": T("Keyingi", "Next", "Keyingi", "Далее"), "build": T("Jobanı dúziw", "Build my plan", "Rejani tuzish", "Составить план"),
 # questions
 "q_grade": T("Házir neshinshi klasstasız?", "Which grade are you in now?", "Hozir nechanchi sinfdasiz?", "В каком вы классе?"),
 "h_grade": T("Bul múddetlerdi esaplaw ushın kerek.", "This sets the dates in your timeline.", "Bu muddatlarni hisoblash uchun kerak.", "Это нужно, чтобы рассчитать даты."),
 "g": T("{n}-klass", "Grade {n}", "{n}-sinf", "{n} класс"), "g12": T("Mektepti pitkerdim", "Already graduated", "Maktabni bitirganman", "Уже окончил(а) школу"),
 "q_c": T("Qaysı mámleketler qızıqtıradı?", "Which countries interest you?", "Qaysi davlatlar qiziqtiradi?", "Какие страны вам интересны?"),
 "h_c": T("3 ke shekem tańlań.", "Choose up to 3.", "3 tagacha tanlang.", "Выберите до 3."),
 "q_f": T("Qaysı tarawda oqımaqshısız?", "What do you want to study?", "Qaysi sohada o‘qimoqchisiz?", "Что хотите изучать?"),
 "h_f": T("Anıq bolmasa — «Ele anıq emes» ti tańlań.", "Not sure? Choose “Not sure yet”.", "Aniq bo‘lmasa — «Hali aniq emas» ni tanlang.", "Не уверены? Выберите «Пока не знаю»."),
 "q_a": T("Maqsetińiz qanday?", "What is your goal?", "Maqsadingiz qanday?", "Какая у вас цель?"),
 "h_a": T("Bul test maqsetlerin ózgertedi.", "This changes your test targets.", "Bu test maqsadlarini o‘zgartiradi.", "От этого зависят целевые баллы."),
 "q_i": T("Ingliz tili dárejeńiz (IELTS)?", "Your English level (IELTS)?", "Ingliz tili darajangiz (IELTS)?", "Ваш уровень английского (IELTS)?"),
 "h_i": T("Rásmiy ball yamasa ádil bahalawıńız.", "An official score or your honest estimate.", "Rasmiy ball yoki halol bahoingiz.", "Официальный балл или честная оценка."),
 "q_s": T("SAT ballıńız?", "Your SAT score?", "SAT ballingiz?", "Ваш балл SAT?"),
 "h_s": T("Sınaq testi de esapqa alınadı.", "A practice-test score is fine.", "Sinov testi natijasi ham bo‘ladi.", "Подойдёт и результат пробного теста."),
 "q_b": T("Shańaraq jılına qansha tóley aladı?", "How much can your family pay per year?", "Oila yiliga qancha to‘lay oladi?", "Сколько семья может платить в год?"),
 "h_b": T("Oqıw + jasaw. Bul tek esap ushın.", "Tuition plus living costs. Used only for the estimate.", "O‘qish + yashash. Faqat hisob uchun.", "Обучение и проживание. Только для расчёта."),
 "q_x": T("Stipendiya qanshelli kerek?", "How much do you need a scholarship?", "Stipendiya qanchalik kerak?", "Насколько нужна стипендия?"),
 "h_x": T("Ádil juwap beriń — joba soǵan qaray dúziledi.", "Be honest: the plan depends on it.", "Halol javob bering — reja shunga qarab tuziladi.", "Ответьте честно: от этого зависит план."),
 # options
 "f_eng": T("Injeneriya hám IT", "Engineering & IT", "Muhandislik va IT", "Инженерия и IT"), "f_med": T("Medicina", "Medicine", "Tibbiyot", "Медицина"),
 "f_bus": T("Biznes hám ekonomika", "Business & economics", "Biznes va iqtisodiyot", "Бизнес и экономика"), "f_sci": T("Tábiyiy pánler hám matematika", "Sciences & maths", "Tabiiy fanlar va matematika", "Естественные науки и математика"),
 "f_hum": T("Gumanitar hám social pánler", "Humanities & social sciences", "Gumanitar va ijtimoiy fanlar", "Гуманитарные и социальные науки"), "f_und": T("Ele anıq emes", "Not sure yet", "Hali aniq emas", "Пока не знаю"),
 "a_top": T("Dúnyadaǵı top universitetler", "World top universities", "Dunyodagi top universitetlar", "Топ-вузы мира"), "a_top_s": T("Eń kúshli tańlaw", "Most competitive", "Eng kuchli tanlov", "Самый высокий конкурс"),
 "a_strong": T("Jaqsı xalıqaralıq universitet", "A good international university", "Yaxshi xalqaro universitet", "Хороший международный вуз"), "a_strong_s": T("Balans", "Balanced", "Muvozanat", "Баланс"),
 "a_value": T("Arzan hám isenimli", "Affordable and safe choice", "Arzon va ishonchli", "Доступно и надёжно"), "a_value_s": T("Qárejet birinshi orında", "Cost comes first", "Xarajat birinchi o‘rinda", "Главное — стоимость"),
 "i0": T("Ele tapsırmaǵanman", "No score yet", "Hali topshirmaganman", "Ещё не сдавал(а)"), "i45": T("5.0 den tómen", "Below 5.0", "5.0 dan past", "Ниже 5.0"),
 "s0": T("Ele tapsırmaǵanman", "No score yet", "Hali topshirmaganman", "Ещё не сдавал(а)"), "s950": T("1000 nan tómen", "Below 1000", "1000 dan past", "Ниже 1000"),
 "x_full": T("Tek tolıq stipendiya menen", "Only with a full scholarship", "Faqat to‘liq stipendiya bilan", "Только с полной стипендией"),
 "x_part": T("Bólekli járdem jetkilikli", "Partial help is enough", "Qisman yordam yetarli", "Хватит частичной помощи"),
 "x_none": T("Shańaraq tóley aladı", "My family can pay", "Oila to‘lay oladi", "Семья может оплатить"),
 # results
 "r_for": T("Jeke joba", "Personal plan", "Shaxsiy reja", "Личный план"), "r_start": T("Oqıw baslanıwı", "Studies start", "O‘qish boshlanishi", "Начало учёбы"),
 "ready": T("Tayarlıq", "Readiness", "Tayyorgarlik", "Готовность"),
 "rl3": T("Kúshli baslaw", "Strong start", "Kuchli boshlanish", "Сильный старт"), "rl2": T("Durıs jolda", "On track", "To‘g‘ri yo‘ldasiz", "На верном пути"),
 "rl1": T("Jumıs kerek", "Needs work", "Ishlash kerak", "Нужно поработать"), "rl0": T("Tez háreket etiń", "Act now", "Tez harakat qiling", "Действуйте сейчас"),
 "k_eng": T("Ingliz tili", "English", "Ingliz tili", "Английский"), "k_test": T("Testler", "Tests", "Testlar", "Тесты"), "k_money": T("Qárejet", "Money", "Xarajat", "Деньги"), "k_time": T("Waqıt", "Time", "Vaqt", "Время"),
 "week_h": T("Usı hápte islew kerek", "Do this week", "Shu hafta qiling", "Сделайте на этой неделе"),
 "c_h": T("Mámleketler: sizge qanshelli sáykes", "Countries: how well they fit you", "Davlatlar: sizga qanchalik mos", "Страны: насколько подходят"),
 "fit2": T("Jaqsı sáykes", "Good fit", "Yaxshi mos", "Хорошо подходит"), "fit1": T("Múmkin", "Possible", "Mumkin", "Возможно"), "fit0": T("Qıyın", "Challenging", "Qiyin", "Сложно"),
 "cost_y": T("Jılına shama menen", "Approx. per year", "Yiliga taxminan", "Примерно в год"),
 "m_ok": T("Byudjetińiz jetedi", "Your budget covers it", "Byudjetingiz yetadi", "Бюджета хватает"),
 "m_lo": T("Arzan universitette jetedi", "Covered at a lower-cost university", "Arzonroq universitetda yetadi", "Хватит в недорогом вузе"),
 "m_no": T("Byudjetten joqarı", "Above your budget", "Byudjetdan yuqori", "Выше бюджета"),
 "s_gov": T("Tolıq mámleketlik stipendiya bar", "Full government scholarship available", "To‘liq davlat stipendiyasi bor", "Есть полная госстипендия"),
 "s_need": T("Top universitetler mútájlikke qaray járdem beredi (kúshli tańlaw)", "Top universities give need-based aid (very competitive)", "Top universitetlar ehtiyojga qarab yordam beradi (kuchli tanlov)", "Топ-вузы дают помощь по потребности (большой конкурс)"),
 "s_none": T("Tolıq stipendiya az", "Few full scholarships", "To‘liq stipendiya kam", "Мало полных стипендий"),
 "e_ok": T("IELTS maqsetke jetken ({t})", "IELTS meets the target ({t})", "IELTS maqsadga yetgan ({t})", "IELTS на уровне цели ({t})"),
 "e_gap": T("IELTS maqset {t}: +{g} kerek", "IELTS target {t}: +{g} needed", "IELTS maqsad {t}: +{g} kerak", "Цель IELTS {t}: нужно +{g}"),
 "e_none": T("IELTS maqset {t}: ele ball joq", "IELTS target {t}: no score yet", "IELTS maqsad {t}: hali ball yo‘q", "Цель IELTS {t}: балла пока нет"),
 "t_ok": T("SAT maqsetke jetken", "SAT meets the target", "SAT maqsadga yetgan", "SAT на уровне цели"), "t_gap": T("SAT maqset {t}+", "SAT target {t}+", "SAT maqsad {t}+", "Цель SAT {t}+"),
 "t_no": T("SAT kerek emes", "SAT not needed", "SAT kerak emas", "SAT не нужен"),
 "loc": T("Kóp baǵdarlamalar jergilikli tilde; mámleketlik stipendiyada til úyreniw jılı bar.", "Many programmes are taught in the local language; the government scholarship includes a language year.",
          "Ko‘p dasturlar mahalliy tilda; davlat stipendiyasida til o‘rganish yili bor.", "Многие программы на местном языке; госстипендия включает год языка."),
 "cmp": T("Mámleketlerdi salıstırıw", "Compare countries", "Davlatlarni solishtirish", "Сравнить страны"),
 "calc": T("Kalkulyator", "Cost calculator", "Kalkulyator", "Калькулятор"),
 "more": T("Tolıǵıraq", "Details", "Batafsil", "Подробнее"), "official": T("Rásmiy sayt", "Official site", "Rasmiy sayt", "Официальный сайт"),
 "r_tests": T("Testler", "Tests", "Testlar", "Тесты"), "r_lang": T("Til", "Language", "Til", "Язык"), "r_schol": T("Stipendiyalar", "Scholarships", "Stipendiyalar", "Стипендии"),
 "x_h": T("Testler jobası", "Exam plan", "Testlar rejasi", "План экзаменов"),
 "x_now": T("Házir", "Now", "Hozir", "Сейчас"), "x_goal": T("Maqset", "Target", "Maqsad", "Цель"), "x_by": T("Tapsırıw múddeti", "Take it by", "Topshirish muddati", "Сдать до"),
 "x_prep": T("Tayarlıq: shama menen {w} hápte", "Preparation: about {w} weeks", "Tayyorgarlik: taxminan {w} hafta", "Подготовка: около {w} недель"),
 "x_done": T("Maqsetke jetken — tek sertifikat múddetin tekseriń (2 jıl).", "Target reached: just check the certificate is still valid (2 years).", "Maqsadga yetgan — faqat sertifikat muddatini tekshiring (2 yil).", "Цель достигнута: проверьте срок действия сертификата (2 года)."),
 "x_sat_dates": T("Jaqın SAT kúnleri", "Next SAT dates", "Yaqin SAT sanalari", "Ближайшие даты SAT"), "x_reg": T("dizimnen ótiw {d} ge shekem", "register by {d}", "ro‘yxatdan o‘tish {d} gacha", "регистрация до {d}"),
 "x_ielts_note": T("IELTS ushın belgilengen sánesler joq: imtihandı 6–8 hápte aldın jazılıń.", "IELTS has many dates: book 6–8 weeks ahead.", "IELTS sanalari ko‘p: 6–8 hafta oldin yoziling.", "У IELTS много дат: записывайтесь за 6–8 недель."),
 "tl_h": T("Kún-kún joba", "Your timeline", "Sanali reja", "План по датам"),
 "tl_done": T("{a} / {b} orınlandı", "{a} of {b} done", "{a} / {b} bajarildi", "Выполнено {a} из {b}"),
 "past": T("Ótip ketti", "Passed", "O‘tib ketdi", "Прошло"), "nextc": T("Keyingi", "Next", "Keyingi", "Следующее"), "exp": T("shama menen", "expected", "taxminan", "ожидается"),
 "in_d": T("{n} kúnnen keyin", "in {n} days", "{n} kundan keyin", "через {n} дн."), "today": T("búgin", "today", "bugun", "сегодня"),
 "mo_h": T("Qárejet hám byudjet", "Cost vs your budget", "Xarajat va byudjet", "Расходы и бюджет"),
 "mo_b": T("Sizdiń byudjet", "Your budget", "Sizning byudjet", "Ваш бюджет"),
 "mo_note": T("Jılına oqıw + jasaw, AQSh dollarında. Arzan hám ádettegi universitet arasındaǵı aralıq. Bahalar shama menen — Kalkulyatorda tekseriń.", "Tuition plus living per year in US dollars: range from a lower-cost to a typical university. Estimates only; check details in the Calculator.",
              "Yiliga o‘qish + yashash, AQSh dollarida: arzon va oddiy universitet oralig‘i. Taxminiy — Kalkulyatorda tekshiring.", "Обучение и проживание в год, в долларах США: от недорогого до типичного вуза. Это оценка — уточните в Калькуляторе."),
 "sc_h": T("Stipendiyalar", "Scholarships for you", "Siz uchun stipendiyalar", "Стипендии для вас"),
 "sc_warn": T("Tańlaǵan mámleketlerińizde tolıq stipendiya az. Tolıq mámleketlik stipendiyası bar mámleketti qosıwdı oylap kóriń:", "Your chosen countries have few full scholarships. Consider adding a country with a full government scholarship:",
              "Tanlagan davlatlaringizda to‘liq stipendiya kam. To‘liq davlat stipendiyasi bor davlatni qo‘shishni o‘ylab ko‘ring:", "В выбранных странах мало полных стипендий. Подумайте о стране с полной госстипендией:"),
 "sc_need": T("AQSh hám Singapurdıń ayırım top universitetleri xalıqaralıq studentlerge mútájlikke qaray járdem beredi, biraq tańlaw júdá kúshli.", "Some top universities in the US and Singapore give need-based aid to international students, but competition is very strong.",
              "AQSh va Singapurning ayrim top universitetlari xalqaro talabalarga ehtiyojga qarab yordam beradi, lekin tanlov juda kuchli.", "Некоторые топ-вузы США и Сингапура дают помощь по потребности иностранцам, но конкурс очень высокий."),
 "u_h": T("Universitetler dizimi", "University shortlist", "Universitetlar ro‘yxati", "Список вузов"),
 "u_reach": T("Arman", "Reach", "Orzu", "Мечта"),
 "u_note": T("Dizimge 2–3 «arman», 3–4 «sáykes» hám 2 «isenimli» universitet qosıń. Sáykes hám isenimli universitetlerdi mektep másláhátshisi menen birge tańlań.", "A good list has 2–3 reach, 3–4 match and 2 safe universities. Choose match and safe ones together with the school counselor.",
           "Ro‘yxatga 2–3 «orzu», 3–4 «mos» va 2 «ishonchli» universitet qo‘shing. Mos va ishonchli universitetlarni maktab maslahatchisi bilan tanlang.", "В хорошем списке 2–3 «мечты», 3–4 «подходящих» и 2 «надёжных» вуза. Подходящие и надёжные выберите вместе со школьным консультантом."),
 "u_none": T("Tańlaǵan mámleketlerińizde bizdiń Top 10 dizimimizden universitet joq.", "None of our Top 10 universities are in your chosen countries.", "Tanlagan davlatlaringizda bizning Top 10 ro‘yxatimizdan universitet yo‘q.", "В выбранных странах нет вузов из нашего Топ-10."),
 "f_tip": T("Taraw boyınsha másláhát", "Tip for your field", "Soha bo‘yicha maslahat", "Совет по направлению"),
 "print": T("PDF / basıp shıǵarıw", "Save PDF / print", "PDF / chop etish", "PDF / печать"), "share": T("Ata-anaǵa jiberiw", "Share with parents", "Ota-onaga yuborish", "Отправить родителям"),
 "copied": T("Joba teksti kóshirildi.", "Plan text copied.", "Reja matni nusxalandi.", "Текст плана скопирован."),
 "edit": T("Juwaplardı ózgertiw", "Edit answers", "Javoblarni o‘zgartirish", "Изменить ответы"), "reset": T("Basınan baslaw", "Start over", "Boshidan boshlash", "Начать заново"),
 "sure": T("Joba hám belgileriniz óshiriledi. Dawam etemiz be?", "Your plan and ticks will be deleted. Continue?", "Reja va belgilaringiz o‘chiriladi. Davom etamizmi?", "План и отметки будут удалены. Продолжить?"),
 "disc": T("Bul joba — baǵdar, rásmiy kepillik emes. Múddetler hám talaplar jıl sayın ózgeredi: hár qádemdi universitettiń rásmiy saytında tekseriń hám mektep másláhátshisi menen sóylesiń.",
           "This plan is a guide, not a guarantee. Deadlines and requirements change every year: check each step on the official university site and talk to the school counselor.",
           "Bu reja — yo‘nalish, rasmiy kafolat emas. Muddatlar va talablar har yili o‘zgaradi: har bir qadamni universitetning rasmiy saytida tekshiring va maktab maslahatchisi bilan gaplashing.",
           "Этот план — ориентир, а не гарантия. Сроки и требования меняются каждый год: проверяйте каждый шаг на официальном сайте вуза и обсуждайте с консультантом школы."),
 "gap": T("Mektepti pitkergensiz: arzalardı usı mawsımda berip, bir jıl «gap year» etip oqıwǵa kiriwińiz múmkin.", "You have graduated: you can apply this season and start after a gap year.",
          "Maktabni bitirgansiz: arizalarni shu mavsumda topshirib, «gap year» dan keyin o‘qishga kirishingiz mumkin.", "Вы окончили школу: можно подать документы в этом сезоне и начать учёбу после gap year."),
 "late": T("Bul mawsımnıń ayırım múddetleri ótip ketti. Qalǵan múddetlerge tayarlanıń yamasa keyingi jılǵa joba dúziń.", "Some deadlines of this season have passed. Focus on the ones still open, or plan for next year.",
           "Bu mavsumning ayrim muddatlari o‘tib ketdi. Qolganlariga tayyorlaning yoki keyingi yilga reja tuzing.", "Часть сроков этого сезона уже прошла. Сосредоточьтесь на оставшихся или планируйте следующий год."),
 # action items
 "a_dl": T("Keyingi múddet: {t} — {d}", "Next deadline: {t} on {d}", "Keyingi muddat: {t} — {d}", "Следующий срок: {t} — {d}"),
 "a_i0": T("Ingliz tili dárejeńizdi anıqlań: biypul sınaq testin isleń", "Find your English level: do a free practice test", "Ingliz tili darajangizni aniqlang: bepul sinov testini ishlang", "Узнайте свой уровень английского: пройдите бесплатный пробный тест"),
 "a_ig": T("IELTS ta +{g} ball kerek: kúnlik tayarlıq jobasın baslań", "You need +{g} in IELTS: start the daily practice plan", "IELTS da +{g} ball kerak: kunlik tayyorgarlik rejasini boshlang", "Нужно +{g} по IELTS: начните ежедневный план"),
 "a_s0": T("Bluebook qosımshasında biypul SAT sınaq testin isleń", "Take a free full SAT practice test in the Bluebook app", "Bluebook ilovasida bepul SAT sinov testini ishlang", "Пройдите бесплатный пробный SAT в приложении Bluebook"),
 "a_sg": T("SAT maqset {t}+: keyingi imtihan kúnin tańlań", "SAT target {t}+: choose your next test date", "SAT maqsad {t}+: keyingi imtihon sanasini tanlang", "Цель SAT {t}+: выберите следующую дату"),
 "a_mo": T("Tolıq stipendiyası bar mámleketti qosıń (Túrkiya, Vengriya, Koreya, Yaponiya)", "Add a country with full government scholarships (Türkiye, Hungary, Korea, Japan)", "To‘liq stipendiyasi bor davlatni qo‘shing (Turkiya, Vengriya, Koreya, Yaponiya)", "Добавьте страну с полной госстипендией (Турция, Венгрия, Корея, Япония)"),
 "a_es": T("Esse ushın ideyalardı jazıp baslań", "Start collecting ideas for your essay", "Esse uchun g‘oyalarni yozishni boshlang", "Начните собирать идеи для эссе"),
 "a_par": T("Usı jobanı ata-anańızǵa hám mektep másláhátshisine kórsetiń", "Show this plan to your parents and the school counselor", "Ushbu rejani ota-onangiz va maktab maslahatchisiga ko‘rsating", "Покажите этот план родителям и школьному консультанту"),
 # timeline items
 "e_iprep": T("IELTS tayarlıǵın baslaw (maqset {t})", "Start IELTS preparation (target {t})", "IELTS tayyorgarligini boshlash (maqsad {t})", "Начать подготовку к IELTS (цель {t})"),
 "e_itake": T("IELTS imtihanın tapsırıw", "Take the IELTS exam", "IELTS imtihonini topshirish", "Сдать IELTS"),
 "e_iasap": T("IELTS ti múmkinshilikke qaray tez tapsırıń", "Take IELTS as soon as possible", "IELTS ni imkon qadar tez topshiring", "Сдайте IELTS как можно скорее"),
 "e_spr": T("Bluebook ta biypul SAT sınaq testi", "Free SAT practice test in Bluebook", "Bluebook da bepul SAT sinov testi", "Бесплатный пробный SAT в Bluebook"),
 "e_sat": T("SAT imtihan kúni", "SAT test day", "SAT imtihon kuni", "День SAT"),
 "e_satg": T("SAT: báhár yamasa gúz kúnine jazılıń (sánesler College Board saytında)", "SAT: register for a spring or autumn date (dates on the College Board site)", "SAT: bahor yoki kuz sanasiga yoziling (sanalar College Board saytida)", "SAT: запишитесь на весеннюю или осеннюю дату (даты на сайте College Board)"),
 "e_act": T("Jazǵı jumıslar: joybarlar, olimpiadalar, volontyorlıq", "Summer: projects, olympiads, volunteering", "Yozgi ishlar: loyihalar, olimpiadalar, volontyorlik", "Лето: проекты, олимпиады, волонтёрство"),
 "e_actn": T("Bul arzańızdı kúsheytedi.", "These make your application stronger.", "Bu arizangizni kuchaytiradi.", "Это усиливает заявку."),
 "e_pass": T("Pasporttı tekseriń (oqıw dáwirine jaramlı bolsın)", "Check your passport (valid for the whole study period)", "Pasportni tekshiring (o‘qish davriga yaroqli bo‘lsin)", "Проверьте паспорт (действителен на весь срок учёбы)"),
 "e_essay": T("Esse / personal statement jazıwdı baslaw", "Start your essay / personal statement", "Esse / personal statement yozishni boshlash", "Начать эссе / personal statement"),
 "e_rec": T("2 muǵallimnen usınıs xatın soraw", "Ask 2 teachers for recommendation letters", "2 o‘qituvchidan tavsiya xati so‘rash", "Попросить 2 учителей о рекомендациях"),
 "e_tr": T("Bahalar kóshirmesi (transcript) hám rásmiy awdarmalar", "Order transcripts and certified translations", "Baholar ko‘chirmasi (transcript) va rasmiy tarjimalar", "Заказать выписку оценок и заверенные переводы"),
 "e_aid": T("AQSh: qarjılıq járdem formaları (CSS Profile / ISFAA)", "US: financial aid forms (CSS Profile / ISFAA)", "AQSh: moliyaviy yordam shakllari (CSS Profile / ISFAA)", "США: формы финансовой помощи (CSS Profile / ISFAA)"),
 "e_aidn": T("Kóbinese arza menen birge; hár universitettiń múddetin tekseriń.", "Often due with the application; check each university's deadline.", "Ko‘pincha ariza bilan birga; har bir universitet muddatini tekshiring.", "Часто вместе с заявкой; проверьте срок каждого вуза."),
 "e_open": T("{c}: múddetler universitetke qaray hár qıylı — rásmiy saytta tekseriń", "{c}: deadlines differ by university — check the official sites", "{c}: muddatlar universitetga qarab har xil — rasmiy saytda tekshiring", "{c}: сроки зависят от вуза — проверьте на официальных сайтах"),
 "e_usdec": T("AQSh: tiykarǵı nátiyjeler kóbinese mart aqırında keledi", "US: most regular decisions arrive by late March", "AQSh: asosiy natijalar ko‘pincha mart oxirida keladi", "США: основные решения обычно к концу марта"),
 "e_ukdec": T("UK: universitetler may ayına shekem juwap beredi", "UK: universities send decisions by May", "UK: universitetlar may oyigacha javob beradi", "Великобритания: вузы отвечают до мая"),
 "e_visa": T("Student vizasına arza beriw", "Apply for your student visa", "Talaba vizasiga ariza topshirish", "Подать на студенческую визу"),
 "e_visan": T("Ádette oqıw baslanıwınan 2–4 ay aldın.", "Usually 2–4 months before the course starts.", "Odatda o‘qish boshlanishidan 2–4 oy oldin.", "Обычно за 2–4 месяца до начала учёбы."),
 "e_fly": T("Ushıw hám oqıwdı baslaw", "Fly out and start studying", "Uchish va o‘qishni boshlash", "Вылет и начало учёбы"),
 "e_flyn": T("Koreya hám Yaponiyada oqıw kóbinese báhárde (mart/aprel) baslanadı.", "In Korea and Japan studies often start in spring (March/April).", "Koreya va Yaponiyada o‘qish ko‘pincha bahorda (mart/aprel) boshlanadi.", "В Корее и Японии учёба часто начинается весной (март/апрель)."),
}
FIELD_TIP = {
 "eng": T("Matematika hám fizika eń áhmiyetli. Germaniya, Koreya hám Yaponiya injeneriyada kúshli hám salıstırmalı arzan.", "Maths and physics matter most. Germany, Korea and Japan are strong in engineering and relatively affordable.",
          "Matematika va fizika eng muhim. Germaniya, Koreya va Yaponiya muhandislikda kuchli va nisbatan arzon.", "Важнее всего математика и физика. Германия, Корея и Япония сильны в инженерии и относительно доступны."),
 "med": T("Medicina uzaq hám tańlawı kúshli. UK de kóp medicina fakultetleri UCAT testin soraydı hám arza 15-oktyabrge shekem beriledi; AQSh ta medicina bakalavrdan keyin oqıladı.",
          "Medicine is long and very competitive. In the UK most medical schools ask for the UCAT test and the deadline is 15 October; in the US medicine is studied after a bachelor's degree.",
          "Tibbiyot uzoq va tanlovi kuchli. UK da ko‘p tibbiyot fakultetlari UCAT testini so‘raydi va ariza 15-oktabrgacha topshiriladi; AQShda tibbiyot bakalavrdan keyin o‘qiladi.",
          "Медицина — долго и с большим конкурсом. В Великобритании большинство медвузов требуют UCAT, срок подачи — 15 октября; в США медицину изучают после бакалавриата."),
 "bus": T("Matematika hám ingliz tili áhmiyetli. Mektep joybarları, biznes jarısları hám liderlik tájiriybesi arzanı kúsheytedi.", "Maths and English matter. School projects, business competitions and leadership experience strengthen your application.",
          "Matematika va ingliz tili muhim. Maktab loyihalari, biznes musobaqalari va yetakchilik tajribasi arizani kuchaytiradi.", "Важны математика и английский. Школьные проекты, бизнес-конкурсы и опыт лидерства усиливают заявку."),
 "sci": T("Olimpiada nátiyjeleri hám ilimiy joybarlar top universitetlerge arzanı kúsheytedi.", "Olympiad results and research projects strengthen applications to top universities.",
          "Olimpiada natijalari va ilmiy loyihalar top universitetlarga arizani kuchaytiradi.", "Олимпиады и исследовательские проекты усиливают заявку в топ-вузы."),
 "hum": T("Jazıw kónlikpesi eń áhmiyetli: IELTS ta 7.0+ ge umtılıń hám esseni erte baslań.", "Writing matters most: aim for IELTS 7.0+ and start your essay early.",
          "Yozish ko‘nikmasi eng muhim: IELTS da 7.0+ ga intiling va esseni erta boshlang.", "Важнее всего письмо: цельтесь на IELTS 7.0+ и начните эссе заранее."),
 "und": T("Bul ádettegi jaǵday. 2–3 qızıqtıratuǵın tarawdı tańlap, universitet saytlarında pánler dizimin salıstırıń.", "That's normal. Pick 2–3 fields you like and compare the course lists on university websites.",
          "Bu odatiy holat. 2–3 qiziqtirgan sohani tanlab, universitet saytlarida fanlar ro‘yxatini solishtiring.", "Это нормально. Выберите 2–3 интересных направления и сравните программы на сайтах вузов."),
}
FIELD_ICON = {"eng": '<path d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/><path d="M19.400 15a1.700 1.700 0 0 0 .3 1.800l.1.1a2 2 0 1 1-2.800 2.800l-.1-.1a1.700 1.700 0 0 0-1.800-.3 1.700 1.700 0 0 0-1 1.500V21a2 2 0 1 1-4 0v-.1a1.700 1.700 0 0 0-1.100-1.500 1.700 1.700 0 0 0-1.800.3l-.1.1a2 2 0 1 1-2.800-2.800l.1-.1a1.700 1.700 0 0 0 .3-1.800 1.700 1.700 0 0 0-1.500-1H3a2 2 0 1 1 0-4h.1A1.700 1.700 0 0 0 4.600 9a1.700 1.700 0 0 0-.3-1.800l-.1-.1a2 2 0 1 1 2.800-2.800l.1.1a1.700 1.700 0 0 0 1.800.3H9a1.700 1.700 0 0 0 1-1.500V3a2 2 0 1 1 4 0v.1a1.700 1.700 0 0 0 1 1.500 1.700 1.700 0 0 0 1.800-.3l.1-.1a2 2 0 1 1 2.800 2.800l-.1.1a1.700 1.700 0 0 0-.3 1.800V9a1.700 1.700 0 0 0 1.500 1H21a2 2 0 1 1 0 4h-.1a1.700 1.700 0 0 0-1.500 1z"/>',
              "med": '<path d="M12 21s-7-4.500-7-10a4 4 0 0 1 7-2.500A4 4 0 0 1 19 11c0 5.500-7 10-7 10z"/><path d="M12 9v5M9.500 11.500h5"/>',
              "bus": '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
              "sci": '<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3"/><path d="M8 15h8"/>',
              "hum": '<path d="M12 6c-2-1.500-5-2-8-1.500V18c3-.5 6 0 8 1.500 2-1.500 5-2 8-1.500V4.500C17 4 14 4.500 12 6z"/><path d="M12 6v13.500"/>',
              "und": '<circle cx="12" cy="12" r="9"/><path d="M9.500 9a2.500 2.500 0 1 1 3.500 2.300c-.6.300-1 .8-1 1.500V14M12 17h.01"/>'}
AMB_ICON = {"top": '<path d="M12 2.500l2.600 5.300 5.900.9-4.300 4.100 1 5.800L12 15.900l-5.200 2.700 1-5.800L3.500 8.700l5.900-.9z"/>',
            "strong": '<path d="M3 9l9-5 9 5-9 5-9-5z"/><path d="M7 11.500V16c0 1 2.500 2.500 5 2.500s5-1.500 5-2.500v-4.500"/>',
            "value": '<circle cx="12" cy="12" r="9"/><path d="M14.500 9.500c-.5-1-1.500-1.500-2.500-1.500-1.400 0-2.500.8-2.500 2s1.100 1.700 2.500 2 2.500.8 2.500 2-1.100 2-2.500 2c-1 0-2-.5-2.500-1.500M12 6.500v11"/>'}
# typical safe English targets by country (before the goal adjustment) and SAT relevance (2 = expected at most top universities, 1 = sometimes asked)
IELTS = {"usa": 6.5, "uk": 6.5, "canada": 6.5, "singapore": 6.5, "germany": 6.5, "malaysia": 6.0, "hungary": 6.0, "turkey": 6.0, "japan": 6.0, "korea": 5.5}
SATN = {"usa": 2, "singapore": 1}
LOCAL = {"turkey", "korea", "japan"}
FLAG2K = {"🇺🇸": "usa", "🇬🇧": "uk", "🇸🇬": "singapore", "🇹🇷": "turkey", "🇭🇺": "hungary", "🇯🇵": "japan", "🇰🇷": "korea", "🇨🇦": "canada", "🇩🇪": "germany", "🇲🇾": "malaysia"}
UNI2K = {"US": "usa", "UK": "uk", "SG": "singapore"}
SCH2K = {"Turkey": "turkey", "Hungary": "hungary", "Japan": "japan", "South Korea": "korea"}
BUDGET = [1500, 4000, 10000, 22000, 40000]   # USD per year (upper value of each option)
MON = [("Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"),
       ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"),
       ("Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"),
       ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")]

def _cost(k):
    c = CAL.D[k]; r = CAL.RATES[c["cur"]]
    run = (c["food"] + c["tr"] + c["ins"] + c["oth"]) * 12 + c["fee"] + c["fly"]
    lo = (c["tu"][0][0] + c["hs"][0] * 12 + run) / r
    ty = (c["tu"][1][0] + c["hs"][1] * 12 + run) / r
    return int(round(lo, -2)), int(round(ty, -2))

def _data(i, links):
    ui = {k: v[i] for k, v in UI.items()}
    cs = []
    for c in CO.C:
        k = c["k"]; lo, ty = _cost(k)
        sch = [dict(n=s[2] if isinstance(s[2], str) else s[2][i], u=s[0], cov=s[4][i]) for s in __import__("abroad").SCHOL if SCH2K.get(s[1][1]) == k]
        cs.append(dict(k=k, f=c["flag"], n=c["name"][i], tier=c["tier"], sch=c["schol"], u=c["url"], lo=lo, ty=ty, ie=IELTS[k], sat=SATN.get(k, 0), loc=k in LOCAL, sl=sch,
                       r={x: c["rows"][x][i] for x in ("tests", "lang", "schol") if x in c["rows"]}))
    ev = [dict(d=e["d"], k=FLAG2K[e["f"]], t=e["t"][i], n=e["n"][i] if e.get("n") else "", u=e.get("u", ""), e=e.get("s") == "e")
          for e in DL.E if e["c"] in ("uni", "schol") and e["f"] in FLAG2K]
    sat = [dict(d=d, r=r) for d, r, _ in SAT.DATES] + [dict(d=d, r="") for d in SAT.ANT]
    unis = [dict(k=UNI2K[u["c"]], n=u["name"][1 if i == 3 else 0], u=u["url"], s=TP.SEAL[u["key"]][0], col=TP.SEAL[u["key"]][1]) for u in TP.UNIS if u["c"] in UNI2K]
    tips = {k: v[i] for k, v in FIELD_TIP.items()}
    mln = ("mln sum", "mln UZS", "mln so‘m", "млн сум")[i]
    up = [2000, 6000, 15000, 30000]
    big = ["< $2 000", "$2 000 – 6 000", "$6 000 – 15 000", "$15 000 – 30 000", "$30 000+"]
    uz = lambda v: f"{int(round(v * CAL.RATES['UZS'] / 1e6))} {mln}"
    lab = [f"< {uz(up[0])}", f"{uz(up[0]).split()[0]}–{uz(up[1])}", f"{uz(up[1]).split()[0]}–{uz(up[2])}", f"{uz(up[2]).split()[0]}–{uz(up[3])}", f"{uz(up[3])}+"]
    bud = [dict(v=v, big=big[n], l="≈ " + lab[n]) for n, v in enumerate(BUDGET)]
    mong = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"] if i == 3 else None
    return dict(ui=ui, cs=cs, ev=ev, sat=sat, unis=unis, tips=tips, bud=bud, mon=list(MON[i]), mong=mong, lang=i, L=links,
                fi=FIELD_ICON, ai=AMB_ICON)

def body(i, tabs_html, href):
    links = {k: href(v) for k, v in dict(co="abroad/countries/", calc="abroad/calculator/", ck="abroad/checklist/", ielts="ielts/", sat="abroad/sat/", essay="abroad/essay/",
                                          sch="abroad/scholarships/", cal="abroad/calendar/", top="abroad/top10/", app="abroad/applications/").items()}
    data = json.dumps(_data(i, links), ensure_ascii=False, separators=(",", ":"))
    return (f'{tabs_html}<div id="pl" class="pl"><div class="plintro"><h2>{TITLE[i]}</h2><p class="lead2">{UI["intro"][i]}</p></div>'
            f'<div id="plwiz" class="card plwiz"></div><div id="plres" class="plres" hidden></div>'
            f'<p class="note pldisc">{UI["disc"][i]}</p></div><script>var PLD={data};</script><script>{PLAN_JS}</script>')

CTA = T("8 sorawǵa juwap beriń — jeke shet elde oqıw jobańızdı alıń", "Answer 8 questions and get your personal study abroad plan", "8 ta savolga javob bering — shaxsiy xorijda o‘qish rejangizni oling", "Ответьте на 8 вопросов и получите личный план поступления")
CTA_BTN = T("Jobanı dúziw", "Build my plan", "Rejani tuzish", "Составить план")

def banner(i, href):
    return (f'<a class="plcta" href="{href}"><span class="plctai"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/></svg></span>'
            f'<span class="plctat"><b>{TITLE[i]}</b><small>{CTA[i]}</small></span><span class="plctab">{CTA_BTN[i]} →</span></a>')

PLAN_JS = r"""(function(){
var D=PLD,U=D.ui,$=function(i){return document.getElementById(i)},KEY='abroadPlan';
var esc=function(s){return String(s==null?'':s).replace(/[&<>"']/g,function(m){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]})};
var IC=function(p,s){return '<svg viewBox="0 0 24 24" width="'+(s||20)+'" height="'+(s||20)+'" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+p+'</svg>'};
var P={a:{},done:{},step:0,built:false};
try{var raw=localStorage.getItem(KEY);if(raw){var o=JSON.parse(raw);if(o&&o.a)P=Object.assign(P,o)}}catch(e){}
function save(){try{localStorage.setItem(KEY,JSON.stringify(P))}catch(e){}}
var CS={};D.cs.forEach(function(c){CS[c.k]=c});
var now=new Date(),T0=new Date(now.getFullYear(),now.getMonth(),now.getDate());
function pd(s){var p=s.split('-');return new Date(+p[0],+p[1]-1,+(p[2]||1))}
function ds(d){return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2)}
function addD(d,n){var x=new Date(d);x.setDate(x.getDate()+n);return x}
function mn(d){var m=(D.mong||D.mon)[d.getMonth()];return D.lang===1?m:m.toLowerCase()}
function fd(d){return d.getDate()+' '+mn(d)+' '+d.getFullYear()}
function fmtUSD(v){return '$'+Math.round(v).toLocaleString('en-US')}
function rep(s,o){for(var k in o)s=s.split('{'+k+'}').join(o[k]);return s}
/* ---------- wizard ---------- */
var STEPS=[
 {k:'g',q:U.q_grade,h:U.h_grade,o:[9,10,11,12].map(function(n){return {v:n,l:n===12?U.g12:rep(U.g,{n:n}),big:n===12?'✓':String(n)}})},
 {k:'c',q:U.q_c,h:U.h_c,multi:3,o:D.cs.map(function(c){return {v:c.k,l:c.n,flag:c.f}})},
 {k:'f',q:U.q_f,h:U.h_f,o:['eng','med','bus','sci','hum','und'].map(function(k){return {v:k,l:U['f_'+k],ic:D.fi[k]}})},
 {k:'m',q:U.q_a,h:U.h_a,o:['top','strong','value'].map(function(k){return {v:k,l:U['a_'+k],s:U['a_'+k+'_s'],ic:D.ai[k]}})},
 {k:'i',q:U.q_i,h:U.h_i,o:[{v:0,l:U.i0,big:'—'},{v:4.5,l:U.i45,big:'<5'},{v:5,big:'5.0'},{v:5.5,big:'5.5'},{v:6,big:'6.0'},{v:6.5,big:'6.5'},{v:7,big:'7.0'},{v:7.5,big:'7.5+'}]},
 {k:'s',q:U.q_s,h:U.h_s,o:[{v:0,l:U.s0,big:'—'},{v:950,l:U.s950,big:'<1000'},{v:1100,big:'1000–1190'},{v:1270,big:'1200–1340'},{v:1400,big:'1350–1440'},{v:1480,big:'1450+'}]},
 {k:'b',q:U.q_b,h:U.h_b,o:D.bud.map(function(b){return {v:b.v,big:b.big,l:b.l}})},
 {k:'x',q:U.q_x,h:U.h_x,o:[{v:'full',l:U.x_full,big:'★'},{v:'part',l:U.x_part,big:'½'},{v:'none',l:U.x_none,big:'✓'}]}
];
function answered(st){var v=P.a[st.k];return st.multi?(v&&v.length>0):v!==undefined}
function wiz(){
 var st=STEPS[P.step],n=STEPS.length,w=$('plwiz');
 var opts=st.o.map(function(o){var v=P.a[st.k],on=st.multi?(v||[]).indexOf(o.v)>=0:v===o.v;
  return '<button type="button" class="plopt'+(on?' on':'')+(o.flag?' flag':'')+(o.ic?' ic':'')+'" data-v="'+esc(o.v)+'" aria-pressed="'+on+'">'
   +(o.flag?'<span class="plf">'+o.flag+'</span>':o.ic?'<span class="pli">'+IC(o.ic,22)+'</span>':o.big?'<span class="plbig">'+esc(o.big)+'</span>':'')
   +(o.l?'<span class="pll">'+esc(o.l)+'</span>':'')+(o.s?'<small>'+esc(o.s)+'</small>':'')+(on?'<span class="plck">'+IC('<path d="M5 12l5 5L20 7"/>',14)+'</span>':'')+'</button>'}).join('');
 var cnt=st.multi?'<span class="plcnt">'+((P.a[st.k]||[]).length)+' / '+st.multi+'</span>':'';
 w.innerHTML='<div class="plprog"><span style="width:'+Math.round((P.step+1)/n*100)+'%"></span></div>'
  +'<div class="plstep">'+rep(U.step,{n:P.step+1,t:n})+cnt+'</div><h3 class="plq">'+esc(st.q)+'</h3><p class="plh">'+esc(st.h)+'</p>'
  +'<div class="plopts c'+st.k+'">'+opts+'</div><div class="plnav">'
  +(P.step>0?'<button type="button" class="btn s" id="plback">← '+esc(U.back)+'</button>':'<span></span>')
  +'<button type="button" class="btn p" id="plnext"'+(answered(st)?'':' disabled')+'>'+esc(P.step===n-1?U.build:U.next)+(P.step===n-1?' ✓':' →')+'</button></div>';
 [].forEach.call(w.querySelectorAll('.plopt'),function(b){b.onclick=function(){
   var raw=b.dataset.v,o=st.o.filter(function(x){return String(x.v)===raw})[0],v=o.v;
   if(st.multi){var a=(P.a[st.k]||[]).slice(),ix=a.indexOf(v);if(ix>=0)a.splice(ix,1);else{if(a.length>=st.multi)a.shift();a.push(v)}P.a[st.k]=a;save();wiz()}
   else{P.a[st.k]=v;save();wiz();setTimeout(function(){if(P.step<n-1){P.step++;save();wiz();top()}},180)}}});
 if($('plback'))$('plback').onclick=function(){P.step--;save();wiz();top()};
 $('plnext').onclick=function(){if(!answered(st))return;if(P.step<n-1){P.step++;save();wiz();top()}else{P.built=true;save();show()}};
}
function top(){var e=$('pl');if(e&&e.getBoundingClientRect().top<0)e.scrollIntoView({behavior:'smooth'})}
/* ---------- plan logic ---------- */
function calc(){
 var a=P.a,sel=(a.c||[]).map(function(k){return CS[k]}).filter(Boolean),amb=a.m,g=a.g;
 var sY=now.getMonth()>=8?now.getFullYear():now.getFullYear()-1,A=g===12?sY:sY+(11-g),start=A+1;
 var adj=amb==='top'?0.5:amb==='value'?-0.5:0;
 var ieT=0;sel.forEach(function(c){ieT=Math.max(ieT,Math.max(5.5,c.ie+adj))});
 var satNeed=sel.some(function(c){return c.sat===2})?2:sel.some(function(c){return c.sat===1})?1:0;
 var satT=amb==='top'?1450:amb==='strong'?1300:1150;
 var bud=a.b,x=a.x;
 /* countries */
 var fits=sel.map(function(c){
  var R=[],pts=0,money=a.b>=c.ty?2:a.b>=c.lo?1:0;
  if(x==='full'){if(c.sch==='gov'){pts+=3;R.push(['ok',U.s_gov])}else if(c.sch==='need'){pts+=1;R.push(['warn',U.s_need])}else{R.push(['no',U.s_none])}}
  else{if(money===2){pts+=3;R.push(['ok',U.m_ok])}else if(money===1){pts+=2;R.push(['warn',U.m_lo])}else if(c.sch==='gov'){pts+=2;R.push(['warn',U.m_no+' · '+U.s_gov])}else if(c.sch==='need'){pts+=1;R.push(['warn',U.m_no+' · '+U.s_need])}else R.push(['no',U.m_no])}
  var t=Math.max(5.5,c.ie+adj),gp=Math.round((t-(a.i||0))*10)/10,young=g<=10;
  if(!a.i){pts+=young?1:0;R.push(['warn',rep(U.e_none,{t:t.toFixed(1)})])}else if(gp<=0){pts+=2;R.push(['ok',rep(U.e_ok,{t:t.toFixed(1)})])}else{pts+=gp<=1||young?1:0;R.push([gp<=1?'warn':'no',rep(U.e_gap,{t:t.toFixed(1),g:gp.toFixed(1)})])}
  if(c.sat){if(a.s>=satT){pts+=2;R.push(['ok',U.t_ok])}else{pts+=(a.s>=satT-150||young)?1:0;R.push([c.sat===2?'warn':'info',rep(U.t_gap,{t:satT})])}}else{pts+=2;R.push(['ok',U.t_no])}
  if(c.loc)R.push(['info',U.loc]);
  return {c:c,fit:pts>=6?2:pts>=4?1:0,R:R,money:money}});
 /* timeline */
 var ev=[],shift=A-2026,usuk=sel.some(function(c){return ['usa','uk','singapore'].indexOf(c.k)>=0}),ks=sel.map(function(c){return c.k});
 function E(id,d,cat,t,n,u,exp,flag){ev.push({id:id,d:d,cat:cat,t:t,n:n||'',u:u||'',exp:!!exp,f:flag||''})}
 function at(m,d,y){return new Date(y==null?A:y,m-1,d)}
 function fut(d,fallback){return d<T0?addD(T0,fallback):d}
 D.ev.forEach(function(e,n){if(ks.indexOf(e.k)<0)return;var d=pd(e.d);d.setFullYear(d.getFullYear()+shift);E('dl'+n,d,'dl',e.t,e.n,e.u,e.e||shift>0,CS[e.k].f)});
 ['canada','germany','korea','malaysia'].forEach(function(k){if(ks.indexOf(k)>=0)E('op'+k,fut(at(10,1),21),'dl',rep(U.e_open,{c:CS[k].n}),'',CS[k].u,true,CS[k].f)});
 var ieBy=usuk?at(9,30):at(10,31),prepW=!a.i?24:Math.max(4,Math.min(24,Math.round((ieT-a.i)*16)));
 if(a.i<ieT){var ps=addD(ieBy,-prepW*7);E('iprep',ps<T0?T0:ps,'exam',rep(U.e_iprep,{t:ieT.toFixed(1)}),rep(U.x_prep,{w:prepW}),D.L.ielts);
  if(ieBy<addD(T0,42))E('itake',addD(T0,Math.max(42,prepW*7)),'exam',U.e_iasap,U.x_ielts_note,D.L.ielts);else E('itake',ieBy,'exam',U.e_itake,U.x_ielts_note,D.L.ielts)}
 var satList=[];
 if(satNeed&&a.s<satT){E('spr',addD(T0,14),'exam',U.e_spr,'',D.L.sat);
  D.sat.forEach(function(s){var d=pd(s.d);if(d>T0&&(!s.r||addD(pd(s.r),4)>=T0)&&d<=at(12,31)&&satList.length<2){satList.push(s);E('sat'+s.d,d,'exam',U.e_sat,s.r?rep(U.x_reg,{d:fd(pd(s.r))}):'',D.L.sat)}});
  if(!satList.length)E('satg',fut(at(3,1),30),'exam',U.e_satg,'',D.L.sat)}
 if(g<=10)E('act',at(6,15),'school',U.e_act,U.e_actn);
 E('pass',fut(at(6,1),14),'doc',U.e_pass,'',D.L.ck);
 if(usuk||ks.indexOf('canada')>=0)E('essay',fut(at(6,1),7),'app',U.e_essay,'',D.L.essay);
 if(usuk||ks.indexOf('canada')>=0)E('rec',fut(at(9,15),10),'doc',U.e_rec,'',D.L.ck);
 E('tr',fut(at(9,1),14),'doc',U.e_tr,'',D.L.ck);
 if(ks.indexOf('usa')>=0)E('aid',fut(at(11,1),14),'money',U.e_aid,U.e_aidn,D.L.sch);
 if(ks.indexOf('usa')>=0)E('usdec',at(3,31,start),'app',U.e_usdec,'',D.L.app);
 if(ks.indexOf('uk')>=0)E('ukdec',at(5,15,start),'app',U.e_ukdec,'',D.L.app);
 E('visa',at(5,15,start),'visa',U.e_visa,U.e_visan,D.L.ck);
 E('fly',at(8,20,start),'go',U.e_fly,(ks.indexOf('korea')>=0||ks.indexOf('japan')>=0)?U.e_flyn:'');
 ev.sort(function(p,q){return p.d-q.d});
 var firstDl=ev.filter(function(e){return e.cat==='dl'&&e.d>=T0&&e.id.indexOf('op')!==0})[0],passedDl=ev.some(function(e){return e.cat==='dl'&&e.d<T0});
 /* readiness */
 var sE=!a.i?(g<=10?8:3):a.i>=ieT?25:ieT-a.i<=0.5?17:ieT-a.i<=1?10:5;
 var sT=!satNeed?25:a.s>=satT?25:a.s>=satT-150?16:a.s?9:(g<=10?9:4);
 var cheap=Math.min.apply(null,sel.map(function(c){return c.lo})),hasGov=sel.some(function(c){return c.sch==='gov'}),hasNeed=sel.some(function(c){return c.sch==='need'});
 var sM=x==='full'?(hasGov?18:hasNeed?10:4):bud>=Math.min.apply(null,sel.map(function(c){return c.ty}))?25:bud>=cheap?19:hasGov?14:hasNeed?8:4;
 var mo=firstDl?(firstDl.d-T0)/864e5/30:(at(12,1)-T0)/864e5/30,sTi=mo>18?25:mo>9?21:mo>4?14:mo>1.5?9:5;
 var score=sE+sT+sM+sTi;
 return {sel:sel,fits:fits,ev:ev,A:A,start:start,ieT:ieT,satNeed:satNeed,satT:satT,satList:satList,prepW:prepW,ieBy:ieBy,score:score,parts:[[U.k_eng,sE],[U.k_test,sT],[U.k_money,sM],[U.k_time,sTi]],firstDl:firstDl,passedDl:passedDl,hasGov:hasGov,hasNeed:hasNeed};
}
var CAT={dl:['#a3202c','<path d="M12 8v4l3 2"/><circle cx="12" cy="12" r="9"/>'],exam:['#7c3aed','<path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/>'],doc:['#0b7a8f','<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>'],
 app:['#2a7fd1','<path d="M4 20h4L18.500 9.500a2.800 2.800 0 0 0-4-4L4 16v4z"/>'],money:['#d97706','<circle cx="12" cy="12" r="9"/><path d="M14.500 9.500c-.5-1-1.500-1.500-2.500-1.500-1.400 0-2.500.8-2.500 2s1.100 1.700 2.500 2 2.500.8 2.500 2-1.100 2-2.500 2c-1 0-2-.5-2.500-1.500M12 6.500v11"/>'],
 visa:['#15803d','<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="12" r="2.500"/><path d="M14 10h4M14 14h3"/>'],school:['#be185d','<path d="M12 2.500l2.600 5.300 5.900.9-4.300 4.100 1 5.800L12 15.900l-5.200 2.700 1-5.800L3.500 8.700l5.900-.9z"/>'],
 go:['#0b5f78','<path d="M2 16l20-8-8 14-2-6z"/>']};
function show(){
 var R=calc(),a=P.a,w=$('plwiz'),r=$('plres');w.hidden=true;r.hidden=false;
 var sc=R.score,lv=sc>=80?3:sc>=60?2:sc>=40?1:0,C=2*Math.PI*52;
 var gl=a.g===12?U.g12:rep(U.g,{n:a.g});
 var hero='<section class="plhero"><div class="plht"><small>'+esc(U.r_for)+'</small><h3>'+R.sel.map(function(c){return c.f}).join(' ')+' '+esc(R.sel.map(function(c){return c.n}).join(' · '))+'</h3>'
  +'<div class="plchips"><span>'+esc(gl)+'</span><span>'+IC(D.fi[a.f],14)+esc(U['f_'+a.f])+'</span><span>'+esc(U.r_start)+': '+esc(D.mon[8])+' '+R.start+'</span></div>'
  +'<div class="plparts">'+R.parts.map(function(p){return '<div><span>'+esc(p[0])+'</span><i><b style="width:'+(p[1]*4)+'%"></b></i></div>'}).join('')+'</div></div>'
  +'<div class="plring"><svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="52" class="rb"/><circle cx="60" cy="60" r="52" class="rf l'+lv+'" style="stroke-dasharray:'+C+';stroke-dashoffset:'+(C*(1-sc/100))+'" transform="rotate(-90 60 60)"/></svg><div><b>'+sc+'</b><small>'+esc(U.ready)+'</small><em class="l'+lv+'">'+esc(U['rl'+lv])+'</em></div></div></section>';
 var notes='';if(a.g===12)notes+='<p class="plnote">'+esc(U.gap)+'</p>';if(R.passedDl&&(a.g>=11))notes+='<p class="plnote warn">'+esc(U.late)+'</p>';
 /* actions */
 var acts=[];
 if(R.firstDl&&(R.firstDl.d-T0)/864e5<=75)acts.push(['dl',rep(U.a_dl,{t:R.firstDl.t,d:fd(R.firstDl.d)}),R.firstDl.u]);
 if(!a.i)acts.push(['exam',U.a_i0,D.L.ielts]);else if(a.i<R.ieT)acts.push(['exam',rep(U.a_ig,{g:(R.ieT-a.i).toFixed(1)}),D.L.ielts]);
 if(R.satNeed&&!a.s)acts.push(['exam',U.a_s0,D.L.sat]);else if(R.satNeed&&a.s<R.satT)acts.push(['exam',rep(U.a_sg,{t:R.satT}),D.L.sat]);
 if(a.x==='full'&&!R.hasGov)acts.push(['money',U.a_mo,D.L.sch]);
 if(acts.length<3&&R.sel.some(function(c){return ['usa','uk','canada','singapore'].indexOf(c.k)>=0}))acts.push(['app',U.a_es,D.L.essay]);
 acts=acts.slice(0,3);acts.push(['school',U.a_par,'']);
 var week='<section class="card plsec"><h3 class="plsh">'+IC('<path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/>')+esc(U.week_h)+'</h3><ol class="placts">'
  +acts.map(function(x){return '<li style="--cc:'+CAT[x[0]][0]+'"><span class="plai">'+IC(CAT[x[0]][1],18)+'</span>'+(x[2]?'<a href="'+esc(x[2])+'">'+esc(x[1])+' →</a>':'<span>'+esc(x[1])+'</span>')+'</li>'}).join('')+'</ol>'
  +'<div class="pltip"><b>'+IC(D.fi[a.f],16)+esc(U.f_tip)+'</b><p>'+esc(D.tips[a.f])+'</p></div></section>';
 /* countries */
 var cc='<section class="plsec"><h3 class="plsh">'+IC('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>')+esc(U.c_h)+'</h3><div class="plcgrid">'
  +R.fits.map(function(F){var c=F.c,rows='';for(var k in c.r)rows+='<dt>'+esc(U['r_'+k])+'</dt><dd>'+esc(c.r[k])+'</dd>';
   return '<article class="card plc f'+F.fit+'"><header><span class="plcf">'+c.f+'</span><div><h4>'+esc(c.n)+'</h4><span class="plfit">'+esc(U['fit'+F.fit])+'</span></div></header>'
   +'<div class="plcost"><small>'+esc(U.cost_y)+'</small><b>'+(c.lo===0&&c.ty===0?'$0':fmtUSD(c.lo)+' – '+fmtUSD(c.ty))+'</b></div>'
   +'<ul class="plr">'+F.R.map(function(x){return '<li class="'+x[0]+'">'+esc(x[1])+'</li>'}).join('')+'</ul>'
   +'<details><summary>'+esc(U.more)+'</summary><dl>'+rows+'</dl></details>'
   +'<div class="plcl"><a href="'+esc(D.L.co)+'">'+esc(U.cmp)+' →</a><a href="'+esc(c.u)+'" target="_blank" rel="noopener">'+esc(U.official)+' ↗</a></div></article>'}).join('')+'</div></section>';
 /* exams */
 var ieBox='<div class="plex"><h4>IELTS</h4><div class="plexn"><div><small>'+esc(U.x_now)+'</small><b>'+(a.i?a.i.toFixed(1):'—')+'</b></div><span class="plarr">→</span><div><small>'+esc(U.x_goal)+'</small><b>'+R.ieT.toFixed(1)+'</b></div></div>'
  +(a.i>=R.ieT?'<p class="ok">'+esc(U.x_done)+'</p>':'<p>'+esc(rep(U.x_prep,{w:R.prepW}))+'</p><p><b>'+esc(U.x_by)+':</b> '+esc(fd(R.ieBy<addD(T0,42)?addD(T0,Math.max(42,R.prepW*7)):R.ieBy))+'</p><p class="note">'+esc(U.x_ielts_note)+'</p>')
  +'<a class="btn s" href="'+esc(D.L.ielts)+'">IELTS →</a></div>';
 var satBox=R.satNeed?'<div class="plex"><h4>SAT</h4><div class="plexn"><div><small>'+esc(U.x_now)+'</small><b>'+(a.s?(a.s===950?'<1000':a.s===1480?'1450+':a.s):'—')+'</b></div><span class="plarr">→</span><div><small>'+esc(U.x_goal)+'</small><b>'+R.satT+'+</b></div></div>'
  +(a.s>=R.satT?'<p class="ok">'+esc(U.t_ok)+'</p>':R.satList.length?'<p><b>'+esc(U.x_sat_dates)+':</b></p><ul class="plsat">'+R.satList.map(function(s){return '<li><b>'+esc(fd(pd(s.d)))+'</b>'+(s.r?'<small>'+esc(rep(U.x_reg,{d:fd(pd(s.r))}))+'</small>':'<small>'+esc(U.exp)+'</small>')+'</li>'}).join('')+'</ul>':'<p>'+esc(U.e_satg)+'</p>')
  +'<a class="btn s" href="'+esc(D.L.sat)+'">SAT →</a></div>':'';
 var ex='<section class="card plsec"><h3 class="plsh">'+IC(CAT.exam[1])+esc(U.x_h)+'</h3><div class="plexg">'+ieBox+satBox+'</div></section>';
 /* timeline */
 var nx=R.ev.filter(function(e){return e.d>=T0&&!P.done[e.id]})[0],cur='',tl='',dn=R.ev.filter(function(e){return P.done[e.id]}).length;
 R.ev.forEach(function(e){var m=D.mon[e.d.getMonth()]+' '+e.d.getFullYear();if(m!==cur){tl+=(cur?'</ol>':'')+'<h4 class="plmo">'+esc(m)+'</h4><ol class="pltl">';cur=m}
  var past=e.d<T0,dd=Math.round((e.d-T0)/864e5),isN=nx&&nx.id===e.id,ck=!!P.done[e.id];
  tl+='<li class="'+(ck?'done ':'')+(past&&!ck?'past ':'')+(isN?'next':'')+'" style="--cc:'+CAT[e.cat][0]+'"><label class="plchk"><input type="checkbox" data-id="'+e.id+'"'+(ck?' checked':'')+'><span>'+IC('<path d="M5 12l5 5L20 7"/>',14)+'</span></label>'
   +'<span class="plti">'+IC(CAT[e.cat][1],16)+'</span><div class="pltx"><div class="plttop"><time>'+esc(e.d.getDate()+' '+D.mon[e.d.getMonth()].toLowerCase())+'</time>'
   +(isN?'<em class="b n">'+esc(U.nextc)+'</em>':'')+(past&&!ck?'<em class="b p">'+esc(U.past)+'</em>':'')+(!past&&dd<=60?'<em class="b s">'+esc(dd===0?U.today:rep(U.in_d,{n:dd}))+'</em>':'')+(e.exp?'<em class="b e">'+esc(U.exp)+'</em>':'')+'</div>'
   +'<b>'+(e.f?e.f+' ':'')+esc(e.t)+'</b>'+(e.n?'<small>'+esc(e.n)+'</small>':'')+(e.u?'<a href="'+esc(e.u)+'"'+(/^https?:/.test(e.u)?' target="_blank" rel="noopener"':'')+'>'+esc(U.more)+' →</a>':'')+'</div></li>'});
 tl+='</ol>';
 var tls='<section class="card plsec"><h3 class="plsh">'+IC('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>')+esc(U.tl_h)+'</h3><div class="pltlp"><span>'+esc(rep(U.tl_done,{a:dn,b:R.ev.length}))+'</span><i><b style="width:'+Math.round(dn/R.ev.length*100)+'%"></b></i></div>'+tl+'</section>';
 /* money */
 var mx=Math.max(a.b,Math.max.apply(null,R.sel.map(function(c){return c.ty})))*1.08||1;
 var mo='<section class="card plsec"><h3 class="plsh">'+IC(CAT.money[1])+esc(U.mo_h)+'</h3><div class="plmo2">'
  +R.sel.map(function(c){var st=a.b>=c.ty?'ok':a.b>=c.lo?'warn':'no';return '<div class="plmr '+st+'"><span>'+c.f+' '+esc(c.n)+'</span><div class="plmb"><i style="left:'+(c.lo/mx*100)+'%;width:'+Math.max(1.5,(c.ty-c.lo)/mx*100)+'%"></i><u style="left:'+(a.b/mx*100)+'%"></u></div><b>'+fmtUSD(c.lo)+'–'+fmtUSD(c.ty)+'</b></div>'}).join('')
  +'<div class="plml"><u></u> '+esc(U.mo_b)+': '+esc(D.bud.filter(function(b){return b.v===a.b})[0].big)+'</div></div><p class="note">'+esc(U.mo_note)+'</p><a class="btn s" href="'+esc(D.L.calc)+'">'+esc(U.k_money)+' →</a></section>';
 /* scholarships */
 var sl=[];R.sel.forEach(function(c){c.sl.forEach(function(s){sl.push([c,s])})});
 var sch='<section class="card plsec"><h3 class="plsh">'+IC('<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0zM17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>')+esc(U.sc_h)+'</h3>'
  +(sl.length?'<div class="plsl">'+sl.map(function(p){return '<a class="plsch" href="'+esc(p[1].u)+'" target="_blank" rel="noopener"><span>'+p[0].f+'</span><div><b>'+esc(p[1].n)+'</b><small>'+esc(p[1].cov)+'</small></div><em>↗</em></a>'}).join('')+'</div>':'')
  +(R.hasNeed?'<p class="plnote">'+esc(U.sc_need)+'</p>':'')
  +((a.x!=='none'&&!R.hasGov)?'<p class="plnote warn">'+esc(U.sc_warn)+' '+D.cs.filter(function(c){return c.sch==='gov'}).map(function(c){return c.f+' '+esc(c.n)}).join(', ')+'</p>':'')
  +'<a class="btn s" href="'+esc(D.L.sch)+'">'+esc(U.r_schol)+' →</a></section>';
 /* universities */
 var un=D.unis.filter(function(u){return R.sel.some(function(c){return c.k===u.k})});
 var uni='<section class="card plsec"><h3 class="plsh">'+IC(D.ai.strong)+esc(U.u_h)+'</h3>'
  +(un.length?'<div class="plun">'+un.map(function(u){return '<a href="'+esc(u.u)+'" target="_blank" rel="noopener"><span class="plseal" style="background:'+u.col+'">'+esc(u.s)+'</span><b>'+esc(u.n)+'</b><em>'+esc(U.u_reach)+'</em></a>'}).join('')+'</div>':'<p class="note">'+esc(U.u_none)+'</p>')
  +'<p class="plnote">'+esc(U.u_note)+'</p><a class="btn s" href="'+esc(D.L.top)+'">Top 10 →</a></section>';
 var tools='<div class="pltools"><button type="button" class="btn p" id="plprint">'+IC('<path d="M6 9V3h12v6M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><path d="M6 14h12v7H6z"/>',18)+esc(U.print)+'</button>'
  +'<button type="button" class="btn s" id="plshare">'+IC('<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.600 13.500l6.800 4M15.400 6.500l-6.800 4"/>',18)+esc(U.share)+'</button>'
  +'<button type="button" class="btn s" id="pledit">'+esc(U.edit)+'</button><button type="button" class="pllink" id="plreset">'+esc(U.reset)+'</button><span id="plmsg" class="plmsgx" role="status"></span></div>';
 r.innerHTML=hero+notes+tools+week+cc+ex+tls+mo+sch+uni;
 [].forEach.call(r.querySelectorAll('.pltl input'),function(b){b.onchange=function(){if(b.checked)P.done[b.dataset.id]=1;else delete P.done[b.dataset.id];save();var y=window.scrollY;show();window.scrollTo(0,y)}});
 $('plprint').onclick=function(){window.print()};
 $('pledit').onclick=function(){P.step=0;save();r.hidden=true;w.hidden=false;wiz();top()};
 $('plreset').onclick=function(){if(confirm(U.sure)){P={a:{},done:{},step:0,built:false};save();r.hidden=true;w.hidden=false;wiz();top()}};
 $('plshare').onclick=function(){
  var txt=U.r_for+': '+R.sel.map(function(c){return c.f+' '+c.n}).join(', ')+'\n'+U.ready+': '+R.score+'/100 ('+U['rl'+lv]+')\n'+U.r_start+': '+D.mon[8]+' '+R.start+'\nIELTS: '+(a.i||'—')+' → '+R.ieT.toFixed(1)+(R.satNeed?'\nSAT: '+(a.s||'—')+' → '+R.satT+'+':'')+'\n\n'+U.tl_h+':\n'
   +R.ev.filter(function(e){return e.d>=T0}).slice(0,8).map(function(e){return '• '+fd(e.d)+' — '+e.t}).join('\n')+'\n\n'+location.href;
  if(navigator.share){navigator.share({title:document.title,text:txt}).catch(function(){})}
  else if(navigator.clipboard){navigator.clipboard.writeText(txt).then(function(){$('plmsg').textContent=U.copied})}};
 top();
}
if(P.built&&P.a.c&&P.a.c.length&&P.a.x)show();else wiz();
})();"""
