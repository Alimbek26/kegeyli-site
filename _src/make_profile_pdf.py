# Makes files/kegeyli-school-profile-2026-2027.pdf from school-profile/index.html (needs Chrome + Playwright).
# Run after build.py, then run build.py again so the page shows the "Download PDF" button.
import os, sys, subprocess, time
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import school_profile as SP
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8799"], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
try:
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = b.new_page()
        pg.goto("http://localhost:8799/school-profile/"); pg.wait_for_timeout(800)
        os.makedirs(os.path.join(ROOT, "files"), exist_ok=True)
        pg.pdf(path=os.path.join(ROOT, SP.PDF), format="A4", print_background=True, margin=dict(top="0", bottom="0", left="0", right="0"))
        b.close()
finally:
    srv.terminate()
print("PDF:", SP.PDF)
