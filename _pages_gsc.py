"""Pages added 2026-11-19 from real Search Console queries (github.io property, 90 days) where we rank 5-95 with no dedicated page.

Each page targets queries that actually appeared in GSC. Search volumes are small (single/double digit impressions per query),
so these are long-tail pages: low competition, low volume. No claim of own tests; claim-safe per product-knowledge.json.
"""
from __future__ import annotations

UPDATED = "2026-11-19"
CHECKED = "Checked 19 Nov 2026."


def register_gsc(ns: dict) -> None:
    article_page = ns["article_page"]
    NAME = ns["NAME"]

    def src(*links: tuple[str, str]) -> str:
        items = "; ".join(f'<a href="{u}" rel="noopener">{t}</a>' for t, u in links)
        return f"<p><small>Sources: {items}. {CHECKED}</small></p>"

    # 1 -------------------------------------------------------------
    article_page(
        "learn/exchangeable-image-file-format",
        title="Exchangeable Image File Format (EXIF): Full Form, History, Versions | EXIF+",
        description="EXIF stands for Exchangeable Image File Format. What it is, who created it, which versions exist and what it means for your photos.",
        h1="Exchangeable Image File Format (EXIF): full form and meaning",
        lead="EXIF means Exchangeable Image File Format: a standard for storing camera and shot details inside image files.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> <strong>EXIF</strong> is short for <strong>Exchangeable Image File Format</strong>. It is a specification that defines how a camera or phone writes extra information (device, settings, time, optionally GPS) into JPEG, TIFF and similar image files. The word is also used for the data itself: "the photo's EXIF".</p>
        <h2>Key facts</h2>
        <table>
          <thead><tr><th>Item</th><th>Detail</th></tr></thead>
          <tbody>
            <tr><td>Full form</td><td>Exchangeable Image File Format</td></tr>
            <tr><td>First published</td><td>1995, by the Japan Electronic Industries Development Association (JEIDA, now part of JEITA)</td></tr>
            <tr><td>Maintained by</td><td>CIPA and JEITA</td></tr>
            <tr><td>Latest major version</td><td>Exif 3.0 (2023), which adds UTF-8 text support</td></tr>
            <tr><td>Stored in</td><td>JPEG (APP1 segment), TIFF, HEIF/HEIC and others</td></tr>
            <tr><td>Typical content</td><td>Make, model, exposure, date and time, GPS, orientation, thumbnail</td></tr>
          </tbody>
        </table>
        <h2>"EXIF data" in plain words</h2>
        <p>It is the hidden label attached to a photo. You do not see it in the picture, but software can read it. That is why a photo can carry the place and time it was taken. See the <a href="../exif-tags-cheat-sheet/">tags cheat sheet</a> and <a href="../what-is-exif/">what is EXIF</a>.</p>
        <h2>What is EXIF used for?</h2>
        <ul>
          <li>Photo apps use it to sort pictures by date and rotate them the right way.</li>
          <li>Photographers read exposure, ISO and lens to learn from a shot.</li>
          <li>Maps and galleries use the GPS tags to place photos on a map.</li>
          <li>Privacy checks use it to see what a photo reveals before sharing: <a href="../is-exif-data-a-privacy-risk/">is EXIF data a privacy risk?</a></li>
        </ul>
        <h2>Is it the same as IPTC?</h2>
        <p>No. EXIF is mostly written by the device. IPTC holds descriptive text such as caption and copyright: <a href="../exif-vs-iptc/">EXIF vs IPTC</a>.</p>
        <p>To read yours, use the <a href="../../exif-viewer/">browser EXIF viewer</a> or {NAME} on iPhone.</p>
        {src(("Exif (Wikipedia)", "https://en.wikipedia.org/wiki/Exif"), ("ExifTool EXIF tags", "https://exiftool.org/TagNames/EXIF.html"))}""",
        faqs=[
            ("What is the full form of EXIF?", "Exchangeable Image File Format."),
            ("Who created EXIF?", "The Japan Electronic Industries Development Association (JEIDA) published the first version in 1995. It is now maintained by CIPA and JEITA."),
            ("What does EXIF data mean?", "It is the camera and shot information stored inside a photo file: device, settings, time and optional GPS."),
            ("Is EXIF only for JPEG?", "No. It is also used in TIFF and HEIF/HEIC files."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    # 2 -------------------------------------------------------------
    article_page(
        "learn/exif-image-unique-id",
        title="EXIF ImageUniqueID: What the Image Unique ID Tag Is | EXIF+",
        description="ImageUniqueID is an EXIF tag that can give each image an identifier. What it contains, which cameras write it, and whether to remove it.",
        h1="EXIF ImageUniqueID (image unique ID)",
        lead="ImageUniqueID is an optional EXIF tag meant to identify one image. Many phones leave it empty.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> <strong>ImageUniqueID</strong> (tag 0xA420) is an optional EXIF field that holds a 32-character hexadecimal string intended to be unique to one image. Whether it is written depends on the camera or app; many phones and tools do not write it. If it is present, copies of the file carry the same value.</p>
        <table>
          <thead><tr><th>Question</th><th>Answer</th></tr></thead>
          <tbody>
            <tr><td>Tag name</td><td>ImageUniqueID</td></tr>
            <tr><td>Tag number</td><td>0xA420 (EXIF IFD)</td></tr>
            <tr><td>Format</td><td>ASCII text, 32 hex characters plus terminator</td></tr>
            <tr><td>Written by</td><td>Some cameras and editing software; not guaranteed</td></tr>
            <tr><td>Privacy angle</td><td>Can link copies of the same file; does not contain your name or location</td></tr>
          </tbody>
        </table>
        <h2>Should you remove it?</h2>
        <p>If you want unlinkable copies, remove all metadata before sharing. {NAME} can remove EXIF, IPTC and GPS in one action and saves the result as a new photo. Check what a file holds with the <a href="../../exif-viewer/">EXIF viewer</a>.</p>
        <p>Related: <a href="../exif-tags-cheat-sheet/">EXIF tags cheat sheet</a>, <a href="../what-is-exif/">what is EXIF</a>.</p>
        {src(("ExifTool EXIF tags", "https://exiftool.org/TagNames/EXIF.html"))}""",
        faqs=[
            ("What is Image Unique ID in EXIF?", "An optional tag with a 32-character hex string meant to identify an image."),
            ("Does every photo have an Image Unique ID?", "No. It is optional and many phones do not write it."),
            ("Does the Image Unique ID reveal my identity?", "Not by itself. It can link copies of the same file, but it holds no name or location."),
            ("How do I remove it?", "Remove all metadata with a metadata remover; selective removal of this tag needs a tool such as ExifTool."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    # 3 -------------------------------------------------------------
    article_page(
        "how-to/read-exif-data-from-image",
        title="How to Read EXIF Data From an Image: 6 Ways | EXIF+",
        description="How to read EXIF data from a photo on iPhone, Windows, Mac, Android, in a browser, and with ExifTool. Pick the way that fits your device.",
        h1="How to read EXIF data from an image",
        lead="Six ways to read the EXIF in a photo, from a right-click to a command line.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> The fastest way on any device is to drop the file into a browser EXIF viewer. On a computer you can also use file properties (Windows) or Preview (Mac). On iPhone, use Photos for the basics or an app such as {NAME} for the full list. For every tag, use ExifTool.</p>
        <table>
          <thead><tr><th>Where</th><th>How</th><th>Shows</th></tr></thead>
          <tbody>
            <tr><td>Any browser</td><td>Open the <a href="../../exif-viewer/">EXIF viewer</a>, add a JPEG, PNG or WebP</td><td>Most tags, read locally</td></tr>
            <tr><td>iPhone</td><td>Swipe up on a photo in Photos; or use {NAME}</td><td>Basics; full list in the app</td></tr>
            <tr><td>Windows</td><td>Right-click → Properties → Details</td><td>Camera, date, GPS</td></tr>
            <tr><td>Mac</td><td>Preview → Tools → Show Inspector → (i) tab</td><td>EXIF and GPS panels</td></tr>
            <tr><td>Android</td><td>Gallery → Details / info</td><td>Basics, location if present</td></tr>
            <tr><td>Command line</td><td><code>exiftool photo.jpg</code></td><td>All tags</td></tr>
          </tbody>
        </table>
        <h2>If the tool shows nothing</h2>
        <p>The photo may have had metadata removed (messengers and many sites do this), or it is a screenshot, or the tool cannot read HEIC. See <a href="../../learn/heic-vs-jpeg-metadata/">HEIC vs JPEG metadata</a>.</p>
        <p>More: <a href="../find-exif-data/">find EXIF data</a>, <a href="../view-exif-on-iphone/">view EXIF on iPhone</a>, <a href="../check-if-photo-has-location/">check for location</a>.</p>""",
        faqs=[
            ("How do I read EXIF data from a photo?", "Use a browser EXIF viewer, your computer's file properties or Preview, an iPhone app, or ExifTool on the command line."),
            ("How can I see EXIF data without installing anything?", "Use the browser viewer on this site; the file is read in your tab and not uploaded."),
            ("Why is the EXIF data empty?", "It was stripped by an app or site, the file is a screenshot, or the viewer does not support the format."),
            ("Which tool shows the most tags?", "ExifTool lists nearly every tag, including maker-specific ones."),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
    )

    # 4 -------------------------------------------------------------
    article_page(
        "how-to/view-png-metadata",
        title="How to View PNG Metadata (and What PNG Stores) | EXIF+",
        description="PNG stores metadata differently from JPEG: text chunks and an optional EXIF chunk. How to view it online and on your computer.",
        h1="How to view PNG metadata",
        lead="PNG files carry metadata in chunks. Many have none, and some carry EXIF.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> To view PNG metadata, drop the file into a browser metadata viewer or run ExifTool. PNG does not use JPEG's EXIF block by default; it stores text in <strong>tEXt, zTXt and iTXt</strong> chunks and can hold EXIF in an <strong>eXIf</strong> chunk. A plain PNG often shows little more than size, bit depth and colour type.</p>
        <table>
          <thead><tr><th>PNG chunk</th><th>Holds</th></tr></thead>
          <tbody>
            <tr><td>IHDR</td><td>Width, height, bit depth, colour type</td></tr>
            <tr><td>tEXt / zTXt / iTXt</td><td>Text key-value pairs, such as Title, Author, Software, Comment</td></tr>
            <tr><td>eXIf</td><td>An EXIF block, if the software wrote one</td></tr>
            <tr><td>tIME</td><td>Last-modified time, if present</td></tr>
          </tbody>
        </table>
        <h2>How to look</h2>
        <ol>
          <li>Open the <a href="../../exif-viewer/">browser metadata viewer</a> and add the PNG (read locally in your tab).</li>
          <li>Or run <code>exiftool image.png</code> to list every chunk it understands.</li>
        </ol>
        <h2>Do PNGs hold location?</h2>
        <p>Only if an app wrote GPS into an eXIf chunk. Screenshots normally do not. Some AI image tools write text chunks describing the generation settings: see <a href="../../learn/ai-image-metadata-c2pa/">AI image metadata and C2PA</a>. More: <a href="../../learn/pdf-video-png-metadata/">PDF, video and PNG metadata</a>.</p>
        <p>To strip PNG metadata, use the <a href="../../remove-exif/">browser remover</a>.</p>
        {src(("PNG (Wikipedia)", "https://en.wikipedia.org/wiki/PNG"), ("ExifTool PNG tags", "https://exiftool.org/TagNames/PNG.html"))}""",
        faqs=[
            ("Does PNG have EXIF data?", "Only if the software that made it wrote an eXIf chunk. Many PNGs have none."),
            ("How do I view metadata of a PNG?", "Use a browser metadata viewer or ExifTool."),
            ("Do PNG files contain GPS?", "Rarely. Screenshots and exported graphics usually do not."),
            ("Can PNG hold text like a prompt or author?", "Yes, in tEXt, zTXt or iTXt chunks, if an app writes them."),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
    )

    # 5 -------------------------------------------------------------
    article_page(
        "learn/exiftool-online",
        title="ExifTool Online: Browser Alternative and Commands | EXIF+",
        description="ExifTool is a command-line program, not a website. Browser tools that do the same job for common files, and the ExifTool commands to view and remove metadata.",
        h1="ExifTool online: what to use instead",
        lead="ExifTool itself runs on your computer. For quick jobs in a browser there are online viewers; for full control, learn four commands.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> ExifTool, written by Phil Harvey, is a free command-line program for reading and writing metadata in many file types. It is not an online service. If you want something in a browser, use an online metadata viewer such as the one on this site, which reads JPEG, PNG and WebP in your tab without uploading them.</p>
        <h2>Four commands worth knowing</h2>
        <table>
          <thead><tr><th>Goal</th><th>Command</th></tr></thead>
          <tbody>
            <tr><td>View all tags</td><td><code>exiftool photo.jpg</code></td></tr>
            <tr><td>Remove all metadata</td><td><code>exiftool -all= photo.jpg</code> (keeps a <code>_original</code> backup)</td></tr>
            <tr><td>Remove GPS only</td><td><code>exiftool -gps:all= photo.jpg</code></td></tr>
            <tr><td>Clean a whole folder</td><td><code>exiftool -r -all= folder/</code></td></tr>
          </tbody>
        </table>
        <p>Removing all tags can also drop the orientation and colour profile, so a photo may look rotated or slightly different afterwards. Test on a copy first.</p>
        <h2>Browser or app instead</h2>
        <ul>
          <li><strong>Browser:</strong> <a href="../../exif-viewer/">EXIF viewer</a>, <a href="../../remove-exif/">EXIF remover</a>, <a href="../../remove-gps/">GPS remover</a>.</li>
          <li><strong>iPhone:</strong> {NAME} for photos in your library; HEIC is supported.</li>
        </ul>
        <p>See also <a href="../../compare/exif-viewer-alternatives/">EXIF viewer alternatives</a>.</p>
        {src(("ExifTool by Phil Harvey", "https://exiftool.org/"))}""",
        faqs=[
            ("Is there an ExifTool online?", "ExifTool is a command-line program. Online viewers offer a similar view for common formats."),
            ("Is ExifTool free?", "Yes, it is free and open source."),
            ("How do I remove all metadata with ExifTool?", "Run exiftool -all= followed by the file name. It keeps a backup copy with _original in the name."),
            ("Is an online tool safe for private photos?", "Pick one that processes files in your browser, as the viewer here does, rather than uploading them."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    # 6 -------------------------------------------------------------
    article_page(
        "how-to/delete-image-metadata-windows",
        title="How to Delete Image Metadata on Windows (Step by Step) | EXIF+",
        description="Remove EXIF, GPS and personal info from a photo on Windows 10 and 11 using Properties, and what that method does not cover.",
        h1="How to delete image metadata on Windows",
        lead="Windows can remove photo properties without extra software. Here are the steps and the limits.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> Right-click the photo, choose <strong>Properties → Details</strong>, click <strong>Remove Properties and Personal Information</strong>, then pick either a cleaned copy or removal from the original file. This works for common formats such as JPEG; always open the result to check.</p>
        <h2>Steps</h2>
        <ol>
          <li>Right-click the image → <strong>Properties</strong> → <strong>Details</strong> tab.</li>
          <li>Click <strong>Remove Properties and Personal Information</strong> at the bottom.</li>
          <li>Choose <em>Create a copy with all possible properties removed</em> (safest), or <em>Remove the following properties from this file</em> and tick the ones you want gone (GPS, camera, dates).</li>
          <li>Click OK. A copy is saved next to the original with "- Copy" in the name.</li>
        </ol>
        <h2>Limits</h2>
        <ul>
          <li>Not every format or tag is covered; HEIC support depends on your codecs.</li>
          <li>Batch: you can select several files before opening Properties.</li>
          <li>To verify, reopen Details or use the <a href="../../exif-viewer/">browser viewer</a>.</li>
        </ul>
        <h2>Alternatives</h2>
        <p>Use the <a href="../../remove-exif/">browser EXIF remover</a> for a quick clean without installing anything, or ExifTool for scripts: <a href="../../learn/exiftool-online/">ExifTool commands</a>. All platforms: <a href="../remove-photo-metadata-mac-windows/">remove metadata on Mac and Windows</a>.</p>""",
        faqs=[
            ("How do I remove metadata from a photo in Windows 11?", "Right-click the file, open Properties → Details, and choose Remove Properties and Personal Information."),
            ("Does Windows remove GPS from photos?", "Yes, the Remove Properties dialog lets you remove location tags, if the format is supported."),
            ("Does it change the original?", "Only if you choose to remove properties from the file itself; the copy option leaves the original untouched."),
            ("Can I clean many photos at once?", "Yes, select them all before opening Properties."),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
    )

    # 7 -------------------------------------------------------------
    article_page(
        "how-to/delete-image-metadata-mac",
        title="How to Delete Image Metadata on Mac (Location and More) | EXIF+",
        description="Remove location from a photo on Mac using Preview or Photos export, and what these built-in methods leave behind.",
        h1="How to delete image metadata on Mac",
        lead="macOS removes location easily; removing every tag needs another tool.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> On a Mac, open the photo in <strong>Preview → Tools → Show Inspector</strong>, go to the <strong>GPS</strong> tab and click <strong>Remove Location Info</strong>. In the Photos app, choose <strong>File → Export</strong> and untick the location option. These remove location; they do not clear camera and date tags.</p>
        <table>
          <thead><tr><th>Method</th><th>Removes</th><th>Leaves</th></tr></thead>
          <tbody>
            <tr><td>Preview, GPS tab</td><td>Location</td><td>Camera, dates, other EXIF</td></tr>
            <tr><td>Photos export, location unticked</td><td>Location in the exported copy</td><td>Other metadata</td></tr>
            <tr><td><a href="../../remove-exif/">Browser EXIF remover</a></td><td>All EXIF, GPS and text tags (JPEG, PNG, WebP)</td><td>Pixels</td></tr>
            <tr><td>ExifTool <code>-all=</code></td><td>Nearly everything</td><td>Pixels</td></tr>
          </tbody>
        </table>
        <p>If the photo came from an iPhone, you can clean it on the phone instead: {NAME} saves a cleaned copy and keeps the original. See <a href="../remove-photo-metadata-iphone/">remove photo metadata on iPhone</a> and <a href="../remove-photo-metadata-mac-windows/">Mac and Windows overview</a>.</p>""",
        faqs=[
            ("How do I remove location from a photo on Mac?", "Preview → Tools → Show Inspector → GPS tab → Remove Location Info."),
            ("Does Preview remove all metadata?", "No. It removes location; camera and date tags remain."),
            ("Can Photos export without location?", "Yes. Untick the location option in the export dialog."),
            ("How do I remove everything?", "Use a metadata remover such as the browser tool here or ExifTool."),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
    )

    # 8 -------------------------------------------------------------
    article_page(
        "learn/do-iphone-screenshots-have-location",
        title="Do iPhone Screenshots Have Location Data or Metadata? | EXIF+",
        description="Screenshots are PNG files made by the screen, not the camera. What they usually contain, what they do not, and when to still check.",
        h1="Do iPhone screenshots have location data?",
        lead="Usually no GPS. A screenshot is not a camera photo, so it is not geotagged the way one is.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> iPhone screenshots are saved as images of the screen and normally contain no GPS location. They can still carry basic information such as creation date and the device, but no camera settings. The sources we found do not fully agree on exact fields, and Apple does not document them, so check a specific file if it matters.</p>
        <table>
          <thead><tr><th>Item</th><th>In a typical screenshot?</th></tr></thead>
          <tbody>
            <tr><td>GPS location</td><td>No</td></tr>
            <tr><td>Camera settings (ISO, aperture)</td><td>No</td></tr>
            <tr><td>Date and time</td><td>Yes (file date, often in tags too)</td></tr>
            <tr><td>Device</td><td>Possibly</td></tr>
            <tr><td>What the screenshot shows</td><td>Yes: names, addresses, map pins in the picture itself</td></tr>
          </tbody>
        </table>
        <h2>The bigger risk is the picture</h2>
        <p>A screenshot of a map, chat or order page shows information in plain sight. Metadata is not the issue; crop it first.</p>
        <h2>How to check one</h2>
        <p>Open it in the <a href="../../exif-viewer/">browser viewer</a> or in {NAME}. More: <a href="../does-screenshot-have-exif/">do screenshots have EXIF</a>, <a href="../../how-to/check-if-photo-has-location/">check for location</a>.</p>
        <p><small>Based on public sources including <a href="https://discussions.apple.com/thread/6454553" rel="noopener">Apple Community</a>. We have not tested every iOS version. {CHECKED}</small></p>""",
        faqs=[
            ("Do iPhone screenshots contain location?", "Normally no. Screenshots are not geotagged like camera photos."),
            ("Do screenshots have any metadata?", "Usually basic details such as date and device, but not camera settings."),
            ("Can someone find me from a screenshot?", "Not from GPS tags, but from what the screenshot displays, such as addresses or names."),
            ("How can I be sure?", "Inspect the file with an EXIF viewer."),
            ("Do screenshots have EXIF data?", "Usually only basic fields such as date and device, not camera settings or GPS. Open the file in an EXIF viewer to see exactly what it holds."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    # 9 -------------------------------------------------------------
    article_page(
        "learn/does-gmail-remove-exif",
        title="Does Gmail Remove EXIF Data From Photos? | EXIF+",
        description="Does Gmail strip location and EXIF from photo attachments? What we can say, what we could not verify, and the safe habit.",
        h1="Does Gmail strip EXIF data?",
        lead="Treat an emailed photo as unchanged. We found no Google statement that Gmail strips EXIF from attachments.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> Do not assume Gmail removes EXIF. Photos sent as attachments are delivered as files, so the recipient can normally download the original with its metadata. We found no Google documentation saying attachments are cleaned, and we have not run our own test. Previews may look different from the downloaded file.</p>
        <table>
          <thead><tr><th>How you send</th><th>Metadata likely kept?</th></tr></thead>
          <tbody>
            <tr><td>Attachment</td><td>Yes: assume the file arrives unchanged</td></tr>
            <tr><td>Photo pasted inline in the message body</td><td>Unclear; the client may re-encode it</td></tr>
            <tr><td>Link to a photo in Google Photos or Drive</td><td>Depends on sharing settings; the original can be downloadable</td></tr>
          </tbody>
        </table>
        <h2>Safe habit</h2>
        <p>Clean the photo before it leaves your device: <a href="../../how-to/remove-location-from-photos-iphone/">remove location on iPhone</a> or use the <a href="../../remove-gps/">browser GPS remover</a>. {NAME} saves a cleaned copy, so attach that one.</p>
        <p>Details for email in general: <a href="../does-email-attachment-keep-exif/">do email attachments keep EXIF</a>.</p>""",
        faqs=[
            ("Does Gmail strip EXIF data?", "We found no evidence that it does for attachments; assume the file keeps its metadata."),
            ("Can the recipient see where my photo was taken?", "If the file has GPS tags and you attach it unchanged, yes."),
            ("How do I send a photo by email without location?", "Remove location first, then attach the cleaned copy."),
            ("Did you test Gmail?", "No. This page reflects public documentation and general behaviour, not our own test."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    # 10 ------------------------------------------------------------
    article_page(
        "learn/does-airdrop-keep-location",
        title="Does AirDrop Keep Photo Location? Options Switch Explained | EXIF+",
        description="AirDrop sends the photo file. Whether it includes location depends on the share sheet's Options. What to check before you AirDrop a photo.",
        h1="Does AirDrop send photo location?",
        lead="By default, assume yes. AirDrop sends the photo itself, and the share sheet's Options decide what travels with it.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> AirDrop transfers the photo file, so location can go with it. On recent iOS versions the share sheet has an <strong>Options</strong> button at the top where you can turn <strong>Location</strong> off for that send. Whether you rely on the default or the switch, the safest option is to send a cleaned copy.</p>
        <h2>Before you AirDrop</h2>
        <ol>
          <li>Select the photo, tap Share.</li>
          <li>Tap <strong>Options</strong> at the top and switch <strong>Location</strong> off.</li>
          <li>Choose the AirDrop recipient.</li>
        </ol>
        <table>
          <thead><tr><th></th><th>Options switch</th><th>Cleaned copy ({NAME})</th></tr></thead>
          <tbody>
            <tr><td>Applies to</td><td>This one send</td><td>A new file in your library</td></tr>
            <tr><td>Camera and date tags</td><td>Not covered</td><td>Removed, or edited</td></tr>
            <tr><td>Reusable</td><td>No</td><td>Yes</td></tr>
          </tbody>
        </table>
        <p>Related: <a href="../does-imessage-remove-location/">iMessage and AirDrop location</a>, <a href="../../compare/ios-share-options-vs-exif-app/">Options vs an EXIF app</a>, <a href="../../how-to/share-photo-without-metadata/">share without metadata</a>.</p>""",
        faqs=[
            ("Does AirDrop send GPS location?", "It can. AirDrop sends the file; use the share sheet's Options to turn Location off, or send a cleaned copy."),
            ("Where is the Location switch?", "Tap Share on a photo, then Options at the top of the share sheet."),
            ("Does the switch remove camera and date tags?", "Do not assume so. It targets location; use a metadata remover for the rest."),
            ("Does the switch change my original photo?", "No. It only affects what is sent."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    # 11 ------------------------------------------------------------
    article_page(
        "learn/what-is-iptc-data",
        title="What Is IPTC Data in a Photo? Fields and Examples | EXIF+",
        description="IPTC is photo metadata for captions, keywords, creator and copyright. What the fields are and how it differs from EXIF.",
        h1="What is IPTC data?",
        lead="IPTC is the descriptive layer of photo metadata: who made it, what it shows, and who owns it.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> <strong>IPTC data</strong> is photo metadata defined by the International Press Telecommunications Council. It holds text a person writes about an image: caption, headline, keywords, creator, credit and copyright notice. EXIF, by contrast, is mostly technical data written by the camera.</p>
        <table>
          <thead><tr><th>IPTC field</th><th>Example</th></tr></thead>
          <tbody>
            <tr><td>Headline</td><td>Harbour at sunrise</td></tr>
            <tr><td>Description / Caption</td><td>Fishing boats leaving the harbour at 6 a.m.</td></tr>
            <tr><td>Keywords</td><td>harbour, boats, sunrise</td></tr>
            <tr><td>Creator</td><td>Photographer's name</td></tr>
            <tr><td>Copyright Notice</td><td>© 2026 Name</td></tr>
            <tr><td>Date Created, City, Country</td><td>2026-11-02, Lisbon, Portugal</td></tr>
          </tbody>
        </table>
        <h2>Why it matters</h2>
        <p>IPTC can contain your name and location in words, not only in coordinates, so a GPS-only cleanup does not remove it. {NAME} reads EXIF, IPTC and GPS and can edit or remove them. See <a href="../exif-vs-iptc/">EXIF vs IPTC</a>, <a href="../../how-to/batch-edit-copyright/">batch edit copyright</a> and the <a href="../glossary/">glossary</a>.</p>
        {src(("IPTC Photo Metadata Standard", "https://iptc.org/standards/photo-metadata/"))}""",
        faqs=[
            ("What does IPTC stand for?", "International Press Telecommunications Council."),
            ("What is IPTC metadata used for?", "Captions, keywords, creator, credit and copyright text, mainly for publishing and archiving."),
            ("Is IPTC the same as EXIF?", "No. EXIF is mostly camera-written technical data; IPTC is descriptive text added by people or software."),
            ("Can IPTC reveal my name?", "Yes, if a Creator or Copyright field is filled in."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    # 12 ------------------------------------------------------------
    article_page(
        "how-to/preview-content-credentials-photoshop",
        title="Preview Content Credentials Before Exporting in Photoshop | EXIF+",
        description="Where to see what Content Credentials Photoshop will attach to an export, what they can include, and how to choose what to share.",
        h1="How to preview Content Credentials before exporting in Photoshop",
        lead="Photoshop shows a preview of what will be attached when you export. Here is where to look.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> In Photoshop, open <strong>File → Export As</strong> and review the <strong>Content Credentials</strong> options in the lower-right of the dialog. The <strong>Preview</strong> tab of the Content Credentials panel lists what would be attached, such as identity details, connected social accounts, edit history and ingredients. Choose <strong>None</strong> to attach no Content Credentials. Menu names can differ by version, as Adobe still labels the feature Beta in places.</p>
        <h2>What can be included</h2>
        <table>
          <thead><tr><th>Item</th><th>You control it in</th></tr></thead>
          <tbody>
            <tr><td>Your name</td><td>Content Credentials Settings</td></tr>
            <tr><td>Connected social accounts</td><td>Settings, after you connect them</td></tr>
            <tr><td>Edit activity</td><td>Settings</td></tr>
            <tr><td>Ingredients (source images)</td><td>Reflected in the Preview tab</td></tr>
          </tbody>
        </table>
        <h2>Check the exported file</h2>
        <p>Inspect the result with Adobe's Content Credentials verify tool, and read the ordinary EXIF with a <a href="../../exif-viewer/">metadata viewer</a>. Content Credentials (C2PA) and EXIF are separate things: <a href="../../learn/ai-image-metadata-c2pa/">AI image metadata and C2PA</a>. To strip EXIF and GPS from the exported file on iPhone, use {NAME}; note that cleaning rewrites the file and this page does not claim to remove or preserve Content Credentials.</p>
        {src(("Adobe: apply Content Credentials in Photoshop", "https://www.adobe.com/learn/photoshop/web/apply-content-credentials-photoshop"), ("Adobe: secure image data with Content Credentials", "https://www.adobe.com/learn/photoshop/web/secure-image-data-enable-content-credentials-photoshop"))}""",
        faqs=[
            ("Where do I preview Content Credentials in Photoshop?", "In Export As, check the Content Credentials options at the lower right; the panel's Preview tab shows what will be attached."),
            ("How do I export without Content Credentials?", "Choose None in the Content Credentials option."),
            ("What can Content Credentials include?", "Identity details, connected social accounts, edit history and image ingredients, depending on your settings."),
            ("Are Content Credentials the same as EXIF?", "No. They are a separate signed record (C2PA) from the EXIF tags in the file."),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
    )
