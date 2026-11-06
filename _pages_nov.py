"""Pages added 2026-11: question-style pages written to be cited by AI answers, with honest EXIF+ recommendation blocks.

Claim-safe: follows product-knowledge.json claimsPolicy (no XMP, no video, no zero-analytics, no lossless claims).
"""
from __future__ import annotations

UPDATED = "2026-11-06"


def register_nov(ns: dict) -> None:
    article_page = ns["article_page"]
    NAME = ns["NAME"]

    fits = f"""        <h2>When {NAME} fits, and when it does not</h2>
        <p><strong>It fits if</strong> you have an iPhone or iPad (iOS 17+) and want to see, edit or remove EXIF, IPTC and GPS on photos in your Photo Library. Single-photo view, edit and remove are free; multi-select batch and strip-on-share need Premium. Cleaned photos are saved as new Library items and the original is kept.</p>
        <p><strong>It does not fit if</strong> you need to edit video metadata, read or write XMP, or work on a computer. For one JPEG, PNG or WebP on a computer, the <a href="../../remove-exif/">browser EXIF remover</a> is enough.</p>"""

    # 1 ---------------------------------------------------------------
    article_page(
        "compare/best-app-to-remove-exif-iphone",
        title="Best App to Remove EXIF Data on iPhone (2026) | EXIF+",
        description="How to choose an app that removes EXIF and location from iPhone photos: five criteria, the main options compared, and where EXIF+ fits.",
        h1="Best app to remove EXIF data on iPhone",
        lead="The best app is the one that cleans the photo on your device, keeps the original, and does the job in few taps. Here are the criteria, the options, and where EXIF+ fits.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> Pick an iPhone app that removes EXIF and GPS on the device (no upload), saves the result as a new photo instead of overwriting the original, supports HEIC, and lets you clean several photos at once. {NAME} does these things; the iOS share sheet can drop location only, and a browser tool is fine for a single JPEG, PNG or WebP.</p>
        <h2>Five criteria that matter</h2>
        <ol>
          <li><strong>Processing stays on the device.</strong> A photo you want to make private should not be uploaded to a server to be cleaned.</li>
          <li><strong>Original is kept.</strong> The tool should save a new copy so a mistake cannot destroy your only photo.</li>
          <li><strong>HEIC works.</strong> iPhone photos are usually HEIC; many browser tools cannot open them.</li>
          <li><strong>Removes more than location.</strong> Camera model, software and date also describe you.</li>
          <li><strong>Batch.</strong> Cleaning one photo at a time stops being practical after a few.</li>
        </ol>
        <h2>Options compared</h2>
        <table>
          <thead><tr><th>Option</th><th>Removes</th><th>Good for</th><th>Limit</th></tr></thead>
          <tbody>
            <tr><td>iOS share sheet → Options</td><td>Location (and some data) for that share</td><td>Quick one-off send</td><td>Does not give you a cleaned file in your library</td></tr>
            <tr><td><a href="../../remove-exif/">Browser EXIF remover</a></td><td>All EXIF/GPS in the file</td><td>JPEG, PNG, WebP on any device</td><td>HEIC from the iPhone library is often not readable</td></tr>
            <tr><td>{NAME} app</td><td>EXIF, IPTC and GPS; selective edit or remove all</td><td>iPhone Photo Library, HEIC, batch (Premium)</td><td>iOS/iPadOS only; no video or XMP</td></tr>
            <tr><td>ExifTool</td><td>Almost any tag in many file types</td><td>Computers, scripts</td><td>Command line</td></tr>
          </tbody>
        </table>
{fits}
        <p>See also: <a href="../online-vs-iphone-app/">online tool vs iPhone app</a>, <a href="../../how-to/remove-photo-metadata-iphone/">how to remove photo metadata on iPhone</a>.</p>""",
        faqs=[
            ("What is the best app to remove EXIF data on iPhone?", f"Look for on-device processing, HEIC support, a saved copy instead of overwriting, and batch cleaning. {NAME} is built around those."),
            ("Can I remove EXIF on iPhone without an app?", "Partly. The share sheet's Options lets you turn off location for that send, but it does not remove camera and date tags from a saved file."),
            ("Is it safe to use an online EXIF remover?", "Only if it processes the file locally. Check the tool's privacy statement; the browser tools on this site read files in your tab."),
            ("Does removing EXIF lower photo quality?", "Stripping tags does not change the pixels, but an app that re-saves a JPEG or HEIC may recompress it. See the page on quality."),
        ],
        nav="Compare",
        parent=("Compare", "compare/"),
        priority=True,
    )

    # 2 ---------------------------------------------------------------
    article_page(
        "compare/best-exif-viewer-iphone",
        title="Best EXIF Viewer for iPhone: What to Look For | EXIF+",
        description="How to pick an EXIF viewer for iPhone: reads HEIC, shows GPS on a map, works on library photos, and lets you act on what you find.",
        h1="Best EXIF viewer for iPhone",
        lead="An iPhone EXIF viewer should open library photos directly, understand HEIC, show location clearly, and let you remove what it finds.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> The Photos app shows only a few details (date, camera, size, sometimes a map). A dedicated EXIF viewer such as {NAME} lists the full EXIF, IPTC and GPS tags of a photo in your library, including HEIC, and lets you edit or remove them from the same screen.</p>
        <h2>What the built-in Photos app shows</h2>
        <p>Swipe up on a photo or tap the info button to see date, camera, lens and file size, and a location map if the photo has GPS. It does not list every tag and it cannot remove most of them.</p>
        <h2>What to look for in a viewer</h2>
        <ul>
          <li><strong>Direct access to the Photo Library</strong> so you do not have to export first.</li>
          <li><strong>HEIC support</strong>, since most iPhone photos are HEIC.</li>
          <li><strong>GPS shown plainly</strong>, as coordinates or on a map.</li>
          <li><strong>An action next to the data</strong>: edit a wrong date, or remove location before sharing.</li>
        </ul>
        <h2>Computer or browser instead</h2>
        <p>For a JPEG, PNG or WebP on a computer use the <a href="../../exif-viewer/">browser EXIF viewer</a>; it reads the file in your tab. For other options see <a href="../exif-viewer-alternatives/">EXIF viewer alternatives</a>.</p>
{fits}""",
        faqs=[
            ("Does iPhone have a built-in EXIF viewer?", "The Photos info panel shows basic details such as date, camera and location, but not the full tag list."),
            ("How do I see all EXIF data on iPhone?", f"Use an EXIF viewer app. {NAME} reads EXIF, IPTC and GPS from photos in your library."),
            ("Can an EXIF viewer read HEIC?", f"Many desktop and browser tools cannot. {NAME} reads HEIC from the Photo Library."),
            ("Is there a free EXIF viewer?", "Yes. The browser viewer here is free, and single-photo viewing in the app does not need Premium."),
        ],
        nav="Compare",
        parent=("Compare", "compare/"),
        priority=True,
    )

    # 3 ---------------------------------------------------------------
    article_page(
        "compare/ios-share-options-vs-exif-app",
        title="iPhone Share Options vs an EXIF App: Which to Use? | EXIF+",
        description="The iOS share sheet can turn off location for one send. When is that enough, and when do you need an app that cleans the file itself?",
        h1="iPhone share-sheet Options vs an EXIF remover app",
        lead="The share sheet can drop location for one send. An EXIF app changes the file itself. Which one you need depends on where the photo goes.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> If you only need to send one photo through Messages, Mail or AirDrop without its location, the share sheet's Options switch is enough. If you need the photo cleaned of camera, date and GPS tags, kept as its own file, or cleaned in bulk, use an app like {NAME}.</p>
        <table>
          <thead><tr><th></th><th>Share sheet Options</th><th>{NAME}</th></tr></thead>
          <tbody>
            <tr><td>What changes</td><td>What is sent this time</td><td>A cleaned copy saved in your library</td></tr>
            <tr><td>Tags covered</td><td>Location, and what Apple lets you toggle</td><td>EXIF, IPTC and GPS; selective or all</td></tr>
            <tr><td>Reuse the clean file later</td><td>No</td><td>Yes, it is a new Library item</td></tr>
            <tr><td>Many photos at once</td><td>Send them together; same toggle</td><td>Batch remove (Premium)</td></tr>
            <tr><td>Also edit tags</td><td>No</td><td>Date, location, camera, author, copyright</td></tr>
          </tbody>
        </table>
        <h2>Practical rule</h2>
        <p>Casual send to a friend: Options. Upload to a website, marketplace or social app, or anything public: clean the file first. See <a href="../../learn/does-imessage-remove-location/">what iMessage and AirDrop do with location</a> and <a href="../../how-to/share-photo-without-metadata/">share without metadata</a>.</p>
{fits}""",
        faqs=[
            ("How do I send a photo without location on iPhone?", "Open the share sheet, tap Options at the top, and turn Location off before sending."),
            ("Does the Options switch change the saved photo?", "No. It only changes what is sent in that share."),
            ("Does the share sheet remove camera and date info?", "Do not assume so. The location switch targets location; use a metadata remover for the rest."),
            ("When should I use an EXIF app instead?", "When the photo goes to a public site, when you want a reusable clean copy, or when you have many photos."),
        ],
        nav="Compare",
        parent=("Compare", "compare/"),
    )

    # 4 ---------------------------------------------------------------
    article_page(
        "compare/free-exif-remover-vs-paid",
        title="Free EXIF Remover vs Paid: What Is Actually Free? | EXIF+",
        description="Is there a free way to remove EXIF? Yes: browser tools, the iOS share toggle, and single-photo removal in EXIF+. Here is what Premium adds.",
        h1="Free EXIF remover vs paid: what you really get",
        lead="You can remove EXIF for free in several ways. Paying only makes sense when you clean many photos or share often.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> Yes, free options exist. The <a href="../../remove-exif/">browser EXIF remover</a> on this site is free and local. In {NAME}, viewing, editing and removing metadata from a single photo is free; Premium adds multi-select batch remove and edit, and sharing a stripped temporary copy.</p>
        <table>
          <thead><tr><th>Need</th><th>Free path</th><th>Needs Premium?</th></tr></thead>
          <tbody>
            <tr><td>Clean one JPEG, PNG or WebP</td><td>Browser remover</td><td>No</td></tr>
            <tr><td>Clean one iPhone photo (incl. HEIC)</td><td>{NAME}, single photo</td><td>No</td></tr>
            <tr><td>Remove location for one send</td><td>iOS share sheet Options</td><td>No</td></tr>
            <tr><td>Clean many photos in one go</td><td>One by one for free</td><td>Yes, batch</td></tr>
            <tr><td>Share a stripped copy without saving it</td><td>—</td><td>Yes</td></tr>
          </tbody>
        </table>
        <p>Details and prices are on the <a href="../../app/free-vs-premium/">free vs Premium</a> page and in the App Store listing.</p>""",
        faqs=[
            ("Is there a free EXIF remover?", "Yes. A browser-based remover is free, and single-photo removal in EXIF+ is available without Premium."),
            ("What does EXIF+ Premium add?", "Multi-select batch remove and edit, and sharing a stripped temporary copy."),
            ("Do free EXIF removers upload my photo?", "Some do. The browser tools on this site read the file locally in your tab."),
            ("Is it worth paying for an EXIF remover?", "Only if you regularly clean many photos or want strip-on-share. For occasional single photos, free options work."),
        ],
        nav="Compare",
        parent=("Compare", "compare/"),
    )

    # 5 ---------------------------------------------------------------
    article_page(
        "learn/can-photo-metadata-reveal-your-location",
        title="Can a Photo Reveal Your Location? Yes, via EXIF | EXIF+",
        description="Yes. A photo can store exact GPS coordinates in its EXIF data. What reveals location, what does not, and how to check and remove it.",
        h1="Can a photo reveal your location?",
        lead="Yes. If Location Services were on when you took the photo, the file can carry exact GPS coordinates. Whether others can read them depends on how the photo is shared.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> A photo reveals your location when its EXIF data includes GPS latitude and longitude. Anyone who receives the original file can paste those numbers into a map. Many social apps re-encode uploads and drop them from the public copy, but files sent as originals usually keep them.</p>
        <h2>Two ways a photo gives away a place</h2>
        <ul>
          <li><strong>Hidden data:</strong> GPS coordinates, and often a timestamp, in EXIF.</li>
          <li><strong>Visible clues:</strong> street signs, house numbers, landmarks and reflections. Removing metadata does not hide these.</li>
        </ul>
        <h2>When the file keeps its GPS</h2>
        <ul>
          <li>Photo sent as a file or document, or by email attachment</li>
          <li>Original uploaded to your own website or a cloud link</li>
          <li>Direct AirDrop with location left on</li>
        </ul>
        <h2>How to check and remove it</h2>
        <ol>
          <li>Check: <a href="../../how-to/check-if-photo-has-location/">how to check if a photo has location data</a>.</li>
          <li>Remove: <a href="../../remove-gps/">GPS remover in your browser</a>, or {NAME} on iPhone (<a href="../../how-to/remove-location-from-photos-iphone/">steps</a>).</li>
          <li>Prevent: turn off location for the Camera app in iPhone Settings → Privacy &amp; Security → Location Services.</li>
        </ol>""",
        faqs=[
            ("Can someone find my location from a photo?", "Yes, if the file you gave them still has GPS EXIF data. They can read the coordinates and open them on a map."),
            ("Does posting on social media reveal my location through EXIF?", "Often the public copy is stripped, but it is not guaranteed for every route. Remove metadata before posting."),
            ("How accurate is photo GPS data?", "Usually accurate to a few metres outdoors, so it can point to a house."),
            ("Does removing EXIF hide where a photo was taken?", "It removes the coordinates, but visible landmarks in the image can still give the place away."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
        priority=True,
    )

    # 6 ---------------------------------------------------------------
    article_page(
        "learn/what-metadata-does-an-iphone-photo-contain",
        title="What Metadata Does an iPhone Photo Contain? | EXIF+",
        description="An iPhone photo stores date, location, device model, lens, exposure, orientation and more. The full list by category, and which parts are private.",
        h1="What metadata does an iPhone photo contain?",
        lead="Every iPhone photo carries more than pixels: when, where and with what it was taken.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> An iPhone photo typically contains the date and time, GPS location (if Location Services were on), device make and model, lens, exposure settings such as ISO and shutter speed, orientation, and image size. Some photos also carry software names and, if added later, author and copyright.</p>
        <table>
          <thead><tr><th>Category</th><th>Examples</th><th>Privacy weight</th></tr></thead>
          <tbody>
            <tr><td>Date &amp; Time</td><td>Date taken, date created</td><td>Medium: shows when you were there</td></tr>
            <tr><td>Location</td><td>Latitude, longitude, altitude</td><td>High: shows where you were</td></tr>
            <tr><td>Camera</td><td>Make, model, lens</td><td>Low to medium: identifies your device</td></tr>
            <tr><td>Camera settings</td><td>ISO, aperture, shutter, focal length, flash</td><td>Low</td></tr>
            <tr><td>Image information</td><td>Dimensions, orientation, color profile</td><td>Low</td></tr>
            <tr><td>Author &amp; description</td><td>Author, copyright, caption</td><td>Depends on what you added</td></tr>
          </tbody>
        </table>
        <h2>See it yourself</h2>
        <p>{NAME} groups tags in these same categories for any photo in your library: <a href="../../how-to/view-exif-on-iphone/">view EXIF on iPhone</a>. For a file on a computer use the <a href="../../image-metadata-viewer/">image metadata viewer</a>. HEIC specifics are on the <a href="../../heic-metadata/">HEIC metadata</a> page; definitions are in <a href="../what-is-exif/">What is EXIF?</a>.</p>""",
        faqs=[
            ("What data is stored in an iPhone photo?", "Date and time, GPS location when enabled, device and lens, exposure settings, orientation and image size."),
            ("Do iPhone photos include location?", "Yes, when Location Services are enabled for the Camera app."),
            ("Does an iPhone photo show my phone model?", "Yes. The camera make and model are stored in EXIF."),
            ("How do I remove metadata from an iPhone photo?", "Use an EXIF remover app, or the Options switch for location on a single share."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    # 7 ---------------------------------------------------------------
    others = '<p>Other platforms: <a href="../does-instagram-remove-exif/">Instagram</a>, <a href="../does-facebook-remove-exif/">Facebook</a>, <a href="../does-twitter-x-remove-exif/">X</a>, <a href="../does-whatsapp-remove-exif/">WhatsApp</a>, <a href="../does-telegram-remove-exif/">Telegram</a>, <a href="../does-discord-remove-exif/">Discord</a>. Full list: <a href="../which-apps-remove-photo-metadata/">which apps remove photo metadata</a>.</p>'

    def platform(slug: str, label: str, short: str, extra: str) -> None:
        article_page(
            f"learn/does-{slug}-remove-exif",
            title=f"Does {label} Remove EXIF Data? Short Answer | EXIF+",
            description=f"Does {label} strip EXIF and GPS from photos? What is usually true, what is not guaranteed, and how to send photos safely.",
            h1=f"Does {label} remove EXIF?",
            lead=short,
            updated=UPDATED,
            prose=f"""        <p><strong>Direct answer:</strong> {short}</p>
        <h2>What is not covered</h2>
        {extra}
        <h2>Safe workflow</h2>
        <p>Clean first, then send: <a href="../../remove-exif/">strip EXIF online</a>, the <a href="../../remove-gps/">GPS remover</a>, or <a href="../../how-to/remove-photo-metadata-iphone/">remove photo metadata on iPhone</a>. The same step works on every platform.</p>
        {others}""",
            faqs=[
                (f"Does {label} remove EXIF data?", f"{label} does not publish a guarantee for every route. Clean the file before sending if privacy matters."),
                (f"Does {label} remove location from photos?", "It may for the copy others see, but the original upload still reaches the service with its metadata."),
                ("What is the safest way to send a photo without location?", "Strip EXIF/GPS yourself first, then send the cleaned copy."),
            ],
            nav="Learn",
            parent=("Learn", "learn/"),
        )

    platform(
        "signal",
        "Signal",
        "Signal is a privacy-focused messenger and processes images it sends, so the copy a recipient gets usually does not carry your original EXIF. This can differ for files sent as attachments, so it is safest to clean the file yourself.",
        "<p>Sending a photo as a generic file attachment may keep the original bytes. Behavior can also change between app versions.</p>",
    )
    platform(
        "snapchat",
        "Snapchat",
        "Snapchat usually re-processes images and snaps, so the copy others see often loses EXIF and GPS — but not as a promise. Photos you upload from your camera roll still reach the service with their original metadata first.",
        "<p>Saved Memories, exported media and anything uploaded from the camera roll are separate routes. Treat each one on its own.</p>",
    )

    # 8 ---------------------------------------------------------------
    article_page(
        "learn/does-email-attachment-keep-exif",
        title="Do Email Attachments Keep EXIF and GPS Data? | EXIF+",
        description="Yes, usually. A photo attached to an email normally arrives as the original file, with its EXIF and GPS. How to send without location.",
        h1="Do email attachments keep EXIF data?",
        lead="Usually yes. An emailed photo tends to arrive as the same file, so the recipient can read its EXIF and location.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> A photo attached to an email is normally delivered as a file, so its EXIF and GPS data travel with it. Some mail apps can resize an image before sending, which may rewrite the file, but that is not a reliable way to remove metadata. Clean the photo before you attach it.</p>
        <h2>Why email is different from social apps</h2>
        <p>Social apps re-encode images they host, which often drops metadata from the public copy. Email carries your file to the recipient as is. The same is true for files sent as documents in chat apps.</p>
        <h2>How to send a photo by email without location</h2>
        <ol>
          <li>Remove location or all metadata first: <a href="../../remove-gps/">GPS remover</a>, <a href="../../remove-exif/">strip EXIF online</a>, or {NAME} on iPhone.</li>
          <li>Attach the cleaned copy, not the original.</li>
          <li>Open the cleaned file in the <a href="../../image-metadata-viewer/">image metadata viewer</a> if you want to confirm.</li>
        </ol>
        <p>On iPhone, the share sheet's Options switch can also remove location for a single send; see <a href="../../compare/ios-share-options-vs-exif-app/">Options vs an EXIF app</a>.</p>""",
        faqs=[
            ("Does Gmail remove EXIF data?", "Do not rely on it. An attached photo generally arrives as the file you sent, with its metadata."),
            ("Can a person who receives my email photo see my location?", "Yes, if the attached file contains GPS data."),
            ("How do I email a photo without metadata?", "Strip the metadata from the file first, then attach the cleaned copy."),
            ("Does resizing a photo in Mail remove metadata?", "It may change the file, but do not count on it. Remove metadata explicitly."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    # 9 ---------------------------------------------------------------
    article_page(
        "how-to/remove-location-before-selling-online",
        title="Remove Photo Location Before Selling Online | EXIF+",
        description="Selling on Marketplace, eBay, Craigslist or Vinted? Photos can carry your home's GPS. How to remove location from listing photos first.",
        h1="Remove photo location before selling online",
        lead="Photos taken at home can hold the exact GPS coordinates of your home. Clean them before you post a listing.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> Before you post listing photos, remove their GPS data. Marketplaces often re-encode photos, but you cannot verify that for every listing route, and photos you send to buyers by message or email can still carry location. Strip the metadata first.</p>
        <h2>Steps on iPhone</h2>
        <ol>
          <li>Open {NAME} and select the listing photo.</li>
          <li>Remove location (or all metadata) and save. The cleaned photo is added as a new item; your original stays.</li>
          <li>For many photos, use batch remove (Premium), or clean them one by one.</li>
          <li>Upload the cleaned copies.</li>
        </ol>
        <p>Full walkthrough: <a href="../remove-location-from-photos-iphone/">remove location from photos on iPhone</a>.</p>
        <h2>Steps on a computer</h2>
        <ol>
          <li>Open the <a href="../../remove-gps/">GPS remover</a> or <a href="../../remove-exif/">strip EXIF online</a>.</li>
          <li>Choose a JPEG, PNG or WebP and download the cleaned file.</li>
        </ol>
        <h2>Also check the picture</h2>
        <p>Metadata is one risk. Visible house numbers, street views through windows and parcels with your address are another. See <a href="../../learn/can-photo-metadata-reveal-your-location/">can a photo reveal your location</a>.</p>""",
        faqs=[
            ("Do Facebook Marketplace photos show my location?", "The public copy is commonly re-encoded, but not guaranteed. Remove GPS before uploading and before sending photos to buyers."),
            ("How do I remove location from photos before selling?", "Strip GPS from each photo with a metadata remover, then upload the cleaned copies."),
            ("Can buyers see where I live from item photos?", "If the file keeps GPS data, yes. Also check for visible clues in the image."),
            ("Do I need to remove all metadata or only location?", "Location matters most. Removing everything also hides camera and date info."),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
    )

    # 10 --------------------------------------------------------------
    article_page(
        "how-to/remove-exif-from-multiple-photos-iphone",
        title="Remove EXIF From Multiple Photos at Once on iPhone | EXIF+",
        description="How to remove EXIF and location from many iPhone photos in one go: select in EXIF+, run batch remove, and check the results.",
        h1="Remove EXIF from multiple photos on iPhone",
        lead="Batch remove lets you select several photos and clean them in one action. Here are the steps and what to expect.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> In {NAME}, select several photos from your library and run batch remove. Multi-select batch remove is a Premium feature. Cleaned photos are saved as new Photo Library items and your originals are kept. Without Premium you can clean photos one at a time.</p>
        <h2>Steps</h2>
        <ol>
          <li>Open {NAME} and enter selection mode.</li>
          <li>Tap the photos you want to clean.</li>
          <li>Choose remove metadata and confirm.</li>
          <li>Find the cleaned copies in your Photo Library; share those, not the originals.</li>
        </ol>
        <h2>Good to know</h2>
        <ul>
          <li>Cleaning rewrites the file, so JPEG and HEIC may be recompressed. See <a href="../../learn/does-cleaning-reduce-quality/">does cleaning reduce quality</a>.</li>
          <li>The cleaned copy appears as a duplicate in your library by design: <a href="../../learn/why-cleaned-photo-is-a-duplicate/">why</a>.</li>
          <li>Video is not supported.</li>
        </ul>
        <p>More: <a href="../../batch-remove/">batch remove</a>, <a href="../../app/free-vs-premium/">free vs Premium</a>, <a href="../strip-metadata-before-sharing/">pre-share checklist</a>.</p>""",
        faqs=[
            ("Can I remove EXIF from many photos at once on iPhone?", "Yes, with multi-select batch remove in EXIF+, which is a Premium feature."),
            ("Is batch EXIF removal free?", "Single-photo removal is free; multi-select batch remove needs Premium."),
            ("Are my original photos deleted?", "No. Cleaned photos are saved as new items and the originals are kept."),
            ("Does batch remove work on HEIC?", "Yes. HEIC and HEIF can be preserved when saving from the library."),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
    )

    # 11 --------------------------------------------------------------
    article_page(
        "how-to/check-if-photo-has-location",
        title="How to Check If a Photo Has Location Data | EXIF+",
        description="Find out in seconds whether a photo contains GPS coordinates: on iPhone, on Mac or Windows, and in your browser. What to do if it does.",
        h1="How to check if a photo has location data",
        lead="Open its metadata and look for GPS latitude and longitude. Here is how on iPhone, a computer, and in a browser.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> A photo has location data if its EXIF includes GPS latitude and longitude. On iPhone, the Photos info panel shows a map when it does. On a computer use file properties or a metadata viewer. The browser viewer on this site shows the GPS fields without uploading the file.</p>
        <h2>On iPhone</h2>
        <ol>
          <li>Open the photo in Photos and swipe up (or tap the info button).</li>
          <li>If a map with a pin is shown, the photo has GPS data.</li>
          <li>For the full tag list use {NAME}: <a href="../view-exif-on-iphone/">view EXIF on iPhone</a>.</li>
        </ol>
        <h2>On Windows</h2>
        <p>Right-click the file → Properties → Details, and look for Latitude and Longitude under GPS.</p>
        <h2>On Mac</h2>
        <p>Open in Preview → Tools → Show Inspector → the GPS tab (it appears only when the photo has location).</p>
        <h2>In any browser</h2>
        <p>Drop the file into the <a href="../../image-metadata-viewer/">image metadata viewer</a> (JPEG, PNG, WebP). Read the fields locally, nothing is uploaded to our servers.</p>
        <h2>If it has location</h2>
        <p>Remove it with the <a href="../../remove-gps/">GPS remover</a> or on iPhone via <a href="../remove-location-from-photos-iphone/">remove location from photos</a>. Why it matters: <a href="../../learn/can-photo-metadata-reveal-your-location/">can a photo reveal your location</a>.</p>""",
        faqs=[
            ("How can I tell if a photo has GPS data?", "Open its metadata and look for latitude and longitude. In Photos on iPhone, a map in the info panel means it does."),
            ("How do I see where a photo was taken?", "Use the Photos info panel, or a metadata viewer that lists GPS coordinates."),
            ("Why does my photo have no location?", "Location Services were off for the camera, or an app or service removed the data."),
            ("Does a screenshot have location data?", "Usually not. See the page on screenshot metadata."),
        ],
        nav="How-to",
        parent=("How-to", "how-to/"),
    )
