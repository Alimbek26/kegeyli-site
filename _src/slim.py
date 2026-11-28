# Post-build slimming: parts repeated on many pages are moved into shared files
# that the browser downloads once and then keeps in its cache.
#  - inline <script> blocks repeated on 3+ pages  -> js/<hash>.js
#  - inline <svg> icons repeated 10+ times        -> one sprite file icons.<hash>.svg, used with <use href>
#  - whitespace between tags is collapsed
import hashlib, os, re, collections

SCRIPT = re.compile(r"<script>(.*?)</script>", re.S)
SVG = re.compile(r"(<svg\b[^>]*>)(.*?)(</svg>)", re.S)
JS_MIN, JS_MIN_PAGES, SVG_MIN_USES = 250, 3, 10


def _h(s):
    return hashlib.sha1(s.encode()).hexdigest()[:10]


def _split(html):
    """Yield (is_protected, text) so we never touch <script>/<style>/<pre>/<textarea> contents."""
    pos = 0
    for m in re.finditer(r"<(script|style|pre|textarea)\b.*?</\1>", html, re.S):
        yield False, html[pos:m.start()]
        yield True, m.group(0)
        pos = m.end()
    yield False, html[pos:]


def run(root):
    files = []
    for d, dirs, fs in os.walk(root):
        dirs[:] = [x for x in dirs if not x.startswith((".", "_")) and x not in ("js",)]
        files += [os.path.join(d, f) for f in fs if f.endswith(".html")]
    pages = {f: open(f, encoding="utf-8").read() for f in files}

    # 1. shared scripts
    jcount = collections.Counter()
    for s in pages.values():
        for body in set(SCRIPT.findall(s)):
            if len(body) >= JS_MIN:
                jcount[body] += 1
    shared = {b: f"js/{_h(b)}.js" for b, n in jcount.items() if n >= JS_MIN_PAGES}

    # 2. icon sprite
    scount = collections.Counter()
    for s in pages.values():
        for prot, part in _split(s):
            if not prot:
                for _, inner, _ in SVG.findall(part):
                    if inner.strip() and " id=" not in inner and "url(#" not in inner and "<use" not in inner:
                        scount[inner] += 1
    icons = {inner: f"i{k}" for k, (inner, n) in enumerate(scount.most_common()) if n >= SVG_MIN_USES}
    sprite = ('<svg xmlns="http://www.w3.org/2000/svg">'
              + "".join(f'<symbol id="{i}" overflow="visible">{inner}</symbol>' for inner, i in icons.items()) + "</svg>")
    sprite_name = f"icons.{_h(sprite)}.svg"

    # clean old generated files, write new ones
    os.makedirs(os.path.join(root, "js"), exist_ok=True)
    keep = {os.path.basename(v) for v in shared.values()}
    for f in os.listdir(os.path.join(root, "js")):
        if re.fullmatch(r"[0-9a-f]{10}\.js", f) and f not in keep:
            os.remove(os.path.join(root, "js", f))
    for b, name in shared.items():
        open(os.path.join(root, name), "w", encoding="utf-8").write(b.strip() + "\n")
    for f in os.listdir(root):
        if re.fullmatch(r"icons\.[0-9a-f]{10}\.svg", f) and f != sprite_name:
            os.remove(os.path.join(root, f))
    open(os.path.join(root, sprite_name), "w", encoding="utf-8").write(sprite)

    before = after = 0
    for f, s in pages.items():
        before += len(s.encode())
        up = os.path.relpath(root, os.path.dirname(f)).replace(os.sep, "/")
        up = "" if up == "." else up + "/"
        s = SCRIPT.sub(lambda m: f'<script src="{up}{shared[m.group(1)]}"></script>' if m.group(1) in shared else m.group(0), s)
        out = []
        for prot, part in _split(s):
            if not prot:
                part = SVG.sub(lambda m: f'{m.group(1)}<use href="{up}{sprite_name}#{icons[m.group(2)]}"/>{m.group(3)}'
                               if m.group(2) in icons else m.group(0), part)
                part = re.sub(r"\n\s+", "\n", part)
            out.append(part)
        s = "".join(out)
        after += len(s.encode())
        open(f, "w", encoding="utf-8").write(s)
    return len(pages), before, after, len(shared), len(icons)
