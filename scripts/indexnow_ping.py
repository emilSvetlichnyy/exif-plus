#!/usr/bin/env python3
"""Ping IndexNow for priority EXIF+ URLs."""
from __future__ import annotations

import json
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOST = "emilsvetlichnyy.github.io"
BASE = f"https://{HOST}/exif-plus"
KEY = (ROOT / "indexnow-key.txt").read_text().strip()

PRIORITY = [
    f"{BASE}/",
    f"{BASE}/remove-exif/",
    f"{BASE}/exif-viewer/",
    f"{BASE}/remove-gps/",
    f"{BASE}/heic-metadata/",
    f"{BASE}/learn/what-is-exif/",
    f"{BASE}/learn/exif-vs-iptc/",
    f"{BASE}/how-to/remove-location-from-photos-iphone/",
    f"{BASE}/how-to/share-photo-without-metadata/",
    f"{BASE}/app/free-vs-premium/",
    f"{BASE}/about/",
    f"{BASE}/tools/",
    f"{BASE}/sitemap.xml",
]


def main() -> None:
    key_url = f"{BASE}/{KEY}.txt"
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": key_url,
        "urlList": PRIORITY,
    }
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            print(f"IndexNow HTTP {resp.status} ({len(PRIORITY)} URLs)")
            if body:
                print(body[:500])
    except urllib.error.HTTPError as e:
        print(f"IndexNow HTTPError {e.code}: {e.read()[:500]}")
        raise SystemExit(1)
    except Exception as e:
        print(f"IndexNow failed: {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
