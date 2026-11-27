# School canteen page: official list of foods not allowed in general education schools (4 languages).
import json
# Source PDF: files/taqiqlangan-mahsulotlar.pdf (Uzbek original). Item order inside categories follows the document.
NAME = ("Mektep asxanası", "School canteen", "Maktab oshxonasi", "Школьная столовая")
DESC = ("Mektepte ruqsat etilmeytuǵın azıq-awqat ónimleri hám taǵamlar dizimi: ishimlikler, chipsı, fast-fud, saqız hám basqalar.",
        "Foods and dishes not allowed at school: fizzy and energy drinks, chips, fast food, chewing gum, home-made food and more.",
        "Maktabda ruxsat etilmaydigan oziq-ovqat mahsulotlari va taomlar ro‘yxati: gazli va energetik ichimliklar, chips, fast-fud, saqich va boshqalar.",
        "Продукты и блюда, запрещённые в школе: газировка и энергетики, чипсы, фастфуд, жвачка, домашняя еда и другое.")
SUBS = ["canteen/", "canteen/not-allowed/"]
NAMES = {"canteen/": NAME,
         "canteen/not-allowed/": ("Ruqsat etilmegen ónimler", "Foods not allowed", "Ruxsat etilmagan mahsulotlar", "Запрещённые продукты")}
DESCS = {"canteen/": ("Kegeyli rayonı qánigelestirilgen mektebiniń asxanası: oqıwshılardı awqatlandırıw hám densawlıq qaǵıydaları.",
                      "The canteen of Kegeyli District Specialized School: student meals and healthy-eating rules.",
                      "Kegeli tumani ixtisoslashtirilgan maktabi oshxonasi: o‘quvchilarni ovqatlantirish va sog‘lom ovqatlanish qoidalari.",
                      "Столовая Кегейлийской районной специализированной школы: питание учеников и правила здорового питания."),
         "canteen/not-allowed/": DESC}
PDF = "files/taqiqlangan-mahsulotlar.pdf"
THUMB = "files/taqiqlangan-mahsulotlar.jpg"

def _svg(p, s=24, w=2):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'

I_DRINK = '<path d="M6 8h12l-1.500 13h-9z"/><path d="M12 8l2-6h3"/><path d="M6.500 12.500h11"/>'
I_CHIPS = '<path d="M6 3h12l-1 3 1 3-1 3 1 3-1 3 1 3H6l1-3-1-3 1-3-1-3 1-3z"/><circle cx="12" cy="11" r="2.500"/>'
I_BURGER = '<path d="M4 11a8 6 0 0 1 16 0z"/><path d="M3 14h18"/><path d="M4 17h16l-1 3H5z"/>'
I_MEAT = '<path d="M14.500 3.500a6 6 0 0 1 6 6c0 3.500-3.500 5.500-6.500 5.500L10 19a2 2 0 1 1-3.200 1.200A2 2 0 1 1 5 17.200 2 2 0 0 1 6 14l4-4c0-3.500 1.500-6.500 4.500-6.500z"/>'
I_MILK = '<path d="M8 2h8v4l2 3v13H6V9l2-3z"/><path d="M6 9h12M10 14h4"/>'
I_BOWL = '<path d="M3 11h18a9 9 0 0 1-18 0z"/><path d="M8 7c0-2 2-2 2-4M13 7c0-2 2-2 2-4"/>'
I_WARN = '<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18h.01"/>'
I_CAN = '<rect x="7" y="3" width="10" height="18" rx="2"/><path d="M7 7h10M7 17h10"/><path d="M10 11.500c1-.8 3-.8 4 0"/>'
I_ENERGY = '<rect x="7" y="3" width="10" height="18" rx="2"/><path d="M13 6.500l-3 5.500h4l-3 5.500"/>'
I_GUM = '<rect x="3" y="8" width="18" height="8" rx="2"/><path d="M7.500 8v8M12 8v8M16.500 8v8"/>'
I_HOME = '<path d="M3 11l9-7 9 7v10H3z"/><path d="M9 21v-6h6v6"/>'
I_CAKE = '<path d="M4 21h16v-8H4z"/><path d="M4 16c2 1.500 4 1.500 6 0s4-1.500 6 0 3 1 4 0"/><path d="M12 9v4M12 5.500c-.8.700-.8 1.700 0 2.200.8-.500.8-1.500 0-2.200z"/>'
I_X = '<path d="M6 6l12 12M18 6L6 18"/>'
I_HEART = '<path d="M12 20s-7-4.400-9-9a4.500 4.500 0 0 1 9-3 4.500 4.500 0 0 1 9 3c-2 4.600-9 9-9 9z"/>'
I_SHIELD = '<path d="M12 3l8 3v6c0 5-3.500 8-8 9-4.500-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>'
I_BRAIN = '<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 6 1V4.500A3 3 0 0 0 9 4zM15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-6 1"/>'
I_DL = '<path d="M12 3v12M7 10l5 5 5-5M5 21h14"/>'
I_SEARCH = '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>'
I_OK = '<path d="M5 12l5 5L20 7"/>'
I_WATER = '<path d="M12 3s6 6.500 6 11a6 6 0 0 1-12 0c0-4.500 6-11 6-11z"/>'
I_APPLE = '<path d="M12 7c-2-1.500-6-1-7 3-1 4.500 2 10 5 10 1 0 1.500-.500 2-.500s1 .500 2 .500c3 0 6-5.500 5-10-1-4-5-4.500-7-3z"/><path d="M12 7c0-2 1-3.500 3-4"/>'
I_TEA = '<path d="M4 9h13v5a6 6 0 0 1-6 6h-1a6 6 0 0 1-6-6z"/><path d="M17 11h2a2 2 0 0 1 0 4h-2M8 3c0 2 2 2 2 4M12 3c0 2 2 2 2 4"/>'
I_PLATE = '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/>'

CATS = [
 ("drinks", "#2a7fd1", I_DRINK, ("Ishimlikler", "Drinks", "Ichimliklar", "Напитки"), [
   ("Reńli hám reńsiz gazlı ishimlikler", "Coloured and clear fizzy drinks", "Rangli va rangsiz gazlangan ichimliklar", "Цветные и бесцветные газированные напитки"),
   ("Energetikalıq hám tetiklendiriwshi ishimlikler, tábiyiy kofe, alkogol", "Energy and stimulant drinks, natural coffee, alcohol", "Energetik va tetiklantiruvchi ichimliklar, tabiiy kofe, alkogol", "Энергетические и тонизирующие напитки, натуральный кофе, алкоголь"),
   ("Kvas", "Kvass", "Kvas", "Квас"),
   ("Termik islenbegen miywe hám rezavor ishimlikleri, morslar", "Fruit and berry cold drinks and mors without heat treatment", "Termik ishlov berilmagan meva va rezavor yaxna ichimliklari, morslar", "Фруктово-ягодные напитки и морсы без термообработки"),
   ("Qımız hám quramında 0,5%-dan artıq spirt bar ashıtılǵan sút ónimleri", "Kumis and fermented milk drinks with over 0.5% alcohol", "Qimiz va tarkibida 0,5%dan ortiq etanol bo‘lgan achitilgan sutli mahsulotlar", "Кумыс и кисломолочные продукты с этанолом более 0,5%"),
 ]),
 ("snacks", "#d97706", I_CHIPS, ("Jeńil awqatlar hám tatlılar", "Snacks and sweets", "Gazaklar va shirinliklar", "Снеки и сладости"), [
   ("Chipslar", "Chips (crisps)", "Chipslar", "Чипсы"),
   ("Jasalma konservantlı ónimler (kirieshki, xrustyashki)", "Snacks with artificial preservatives (kiriyeshki, crackers)", "Sun’iy konservantli mahsulotlar (kiriyeshki, xrustyashki)", "Продукты с искусственными консервантами (кириешки, хрустяшки)"),
   ("Jasalma dám, iyis, boyaw hám aromatizator qosılǵan konditer ónimleri", "Sweets with artificial flavours, colours and aromas", "Sun’iy ta’m, hid, bo‘yoq va aromatizatorli qandolat mahsulotlari", "Кондитерские изделия с искусственными вкусами, красителями и ароматизаторами"),
   ("Kremli tort hám pirojnoeler", "Cream cakes and pastries", "Kremli tort va pishiriqlar", "Кремовые торты и пирожные"),
   ("Saqız", "Chewing gum", "Saqich", "Жевательная резинка"),
   ("Súyekli miywelerdiń mag‘zi", "Kernels of stone fruits", "Danakli mevalarning mag‘zi", "Ядра косточковых плодов"),
 ]),
 ("fast", "#d6452f", I_BURGER, ("Fast-fud hám souslar", "Fast food and sauces", "Fast-fud va souslar", "Фастфуд и соусы"), [
   ("Gósh, mayonez, ketchup qosılǵan nanlar: gamburger, chizburger, xot-dog", "Burgers, cheeseburgers and hot dogs with meat, mayonnaise, ketchup", "Go‘sht, mayonez, ketchup qo‘shilgan non mahsulotlari: gamburger, chizburger, xot-dog", "Гамбургеры, чизбургеры и хот-доги с мясом, майонезом, кетчупом"),
   ("Ashshı souslar, ketchup, mayonez, konservalar, marinadlanǵan ovosh hám miyweler", "Spicy sauces, ketchup, mayonnaise, canned and pickled vegetables and fruit", "O‘tkir souslar, ketchup, mayonez, konservalar, marinadlangan sabzavot va mevalar", "Острые соусы, кетчуп, майонез, консервы, маринованные овощи и фрукты"),
   ("Sirke, gorchica, xren, ashshı burısh hám basqa ashshı ziravorlar", "Vinegar, mustard, horseradish, hot pepper and other spicy seasonings", "Sirka, xantal, xren, o‘tkir qalampir va boshqa o‘tkir ziravorlar", "Уксус, горчица, хрен, острый перец и другие острые приправы"),
 ]),
 ("meat", "#b23a48", I_MEAT, ("Gósh hám kolbasalar", "Meat and sausages", "Go‘sht va kolbasalar", "Мясо и колбасы"), [
   ("Veterinariya qadaǵalawınan ótpegen gósh, balıq, quslar", "Meat, fish and poultry without veterinary inspection", "Veterinariya nazoratidan o‘tmagan go‘sht, baliq, parrandalar", "Мясо, рыба и птица без ветеринарного контроля"),
   ("Bawır, til hám júrekten basqa barlıq ishek-qarın", "All offal except liver, tongue and heart", "Jigar, til va yurakdan tashqari barcha kalla-pochalar", "Все субпродукты, кроме печени, языка и сердца"),
   ("Ishek-qarnınan tazalanbaǵan quslar", "Poultry not cleaned of entrails", "Ichak-chavoqdan tozalanmagan parranda", "Непотрошёная птица"),
   ("Xolodec, kalla góshi ruletleri, ókpe-bawır hám qan kolbasaları", "Aspic, head-meat rolls, liver and blood sausages", "Xolodes, kalla go‘shti ruletlari, o‘pka-jigarli va qondan qilingan kolbasalar", "Холодец, рулеты из мяса голов, ливерные и кровяные колбасы"),
   ("Xom ısqlanǵan gósh ónimleri hám kolbasalar, sonıń ishinde qaynatılǵan kolbasa", "Raw-smoked meats and sausages, including boiled sausage", "Xom dudlangan go‘shtli mahsulotlar va kolbasalar, shu jumladan qaynatilgan kolbasa", "Сырокопчёные мясные изделия и колбасы, включая варёную колбасу"),
   ("Issılıq penen islenbegen gósh, qus hám balıq taǵamları", "Meat, poultry and fish dishes without heat treatment", "Issiqlik bilan ishlov berilmagan go‘sht, parranda, baliq taomlari", "Блюда из мяса, птицы и рыбы без термообработки"),
   ("Gósh hám balıq salınǵan taǵamlar, seledka hám kartoshkadan forshmak", "Dishes topped with meat or fish, herring-and-potato forshmak", "Ustiga go‘sht yoki baliq solinadigan taomlar, seld va kartoshkali ovqat", "Блюда с мясной или рыбной заливкой, форшмак из сельди с картофелем"),
   ("Pashtet, gósh hám tvorog quymaqları", "Pâté, meat and cottage-cheese pancakes", "Pashtet, go‘sht va tvorogli quymoqlar", "Паштет, мясные и творожные блинчики"),
 ]),
 ("dairy", "#0b7a8f", I_MILK, ("Sút ónimleri hám máyek", "Dairy and eggs", "Sut mahsulotlari va tuxum", "Молочное и яйца"), [
   ("Pasterizaciyalanbaǵan sút hám sút ónimleri", "Unpasteurised milk and dairy products", "Pasterizatsiya qilinmagan sut va sut mahsulotlari", "Непастеризованное молоко и молочные продукты"),
   ("Pasterizaciyalanbaǵan tvorog hám qaymaq (flyagadaǵı)", "Unpasteurised cottage cheese and sour cream (from churns)", "Pasterizatsiya qilinmagan (flyagadagi) tvorog va qaymoq", "Непастеризованный (флажный) творог и сметана"),
   ("Úyde tayarlanǵan qatıq", "Home-made yoghurt (qatiq)", "Qo‘lbola qatiq", "Домашний катык"),
   ("Pataslanǵan, sınǵan yamasa qáwipli fermalardan alınǵan máyekler", "Dirty or cracked eggs, eggs from salmonella-risk farms", "Iflos, singan yoki salmonellyozga nohush xo‘jaliklardan olingan tuxumlar", "Грязные, битые яйца и яйца из неблагополучных по сальмонеллёзу хозяйств"),
   ("Mayda qorılǵan máyek", "Fried eggs", "Yog‘da qovurilgan tuxum", "Яичница, жаренная на масле"),
 ]),
 ("dishes", "#7c3aed", I_BOWL, ("Taǵamlar hám ónimler", "Dishes and ingredients", "Taomlar va masalliqlar", "Блюда и ингредиенты"), [
   ("Okroshka hám suwıq sorpalar", "Okroshka and cold soups", "Okroshka va sovuq sho‘rvalar", "Окрошка и холодные супы"),
   ("Qıyma qosılǵan makaron, máyekli makaron (po-flotski)", "Navy-style pasta with mince or chopped egg", "Qiymali makaron, to‘g‘ralgan tuxumli makaron (po flotski)", "Макароны по-флотски, макароны с рубленым яйцом"),
   ("Tez tayarlanatuǵın qurǵaq koncentrat taǵamlar", "Instant meals from dry food concentrates", "Tez tayyorlanadigan quruq konsentrat asosidagi taomlar", "Первые и вторые блюда из сухих концентратов быстрого приготовления"),
   ("Sańırawqulaqlar hám olardan tayarlanǵan ónimler", "Mushrooms and mushroom products", "Qo‘ziqorinlar va ulardan tayyorlangan mahsulotlar", "Грибы и продукты из них"),
   ("Pazandalıq mayları, shoshqa mayı, margarin hám gidrogenlengen maylar", "Cooking fats, lard, margarine and hydrogenated fats", "Pazandalik moylari, cho‘chqa yog‘i, margarin va gidrogen yog‘lar", "Кулинарные жиры, свиное сало, маргарин и гидрогенизированные жиры"),
 ]),
 ("unsafe", "#5b6472", I_WARN, ("Buzılǵan hám úy awqatları", "Spoiled and home-made food", "Buzilgan va uy ovqatlari", "Испорченная и домашняя еда"), [
   ("Úy sharayatında tayarlanǵan barlıq azıq-awqat", "All home-made (non-factory) food", "Uy sharoitida tayyorlangan barcha oziq-ovqat mahsulotlari", "Вся еда домашнего (непромышленного) приготовления"),
   ("Jaramlılıq múddeti ótken hám sapası tómen ónimler", "Expired and poor-quality food", "Yaroqlilik muddati tugagan va sifatsiz mahsulotlar", "Просроченные и некачественные продукты"),
   ("Bir kún aldın tayarlanıp, qalıp qoyǵan awqatlar", "Leftovers cooked the day before", "Bir kun oldin tayyorlangan va qolib ketgan ovqatlar", "Блюда, приготовленные накануне и оставшиеся"),
   ("Eskirgen, buzılǵan ovoshlar", "Stale or spoiled vegetables", "Eskirgan, sifati buzilgan sabzavotlar", "Несвежие, испорченные овощи"),
   ("Bankası buzılǵan, isingen, zanglaǵan, yarlıǵı joq konservalar", "Damaged, bulging, rusty or unlabelled canned goods", "Germetikligi buzilgan, bombajli, zanglagan, yorlig‘siz konservalar", "Консервы с нарушенной герметичностью, бомбажем, ржавчиной, без маркировки"),
   ("Zıyankesler menen zaqımlanǵan yarma, un, quwraq miyweler", "Grains, flour and dried fruit infested by pests", "Zararkunandalar bilan zararlangan yorma, un, quritilgan mevalar", "Крупы, мука и сухофрукты, поражённые вредителями"),
 ]),
]
TOP = [  # most common things children bring from home
 (I_CHIPS, "#d97706", ("Chipslar", "Chips", "Chipslar", "Чипсы")),
 (I_CAN, "#2a7fd1", ("Gazlı ishimlikler", "Fizzy drinks", "Gazli ichimliklar", "Газировка")),
 (I_ENERGY, "#d6452f", ("Energetikler", "Energy drinks", "Energetiklar", "Энергетики")),
 (I_GUM, "#7c3aed", ("Saqız", "Chewing gum", "Saqich", "Жвачка")),
 (I_BURGER, "#b23a48", ("Xot-dog, burger", "Hot dogs, burgers", "Xot-dog, burger", "Хот-доги, бургеры")),
 (I_HOME, "#0b7a8f", ("Úy awqatları", "Home-made food", "Uy ovqatlari", "Домашняя еда")),
]
WHY = [
 (I_HEART, "#d6452f", ("Densawlıq", "Health", "Sog‘liq", "Здоровье"),
  ("Jasalma qospalar, artıq qant hám may balalar organizmine zıyan.", "Artificial additives, excess sugar and fat harm a growing body.", "Sun’iy qo‘shimchalar, ortiqcha shakar va yog‘ o‘sayotgan organizmga zarar.", "Искусственные добавки, лишний сахар и жир вредят растущему организму.")),
 (I_SHIELD, "#0b7a8f", ("Azıq-awqat qáwipsizligi", "Food safety", "Oziq-ovqat xavfsizligi", "Пищевая безопасность"),
  ("Tekserilmegen hám buzılǵan ónimler zaharlanıwǵa alıp keliwi múmkin.", "Unchecked or spoiled food can cause food poisoning.", "Tekshirilmagan va buzilgan mahsulotlar zaharlanishga olib kelishi mumkin.", "Непроверенные и испорченные продукты могут вызвать отравление.")),
 (I_BRAIN, "#7c3aed", ("Itibar hám oqıw", "Focus in class", "Diqqat va o‘qish", "Внимание на уроках"),
  ("Kofein hám energetikler uyqını hám itibardı buzadı.", "Caffeine and energy drinks disturb sleep and concentration.", "Kofein va energetiklar uyqu va diqqatni buzadi.", "Кофеин и энергетики нарушают сон и концентрацию.")),
]
BETTER = [
 (I_WATER, "#2a7fd1", ("Taza suw", "Clean water", "Toza suv", "Чистая вода")),
 (I_APPLE, "#2f8f5b", ("Jańa miyweler", "Fresh fruit", "Yangi mevalar", "Свежие фрукты")),
 (I_TEA, "#b45309", ("Shay", "Tea", "Choy", "Чай")),
 (I_PLATE, "#0b7a8f", ("Asxanadaǵı ıssı awqat", "A hot meal in the canteen", "Oshxonadagi issiq ovqat", "Горячее блюдо в столовой")),
]
X = {
 "tag": ("Densawlıq ushın", "For healthy students", "Sog‘lom o‘quvchilar uchun", "Ради здоровья учеников"),
 "hero_h": ("Mektepte ruqsat etilmeytuǵın azıq-awqatlar", "Foods not allowed at school", "Maktabda ruxsat etilmaydigan oziq-ovqatlar", "Продукты, запрещённые в школе"),
 "hero_p": ("Ulıwma bilim beriw mekemelerinde ruqsat etilmeytuǵın ónimler hám taǵamlardıń rásmiy dizimi. Mektepke usı ónimlerdi alıp kelmeń.",
            "The official list of foods and dishes not allowed in general education schools. Please don’t bring these to school.",
            "Umumta’lim muassasalarida ruxsat etilmaydigan oziq-ovqat mahsulotlari va taomlarining rasmiy ro‘yxati. Iltimos, ularni maktabga olib kelmang.",
            "Официальный список продуктов и блюд, не допускаемых в общеобразовательных учреждениях. Пожалуйста, не приносите их в школу."),
 "items": ("ónim hám taǵam", "foods and dishes", "ta mahsulot va taom", "продуктов и блюд"),
 "groups": ("toparǵa bólingen", "groups", "ta guruhga bo‘lingan", "групп"),
 "pdf": ("Rásmiy hújjet (PDF)", "Official document (PDF)", "Rasmiy hujjat (PDF)", "Официальный документ (PDF)"),
 "top_h": ("Úyde qaldırıń", "Leave these at home", "Uyda qoldiring", "Оставьте дома"),
 "top_p": ("Balalar mektepke kóbinese alıp keletuǵın ónimler — olar ruqsat etilmeydi.", "What children most often bring from home — none of it is allowed.", "Bolalar maktabga ko‘pincha olib keladigan mahsulotlar — ular ruxsat etilmaydi.", "То, что дети чаще всего приносят из дома, — всё это запрещено."),
 "list_h": ("Tolıq dizim", "The full list", "To‘liq ro‘yxat", "Полный список"),
 "search": ("Ónimdi izlew: mısalı, kvas", "Search a product, e.g. kvass", "Mahsulotni qidirish: masalan, kvas", "Поиск продукта, например квас"),
 "none": ("Hesh nárse tabılmadı. Bul ónim dizimde joq.", "Nothing found — this product isn’t on the list.", "Hech narsa topilmadi — bu mahsulot ro‘yxatda yo‘q.", "Ничего не найдено — этого продукта нет в списке."),
 "found": ("tabıldı", "found", "ta topildi", "найдено"),
 "all": ("Barlıǵı", "All", "Barchasi", "Все"),
 "why_h": ("Nege bul áhmiyetli?", "Why it matters", "Nega bu muhim?", "Почему это важно"),
 "better_h": ("Onıń ornına", "Better choices", "Buning o‘rniga", "Лучше выбрать"),
 "better_p": ("Mektep asxanası kún sayın ıssı awqat tayarlaydı.", "The school canteen serves a hot meal every school day.", "Maktab oshxonasi har kuni issiq ovqat tayyorlaydi.", "Школьная столовая каждый день готовит горячее."),
 "doc_h": ("Rásmiy hújjet", "Official document", "Rasmiy hujjat", "Официальный документ"),
 "doc_p": ("Umumta’lim muassasalarida ruxsat etilmaydigan oziq-ovqat mahsulotlari va taomlari ro‘yxati (ózbek tilinde, 2 bet).",
           "“List of foods and dishes not allowed in general education institutions” (in Uzbek, 2 pages).",
           "“Umumta’lim muassasalarida ruxsat etilmaydigan oziq-ovqat mahsulotlari va taomlari ro‘yxati” (2 bet).",
           "«Список продуктов и блюд, не допускаемых в общеобразовательных учреждениях» (на узбекском, 2 стр.)."),
 "open": ("Ashıw", "Open", "Ochish", "Открыть"),
 "dl": ("Júklep alıw", "Download", "Yuklab olish", "Скачать"),
 "parents": ("Ata-analarǵa: balańızǵa suw hám miywe beriń, qalǵanın mektep asxanası tayarlaydı.", "For parents: give your child water and fruit — the canteen takes care of the rest.",
             "Ota-onalarga: farzandingizga suv va meva bering — qolganini maktab oshxonasi tayyorlaydi.", "Родителям: дайте ребёнку воду и фрукты — остальным займётся школьная столовая."),
}

H = {
 "intro_h": ("Mektebimizdiń asxanası", "Our school canteen", "Maktabimiz oshxonasi", "Наша школьная столовая"),
 "intro_p": ("Mektepte oqıwshılar ushın óz asxanası bar. Mektep internat emes — oqıwshılar kúndizgi formada oqıydı hám sabaq kúni asxanada awqatlanadı.",
             "The school has its own canteen for students. It is a day school, not a boarding school, so students eat in the canteen during the school day.",
             "Maktabda o‘quvchilar uchun o‘z oshxonasi ishlaydi. Maktab internat emas — o‘quvchilar kunduzgi shaklda o‘qiydi va dars kuni oshxonada ovqatlanadi.",
             "В школе есть собственная столовая. Школа не интернат — ученики учатся в дневной форме и питаются в столовой в учебный день."),
 "f1": ("Óz asxanası", "Own canteen", "O‘z oshxonasi", "Своя столовая"),
 "f2": ("Kúndizgi mektep", "Day school", "Kunduzgi maktab", "Дневная школа"),
 "f3": ("Rásmiy qaǵıydalar", "Official rules", "Rasmiy qoidalar", "Официальные правила"),
 "card_p": ("Mektepke alıp keliwge bolmaytuǵın ónimler: ishimlikler, chipsı, fast-fud, úy awqatları hám basqalar. Izlew, toparlar hám rásmiy PDF.",
            "What can’t be brought to school: drinks, chips, fast food, home-made food and more — with search, groups and the official PDF.",
            "Maktabga olib kelish mumkin bo‘lmagan mahsulotlar: ichimliklar, chips, fast-fud, uy ovqatlari va boshqalar — qidiruv, guruhlar va rasmiy PDF.",
            "Что нельзя приносить в школу: напитки, чипсы, фастфуд, домашняя еда и другое — с поиском, группами и официальным PDF."),
 "see": ("Tolıq kóriw", "See the full list", "To‘liq ko‘rish", "Смотреть полностью"),
}

def tabs(sub, i, href):
    ic = {"canteen/": I_BOWL, "canteen/not-allowed/": I_WARN}
    col = {"canteen/": "#2f8f5b", "canteen/not-allowed/": "#d6452f"}
    items = "".join(f'<a href="{href(k)}"' + (' aria-current="page"' if k == sub else "") + f'><span class="mi" style="--mc:{col[k]}">{_svg(ic[k], 18)}</span>{NAMES[k][i]}</a>' for k in SUBS)
    js = "<script>(function(){var a=document.querySelector('.abtabs [aria-current]');if(a){var n=a.parentNode;n.scrollLeft=a.offsetLeft-n.offsetLeft-16}})();</script>"
    return f'<nav class="abtabs" aria-label="{NAME[i]}">{items}</nav>{js}'

def hub(i, up, href):
    facts = "".join(f'<li style="--ac:{c}"><span>{_svg(p, 22)}</span><b>{t[i]}</b></li>' for p, c, t in
                    [(I_PLATE, "#2f8f5b", H["f1"]), (I_HOME, "#2a7fd1", H["f2"]), (I_SHIELD, "#d6452f", H["f3"])])
    icons = "".join(f'<span class="cnmi" style="--ac:{c}">{_svg(p, 22)}</span>' for p, c, _ in TOP)
    card = (f'<a class="cnlink card" href="{href("canteen/not-allowed/")}"><div class="cnlh"><span class="cnci">{_svg(I_WARN, 28)}</span>'
            f'<div><h2>{NAMES["canteen/not-allowed/"][i]}</h2><p>{H["card_p"][i]}</p></div></div>'
            f'<div class="cnmis">{icons}</div><div class="cnstat"><div><b>{count()}</b><span>{X["items"][i]}</span></div><div><b>{len(CATS)}</b><span>{X["groups"][i]}</span></div></div>'
            f'<span class="btn p">{H["see"][i]} →</span></a>')
    return (f'{tabs("canteen/", i, href)}<div class="cnhero cnhub"><div><span class="cntag">{_svg(I_HEART, 16)} {X["tag"][i]}</span>'
            f'<h2>{H["intro_h"][i]}</h2><p>{H["intro_p"][i]}</p><ul class="cnfacts">{facts}</ul></div>'
            f'<div class="cnplate ok" aria-hidden="true"><div class="cnp1">{_svg(I_WATER, 30)}</div><div class="cnp2">{_svg(I_APPLE, 30)}</div>'
            f'<div class="cnp3">{_svg(I_TEA, 30)}</div><div class="cnp4">{_svg(I_PLATE, 30)}</div></div></div>{card}')

def count():
    return sum(len(c[4]) for c in CATS)

def body(sub, i, up, href):
    return hub(i, up, href) if sub == "canteen/" else tabs(sub, i, href) + full(i, up, href)

def full(i, up, href):
    n = count()
    plate = (f'<div class="cnplate" aria-hidden="true"><div class="cnp1">{_svg(I_CHIPS, 30)}</div><div class="cnp2">{_svg(I_CAN, 30)}</div>'
             f'<div class="cnp3">{_svg(I_BURGER, 30)}</div><div class="cnp4">{_svg(I_GUM, 30)}</div><div class="cnno"></div></div>')
    hero = (f'<div class="cnhero"><div><span class="cntag">{_svg(I_HEART, 16)} {X["tag"][i]}</span><h2>{X["hero_h"][i]}</h2><p>{X["hero_p"][i]}</p>'
            f'<div class="cnstat"><div><b>{n}</b><span>{X["items"][i]}</span></div><div><b>{len(CATS)}</b><span>{X["groups"][i]}</span></div></div>'
            f'<div class="btns"><a class="btn p" href="{up}{PDF}" download>{_svg(I_DL, 18)} {X["pdf"][i]}</a><a class="btn s" href="#cnlist">{X["list_h"][i]} ↓</a></div></div>{plate}</div>')
    top = "".join(f'<li style="--ac:{c}"><span class="cnti">{_svg(p, 34, 1.8)}<i>{_svg(I_X, 14, 3)}</i></span><b>{t[i]}</b></li>' for p, c, t in TOP)
    top = f'<h2>{X["top_h"][i]}</h2><p class="cnsub">{X["top_p"][i]}</p><ul class="cntop">{top}</ul>'
    chips = f'<button type="button" class="cnchip" aria-pressed="true" data-c="all">{X["all"][i]} <em>{n}</em></button>' + "".join(
        f'<button type="button" class="cnchip" aria-pressed="false" data-c="{k}" style="--ac:{c}">{_svg(p, 16)} {nm[i]} <em>{len(L)}</em></button>' for k, c, p, nm, L in CATS)
    cards = ""
    for k, c, p, nm, L in CATS:
        items = "".join(f'<li><span class="cnx">{_svg(I_X, 12, 3)}</span><span class="cnt">{it[i]}</span></li>' for it in L)
        cards += (f'<section class="cncat" data-c="{k}" style="--ac:{c}"><header><span class="cnci">{_svg(p, 28)}</span><h3>{nm[i]}</h3><b class="cncn">{len(L)}</b></header>'
                  f'<ul>{items}</ul></section>')
    search = (f'<label class="cnsearch">{_svg(I_SEARCH, 20)}<input type="search" id="cnq" placeholder="{X["search"][i]}" autocomplete="off"></label>'
              f'<p class="cnres" id="cnres" role="status"></p>')
    lst = f'<h2 id="cnlist">{X["list_h"][i]}</h2>{search}<div class="cnchips">{chips}</div><div class="cncats">{cards}</div><p class="cnnone" id="cnnone" hidden>{X["none"][i]}</p>'
    why = "".join(f'<div class="card cnwhy" style="--ac:{c}"><span class="cnci">{_svg(p, 26)}</span><h3>{h[i]}</h3><p>{t[i]}</p></div>' for p, c, h, t in WHY)
    better = "".join(f'<li style="--ac:{c}"><span class="cnbi">{_svg(p, 26)}<i>{_svg(I_OK, 12, 3)}</i></span><b>{t[i]}</b></li>' for p, c, t in BETTER)
    sec2 = (f'<h2>{X["why_h"][i]}</h2><div class="cnwhys">{why}</div>'
            f'<div class="card cnbetter"><h2>{X["better_h"][i]}</h2><p>{X["better_p"][i]}</p><ul>{better}</ul><p class="cnpar">{X["parents"][i]}</p></div>')
    doc = (f'<div class="card cndoc"><a class="cnthumb" href="{up}{PDF}" target="_blank" rel="noopener"><img src="{up}{THUMB}" alt="{X["doc_h"][i]}" width="662" height="936"><span>PDF</span></a>'
           f'<div><span class="cntag">{_svg(I_SHIELD, 16)} {X["doc_h"][i]}</span><h3>{X["doc_p"][i]}</h3>'
           f'<div class="btns"><a class="btn p" href="{up}{PDF}" download>{_svg(I_DL, 18)} {X["dl"][i]}</a><a class="btn s" href="{up}{PDF}" target="_blank" rel="noopener">{X["open"][i]} →</a></div></div></div>')
    js = ("<script>(function(){var q=document.getElementById('cnq'),res=document.getElementById('cnres'),none=document.getElementById('cnnone'),cur='all',FOUND="
          + json.dumps(X["found"][i]) + ";"
          "var ch=document.querySelectorAll('.cnchip'),cats=document.querySelectorAll('.cncat');"
          "function norm(s){return s.toLowerCase().replace(/[ʻʼ‘’'`]/g,'')}"
          "function run(){var v=norm(q.value.trim()),tot=0;cats.forEach(function(c){var show=cur==='all'||c.dataset.c===cur,n=0;"
          "c.querySelectorAll('li').forEach(function(li){var m=!v||norm(li.textContent).indexOf(v)>-1;li.hidden=!m;li.classList.toggle('hit',!!v&&m);if(m)n++});"
          "c.hidden=!show||n===0;if(!c.hidden)tot+=n});none.hidden=tot>0;res.textContent=v?(tot+' '+FOUND):''}"
          "q.addEventListener('input',run);ch.forEach(function(b){b.addEventListener('click',function(){cur=b.dataset.c;ch.forEach(function(x){x.setAttribute('aria-pressed',x===b)});run()})})})();</script>")
    return f'{hero}{top}{lst}{sec2}<h2>{X["doc_h"][i]}</h2>{doc}{js}'
