# Badges and staff statistics for the Teachers section (derived from profiles.py, heads.py and the timetable).
import re
from teachers import TEACHERS
from profiles import PROFILES
import heads as HD

BADGE = {  # key: (label x4, colour)
 "head": (("Klass basshısı {c}", "Class teacher {c}", "{c} sinf rahbari", "Кл. рук. {c}"), "#d4a017"),
 "phd": (("PhD", "PhD", "PhD", "PhD"), "#a3202c"),
 "ma": (("Magistr", "Master’s", "Magistr", "Магистр"), "#7c3aed"),
 "sat": (("SAT", "SAT", "SAT", "SAT"), "#2a7fd1"),
 "ielts": (("IELTS", "IELTS", "IELTS", "IELTS"), "#d6452f"),
 "nat": (("Milliy sertifikat", "National cert.", "Milliy sertifikat", "Нацсертификат"), "#0b7a8f"),
 "cefr": (("CEFR", "CEFR", "CEFR", "CEFR"), "#2f8f5b"),
 "tefl": (("TEFL/TKT", "TEFL/TKT", "TEFL/TKT", "TEFL/TKT"), "#b45309"),
 "award": (("Kókirek belgisi", "State award", "Ko‘krak nishoni", "Награда"), "#5b6472"),
}
def keys(j):
    p = PROFILES[j]; en = " | ".join(a[1] for a in p["ach"]); k = []
    cy = TEACHERS[j][0]
    for c, (hc, *_ ) in HD.HEAD.items():
        if hc == cy:
            k.append(("head", c))
    if re.search(r"\bPhD\b", en): k.append(("phd", None))
    if any(d == "ma" for y, u, d in p["edu"]) or "Master’s studies" in en: k.append(("ma", None))
    if re.search(r"\bSAT\b", en): k.append(("sat", None))
    if "IELTS" in en: k.append(("ielts", None))
    if re.search(r"National (certificate|C1|B2|B1)", en, re.I): k.append(("nat", None))
    if re.search(r"CEFR|Multilevel|EF SET", en): k.append(("cefr", None))
    if re.search(r"TEFL|TKT|TESOL", en): k.append(("tefl", None))
    if re.search(r"badge of honour|Medal|Excellence in Public Education", en): k.append(("award", None))
    return k
def html(j, i):
    return '<div class="tbadges">' + "".join(f'<span style="--bc:{BADGE[k][1]}">{BADGE[k][0][i].format(c=c or "")}</span>' for k, c in keys(j)) + '</div>'
def stats():
    K = [set(k for k, c in keys(j)) for j in range(len(TEACHERS))]
    return dict(total=len(TEACHERS), high=sum(1 for t in TEACHERS if t[2] == "high"), ma=sum(1 for k in K if "ma" in k or "phd" in k),
                cert=sum(1 for k in K if k & {"sat", "ielts", "nat", "cefr", "tefl"}), heads=len(HD.HEADS),
                subj=len({t[1] for t in TEACHERS}))
ST = {
 "total": ("muǵallim", "teachers", "nafar o‘qituvchi", "учителей"),
 "high": ("joqarı kategoriyalı", "highest category", "oliy toifali", "высшей категории"),
 "ma": ("magistr yamasa PhD", "master’s or PhD", "magistr yoki PhD", "магистр или PhD"),
 "cert": ("sertifikatı bar", "hold certificates", "sertifikati bor", "имеют сертификаты"),
 "heads": ("klass basshısı", "class teachers", "nafar sinf rahbari", "классных руководителей"),
 "subj": ("pán", "subjects", "ta fan", "предметов"),
}
