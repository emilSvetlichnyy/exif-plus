# Indexation checklist — EXIF+

Property: `https://emilsvetlichnyy.app/exif-plus/`

## GitHub Pages
1. Repo Settings → Pages → Deploy from branch `main` / root (or `/docs` if you move it).
2. Confirm: https://emilsvetlichnyy.app/exif-plus/

## Google Search Console
1. Add URL-prefix property: `https://emilsvetlichnyy.app/exif-plus/`
2. Verify ownership (HTML file upload or meta tag).
3. Sitemaps → submit: `https://emilsvetlichnyy.app/exif-plus/sitemap.xml`
4. URL Inspection → Request indexing for:
   - `https://emilsvetlichnyy.app/exif-plus/`
   - `https://emilsvetlichnyy.app/exif-plus/remove-exif/`
   - `https://emilsvetlichnyy.app/exif-plus/exif-viewer/`
   - `https://emilsvetlichnyy.app/exif-plus/remove-gps/`
   - `https://emilsvetlichnyy.app/exif-plus/learn/what-is-exif/`
   - `https://emilsvetlichnyy.app/exif-plus/how-to/remove-location-from-photos-iphone/`
   - `https://emilsvetlichnyy.app/exif-plus/about/`

## Bing Webmaster Tools
1. Import from GSC or add the site.
2. Submit the same sitemap.
3. IndexNow key file: `https://emilsvetlichnyy.app/exif-plus/29dcae78f2825b290fd2b9eea7068062.txt`
4. After content pushes: `python3 scripts/indexnow_ping.py`

## Done when
`site:emilsvetlichnyy.app/exif-plus` returns URLs in Google or Bing.
