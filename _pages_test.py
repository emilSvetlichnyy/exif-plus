"""Own test: one iPhone photo sent through ~10 apps (step 4 of the growth plan).

The page is built only from real results in test-results/app-metadata-test.csv.
Fill gps_kept / date_kept / camera_kept / copyright_kept with yes / no for each row
(and tested_on as YYYY-MM-DD). Rows left empty are skipped; with no filled rows the
page is not built at all, so nothing unverified is ever published.
"""
from __future__ import annotations

import csv
from pathlib import Path

CSV = Path(__file__).resolve().parent / "test-results" / "app-metadata-test.csv"
FIELDS = ("gps_kept", "date_kept", "camera_kept", "copyright_kept")


def _rows() -> list[dict]:
    if not CSV.exists():
        return []
    with CSV.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return [r for r in rows if all((r.get(k) or "").strip().lower() in ("yes", "no") for k in FIELDS)]


def _cell(v: str) -> str:
    return "Kept" if v.strip().lower() == "yes" else "Removed"


def register_test(ns: dict) -> None:
    rows = _rows()
    if not rows:
        return
    article_page, esc, NAME = ns["article_page"], ns["esc"], ns["NAME"]
    tested = max((r.get("tested_on") or "").strip() for r in rows) or "2026"
    ios = sorted({(r.get("ios_version") or "").strip() for r in rows} - {""})
    leaks = [r for r in rows if r["gps_kept"].strip().lower() == "yes"]
    clean = [r for r in rows if r["gps_kept"].strip().lower() == "no"]
    trs = "\n".join(
        f"            <tr><td>{esc(r['app'])}</td><td>{esc(r['route'])}</td>"
        + "".join(f"<td>{_cell(r[k])}</td>" for k in FIELDS)
        + f"<td>{esc((r.get('note') or '').strip())}</td></tr>"
        for r in rows
    )
    leak_list = ", ".join(f"{r['app']} ({r['route']})" for r in leaks) or "none of the routes we tested"
    article_page(
        "learn/photo-metadata-test-10-apps",
        title=f"We Sent One Photo Through {len({r['app'] for r in rows})} Apps: Who Kept GPS? | EXIF+",
        description=f"Our own test: one iPhone photo with GPS, date, camera and copyright sent through {len(rows)} app routes. Which ones kept the location, and which removed it.",
        h1="One photo, many apps: which ones keep your location?",
        lead=f"We sent the same iPhone photo through {len(rows)} sharing routes and read the received file. Here is what survived.",
        prose=f"""        <p><strong>Direct answer:</strong> In our test the GPS location survived in: {esc(leak_list)}. It was removed in {len(clean)} of {len(rows)} routes. A route that strips GPS today can change with an app update, so clean the photo yourself before sending when location matters.</p>
        <h2>Results</h2>
        <table>
          <thead><tr><th>App</th><th>Route</th><th>GPS</th><th>Date</th><th>Camera</th><th>Copyright</th><th>Note</th></tr></thead>
          <tbody>
{trs}
          </tbody>
        </table>
        <h2>How we tested</h2>
        <p>One HEIC photo taken on iPhone with Location on, plus an IPTC copyright line added in {NAME}. We sent it through each route to a second device, saved the received file, and read its metadata with {NAME} and the <a href="../../exif-viewer/">browser EXIF viewer</a>. Tested on {esc(tested)}{(' with iOS ' + esc(', '.join(ios))) if ios else ''}. “Downloaded copy” means the file another person gets when they save your post.</p>
        <h2>What to do with this</h2>
        <p>Do not rely on the app: <a href="../../how-to/remove-location-from-photos-iphone/">remove location on iPhone</a> or <a href="../../remove-exif/">strip EXIF online</a> before sending. Per-app details: <a href="../which-apps-remove-photo-metadata/">which apps remove photo metadata</a>.</p>""",
        faqs=[
            ("Which apps keep the location of a photo?", f"In our test: {leak_list}."),
            ("Does sending as a file keep metadata?", "Usually yes: file or document routes deliver the original bytes, including GPS."),
            ("Will these results stay true?", "Not guaranteed. Apps change how they process uploads; re-check or clean the photo yourself first."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
        priority=True,
        updated=tested if len(tested) == 10 else None,
    )
