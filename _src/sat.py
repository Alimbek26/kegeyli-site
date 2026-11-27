import json
NAME = ("SAT qollanbası", "SAT guide", "SAT qo‘llanmasi", "Гид по SAT")
TAB = ("SAT", "SAT", "SAT", "SAT")
DESC = ("Digital SAT haqqında hámmesi: dúzilisi, mánisi, sanalar hám múddetler, qaysı universitetlerge kerek, tayarlıq rejesi hám imtixan kúni dizimi.",
        "Everything about the digital SAT: format, scoring, test dates and deadlines, which universities need it, a study plan and an exam-day checklist.",
        "Digital SAT haqida hammasi: tuzilishi, ballar, sanalar va muddatlar, qaysi universitetlarga kerak, tayyorlanish rejasi va imtihon kuni ro‘yxati.",
        "Всё о цифровом SAT: формат, баллы, даты и дедлайны, каким вузам он нужен, план подготовки и чек-лист на день экзамена.")
def T(a, b, c, d): return (a, b, c, d)
UI = {
 "intro": T("SAT — AQSh universitetleri soraytuǵın standart test. Tómende ol qanday dúzilgeni, qansha turatuǵını, qaysı sanada tapsırıwǵa bolatuǵını hám sizge kerek-kermesligin kóriń.",
            "The SAT is the standard test many US universities ask for. Below: how it is built, what it costs, which dates are open, and whether you need it at all.",
            "SAT — AQSh universitetlari ko‘p so‘raydigan standart test. Quyida: u qanday tuzilgan, qancha turadi, qaysi sanalarda topshirish mumkin va sizga kerak-kerakmasligi.",
            "SAT — стандартный тест, который требуют многие вузы США. Ниже: как он устроен, сколько стоит, какие даты открыты и нужен ли он вам вообще."),
 "tiles": (T(("2 saat 14 min", "Tek tapsırıw waqtı"), ("2 h 14 min", "Testing time"), ("2 soat 14 daq.", "Test vaqti"), ("2 ч 14 мин", "Время теста")),
           T(("98", "Soraw"), ("98", "Questions"), ("98", "Savol"), ("98", "Вопроса")),
           T(("400–1600", "Ball shkalası"), ("400–1600", "Score scale"), ("400–1600", "Ball shkalasi"), ("400–1600", "Шкала баллов")),
           T(("$111", "Shet elde: $68 + $43"), ("$111", "Outside the US: $68 + $43"), ("$111", "Chet elda: $68 + $43"), ("$111", "Вне США: $68 + $43"))),
 "h_fmt": T("Test qanday dúzilgen", "How the test is built", "Test qanday tuzilgan", "Как устроен тест"),
 "fmt_p": T("Test kompyuterde (Bluebook programması) tapsırıladı. Eki bólim bar, hár biri eki moduldan turadı. Ekinshi modul birinshi modulda qanshelli juwap bergenińizge qarap jeńilirek yamasa qıyınıraq boladı (adaptiv).",
            "The test is taken on a computer in the Bluebook app. It has two sections, each with two modules. The second module is easier or harder depending on how you did in the first (adaptive), so try your best on every question.",
            "Test kompyuterda (Bluebook ilovasi) topshiriladi. Ikki bo‘lim bor, har biri ikki moduldan iborat. Ikkinchi modul birinchisidagi natijangizga qarab osonroq yoki qiyinroq bo‘ladi (adaptiv).",
            "Тест сдаётся на компьютере в приложении Bluebook. Два раздела, в каждом по два модуля. Второй модуль легче или сложнее — в зависимости от результата в первом (адаптивный тест)."),
 "m_rw": T("Oqıw hám jazıw", "Reading & Writing", "O‘qish va yozish", "Чтение и письмо"), "m_m": T("Matematika", "Math", "Matematika", "Математика"),
 "m_br": T("Tanaffus 10 min", "10-min break", "Tanaffus 10 daq.", "Перерыв 10 мин"), "min": T("min", "min", "daq.", "мин"), "q": T("soraw", "questions", "savol", "вопросов"),
 "score_p": T("Hár bólim 200–800 ball, jámi 400–1600. Ortasha nátiyje shama menen 1000 ball.", "Each section is scored 200–800; the total is 400–1600. A typical score is around 1000.", "Har bir bo‘lim 200–800 ball, jami 400–1600. O‘rtacha natija taxminan 1000 ball.", "Каждый раздел оценивается от 200 до 800, итого 400–1600. Средний результат — около 1000."),
 "h_dates": T("Test sanaları hám múddetler", "Test dates and deadlines", "Test sanalari va muddatlar", "Даты и дедлайны"),
 "dates_p": T("Sanalar barlıq mámleketler ushın birdey. Múddetler AQSh waqtı boyınsha 23:59 da tawsıladı. Keshigip dizimnen ótiw $38, sanani ózgertiw $34.",
              "Dates are the same worldwide. Deadlines end at 11:59 p.m. US Eastern time. Late registration costs $38 extra; changing a date costs $34.",
              "Sanalar butun dunyo uchun bir xil. Muddatlar AQSh sharqiy vaqti bilan 23:59 da tugaydi. Kechikib ro‘yxatdan o‘tish $38, sanani o‘zgartirish $34.",
              "Даты одинаковы для всех стран. Дедлайны заканчиваются в 23:59 по восточному времени США. Поздняя регистрация — $38, перенос даты — $34."),
 "test": T("Test", "Test", "Test", "Тест"), "reg": T("Dizimnen ótiw", "Register by", "Ro‘yxat", "Регистрация до"), "late": T("Keshigip (+$38)", "Late (+$38)", "Kechikib (+$38)", "Поздно (+$38)"),
 "closed": T("Jabıldı", "Closed", "Yopildi", "Закрыто"), "lateonly": T("Tek keshigip", "Late only", "Faqat kechikib", "Только поздно"), "open": T("Ashıq", "Open", "Ochiq", "Открыто"),
 "left": T("{n} kún qaldı", "{n} days left", "{n} kun qoldi", "осталось {n} дн."), "ant": T("Boljanǵan sanalar (2027-gúz) — rásmiy saytta tastıyıqlań", "Expected fall 2027 dates — confirm on the official site", "Kutilayotgan sanalar (2027-kuz) — rasmiy saytda tasdiqlang", "Ожидаемые даты (осень 2027) — подтвердите на официальном сайте"),
 "which": T("Qaysısın tańlaw kerek? 11-klass oqıwshıları ushın: gúzgi arza jibermesten aldın 2 ret tapsırıp kóriw ushın bahar (mart–iyun) hám jaz-gúz sanaların rejelestiriń. 12-klasstaǵılar ushın hár bir universitettiń sońǵı qabıl etetuǵın sanasın tekseriń.",
           "Which to pick? Aim for two attempts before you apply, e.g. spring 2027 and early autumn 2027, so a retake is possible. If you are applying right now, check each university’s last accepted test date.",
           "Qaysini tanlash kerak? Ariza topshirishdan oldin 2 marta topshirishni rejalashtiring: masalan, 2027-bahor va kuz boshi. Hozir ariza topshirayotgan bo‘lsangiz, har bir universitetning oxirgi qabul qiladigan sanasini tekshiring.",
           "Что выбрать? Планируйте две попытки до подачи документов: например, весна 2027 и начало осени 2027 — тогда останется время на пересдачу. Если подаёте сейчас, проверьте последнюю принимаемую дату у каждого вуза."),
 "h_need": T("Maǵan SAT kerek pe?", "Do I need the SAT?", "Menga SAT kerakmi?", "Нужен ли мне SAT?"),
 "need_p": T("Hár bir universitettiń óz qaǵıydası bar. Tańlaǵan baǵdarıńızdıń betin tekseriń.", "Every university sets its own rule. Always check the page of your chosen programme.", "Har bir universitetning o‘z qoidasi bor. Tanlagan yo‘nalishingiz sahifasini tekshiring.", "У каждого вуза свои правила. Проверяйте страницу выбранной программы."),
 "h_range": T("Joqarı universitetlerde ball", "Scores at top universities", "Top universitetlarda ball", "Баллы в топ-вузах"),
 "range_p": T("Qabıl etilgen oqıwshılardıń ortasha 50 % ballı. Ballıńızdı kiritip salıstırıp kóriń.", "The middle 50% of scores of admitted students. Type your score to compare.", "Qabul qilinganlarning o‘rtadagi 50% bali. O‘z ballingizni kiritib solishtiring.", "Средние 50% баллов поступивших. Введите свой балл и сравните."),
 "myscore": T("Meniń ballım", "My score", "Mening ballim", "Мой балл"), "below": T("{n} ball kem", "{n} points below", "{n} ball kam", "ниже на {n}"), "inside": T("Aralıqta", "Inside the range", "Oraliqda", "В диапазоне"), "above": T("Joqarıda", "Above the range", "Oraliqdan yuqori", "Выше диапазона"),
 "range_note": T("Bul ball — kepil emes: universitetler oqıw bahaların, esseni hám jetiskenliklerdi de qaraydı.", "A score is not a guarantee: universities also read grades, essays and achievements.", "Ball kafolat emas: universitetlar baholar, esse va yutuqlarni ham ko‘radi.", "Балл — не гарантия: вузы смотрят также оценки, эссе и достижения."),
 "h_plan": T("Tayarlıq rejesi", "Your study plan", "Tayyorgarlik rejasi", "План подготовки"),
 "plan_p": T("Test sanasın tańlań — reje qalǵan háptege qarap dúziledi.", "Pick a test date — the plan adapts to the weeks you have left.", "Test sanasini tanlang — reja qolgan haftalarga moslashadi.", "Выберите дату теста — план подстроится под оставшиеся недели."),
 "weeks": T("{n} hápte", "{n} weeks", "{n} hafta", "{n} нед."), "wk": T("{a}–{b}-hápte", "Weeks {a}–{b}", "{a}–{b}-hafta", "Недели {a}–{b}"), "wk1": T("{a}-hápte", "Week {a}", "{a}-hafta", "Неделя {a}"),
 "tight": T("Waqıt az. Reje qısqartılǵan; mümkin bolsa keyingi sanaǵa kóshiriw haqqında oylań.", "Time is tight. The plan is squeezed; consider a later date if you can.", "Vaqt kam. Reja qisqartirilgan; imkon bo‘lsa, keyingi sanani o‘ylab ko‘ring.", "Времени мало. План сжат; по возможности рассмотрите более позднюю дату."),
 "ph": (T("Baslang‘ısh test hám qáteler", "Diagnostic test and gaps", "Boshlang‘ich test va bo‘shliqlar", "Диагностика и пробелы"),
        T("Bluebook ishinde tolıq sınaq testin tapsırıń, hár bir qátege sebep jazıń. Qaysı temalar álsiz ekenin dizimge alıń.", "Take one full practice test in Bluebook and write down why you missed each question. List your weakest topics.", "Bluebook’da to‘liq sinov testini topshiring va har bir xato sababini yozing. Zaif mavzularni ro‘yxatga oling.", "Пройдите полный пробный тест в Bluebook и запишите причину каждой ошибки. Составьте список слабых тем.")),
 "ph2": (T("Temalar boyınsha jumıs", "Topic practice", "Mavzular bo‘yicha ishlash", "Работа по темам"),
         T("Álsiz temalardı Khan Academy hám Bluebook sorawları menen kúnine 45–60 min jumıs islep shıǵıń. Matematikada formulalar, oqıwda grammatika qaǵıydaların úyreniń.", "Drill weak topics with Khan Academy and Bluebook questions, 45–60 min a day. Learn the math formulas and grammar rules that keep appearing.", "Zaif mavzularni Khan Academy va Bluebook savollari bilan kuniga 45–60 daq. ishlang. Matematikada formulalar, o‘qishda grammatika qoidalarini o‘rganing.", "Отрабатывайте слабые темы по материалам Khan Academy и Bluebook, 45–60 мин в день. Выучите формулы по математике и правила грамматики.")),
 "ph3": (T("Tolıq sınaq testleri", "Full practice tests", "To‘liq sinov testlari", "Полные пробные тесты"),
         T("Hápte sayın bir tolıq test: shın test sıyaqlı, tınıq jerde hám waqıtqa qarap. Keyin qátelerdi 2 saat talqılań.", "One full test a week, like the real thing: quiet room, on the clock. Then spend time reviewing every mistake.", "Haftada bitta to‘liq test: haqiqiy testdek, tinch joyda va vaqt bilan. So‘ng xatolarni tahlil qiling.", "Раз в неделю полный тест, как на настоящем экзамене: тихо и по времени. Затем разберите каждую ошибку.")),
 "ph4": (T("Sońǵı hápte", "Final week", "Oxirgi hafta", "Последняя неделя"),
         T("Jańa nárse oqımań. Qátelerińizdi qaytalań, jaqsı uyqılań, imtixan kúnine jaǵdaydı tayarlań (tómendegi dizim).", "Do not learn new things. Review your mistake log, sleep well and prepare for exam day (checklist below).", "Yangi narsa o‘rganmang. Xatolar daftarini takrorlang, yaxshi uxlang va imtihon kuniga tayyorlaning (quyidagi ro‘yxat).", "Не учите новое. Повторите журнал ошибок, выспитесь и подготовьтесь к дню экзамена (чек-лист ниже).")),
 "h_free": T("Biypul hám rásmiy materiallar", "Free and official material", "Bepul va rasmiy materiallar", "Бесплатные и официальные материалы"),
 "free": (T("Bluebook", "Bluebook", "Bluebook", "Bluebook"), T("Testtiń ózi usı programmada tapsırıladı. Sol jerde rásmiy tolıq sınaq testleri bar.", "The real test runs in this app, and it contains official full-length practice tests.", "Haqiqiy test shu ilovada topshiriladi, unda rasmiy to‘liq sinov testlari bor.", "Реальный тест проходит в этом приложении; в нём есть официальные пробные тесты."), "https://bluebook.collegeboard.org"),
 "free2": (T("Rásmiy tayarlıq betleri", "Official practice pages", "Rasmiy tayyorgarlik sahifalari", "Официальные страницы подготовки"), T("College Board sınaq materialları hám Khan Academy menen biypul rásmiy kurs.", "College Board practice material and the free official course with Khan Academy.", "College Board sinov materiallari va Khan Academy bilan bepul rasmiy kurs.", "Материалы College Board и бесплатный официальный курс вместе с Khan Academy."), "https://satsuite.collegeboard.org/sat/practice-preparation"),
 "free3": (T("Test sanaları hám dizimnen ótiw", "Dates and registration", "Sanalar va ro‘yxatdan o‘tish", "Даты и регистрация"), T("Sońǵı múddetler hám test orayları tizimi usı jerde.", "Latest deadlines and the list of test centres are here.", "So‘nggi muddatlar va test markazlari ro‘yxati shu yerda.", "Актуальные дедлайны и список центров тестирования здесь."), "https://satsuite.collegeboard.org/sat/dates-deadlines"),
 "h_uz": T("Ózbekstanda tapsırıw", "Taking it in Uzbekistan", "O‘zbekistonda topshirish", "Сдача в Узбекистане"),
 "uz_p": T("Digital SAT Ózbekstanda tapsırıladı: Tashkent hám basqa qalalardaǵı orayda, sonday-aq Oliy ta’lim bahalaw agentligi (DTM) filiallarında da ótkerilgen. Nukusqa jaqın orayǵı dizimnen ótkende College Board sayttaǵı test orayları dizimin tekseriń. Sertifikat Ózbekstan universitetlerine kiriwde de imtiyaz beriwi múmkin — DTM sayttaǵı shártlerdi tekseriń. Másláhátshi menen sóylesiń.",
          "The digital SAT is given in Uzbekistan, at private centres in Tashkent, Samarkand and other cities, and the Agency (DTM) has also run it at its regional branches. When you register, check College Board’s list of test centres for the one nearest Nukus. A SAT certificate can also give a privilege when applying to Uzbek universities — check the conditions on the DTM site. Ask the counsellor if you are unsure.",
          "Digital SAT O‘zbekistonda topshiriladi: Toshkent, Samarqand va boshqa shaharlardagi xususiy markazlarda, shuningdek DTM filiallarida ham o‘tkazilgan. Ro‘yxatdan o‘tganda College Board saytidagi test markazlari ro‘yxatidan Nukusga eng yaqinini tekshiring. Sertifikat O‘zbekiston universitetlariga kirishda ham imtiyoz berishi mumkin — shartlarni DTM saytidan tekshiring. Shubha bo‘lsa, maslahatchiga murojaat qiling.",
          "Цифровой SAT проводится в Узбекистане: в частных центрах Ташкента, Самарканда и других городов, а также в региональных филиалах ДТМ. При регистрации посмотрите в списке центров College Board ближайший к Нукусу. Сертификат SAT может давать льготу и при поступлении в вузы Узбекистана — условия смотрите на сайте ДТМ. Если сомневаетесь, спросите консультанта."),
 "h_ck": T("Imtixan kúni dizimi", "Exam-day checklist", "Imtihon kuni ro‘yxati", "Чек-лист на день экзамена"),
 "ck": (T("College Board akkaunt ashıldı", "College Board account created", "College Board akkaunti ochildi", "Аккаунт College Board создан"),
        T("Dizimnen ótip, admission ticket saqlandı", "Registered and admission ticket saved", "Ro‘yxatdan o‘tildi, admission ticket saqlandi", "Зарегистрировался, билет (admission ticket) сохранён"),
        T("Bluebook ornatıldı hám sınaq testi tapsırıldı", "Bluebook installed and a practice test taken", "Bluebook o‘rnatildi va sinov testi topshirildi", "Bluebook установлен и пробный тест пройден"),
        T("Pasport (yamasa rásmiy ID) tayar", "Passport (or the accepted ID) ready", "Pasport (yoki qabul qilingan ID) tayyor", "Паспорт (или принимаемый документ) готов"),
        T("Noutbuk / planshet toliq zaryadlandı, zaryadlaǵısh alındı", "Laptop or tablet fully charged, charger packed", "Noutbuk / planshet to‘liq zaryadlangan, zaryadka olingan", "Ноутбук/планшет заряжен, зарядка взята"),
        T("Orayǵa jol hám waqıt anıq", "Route and travel time to the centre known", "Markazga yo‘l va vaqt aniq", "Маршрут и время в пути до центра известны"),
        T("Tamaq / suw tayar (tanaffus ushın)", "Snack and water for the break", "Tanaffus uchun yegulik va suv", "Перекус и вода на перерыв"),
        T("Aldınǵı kúni jaqsı uyıqladım", "Slept well the night before", "Oldingi kecha yaxshi uxladim", "Выспался накануне")),
 "ck_note": T("Bul dizim — ulıwma baǵdar. Anıq talaplar (qanday ID, qanday qurılma) dizimnen ótkennen keyin kelgen admission ticketta jazılǵan.", "This is a general guide. The exact rules (which ID, which device) are on the admission ticket you get after registering.", "Bu ro‘yxat — umumiy yo‘nalish. Aniq talablar (qanday ID, qanday qurilma) ro‘yxatdan o‘tgach kelgan admission ticketda yozilgan.", "Это общая памятка. Точные правила (какой документ, какое устройство) указаны в билете, который приходит после регистрации."),
 "dev": T("Qurılma joq bolsa, College Board-tan qarızǵa alıwǵa boladı, biraq test sanasınan keminde 30 kún aldın sorań.", "If you have no device, you can borrow one from College Board, but request it at least 30 days before the test.", "Qurilma bo‘lmasa, College Board’dan qarzga olish mumkin, lekin test sanasidan kamida 30 kun oldin so‘rang.", "Если нет устройства, его можно взять у College Board, но запросите не позже чем за 30 дней до теста."),
 "foot": T("Maǵlıwmatlar 2026-yıl noyabrde College Board hám universitetlerdiń rásmiy betlerinen alındı. Haqı hám sanalar ózgeriwi múmkin — dizimnen ótiwden aldın sat.org-dan tekseriń.",
           "Information was checked against College Board and university pages in November 2026. Fees and dates can change, so confirm on the official site before you register.",
           "Ma’lumotlar 2026-yil noyabrda College Board va universitetlar rasmiy sahifalaridan olingan. Narx va sanalar o‘zgarishi mumkin — ro‘yxatdan o‘tishdan oldin rasmiy saytda tekshiring.",
           "Сведения проверены по официальным страницам College Board и вузов в ноябре 2026 года. Цены и даты могут измениться — перед регистрацией проверьте на официальном сайте."),
}
MONTHS = [["yan.","fev.","mart","apr.","may","iyun","iyul","avg.","sent.","okt.","noy.","dek."],["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],["yan.","fev.","mart","apr.","may","iyun","iyul","avg.","sent.","okt.","noy.","dek."],["янв.","фев.","мар.","апр.","мая","июн.","июл.","авг.","сен.","окт.","нояб.","дек."]]
MODS = [("rw", 32, 27), ("rw", 32, 27), ("br", 10, 0), ("m", 35, 22), ("m", 35, 22)]
DATES = [("2026-12-05", "2026-11-20", "2026-11-24"), ("2027-03-06", "2027-02-19", "2027-02-23"), ("2027-05-01", "2027-04-16", "2027-04-20"), ("2027-06-05", "2027-05-21", "2027-05-25")]
ANT = ["2027-08-28", "2027-09-18", "2027-10-09", "2027-11-06", "2027-12-04"]
NEED = [
 ("us", "🇺🇸", T("AQSh", "USA", "AQSh", "США"), "ok",
  T("2026–27 ushın Harvard, Yale, Penn, Brown, Dartmouth, Cornell, Stanford, MIT, Caltech, Johns Hopkins, Georgetown, sonday-aq Florida hám Georgia kárxanalıq universitetleri SAT yamasa ACT soraydı. Basqalarınıń kópshiligi test-optional: ball jibermew múmkin, biraq jaqsı ball arzańızdı kúsheytedi.",
    "For 2026–27, Harvard, Yale, Penn, Brown, Dartmouth, Cornell, Stanford, MIT, Caltech, Johns Hopkins, Georgetown and the Florida and Georgia public systems ask for an SAT or ACT. Many other universities are test-optional: you may skip it, but a good score can still strengthen your application.",
    "2026–27 uchun Harvard, Yale, Penn, Brown, Dartmouth, Cornell, Stanford, MIT, Caltech, Johns Hopkins, Georgetown, shuningdek Florida va Georgia davlat universitetlari SAT yoki ACT so‘raydi. Boshqalarning ko‘pi test-optional: ball yubormaslik mumkin, lekin yaxshi ball arizangizni kuchaytiradi.",
    "На 2026–27 SAT или ACT требуют Harvard, Yale, Penn, Brown, Dartmouth, Cornell, Stanford, MIT, Caltech, Johns Hopkins, Georgetown, а также государственные вузы Флориды и Джорджии. Многие другие — test-optional: балл можно не присылать, но хороший результат всё равно усиливает заявку.")),
 ("uk", "🇬🇧", T("Ullı Britaniya", "UK", "Buyuk Britaniya", "Великобритания"), "chk",
  T("Kópshilik UK universitetleri SAT soramaydı; olar mektep dárejesi hám IELTS ke qaraydı. Ayırım kurslarda ózgeshe talap bolıwı múmkin — kurs betin tekseriń.", "Most UK universities do not ask for the SAT; they look at school qualifications and English tests such as IELTS. A few courses may differ, so check the course page.", "Aksariyat Buyuk Britaniya universitetlari SAT so‘ramaydi; ular maktab natijalari va IELTS kabi ingliz tili testiga qaraydi. Ayrim kurslarda boshqacha talab bo‘lishi mumkin — kurs sahifasini tekshiring.", "Большинство британских вузов SAT не требуют: они смотрят на школьные результаты и тест по английскому (IELTS). У отдельных курсов могут быть иные правила — проверьте страницу курса.")),
 ("ca", "🇨🇦", T("Kanada", "Canada", "Kanada", "Канада"), "chk",
  T("Kóbinese talap etilmeydi: baha hám inglis tili testi áhmiyetli. Ayırım universitetler tańlawlı túrde qabıl etiwi múmkin.", "Usually not required: grades and an English test matter more. Some universities may accept it as an extra.", "Odatda talab qilinmaydi: baholar va ingliz tili testi muhimroq. Ba’zi universitetlar qo‘shimcha sifatida qabul qilishi mumkin.", "Обычно не требуется: важнее оценки и тест по английскому. Некоторые вузы могут принять его как дополнение.")),
 ("de", "🇩🇪", T("Germaniya", "Germany", "Germaniya", "Германия"), "chk",
  T("Qabıllaw hújjetlerge (attestat, til) tiykarlanadı; SAT kóbinese soralmaydı. Hár bir universitet hám baǵdardı DAAD hám uni-assist arqalı tekseriń.", "Admission is based on your school documents and language proof; the SAT is usually not asked. Check each university and programme through DAAD and uni-assist.", "Qabul hujjatlar (attestat, til)ga asoslanadi; SAT odatda so‘ralmaydi. Har bir universitet va yo‘nalishni DAAD va uni-assist orqali tekshiring.", "Приём основан на школьных документах и подтверждении языка; SAT обычно не требуется. Проверяйте вуз и программу через DAAD и uni-assist.")),
 ("uz", "🇺🇿", T("Ózbekstan", "Uzbekistan", "O‘zbekiston", "Узбекистан"), "chk",
  T("SAT sertifikatı Ózbekstan universitetlerine kiriwde imtiyaz beriwi múmkin. Shártlerin DTM rásmiy betinen tekseriń.", "A SAT certificate may give a privilege for entry to Uzbek universities. Check the conditions on the DTM official page.", "SAT sertifikati O‘zbekiston universitetlariga kirishda imtiyoz berishi mumkin. Shartlarini DTM rasmiy sahifasidan tekshiring.", "Сертификат SAT может давать льготу при поступлении в вузы Узбекистана. Условия смотрите на официальной странице ДТМ.")),
]
NB = {"ok": T("Rásmiy betlerden tekserildi", "Checked against official sources", "Rasmiy manbalar bilan tekshirilgan", "Проверено по официальным источникам"), "chk": T("Ulıwma qaǵıyda — universitet saytında tastıyıqlań", "General rule — confirm on the university site", "Umumiy qoida — universitet saytida tasdiqlang", "Общее правило — подтвердите на сайте вуза")}
RANGE = [("Harvard", 1510, 1580), ("Yale", 1500, 1570), ("Penn", 1500, 1570), ("Dartmouth", 1490, 1560), ("Brown", 1490, 1560), ("Cornell", 1470, 1550)]
def body(i, tabs_html):
    data = {"ui": {k: (v[i] if isinstance(v, tuple) and len(v) == 4 and all(isinstance(x, str) for x in v) else None) for k, v in UI.items()}}
    data["tiles"] = [[t[i][0], t[i][1]] for t in UI["tiles"]]
    data["ph"] = [[p[0][i], p[1][i]] for p in (UI["ph"], UI["ph2"], UI["ph3"], UI["ph4"])]
    data["free"] = [[f[0][i], f[1][i], f[2]] for f in (UI["free"], UI["free2"], UI["free3"])]
    data["ck"] = [c[i] for c in UI["ck"]]
    data["mods"] = [list(m) for m in MODS]
    data["months"] = MONTHS[i]; data["dates"] = DATES; data["ant"] = ANT; data["range"] = RANGE
    data["need"] = [dict(k=k, f=f, n=n[i], s=s, nb=NB[s][i], t=t[i]) for k, f, n, s, t in NEED]
    js = SAT_JS.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    return (f'{tabs_html}<p class="lead2">{UI["intro"][i]}</p><section id="sat"></section><p class="note">{UI["foot"][i]}</p><script>{js}</script>')
SAT_JS = r"""(function(){var D=__DATA__,U=D.ui,$=function(i){return document.getElementById(i)},root=$('sat');
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;')}
var st={sel:1,need:'us',score:'',ck:{}};try{var o=JSON.parse(localStorage.getItem('satS')||'{}');for(var k in o)st[k]=o[k]}catch(e){}
function save(){try{localStorage.setItem('satS',JSON.stringify({sel:st.sel,need:st.need,score:st.score,ck:st.ck}))}catch(e){}}
var months=D.months;
function dt(s){var p=s.split('-');return new Date(+p[0],+p[1]-1,+p[2],23,59)}
function fd(s){var d=dt(s);return months[d.getMonth()]+' '+d.getDate()+', '+d.getFullYear()}
function days(s){return Math.ceil((dt(s)-new Date())/864e5)}
function fmt(){var t='';D.mods.forEach(function(m,ix){var c=m[0],w=m[1];var lab=c=='br'?U.m_br:(c=='rw'?U.m_rw:U.m_m)+' '+((ix<2?ix:ix-3)+1);
t+='<div class="satm '+c+'" style="flex:'+w+'"><b>'+esc(lab)+'</b><span>'+w+' '+U.min+(m[2]?' · '+m[2]+' '+U.q:'')+'</span></div>'});return t}
function dates(){var h='<div class="satdt">';D.dates.forEach(function(d,ix){var dl=days(d[1]),ll=days(d[2]),cls,lab;
if(dl>=0){cls='op';lab=U.open+' · '+U.left.replace('{n}',dl)}else if(ll>=0){cls='lt';lab=U.lateonly}else{cls='cl';lab=U.closed}
h+='<button type="button" class="satd '+cls+(st.sel==ix?' on':'')+'" data-d="'+ix+'"><b>'+fd(d[0])+'</b><small>'+U.reg+': '+fd(d[1])+'</small><em>'+lab+'</em></button>'});
return h+'</div><details class="satant"><summary>'+esc(U.ant)+'</summary><p>'+D.ant.map(fd).join(' · ')+'</p></details>'}
function need(){var h='<div class="satchips">'+D.need.map(function(n){return '<button type="button" class="satc'+(st.need==n.k?' on':'')+'" data-n="'+n.k+'">'+n.f+' '+esc(n.n)+'</button>'}).join('')+'</div>';
var n=D.need.filter(function(x){return x.k==st.need})[0];
return h+'<div class="satneed card"><span class="satbadge '+n.s+'">'+esc(n.nb)+'</span><p>'+esc(n.t)+'</p></div>'}
function range(){var lo=1300,hi=1600,sc=parseInt(st.score,10),h='<label class="satin">'+U.myscore+' <input type="number" id="satsc" min="400" max="1600" step="10" inputmode="numeric" value="'+(sc||'')+'"></label><div class="satrg">';
D.range.forEach(function(r){var a=(r[1]-lo)/(hi-lo)*100,b=(r[2]-lo)/(hi-lo)*100,msg='';
if(sc){msg=sc<r[1]?U.below.replace('{n}',r[1]-sc):(sc>r[2]?U.above:U.inside)}
h+='<div class="satrow"><span class="satun">'+r[0]+'</span><div class="satbar"><i style="left:'+a+'%;width:'+(b-a)+'%"></i>'+(sc&&sc>=lo&&sc<=hi?'<u style="left:'+((sc-lo)/(hi-lo)*100)+'%"></u>':'')+'</div><span class="satv">'+r[1]+'–'+r[2]+'</span>'+(msg?'<small>'+msg+'</small>':'')+'</div>'});
return h+'</div><p class="note">'+esc(U.range_note)+'</p>'}
function plan(){var d=D.dates[st.sel],w=Math.floor(days(d[0])/7),h='';
if(w<1)return '<p class="note">'+esc(U.closed)+'</p>';
var n=Math.min(w,16),sh=[.15,.5,.25,.1],ws=sh.map(function(x){return Math.max(1,Math.round(x*n))});
if(n<4){ws=[1,Math.max(1,n-3),1,1]}
var cur=1;h='<p class="satw"><b>'+U.weeks.replace('{n}',w)+'</b>'+(w<4?' · '+esc(U.tight):'')+'</p><ol class="satplan">';
D.ph.forEach(function(p,ix){var a=cur,b=cur+ws[ix]-1;cur=b+1;h+='<li><span class="satpw">'+(a==b?U.wk1.replace('{a}',a):U.wk.replace('{a}',a).replace('{b}',b))+'</span><div><b>'+esc(p[0])+'</b><p>'+esc(p[1])+'</p></div></li>'});
return h+'</ol>'}
function ck(){var n=D.ck.length,d=D.ck.filter(function(_,ix){return st.ck[ix]}).length;
return '<div class="satprog"><i style="width:'+(d/n*100)+'%"></i></div><ul class="satck">'+D.ck.map(function(t,ix){return '<li class="'+(st.ck[ix]?'on':'')+'"><label><input type="checkbox" data-c="'+ix+'"'+(st.ck[ix]?' checked':'')+'><span class="ckbx"></span><span>'+esc(t)+'</span></label></li>'}).join('')+'</ul><p class="note">'+esc(U.ck_note)+'</p><p class="note">'+esc(U.dev)+'</p>'}
function render(){root.innerHTML='<div class="sattiles">'+D.tiles.map(function(t,ix){return '<div class="sattile t'+ix+'"><b>'+esc(t[0])+'</b><span>'+esc(t[1])+'</span></div>'}).join('')+'</div>'
+'<h2>'+U.h_fmt+'</h2><p>'+U.fmt_p+'</p><div class="satfmt">'+fmt()+'</div><p class="note">'+U.score_p+'</p>'
+'<h2>'+U.h_dates+'</h2><p>'+U.dates_p+'</p><div id="satdates">'+dates()+'</div><p class="note">'+U.which+'</p>'
+'<h2>'+U.h_need+'</h2><p>'+U.need_p+'</p><div id="satneed">'+need()+'</div>'
+'<h2>'+U.h_range+'</h2><p>'+U.range_p+'</p><div id="satrange">'+range()+'</div>'
+'<h2>'+U.h_plan+'</h2><p>'+U.plan_p+'</p><div id="satplan">'+plan()+'</div>'
+'<h2>'+U.h_free+'</h2><div class="grid2">'+D.free.map(function(f){return '<a class="card satfree" href="'+f[2]+'" rel="noopener"><h3>'+esc(f[0])+'</h3><p>'+esc(f[1])+'</p></a>'}).join('')+'</div>'
+'<h2>'+U.h_uz+'</h2><div class="card"><p>'+U.uz_p+'</p></div>'
+'<h2>'+U.h_ck+'</h2><div id="satck">'+ck()+'</div>'}
root.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
if(b.dataset.d!=null){st.sel=+b.dataset.d;save();$('satdates').innerHTML=dates();$('satplan').innerHTML=plan()}
else if(b.dataset.n){st.need=b.dataset.n;save();$('satneed').innerHTML=need()}});
root.addEventListener('input',function(e){if(e.target.id=='satsc'){st.score=e.target.value;save();var p=e.target.selectionStart;$('satrange').innerHTML=range();var n=$('satsc');n.focus();try{n.setSelectionRange(p,p)}catch(x){}}});
root.addEventListener('change',function(e){var c=e.target;if(c.dataset&&c.dataset.c!=null){if(c.checked)st.ck[c.dataset.c]=1;else delete st.ck[c.dataset.c];save();$('satck').innerHTML=ck()}});
render()})();"""
