#!/usr/bin/env python3
"""
screenshot_themes.py — Take a uniform screenshot of every theme.

Setup (one-time):
    pip install playwright
    playwright install chromium

Usage:
    python3 scripts/screenshot_themes.py

Screenshots are saved to screenshots/<theme-id>.png
"""

import json
import os
import subprocess
import sys
import time
import threading
import http.server

# ── Config ────────────────────────────────────────────────────────────────────
PORT        = 8787
VIEWPORT    = {"width": 1280, "height": 1400}
DEMO_IP     = "1.1.1.1"   # IP shown in screenshots — change to any public IP
REPO_ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR     = os.path.join(REPO_ROOT, "screenshots")
THEMES_FILE = os.path.join(REPO_ROOT, "themes", "index.json")

# ── Local server ──────────────────────────────────────────────────────────────
class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass  # suppress server noise

def start_server():
    os.chdir(REPO_ROOT)
    server = http.server.HTTPServer(("127.0.0.1", PORT), QuietHandler)
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    return server

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    try:
        from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout
    except ImportError:
        print("Error: playwright is not installed.")
        print("Run: pip install playwright && playwright install chromium")
        sys.exit(1)

    os.makedirs(OUT_DIR, exist_ok=True)

    with open(THEMES_FILE) as f:
        themes = json.load(f)["themes"]

    print(f"Starting local server on port {PORT}...")
    server = start_server()
    time.sleep(0.5)  # let the server bind

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.set_viewport_size(VIEWPORT)

        print(f"Loading page with demo IP {DEMO_IP}...")
        page.goto(f"http://127.0.0.1:{PORT}/?ip={DEMO_IP}")

        try:
            # Wait for the IP address to appear (detection complete)
            page.wait_for_selector(".ip-address", timeout=20_000)
            # Let fonts and animations settle
            page.wait_for_timeout(800)
        except PWTimeout:
            print("Warning: IP detection timed out — screenshotting anyway.")



        print(f"\nTaking {len(themes)} screenshots...\n")

        for theme in themes:
            tid = theme["id"]
            out_path = os.path.join(OUT_DIR, f"{tid}.png")

            # Apply theme via the page's own setTheme function
            page.evaluate(f"window.setTheme && window.setTheme({json.dumps(tid)})")
            page.wait_for_timeout(350)  # allow CSS transitions to finish

            page.screenshot(path=out_path, full_page=False)
            print(f"  ✓ {tid}.png")

        browser.close()

    server.shutdown()

    print(f"\nDone. {len(themes)} screenshots saved to screenshots/")

    # Print a ready-to-paste README table
    print("\n── README table (3 columns) ────────────────────────────────────\n")
    rows = []
    row_imgs  = []
    row_names = []
    for i, theme in enumerate(themes):
        tid  = theme["id"]
        row_imgs.append(f'<img src="screenshots/{tid}.png" width="400" alt="{tid}">')
        row_names.append(f'**{tid}**')
        if (i + 1) % 3 == 0 or i == len(themes) - 1:
            while len(row_imgs) < 3:
                row_imgs.append('')
                row_names.append('')
            rows.append(f"| {' | '.join(row_imgs)} |")
            rows.append(f"| {' | '.join(row_names)} |")
            row_imgs, row_names = [], []

    header = "| | | |"
    sep    = "|---|---|---|"
    print(header)
    print(sep)
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
