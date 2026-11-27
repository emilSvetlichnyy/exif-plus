"""Pages added 2026-11-19: reference pages written to be cited (answer-first, tables, dated, primary sources).

Citation-readiness rules used (from GEO research, e.g. Princeton/KDD 2024 GEO study; vendor studies are directional only):
direct answer in the first paragraph, self-contained passages, specific verifiable facts, tables/lists, named sources, visible date.
Claim-safe: follows product-knowledge.json claimsPolicy (no XMP, no video, no zero-analytics, no lossless claims).
"""
from __future__ import annotations

UPDATED = "2026-11-19"


def register_cite(ns: dict) -> None:
    article_page = ns["article_page"]
    NAME = ns["NAME"]

    src_exif = '<p><small>Sources: <a href="https://exiftool.org/TagNames/EXIF.html" rel="noopener">ExifTool EXIF tag names</a>; <a href="https://en.wikipedia.org/wiki/Exif" rel="noopener">Exif (Wikipedia)</a>. Checked {d}.</small></p>'.replace("{d}", "19 Nov 2026")

    # 1 ---------------------------------------------------------------
    article_page(
        "learn/exif-tags-cheat-sheet",
        title="EXIF Tags Cheat Sheet: The Fields Photos Store | EXIF+",
        description="A plain-language table of the most common EXIF tags (Make, Model, DateTimeOriginal, GPSLatitude and more): what each holds and whether it is a privacy risk.",
        h1="EXIF tags cheat sheet",
        lead="The EXIF fields you will meet most often in a photo, what each one means, and which ones can identify you or your location.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> EXIF (Exchangeable image file format) is a block of tags a camera writes into a photo file. The ones that matter for privacy are the GPS tags (where), the date tags (when) and Make, Model and Software (what device). Exposure tags such as ISO and FNumber describe the shot and are low risk.</p>
        <h2>Privacy-sensitive tags</h2>
        <table>
          <thead><tr><th>Tag</th><th>What it holds</th><th>Risk</th></tr></thead>
          <tbody>
            <tr><td>GPSLatitude, GPSLongitude</td><td>Coordinates where the photo was taken</td><td>High: can point to a home, school or workplace</td></tr>
            <tr><td>GPSAltitude</td><td>Height above or below sea level</td><td>Medium: narrows a location</td></tr>
            <tr><td>GPSImgDirection</td><td>Compass direction the camera faced</td><td>Medium</td></tr>
            <tr><td>DateTimeOriginal</td><td>When the shutter was pressed</td><td>Medium: reveals routines and absence from home</td></tr>
            <tr><td>Make, Model</td><td>Phone or camera brand and model</td><td>Low to medium: identifies your device</td></tr>
            <tr><td>Software</td><td>Firmware or editing app version</td><td>Low</td></tr>
            <tr><td>BodySerialNumber, LensSerialNumber</td><td>Serial numbers (mostly dedicated cameras)</td><td>High: can link photos to one camera</td></tr>
            <tr><td>Artist, Copyright</td><td>Name and rights text, if the camera or an app wrote them</td><td>Depends: can name you</td></tr>
          </tbody>
        </table>
        <h2>Shot-setting tags (low risk)</h2>
        <table>
          <thead><tr><th>Tag</th><th>What it holds</th></tr></thead>
          <tbody>
            <tr><td>ExposureTime</td><td>Shutter speed, for example 1/120 s</td></tr>
            <tr><td>FNumber</td><td>Aperture, for example f/1.8</td></tr>
            <tr><td>ISO</td><td>Sensor sensitivity</td></tr>
            <tr><td>FocalLength</td><td>Lens focal length in millimetres</td></tr>
            <tr><td>Flash</td><td>Whether the flash fired</td></tr>
            <tr><td>Orientation</td><td>How to rotate the image for display</td></tr>
            <tr><td>ColorSpace</td><td>Colour profile flag, such as sRGB</td></tr>
          </tbody>
        </table>
        <h2>What to do with them</h2>
        <p>Keep shot settings if you share photos for learning. Remove GPS and serial numbers before you post publicly. {NAME} lists EXIF, IPTC and GPS tags for photos in your library and can remove all of them, or only location. In a browser, use the <a href="../../exif-viewer/">EXIF viewer</a> or the <a href="../../remove-gps/">GPS remover</a>.</p>
        <p>Related: <a href="../what-is-exif/">what is EXIF</a>, <a href="../exif-date-fields-explained/">date fields explained</a>, <a href="../exif-vs-iptc/">EXIF vs IPTC</a>, <a href="../../how-to/read-exif-data-from-image/">how to read EXIF data from a JPG</a>.</p>
        {src_exif}""",
        faqs=[
            ("What are the most common EXIF tags?", "Make, Model, DateTimeOriginal, ExposureTime, FNumber, ISO, FocalLength, Orientation and the GPS tags are the ones found in most phone and camera photos."),
            ("Which EXIF tags are a privacy risk?", "GPS latitude and longitude first, then the date and time, device Make and Model, and camera serial numbers."),
            ("Does every photo have EXIF?", "No. Screenshots usually have little or none, and many websites and messengers strip it from uploaded copies."),
            ("Can I remove only GPS and keep the rest?", f"Yes. {NAME} and the browser GPS remover can remove location only, or all metadata."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
        priority=True,
    )

    # 2 ---------------------------------------------------------------
    article_page(
        "learn/exif-date-fields-explained",
        title="EXIF Date Fields Explained: DateTimeOriginal vs CreateDate vs ModifyDate | EXIF+",
        description="Three EXIF date tags look similar but mean different things. Which one is the shot time, which changes when you edit, and which is the file date.",
        h1="EXIF date fields explained",
        lead="DateTimeOriginal, CreateDate and ModifyDate are three different clocks. Here is which one answers which question.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> <strong>DateTimeOriginal</strong> is when the picture was taken. <strong>CreateDate</strong> (also called DateTimeDigitized) is when it was stored as a digital file, usually the same moment on a phone. <strong>ModifyDate</strong> is when the file was last changed by software. The date in your file manager is a separate file-system date, not EXIF.</p>
        <table>
          <thead><tr><th>Date</th><th>Where it lives</th><th>Changes when you edit?</th><th>Use it to answer</th></tr></thead>
          <tbody>
            <tr><td>DateTimeOriginal</td><td>EXIF</td><td>Normally not</td><td>When was this taken?</td></tr>
            <tr><td>CreateDate (DateTimeDigitized)</td><td>EXIF</td><td>Normally not</td><td>When was it digitised?</td></tr>
            <tr><td>ModifyDate (DateTime)</td><td>EXIF / TIFF</td><td>Often yes</td><td>When did software last save it?</td></tr>
            <tr><td>File created / modified</td><td>File system</td><td>Yes: copying and exporting reset it</td><td>When did this copy appear on this device?</td></tr>
            <tr><td>OffsetTimeOriginal</td><td>EXIF 2.31+</td><td>Normally not</td><td>Which time zone was the shot time in?</td></tr>
          </tbody>
        </table>
        <h2>Why photos sort in the wrong order</h2>
        <p>Library apps usually sort by DateTimeOriginal. If it is missing, they fall back to another date, and photos from messengers or downloads can jump to the day you saved them. Fixing the shot time puts them back in sequence.</p>
        <h2>Privacy angle</h2>
        <p>Shot time plus GPS shows when you were at a place. If you do not want that, remove the dates along with location. To correct a wrong date in the app, see <a href="../../how-to/change-photo-date-iphone/">change photo date on iPhone</a>; {NAME} edits the date fields and saves the result as a new library item, keeping the original.</p>
        <p>Related: <a href="../exif-tags-cheat-sheet/">EXIF tags cheat sheet</a>, <a href="../what-metadata-does-an-iphone-photo-contain/">what an iPhone photo contains</a>.</p>
        {src_exif}""",
        faqs=[
            ("What is the difference between DateTimeOriginal and CreateDate?", "DateTimeOriginal is when the photo was taken; CreateDate (DateTimeDigitized) is when it was stored digitally. On phones they are normally the same."),
            ("Does editing a photo change its EXIF date?", "Editing software usually updates ModifyDate and may leave DateTimeOriginal alone."),
            ("Why is my photo dated today?", "The file-system date changes when you save or download a copy. The shot time is in EXIF, if it is still there."),
            ("Can I change the date a photo was taken?", f"Yes, by editing DateTimeOriginal. {NAME} lets you do this on iPhone."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    # 3 ---------------------------------------------------------------
    article_page(
        "learn/heic-vs-jpeg-metadata",
        title="HEIC vs JPEG Metadata: Do Both Store EXIF and GPS? | EXIF+",
        description="HEIC and JPEG both carry EXIF and GPS. How they store it differently, why browser tools often fail on HEIC, and what to do before sharing.",
        h1="HEIC vs JPEG metadata",
        lead="Both formats store EXIF and GPS, so both can leak your location. The difference is the container, and which tools can read it.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> Yes. A HEIC photo from an iPhone carries EXIF, including GPS, just like a JPEG. JPEG keeps EXIF in an APP1 segment at the start of the file; HEIC (an HEIF file) keeps it as a separate metadata item inside the container. Many older tools read JPEG but not HEIC, which is why a tool can say a HEIC photo has no metadata when it does.</p>
        <table>
          <thead><tr><th></th><th>JPEG</th><th>HEIC (HEIF)</th></tr></thead>
          <tbody>
            <tr><td>Carries EXIF and GPS</td><td>Yes</td><td>Yes</td></tr>
            <tr><td>Where EXIF is stored</td><td>APP1 segment</td><td>Metadata item in the container</td></tr>
            <tr><td>iPhone default</td><td>Optional ("Most Compatible")</td><td>Yes ("High Efficiency") since iOS 11</td></tr>
            <tr><td>Opens in most websites and old software</td><td>Yes</td><td>Often no</td></tr>
            <tr><td>File size at similar quality</td><td>Larger</td><td>Smaller</td></tr>
          </tbody>
        </table>
        <h2>What this means in practice</h2>
        <ul>
          <li>Switching an iPhone to JPEG does not remove location; both formats record it if Location Services is on for the camera.</li>
          <li>The <a href="../../exif-viewer/">browser viewer</a> and <a href="../../remove-exif/">browser remover</a> work best on JPEG, PNG and WebP; HEIC may be unsupported in some browsers. See <a href="../../heic-metadata/">HEIC metadata</a>.</li>
          <li>{NAME} reads HEIC from the Photo Library and can keep HEIC or HEIF when it saves the cleaned copy.</li>
        </ul>
        <p>Related: <a href="../what-is-exif/">what is EXIF</a>, <a href="../does-cleaning-reduce-quality/">does cleaning reduce quality</a>, <a href="../../how-to/read-exif-data-from-image/">how to read EXIF data from a JPG</a>.</p>
        <p><small>Sources: <a href="https://en.wikipedia.org/wiki/High_Efficiency_Image_File_Format" rel="noopener">HEIF (Wikipedia)</a>; <a href="https://exiftool.org/TagNames/EXIF.html" rel="noopener">ExifTool tag names</a>. Checked 19 Nov 2026.</small></p>""",
        faqs=[
            ("Does HEIC have EXIF data?", "Yes. HEIC photos carry EXIF, including GPS, stored as a metadata item in the HEIF container."),
            ("Is HEIC safer for privacy than JPEG?", "No. Both record location when Location Services is on for the camera."),
            ("Why can't my tool read HEIC metadata?", "Many older or browser-based tools do not parse the HEIF container, so they report nothing."),
            ("Does converting HEIC to JPEG remove metadata?", "Not necessarily. Many converters copy the EXIF across, so check the result."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )

    # 4 ---------------------------------------------------------------
    article_page(
        "learn/is-exif-data-a-privacy-risk",
        title="Is EXIF Data a Privacy Risk? What Photos Can Give Away | EXIF+",
        description="When photo metadata is a real privacy risk, when it is not, and a documented case where a geotagged photo exposed a location.",
        h1="Is EXIF data a privacy risk?",
        lead="Sometimes. The risk comes from GPS and date tags in the original file, not from the picture itself.",
        updated=UPDATED,
        prose=f"""        <p><strong>Direct answer:</strong> EXIF is a privacy risk when you share the <em>original file</em> of a photo that contains GPS coordinates. Anyone who receives that file can read where and when it was taken. It is low risk when the platform strips it, or when Location Services was off at capture.</p>
        <h2>A documented example</h2>
        <p>In December 2012, a photo of software founder John McAfee published by a magazine while he was a fugitive carried GPS tags in its EXIF data. Readers extracted the coordinates and located him in Guatemala, and the magazine removed the photo. It is the standard example of a geotag giving away a location the subject was hiding.</p>
        <h2>Risk by situation</h2>
        <table>
          <thead><tr><th>Situation</th><th>Risk</th><th>Why</th></tr></thead>
          <tbody>
            <tr><td>Sending an original by email or "as file" in a messenger</td><td>High</td><td>The file usually arrives unchanged, with tags</td></tr>
            <tr><td>Uploading to a classifieds or marketplace site</td><td>Depends</td><td>Behaviour differs per site; clean first if unsure</td></tr>
            <tr><td>Posting to a major social feed</td><td>Lower</td><td>Many strip EXIF from the public copy, but the original may be kept</td></tr>
            <tr><td>Photos of your home, kids' school or car</td><td>High</td><td>A coordinate links the image to a real place</td></tr>
            <tr><td>Screenshots</td><td>Low</td><td>Typically no GPS</td></tr>
          </tbody>
        </table>
        <h2>Simple routine</h2>
        <ol>
          <li>Check: <a href="../../how-to/check-if-photo-has-location/">does the photo have location</a>.</li>
          <li>Remove location or all metadata: <a href="../../how-to/remove-location-from-photos-iphone/">on iPhone</a> or in the <a href="../../remove-gps/">browser</a>.</li>
          <li>Share the cleaned copy, not the original.</li>
        </ol>
        <p>{NAME} does this on-device and keeps your original. For platform behaviour see <a href="../which-apps-remove-photo-metadata/">which apps remove photo metadata</a> and <a href="../can-photo-metadata-reveal-your-location/">can a photo reveal your location</a>.</p>""",
        faqs=[
            ("Can someone find my home from a photo?", "If the original file has GPS tags and you share it unchanged, yes. Remove location before sharing photos taken at home."),
            ("Do social networks show my EXIF to others?", "Major platforms generally strip it from the public copy, but behaviour varies and the original may be stored, so do not rely on it."),
            ("Is it enough to turn off Location Services?", "It stops new GPS tags. Photos already taken keep theirs until you remove them."),
            ("Does EXIF contain my name?", "Only if a camera or app wrote Artist or Copyright fields. Most phones do not."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
        priority=True,
    )

    # 5 ---------------------------------------------------------------
    article_page(
        "learn/photo-metadata-faq",
        title="Photo Metadata FAQ: 12 Short Answers | EXIF+",
        description="Twelve short, direct answers about photo metadata: what EXIF is, whether it holds location, how to see it, how to remove it, and what stays.",
        h1="Photo metadata FAQ",
        lead="Twelve questions people ask most, each answered in two sentences or less.",
        updated=UPDATED,
        prose=f"""        <h2>What is photo metadata?</h2>
        <p>Data stored inside an image file that describes it: camera, settings, date and sometimes location. The main standards are EXIF and IPTC.</p>
        <h2>What is EXIF?</h2>
        <p>A tag block written by cameras and phones that records device, shot settings, time and, if enabled, GPS. See <a href="../what-is-exif/">what is EXIF</a>.</p>
        <h2>Do photos contain my location?</h2>
        <p>Only if Location Services was on for the camera app. Check with <a href="../../how-to/check-if-photo-has-location/">this guide</a>.</p>
        <h2>How do I see a photo's metadata on iPhone?</h2>
        <p>Swipe up in Photos for basics, or use an app for the full list. Steps: <a href="../../how-to/view-exif-on-iphone/">view EXIF on iPhone</a>.</p>
        <h2>How do I remove metadata on iPhone?</h2>
        <p>Use an app that saves a cleaned copy, such as {NAME}, or turn off Location in the share sheet for a single send. See <a href="../../how-to/remove-photo-metadata-iphone/">remove photo metadata on iPhone</a>.</p>
        <h2>Does removing metadata change the picture?</h2>
        <p>Not visibly in normal use, but the file is rewritten and may be recompressed. See <a href="../does-cleaning-reduce-quality/">does cleaning reduce quality</a>.</p>
        <h2>Do screenshots have EXIF?</h2>
        <p>Usually very little and no GPS. See <a href="../does-screenshot-have-exif/">screenshot metadata</a>.</p>
        <h2>Do messengers and social apps strip it?</h2>
        <p>Often from the displayed copy, rarely from files sent as documents. See <a href="../which-apps-remove-photo-metadata/">which apps remove metadata</a>.</p>
        <h2>Is HEIC different from JPEG for metadata?</h2>
        <p>Both store EXIF and GPS; the container differs. See <a href="../heic-vs-jpeg-metadata/">HEIC vs JPEG metadata</a>.</p>
        <h2>Do social networks remove it for me?</h2>
        <p>It depends on the service and how you send the file. See <a href="../does-twitter-x-remove-exif/">does X (Twitter) strip EXIF data</a> and <a href="../which-apps-remove-photo-metadata/">which apps remove photo metadata</a>.</p>
        <h2>Can I edit metadata instead of deleting it?</h2>
        <p>Yes: date, location, camera and author fields can be changed. See <a href="../../compare/remove-vs-edit-exif/">remove vs edit</a>.</p>
        <h2>What is the difference between EXIF and IPTC?</h2>
        <p>EXIF is mostly technical and device-written; IPTC holds descriptive and rights text such as caption and copyright. See <a href="../exif-vs-iptc/">EXIF vs IPTC</a>.</p>
        <h2>Is there a free way to do this?</h2>
        <p>Yes: the <a href="../../exif-viewer/">browser viewer</a>, the <a href="../../remove-exif/">browser remover</a>, and single-photo remove in the app. Batch needs Premium, see <a href="../../app/free-vs-premium/">free vs Premium</a>.</p>""",
        faqs=[
            ("What is photo metadata?", "Data stored inside an image file that describes it, such as camera, settings, date and sometimes location."),
            ("Can photo metadata reveal where I live?", "Yes, if the original file has GPS tags from photos taken at home and you share it unchanged."),
            ("How do I remove metadata from photos?", f"Use a metadata remover: the browser tools on this site, or {NAME} on iPhone."),
            ("Do I lose the original when I clean a photo?", f"Not in {NAME}: cleaned photos are saved as new Library items and the original is kept."),
        ],
        nav="Learn",
        parent=("Learn", "learn/"),
    )
