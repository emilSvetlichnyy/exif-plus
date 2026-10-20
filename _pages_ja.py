"""Japanese (ja) pages: /ja/, /ja/remove-exif/, /ja/remove-gps/. Called from _build.main()."""
from __future__ import annotations


def register_ja(ctx: dict) -> None:
    page_shell = ctx["page_shell"]
    register = ctx["register"]
    esc = ctx["esc"]
    BASE = ctx["BASE"]
    NAME = ctx["NAME"]
    APP_JP = ctx["APP"].replace("/us/", "/jp/")
    PRIVACY = ctx["PRIVACY"]

    def appstore_btn() -> str:
        return (
            f'<a class="appstore" href="{APP_JP}" target="_blank" rel="noopener noreferrer" '
            f'aria-label="App Storeでダウンロード">{ctx["APPSTORE_SVG"]}'
            '<span class="appstore__text"><span class="appstore__small">ダウンロード</span>'
            '<span class="appstore__big">App Store</span></span></a>'
        )

    def nav(prefix: str) -> str:
        return (
            '<nav class="nav-links" aria-label="メニュー">'
            f'<a href="{prefix}ja/remove-exif/">Exif削除</a>'
            f'<a href="{prefix}ja/remove-gps/">位置情報削除</a>'
            f'<a href="{APP_JP}" rel="noopener noreferrer">アプリ</a>'
            f'<a href="{prefix}">English</a>'
            "</nav>"
        )

    def footer(prefix: str) -> str:
        return f"""    <footer class="site-footer">
      <nav aria-label="フッター">
        <a href="{prefix}ja/">ホーム</a>
        <a href="{prefix}ja/remove-exif/">Exif削除</a>
        <a href="{prefix}ja/remove-gps/">位置情報削除</a>
        <a href="{prefix}">English</a>
        <a href="{PRIVACY}" rel="noopener noreferrer">プライバシーポリシー</a>
      </nav>
      <p>© {NAME} — iPhoneで写真のメタデータを表示・編集・削除。</p>
    </footer>"""

    def faq_html(pairs):
        items = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in pairs)
        return f'<section class="section faq"><div class="section-head"><h2>よくある質問</h2></div>{items}</section>'

    def faq_ld(pairs):
        d = ctx["faq_ld"](pairs)
        d["inLanguage"] = "ja"
        return d

    def tool_panel(mode: str, title: str, blurb: str) -> str:
        download = ""
        if mode in ("remove", "gps"):
            download = '<button type="button" class="btn btn-primary tool-download" hidden>加工後の画像をダウンロード</button>'
        return f"""      <section class="tool-panel" data-exif-tool data-mode="{mode}" aria-label="{esc(title)}">
        <h2 style="margin:0 0 6px;font-family:var(--display);font-size:1.35rem;">{esc(title)}</h2>
        <p class="lead-sm">{esc(blurb)} 写真はこのタブの中だけで処理され、サーバーには送信されません。</p>
        <div class="dropzone" role="button" tabindex="0">
          <strong>ここに写真をドロップ</strong>
          <span>またはクリックして選択（JPEG / PNG / WebP）</span>
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

    def cta(prefix: str) -> str:
        return f"""      <section class="section cta-band">
        <div class="section-head"><h2>iPhoneアプリで、もっと手軽に</h2></div>
        <p class="lead-sm">EXIF+は、写真のExif・IPTC・位置情報（GPS）をiPhone上で表示・編集・削除するアプリです。処理は端末内で行い、加工した写真は新しい写真として保存されるため、元の写真は変更されません。ダウンロードは無料で、1枚ずつの編集・削除は無料、一括処理は Premium です。</p>
        <div class="actions">{appstore_btn()}</div>
      </section>"""

    def build(rel, title, description, h1, lead, main_inner, faqs, crumbs, extra_schemas, include_tool, og):
        prefix = "../" * (len(rel.strip("/").split("/")) if rel else 0)
        crumb_html = '<nav class="breadcrumbs" aria-label="パンくず">' + (
            f'<a href="{prefix}ja/">ホーム</a>' + (f'<span class="crumb-sep" aria-hidden="true">›</span><span aria-current="page">{esc(crumbs)}</span>' if crumbs else "")
        ) + "</nav>"
        body = f"""    {crumb_html}
    <main>
      <section class="hero">
        <h1>{esc(h1)}</h1>
        <p class="lead">{esc(lead)}</p>
        <div class="actions">{appstore_btn()}</div>
      </section>
{main_inner}
      {faq_html(faqs)}
{cta(prefix)}
    </main>"""
        crumb_items = [("ホーム", f"{BASE}/ja/")] + ([(crumbs, f"{BASE}/{rel}/")] if crumbs else [])
        schemas = [ctx["org_ld"](), ctx["breadcrumb_ld"](crumb_items), faq_ld(faqs)] + extra_schemas
        html = page_shell(
            rel=rel,
            title=title,
            description=description,
            canonical_path=f"{rel}/",
            body=body,
            schemas=schemas,
            nav_current=None,
            og_image=og,
            include_tool=include_tool,
            lang="ja",
        )
        # swap English chrome (nav/footer/brand) for Japanese
        import re

        html = re.sub(r'<nav class="nav-links".*?</nav>', nav(prefix), html, count=1, flags=re.S)
        html = re.sub(r'<footer class="site-footer">.*?</footer>', footer(prefix).strip(), html, count=1, flags=re.S)
        html = html.replace(f'<a class="brand" href="{prefix}">', f'<a class="brand" href="{prefix}ja/">')
        html = html.replace(f'<link rel="stylesheet" href="{prefix}styles.css">', f'<link rel="stylesheet" href="{prefix}styles.css">')
        register({"rel": rel, "html": html, "title": h1, "priority": True})

    # ---------- /ja/ ----------
    faq_home = [
        ("EXIF+とは何ですか？", "EXIF+は、写真のExif・IPTC・位置情報（GPS）をiPhone・iPad上で表示・編集・削除するアプリです。このサイトでは、ブラウザ内だけで動く無料の確認・削除ツールも使えます。"),
        ("写真はサーバーにアップロードされますか？", "いいえ。ブラウザのツールは、選んだ写真をこのタブの中だけで処理します。アプリも、写真の表示・編集・削除をiPhone上で行います。"),
        ("元の写真は書き換えられますか？", "いいえ。アプリで編集・削除した写真は、新しい写真として写真ライブラリに保存されます。元の写真は、ご自身で削除しない限り残ります。"),
        ("無料で使えますか？", "ダウンロードは無料です。メタデータの表示と、1枚ずつの編集・削除は無料です。複数の写真をまとめて処理する一括機能と、共有時の自動削除は Premium です。"),
        ("動画にも対応していますか？", "いいえ。動画のメタデータには対応していません。対象は写真です。"),
        ("画質は落ちますか？", "メタデータそのものは画質に影響しませんが、削除した写真を保存し直すときに再エンコードされることがあります。元の写真を残しておけば、いつでも元に戻せます。"),
    ]
    home_main = """      <section class="section">
        <div class="section-head"><h2>要点</h2></div>
        <ul>
          <li><strong>何ができる：</strong>写真に隠れた位置情報（GPS）・撮影日時・カメラ情報を確認して消せます。</li>
          <li><strong>どこで処理：</strong>ブラウザのタブ内、またはiPhone上。サーバーには送りません。</li>
          <li><strong>元の写真：</strong>変更されません。加工後は新しい写真として保存されます。</li>
          <li><strong>料金：</strong>ダウンロード無料。1枚ずつの編集・削除は無料、一括処理は Premium。</li>
        </ul>
      </section>
      <section class="section">
        <div class="section-head"><h2>ツール</h2></div>
        <div class="tiles">
          <a class="tile" href="remove-exif/"><h3>Exifを削除</h3><p>ブラウザで写真のメタデータを消して、加工後の画像を保存。</p></a>
          <a class="tile" href="remove-gps/"><h3>位置情報（GPS）を削除</h3><p>SNS投稿やフリマ出品の前に、撮影場所の情報を消す。</p></a>
        </div>
      </section>
      <section class="section">
        <div class="section-head"><h2>こんなときに</h2></div>
        <ul>
          <li>SNSに投稿する前に、自宅や職場が写真から特定されないようにしたい。</li>
          <li>フリマに出品する写真から、撮影場所や撮影日時を消したい。</li>
          <li>写真にどんな情報が入っているか確認したい。</li>
        </ul>
      </section>"""
    build(
        "ja",
        "写真の位置情報・Exifを消す｜無料・ブラウザ内で完結 | EXIF+",
        "写真の位置情報（GPS）やExifを無料で確認・削除。写真はブラウザ内で処理され、アップロードされません。iPhoneアプリ EXIF+ なら一括処理も。",
        "写真の位置情報・Exifを消す（無料・ブラウザ内で完結）",
        "EXIF+は、写真に隠れた位置情報（GPS）や撮影日時を確認して消せるツールとiPhoneアプリです。処理は端末内で行い、元の写真は変更されません。",
        home_main,
        faq_home,
        "",
        [ctx["software_ld"]() | {"inLanguage": "ja", "url": APP_JP, "downloadUrl": APP_JP}],
        False,
        "home.png",
    )

    # ---------- /ja/remove-exif/ ----------
    faq_exif = [
        ("ブラウザでExifを削除するとアップロードされますか？", "いいえ。選んだ写真はこのタブの中だけで処理され、サーバーには送信されません。"),
        ("削除すると画質は落ちますか？", "メタデータは見た目に影響しませんが、削除した写真は再エンコードして保存されるため、わずかに変わることがあります。元の写真は手元に残してください。"),
        ("HEIC写真は使えますか？", "多くのブラウザはHEICを読み込めません。iPhoneのカメラロールにあるHEIC写真は、EXIF+アプリで処理してください。"),
        ("Exifを消すと何が消えますか？", "カメラの機種、レンズ、撮影日時、位置情報（GPS）など、写真に埋め込まれた撮影情報が消えます。"),
    ]
    exif_main = tool_panel("remove", "Exifを削除（ブラウザ内）", "写真を選ぶと、含まれているメタデータを表示し、削除した画像を保存できます。") + """
      <section class="section">
        <div class="section-head"><h2>Exifとは</h2></div>
        <p>Exifは、写真に自動で埋め込まれる撮影情報です。カメラの機種、撮影日時、位置情報（GPS）などが含まれ、共有した相手にも見えることがあります。SNSやフリマに載せる前に、不要な情報は消しておくと安心です。</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>手順</h2></div>
        <ol>
          <li>上のツールに写真をドロップするか、クリックして選びます。</li>
          <li>表示されたメタデータを確認します。</li>
          <li>「加工後の画像をダウンロード」で、メタデータを消した画像を保存します。</li>
        </ol>
      </section>"""
    build(
        "ja/remove-exif",
        "Exif削除｜写真のメタデータを無料で消す（ブラウザ内） | EXIF+",
        "写真のExif・メタデータをブラウザ内で無料削除。アップロード不要で、撮影日時・カメラ情報・位置情報を消せます。iPhoneアプリで一括処理も。",
        "写真のExifを削除する（無料・アップロード不要）",
        "写真に埋め込まれたExif・メタデータを、ブラウザの中だけで確認して削除できます。写真はサーバーに送られません。",
        exif_main,
        faq_exif,
        "Exif削除",
        [ctx["webapp_ld"]("Exif削除ツール", "写真のExifをブラウザ内で削除する無料ツール", f"{BASE}/ja/remove-exif/") | {"inLanguage": "ja"}],
        True,
        "remove-exif.png",
    )

    # ---------- /ja/remove-gps/ ----------
    faq_gps = [
        ("写真から位置情報を消すには？", "上のツールに写真を入れると、位置情報（GPS）の有無を確認でき、位置情報を消した画像を保存できます。iPhoneでは、EXIF+アプリでも同じことができます。"),
        ("位置情報を消すと、写真の撮影場所は分からなくなりますか？", "写真に埋め込まれた座標は消えます。ただし、写真に写っている景色や看板から場所が分かる場合があります。"),
        ("SNSに投稿すると位置情報は自動で消えますか？", "サービスによって異なります。確実に消したい場合は、投稿前にご自身で位置情報を削除しておくと安心です。"),
        ("フリマに出品する写真も消したほうがいいですか？", "自宅で撮影した写真には自宅の座標が入っていることがあります。出品前に位置情報を消しておくと安心です。"),
    ]
    gps_main = tool_panel("gps", "位置情報（GPS）を削除（ブラウザ内）", "写真の位置情報を確認し、消した画像を保存できます。") + """
      <section class="section">
        <div class="section-head"><h2>位置情報（GPS）が写真に入る仕組み</h2></div>
        <p>iPhoneのカメラで位置情報サービスが有効だと、写真に撮影場所の緯度・経度が記録されます。この座標が残ったまま共有すると、自宅や職場の場所が分かってしまうことがあります。</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>共有前のチェック</h2></div>
        <ul>
          <li>自宅・職場・学校で撮った写真は、位置情報を消してから共有する。</li>
          <li>フリマ出品や、知らない人に送る写真も同様。</li>
          <li>撮影日時も消したい場合は、<a href="../remove-exif/">Exif削除</a>を使う。</li>
        </ul>
      </section>"""
    build(
        "ja/remove-gps",
        "写真の位置情報（GPS）を削除｜無料・ブラウザ内で完結 | EXIF+",
        "写真の位置情報（GPS・ジオタグ）をブラウザ内で無料削除。SNS投稿やフリマ出品の前に、撮影場所の情報を消せます。写真はアップロードされません。",
        "写真の位置情報（GPS）を削除する",
        "SNS投稿やフリマ出品の前に、写真に埋め込まれた撮影場所の情報を確認して消せます。写真はブラウザの外に出ません。",
        gps_main,
        faq_gps,
        "位置情報削除",
        [ctx["webapp_ld"]("位置情報削除ツール", "写真の位置情報（GPS）をブラウザ内で削除する無料ツール", f"{BASE}/ja/remove-gps/") | {"inLanguage": "ja"}],
        True,
        "remove-gps.png",
    )
