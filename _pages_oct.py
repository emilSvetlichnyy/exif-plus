"""Pages added from the 2026-10 SEO/GEO audit (GSC + Google Trends). Claim-safe, same rules as _pages_extra."""
from __future__ import annotations

UPDATED = "2026-10-12"


def register_oct(ns: dict) -> None:
    article_page = ns["article_page"]
    tool_page = ns["tool_page"]
    NAME = ns["NAME"]
    BASE = ns["BASE"]

    # ---- Tool: image metadata viewer (Trends: "image metadata" > "exif data") ----
    tool_page(
        "image-metadata-viewer",
        title="Image Metadata Viewer Online — Check Location & Remove Metadata | EXIF+",
        description="Free image metadata viewer: see what a JPEG, PNG or WebP reveals — location, date, camera, software — then remove it. Runs in your browser, no upload to our servers.",
        h1="Image metadata viewer",
        lead="See what an image reveals before you share it: location, date taken, camera, and software tags — then remove it.",
        mode="view",
        tool_title="Image metadata viewer",
        tool_blurb="Choose an image to list readable metadata fields locally.",
        sections_html="""      <section class="section prose">
        <p><strong>Direct answer:</strong> An image metadata viewer lists the hidden data stored inside an image file — mostly EXIF (camera, date, GPS), sometimes IPTC (author, caption, copyright). Choose a file above and the fields are read in your browser tab.</p>
        <h2>How do I check image metadata location?</h2>
        <p>Look for GPS latitude and longitude in the results. If they are present, anyone who gets the original file can place the photo on a map. If they are missing, location services were off, or an app already removed them.</p>
        <h2>How do I remove image metadata?</h2>
        <p>Use <a href="../remove-exif/">strip EXIF online</a> for a clean download, or <a href="../remove-gps/">remove GPS only</a>. On iPhone, <a href="../how-to/remove-photo-metadata-iphone/">remove photo metadata</a> from your library with EXIF+.</p>
        <h2>Which file types work?</h2>
        <p>JPEG, PNG and WebP in the browser. HEIC from an iPhone is often not decodable in browsers — use the <a href="../heic-metadata/">HEIC metadata</a> workflow in the app. Metadata inside PDFs and videos is outside this tool: see <a href="../learn/pdf-video-png-metadata/">PDF, video and PNG metadata</a>.</p>
        <h2>Related viewers</h2>
        <p><a href="../exif-viewer/">EXIF viewer</a> · <a href="../photo-metadata-viewer/">Photo metadata viewer</a> · <a href="../how-to/find-exif-data/">How to check photo metadata</a></p>
      </section>""",
        faqs=[
            ("How do I check image metadata?", "Open this page, choose a JPEG, PNG or WebP, and read the listed fields. Processing stays in your browser tab."),
            ("Can image metadata show where a photo was taken?", "Yes, if GPS coordinates are stored in the file. Many phone photos include them unless location was off or they were stripped."),
            ("How do I remove metadata from an image?", "Use the EXIF remover on this site for a cleaned download, or EXIF+ on iPhone for Photo Library items."),
            ("Is image metadata the same as EXIF?", "EXIF is the most common kind. IPTC (captions, author, copyright) can also be present in the same file."),
            ("Are my images uploaded?", "Not to our servers for this tool: the file is read locally in your browser."),
        ],
        crumbs=[("Home", f"{BASE}/"), ("Image metadata viewer", f"{BASE}/image-metadata-viewer/")],
        og="photo-metadata-viewer.png",
    )

    # ---- Platform cluster: Facebook / X / Reddit (same template as Discord) ----
    others = '<p>Other platforms: <a href="../does-instagram-remove-exif/">Instagram</a>, <a href="../does-discord-remove-exif/">Discord</a>, <a href="../does-whatsapp-remove-exif/">WhatsApp</a>, <a href="../does-telegram-remove-exif/">Telegram</a>, <a href="../does-imessage-remove-location/">iMessage &amp; AirDrop</a>. Full list: <a href="../which-apps-remove-photo-metadata/">which apps remove photo metadata</a>.</p>'

    def platform(slug: str, label: str, short: str, extra: str) -> None:
        article_page(
            f"learn/does-{slug}-remove-exif",
            title=f"Does {label} Remove EXIF & Metadata From Photos? | EXIF+",
            description=f"Does {label} remove EXIF and GPS from photos? Usually the public copy is re-encoded, but it is not a guarantee, and the service can still receive the original data on upload.",
            h1=f"Does {label} remove EXIF?",
            lead=short,
            updated=UPDATED,
            prose=f"""        <p><strong>Direct answer:</strong> {short}</p>
        <h2>Two different questions</h2>
        <ul>
          <li><strong>Can other people read my photo's location from {label}?</strong> Usually the copy shown to others is re-encoded and often loses EXIF/GPS, but this is not a promise we can verify for every upload path, app version or download route.</li>
          <li><strong>Does {label} itself see the metadata?</strong> Assume yes. The file you upload arrives with its metadata first; any cleanup happens afterwards on the service's side.</li>
        </ul>
        <h2>What is not covered</h2>
        {extra}
        <h2>Safe workflow</h2>
        <p>Clean first, then upload: <a href="../../remove-exif/">strip EXIF online</a>, the <a href="../../remove-gps/">GPS remover</a>, or <a href="../../how-to/remove-photo-metadata-iphone/">remove photo metadata on iPhone</a>. Cleaning the file yourself works the same on every platform.</p>
        {others}""",
            faqs=[
                (f"Does {label} remove EXIF data?", f"The public copy is commonly re-encoded and often loses EXIF and GPS, but {label} does not give a guarantee for every upload path. Clean the file before uploading if privacy matters."),
                (f"Does {label} remove location data from photos?", "Often for the displayed copy, but not reliably for every route. The original upload still reaches the service with its metadata."),
                (f"Can someone get metadata from a photo I post on {label}?", "Possibly, if the file they download still carries it. Do not rely on the platform: remove metadata before posting."),
                ("What is the safest way to post a photo without location?", "Strip EXIF/GPS yourself first, then upload the cleaned copy."),
            ],
            nav="Learn",
            parent=("Learn", "learn/"),
        )

    platform(
        "facebook",
        "Facebook",
        "Facebook usually re-encodes uploaded photos, so the copy other people see often loses EXIF and GPS — but it is not a guarantee, and Facebook still receives the original metadata on upload.",
        "<p>Photos sent as originals or documents in chats, files shared outside the main feed pipeline, and photos downloaded from other sources may behave differently. Treat each route separately.</p>",
    )
    platform(
        "twitter-x",
        "X (Twitter)",
        "X usually re-encodes uploaded images, so the public copy often loses EXIF and GPS — but it is not a guarantee, and X still receives the original metadata on upload.",
        "<p>Behavior can differ by app version, upload method and media type (photo, GIF, video). Direct-message attachments and linked originals are separate routes.</p>",
    )
    platform(
        "reddit",
        "Reddit",
        "Reddit typically re-processes uploaded images, so the public copy often loses EXIF and GPS — but it is not a guarantee, and Reddit still receives the original metadata on upload. Links to images hosted elsewhere keep whatever that host serves.",
        "<p>An image you link from another host (cloud storage, a personal site) is served exactly as stored there, metadata included.</p>",
    )

    # ---- Comparison table page ----
    article_page(
        "learn/which-apps-remove-photo-metadata",
        title="Which Apps Remove Photo Metadata? Instagram, WhatsApp, Discord & More | EXIF+",
        description="Which apps strip EXIF and GPS from photos you send or post? A plain comparison of common apps, with links to details. None is a guarantee — clean the file first.",
        h1="Which apps remove photo metadata?",
        lead="Many apps re-encode photos and drop EXIF/GPS from the copy others see — but none is a guarantee. Here is how the common ones compare and where the risk is.",
        updated=UPDATED,
        prose="""        <p><strong>Direct answer:</strong> Several big apps re-encode photos you upload, which often removes EXIF and GPS from the shared copy. Sending the same photo as a file or document usually keeps the original bytes and metadata. Because behavior varies by app version and route, remove metadata yourself before sharing.</p>
        <h2>Comparison</h2>
        <table>
          <thead><tr><th>App</th><th>What usually matters</th><th>Details</th></tr></thead>
          <tbody>
            <tr><td>Instagram</td><td>Feed pipeline re-encodes uploads</td><td><a href="../does-instagram-remove-exif/">Read</a></td></tr>
            <tr><td>Facebook</td><td>Public copy re-encoded; original reaches the service</td><td><a href="../does-facebook-remove-exif/">Read</a></td></tr>
            <tr><td>X (Twitter)</td><td>Public copy re-encoded; original reaches the service</td><td><a href="../does-twitter-x-remove-exif/">Read</a></td></tr>
            <tr><td>Reddit</td><td>Uploads re-processed; external links keep metadata</td><td><a href="../does-reddit-remove-exif/">Read</a></td></tr>
            <tr><td>Discord</td><td>Chat image vs send-as-file</td><td><a href="../does-discord-remove-exif/">Read</a></td></tr>
            <tr><td>Telegram</td><td>Photo vs send-as-file</td><td><a href="../does-telegram-remove-exif/">Read</a></td></tr>
            <tr><td>WhatsApp</td><td>Photo vs Document</td><td><a href="../does-whatsapp-remove-exif/">Read</a></td></tr>
            <tr><td>iMessage &amp; AirDrop</td><td>Share-sheet Options toggle for location</td><td><a href="../does-imessage-remove-location/">Read</a></td></tr>
          </tbody>
        </table>
        <h2>The rule that always works</h2>
        <p>Clean the file before it leaves your device: <a href="../../remove-exif/">strip EXIF online</a>, <a href="../../remove-gps/">remove GPS only</a>, or <a href="../../how-to/share-photo-without-metadata/">share without metadata on iPhone</a>.</p>""",
        faqs=[
            ("Which apps remove EXIF from photos?", "Many social apps re-encode uploads, which often drops EXIF and GPS from the public copy. Behavior is not guaranteed and differs by route (photo vs file)."),
            ("Does sending a photo as a file keep metadata?", "Usually yes, because file or document sends tend to preserve the original bytes."),
            ("Do these apps see my photo's location?", "Assume the service receives the original upload with its metadata, even if the copy others see is cleaned."),
            ("What is the safest approach?", "Remove metadata yourself before sharing, then check the result with a metadata viewer."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
        priority=True,
    )

    # ---- AI image metadata / C2PA ----
    article_page(
        "learn/ai-image-metadata-c2pa",
        title="AI Image Metadata & C2PA Content Credentials Explained | EXIF+",
        description="What metadata do AI-generated images carry? EXIF, text chunks and C2PA Content Credentials explained in plain language — and what removing EXIF does and does not do.",
        h1="AI image metadata and C2PA, explained",
        lead="AI-generated images can carry metadata that says how they were made. Some of it is ordinary EXIF-style data; some is signed provenance called C2PA Content Credentials.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> AI image metadata is information stored in an image file about how it was made — for example a generator or software name, a prompt in a text field, or signed C2PA Content Credentials. Ordinary EXIF can be viewed and removed with a metadata tool; C2PA is a separate signed record.</p>
        <h2>What is C2PA?</h2>
        <p>C2PA (Coalition for Content Provenance and Authenticity) is an open standard for attaching a signed history to a file — who or what created it and which edits were made. The user-facing name is Content Credentials. It is stored inside the file, but it is not the same as EXIF.</p>
        <h2>Where else can AI info appear?</h2>
        <ul>
          <li><strong>Software/Make fields in EXIF</strong> naming the tool that produced or saved the file.</li>
          <li><strong>PNG text chunks and XMP</strong> where some generators write settings or prompts.</li>
          <li><strong>C2PA manifests</strong> when the generator or editor supports Content Credentials.</li>
        </ul>
        <h2>Does removing EXIF remove C2PA?</h2>
        <p>Not necessarily as a promise. Re-encoding or stripping a file can remove embedded credentials, but that depends on the tool and the file. Metadata can also be missing simply because a platform stripped it, so its absence does not prove an image is real or fake.</p>
        <h2>What {NAME} does and does not do</h2>
        <p>{NAME} reads and edits EXIF, IPTC and GPS on your iPhone. It does <strong>not</strong> verify C2PA signatures or detect AI images. To see which basic fields an image carries, use the <a href="../../image-metadata-viewer/">image metadata viewer</a>.</p>""",
        faqs=[
            ("Do AI images have EXIF data?", "Sometimes. Some tools write a software name or settings into metadata fields; many images have little or none."),
            ("What is C2PA metadata?", "A signed provenance record (Content Credentials) describing how a file was created and edited. It is separate from EXIF."),
            ("Can I tell if an image is AI-generated from metadata?", "Metadata can be a hint, but it is easy to strip, so a missing tag proves nothing."),
            ("Does removing EXIF remove Content Credentials?", "Not guaranteed. It depends on the tool and file. EXIF+ does not verify or manage C2PA."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    # ---- Screenshot metadata ----
    article_page(
        "learn/does-screenshot-have-exif",
        title="Do Screenshots Have Metadata? EXIF in Screenshots | EXIF+",
        description="Do screenshots contain EXIF or location data? Usually far less than a camera photo, but not nothing. What a screenshot can reveal and how to check it.",
        h1="Do screenshots have metadata?",
        lead="A screenshot usually carries much less than a camera photo — no lens or GPS from a camera — but it is not guaranteed to be empty.",
        updated=UPDATED,
        prose="""        <p><strong>Direct answer:</strong> Screenshots typically do not include the GPS coordinates or camera settings a photo has, because nothing was captured by a camera. They can still include a creation date, the device or software name, and dimensions. The pixels themselves can also reveal more than any tag.</p>
        <h2>What a screenshot may contain</h2>
        <ul>
          <li>Date and time created, and image dimensions</li>
          <li>Device or software information, depending on the system</li>
          <li>Text visible on screen — names, messages, addresses — which is the bigger privacy risk</li>
        </ul>
        <h2>How to check</h2>
        <p>Drop the file into the <a href="../../image-metadata-viewer/">image metadata viewer</a>. If any field is sensitive, <a href="../../remove-exif/">strip EXIF online</a>. For an iPhone screenshot in your library, use <a href="../../how-to/view-exif-on-iphone/">view EXIF on iPhone</a>.</p>
        <h2>Before you share one</h2>
        <p>Crop out notification banners, account names and addresses first. Removing metadata does not hide what is visible in the image.</p>""",
        faqs=[
            ("Do screenshots have EXIF data?", "Often a little, such as date and device software, but usually no camera settings and no GPS."),
            ("Can a screenshot show my location?", "Not through GPS tags in most cases, but visible content on screen can."),
            ("How do I check screenshot metadata?", "Open the file in a metadata viewer and read the listed fields."),
            ("Should I remove metadata from screenshots?", "It is a cheap extra step, but cropping private details matters more."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    # ---- PDF / video / PNG ----
    article_page(
        "learn/pdf-video-png-metadata",
        title="PDF, Video & PNG Metadata Viewers: What Each File Type Stores | EXIF+",
        description="What metadata do PDF, video, PNG and JPEG files store, and how to check each? Plain explanation, plus what EXIF+ does and does not cover.",
        h1="PDF, video and PNG metadata: what each stores",
        lead="Metadata is not only for photos. PDFs, videos and PNGs carry their own fields — here is what is in each and where it fits with EXIF+.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> JPEG photos mainly use EXIF/IPTC; PNG uses text chunks (and sometimes EXIF); PDFs store document properties such as author, title and creation tool; videos store container tags such as creation time and sometimes location. The tools on this site read images; they do not read PDFs or video.</p>
        <h2>JPEG, HEIC, WebP</h2>
        <p>Camera, date and GPS in EXIF; captions and copyright in IPTC. Check with the <a href="../../image-metadata-viewer/">image metadata viewer</a>.</p>
        <h2>PNG</h2>
        <p>PNG has no standard camera EXIF block in most files, but can hold text chunks and, in some files, EXIF. Screenshots and generated images are often PNG: see <a href="../does-screenshot-have-exif/">screenshot metadata</a> and <a href="../ai-image-metadata-c2pa/">AI image metadata</a>.</p>
        <h2>PDF</h2>
        <p>Open the document properties in your PDF reader to see author, title, creation tool and dates. {NAME} and the browser tools here do not process PDFs.</p>
        <h2>Video</h2>
        <p>Videos can store creation time and, from phones, sometimes location. {NAME} does <strong>not</strong> edit video metadata.</p>""",
        faqs=[
            ("How do I view PDF metadata?", "Open Document Properties in your PDF reader to see author, title, creation tool and dates."),
            ("Does PNG have EXIF?", "Not usually in the camera sense. It can have text chunks and, in some files, an EXIF block."),
            ("Does EXIF+ edit video metadata?", "No. EXIF+ works on photo metadata (EXIF, IPTC, GPS)."),
            ("Which tool should I use for photos?", "The image metadata viewer here for desktop files, or EXIF+ on iPhone."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    # ---- Compare: viewer alternatives ----
    article_page(
        "compare/exif-viewer-alternatives",
        title="EXIF Viewer Alternatives: ExifTool, Jeffrey's, Jimpl, Metadata2go & EXIF+ | EXIF+",
        description="Comparing ways to read photo metadata: command-line ExifTool, online viewers like Jeffrey's, Jimpl and Metadata2go, and EXIF+. How to choose, with privacy questions to ask.",
        h1="EXIF viewer alternatives: how to choose",
        lead="There are several ways to read photo metadata. The right one depends on whether you need depth, speed, privacy or an iPhone workflow.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> For the deepest tag list and scripting, ExifTool (a free command-line program) is the long-standing choice. For a quick look in a browser, use an online viewer. For iPhone Photo Library and HEIC, use a native app such as {NAME}. Check each online tool's own privacy statement to learn whether files are uploaded.</p>
        <h2>Options at a glance</h2>
        <table>
          <thead><tr><th>Option</th><th>Best for</th><th>Question to ask</th></tr></thead>
          <tbody>
            <tr><td>ExifTool</td><td>Deep tag lists, batch scripts on a computer</td><td>Comfortable with a command line?</td></tr>
            <tr><td>Jeffrey's Image Metadata Viewer</td><td>Detailed online report for a file or URL</td><td>Does it fetch or upload the file?</td></tr>
            <tr><td>Jimpl, Metadata2go</td><td>Quick online lookups</td><td>Is the file uploaded to a server?</td></tr>
            <tr><td><a href="../../image-metadata-viewer/">EXIF+ web viewer</a></td><td>Reading JPEG/PNG/WebP locally in the browser, then removing</td><td>Not for HEIC in most browsers</td></tr>
            <tr><td>{NAME} on iPhone</td><td>Photo Library, HEIC, edit and batch remove</td><td>Needs an iPhone</td></tr>
          </tbody>
        </table>
        <p>We describe other tools only by their general purpose; check their sites for current features and privacy terms.</p>
        <h2>Choosing</h2>
        <ul>
          <li>Privacy first: pick a viewer that reads the file locally, like <a href="../../exif-viewer/">this EXIF viewer</a>.</li>
          <li>iPhone photos: <a href="../../heic-metadata/">HEIC metadata</a> in the app.</li>
          <li>Need to edit, not only read: <a href="../remove-vs-edit-exif/">remove vs edit EXIF</a>.</li>
        </ul>""",
        faqs=[
            ("What is the best free EXIF viewer?", "It depends on the job: ExifTool for depth, an online viewer for speed, and a local browser viewer or iPhone app when privacy matters."),
            ("Is ExifTool an EXIF viewer?", "Yes. It is a free command-line program that reads and writes metadata in many file types."),
            ("Do online EXIF viewers upload my photo?", "Some do and some read it locally. Check each tool's privacy statement. The viewer on this site reads files locally."),
            ("What is the best EXIF viewer for iPhone?", f"{NAME} reads Photo Library items including HEIC and can edit or remove metadata."),
        ],
        nav="Compare",
        parent=("Compare", "compare/"),
    )

    # ---- How-to: Mac / Windows / Android ----
    article_page(
        "how-to/remove-photo-metadata-mac-windows",
        title="How to Remove Photo Metadata on Mac, Windows & Android | EXIF+",
        description="Remove EXIF and location from photos on Mac, Windows or Android: built-in steps, plus a browser tool that strips metadata locally. Step by step.",
        h1="How to remove photo metadata on Mac, Windows and Android",
        lead="Each system can remove some metadata itself. A browser tool covers the rest on any device.",
        updated=UPDATED,
        prose="""        <p><strong>Direct answer:</strong> On Windows use File Properties → Details → Remove Properties and Personal Information. On Mac, open the photo in Preview and remove location info in the Inspector. On any device, including Android, use the <a href="../../remove-exif/">strip EXIF online</a> tool to download a clean copy.</p>
        <h2>Windows</h2>
        <ol>
          <li>Right-click the photo → Properties → Details.</li>
          <li>Click “Remove Properties and Personal Information”.</li>
          <li>Choose a cleaned copy or remove from the original, then confirm.</li>
        </ol>
        <h2>Mac</h2>
        <ol>
          <li>Open the photo in Preview.</li>
          <li>Tools → Show Inspector → the GPS tab.</li>
          <li>Choose “Remove Location Info”, then save.</li>
        </ol>
        <p>This targets location. For camera and other tags, use the browser tool.</p>
        <h2>Android and any browser</h2>
        <ol>
          <li>Open <a href="../../remove-exif/">strip EXIF online</a> in your browser.</li>
          <li>Choose the photo (JPEG, PNG or WebP).</li>
          <li>Download the cleaned copy and share that one.</li>
        </ol>
        <p>Processing stays in your browser tab. Check the result in the <a href="../../image-metadata-viewer/">image metadata viewer</a>. On iPhone see <a href="../remove-photo-metadata-iphone/">remove photo metadata on iPhone</a>.</p>""",
        faqs=[
            ("How do I remove EXIF data on Windows?", "Right-click the file → Properties → Details → Remove Properties and Personal Information."),
            ("How do I remove location from a photo on Mac?", "Open it in Preview → Tools → Show Inspector → GPS tab → Remove Location Info."),
            ("How do I remove metadata on Android?", "Use a browser-based EXIF remover to download a cleaned copy."),
            ("How can I confirm the metadata is gone?", "Open the cleaned file in a metadata viewer."),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
    )
