# Individual teacher profile pages: teachers/<slug>/ (4 languages). Built from teachers.py, profiles.py, heads.py and timetable.json.
import html as _html, json, os, re
from teachers import TEACHERS, SUBJECTS, CATS, latin
from profiles import PROFILES, UNI, DEG, SPEC
import heads as HD

LANGS = ["kaa", "en", "uz", "ru"]
def slug(n):
    return re.sub(r"[^a-z0-9]+", "-", latin(n).lower().replace("ǵ", "g")).strip("-")
SUB = {f"teachers/{slug(t[0])}/": j for j, t in enumerate(TEACHERS)}
def sub_of(j):
    return f"teachers/{slug(TEACHERS[j][0])}/"
def name(j, lang):
    return TEACHERS[j][0] if lang == "ru" else latin(TEACHERS[j][0])

# timetable "Surname I" -> teacher index
def _norm(s):
    s = s.lower()
    for a, b in [("ǵ", "g"), ("q", "k"), ("w", "u"), ("v", "u"), ("ı", "i"), ("á", "a"), ("ó", "o"), ("ú", "u"), ("ń", "n"), ("x", "h"), ("sh", "s")]:
        s = s.replace(a, b)
    return s
# Teachers whose weekly lesson count must not be shown (latin name prefix)
HIDE_LPW = ["Shukirillaev"]
def hide_lpw(j):
    return any(latin(TEACHERS[j][0]).startswith(x) for x in HIDE_LPW)
MANUAL = {"Daurxanov J": "Davirxanov"}
def tt_index(tt):
    names = {x[1] for cl in tt["classes"].values() for day in cl.values() for p in day.values() for x in p if x[1]}
    M = {}
    for t in names:
        if t in MANUAL:
            c = [j for j, x in enumerate(TEACHERS) if latin(x[0]).startswith(MANUAL[t])]
        else:
            sur, ini = t.split()[0], t.split()[1]
            c = [j for j, x in enumerate(TEACHERS) if _norm(latin(x[0]).split()[0])[:5] == _norm(sur)[:5] and _norm(latin(x[0]).split()[1])[:1] == _norm(ini)[:1]]
            if len(c) != 1:
                c = [j for j, x in enumerate(TEACHERS) if _norm(latin(x[0]).split()[0])[:4] == _norm(sur)[:4]]
        if len(c) == 1:
            M[t] = c[0]
    return M

X = {
 "back": ("Barlıq muǵallimler", "All teachers", "Barcha o‘qituvchilar", "Все учителя"),
 "teacher": ("{s} muǵallimi", "{s} teacher", "{s} o‘qituvchisi", "Учитель: {s}"),
 "lead": ("{c} klass basshısı", "Class teacher of {c}", "{c} sinf rahbari", "Классный руководитель {c}"),
 "lpw": ("sabaq háptesine", "lessons a week", "ta dars haftasiga", "уроков в неделю"),
 "ncls": ("klassta sabaq beredi", "classes taught", "ta sinfda dars beradi", "классов"),
 "nach": ("jetiskenlik", "achievements", "ta yutuq", "достижений"),
 "grad": ("pitkergen jılı", "graduated", "bitirgan yili", "год окончания"),
 "edu_h": ("Bilimi", "Education", "Ma’lumoti", "Образование"),
 "about_h": ("Qánigelik", "Professional profile", "Mutaxassislik", "Профессиональный профиль"),
 "spec": ("Qánigeligi", "Specialization", "Mutaxassisligi", "Специальность"),
 "cat": ("Kategoriyası", "Category", "Toifasi", "Категория"),
 "train": ("Sońǵı malaka asırıw", "Latest professional development", "So‘nggi malaka oshirish", "Последнее повышение квалификации"),
 "since": ("Mektepte", "At the school since", "Maktabda", "В школе с"),
 "pos": ("Lawazımı", "Position", "Lavozimi", "Должность"),
 "ach_h": ("Jetiskenlikleri", "Achievements", "Yutuqlari", "Достижения"),
 "cls_h": ("Bul jılı sabaq beretuǵın klassları", "Classes this year", "Bu yil dars beradigan sinflari", "Классы в этом году"),
 "cls_n": ("{n} sabaq/hápte", "{n} lessons/week", "{n} dars/hafta", "{n} ур./нед."),
 "sched_h": ("Háptelik keste", "Weekly schedule", "Haftalik jadval", "Расписание на неделю"),
 "days": (("Dú", "Si", "Sá", "Pi", "Ju"), ("Mon", "Tue", "Wed", "Thu", "Fri"), ("Du", "Se", "Ch", "Pa", "Ju"), ("Пн", "Вт", "Ср", "Чт", "Пт")),
 "les": ("Sabaq", "Lesson", "Dars", "Урок"),
 "tt": ("Tolıq sabaq kestesi", "Full timetable", "To‘liq dars jadvali", "Полное расписание"),
 "share": ("Bólisiw", "Share", "Ulashish", "Поделиться"),
 "copied": ("Silteme kóshirildi", "Link copied", "Havola nusxalandi", "Ссылка скопирована"),
 "coll_h": ("Kásiplesleri", "Colleagues in {s}", "Hamkasblari", "Коллеги"),
 "none_tt": ("Bul muǵallim ushın keste joq.", "No timetable entries for this teacher.", "Bu o‘qituvchi uchun jadval yo‘q.", "Для этого учителя нет расписания."),
 "desc": ("{n} — Kegeyli rayonı qánigelestirilgen mektebiniń {s} muǵallimi: bilimi, jetiskenlikleri hám sabaq kestesi.",
          "{n}, {s} teacher at Kegeyli District Specialized School: education, achievements and weekly schedule.",
          "{n} — Kegeyli tumani ixtisoslashtirilgan maktabining {s} o‘qituvchisi: ma’lumoti, yutuqlari va dars jadvali.",
          "{n} — учитель ({s}) Кегейлийской районной специализированной школы: образование, достижения и расписание."),
}
CATCOL = {"high": "#0b5f78", "first": "#2a8a9e", "second": "#a3202c", "spec": "#7a6a4f", None: "#5b6472"}

def _svg(p, s=22, w=2):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
I_CAP = '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5M22 9v6"/>'
I_STAR = '<path d="M12 3l2.700 5.600 6.100.9-4.400 4.300 1 6.100L12 17l-5.400 2.900 1-6.100L3.200 9.500l6.100-.9z"/>'
I_CERT = '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M7 9h10M7 12h6"/><circle cx="16" cy="17" r="3"/>'
I_MEDAL = '<circle cx="12" cy="15" r="6"/><path d="M8.500 10.200L5 3h4l3 6 3-6h4l-3.500 7.200"/>'
I_BOOK = '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 21V5M9 7h6"/>'
I_CLK = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'
I_USR = '<circle cx="9" cy="8" r="3"/><path d="M3 20c.5-3.500 3-5.500 6-5.500s5.500 2 6 5.500"/><path d="M16 6a3 3 0 0 1 0 5.500M18 14.500c1.700.8 2.700 2.500 3 5"/>'
I_SHARE = '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.600 13.500l6.800 4M15.400 6.500l-6.800 4"/>'
I_TG = '<path d="M21 4L3 11l6 2 2 6 3-4 5 4z"/><path d="M9 13l8-6"/>'
I_UP = '<path d="M4 15l4-4 4 3 7-7"/><path d="M15 7h4v4"/>'

def _ach_icon(a):
    s = a.lower()
    if any(k in s for k in ("sat", "ielts", "sertif", "certif", "cefr", "toefl")):
        return I_CERT, "#7c3aed"
    if any(k in s for k in ("olimp", "olymp", "medal", "orın", "place", "o‘rin", "место", "jeńimpaz", "winner", "g‘olib", "побед")):
        return I_MEDAL, "#d4a017"
    if any(k in s for k in ("malaka", "training", "kurs", "course", "kurs", "трен")):
        return I_UP, "#0b7a8f"
    return I_STAR, "#d6452f"

def schedule(j, tt, M):
    """returns {(day, period): [(class, subj_sheet_name)]}"""
    K = ["mon", "tue", "wed", "thu", "fri"]; out = {}
    for c, cl in tt["classes"].items():
        for d, k in enumerate(K):
            for p, xs in (cl.get(k) or {}).items():
                for s, t in xs:
                    if t and M.get(t) == j:
                        out.setdefault((d, int(p)), []).append((c, s))
    return out

def body(sub, lang, up, href, ctx):
    i = LANGS.index(lang); esc = _html.escape; j = SUB[sub]
    cy, sk, ck = TEACHERS[j]; pr = PROFILES[j]; nm = name(j, lang); subj = SUBJECTS[sk][lang]
    tt, M, TT_SUBJ, BELLS, ROOT = ctx["tt"], ctx["M"], ctx["TT_SUBJ"], ctx["BELLS"], ctx["ROOT"]
    col = CATCOL.get(ck, "#5b6472"); sl = slug(cy)
    photo = os.path.exists(os.path.join(ROOT, "photos", "teachers", sl + ".jpg"))
    ini = "".join(w[0] for w in nm.split()[:2])
    av = f'<img src="{up}photos/teachers/{sl}.jpg" alt="{esc(nm)}">' if photo else f'<span>{ini}</span>'
    leads = [c for c in HD.HEAD if HD.HEAD[c][0] == cy]
    S = schedule(j, tt, M)
    per_cls = {}
    for (d, p), xs in S.items():
        for c, s in xs:
            per_cls.setdefault(c, {}).setdefault(s, 0); per_cls[c][s] += 1
    lpw = len(S)
    chips = (f'<span class="tpchip" style="--ac:{col}">{_svg(I_BOOK, 16)} {X["teacher"][i].format(s=subj)}</span>'
             + (f'<span class="tpchip gold">{_svg(I_STAR, 16)} {CATS[ck][lang]}</span>' if ck else "")
             + "".join(f'<span class="tpchip lead">{_svg(I_USR, 16)} {X["lead"][i].format(c=c)}</span>' for c in leads))
    share = (f'<div class="tpshare"><button type="button" class="btn s" id="tpsh">{_svg(I_SHARE, 18)} {X["share"][i]}</button>'
             f'<a class="btn s" id="tptg" href="#" rel="noopener">{_svg(I_TG, 18)} Telegram</a><span id="tpok" role="status"></span></div>')
    hero = (f'<p class="rsback"><a href="{href("teachers/")}">← {X["back"][i]}</a></p>'
            f'<div class="tphero" style="--ac:{col}"><div class="tpav">{av}</div><div class="tpht"><h2>{esc(nm)}</h2><div class="tpchips">{chips}</div>{share}</div></div>')
    grad = max((y for y, u, d in pr["edu"]), default=None)
    tiles = ([] if hide_lpw(j) else [(lpw or "—", X["lpw"][i], I_CLK, "#2a7fd1")]) + [(len(per_cls) or "—", X["ncls"][i], I_USR, "#0b7a8f"),
             (len(pr["ach"]), X["nach"][i], I_STAR, "#d4a017")]
    if grad:
        tiles.append((grad, X["grad"][i], I_CAP, "#7c3aed"))
    tiles = '<div class="actiles">' + "".join(f'<div class="actile" style="--ac:{c}"><span class="aci">{_svg(p)}</span><b>{v}</b><span>{l}</span></div>' for v, l, p, c in tiles) + '</div>'
    # education timeline + profile facts
    edu = "".join(f'<li><span class="tpy">{y}</span><div><b>{UNI[u][i]}</b><small>{DEG[d][i]}</small></div></li>' for y, u, d in sorted(pr["edu"]))
    facts = ""
    if pr.get("pos"):
        facts += f'<div><dt>{X["pos"][i]}</dt><dd>{pr["pos"][i]}</dd></div>'
    if pr["spec"]:
        facts += f'<div><dt>{X["spec"][i]}</dt><dd>{SPEC[pr["spec"]][i]}</dd></div>'
    if ck:
        facts += f'<div><dt>{X["cat"][i]}</dt><dd>{CATS[ck][lang]}</dd></div>'
    if pr.get("since"):
        facts += f'<div><dt>{X["since"][i]}</dt><dd>{pr["since"]}</dd></div>'
    if pr["train"]:
        facts += f'<div><dt>{X["train"][i]}</dt><dd>{pr["train"]}</dd></div>'
    two = (f'<div class="actwo"><div class="card tpedu"><h3>{_svg(I_CAP, 20)} {X["edu_h"][i]}</h3><ol>{edu}</ol></div>'
           f'<div class="card tpfacts"><h3>{_svg(I_BOOK, 20)} {X["about_h"][i]}</h3><dl>{facts}</dl></div></div>')
    ach = ""
    if pr["ach"]:
        cards = ""
        for a in pr["ach"]:
            ic, c = _ach_icon(a[1] + " " + a[i])
            cards += f'<li style="--ac:{c}"><span>{_svg(ic, 20)}</span><p>{esc(a[i])}</p></li>'
        ach = f'<h2>{X["ach_h"][i]}</h2><ul class="tpach">{cards}</ul>'
    # classes
    cls = ""
    if per_cls:
        order = sorted(per_cls, key=lambda c: (int(c.split("-")[0]), c))
        cc = ""
        for c in order:
            n = sum(per_cls[c].values()); ss = ", ".join(TT_SUBJ.get(s, (s,) * 4)[i] for s in per_cls[c])
            cc += f'<li class="{"lead" if c in leads else ""}"><b>{c}</b><span>{ss}</span>' + ("" if hide_lpw(j) else f'<small>{X["cls_n"][i].format(n=n)}</small>') + '</li>'
        cls = f'<h2>{X["cls_h"][i]}</h2><ul class="tpcls">{cc}</ul>'
    # weekly grid
    sched = ""
    if S and not hide_lpw(j):
        P = sorted({p for d, p in S}); rows = ""
        head = "".join(f"<th>{d}</th>" for d in X["days"][i])
        for p in range(1, max(P) + 1):
            cells = ""
            for d in range(5):
                xs = S.get((d, p))
                if xs:
                    c, s = xs[0]; scol = TT_SUBJ.get(s, ("",) * 4 + ("#0b7a8f",))[4]
                    cells += f'<td><span class="tpcell" style="--ac:{scol}"><b>{c}</b><small>{TT_SUBJ.get(s, (s,) * 4)[i]}</small></span></td>'
                else:
                    cells += "<td></td>"
            a, e = BELLS[p - 1] if p - 1 < len(BELLS) else ("", "")
            rows += f'<tr><th><b>{p}</b><small>{a}</small></th>{cells}</tr>'
        sched = (f'<h2>{X["sched_h"][i]}</h2><div class="card tpsched"><table><thead><tr><th></th>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
                 f'<p><a class="btn s" href="{href("timetable/")}">{X["tt"][i]} →</a></p>')
    colls = [k for k, t in enumerate(TEACHERS) if t[1] == sk and k != j]
    coll = ""
    if colls:
        coll = f'<h2>{X["coll_h"][i].format(s=subj)}</h2><div class="tpcoll">' + "".join(
            f'<a href="{href(sub_of(k))}" style="--ac:{CATCOL.get(TEACHERS[k][2], "#5b6472")}"><span>{"".join(w[0] for w in name(k, lang).split()[:2])}</span>{esc(name(k, lang))}</a>' for k in colls) + '</div>'
    js = ("<script>(function(){var u=location.href,t=document.title,ok=document.getElementById('tpok');"
          "document.getElementById('tptg').href='https://t.me/share/url?url='+encodeURIComponent(u)+'&text='+encodeURIComponent(t);"
          "document.getElementById('tpsh').addEventListener('click',function(){if(navigator.share){navigator.share({title:t,url:u}).catch(function(){})}"
          "else if(navigator.clipboard){navigator.clipboard.writeText(u).then(function(){ok.textContent=" + json.dumps(X["copied"][i]) + "})}})})();</script>")
    return f'{hero}{tiles}{two}{ach}{cls}{sched}{coll}{js}'

def desc(j):
    sk = TEACHERS[j][1]
    return tuple(X["desc"][n].format(n=name(j, l), s=SUBJECTS[sk][l].lower() if n != 1 else SUBJECTS[sk][l]) for n, l in enumerate(LANGS))
