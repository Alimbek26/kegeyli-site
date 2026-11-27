# Facts for the School Profile (not published yet). Confirmed by the school counselor, 28.11.2026.
ADMISSION = "Entrance exams run by the Agency for Specialized Educational Institutions at grade 5 and grade 7."
COUNSELOR = dict(name="Alimbek Jumamuratov", role="School Counselor", email="ixm013@piima.uz")
# Enrolment 2026/2027: students who sat the CHSB diagnostic tests (Oct–Nov 2026); absentees not counted.
ENROLMENT = {5: 48, 6: 46, 7: 69, 8: 45, 9: 69, 10: 69, 11: 37}   # total 383, 17 classes, 43 teachers
# Grade distribution: official CHSB assessment, grades 9–11, from "Kegeyli IM ko'rsatgich" table 4 (5/4/3/2 counts).
CHSB = {  # year: {grade: {subject: (sat, n5, n4, n3, n2)}}
 "2025/2026": {9: {"math": (44, 10, 34, 0, 0), "phys": (44, 2, 42, 0, 0), "chem": (21, 11, 10, 0, 0)},
               10: {"math": (38, 11, 27, 0, 0), "phys": (38, 8, 30, 0, 0)},
               11: {"math": (34, 11, 23, 0, 0), "phys": (34, 5, 29, 0, 0), "chem": (22, 3, 19, 0, 0)}},
}
