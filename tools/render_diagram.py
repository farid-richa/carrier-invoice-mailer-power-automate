"""Render tools/flow_diagram.html to docs/flow.png (needs Playwright + Chromium).

    python tools/render_diagram.py
"""
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1180, "height": 800}, device_scale_factor=2)
    page.goto((ROOT / "tools" / "flow_diagram.html").as_uri())
    page.wait_for_timeout(300)
    page.locator(".page").screenshot(path=str(ROOT / "docs" / "flow.png"))
    browser.close()
print("wrote docs/flow.png")
