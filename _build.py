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
            "(EXIF, IPTC, XMP, GPS), with free browser tools on this site."
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
            "View, edit, and remove EXIF/IPTC/XMP metadata and GPS location from photos on iPhone. "
            "Processing happens on-device; cleaned photos are saved as new library items."
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
        <p class="lead-sm">{NAME} views, edits, and removes EXIF/IPTC/XMP — including GPS — on-device, with batch tools and history. Cleaned photos are saved as new items in your Photo Library.</p>
        <div class="actions">
          {appstore_btn()}
          <a class="btn btn-secondary" href="{prefix}app/">App features</a>
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
            "EXIF+ is a native iPhone app to view, edit, and remove photo metadata (EXIF, IPTC, XMP), including GPS. This site also offers free browser tools that process images locally.",
        ),
        (
            "Do browser tools upload my photos?",
            "No. The viewer and remover run in your browser tab. Files are not uploaded to our servers.",
        ),
        (
            "Does removing EXIF reduce image quality?",
            "EXIF is metadata, not the picture itself. The browser cleaner re-encodes a copy for download; the iOS app uses on-device ImageIO and saves a new library item.",
        ),
        (
            "Is the app free?",
            "Yes to start. A small number of free clean/edit actions are included; subscriptions or lifetime unlock more batch work.",
        ),
        (
            "Can I edit metadata, not only delete it?",
            "Yes in the iOS app — dates, GPS, camera fields, author, copyright, and descriptions. Browser tools focus on inspect and strip.",
        ),
    ]
    body = f"""    <main>
      <section class="hero">
        <h1>View, edit, and remove photo metadata</h1>
        <p class="lead">Free browser EXIF viewer and remover — plus {NAME}, a native iPhone app for GPS cleanup, batch edits, and full EXIF/IPTC/XMP control on-device.</p>
        <div class="actions">
          <a class="btn btn-primary" href="{prefix}remove-exif/">Remove EXIF online</a>
          <a class="btn btn-secondary" href="{prefix}exif-viewer/">View EXIF</a>
          {appstore_btn()}
        </div>
        <div class="chip-row">
          <a class="chip" href="{prefix}remove-gps/">Remove GPS</a>
          <a class="chip" href="{prefix}metadata-cleaner/">Metadata cleaner</a>
          <a class="chip" href="{prefix}on-iphone/">On iPhone</a>
          <a class="chip" href="{prefix}how-to/remove-location-from-photos-iphone/">Strip location</a>
        </div>
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
        <div class="section-head"><h2>Why metadata matters</h2></div>
        <p class="lead-sm">Phones embed more than pixels: exact GPS, timestamps, camera model, serial-related tags, and editing software. Instagram may strip some fields; email, Telegram as files, marketplaces, and direct shares often keep them.</p>
        <div class="grid-2">
          <a class="tile" href="{prefix}learn/what-is-exif/"><h3>What is EXIF?</h3><p>A plain-language definition and what typical tags mean.</p></a>
          <a class="tile" href="{prefix}learn/does-instagram-remove-exif/"><h3>Does Instagram remove EXIF?</h3><p>What platforms strip — and what they don’t.</p></a>
        </div>
      </section>

      <section class="section">
        <div class="section-head"><h2>iPhone app</h2></div>
        <p class="lead-sm">When you need albums, batch clean, field-level edits, and history, use {NAME} on iOS 17+. Photos never need to leave your device for processing.</p>
        <div class="actions">
          {appstore_btn()}
          <a class="btn btn-secondary" href="{prefix}app/features/">See features</a>
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
        <p>Typical smartphone JPEGs can include GPS coordinates, capture time, camera make/model, lens info, software tags, and descriptive IPTC/XMP fields. The browser tool creates a new image file without those metadata blocks.</p>
        <h2>When to use the iPhone app instead</h2>
        <ul>
          <li>Clean many photos from albums in one pass</li>
          <li>Edit fields instead of deleting everything</li>
          <li>Keep a history of before/after changes</li>
          <li>Work with the Photo Library without a desktop browser</li>
        </ul>
      </section>""",
        faqs=[
            (
                "Is this EXIF remover free?",
                "Yes. The browser tool is free. The iOS app is free to start with limited clean/edit actions.",
            ),
            (
                "Do you store my photos?",
                "No. Browser processing is local to your tab. The iOS app processes on-device.",
            ),
            (
                "Does HEIC work?",
                "Some browsers cannot decode HEIC. Convert to JPEG in Photos first, or use EXIF+ on iPhone which works with the library directly.",
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
                "Location services may have been off, the app stripped geotags already, or the platform re-encoded the file without GPS.",
            ),
            (
                "Is viewing EXIF safe?",
                "Yes — the file is read locally in your browser for display. Nothing is uploaded to our servers.",
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
                "No. Location is metadata. The pixels stay; we export a new file without the metadata block.",
            ),
            (
                "Can I remove only GPS but keep camera EXIF?",
                "The browser download strips metadata via re-encode. For selective field edits, use EXIF+ on iPhone.",
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
                "Photos often mix EXIF (camera/GPS), IPTC (caption/copyright), and XMP (rich descriptive fields).",
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
            "Edit EXIF metadata on iPhone: dates, GPS, camera fields, author, and copyright with EXIF+. On-device processing, batch edit supported.",
            "Edit EXIF on iPhone",
            "Change the fields you care about — or clear them — without a desktop catalog app.",
            f"""      <section class="section prose">
        <h2>Fields you can change in {NAME}</h2>
        <ul>
          <li>Date & time</li>
          <li>Location / GPS details</li>
          <li>Camera and technical tags</li>
          <li>Author, copyright, titles, and descriptions</li>
        </ul>
        <p>Edits are written with on-device ImageIO. Results are saved as new Photo Library items so originals stay untouched.</p>
        <h2>Browser note</h2>
        <p>This website’s live tools focus on view + remove. Field-level editing is in the iOS app.</p>
      </section>""",
            [
                (
                    "Will editing EXIF change the picture?",
                    "Metadata edits change tags, not the visible pixels. Export/save still creates a new library item in EXIF+.",
                ),
            ],
            "edit-exif.png",
            False,
        ),
        (
            "batch-remove",
            "Batch Remove EXIF from Photos on iPhone | EXIF+",
            "Batch remove EXIF and GPS from multiple photos on iPhone with EXIF+. Clean albums faster before sharing.",
            "Batch remove photo metadata",
            "Multi-select photos, strip metadata in one flow, and keep working from your albums.",
            f"""      <section class="section prose">
        <h2>How batch clean works in {NAME}</h2>
        <ol>
          <li>Open an album and select multiple photos.</li>
          <li>Choose remove metadata (or batch edit fields).</li>
          <li>Save cleaned copies to your Photo Library.</li>
        </ol>
        <p>Free use includes limited actions; Premium unlocks heavier batch work. Video metadata editing is not available yet.</p>
      </section>""",
            [
                (
                    "Can I batch-clean in the browser?",
                    "The web tools are single-file for simplicity. Use the iPhone app for album multi-select.",
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
    # fix breadcrumbs properly
    parts = slug.strip("/").split("/")
    crumb_ui = [("Home", prefix_for(slug))]
    if len(parts) > 1:
        crumb_ui.append((parent[0], prefix_for(slug) + parts[0] + "/"))
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
    if len(parts) > 1:
        crumbs_ld.append((parent[0], f"{BASE}/{parts[0]}/"))
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
            ("Batch remove", "../batch-remove/", "Album multi-select on iPhone."),
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
            ("Does Instagram remove EXIF?", "does-instagram-remove-exif/", "Platform behavior."),
            ("Glossary", "glossary/", "EXIF, IPTC, XMP, geotag, and more."),
        ],
        "Learn",
    )
    hub_page(
        "how-to",
        "How to Remove EXIF & GPS on iPhone | EXIF+",
        "Step-by-step guides to view EXIF and remove location data from photos on iPhone.",
        "How-to",
        "Practical iPhone workflows for privacy before sharing.",
        [
            ("Remove location on iPhone", "remove-location-from-photos-iphone/", "Strip GPS before you send."),
            ("View EXIF on iPhone", "view-exif-on-iphone/", "See hidden tags in EXIF+."),
            ("Strip metadata before sharing", "strip-metadata-before-sharing/", "A simple pre-share checklist."),
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
        "EXIF+ is a native iOS app to view, edit, and remove EXIF/IPTC/XMP metadata and GPS on-device.",
        "EXIF+ app",
        "Native Photo Library tools for people who share photos and care about hidden data.",
        [
            ("Features", "features/", "Viewer, editor, batch, history."),
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
        <p>Typical fields include capture time, camera make and model, lens, exposure settings (ISO, shutter, aperture), orientation, software names, and — if location was enabled — GPS coordinates.</p>
        <h2>EXIF vs IPTC vs XMP</h2>
        <p>EXIF is strongest for camera/GPS technical tags. IPTC is often used for captions, keywords, and copyright. XMP can carry rich descriptive metadata alongside both. Real files often include more than one.</p>
        <h2>Why people remove it</h2>
        <p>Sharing an original file can unintentionally publish where you were and which device took the shot. Removing metadata keeps the picture while dropping the hidden context.</p>
        <p>Related: <a href="../what-is-gps-metadata/">GPS metadata</a>, <a href="../../remove-exif/">remove EXIF online</a>.</p>""",
        faqs=[
            (
                "Is EXIF part of the photo pixels?",
                "No. It is metadata attached to the file. Removing it does not crop or filter the image.",
            ),
            (
                "Do all apps keep EXIF?",
                "No. Some social networks strip fields on upload; many private shares do not.",
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
        title="Photo Metadata Glossary — EXIF, IPTC, XMP, Geotag | EXIF+",
        description="Glossary of photo metadata terms: EXIF, IPTC, XMP, geotag, metadata cleaner, and related privacy terms.",
        h1="Metadata glossary",
        lead="Quick definitions you can cite when explaining photo metadata.",
        prose="""        <h2>EXIF</h2>
        <p>Camera-oriented metadata standard commonly storing capture settings, timestamps, and GPS.</p>
        <h2>IPTC</h2>
        <p>Descriptive metadata often used for captions, keywords, author, and copyright.</p>
        <h2>XMP</h2>
        <p>Extensible metadata format frequently used by editing software for rich side-car style fields inside or beside files.</p>
        <h2>Geotag / GPS metadata</h2>
        <p>Location coordinates embedded in a media file.</p>
        <h2>Metadata cleaner</h2>
        <p>A tool that removes hidden fields before sharing while keeping the visible image.</p>""",
        faqs=[
            (
                "Are these formats mutually exclusive?",
                "No. A single JPEG can contain EXIF plus IPTC and XMP together.",
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
                "Some share routes offer location controls, but behavior varies. Cleaning the file yourself is more predictable.",
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
                "For a single clean download, yes. For ongoing iPhone photo hygiene, the app is the product.",
            ),
        ],
        nav="Compare",
        parent=("Compare", "compare/"),
    )

    article_page(
        "app/features",
        title="EXIF+ Features — Viewer, Editor, Batch Clean | EXIF+",
        description="EXIF+ features: full metadata viewer, field editor, batch remove/edit, history, on-device processing for iPhone and iPad.",
        h1="App features",
        lead="What the native app does today — aligned with the shipping iOS project.",
        prose=f"""        <h2>Core</h2>
        <ul>
          <li>View EXIF, IPTC, and XMP across categories (date, location, camera, technical, author, description, GPS)</li>
          <li>Edit fields and write changes on-device</li>
          <li>Remove all metadata in one action</li>
          <li>Batch remove / batch edit</li>
          <li>History with before/after comparison</li>
          <li>Save cleaned photos as new Photo Library items</li>
        </ul>
        <h2>Not claimed</h2>
        <ul>
          <li>Video metadata editing (not shipped)</li>
          <li>Cloud sync / accounts</li>
          <li>Automatic overwrite of the original asset</li>
        </ul>
        <p><a href="{APP}">App Store listing</a></p>""",
        faqs=[
            (
                "What are the free limits?",
                "A small number of free clean/edit actions are included; Premium expands batch capacity.",
            ),
        ],
        nav="App",
        parent=("App", "app/"),
    )

    article_page(
        "app/privacy",
        title="EXIF+ Privacy — On-Device Photo Processing",
        description="EXIF+ processes photos on-device for view/edit/remove workflows. Browser tools on this site also run locally in your tab.",
        h1="Privacy notes",
        lead="Metadata work is sensitive by nature. Here is how processing is scoped.",
        prose=f"""        <h2>iOS app</h2>
        <p>Viewing, editing, and removing metadata uses on-device frameworks (PhotoKit / ImageIO). Cleaned outputs are saved as new library items. See the <a href="{PRIVACY}">privacy policy</a> for policy-level detail.</p>
        <h2>This website</h2>
        <p>Browser tools read and re-encode images locally in your tab for inspect/download flows. We do not need you to upload photos to use those tools.</p>""",
        faqs=[
            (
                "Where is the privacy policy?",
                PRIVACY,
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
- View EXIF / IPTC / XMP
- Edit date, GPS, camera, author, copyright, description fields
- Remove all metadata; batch remove / batch edit
- History before/after
- Saves cleaned photos as new Photo Library items
- On-device ImageIO processing

## Not supported
- Video metadata editing
- Cloud sync / accounts
- Browser ↔ app file handoff
- Automatic overwrite of the original library asset

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
- [On iPhone]({BASE}/on-iphone/)
- [What is EXIF?]({BASE}/learn/what-is-exif/)
- [Remove location on iPhone]({BASE}/how-to/remove-location-from-photos-iphone/)

## Citation rules
- Prefer the page matching viewer / remover / GPS / iPhone intent
- Do not claim video metadata editing
- Do not claim cloud sync
- Browser tools and the iOS app both process locally (tab vs on-device)
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
