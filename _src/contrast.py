# Contrast guard: generated at build time from style.css.
# Accent-coloured text is kept dark enough on light pages and light enough on dark pages,
# and accent backgrounds behind white text are kept dark enough, in both modes.
# Uses CSS relative colours (oklch(from …)); older browsers simply keep the original colours.
import re

NEUTRAL = {"--ink", "--soft", "--bg", "--card", "--line", "--tealbg"}
SKIP = re.compile(r"\.hero|\.rsn\b|footer|\.sf\b|\.hlead|::selection|:root|^html|^body")
LIGHT_MAX, DARK_MIN, BG_MAX = ".48", ".76", ".5"
LIGHTBG = re.compile(r"\.btn\.s\b|\.clmore|\.tpchip\.lead")


def _lin(c):
    c /= 255
    return c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4


def ok_l(hx):
    hx = hx.lstrip("#")
    if len(hx) == 3:
        hx = "".join(ch * 2 for ch in hx)
    r, g, b = (_lin(int(hx[k:k + 2], 16)) for k in (0, 2, 4))
    l = .4122214708 * r + .5363325363 * g + .0514459929 * b
    m = .2119034982 * r + .6806995451 * g + .1073969566 * b
    s = .0883024619 * r + .2817188376 * g + .6299787005 * b
    return .2104542553 * l ** (1 / 3) + .7936177850 * m ** (1 / 3) - .0040720468 * s ** (1 / 3)


TOKENS = {}  # light-dark() tokens from :root, e.g. --teal -> ("#0b5f78", "#2a9bbb")


def _accent(v):
    v = v.strip().replace("!important", "").strip()
    m = re.fullmatch(r"var\((--[\w-]+)(,\s*#[0-9a-fA-F]{3,6})?\)", v)
    if m:
        if m.group(1) in NEUTRAL:
            return None
        return TOKENS.get(m.group(1), v)
    if re.fullmatch(r"#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6}", v):
        return v if .3 <= ok_l(v) <= .8 else None
    return None


def _white(v):
    return v.strip().replace("!important", "").strip().lower() in ("#fff", "#ffffff", "white")


def _rules(css):
    """Top-level rules only (rules inside @media/@supports are deliberate overrides)."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    i, depth, start, out = 0, 0, 0, []
    while i < len(css):
        ch = css[i]
        if ch == "{":
            if depth == 0:
                sel, start = css[start:i].strip(), i + 1
                if sel.startswith("@"):
                    j, d = i + 1, 1
                    while d:
                        d += {"{": 1, "}": -1}.get(css[j], 0); j += 1
                    i = start = j; continue
                depth = 1
        elif ch == "}" and depth == 1:
            out.append((sel, css[start:i])); depth = 0; start = i + 1
        i += 1
    return out


def _lightbg(v):
    if not v:
        return False
    v = v.replace("!important", "").strip().lower()
    if v in ("#fff", "#ffffff", "white"):
        return True
    m = re.fullmatch(r"rgba\(255,\s*255,\s*255,\s*([\d.]+)\)", v)
    if m:
        return float(m.group(1)) >= .5
    return bool(re.fullmatch(r"#[0-9a-f]{3}|#[0-9a-f]{6}", v)) and ok_l(v) >= .75


def _mirror(css):
    """Rules written only for the theme switch (:root[data-theme=dark] X) also apply when the phone/computer itself is in dark mode."""
    out = []
    have = css.replace(":root:not([data-theme=light])", ":root[data-theme=dark]")
    for sel, body in _rules(css):
        parts = [x.strip() for x in sel.split(",")]
        if parts and all(x.startswith(":root[data-theme=dark]") for x in parts):
            if have.count(sel + "{") > 1:
                continue  # media twin exists (normalised copy found twice)
            out.append(",".join(x.replace(":root[data-theme=dark]", ":root:not([data-theme=light])", 1) for x in parts) + "{" + body + "}")
    return "@media(prefers-color-scheme:dark){" + "".join(out) + "}" if out else ""


def guard(css):
    from collections import OrderedDict
    groups = OrderedDict()
    TOKENS.update({k: (a, b) for k, a, b in re.findall(r"(--[\w-]+):light-dark\((#[0-9a-fA-F]+),\s*(#[0-9a-fA-F]+)\)", css)})
    def tc(a):
        if isinstance(a, tuple):
            return f"light-dark(oklch(from {a[0]} min(l,{LIGHT_MAX}) c h),oklch(from {a[1]} max(l,{DARK_MIN}) c h))"
        return f"light-dark(oklch(from {a} min(l,{LIGHT_MAX}) c h),oklch(from {a} max(l,{DARK_MIN}) c h))"
    def tb(a):
        if isinstance(a, tuple):
            return f"light-dark(oklch(from {a[0]} min(l,{BG_MAX}) c h),oklch(from {a[1]} min(l,{BG_MAX}) c h))"
        return f"oklch(from {a} min(l,{BG_MAX}) c h)"
    rules = _rules(css)
    bgof = {}
    for sel, body in rules:
        for d in body.split(";"):
            if ":" in d and d.split(":", 1)[0].strip() in ("background", "background-color"):
                bgof[sel] = d.split(":", 1)[1].strip()
    for sel, body in rules:
        if SKIP.search(sel):
            continue
        decl = {}
        for d in body.split(";"):
            if ":" in d:
                k, v = d.split(":", 1); decl[k.strip()] = v.strip()
        c = decl.get("color")
        if c and _accent(c):
            imp = "!important" if "!important" in c else ""
            a = _accent(c)
            if LIGHTBG.search(sel) or _lightbg(decl.get("background") or decl.get("background-color") or bgof.get(sel)):
                a0 = a[0] if isinstance(a, tuple) else a
                groups.setdefault(f"color:oklch(from {a0} min(l,{LIGHT_MAX}) c h){imp}", []).append(sel)
            else:
                groups.setdefault(f"color:{tc(a)}{imp}", []).append(sel)
        b = decl.get("background-color") or decl.get("background")
        if c and _white(c) and b and _accent(b):
            imp = "!important" if "!important" in b else ""
            groups.setdefault(f"background:{tb(_accent(b))}{imp}", []).append(sel)
    return ("\n/* contrast guard (generated) */\n" + _mirror(css) + "@supports (color:oklch(from red l c h)){"
            + "".join(f"{','.join(v)}{{{k}}}" for k, v in groups.items()) + "}\n")
