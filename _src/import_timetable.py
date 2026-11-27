#!/usr/bin/env python3
"""Convert the school's teacher timetable (sabaq keste .xlsx) into _src/timetable.json (per class).
Usage: python3 _src/import_timetable.py path/to/sabaq_keste.xlsx [dd.mm.yyyy]
Layout expected: row 9-10 headers; col B teacher, col C subject; D..K Mon 1-8, L..S Tue, T..AA Wed, AB..AI Thu, AJ..AP Fri 1-7.
"""
import json, sys, os, re, collections, openpyxl
from openpyxl.utils import column_index_from_string as ci
src = sys.argv[1]; date = sys.argv[2] if len(sys.argv) > 2 else ""
ws = openpyxl.load_workbook(src, data_only=True).worksheets[0]
DAYS = {"mon": ("D", 8), "tue": ("L", 8), "wed": ("T", 8), "thu": ("AB", 8), "fri": ("AJ", 7)}
CLEAN = {"Temirxanaova Aynur": "Temirxanova A", "Uteshova (tarbiya)": "Uteshova G", "Erejepov Z (dene t)": "Erejepov Z", "Vakant (xim)": "", "Jumamuratov A": ""}  # "" = keep the lesson, hide the name
tt = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(list)))
for r in range(11, ws.max_row + 1):
    row = [c.value for c in ws[r]]
    if not (row[1] and row[2]) or not isinstance(row[0], int):
        continue
    t = str(row[1]).strip(); t = CLEAN.get(t, t); s = str(row[2]).strip()
    for d, (col, n) in DAYS.items():
        c0 = ci(col) - 1
        for k in range(n):
            v = row[c0 + k]
            if v:
                tt[str(v).strip().upper()][d][str(k + 1)].append([s, t])
classes = sorted(tt, key=lambda c: (int(c.split("-")[0]), c.split("-")[1]))
out = {"date": date, "classes": {c: {d: dict(sorted(tt[c][d].items(), key=lambda x: int(x[0]))) for d in DAYS if d in tt[c]} for c in classes}}
json.dump(out, open(os.path.join(os.path.dirname(__file__), "timetable.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("classes:", ", ".join(classes))
