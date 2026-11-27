# Class teachers (klass basshıları), 2026/2027. Value = surname as in teachers.py (Latin) — resolved to the full teacher entry.
from teachers import TEACHERS, latin, latin_raw
HEADS = [("5-A", "Aynazarov Qurbanazar"), ("5-B", "Begalieva"), ("6-A", "Qarlibaeva"), ("6-B", "Xudaybergenova"),
         ("7-A", "Qutlimuratov"), ("7-B", "Erejepov"), ("7-C", "Qudaybergenov"), ("8-A", "Orazalieva"), ("8-B", "Oserbaeva"),
         ("9-A", "Salieva"), ("9-B", "Shukirillaev"), ("9-C", "Joldasbaev"), ("10-A", "Nazbergenova"), ("10-B", "Davirxanov"),
         ("10-C", "Elmuratova"), ("11-A", "Tajimuratova"), ("11-B", "Sarsenbaev")]
def _find(key):
    m = [t for t in TEACHERS if latin_raw(t[0]).startswith(key)]
    assert len(m) == 1, (key, m)
    return m[0]
HEAD = {c: _find(k) for c, k in HEADS}          # class -> (cyrillic, subject, category)
def name(c, lang):
    cy = HEAD[c][0]
    return cy if lang == "ru" else latin(cy)
T = {
 "h": ("Klass basshıları", "Class teachers", "Sinf rahbarlari", "Классные руководители"),
 "p": ("2026/2027 oqıw jılı: {n} klass hám olardıń basshıları. Atına basıń — muǵallimniń kartası ashıladı.",
       "2026/2027 school year: {n} classes and their class teachers. Tap a name to open the teacher’s card.",
       "2026/2027 o‘quv yili: {n} ta sinf va ularning rahbarlari. Ismni bosing — o‘qituvchi kartasi ochiladi.",
       "2026/2027 учебный год: {n} классов и их руководители. Нажмите на имя — откроется карточка учителя."),
 "one": ("Klass basshısı", "Class teacher", "Sinf rahbari", "Классный руководитель"),
 "grade": ("{g}-klasslar", "Grade {g}", "{g}-sinflar", "{g} классы"),
 "total": ("klass", "classes", "ta sinf", "классов"),
}
DESC = ("Kegeyli rayonı qánigelestirilgen mektebiniń klass basshıları: 17 klass hám olardıń basshıları.",
        "Class teachers of Kegeyli District Specialized School: 17 classes and who leads each one.",
        "Kegeyli tumani ixtisoslashtirilgan maktabining sinf rahbarlari: 17 ta sinf va ularning rahbarlari.",
        "Классные руководители Кегейлийской районной специализированной школы: 17 классов и их руководители.")
