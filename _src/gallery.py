# Photo gallery (Gallery page is being prepared). Photos live in photos/gallery/<section>/:
#   <name>.jpg (max 1600 px, for the large view) and <name>-t.jpg (600 px thumbnail).
# Sections: building, classrooms, labs, library, canteen, sports, events.
# consent: True once the people shown (and parents, for students) agreed to publication.
# who: teachers shown (Cyrillic names exactly as in teachers.TEACHERS) - links the photo to their profiles.
SECTIONS = ["building", "classrooms", "labs", "library", "canteen", "sports", "events"]
PHOTOS = [
 dict(section="events", file="events/uzbek-language-teachers", who=["Исмайлова Гулмира", "Қутлимуратов Сарманбек"], consent=True,
      cap=("Ózbek tili hám ádebiyatı muǵallimleri Ismaylova Gulmira hám Qutlimuratov Sarmanbek",
           "Uzbek language and literature teachers Ismaylova Gulmira and Qutlimuratov Sarmanbek",
           "O‘zbek tili va adabiyoti o‘qituvchilari Ismaylova Gulmira va Qutlimuratov Sarmanbek",
           "Учителя узбекского языка и литературы Исмайлова Гулмира и Қутлимуратов Сарманбек")),
 dict(section="events", file="events/olympiad-diploma", leader="Islam Pirniyazov", consent=True,   # student and parents agreed
      todo="add student name, class, olympiad name/subject and date",
      cap=("Islam Pirniyazov olimpiada jeńimpazına 1-dárejeli diplom tapsırmaqta",
           "Islam Pirniyazov presents a 1st-degree olympiad diploma",
           "Islam Pirniyazov olimpiada g‘olibiga 1-darajali diplom topshirmoqda",
           "Ислам Пирниязов вручает диплом I степени победителю олимпиады")),
]
