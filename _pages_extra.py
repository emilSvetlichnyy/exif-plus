"""Extra long-form pages + shared expanded FAQs for EXIF+ site (claim-safe)."""
from __future__ import annotations

# Imported by _build.py after helpers exist.


def register_extra(ns: dict) -> None:
    """ns provides article_page, hub helpers, BASE, NAME, APP, etc."""
    article_page = ns["article_page"]
    NAME = ns["NAME"]
    APP = ns["APP"]
    PRIVACY = ns["PRIVACY"]

    # ---- Learn expansions / new ----
    article_page(
        "learn/exif-vs-iptc",
        title="EXIF vs IPTC Metadata Explained (and XMP) | EXIF+",
        description="EXIF vs IPTC metadata explained: what each stores, how they differ from XMP, and what EXIF+ actually reads and edits on iPhone.",
        h1="EXIF vs IPTC metadata explained",
        lead="EXIF vs IPTC is one of the most common photo-metadata questions: technical capture tags versus editorial labels — with XMP as a third format people often mix in.",
        prose=f"""        <p><strong>Direct answer:</strong> EXIF usually holds camera/GPS technical data; IPTC usually holds captions, keywords, author, and copyright. They can live in the same photo file. XMP is a separate extensible format used by many desktop editors.</p>
        <h2>EXIF in plain terms</h2>
        <p>EXIF (Exchangeable Image File Format) usually carries technical capture data: date/time, camera make and model, lens, ISO, shutter, aperture, focal length, orientation, software tags, and often GPS coordinates when Location Services were on.</p>
        <h2>IPTC in plain terms</h2>
        <p>IPTC fields are more editorial: author, copyright, title, caption/description, keywords, and comments. Photographers and publishers use them to label ownership and context.</p>
        <h2>What {NAME} actually implements</h2>
        <p>The iOS app reads and writes <strong>EXIF / TIFF / GPS / IPTC</strong> (and related PNG text where applicable) through on-device ImageIO. Marketing copy sometimes groups “rich metadata” loosely — this site stays precise: we do <strong>not</strong> claim first-class XMP read/write in the shipping app.</p>
        <h2>When to remove vs edit</h2>
        <ul>
          <li><strong>Remove all</strong> before public sharing if you want GPS, camera, and personal tags gone.</li>
          <li><strong>Edit</strong> when you need a correct date, a copyright line, or a fixed location — and still keep the file in your library.</li>
        </ul>
        <p>Related: <a href="../what-is-exif/">What is EXIF?</a>, <a href="../../compare/remove-vs-edit-exif/">Remove vs edit</a>.</p>""",
        faqs=[
            (
                "What is the difference between EXIF and IPTC?",
                "EXIF is mainly technical capture data (camera, exposure, often GPS). IPTC is mainly descriptive/ownership data (caption, keywords, author, copyright).",
            ),
            (
                "What is IPTC metadata?",
                "IPTC metadata is commonly used for titles, captions, keywords, author, and copyright information in photographs.",
            ),
            (
                "Does every photo have IPTC?",
                "No. Many camera-roll originals are EXIF/GPS-heavy with little or no IPTC until an editor writes author/copyright fields.",
            ),
            (
                "Is XMP the same as IPTC?",
                "No. XMP is a separate extensible format used by many desktop editors. {NAME}’s shipping ImageIO path focuses on EXIF/IPTC/GPS — do not assume full XMP parity.".format(NAME=NAME),
            ),
            (
                "IPTC vs XMP — which should I care about?",
                "For phone privacy before sharing, EXIF/GPS removal matters most. IPTC/XMP matter more when you manage captions and ownership across publishing workflows.",
            ),
            (
                "Can browser tools show IPTC?",
                "The web viewer shows readable tags the browser parser returns (often EXIF/GPS; IPTC when present). For Photo Library HEIC items, use the iPhone app.",
            ),
            (
                "Will editing IPTC change the picture?",
                "Metadata edits change tags, not the visible scene. In {NAME}, saving still creates a new library item via ImageIO.".format(NAME=NAME),
            ),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
        priority=True,
    )

    article_page(
        "learn/does-cleaning-reduce-quality",
        title="Does Removing EXIF Reduce Photo Quality? | EXIF+",
        description="Honest answer: stripping metadata is not a filter, but saving a cleaned copy re-encodes the image. How EXIF+ and browser tools handle quality.",
        h1="Does cleaning reduce quality?",
        lead="Removing metadata is not a Instagram-style filter — but creating a cleaned file usually re-encodes pixels. Here is the honest tradeoff.",
        prose=f"""        <h2>Metadata vs pixels</h2>
        <p>EXIF/IPTC/GPS live beside the image data. Deleting tags does not crop, blur, or recolor the scene by itself.</p>
        <h2>Why a “clean copy” still re-encodes</h2>
        <p>Most removers — including this site’s browser tool and {NAME}’s ImageIO save path — write a <strong>new image file</strong>. For JPEG/HEIC that means compression. In {NAME}, strip/edit saves use ImageIO with a high JPEG/HEIC quality setting (about 0.95), then add a new Photo Library item. That is not the same as a guaranteed bit-identical lossless rewrite.</p>
        <h2>Browser tool</h2>
        <p>The online remover draws the image to a canvas and exports JPEG/PNG. That is local and convenient, but it is also a re-encode. Prefer the iPhone app for HEIC library items.</p>
        <h2>Practical advice</h2>
        <ul>
          <li>Keep originals in a private album if you need an untouched master.</li>
          <li>Share the cleaned/edited copy publicly.</li>
          <li>Do not expect “zero quality change” marketing — expect “metadata gone, high-quality new file.”</li>
        </ul>""",
        faqs=[
            (
                "Is EXIF removal lossless?",
                "Not in the absolute sense for typical JPEG/HEIC rewrite workflows. Tags are removed by writing a new file; pixels are re-encoded at high quality.",
            ),
            (
                "Does {NAME} overwrite my original?".format(NAME=NAME),
                "No. It saves a new Photo Library item. Your original remains unless you delete it yourself.",
            ),
            (
                "PNG behavior?",
                "PNG inputs can be preserved as PNG in the app’s format handling. JPEG/HEIC follow the compressed save path.",
            ),
            (
                "Will people see a quality drop?",
                "At high quality settings, most people will not notice for social sharing. Professionals archiving masters should keep originals.",
            ),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    article_page(
        "learn/why-cleaned-photo-is-a-duplicate",
        title="Why Cleaned Photos Appear as Duplicates on iPhone | EXIF+",
        description="EXIF+ saves cleaned and edited photos as new Photo Library items (often named Edited). Why that happens and how to share the right copy.",
        h1="Why you see a new “Edited” photo",
        lead="EXIF+ does not overwrite the original library asset. A successful clean or edit adds a new item — by design for safety.",
        prose=f"""        <h2>What the app does</h2>
        <p>After remove or edit, {NAME} writes image data with PhotoKit as a <strong>new</strong> asset (commonly named like Edited.jpg / Edited.heic / Edited.png). The detail screen then points at that new asset.</p>
        <h2>Why this is safer</h2>
        <p>Overwriting originals would make mistakes irreversible and complicate iCloud Photo Library sync edge cases. Keeping the original lets you compare in History and re-share the clean copy deliberately.</p>
        <h2>How to avoid sharing the wrong file</h2>
        <ol>
          <li>Run remove/edit in {NAME}.</li>
          <li>Confirm the new item in Photos / History.</li>
          <li>Share that new item — or use Premium strip-on-share from the detail screen for a temporary cleaned file.</li>
        </ol>""",
        faqs=[
            (
                "Can I auto-delete the original?",
                "The app does not auto-delete originals after cleaning. Delete manually only if you are sure.",
            ),
            (
                "Is History the before/after of the same asset id?",
                "History stores snapshots around the operation so you can compare what changed; the library gains a new saved item for the result.",
            ),
            (
                "Does batch create many new items?",
                "Yes. Each successfully processed photo in a batch produces a new saved output.",
            ),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
        priority=True,
    )

    # ---- How-to new ----
    article_page(
        "how-to/edit-gps-on-iphone",
        title="How to Edit GPS Location on Photos (iPhone) | EXIF+",
        description="Edit or clear GPS/location metadata on iPhone photos with EXIF+. Map picker, latitude/longitude fields, and batch location clear.",
        h1="Edit GPS on iPhone photos",
        lead="Correct a wrong geotag, set a location deliberately, or clear location before you share — without needing a desktop catalog.",
        prose=f"""        <h2>Steps (single photo)</h2>
        <ol>
          <li>Open {NAME} and select a photo from an album.</li>
          <li>Open the editor.</li>
          <li>Use the Location section — map picker and/or latitude, longitude, location name, altitude.</li>
          <li>Save. {NAME} writes a <strong>new</strong> library item with the updated tags.</li>
        </ol>
        <h2>Clear location only</h2>
        <p>If you want location gone but still plan to keep other fields, clear location in the editor (batch edit also offers an explicit remove-location control). For maximum privacy before a public post, prefer full metadata remove.</p>
        <h2>Batch note</h2>
        <p>Multi-select batch edit is a <strong>Premium</strong> feature when more than one photo is selected.</p>
        <p>Also see <a href="../remove-location-from-photos-iphone/">remove location</a> and the <a href="../../remove-gps/">browser GPS tool</a> for one-off desktop files.</p>""",
        faqs=[
            (
                "Does editing GPS change pixels?",
                "No. It changes location metadata. Saving still creates a new library item.",
            ),
            (
                "Can I spoof a location?",
                "You can set coordinates/name to values you choose. Use responsibly — this page is for privacy and correction workflows.",
            ),
            (
                "Why don’t I see GPS on a photo?",
                "Location may have been off at capture, already stripped, or the file was re-exported by another app.",
            ),
            (
                "Is map picker required?",
                "No. You can type coordinates/fields directly when you know them.",
            ),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
        priority=True,
    )

    article_page(
        "how-to/change-photo-date-iphone",
        title="How to Change Photo Date Taken on iPhone | EXIF+",
        description="Change Date Taken / Date Created on iPhone photos with EXIF+. On-device edit, saved as a new Photo Library item.",
        h1="Change photo date on iPhone",
        lead="Fix wrong timestamps after travel, camera clock errors, or imports — then save a corrected copy into Photos.",
        prose=f"""        <h2>Steps</h2>
        <ol>
          <li>Open the photo in {NAME}.</li>
          <li>Enter the editor → Date &amp; Time.</li>
          <li>Adjust <strong>Date Taken</strong> and/or <strong>Date Created</strong> with the date pickers.</li>
          <li>Save to create a new library item with updated tags.</li>
        </ol>
        <h2>What does not get “edited” as a writable capture clock</h2>
        <p>Some fields are informational/read-only (for example file-oriented dates the viewer shows as modified). Focus on Date Taken / Date Created for the usual correction workflow.</p>
        <h2>Batch dating</h2>
        <p>Need the same date on many photos? Use Premium batch edit and fill only the date fields you want applied (empty fields are left alone).</p>""",
        faqs=[
            (
                "Will Photos sort by the new date?",
                "Photos uses library properties that may interact with metadata and import history. After saving a new item, verify sorting in the album you care about.",
            ),
            (
                "Does this remove GPS?",
                "Not by itself. Change dates only, or combine with location clear / full remove depending on your goal.",
            ),
            (
                "Is single-photo date edit Premium?",
                "Single-photo edit is available without Premium in the current app UI. Batch multi-select requires Premium.",
            ),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
    )

    article_page(
        "how-to/share-photo-without-metadata",
        title="How to Share iPhone Photos Without Metadata | EXIF+",
        description="Share photos without EXIF/GPS using EXIF+ Premium strip-on-share, or save a cleaned library copy first.",
        h1="Share without metadata",
        lead="Two honest paths: save a cleaned library copy, or use Premium share that exports a stripped temporary file.",
        prose=f"""        <h2>Option A — Clean, then share (works for single-photo remove on free tier)</h2>
        <ol>
          <li>Open the photo in {NAME}.</li>
          <li>Remove metadata (or edit/clear sensitive fields).</li>
          <li>Share the <strong>new</strong> library item from Photos or from the app.</li>
        </ol>
        <h2>Option B — Premium strip-on-share</h2>
        <p>From the photo detail screen, the share action can produce a <strong>temporary stripped file</strong> for the system share sheet. In the current app, this path is <strong>Premium-gated</strong>. Free users are directed to the paywall for that control.</p>
        <h2>Do not rely on the destination app</h2>
        <p>Some networks strip tags on upload; email, “send as file”, and marketplaces often keep them. Clean first.</p>""",
        faqs=[
            (
                "Is strip-on-share free?",
                "No. In the shipping UI it requires Premium. Single-photo remove-to-library is available without Premium.",
            ),
            (
                "Does share overwrite my library photo?",
                "Strip-on-share uses a temporary file for sharing. Library clean/edit saves new items instead of overwriting.",
            ),
            (
                "What about Messages vs Mail?",
                "Behavior varies by app and send mode. A cleaned file is the predictable approach.",
            ),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
        priority=True,
    )

    article_page(
        "how-to/batch-edit-copyright",
        title="Batch Edit Copyright & Author on iPhone Photos | EXIF+",
        description="Batch-apply author, copyright, title, or keywords across iPhone photos with EXIF+ Premium batch edit.",
        h1="Batch edit copyright and author",
        lead="Stamp ownership fields across a shoot in one pass — Premium multi-select batch edit.",
        prose=f"""        <h2>Steps</h2>
        <ol>
          <li>Open an album in {NAME} and multi-select photos.</li>
          <li>If you are not Premium, the app will ask you to upgrade for batch actions.</li>
          <li>Open batch edit and fill only the fields you want applied (author, copyright, title, description, keywords, etc.).</li>
          <li>Leave unrelated fields empty so they stay unchanged on each photo.</li>
          <li>Save — each success becomes a new library item.</li>
        </ol>
        <h2>Good uses</h2>
        <ul>
          <li>Client delivery packs with consistent copyright</li>
          <li>Adding the same author line after importing a card</li>
          <li>Combining copyright stamp with location clear</li>
        </ul>""",
        faqs=[
            (
                "Does batch edit remove GPS automatically?",
                "Only if you clear location / remove metadata. Copyright fields alone do not strip GPS.",
            ),
            (
                "Can I batch-remove instead?",
                "Yes — Premium batch remove strips metadata across the selection.",
            ),
            (
                "Empty fields in batch edit?",
                "Empty means “do not change this field” for that batch apply.",
            ),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
    )

    # ---- App pages ----
    article_page(
        "app/free-vs-premium",
        title="EXIF+ Free vs Premium — What Is Gated",
        description="Honest Free vs Premium for EXIF+: single view/edit/remove vs Premium batch multi-select and strip-on-share. Product IDs and limits.",
        h1="Free vs Premium",
        lead="Clear gates based on the shipping iOS UI — not wishlist marketing.",
        prose=f"""        <h2>Available without Premium (current UI)</h2>
        <ul>
          <li>Browse image albums (Recents, Favorites, Screenshots, Selfies, user albums)</li>
          <li>View metadata sections</li>
          <li>Single-photo remove all metadata</li>
          <li>Single-photo edit fields (dates, GPS, camera, author/copyright, descriptions, etc.)</li>
          <li>History of operations (up to 50 items)</li>
        </ul>
        <h2>Premium-gated (current UI)</h2>
        <ul>
          <li>Multi-select <strong>batch remove</strong> / <strong>batch edit</strong> when more than one photo is selected</li>
          <li><strong>Share stripped temporary file</strong> from the photo detail screen</li>
        </ul>
        <h2>Products</h2>
        <ul>
          <li><code>exif.metadata.monthly</code> — monthly subscription</li>
          <li><code>exif.premium.annual</code> — annual subscription (StoreKit config includes a one-week trial)</li>
          <li><code>exif.premium.lifetime</code> — one-time unlock</li>
        </ul>
        <h2>What we will not claim</h2>
        <p>A hard “3 free removals” counter exists in code plumbing but is <strong>not enforced</strong> by current UI call sites. This page describes live gates only. Always check the in-app paywall for the offer you see.</p>
        <p><a href="{APP}">App Store listing</a></p>""",
        faqs=[
            (
                "Is the app download free?",
                "Yes. The App Store listing is free; Premium is an in-app purchase/subscription.",
            ),
            (
                "Do I need Premium to view EXIF?",
                "No.",
            ),
            (
                "Do I need Premium to clean one photo into the library?",
                "No — single-photo remove is available without Premium in the current UI.",
            ),
            (
                "Why did I hit a paywall on share?",
                "Strip-on-share is Premium-gated. Alternative: remove metadata to a new library item, then share that item.",
            ),
            (
                "Restore purchases?",
                "Use Restore on the paywall if you already bought on this Apple ID.",
            ),
        ],
        nav="App",
        parent=("App", "app/"),
        priority=True,
    )

    article_page(
        "app/history",
        title="EXIF+ History — Before & After Metadata Changes",
        description="How EXIF+ History works: before/after comparison for remove and edit actions, 50-item cap, batch entries.",
        h1="History before & after",
        lead="Every clean or edit can be reviewed later — useful when you want proof of what changed.",
        prose=f"""        <h2>What History stores</h2>
        <p>{NAME} keeps recent operations with before/after context for actions such as remove, edit, batch remove, and batch edit. The list is capped (50 items); you can delete entries with swipe.</p>
        <h2>Why it matters for privacy workflows</h2>
        <p>If you cleaned a photo for a marketplace listing, History helps you confirm GPS/camera tags were present before and gone after — without guessing.</p>
        <h2>History vs Photos duplicates</h2>
        <p>History is an in-app log. The Photo Library still holds originals plus new Edited outputs. See <a href="../../learn/why-cleaned-photo-is-a-duplicate/">why cleaned photos look like duplicates</a>.</p>""",
        faqs=[
            (
                "Is History synced to iCloud?",
                "History is maintained by the app’s local persistence — do not assume a separate cross-device History cloud product.",
            ),
            (
                "Does History include failed jobs?",
                "Failures surface as errors during processing; rely on successful completed entries for before/after review.",
            ),
        ],
        nav="App",
        parent=("App", "app/"),
    )

    # ---- Intent landing ----
    article_page(
        "heic-metadata",
        title="HEIC Metadata Viewer & Remover on iPhone | EXIF+",
        description="HEIC metadata: view and remove EXIF/GPS from iPhone HEIC photos with EXIF+. Why online EXIF tools often fail on HEIC and how the app keeps HEIC on save.",
        h1="HEIC metadata on iPhone",
        lead="HEIC metadata is the EXIF/GPS (and related) information inside iPhone HEIC/HEIF photos. Browser tools often cannot open HEIC; EXIF+ works from your Photo Library.",
        prose=f"""        <p><strong>Direct answer:</strong> To view or clean HEIC metadata, use EXIF+ on iPhone. Many online EXIF removers fail because the browser cannot decode HEIC.</p>
        <h2>Why web tools break on HEIC</h2>
        <p>Many browsers cannot decode HEIC for canvas-based removers. That is a browser limitation, not “missing EXIF.”</p>
        <h2>What {NAME} does</h2>
        <ul>
          <li>Opens HEIC/HEIF items from your library</li>
          <li>Shows EXIF/IPTC/GPS-oriented fields</li>
          <li>Removes or edits metadata on-device</li>
          <li>Preserves HEIC/HEIF when saving those formats (PNG stays PNG; other types may become JPEG)</li>
        </ul>
        <h2>Workflow</h2>
        <ol>
          <li>Install {NAME}.</li>
          <li>Grant Photo Library access.</li>
          <li>Open a HEIC photo → view tags → remove or edit → save new item.</li>
        </ol>
        <p>For a JPEG sitting on a laptop, the <a href="../remove-exif/">browser remover</a> is still handy.</p>""",
        faqs=[
            (
                "Can I clean HEIC online here?",
                "Only if your browser can decode it. Most people should use the iPhone app for Camera Roll HEIC.",
            ),
            (
                "Does cleaning convert HEIC to JPEG?",
                "For HEIC inputs, the app’s save path aims to keep HEIC/HEIF. Non-HEIC/PNG types may export as JPEG.",
            ),
            (
                "Live Photos / video?",
                "The app’s library browsing is image-oriented. Video metadata editing is not supported.",
            ),
        ],
        nav="Tools",
        parent=("Tools", "tools/"),
        priority=True,
    )

    article_page(
        "remove-camera-data",
        title="Remove Camera Data from Photos (Make/Model EXIF) | EXIF+",
        description="Remove camera data from photos: strip make, model, lens, and related EXIF device tags online or on iPhone with EXIF+ before you share.",
        h1="Remove camera data from photos",
        lead="Camera data in EXIF can reveal make, model, lens, and software. Remove it with a full metadata strip — or edit those fields in EXIF+ on iPhone.",
        prose=f"""        <p><strong>Direct answer:</strong> To remove camera data from a photo, strip EXIF entirely with the <a href="../remove-exif/">online remover</a> or EXIF+ on iPhone. That also clears GPS and timestamps in a full wipe.</p>
        <h2>What “camera data” usually means</h2>
        <p>Make, model, lens, software, and technical exposure tags. Serial-related fields may appear in the viewer as read-only depending on the file.</p>
        <h2>Fast privacy path</h2>
        <p>Use <strong>remove all metadata</strong> (browser tool or {NAME}) so camera + GPS + timestamps leave together.</p>
        <h2>Selective path</h2>
        <p>In {NAME}’s editor you can change camera make/model/lens/software fields when you need labeling rather than total wipe. Remember: saves create new library items; JPEG/HEIC saves re-encode.</p>""",
        faqs=[
            (
                "How do I remove camera make and model from a photo?",
                "Use a full EXIF remove online or in EXIF+, or edit the camera fields in the iPhone app if you only need those tags changed.",
            ),
            (
                "Is camera model sensitive?",
                "Sometimes — for example when you do not want a public post tied to expensive gear or a unique device fingerprint.",
            ),
            (
                "Does removing camera data also remove GPS?",
                "A full metadata remove does. Selective camera-field edits do not automatically clear location unless you also clear GPS.",
            ),
            (
                "Does Instagram remove camera EXIF?",
                "Often social uploads strip many tags, but other channels keep them. Clean before you send originals.",
            ),
        ],
        nav="Tools",
        parent=("Tools", "tools/"),
    )

    # ---- Trends-driven pages (photo metadata / find EXIF / Discord) ----
    article_page(
        "how-to/find-exif-data",
        title="How to Find EXIF Data on a Photo (Check & Read) | EXIF+",
        description="How to find, check, and read EXIF data on a photo: online EXIF viewer for desktop files, or EXIF+ on iPhone for Camera Roll / HEIC.",
        h1="How to find EXIF data",
        lead="EXIF is hidden inside the file — here is how to find, check, and read it on a computer or iPhone.",
        prose=f"""        <p><strong>Direct answer:</strong> To find EXIF data, open the photo in an EXIF viewer. On a computer use the <a href="../../exif-viewer/">online EXIF viewer</a> or <a href="../../photo-metadata-viewer/">photo metadata viewer</a>; on iPhone use {NAME} for Photo Library items.</p>
        <h2>On a computer (JPEG / PNG / WebP)</h2>
        <ol>
          <li>Open the <a href="../../exif-viewer/">online EXIF viewer</a>.</li>
          <li>Choose the image file.</li>
          <li>Read the listed fields: date, camera, GPS, and other tags the parser returns.</li>
        </ol>
        <p>Processing stays in your browser tab — the file is not uploaded to our servers for this tool.</p>
        <h2>On iPhone (including HEIC)</h2>
        <ol>
          <li>Install {NAME} and allow Photo Library access.</li>
          <li>Open the photo from an album.</li>
          <li>Scroll metadata sections (date, location, camera, author, GPS details).</li>
        </ol>
        <p>Apple Photos shows limited info; {NAME} is built to surface fuller field groups. Step-by-step: <a href="../view-exif-on-iphone/">view EXIF on iPhone</a>.</p>
        <h2>What to do after you find sensitive tags</h2>
        <ul>
          <li><a href="../../remove-exif/">Strip EXIF online</a> for a desktop file</li>
          <li><a href="../remove-photo-metadata-iphone/">Remove photo metadata on iPhone</a> for library items</li>
          <li><a href="../../remove-gps/">Remove GPS only</a> if location is the main concern</li>
        </ul>""",
        faqs=[
            (
                "How do I check if a photo has EXIF data?",
                "Open it in an EXIF / photo metadata viewer. If fields like Date Taken, Make/Model, or GPS appear, the file still carries metadata.",
            ),
            (
                "How do I read EXIF data without installing software?",
                "Use the browser EXIF viewer on this site for JPEG/PNG/WebP. For iPhone HEIC library photos, use the EXIF+ app.",
            ),
            (
                "Why can’t I find EXIF in Photos on iPhone?",
                "Photos shows only a short summary. Full tag groups need a dedicated viewer like EXIF+.",
            ),
            (
                "Does finding EXIF change the photo?",
                "No. Viewing is read-only. Removing or editing creates a new file or library item.",
            ),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
        priority=True,
    )

    article_page(
        "how-to/remove-photo-metadata-iphone",
        title="How to Remove Photo Metadata on iPhone | EXIF+",
        description="Remove photo metadata on iPhone with EXIF+: strip EXIF, IPTC, and GPS from Camera Roll / HEIC photos. Single-photo free; batch is Premium.",
        h1="Remove photo metadata on iPhone",
        lead="iPhone photo metadata often includes EXIF camera tags, timestamps, and GPS. Strip it on-device before you share.",
        prose=f"""        <p><strong>Direct answer:</strong> To remove photo metadata on iPhone, open the photo in {NAME}, run remove metadata, and share the <strong>new</strong> library item — not the original.</p>
        <h2>What iPhone photo metadata usually includes</h2>
        <ul>
          <li>Capture date/time</li>
          <li>Device make/model and camera settings</li>
          <li>GPS / location when Location Services were on</li>
          <li>Author/copyright fields if previously written</li>
        </ul>
        <h2>Steps (single photo)</h2>
        <ol>
          <li>Install {NAME} from the App Store and allow Photo Library access.</li>
          <li>Open the photo and review metadata sections.</li>
          <li>Choose remove metadata (full wipe) or edit/clear only the sensitive fields.</li>
          <li>Save — {NAME} writes a new Photo Library item.</li>
          <li>Share that new item (or use Premium strip-on-share from the detail screen).</li>
        </ol>
        <h2>Batch albums</h2>
        <p>Multi-select batch remove is <strong>Premium</strong>. Single-photo remove is available without Premium in the current UI. See <a href="../../app/free-vs-premium/">Free vs Premium</a>.</p>
        <h2>Browser alternative</h2>
        <p>For a JPEG on a laptop, use the <a href="../../metadata-cleaner/">photo metadata cleaner</a> or <a href="../../remove-exif/">strip EXIF</a> tool. HEIC Camera Roll items are best handled in the app.</p>
        <p>Related: <a href="../remove-location-from-photos-iphone/">remove location only</a>, <a href="../share-photo-without-metadata/">share without metadata</a>.</p>""",
        faqs=[
            (
                "How do I remove photo metadata from an iPhone photo?",
                "Use EXIF+: open the photo, remove metadata (or clear fields), save the new library item, then share that copy.",
            ),
            (
                "Is remove photo metadata the same as remove GPS?",
                "GPS/location is one part. Full metadata remove also clears camera tags, timestamps, and other EXIF/IPTC fields the wipe covers.",
            ),
            (
                "Does this overwrite the original?",
                "No. EXIF+ saves a new item. The original keeps its tags until you delete or edit it separately.",
            ),
            (
                "Will quality drop?",
                "JPEG/HEIC saves re-encode at high quality. Metadata removal is not a visual filter, but it is not a bit-identical lossless promise either.",
            ),
            (
                "Can I do this for many photos?",
                "Yes with Premium multi-select batch remove.",
            ),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
        priority=True,
    )

    article_page(
        "learn/does-discord-remove-exif",
        title="Does Discord Remove EXIF Data? | EXIF+",
        description="Normal Discord chat uploads are often re-encoded and frequently drop EXIF and GPS. Send-as-file can keep the original metadata — Discord is not a privacy guarantee.",
        h1="Does Discord remove EXIF?",
        lead="Normal Discord chat uploads are often re-encoded, which frequently drops EXIF and GPS. Sending as a file can keep the original bytes — including metadata — so Discord is not a privacy guarantee.",
        prose="""        <p><strong>Direct answer:</strong> Normal Discord chat uploads are often re-encoded, which frequently drops EXIF and GPS. Sending as a file can keep the original bytes — including metadata — so Discord is not a privacy guarantee.</p>
        <h2>Why answers online disagree</h2>
        <p>Discord compresses many inline images for size. That re-encode often strips EXIF/GPS. That is not a documented “we always delete all metadata” promise for every path, client, or bot.</p>
        <h2>Risky paths</h2>
        <ul>
          <li>Send as file / attachment modes that preserve the original bytes</li>
          <li>Cloud links to an uncleaned original</li>
          <li>Assuming every server, bot, or client behaves the same</li>
        </ul>
        <h2>Safe workflow</h2>
        <p>Clean first, then upload: use the <a href="../../remove-exif/">strip EXIF</a> tool, <a href="../../metadata-cleaner/">metadata cleaner</a>, or <a href="../../how-to/remove-photo-metadata-iphone/">remove photo metadata on iPhone</a>. Same advice as for <a href="../does-instagram-remove-exif/">Instagram</a> — destination behavior is a bonus, not your control.</p>""",
        faqs=[
            (
                "Does Discord remove EXIF?",
                "Often on compressed chat image uploads, because Discord re-encodes those files. It is not a guarantee: send-as-file and some clients can keep EXIF and GPS.",
            ),
            (
                "Does Discord always strip metadata?",
                "No. Do not treat Discord as a cleaner. If location or camera tags matter, strip them before you upload.",
            ),
            (
                "Does Discord remove GPS metadata?",
                "Often yes on compressed chat image uploads — but do not rely on it. Clean the file yourself if location privacy matters.",
            ),
            (
                "If I send a photo as a file on Discord, is EXIF kept?",
                "File-style sends are more likely to preserve original bytes (and metadata) than compressed inline images. Clean first when unsure.",
            ),
            (
                "Is Discord safer than email for EXIF?",
                "Not reliably. Email attachments frequently keep metadata; Discord is inconsistent by send mode. Cleaning removes the guesswork.",
            ),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
        priority=True,
    )
