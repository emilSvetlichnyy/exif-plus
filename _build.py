#!/usr/bin/env python3
"""Build the EXIF+ SEO + GEO static site for GitHub Pages."""
from __future__ import annotations

import hashlib
import json
import secrets
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PK = json.loads((ROOT / "product-knowledge.json").read_text())
KG = json.loads((ROOT / "knowledge-graph.json").read_text())
BASE = PK["app"]["siteBase"].rstrip("/")
APP = PK["app"]["appStoreUrl"]
DEV = PK["app"]["developerUrl"]
PRIVACY = PK["app"]["privacyPolicyUrl"]
NAME = PK["app"]["displayName"]
DEV_NAME = PK["app"]["developerName"]
TODAY = date.today().isoformat()
PREFIX_PATH = "/exif-plus"

APPSTORE_SVG = (
    '<svg class="appstore__icon" viewBox="0 0 24 24" aria-hidden="true">'
    '<path fill="currentColor" d="M16.365 12.195c-.014-2.09 1.71-3.1 1.783-3.145-.972-1.422-2.48-1.616-3.012-1.64-1.28-.13-2.497.744-3.146.744-.648 0-1.65-.725-2.715-.705-1.396.02-2.69.813-3.41 2.06-1.458 2.53-.371 6.266 1.05 8.312.71 1.02 1.55 2.17 2.65 2.13 1.07-.04 1.47-.69 2.76-.69s1.65.69 2.78.67c1.15-.02 1.88-1.04 2.59-2.06.81-1.18 1.15-2.32 1.16-2.38-.025-.01-2.23-.855-2.49-2.296zM13.64 5.885c.57-.69.955-1.65.85-2.6-.82.03-1.81.545-2.4 1.235-.53.615-.996 1.596-.87 2.54.92.07 1.86-.47 2.42-1.175z"/></svg>'
)


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def jd(obj) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)


def prefix_for(rel: str) -> str:
    rel = rel.strip("/")
    if not rel:
        return "./"
    depth = len(Path(rel).parts)
    return "../" * depth


def appstore_btn() -> str:
    return (
        f'<a class="appstore" href="{APP}" target="_blank" rel="noopener noreferrer" '
        f'aria-label="Download {NAME} on the App Store">{APPSTORE_SVG}'
        '<span class="appstore__text"><span class="appstore__small">Download on the</span>'
        '<span class="appstore__big">App Store</span></span></a>'
    )


def nav_html(prefix: str, current: str | None = None) -> str:
    items = [
        ("Tools", f"{prefix}tools/", "Tools"),
        ("Learn", f"{prefix}learn/", "Learn"),
        ("How-to", f"{prefix}how-to/", "How-to"),
        ("Compare", f"{prefix}compare/", "Compare"),
        ("App", f"{prefix}app/", "App"),
    ]
    links = []
    for label, href, key in items:
        cur = ' aria-current="page"' if current == key else ""
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    return (
        '<nav class="nav-links" aria-label="Sections">\n'
        + "\n".join(f"        {l}" for l in links)
        + "\n      </nav>"
    )


def crumbs_html(items: list[tuple[str, str | None]]) -> str:
    parts = []
    for i, (name, href) in enumerate(items):
        if i:
            parts.append('<span class="crumb-sep" aria-hidden="true">›</span>')
        if href and i < len(items) - 1:
            parts.append(f'<a href="{href}">{esc(name)}</a>')
        else:
            parts.append(f'<span aria-current="page">{esc(name)}</span>')
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'


def breadcrumb_ld(items: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": url,
            }
            for i, (name, url) in enumerate(items)
        ],
    }


def faq_ld(pairs: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in pairs
        ],
    }


def org_ld() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": NAME,
        "alternateName": PK["app"]["alternateNames"],
        "url": f"{BASE}/",
        "logo": f"{BASE}/apple-touch-icon.png",
        "description": (
            "EXIF+ is a native iOS app to view, edit, and remove photo metadata "
            "(EXIF, IPTC, GPS), with free browser tools on this site."
        ),
        "sameAs": [APP, DEV],
        "founder": {"@type": "Person", "name": DEV_NAME, "url": DEV},
    }


def software_ld() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "EXIF+ Viewer, Metadata Remover",
        "alternateName": ["EXIF+", "Metadata Cleaner"],
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "iOS",
        "description": (
            "View, edit, and remove EXIF/IPTC metadata and GPS location from photos on iPhone. "
            "Processing uses on-device PhotoKit/ImageIO; cleaned photos are saved as new library items."
        ),
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "url": APP,
        "author": {"@type": "Person", "name": DEV_NAME, "url": DEV},
        "downloadUrl": APP,
    }


def howto_ld(name: str, steps: list[str]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": name,
        "step": [
            {"@type": "HowToStep", "position": i + 1, "text": s}
            for i, s in enumerate(steps)
        ],
    }


def article_ld(headline: str, description: str, url: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": headline,
        "description": description,
        "author": {"@type": "Person", "name": DEV_NAME, "url": DEV},
        "publisher": {
            "@type": "Organization",
            "name": NAME,
            "logo": {"@type": "ImageObject", "url": f"{BASE}/apple-touch-icon.png"},
        },
        "mainEntityOfPage": url,
        "dateModified": TODAY,
    }


def webapp_ld(name: str, description: str, url: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": name,
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "Any",
        "browserRequirements": "Requires JavaScript",
        "description": description,
        "url": url,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "isAccessibleForFree": True,
    }


def soft_cta(prefix: str) -> str:
    return f"""      <section class="section cta-band">
        <div class="section-head"><h2>Need this on iPhone?</h2></div>
        <p class="lead-sm">{NAME} views, edits, and removes EXIF/IPTC metadata — including GPS — on-device. Single-photo clean and edit are available to start; Premium unlocks multi-select batch tools and share-without-metadata. Cleaned photos are saved as new Photo Library items (originals stay).</p>
        <div class="actions">
          {appstore_btn()}
          <a class="btn btn-secondary" href="{prefix}app/free-vs-premium/">Free vs Premium</a>
        </div>
      </section>"""


def tool_panel(mode: str, title: str, blurb: str) -> str:
    download = ""
    if mode in ("remove", "gps"):
        download = '<button type="button" class="btn btn-primary tool-download" hidden>Download cleaned image</button>'
    return f"""      <section class="tool-panel" data-exif-tool data-mode="{mode}" aria-label="{esc(title)}">
        <h2 style="margin:0 0 6px;font-family:var(--display);font-size:1.35rem;">{esc(title)}</h2>
        <p class="lead-sm">{esc(blurb)} Files stay in this tab — nothing is uploaded to our servers.</p>
        <div class="dropzone" role="button" tabindex="0">
          <strong>Drop a photo here</strong>
          <span>or click to choose JPEG / PNG / WebP</span>
        </div>
        <input class="tool-file" type="file" accept="image/jpeg,image/png,image/webp,image/*" hidden>
        <div class="tool-output">
          <div class="preview-row">
            <img class="tool-preview" alt="">
            <div>
              <p class="tool-filename" style="margin:0 0 6px;font-weight:650;"></p>
              <p class="tool-status note" style="margin:0 0 12px;"></p>
              {download}
            </div>
          </div>
          <div class="meta-host"></div>
        </div>
      </section>"""


def faq_html(pairs: list[tuple[str, str]]) -> str:
    items = []
    for q, a in pairs:
        items.append(
            f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>"
        )
    return '<section class="section faq"><div class="section-head"><h2>FAQ</h2></div>' + "".join(items) + "</section>"


def footer_html(prefix: str) -> str:
    return f"""    <footer class="site-footer">
      <nav aria-label="Footer">
        <a href="{prefix}">Home</a>
        <a href="{prefix}tools/">Tools</a>
        <a href="{prefix}learn/">Learn</a>
        <a href="{prefix}how-to/">How-to</a>
        <a href="{prefix}compare/">Compare</a>
        <a href="{prefix}app/">App</a>
        <a href="{prefix}about/">About</a>
        <a href="{PRIVACY}" rel="noopener noreferrer">Privacy</a>
        <a href="{prefix}llms.txt">llms.txt</a>
      </nav>
      <p>© {date.today().year} {esc(DEV_NAME)}. {esc(NAME)} — view, edit, and remove photo metadata on iPhone.</p>
    </footer>"""


def page_shell(
    *,
    rel: str,
    title: str,
    description: str,
    canonical_path: str,
    body: str,
    schemas: list[dict],
    nav_current: str | None = None,
    og_image: str = "home.png",
    include_tool: bool = False,
) -> str:
    prefix = prefix_for(rel)
    css = f"{prefix}styles.css"
    canon = f"{BASE}/{canonical_path}".replace("//", "/").replace("https:/", "https://")
    if not canon.endswith("/") and canonical_path == "":
        canon = f"{BASE}/"
    elif canonical_path and not canon.endswith("/"):
        # keep file paths like llms as-is; pages use trailing slash
        if not canonical_path.endswith((".xml", ".txt", ".json", ".html", ".ico", ".png")):
            canon += "/"
    og = f"{BASE}/assets/og/{og_image}"
    schema_tags = "\n".join(
        f'  <script type="application/ld+json">\n{jd(s)}\n  </script>' for s in schemas
    )
    tool_tags = ""
    if include_tool:
        tool_tags = (
            '  <script src="https://cdn.jsdelivr.net/npm/exifr@7.1.3/dist/full.umd.js" defer></script>\n'
            f'  <script src="{prefix}tool.js" defer></script>\n'
        )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="canonical" href="{canon}">
  <meta name="theme-color" content="#3b6ea8">
  <link rel="icon" href="{PREFIX_PATH}/favicon.ico">
  <link rel="apple-touch-icon" href="{PREFIX_PATH}/apple-touch-icon.png">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-title" content="{esc(NAME)}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{esc(NAME)}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="{og}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(description)}">
  <meta name="twitter:image" content="{og}">
  <link rel="alternate" type="application/rss+xml" title="{esc(NAME)}" href="{BASE}/feed.xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Serif:wght@500;600&family=Source+Sans+3:wght@400;550;650;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css}">
{schema_tags}
{tool_tags}</head>
<body>
  <div class="wrap">
    <header class="site-nav">
      <a class="brand" href="{prefix}">EXIF+ <small>metadata</small></a>
      {nav_html(prefix, nav_current)}
    </header>
{body}
{footer_html(prefix)}
  </div>
</body>
</html>
"""


def write_page(rel: str, html: str) -> str:
    if rel in ("", "."):
        path = ROOT / "index.html"
        url = f"{BASE}/"
    else:
        path = ROOT / rel / "index.html"
        path.parent.mkdir(parents=True, exist_ok=True)
        url = f"{BASE}/{rel.strip('/')}/"
    path.write_text(html, encoding="utf-8")
    return url


# ---------- Page content ----------

PAGES: list[dict] = []


def register(page: dict) -> None:
    PAGES.append(page)


def build_home() -> None:
    prefix = "./"
    faqs = [
        (
            "What is EXIF+?",
            "EXIF+ is a native iPhone/iPad app to view, edit, and remove photo metadata — primarily EXIF, IPTC, and GPS — using on-device PhotoKit and ImageIO. This website also offers free browser tools that inspect/strip images locally in your tab (no upload to our servers).",
        ),
        (
            "Do browser tools upload my photos?",
            "No. The viewer and remover run entirely in your browser tab for the file you select. We do not need you to upload photos to use those tools.",
        ),
        (
            "Does removing EXIF reduce image quality?",
            "Metadata is not a visible filter, but saving a cleaned copy usually re-encodes the image. The browser tool exports via canvas; EXIF+ writes a new library item with ImageIO at high quality. Keep originals if you need an untouched master — see the “Does cleaning reduce quality?” guide.",
        ),
        (
            "Is the app free?",
            "Download is free. In the current UI you can view metadata and run single-photo edit/remove without Premium. Premium unlocks multi-select batch remove/edit and strip-on-share from the detail screen — see Free vs Premium.",
        ),
        (
            "Can I edit metadata, not only delete it?",
            "Yes in the iOS app — dates, GPS/location, camera fields, author, copyright, titles, descriptions, keywords, and more. Browser tools on this site focus on inspect and strip, not field editors.",
        ),
        (
            "Does EXIF+ overwrite my original photo?",
            "No. Clean and edit flows save a new Photo Library item (often named like Edited). Your original stays unless you delete it yourself.",
        ),
        (
            "Do you support video metadata?",
            "No. Library browsing is image-oriented and video metadata editing is not available in the shipping app.",
        ),
        (
            "Do you support HEIC?",
            "Yes in the iPhone app via the Photo Library; HEIC/HEIF can be preserved on save. Many browsers cannot decode HEIC for the online tools — use the app for Camera Roll HEIC.",
        ),
        (
            "Is XMP fully supported?",
            "This site does not claim first-class XMP read/write. The shipping app’s ImageIO path focuses on EXIF/IPTC/GPS (and related tags). See the EXIF vs IPTC guide for the honest matrix.",
        ),
        (
            "Are photos processed on-device?",
            "Photo view/edit/remove processing uses on-device frameworks. That is separate from optional product analytics/telemetry — we do not market “zero analytics.” See the privacy policy for policy detail.",
        ),
    ]
    body = f"""    <main>
      <section class="hero">
        <h1>View, edit, and remove photo metadata</h1>
        <p class="lead">Free browser EXIF viewer and remover — plus {NAME}, a native iPhone app for GPS cleanup, field edits, batch tools, and on-device Photo Library workflows.</p>
        <div class="actions">
          <a class="btn btn-primary" href="{prefix}remove-exif/">Remove EXIF online</a>
          <a class="btn btn-secondary" href="{prefix}exif-viewer/">View EXIF</a>
          {appstore_btn()}
        </div>
        <div class="chip-row">
          <a class="chip" href="{prefix}remove-gps/">Remove GPS</a>
          <a class="chip" href="{prefix}heic-metadata/">HEIC on iPhone</a>
          <a class="chip" href="{prefix}on-iphone/">On iPhone</a>
          <a class="chip" href="{prefix}app/free-vs-premium/">Free vs Premium</a>
          <a class="chip" href="{prefix}how-to/share-photo-without-metadata/">Share clean</a>
        </div>
      </section>

      <section class="section prose">
        <h2>What this site is for</h2>
        <p>People search for practical jobs: <em>remove EXIF</em>, <em>strip GPS</em>, <em>view photo metadata</em>, <em>clean HEIC on iPhone</em>. Each priority page pairs a clear answer with either a local browser tool or an honest iPhone workflow grounded in what {NAME} actually ships.</p>
      </section>

      <section class="section">
        <div class="section-head"><h2>Start with a tool</h2></div>
        <div class="grid-3">
          <a class="tile" href="{prefix}remove-exif/"><h3>Remove EXIF</h3><p>Strip metadata and download a clean copy in your browser.</p></a>
          <a class="tile" href="{prefix}exif-viewer/"><h3>EXIF viewer</h3><p>See camera, date, software, and GPS tags before you share.</p></a>
          <a class="tile" href="{prefix}remove-gps/"><h3>Remove GPS</h3><p>Focus on location data that can reveal where you were.</p></a>
        </div>
      </section>

      <section class="section">
        <div class="section-head"><h2>Learn the privacy basics</h2></div>
        <p class="lead-sm">Phones embed more than pixels: exact GPS, timestamps, camera model, and software tags. Some social apps strip fields on upload; email, “send as file,” marketplaces, and direct shares often keep them.</p>
        <div class="grid-2">
          <a class="tile" href="{prefix}learn/what-is-exif/"><h3>What is EXIF?</h3><p>Definition, common tags, and why people remove them.</p></a>
          <a class="tile" href="{prefix}learn/exif-vs-iptc/"><h3>EXIF vs IPTC</h3><p>What {NAME} actually reads and edits.</p></a>
          <a class="tile" href="{prefix}learn/does-instagram-remove-exif/"><h3>Does Instagram remove EXIF?</h3><p>Platform behavior vs cleaning yourself.</p></a>
          <a class="tile" href="{prefix}learn/does-cleaning-reduce-quality/"><h3>Quality tradeoffs</h3><p>Re-encode reality without hype.</p></a>
        </div>
      </section>

      <section class="section">
        <div class="section-head"><h2>iPhone app</h2></div>
        <p class="lead-sm">When you need albums, HEIC from Camera Roll, field-level edits, History, and Premium batch/share tools, use {NAME} on iOS 17+. Photo processing runs on-device; outputs are saved as new library items.</p>
        <div class="actions">
          {appstore_btn()}
          <a class="btn btn-secondary" href="{prefix}app/features/">See features</a>
          <a class="btn btn-secondary" href="{prefix}app/free-vs-premium/">Free vs Premium</a>
        </div>
      </section>

      {faq_html(faqs)}
    </main>"""
    schemas = [
        org_ld(),
        software_ld(),
        breadcrumb_ld([("Home", f"{BASE}/")]),
        faq_ld(faqs),
        {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": f"{NAME} — EXIF tools",
            "url": f"{BASE}/",
            "description": "Free EXIF viewer and remover tools plus the EXIF+ iPhone app.",
            "publisher": {"@type": "Organization", "name": NAME},
        },
    ]
    html = page_shell(
        rel="",
        title="EXIF Remover & Viewer Online + iPhone App — EXIF+",
        description="Free EXIF viewer and metadata remover in your browser. Strip GPS and photo metadata locally, or use EXIF+ on iPhone for batch edit and clean.",
        canonical_path="",
        body=body,
        schemas=schemas,
        og_image="home.png",
    )
    register({"rel": "", "html": html, "title": "Home", "priority": True})


def tool_page(
    slug: str,
    *,
    title: str,
    description: str,
    h1: str,
    lead: str,
    mode: str,
    tool_title: str,
    tool_blurb: str,
    sections_html: str,
    faqs: list[tuple[str, str]],
    crumbs: list[tuple[str, str]],
    og: str,
) -> None:
    prefix = prefix_for(slug)
    crumb_ui = [(c[0], prefix + c[1] if c[1] else None) for c in [
        ("Home", ""),
        *[(n, None if u.endswith(slug) else u) for n, u in [(x[0], x[1].replace(f"{BASE}/", "")) for x in crumbs[1:]]],
    ]]
    # simpler crumbs
    crumb_pairs = [("Home", prefix)]
    for name, url in crumbs[1:-1]:
        path = url.replace(f"{BASE}/", "")
        crumb_pairs.append((name, prefix + path if not path.startswith("..") else path))
    crumb_pairs.append((crumbs[-1][0], None))

    body = f"""    {crumbs_html(crumb_pairs)}
    <main>
      <section class="hero">
        <h1>{esc(h1)}</h1>
        <p class="lead">{esc(lead)}</p>
        <div class="actions">
          {appstore_btn()}
          <a class="btn btn-secondary" href="{prefix}app/">iPhone app</a>
        </div>
      </section>
{tool_panel(mode, tool_title, tool_blurb)}
{sections_html}
      {faq_html(faqs)}
      {soft_cta(prefix)}
    </main>"""
    schemas = [
        org_ld(),
        breadcrumb_ld(crumbs),
        faq_ld(faqs),
        webapp_ld(tool_title, description, f"{BASE}/{slug}/"),
        howto_ld(
            tool_title,
            [
                "Choose a photo on your device.",
                "Review detected metadata tags in the browser.",
                "Download a cleaned copy if you used remove mode, or open EXIF+ on iPhone for edits and batch work.",
            ],
        ),
    ]
    html = page_shell(
        rel=slug,
        title=title,
        description=description,
        canonical_path=f"{slug}/",
        body=body,
        schemas=schemas,
        nav_current="Tools",
        og_image=og,
        include_tool=True,
    )
    register({"rel": slug, "html": html, "title": h1, "priority": True})


def build_tool_pages() -> None:
    tool_page(
        "remove-exif",
        title="Remove EXIF Online Free — Strip Photo Metadata | EXIF+",
        description="Remove EXIF and other photo metadata in your browser. No upload to our servers. Download a clean copy, or use EXIF+ on iPhone for batch cleaning.",
        h1="Remove EXIF online",
        lead="Strip hidden photo metadata before you share. Processing stays in your browser; for albums and batch jobs, use EXIF+ on iPhone.",
        mode="remove",
        tool_title="EXIF remover",
        tool_blurb="Drop a photo to inspect tags, then download a re-encoded copy without EXIF/GPS.",
        sections_html="""      <section class="section prose">
        <h2>What gets removed</h2>
        <p>Typical smartphone JPEGs can include GPS coordinates, capture time, camera make/model, lens info, software tags, and descriptive IPTC fields. The browser tool creates a new image file without those metadata blocks by re-encoding in your tab.</p>
        <h2>When to use the iPhone app instead</h2>
        <ul>
          <li>Clean many photos from albums in one pass (Premium multi-select)</li>
          <li>Edit fields instead of deleting everything</li>
          <li>Keep History before/after</li>
          <li>Work with HEIC items in the Photo Library</li>
          <li>Share a stripped temporary file (Premium)</li>
        </ul>
        <h2>Honest limits</h2>
        <p>This page does not claim video support, original overwrite, or lossless pixel identity. For Camera Roll HEIC, prefer the <a href="../heic-metadata/">HEIC guide</a>.</p>
      </section>""",
        faqs=[
            (
                "Is this EXIF remover free?",
                "Yes. The browser tool is free with no account. The iOS app download is also free; Premium is only required for multi-select batch and strip-on-share in the current UI.",
            ),
            (
                "Do you store my photos?",
                "Browser processing is local to your tab — files are not uploaded to our servers for this tool. The iOS app processes with on-device PhotoKit/ImageIO.",
            ),
            (
                "Does HEIC work in the browser?",
                "Often no — many browsers cannot decode HEIC for canvas export. Use EXIF+ on iPhone for Camera Roll HEIC, or convert to JPEG first.",
            ),
            (
                "Will quality change?",
                "The download is a re-encoded copy (canvas export). For library workflows, EXIF+ also writes a new file via ImageIO at high quality rather than promising bit-identical lossless output.",
            ),
            (
                "Does remove EXIF also remove GPS?",
                "Yes — a full strip removes location tags along with other metadata blocks the exporter drops.",
            ),
            (
                "Should I use the app instead?",
                "Use the app for albums, HEIC, field-level edits, History, and Premium batch/share. Use the browser for a quick single JPEG/PNG/WebP.",
            ),
        ],
        crumbs=[
            ("Home", f"{BASE}/"),
            ("Remove EXIF", f"{BASE}/remove-exif/"),
        ],
        og="remove-exif.png",
    )

    tool_page(
        "exif-viewer",
        title="EXIF Viewer Online Free — See Photo Metadata | EXIF+",
        description="Free online EXIF viewer. Inspect camera settings, dates, software tags, and GPS location in your browser — no upload to our servers.",
        h1="EXIF viewer online",
        lead="See what your photo is really carrying — camera, timestamps, software, and GPS — before you post or send it.",
        mode="view",
        tool_title="EXIF viewer",
        tool_blurb="Choose a photo to list readable EXIF/IPTC/GPS fields locally.",
        sections_html="""      <section class="section prose">
        <h2>What you can check</h2>
        <p>Common fields include date taken, camera make/model, lens, ISO, aperture, shutter, software, copyright, and GPS latitude/longitude when present.</p>
        <h2>Next step after viewing</h2>
        <p>If you see location data you do not want to share, use the <a href="../remove-gps/">GPS remover</a> or <a href="../remove-exif/">full EXIF remover</a>. On iPhone, open EXIF+ to edit individual fields or batch-clean albums.</p>
      </section>""",
        faqs=[
            (
                "Why don’t I see GPS?",
                "Location services may have been off at capture, tags were already stripped, or another app re-exported the file without GPS.",
            ),
            (
                "Is viewing EXIF safe?",
                "The file is read locally in your browser for display. It is not uploaded to our servers for this tool.",
            ),
            (
                "Why are some fields missing compared with desktop apps?",
                "Parsers differ. This viewer shows common EXIF/IPTC/GPS fields returned in-browser. For fuller Photo Library inspection on iPhone, use EXIF+.",
            ),
            (
                "Can I edit from the viewer?",
                "Not in the browser tool. Use EXIF+ on iPhone for field editors, or switch to the remover if you want a clean download.",
            ),
            (
                "Does the viewer work offline?",
                "After the page and script assets load, inspection runs locally on the file you pick. A network drop mid-session may still affect CDN script load on first visit.",
            ),
        ],
        crumbs=[
            ("Home", f"{BASE}/"),
            ("EXIF viewer", f"{BASE}/exif-viewer/"),
        ],
        og="exif-viewer.png",
    )

    tool_page(
        "remove-gps",
        title="Remove GPS from Photos Online — Strip Location Data | EXIF+",
        description="Remove GPS location from photos in your browser. Strip geotags before sharing. For batch cleanup on iPhone, use EXIF+.",
        h1="Remove GPS from photos",
        lead="Geotags can reveal your home, hotel, or workplace. Strip location data locally, then share the cleaned file.",
        mode="gps",
        tool_title="GPS / location remover",
        tool_blurb="We’ll highlight GPS if present, then you can download a copy without metadata.",
        sections_html="""      <section class="section prose">
        <h2>Why GPS metadata is sensitive</h2>
        <p>Coordinates are often accurate to roughly building-level precision. A single shared original can leak where you live or travel — even when the visible picture looks harmless.</p>
        <h2>Platforms that may keep GPS</h2>
        <p>Many social networks strip location on upload. Email attachments, messaging “as file”, cloud links, and marketplace listings frequently preserve it. Do not rely on the destination app.</p>
      </section>""",
        faqs=[
            (
                "Does removing GPS blur the photo?",
                "No. Location is metadata. We export a new file without those tags; the visible scene is not intentionally blurred or censored.",
            ),
            (
                "Can I remove only GPS but keep camera EXIF?",
                "The browser download path strips broadly via re-encode. For selective location clear while keeping other fields, use EXIF+’s editor on iPhone.",
            ),
            (
                "Is GPS the same as the Photos “Location” album label?",
                "Related but not identical. Embedded coordinates are file metadata; Moments/Maps features also use library location databases.",
            ),
            (
                "Will AirDrop keep GPS?",
                "If you send an original with tags, recipients can still read them. Clean first when privacy matters.",
            ),
            (
                "What about screenshots?",
                "Many screenshots lack camera GPS. Always inspect if the source was a camera original or a re-export.",
            ),
        ],
        crumbs=[
            ("Home", f"{BASE}/"),
            ("Remove GPS", f"{BASE}/remove-gps/"),
        ],
        og="remove-gps.png",
    )

    tool_page(
        "metadata-cleaner",
        title="Metadata Cleaner Online — Clean Photo EXIF | EXIF+",
        description="Online metadata cleaner for photos. Remove EXIF, IPTC, and GPS locally in your browser, or clean batches with EXIF+ on iPhone.",
        h1="Metadata cleaner",
        lead="One place to inspect and clean photo metadata before sharing — browser quick clean or iPhone batch tools.",
        mode="remove",
        tool_title="Metadata cleaner",
        tool_blurb="Inspect tags, then download a cleaned image copy.",
        sections_html="""      <section class="section prose">
        <h2>Cleaner vs editor</h2>
        <p>A cleaner removes hidden fields. An editor changes them (new date, new copyright, corrected GPS). This page is a cleaner; the iOS app does both.</p>
        <div class="grid-2">
          <a class="tile" href="../compare/remove-vs-edit-exif/"><h3>Remove vs edit</h3><p>Which workflow fits privacy vs organization.</p></a>
          <a class="tile" href="../batch-remove/"><h3>Batch remove</h3><p>How album cleaning works on iPhone.</p></a>
        </div>
      </section>""",
        faqs=[
            (
                "What metadata standards are involved?",
                "Photos often mix EXIF (camera/GPS) and IPTC (caption/copyright). Some desktop tools also use XMP; this site does not claim full XMP support in EXIF+.",
            ),
            (
                "Cleaner vs EXIF+ Premium batch?",
                "This page’s browser tool is single-file. Album multi-select batch cleaning is an EXIF+ Premium iPhone feature.",
            ),
            (
                "Does cleaning overwrite files on disk?",
                "The browser downloads a new file. The iOS app saves a new Photo Library item and leaves the original in place.",
            ),
        ],
        crumbs=[
            ("Home", f"{BASE}/"),
            ("Metadata cleaner", f"{BASE}/metadata-cleaner/"),
        ],
        og="metadata-cleaner.png",
    )

    # edit-exif / batch / on-iphone are content+CTA pages (edit is app-focused)
    for slug, title, description, h1, lead, prose, faqs, og, tool in [
        (
            "edit-exif",
            "Edit EXIF Data on iPhone — Change Photo Metadata | EXIF+",
            "Edit EXIF metadata on iPhone: dates, GPS, camera fields, author, and copyright with EXIF+. On-device processing; batch edit is Premium.",
            "Edit EXIF on iPhone",
            "Change the fields you care about — or clear them — without a desktop catalog app.",
            f"""      <section class="section prose">
        <h2>Fields you can change in {NAME}</h2>
        <ul>
          <li>Date Taken / Date Created</li>
          <li>Location name, latitude, longitude, altitude (+ map picker)</li>
          <li>Camera make/model, lens, software</li>
          <li>ISO, shutter, aperture, focal length, exposure, flash, white balance</li>
          <li>Author, copyright, title, description, comment, keywords</li>
        </ul>
        <p>Edits are written with on-device ImageIO. Results are saved as <strong>new</strong> Photo Library items so originals stay unless you delete them. Some viewer fields are informational/read-only (dimensions, file size, serials, etc.).</p>
        <h2>Batch edit</h2>
        <p>Multi-select batch edit is <strong>Premium</strong>. Empty fields mean “leave unchanged” for that batch apply.</p>
        <h2>Browser note</h2>
        <p>This website’s live tools focus on view + remove. Field-level editing is in the iOS app.</p>
      </section>""",
            [
                (
                    "Will editing EXIF change the picture?",
                    "Metadata edits change tags, not the scene. Saving still re-encodes into a new library item — high quality, not a lossless promise.",
                ),
                (
                    "Is single edit free?",
                    "Yes in the current UI. Premium is for multi-select batch and strip-on-share.",
                ),
                (
                    "Can I edit GPS only?",
                    "Yes — see the Edit GPS how-to. Clearing location is also available in batch edit.",
                ),
            ],
            "edit-exif.png",
            False,
        ),
        (
            "batch-remove",
            "Batch Remove EXIF from Photos on iPhone | EXIF+",
            "Batch remove EXIF and GPS from multiple photos on iPhone with EXIF+ Premium. Clean albums faster before sharing.",
            "Batch remove photo metadata",
            "Multi-select photos, strip metadata in one flow, and keep working from your albums — Premium when more than one photo is selected.",
            f"""      <section class="section prose">
        <h2>How batch clean works in {NAME}</h2>
        <ol>
          <li>Open an album and multi-select photos.</li>
          <li>If you are not Premium, the app presents the paywall for batch actions.</li>
          <li>Choose batch remove metadata (or batch edit fields).</li>
          <li>Each success is saved as a <strong>new</strong> Photo Library item.</li>
        </ol>
        <p>Single-photo remove remains available without Premium. Video metadata editing is not available. See <a href="../app/free-vs-premium/">Free vs Premium</a>.</p>
      </section>""",
            [
                (
                    "Can I batch-clean in the browser?",
                    "The web tools are single-file for simplicity. Use the iPhone app for album multi-select.",
                ),
                (
                    "Is batch remove free?",
                    "No. Multi-select batch remove/edit requires Premium in the current UI.",
                ),
                (
                    "Does batch delete originals?",
                    "No. Outputs are new items; originals stay unless you delete them.",
                ),
            ],
            "batch-remove.png",
            False,
        ),
        (
            "on-iphone",
            "Remove EXIF on iPhone — Metadata Cleaner App | EXIF+",
            "Remove EXIF and GPS on iPhone with EXIF+. View full metadata, edit fields, and batch-clean photos on-device.",
            "EXIF tools on iPhone",
            "Built for Photo Library workflows: view every tag, edit what you need, remove what you don’t — on-device.",
            f"""      <section class="section prose">
        <h2>Why a native app</h2>
        <p>Browser tools are great for a quick single file. iPhone albums, HEIC library items, batch selection, and history need a native Photos-integrated app.</p>
        <div class="grid-2">
          <a class="tile" href="../how-to/view-exif-on-iphone/"><h3>View EXIF on iPhone</h3><p>Step-by-step.</p></a>
          <a class="tile" href="../how-to/remove-location-from-photos-iphone/"><h3>Remove location</h3><p>Strip GPS before sharing.</p></a>
        </div>
      </section>""",
            [
                (
                    "What iOS version is required?",
                    "iOS 17.0 or later.",
                ),
            ],
            "on-iphone.png",
            False,
        ),
    ]:
        prefix = prefix_for(slug)
        body = f"""    {crumbs_html([("Home", prefix), (h1, None)])}
    <main>
      <section class="hero">
        <h1>{esc(h1)}</h1>
        <p class="lead">{esc(lead)}</p>
        <div class="actions">
          {appstore_btn()}
          <a class="btn btn-secondary" href="{prefix}remove-exif/">Browser remover</a>
        </div>
      </section>
{prose}
      {faq_html(faqs)}
      {soft_cta(prefix)}
    </main>"""
        schemas = [
            org_ld(),
            software_ld(),
            breadcrumb_ld([("Home", f"{BASE}/"), (h1, f"{BASE}/{slug}/")]),
            faq_ld(faqs),
            article_ld(h1, description, f"{BASE}/{slug}/"),
        ]
        html = page_shell(
            rel=slug,
            title=title,
            description=description,
            canonical_path=f"{slug}/",
            body=body,
            schemas=schemas,
            nav_current="App" if slug == "on-iphone" else "Tools",
            og_image=og,
            include_tool=tool,
        )
        register({"rel": slug, "html": html, "title": h1, "priority": True})


def hub_page(slug: str, title: str, description: str, h1: str, lead: str, tiles: list[tuple[str, str, str]], nav: str) -> None:
    prefix = prefix_for(slug)
    # Tile hrefs are relative to the hub page itself (do not prepend prefix again).
    tiles_html = "".join(
        f'<a class="tile" href="{href}"><h3>{esc(n)}</h3><p>{esc(d)}</p></a>'
        for n, href, d in tiles
    )
    body = f"""    {crumbs_html([("Home", prefix), (h1, None)])}
    <main>
      <section class="hero">
        <h1>{esc(h1)}</h1>
        <p class="lead">{esc(lead)}</p>
      </section>
      <section class="section">
        <div class="grid-2">{tiles_html}</div>
      </section>
      {soft_cta(prefix)}
    </main>"""
    html = page_shell(
        rel=slug,
        title=title,
        description=description,
        canonical_path=f"{slug}/",
        body=body,
        schemas=[
            org_ld(),
            breadcrumb_ld([("Home", f"{BASE}/"), (h1, f"{BASE}/{slug}/")]),
        ],
        nav_current=nav,
        og_image="home.png",
    )
    register({"rel": slug, "html": html, "title": h1, "priority": True})


def article_page(
    slug: str,
    *,
    title: str,
    description: str,
    h1: str,
    lead: str,
    prose: str,
    faqs: list[tuple[str, str]],
    nav: str,
    parent: tuple[str, str],
    og: str = "home.png",
    priority: bool = False,
) -> None:
    prefix = prefix_for(slug)
    parent_href = prefix + parent[1]
    body = f"""    {crumbs_html([("Home", prefix + ("../" * (len(Path(slug).parts) - 1) if "/" in slug else "")), (parent[0], parent_href), (h1, None)])}
    <main>
      <article class="prose">
        <section class="hero">
          <h1>{esc(h1)}</h1>
          <p class="lead">{esc(lead)}</p>
        </section>
{prose}
      </article>
      {faq_html(faqs)}
      {soft_cta(prefix)}
    </main>"""
    # Breadcrumbs: Home → optional parent hub → page
    parts = slug.strip("/").split("/")
    crumb_ui = [("Home", prefix_for(slug))]
    if parent:
        parent_rel = parent[1].strip("/")
        crumb_ui.append((parent[0], prefix_for(slug) + parent_rel + "/"))
    crumb_ui.append((h1, None))
    body = f"""    {crumbs_html(crumb_ui)}
    <main>
      <article class="prose">
        <section class="hero">
          <h1>{esc(h1)}</h1>
          <p class="lead">{esc(lead)}</p>
        </section>
{prose}
      </article>
      {faq_html(faqs)}
      {soft_cta(prefix)}
    </main>"""
    crumbs_ld = [("Home", f"{BASE}/")]
    if parent:
        crumbs_ld.append((parent[0], f"{BASE}/{parent[1].strip('/')}/"))
    crumbs_ld.append((h1, f"{BASE}/{slug}/"))
    html = page_shell(
        rel=slug,
        title=title,
        description=description,
        canonical_path=f"{slug}/",
        body=body,
        schemas=[
            org_ld(),
            breadcrumb_ld(crumbs_ld),
            article_ld(h1, description, f"{BASE}/{slug}/"),
            faq_ld(faqs),
        ],
        nav_current=nav,
        og_image=og,
    )
    register({"rel": slug, "html": html, "title": h1, "priority": priority})


def build_hubs_and_articles() -> None:
    hub_page(
        "tools",
        "EXIF Tools — Viewer, Remover, GPS Cleaner | EXIF+",
        "Free browser EXIF tools: viewer, metadata remover, and GPS cleaner. Local processing, plus the EXIF+ iPhone app.",
        "Tools",
        "Quick local tools in the browser. Use the iPhone app when you need albums, batch, and field editors.",
        [
            ("Remove EXIF", "../remove-exif/", "Strip metadata and download a clean copy."),
            ("EXIF viewer", "../exif-viewer/", "Inspect tags before you share."),
            ("Remove GPS", "../remove-gps/", "Focus on location data."),
            ("Metadata cleaner", "../metadata-cleaner/", "All-in-one clean intent page."),
            ("HEIC metadata", "../heic-metadata/", "Camera Roll HEIC via the iPhone app."),
            ("Remove camera data", "../remove-camera-data/", "Make/model and device tags."),
            ("Batch remove", "../batch-remove/", "Album multi-select on iPhone (Premium)."),
            ("Edit EXIF", "../edit-exif/", "Change fields in the iOS app."),
        ],
        "Tools",
    )
    hub_page(
        "learn",
        "Learn Photo Metadata — EXIF, GPS, Privacy | EXIF+",
        "Learn what EXIF and GPS metadata are, when platforms strip them, and how to share photos more privately.",
        "Learn",
        "Short explainers written so humans and AI systems can cite clear definitions.",
        [
            ("What is EXIF?", "what-is-exif/", "Definition and common tags."),
            ("What is GPS metadata?", "what-is-gps-metadata/", "Why geotags matter."),
            ("EXIF vs IPTC", "exif-vs-iptc/", "What the app actually implements."),
            ("Does Instagram remove EXIF?", "does-instagram-remove-exif/", "Platform behavior."),
            ("Does cleaning reduce quality?", "does-cleaning-reduce-quality/", "Re-encode tradeoffs."),
            ("Why a duplicate appears", "why-cleaned-photo-is-a-duplicate/", "Save-as-new explained."),
            ("Glossary", "glossary/", "EXIF, IPTC, geotag, cleaner, HEIC."),
        ],
        "Learn",
    )
    hub_page(
        "how-to",
        "How to Remove EXIF & GPS on iPhone | EXIF+",
        "Step-by-step guides to view EXIF, edit GPS/dates, share without metadata, and batch-clean on iPhone.",
        "How-to",
        "Practical iPhone workflows for privacy before sharing — matched to shipping EXIF+ features.",
        [
            ("Remove location on iPhone", "remove-location-from-photos-iphone/", "Strip GPS before you send."),
            ("Edit GPS on iPhone", "edit-gps-on-iphone/", "Map picker and coordinates."),
            ("Change photo date", "change-photo-date-iphone/", "Fix Date Taken / Created."),
            ("Share without metadata", "share-photo-without-metadata/", "Library clean vs Premium share."),
            ("Batch copyright/author", "batch-edit-copyright/", "Premium batch edit."),
            ("View EXIF on iPhone", "view-exif-on-iphone/", "See hidden tags in EXIF+."),
            ("Strip metadata checklist", "strip-metadata-before-sharing/", "Pre-share checklist."),
        ],
        "How-to",
    )
    hub_page(
        "compare",
        "Compare EXIF Workflows — Remove vs Edit, Web vs App | EXIF+",
        "Compare removing vs editing EXIF, and browser tools vs the EXIF+ iPhone app.",
        "Compare",
        "Pick the right workflow for privacy vs organization.",
        [
            ("Remove vs edit EXIF", "remove-vs-edit-exif/", "Delete everything or change fields."),
            ("Online vs iPhone app", "online-vs-iphone-app/", "When each option wins."),
        ],
        "Compare",
    )
    hub_page(
        "app",
        "EXIF+ iPhone App — View, Edit, Remove Metadata",
        "EXIF+ is a native iOS app to view, edit, and remove EXIF/IPTC metadata and GPS on-device.",
        "EXIF+ app",
        "Native Photo Library tools for people who share photos and care about hidden data.",
        [
            ("Features", "features/", "Viewer, editor, batch, history."),
            ("Free vs Premium", "free-vs-premium/", "What is actually gated."),
            ("History", "history/", "Before/after comparisons."),
            ("Privacy", "privacy/", "On-device processing notes."),
            ("On iPhone overview", "../on-iphone/", "Why native matters."),
        ],
        "App",
    )

    article_page(
        "learn/what-is-exif",
        title="What Is EXIF Data? Photo Metadata Explained | EXIF+",
        description="EXIF is metadata embedded in photos: camera settings, timestamps, software tags, and often GPS. Learn what it is and why it matters for privacy.",
        h1="What is EXIF?",
        lead="EXIF (Exchangeable Image File Format) is a common way cameras and phones store technical details inside image files.",
        prose="""        <h2>What EXIF usually contains</h2>
        <p>Typical fields include capture time, camera make and model, lens, exposure settings (ISO, shutter, aperture), orientation, software names, and — if location was enabled — GPS coordinates. Viewers may also show related IPTC labels such as author or copyright when present.</p>
        <h2>EXIF vs IPTC (and why we mention XMP carefully)</h2>
        <p>EXIF is strongest for camera/GPS technical tags. IPTC is often used for captions, keywords, and copyright. XMP appears in many desktop editing workflows, but EXIF+’s shipping implementation is documented on the <a href="../exif-vs-iptc/">EXIF vs IPTC</a> page as EXIF/IPTC/GPS-focused — not full XMP parity.</p>
        <h2>Why people remove it</h2>
        <p>Sharing an original file can unintentionally publish where you were and which device took the shot. Removing metadata keeps the picture while dropping the hidden context. Remember that creating a cleaned file usually re-encodes pixels — see <a href="../does-cleaning-reduce-quality/">quality notes</a>.</p>
        <h2>How to inspect a file right now</h2>
        <p>Use the <a href="../../exif-viewer/">browser EXIF viewer</a> for JPEG/PNG/WebP, or open the photo in EXIF+ on iPhone for Camera Roll / HEIC library items.</p>
        <p>Related: <a href="../what-is-gps-metadata/">GPS metadata</a>, <a href="../../remove-exif/">remove EXIF online</a>.</p>""",
        faqs=[
            (
                "Is EXIF part of the photo pixels?",
                "No. It is metadata attached to the file. Removing it does not crop or stylize the image by itself, though saving a cleaned copy usually re-encodes the file.",
            ),
            (
                "Do all apps keep EXIF?",
                "No. Some social networks strip fields on upload; email, messaging as files, cloud links, and marketplaces often keep them.",
            ),
            (
                "What is the difference between EXIF and GPS metadata?",
                "GPS/location tags are often stored inside or alongside the EXIF structure. People say “remove GPS” when they mainly care about coordinates, and “remove EXIF” when they want a broader wipe.",
            ),
            (
                "Can iPhone Photos show full EXIF?",
                "Photos shows limited information. EXIF+ surfaces fuller field groups for privacy and editing decisions.",
            ),
            (
                "Does removing EXIF make a photo anonymous?",
                "It removes embedded tags from that file. It does not remove faces, landmarks, or anything visible in the pixels.",
            ),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
        priority=True,
    )

    article_page(
        "learn/what-is-gps-metadata",
        title="What Is GPS Metadata in Photos? | EXIF+",
        description="GPS metadata (geotags) stores where a photo was taken. Learn the privacy risk and how to remove location data.",
        h1="What is GPS metadata?",
        lead="GPS metadata records the location where a photo was captured — often as latitude, longitude, and sometimes altitude.",
        prose="""        <h2>How geotags get into photos</h2>
        <p>When location services are on, phones write coordinates into the image file. Screenshots and some exported images may not include GPS; camera originals often do.</p>
        <h2>Privacy risk</h2>
        <p>A single geotagged photo can reveal home addresses, schools, hotels, or workplaces. That risk is why “remove location from photo” is one of the most common metadata tasks.</p>
        <p>Try the <a href="../../remove-gps/">GPS remover</a> or the iPhone guide to <a href="../../how-to/remove-location-from-photos-iphone/">strip location</a>.</p>""",
        faqs=[
            (
                "Does turning off location for Camera stop old geotags?",
                "It stops new ones. Old photos may still contain GPS until you remove metadata.",
            ),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    article_page(
        "learn/does-instagram-remove-exif",
        title="Does Instagram Remove EXIF Data? | EXIF+",
        description="Instagram typically strips most EXIF/GPS on upload, but email, Telegram files, and many other channels keep metadata. Clean photos before you share elsewhere.",
        h1="Does Instagram remove EXIF?",
        lead="Major social networks often strip camera and GPS metadata on upload — but that is not a universal privacy guarantee.",
        prose="""        <h2>Short answer</h2>
        <p>Instagram and similar feed apps generally do not publish full original EXIF to viewers. That still leaves gaps: other apps, email, messaging “as file”, cloud links, and downloads of your original can preserve everything.</p>
        <h2>What to do instead</h2>
        <p>Treat destination stripping as a bonus, not a control. Clean the file first with a <a href="../../metadata-cleaner/">metadata cleaner</a> or <a href="../../on-iphone/">EXIF+ on iPhone</a>, then share.</p>""",
        faqs=[
            (
                "If Instagram strips EXIF, why bother cleaning?",
                "Because you will not only share on Instagram — and even there, your local original still has the data until you clean it.",
            ),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    article_page(
        "learn/glossary",
        title="Photo Metadata Glossary — EXIF, IPTC, Geotag, HEIC | EXIF+",
        description="Glossary of photo metadata terms: EXIF, IPTC, geotag, metadata cleaner, HEIC, and related privacy terms.",
        h1="Metadata glossary",
        lead="Quick definitions you can cite when explaining photo metadata — aligned with what this site claims.",
        prose="""        <h2>EXIF</h2>
        <p>Camera-oriented metadata standard commonly storing capture settings, timestamps, and GPS.</p>
        <h2>IPTC</h2>
        <p>Descriptive metadata often used for captions, keywords, author, and copyright.</p>
        <h2>XMP</h2>
        <p>Extensible metadata format used by many desktop editors. Mentioned for literacy; EXIF+ pages do not claim full XMP read/write in the shipping iOS app.</p>
        <h2>Geotag / GPS metadata</h2>
        <p>Location coordinates embedded in a media file.</p>
        <h2>Metadata cleaner</h2>
        <p>A tool that removes hidden fields before sharing while keeping the visible image (usually by writing a new file).</p>
        <h2>HEIC / HEIF</h2>
        <p>Common iPhone capture format. Best handled in EXIF+ via the Photo Library; many browsers cannot decode it for web tools.</p>
        <h2>Save as new item</h2>
        <p>EXIF+ writes cleaned/edited outputs as new Photo Library assets instead of overwriting the original.</p>""",
        faqs=[
            (
                "Are these formats mutually exclusive?",
                "No. A single JPEG can contain multiple metadata blocks. What any one app reads/writes still depends on its implementation.",
            ),
            (
                "What should I cite for EXIF+ capabilities?",
                "Prefer EXIF, IPTC, and GPS view/edit/remove on-device; Premium batch and strip-on-share; save-as-new library items.",
            ),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    article_page(
        "how-to/remove-location-from-photos-iphone",
        title="How to Remove Location from Photos on iPhone | EXIF+",
        description="Step-by-step: remove GPS location from photos on iPhone with EXIF+. Strip geotags before sharing.",
        h1="Remove location from photos on iPhone",
        lead="Use EXIF+ to find GPS tags and save cleaned copies without location data.",
        prose=f"""        <h2>Steps</h2>
        <ol>
          <li>Install {NAME} from the App Store.</li>
          <li>Allow Photo Library access.</li>
          <li>Open a photo and check the Location / GPS section.</li>
          <li>Remove metadata (or clear location fields) and save the cleaned copy.</li>
          <li>Share the new item — not the uncleaned original.</li>
        </ol>
        <p>For a one-off file on a computer, use the <a href="../../remove-gps/">browser GPS remover</a>.</p>""",
        faqs=[
            (
                "Does iOS Photos remove GPS when I share?",
                "Some share routes offer location controls, but behavior varies by app and send mode. Cleaning the file yourself is more predictable.",
            ),
            (
                "Is remove location the same as remove all metadata?",
                "No. You can clear location fields in the editor, or remove all metadata for a broader wipe including camera tags and timestamps.",
            ),
            (
                "Will the original keep GPS?",
                "Yes — EXIF+ saves a new item. The original library asset still has its old tags until you delete or edit it separately.",
            ),
            (
                "Can I do this for many photos?",
                "Yes with Premium multi-select batch remove, or batch edit with remove-location.",
            ),
            (
                "Does this work for HEIC?",
                "Yes in the iPhone app via the Photo Library. Browser GPS tools may not decode HEIC.",
            ),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
        priority=True,
    )

    article_page(
        "how-to/view-exif-on-iphone",
        title="How to View EXIF Data on iPhone | EXIF+",
        description="View EXIF metadata on iPhone with EXIF+: camera settings, dates, GPS, and more from your Photo Library.",
        h1="View EXIF on iPhone",
        lead="See the hidden fields attached to any photo in your library.",
        prose=f"""        <h2>Steps</h2>
        <ol>
          <li>Open {NAME}.</li>
          <li>Pick a photo from an album.</li>
          <li>Scroll metadata sections: date, location, camera, technical, author, GPS details.</li>
        </ol>
        <p>Need a desktop quick look? Use the <a href="../../exif-viewer/">online EXIF viewer</a>.</p>""",
        faqs=[
            (
                "Can the built-in Photos app show full EXIF?",
                "Photos shows limited info. EXIF+ surfaces a fuller field set for privacy and editing decisions.",
            ),
            (
                "Which sections should I check first?",
                "Location/GPS for privacy, then Date & Time, Camera, and Author/Copyright if you care about ownership labels.",
            ),
            (
                "Can I copy values?",
                "The viewer is built for inspection workflows with copy-friendly rows in the app UI.",
            ),
            (
                "Does viewing require Premium?",
                "No.",
            ),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
    )

    article_page(
        "how-to/strip-metadata-before-sharing",
        title="How to Strip Photo Metadata Before Sharing | EXIF+",
        description="A simple checklist to strip EXIF and GPS before sharing photos by message, email, or upload.",
        h1="Strip metadata before sharing",
        lead="A short pre-share checklist so originals with GPS do not leak by habit.",
        prose="""        <h2>Checklist</h2>
        <ol>
          <li>Decide whether you need any metadata (copyright) or want a fully clean file.</li>
          <li>Inspect the photo in an EXIF viewer.</li>
          <li>Remove GPS at minimum; remove all metadata when sharing publicly.</li>
          <li>Share the cleaned copy. Keep originals in a private album if you still need them.</li>
        </ol>""",
        faqs=[
            (
                "Should I delete the original?",
                "Not required. Keep originals privately if you want history; just do not attach them when sharing.",
            ),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
    )

    article_page(
        "compare/remove-vs-edit-exif",
        title="Remove EXIF vs Edit EXIF — Which Should You Use? | EXIF+",
        description="Compare removing all photo metadata vs editing specific EXIF fields. Privacy cleanup vs organizing dates and copyright.",
        h1="Remove vs edit EXIF",
        lead="Removal is for privacy. Editing is for correcting or labeling fields you still want to keep.",
        prose="""        <table class="compare-table">
          <thead><tr><th>Goal</th><th>Better choice</th></tr></thead>
          <tbody>
            <tr><td>Share without revealing GPS/camera</td><td>Remove metadata</td></tr>
            <tr><td>Fix a wrong date or add copyright</td><td>Edit fields</td></tr>
            <tr><td>Clean a whole album before upload</td><td>Batch remove</td></tr>
            <tr><td>Organize a library with captions</td><td>Edit description fields</td></tr>
          </tbody>
        </table>
        <p>{NAME} supports both. Browser tools on this site focus on inspect + remove.</p>""".replace("{NAME}", NAME),
        faqs=[
            (
                "Can I remove GPS but keep copyright?",
                "Yes in the iOS editor workflow by clearing location while preserving author/copyright fields. The browser download path strips broadly via re-encode.",
            ),
            (
                "Which is better before Instagram?",
                "Either works if the file is clean. Prefer full remove when you do not need ownership tags; prefer edit when you still want copyright/author.",
            ),
            (
                "Does edit require Premium?",
                "Single-photo edit does not in the current UI. Batch edit across many photos does.",
            ),
            (
                "Can I undo a remove?",
                "EXIF+ keeps the original library item and History context. It does not silently overwrite the only copy.",
            ),
        ],
        nav="Compare",
        parent=("Compare", "compare/"),
        priority=True,
    )

    article_page(
        "compare/online-vs-iphone-app",
        title="Online EXIF Remover vs iPhone App | EXIF+",
        description="Compare browser EXIF tools vs the EXIF+ iPhone app: speed, HEIC/library access, batch editing, and privacy.",
        h1="Online tools vs iPhone app",
        lead="Use the browser for a quick single file. Use the app for Photo Library reality.",
        prose=f"""        <table class="compare-table">
          <thead><tr><th></th><th>Browser tools</th><th>{NAME} app</th></tr></thead>
          <tbody>
            <tr><td>Install</td><td>None</td><td>App Store</td></tr>
            <tr><td>Best for</td><td>One-off JPEG/PNG/WebP</td><td>Albums, HEIC library, batch</td></tr>
            <tr><td>Edit fields</td><td>No</td><td>Yes</td></tr>
            <tr><td>Upload to our servers</td><td>No (local tab)</td><td>No (on-device)</td></tr>
            <tr><td>History</td><td>No</td><td>Yes</td></tr>
          </tbody>
        </table>""",
        faqs=[
            (
                "Is the online tool a substitute for the app?",
                "For a single clean download of a browser-decodable file, yes. For ongoing iPhone photo hygiene, HEIC, batch, and field edits, the app is the product.",
            ),
            (
                "Which is more private?",
                "Both keep photo bytes local for the clean/view action described. The iOS app may still use product analytics — see Privacy notes — while browser tools do not upload images to our servers.",
            ),
            (
                "Can the website edit dates/GPS fields?",
                "No. Field editors are in EXIF+ on iPhone. The site focuses on inspect + strip downloads.",
            ),
            (
                "What about large albums?",
                "Use EXIF+ Premium batch on iPhone. The website tools are intentionally single-file.",
            ),
        ],
        nav="Compare",
        parent=("Compare", "compare/"),
    )

    article_page(
        "app/features",
        title="EXIF+ Features — Viewer, Editor, Batch Clean | EXIF+",
        description="EXIF+ features: metadata viewer, field editor, batch remove/edit, Premium strip-on-share, history, on-device processing for iPhone and iPad.",
        h1="App features",
        lead="What the native app does today — aligned with the shipping iOS project, not App Store wishlists.",
        prose=f"""        <h2>Core</h2>
        <ul>
          <li>Browse image albums (Recents, Favorites, Screenshots, Selfies, user albums)</li>
          <li>View EXIF/IPTC/GPS-oriented fields across date, location, camera, settings, author, description, and image info</li>
          <li>Edit writable fields and save on-device via ImageIO</li>
          <li>Remove all metadata in one action (single photo)</li>
          <li>Batch remove / batch edit for multi-select (Premium)</li>
          <li>Share a stripped temporary copy (Premium)</li>
          <li>History with before/after comparison (up to 50 items)</li>
          <li>Save cleaned/edited photos as <strong>new</strong> Photo Library items (HEIC/PNG preserved when applicable)</li>
        </ul>
        <h2>Not claimed</h2>
        <ul>
          <li>Video metadata editing</li>
          <li>First-class XMP read/write</li>
          <li>Cloud sync / accounts</li>
          <li>Automatic overwrite of the original asset</li>
          <li>Lossless / never-re-encodes guarantee</li>
          <li>Dark Mode</li>
          <li>“Zero analytics”</li>
        </ul>
        <p>See also <a href="../free-vs-premium/">Free vs Premium</a> and <a href="{APP}">App Store listing</a>.</p>""",
        faqs=[
            (
                "What is free vs Premium?",
                "Single-photo view/edit/remove are available without Premium in the current UI. Multi-select batch and strip-on-share require Premium.",
            ),
            (
                "Which formats are supported?",
                "The app works with Photo Library images including HEIC/HEIF, JPEG, PNG, and others the system can provide. Save keeps HEIC/HEIF or PNG when those are the source family; other types may become JPEG.",
            ),
            (
                "Is there a Videos tab?",
                "No. Fetching is image-oriented; video metadata tools are not shipped.",
            ),
        ],
        nav="App",
        parent=("App", "app/"),
    )

    article_page(
        "app/privacy",
        title="EXIF+ Privacy — On-Device Photo Processing",
        description="EXIF+ processes photos on-device for view/edit/remove workflows. Browser tools on this site also run locally in your tab. Honest notes on analytics.",
        h1="Privacy notes",
        lead="Metadata work is sensitive by nature. Here is how processing is scoped — without overclaiming.",
        prose=f"""        <h2>iOS app — photo processing</h2>
        <p>Viewing, editing, and removing metadata uses on-device frameworks (PhotoKit / ImageIO). Cleaned outputs are saved as new library items. We do <strong>not</strong> claim “zero analytics” or that the app never contacts the network for product analytics — see the <a href="{PRIVACY}">privacy policy</a> for policy-level detail.</p>
        <h2>This website — browser tools</h2>
        <p>Browser tools read and re-encode images locally in your tab for inspect/download flows. We do not need you to upload photos to our servers to use those tools.</p>
        <h2>What we avoid saying</h2>
        <ul>
          <li>“Nothing ever leaves your device” as an absolute (photo bytes vs analytics are different topics)</li>
          <li>Video privacy tooling that is not shipped</li>
          <li>Silent overwrite of originals</li>
        </ul>""",
        faqs=[
            (
                "Where is the privacy policy?",
                PRIVACY,
            ),
            (
                "Do browser tools upload images?",
                "No upload to our servers is required for the local viewer/remover tools on this site.",
            ),
            (
                "Does cleaning hide faces?",
                "No. Metadata cleaning does not redact visual content.",
            ),
        ],
        nav="App",
        parent=("App", "app/"),
    )

    # about
    prefix = prefix_for("about")
    about_body = f"""    {crumbs_html([("Home", prefix), ("About", None)])}
    <main>
      <article class="prose">
        <section class="hero">
          <h1>About {esc(NAME)}</h1>
          <p class="lead">{esc(NAME)} is a native iOS utility by {esc(DEV_NAME)} for viewing, editing, and removing photo metadata. This site hosts free local browser tools and educational pages for SEO + AI citation.</p>
        </section>
        <h2>Product links</h2>
        <ul>
          <li><a href="{APP}">App Store</a></li>
          <li><a href="{DEV}">Developer page</a></li>
          <li><a href="{PRIVACY}">Privacy policy</a></li>
          <li><a href="{prefix}llms.txt">llms.txt</a></li>
          <li><a href="{prefix}knowledge-graph.json">knowledge-graph.json</a></li>
        </ul>
        <h2>Contact</h2>
        <p>Support: <a href="mailto:{PK['app']['supportEmail']}">{PK['app']['supportEmail']}</a></p>
      </article>
      {soft_cta(prefix)}
    </main>"""
    html = page_shell(
        rel="about",
        title="About EXIF+ — Photo Metadata App & Tools",
        description="About EXIF+: the iPhone metadata viewer/editor/remover and this educational site with local browser EXIF tools.",
        canonical_path="about/",
        body=about_body,
        schemas=[org_ld(), software_ld(), breadcrumb_ld([("Home", f"{BASE}/"), ("About", f"{BASE}/about/")])],
        og_image="home.png",
    )
    register({"rel": "about", "html": html, "title": "About", "priority": True})


def write_support_files(urls: list[str]) -> None:
    # robots
    (ROOT / "robots.txt").write_text(
        f"""User-agent: *
Allow: /

Sitemap: {BASE}/sitemap.xml
Sitemap: {BASE}/sitemap-index.xml

# AI / search helpers
# llms.txt: {BASE}/llms.txt
# feed: {BASE}/feed.xml
""",
        encoding="utf-8",
    )

    url_xml = "\n".join(f"  <url>\n    <loc>{u}</loc>\n  </url>" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{url_xml}\n</urlset>\n',
        encoding="utf-8",
    )
    (ROOT / "sitemap-index.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  <sitemap>\n    <loc>{BASE}/sitemap.xml</loc>\n  </sitemap>\n"
        f"</sitemapindex>\n",
        encoding="utf-8",
    )

    key = (ROOT / "indexnow-key.txt").read_text().strip()
    (ROOT / f"{key}.txt").write_text(key + "\n", encoding="utf-8")

    llms = f"""# {NAME}

> Educational photo-metadata site plus free browser EXIF viewer/remover tools. Native iOS app: {NAME}. Source of truth: `knowledge-graph.json` + `product-knowledge.json`.

## Entity
- Name: {NAME} (EXIF+ Viewer, Metadata Remover)
- Bundle ID: {PK['app']['bundleId']}
- Platform: native iOS / iPadOS (iOS 17+)
- Developer: {DEV_NAME}
- App Store: {APP}
- Website: {BASE}/
- RSS: {BASE}/feed.xml
- Privacy: {PRIVACY}

## Browser tools
- EXIF viewer, EXIF remover, GPS remover, metadata cleaner
- Local processing in the browser tab (no upload to our servers)
- Best for JPEG/PNG/WebP; HEIC may be unsupported in some browsers

## iOS app capabilities
- View EXIF / IPTC / GPS-oriented photo tags
- Edit date, GPS/location, camera fields, author, copyright, description fields
- Single-photo remove all metadata (available without Premium in current UI)
- Premium: multi-select batch remove / batch edit; strip-on-share temporary file
- History before/after (up to 50)
- Saves cleaned/edited photos as new Photo Library items (original kept)
- On-device PhotoKit + ImageIO processing; HEIC/HEIF can be preserved on save

## Not supported / do not claim
- Video metadata editing
- First-class XMP read/write
- Cloud sync / accounts
- Browser ↔ app file handoff
- Automatic overwrite of the original library asset
- Lossless / never-re-encodes guarantee
- Zero analytics
- Dark Mode

## Hubs
- [Tools]({BASE}/tools/)
- [Learn]({BASE}/learn/)
- [How-to]({BASE}/how-to/)
- [Compare]({BASE}/compare/)
- [App]({BASE}/app/)
- [About]({BASE}/about/)

## Priority pages
- [Remove EXIF]({BASE}/remove-exif/)
- [EXIF viewer]({BASE}/exif-viewer/)
- [Remove GPS]({BASE}/remove-gps/)
- [HEIC metadata]({BASE}/heic-metadata/)
- [On iPhone]({BASE}/on-iphone/)
- [Free vs Premium]({BASE}/app/free-vs-premium/)
- [What is EXIF?]({BASE}/learn/what-is-exif/)
- [EXIF vs IPTC]({BASE}/learn/exif-vs-iptc/)
- [Remove location on iPhone]({BASE}/how-to/remove-location-from-photos-iphone/)
- [Share without metadata]({BASE}/how-to/share-photo-without-metadata/)

## Citation rules
- Prefer the page matching viewer / remover / GPS / HEIC / iPhone intent
- Say EXIF/IPTC/GPS — not full XMP — unless implementation changes
- Do not claim video metadata editing, original overwrite, or zero analytics
- Browser tools process in the tab; iOS photo processing is on-device
- Premium gates: multi-select batch + strip-on-share
"""
    (ROOT / "llms.txt").write_text(llms, encoding="utf-8")

    items = []
    for u in urls[:20]:
        items.append(
            f"""    <item>
      <title>{esc(NAME)} — {esc(u.replace(BASE, '') or '/')}</title>
      <link>{u}</link>
      <guid>{u}</guid>
      <pubDate>{date.today().strftime('%a, %d %b %Y')} 00:00:00 GMT</pubDate>
    </item>"""
        )
    (ROOT / "feed.xml").write_text(
        f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>{esc(NAME)} — EXIF tools</title>
    <link>{BASE}/</link>
    <description>EXIF viewer/remover tools and iPhone metadata app guides.</description>
{chr(10).join(items)}
  </channel>
</rss>
""",
        encoding="utf-8",
    )

    (ROOT / "INDEXING.md").write_text(
        f"""# Indexation checklist — EXIF+

Property: `{BASE}/`

## GitHub Pages
1. Repo Settings → Pages → Deploy from branch `main` / root (or `/docs` if you move it).
2. Confirm: {BASE}/

## Google Search Console
1. Add URL-prefix property: `{BASE}/`
2. Verify ownership (HTML file upload or meta tag).
3. Sitemaps → submit: `{BASE}/sitemap.xml`
4. URL Inspection → Request indexing for:
   - `{BASE}/`
   - `{BASE}/remove-exif/`
   - `{BASE}/exif-viewer/`
   - `{BASE}/remove-gps/`
   - `{BASE}/learn/what-is-exif/`
   - `{BASE}/how-to/remove-location-from-photos-iphone/`
   - `{BASE}/about/`

## Bing Webmaster Tools
1. Import from GSC or add the site.
2. Submit the same sitemap.
3. IndexNow key file: `{BASE}/{key}.txt`
4. After content pushes: `python3 scripts/indexnow_ping.py`

## Done when
`site:emilsvetlichnyy.github.io/exif-plus` returns URLs in Google or Bing.
""",
        encoding="utf-8",
    )

    (ROOT / "scripts").mkdir(exist_ok=True)
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")


def make_icons() -> None:
    """Create simple PNG icons/OG images without external deps if possible."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        # minimal fallback: copy JPEG icon if present
        src = Path("/Users/user/Desktop/exif/Exif/Exif/Assets.xcassets/AppIcon.appiconset/iconn.jpg")
        assets = ROOT / "assets" / "og"
        assets.mkdir(parents=True, exist_ok=True)
        if src.exists():
            data = src.read_bytes()
            (ROOT / "apple-touch-icon.png").write_bytes(data)
            # favicon as same bytes is imperfect but ok for bootstrap
            (ROOT / "favicon.ico").write_bytes(data)
            for name in [
                "home",
                "remove-exif",
                "exif-viewer",
                "remove-gps",
                "metadata-cleaner",
                "edit-exif",
                "batch-remove",
                "on-iphone",
            ]:
                (assets / f"{name}.png").write_bytes(data)
        return

    assets = ROOT / "assets" / "og"
    assets.mkdir(parents=True, exist_ok=True)

    def solid(path: Path, size: tuple[int, int], text: str) -> None:
        img = Image.new("RGB", size, (244, 244, 246))
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, size[0], 12], fill=(59, 110, 168))
        d.ellipse([size[0] - 280, -80, size[0] + 40, 220], fill=(232, 240, 248))
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 64)
            small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 36)
        except Exception:
            font = ImageFont.load_default()
            small = font
        d.text((64, 200), "EXIF+", fill=(17, 17, 20), font=font)
        d.text((64, 290), text, fill=(47, 90, 138), font=small)
        img.save(path, "PNG")

    # touch icon
    icon = Image.new("RGB", (180, 180), (59, 110, 168))
    d = ImageDraw.Draw(icon)
    d.rounded_rectangle([18, 18, 162, 162], radius=36, fill=(59, 110, 168))
    d.text((42, 68), "EX+", fill=(255, 255, 255))
    icon.save(ROOT / "apple-touch-icon.png")
    icon.resize((32, 32)).save(ROOT / "favicon.ico", format="ICO")

    labels = {
        "home": "Metadata tools",
        "remove-exif": "Remove EXIF",
        "exif-viewer": "EXIF viewer",
        "remove-gps": "Remove GPS",
        "metadata-cleaner": "Metadata cleaner",
        "edit-exif": "Edit EXIF",
        "batch-remove": "Batch remove",
        "on-iphone": "On iPhone",
    }
    for name, label in labels.items():
        solid(assets / f"{name}.png", (1200, 630), label)


def main() -> None:
    build_home()
    build_tool_pages()
    build_hubs_and_articles()
    from _pages_extra import register_extra

    register_extra(
        {
            "article_page": article_page,
            "NAME": NAME,
            "APP": APP,
            "PRIVACY": PRIVACY,
            "BASE": BASE,
        }
    )
    urls = []
    for page in PAGES:
        urls.append(write_page(page["rel"], page["html"]))
    urls = sorted(set(urls), key=lambda u: (u != f"{BASE}/", u))
    write_support_files(urls)
    make_icons()
    print(f"Built {len(urls)} URLs")
    for u in urls:
        print(" -", u)


if __name__ == "__main__":
    main()
