"""Localized pages for ko / de / es, modelled on _pages_ja.py. Called from _build.main().

Each language gets the same set of pages (slugs mirror the English site so hreflang
groups in _build.I18N_GROUPS line up):
  /{lang}/                                         home
  /{lang}/remove-exif/                             browser metadata remover
  /{lang}/remove-gps/                              browser location remover
  /{lang}/exif-viewer/                             browser EXIF viewer
  /{lang}/how-to/remove-location-from-photos-iphone/
  /{lang}/learn/does-<messenger>-remove-exif/      KakaoTalk (ko), WhatsApp (de, es)

Text is written for the searches people use in that country, not translated line by line.
Inside page HTML, "{L}" is replaced with the relative path to the language root.
"""
from __future__ import annotations

import re

# ---------------------------------------------------------------- locales

LOCALES: dict[str, dict] = {}

# ======================================================================== ko
LOCALES["ko"] = {
    "store": "kr",
    "lang_name": "한국어",
    "ui": {
        "appstore_aria": "App Store에서 다운로드",
        "appstore_small": "다운로드",
        "nav_aria": "메뉴",
        "nav": [("remove-gps/", "사진 위치 삭제"), ("remove-exif/", "메타데이터 삭제"), ("exif-viewer/", "EXIF 뷰어")],
        "nav_app": "앱",
        "footer_aria": "푸터",
        "home": "홈",
        "privacy": "개인정보 처리방침",
        "tagline": "iPhone에서 사진 메타데이터 보기·편집·삭제.",
        "crumb_aria": "경로",
        "faq": "자주 묻는 질문",
        "drop_strong": "여기에 사진을 끌어다 놓기",
        "drop_span": "또는 클릭해서 선택 (JPEG / PNG / WebP)",
        "download": "정리된 사진 다운로드",
        "local_note": "사진은 이 탭 안에서만 처리되며 서버로 전송되지 않습니다.",
        "cta_h": "iPhone 앱으로 더 간편하게",
        "cta_p": "EXIF+는 iPhone에서 사진의 EXIF·IPTC·위치 정보(GPS)를 보고, 편집하고, 삭제하는 앱입니다. 처리는 기기 안에서 이루어지고, 정리한 사진은 새 사진으로 저장되므로 원본은 그대로 남습니다. 다운로드는 무료이며 한 장씩 편집·삭제는 무료, 여러 장 일괄 처리는 Premium입니다.",
        "related": "관련 페이지",
    },
    "llms": [
        ("", "홈: 사진 위치 정보·메타데이터 삭제"),
        ("remove-gps/", "사진 위치 삭제 (브라우저)"),
        ("remove-exif/", "메타데이터·EXIF 삭제 (브라우저)"),
        ("exif-viewer/", "EXIF 뷰어 (브라우저)"),
        ("how-to/remove-location-from-photos-iphone/", "iPhone 사진 위치 정보 삭제 방법"),
        ("learn/does-kakaotalk-remove-exif/", "카카오톡으로 보내면 위치 정보가 지워지나요?"),
    ],
}
LOCALES["ko"]["pages"] = [
    {
        "slug": "",
        "title": "사진 위치 정보·메타데이터 삭제｜무료, 업로드 없음 | EXIF+",
        "description": "사진에 숨은 위치 정보(GPS)와 EXIF 메타데이터를 무료로 확인하고 삭제하세요. 사진은 브라우저 안에서만 처리됩니다. iPhone 앱 EXIF+로 여러 장도 한 번에.",
        "h1": "사진 위치 정보·메타데이터 삭제 (무료, 업로드 없음)",
        "lead": "EXIF+는 사진에 숨은 위치 정보(GPS), 촬영 날짜, 카메라 정보를 확인하고 지우는 무료 도구이자 iPhone 앱입니다. 처리는 기기 안에서 이루어지고 원본 사진은 바뀌지 않습니다.",
        "crumb": "",
        "tool": None,
        "og": "home.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>핵심 요약</h2></div>
        <ul>
          <li><strong>무엇을:</strong> 사진에 기록된 위치 정보(GPS), 촬영 날짜, 카메라 정보를 확인하고 삭제합니다.</li>
          <li><strong>어디서:</strong> 브라우저 탭 안 또는 iPhone 안. 서버로 보내지 않습니다.</li>
          <li><strong>원본:</strong> 바뀌지 않습니다. 정리한 사진은 새 사진으로 저장됩니다.</li>
          <li><strong>요금:</strong> 다운로드 무료. 한 장씩 편집·삭제는 무료, 일괄 처리는 Premium.</li>
        </ul>
      </section>
      <section class="section">
        <div class="section-head"><h2>도구</h2></div>
        <div class="tiles">
          <a class="tile" href="{L}remove-gps/"><h3>사진 위치 삭제</h3><p>SNS·중고거래 올리기 전에 촬영 장소 정보를 지웁니다.</p></a>
          <a class="tile" href="{L}remove-exif/"><h3>메타데이터 삭제</h3><p>EXIF 전체를 지우고 깨끗한 사진을 저장합니다.</p></a>
          <a class="tile" href="{L}exif-viewer/"><h3>EXIF 뷰어</h3><p>사진에 어떤 정보가 들어 있는지 확인합니다.</p></a>
          <a class="tile" href="{L}how-to/remove-location-from-photos-iphone/"><h3>iPhone에서 위치 삭제</h3><p>앨범 사진의 위치 정보를 지우는 방법.</p></a>
        </div>
      </section>
      <section class="section">
        <div class="section-head"><h2>이럴 때 쓰세요</h2></div>
        <ul>
          <li>당근마켓·번개장터에 올릴 사진에서 집 위치를 지우고 싶을 때.</li>
          <li>인스타그램·블로그에 올리기 전에 촬영 장소와 날짜를 숨기고 싶을 때.</li>
          <li>카카오톡으로 <a href="{L}learn/does-kakaotalk-remove-exif/">원본 사진</a>을 보내기 전에.</li>
        </ul>
      </section>""",
        "faqs": [
            ("EXIF+는 무엇인가요?", "EXIF+는 iPhone·iPad에서 사진의 EXIF·IPTC·위치 정보(GPS)를 보고, 편집하고, 삭제하는 앱입니다. 이 사이트에서는 브라우저 안에서만 동작하는 무료 확인·삭제 도구도 쓸 수 있습니다."),
            ("사진이 서버에 업로드되나요?", "아니요. 브라우저 도구는 선택한 사진을 이 탭 안에서만 처리합니다. 앱도 사진을 iPhone 안에서 처리합니다."),
            ("원본 사진이 바뀌나요?", "아니요. 앱에서 편집·삭제한 사진은 새 사진으로 사진 보관함에 저장됩니다. 원본은 직접 지우지 않는 한 남아 있습니다."),
            ("무료인가요?", "다운로드는 무료입니다. 메타데이터 보기와 한 장씩 편집·삭제는 무료이고, 여러 장을 한 번에 처리하는 일괄 기능과 공유 시 자동 삭제는 Premium입니다."),
            ("동영상도 되나요?", "아니요. 동영상 메타데이터는 지원하지 않습니다. 사진만 대상입니다."),
        ],
    },
    {
        "slug": "remove-gps",
        "title": "사진 위치 삭제｜위치 정보(GPS) 무료로 지우기 | EXIF+",
        "description": "사진 위치 정보(GPS·지오태그)를 브라우저에서 무료로 삭제하세요. 업로드 없이 촬영 장소 좌표를 지우고 깨끗한 사진을 저장합니다. iPhone은 EXIF+ 앱으로.",
        "h1": "사진 위치 삭제 (위치 정보·GPS 지우기)",
        "lead": "SNS나 중고거래에 올리기 전에, 사진에 기록된 촬영 장소 좌표를 확인하고 지울 수 있습니다. 사진은 브라우저 밖으로 나가지 않습니다.",
        "crumb": "사진 위치 삭제",
        "tool": ("gps", "사진 위치 삭제 (브라우저)", "사진의 위치 정보 유무를 확인하고, 위치를 지운 사진을 저장할 수 있습니다."),
        "og": "remove-gps.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>사진에 위치가 기록되는 이유</h2></div>
        <p>iPhone 카메라에 위치 서비스가 켜져 있으면 사진마다 촬영 장소의 위도·경도가 저장됩니다. 이 좌표가 남은 채로 공유하면 집이나 회사 위치가 드러날 수 있습니다.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>올리기 전 체크</h2></div>
        <ul>
          <li>집·회사·학교에서 찍은 사진은 위치를 지우고 공유하기.</li>
          <li>당근마켓 등 중고거래 사진, 모르는 사람에게 보내는 사진도 마찬가지.</li>
          <li>촬영 날짜·카메라 정보까지 지우려면 <a href="{L}remove-exif/">메타데이터 삭제</a>를 사용하기.</li>
          <li>iPhone 앨범 사진은 <a href="{L}how-to/remove-location-from-photos-iphone/">iPhone에서 위치 삭제하는 방법</a>을 참고하기.</li>
        </ul>
      </section>""",
        "faqs": [
            ("사진 위치 정보는 어떻게 지우나요?", "위 도구에 사진을 넣으면 위치 정보(GPS)가 있는지 확인하고, 위치를 지운 사진을 저장할 수 있습니다. iPhone에서는 EXIF+ 앱으로 같은 작업을 할 수 있습니다."),
            ("위치를 지우면 촬영 장소를 전혀 알 수 없나요?", "사진 파일에 저장된 좌표는 사라집니다. 다만 사진에 찍힌 풍경이나 간판으로 장소를 알 수 있는 경우가 있습니다."),
            ("SNS에 올리면 위치 정보가 자동으로 지워지나요?", "서비스마다 다릅니다. 확실히 지우려면 올리기 전에 직접 위치 정보를 삭제하는 것이 안전합니다."),
            ("HEIC 사진도 되나요?", "대부분의 브라우저는 HEIC를 읽지 못합니다. iPhone 앨범의 HEIC 사진은 EXIF+ 앱에서 처리하세요."),
        ],
    },
    {
        "slug": "remove-exif",
        "title": "메타데이터 삭제｜사진 EXIF 무료로 지우기 (업로드 없음) | EXIF+",
        "description": "사진 메타데이터(EXIF)를 브라우저에서 무료로 삭제하세요. 촬영 날짜, 카메라 정보, 위치 정보를 업로드 없이 지웁니다. iPhone 앱으로 여러 장도 한 번에.",
        "h1": "사진 메타데이터 삭제 (EXIF 지우기, 업로드 없음)",
        "lead": "사진에 저장된 EXIF 메타데이터를 브라우저 안에서만 확인하고 삭제할 수 있습니다. 사진은 서버로 보내지 않습니다.",
        "crumb": "메타데이터 삭제",
        "tool": ("remove", "메타데이터 삭제 (브라우저)", "사진을 고르면 들어 있는 메타데이터를 보여 주고, 지운 사진을 저장할 수 있습니다."),
        "og": "remove-exif.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>EXIF 메타데이터란</h2></div>
        <p>EXIF는 사진에 자동으로 저장되는 촬영 정보입니다. 카메라·휴대폰 기종, 촬영 날짜와 시간, 위치 정보(GPS) 등이 들어 있고, 사진을 받은 사람도 볼 수 있습니다.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>삭제 방법</h2></div>
        <ol>
          <li>위 도구에 사진을 끌어다 놓거나 클릭해서 고릅니다.</li>
          <li>표시된 메타데이터를 확인합니다.</li>
          <li>다운로드 버튼으로 메타데이터를 지운 사진을 저장합니다.</li>
        </ol>
        <p>위치만 지우고 싶다면 <a href="{L}remove-gps/">사진 위치 삭제</a>, 먼저 내용만 보고 싶다면 <a href="{L}exif-viewer/">EXIF 뷰어</a>를 쓰세요.</p>
      </section>""",
        "faqs": [
            ("브라우저에서 삭제하면 사진이 업로드되나요?", "아니요. 고른 사진은 이 탭 안에서만 처리되고 서버로 전송되지 않습니다."),
            ("메타데이터를 지우면 화질이 떨어지나요?", "메타데이터 자체는 화질과 관계없지만, 지운 사진을 다시 저장할 때 재인코딩되어 약간 달라질 수 있습니다. 원본은 따로 보관하세요."),
            ("EXIF를 지우면 무엇이 사라지나요?", "기종, 렌즈, 촬영 날짜, 위치 정보(GPS) 등 사진에 들어 있던 촬영 정보가 사라집니다."),
            ("여러 장을 한 번에 지울 수 있나요?", "브라우저 도구는 한 장씩입니다. iPhone 앱 EXIF+의 Premium 일괄 처리로 여러 장을 한 번에 정리할 수 있습니다."),
        ],
    },
    {
        "slug": "exif-viewer",
        "title": "EXIF 뷰어｜사진 메타데이터 확인 (무료, 업로드 없음) | EXIF+",
        "description": "무료 EXIF 뷰어로 사진의 촬영 날짜, 카메라·렌즈, ISO, 위치 정보(GPS)를 확인하세요. 사진은 브라우저 안에서만 읽습니다. iPhone은 EXIF+ 앱으로.",
        "h1": "EXIF 뷰어 (사진 정보 확인)",
        "lead": "사진에 숨은 EXIF 정보를 무료로 확인하세요. 촬영 날짜, 카메라와 렌즈, 노출 설정, 위치 정보(GPS)를 보여 줍니다. 사진은 업로드되지 않습니다.",
        "crumb": "EXIF 뷰어",
        "tool": ("view", "EXIF 뷰어 (브라우저)", "사진을 고르면 읽을 수 있는 EXIF·IPTC·GPS 항목을 보여 줍니다."),
        "og": "exif-viewer.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>확인할 수 있는 정보</h2></div>
        <p>촬영 날짜와 시간, 카메라·휴대폰 기종, 렌즈, ISO, 조리개, 셔터 속도, 편집 소프트웨어, 저작권, 그리고 기록되어 있다면 위치 정보(위도·경도).</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>확인한 다음에는</h2></div>
        <p>공유하고 싶지 않은 위치가 보이면 <a href="{L}remove-gps/">사진 위치 삭제</a>, 정보를 전부 지우려면 <a href="{L}remove-exif/">메타데이터 삭제</a>를 쓰세요. iPhone 앨범 사진은 EXIF+ 앱에서 바로 보고 편집할 수 있습니다.</p>
      </section>""",
        "faqs": [
            ("사진 EXIF 정보는 어떻게 보나요?", "이 페이지에서 JPEG·PNG·WebP 사진을 고르면 항목이 표시됩니다. iPhone 앨범 사진과 HEIC는 EXIF+ 앱에서 확인하세요."),
            ("위치 정보가 안 보이는 이유는?", "촬영할 때 위치 서비스가 꺼져 있었거나, 이미 지워졌거나, 다른 앱이 위치 없이 다시 저장했을 수 있습니다."),
            ("EXIF를 확인하는 것은 안전한가요?", "파일은 브라우저 안에서만 읽고 표시합니다. 서버로 업로드하지 않습니다."),
            ("뷰어에서 바로 편집할 수 있나요?", "브라우저 도구로는 편집할 수 없습니다. 편집은 iPhone 앱 EXIF+에서, 삭제는 메타데이터 삭제 도구에서 할 수 있습니다."),
        ],
    },
    {
        "slug": "how-to/remove-location-from-photos-iphone",
        "title": "아이폰 사진 위치 정보 삭제 방법 (원본 유지) | EXIF+",
        "description": "아이폰 사진의 위치 정보를 지우는 방법: 공유할 때 위치 끄기, EXIF+ 앱으로 위치를 지운 사본 저장. 원본은 그대로, 여러 장은 일괄 처리로.",
        "h1": "아이폰 사진 위치 정보 삭제 방법",
        "lead": "아이폰 사진의 위치 정보는 두 가지 방법으로 지울 수 있습니다. 한 번 보낼 때만 지우는 iOS 공유 옵션, 그리고 위치를 지운 사진을 새로 저장하는 EXIF+ 앱입니다.",
        "crumb": "아이폰 사진 위치 삭제",
        "tool": None,
        "og": "on-iphone.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>방법 1. 공유할 때 위치 끄기 (iOS 기본)</h2></div>
        <ol>
          <li>사진 앱에서 사진을 고르고 공유 버튼을 누릅니다.</li>
          <li>위쪽의 「옵션」을 누릅니다.</li>
          <li>「위치」를 끄고 완료를 누른 뒤 공유합니다.</li>
        </ol>
        <p>이번 공유에만 적용되고, 앨범의 사진에는 위치가 그대로 남습니다. 앱이나 보내는 방식에 따라 옵션이 보이지 않을 수 있습니다.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>방법 2. EXIF+ 앱으로 위치를 지운 사진 저장</h2></div>
        <ol>
          <li>App Store에서 EXIF+를 설치하고 사진 접근을 허용합니다.</li>
          <li>사진을 열고 위치(GPS) 항목을 확인합니다.</li>
          <li>위치를 지우거나 메타데이터 전체를 삭제하고 저장합니다.</li>
          <li>새로 저장된 사진을 공유합니다. 원본은 바뀌지 않습니다.</li>
        </ol>
        <p>컴퓨터에 있는 파일 한 장이라면 <a href="{L}remove-gps/">브라우저 위치 삭제 도구</a>로도 됩니다.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>앞으로 찍을 사진에 위치를 남기지 않으려면</h2></div>
        <p>설정 → 개인정보 보호 및 보안 → 위치 서비스 → 카메라에서 「안 함」을 고르면 새로 찍는 사진에 위치가 기록되지 않습니다. 이미 찍은 사진의 위치는 지워지지 않습니다.</p>
      </section>""",
        "faqs": [
            ("공유 옵션에서 위치를 끄면 원본에서도 지워지나요?", "아니요. 그 공유에서만 위치가 빠지고, 앨범의 원본에는 위치가 남아 있습니다."),
            ("위치만 지우는 것과 메타데이터 전체 삭제는 다른가요?", "네. EXIF+에서는 위치 항목만 지울 수도 있고, 카메라 정보와 촬영 날짜까지 모두 지울 수도 있습니다."),
            ("여러 장을 한 번에 지울 수 있나요?", "네. EXIF+ Premium의 여러 장 선택 일괄 삭제로 한 번에 처리할 수 있습니다."),
            ("HEIC 사진도 되나요?", "네. iPhone 앱에서는 사진 보관함의 HEIC 사진도 처리할 수 있습니다."),
        ],
    },
    {
        "slug": "learn/does-kakaotalk-remove-exif",
        "title": "카카오톡으로 사진 보내면 위치 정보가 지워질까? | EXIF+",
        "description": "카카오톡 일반 사진 전송은 압축되어 보통 위치 정보·EXIF가 사라집니다. 원본 화질이나 파일로 보내면 남을 수 있습니다. 보내기 전에 위치를 지우는 방법.",
        "h1": "카카오톡으로 사진을 보내면 위치 정보가 지워질까?",
        "lead": "짧은 답: 일반 화질로 보내면 사진이 압축되어 보통 위치 정보와 EXIF가 사라집니다. 원본 화질이나 파일로 보내면 원본 파일이 그대로 가서 위치가 남을 수 있습니다.",
        "crumb": "카카오톡 사진 위치 정보",
        "tool": None,
        "og": "home.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>보내는 방식별 정리</h2></div>
        <ul>
          <li><strong>일반 화질 사진 전송:</strong> 재압축되어 EXIF·GPS가 보통 사라집니다.</li>
          <li><strong>원본 화질 전송:</strong> 원본에 가깝게 보내므로 메타데이터가 남을 수 있습니다.</li>
          <li><strong>파일로 보내기:</strong> 원본 파일 그대로 전달되어 촬영 날짜·기종·위치가 보통 남습니다.</li>
        </ul>
        <p>카카오톡의 압축은 개인정보 보호 기능이 아니라 용량을 줄이는 과정의 부수 효과입니다. 설정이나 앱 버전에 따라 결과가 달라질 수 있습니다.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>안전하게 보내는 방법</h2></div>
        <p>먼저 지우고 보내세요. 컴퓨터라면 <a href="{L}remove-gps/">브라우저에서 위치 삭제</a>, iPhone이라면 <a href="{L}how-to/remove-location-from-photos-iphone/">아이폰 사진 위치 삭제 방법</a>을 따라 하세요. EXIF+는 정리한 사진을 새로 저장하므로 원본은 그대로입니다.</p>
      </section>""",
        "faqs": [
            ("카카오톡 사진에서 위치를 알 수 있나요?", "일반 화질로 받은 사진은 EXIF가 보통 지워져 있어 위치를 알기 어렵습니다. 원본 화질이나 파일로 받은 사진은 촬영 시 위치가 기록되었다면 알 수 있습니다."),
            ("원본으로 보내면 메타데이터가 남나요?", "남을 수 있습니다. 화질을 유지하려고 원본으로 보낼 때는 먼저 위치 정보를 지우세요."),
            ("받은 사진에 위치가 있는지 확인하려면?", "사진을 저장한 뒤 EXIF 뷰어로 열어 GPS 항목이 있는지 보면 됩니다."),
        ],
    },
]

# ======================================================================== de
LOCALES["de"] = {
    "store": "de",
    "lang_name": "Deutsch",
    "ui": {
        "appstore_aria": "Im App Store laden",
        "appstore_small": "Laden im",
        "nav_aria": "Menü",
        "nav": [("remove-gps/", "Standort entfernen"), ("remove-exif/", "Metadaten entfernen"), ("exif-viewer/", "EXIF anzeigen")],
        "nav_app": "App",
        "footer_aria": "Fußzeile",
        "home": "Start",
        "privacy": "Datenschutz",
        "tagline": "Foto-Metadaten auf dem iPhone anzeigen, bearbeiten und entfernen.",
        "crumb_aria": "Brotkrumen",
        "faq": "Häufige Fragen",
        "drop_strong": "Foto hierher ziehen",
        "drop_span": "oder klicken und auswählen (JPEG / PNG / WebP)",
        "download": "Bereinigtes Foto herunterladen",
        "local_note": "Das Foto wird nur in diesem Tab verarbeitet und nicht an einen Server gesendet.",
        "cta_h": "Noch einfacher mit der iPhone-App",
        "cta_p": "EXIF+ ist eine iPhone-App, mit der Sie EXIF-, IPTC- und Standortdaten (GPS) von Fotos anzeigen, bearbeiten und entfernen. Alles läuft auf dem Gerät. Bereinigte Fotos werden als neues Foto gespeichert, das Original bleibt unverändert. Der Download ist kostenlos, einzelne Fotos bearbeiten und bereinigen ist kostenlos, Stapelverarbeitung ist Premium.",
        "related": "Weiterlesen",
    },
    "llms": [
        ("", "Start: Standort und Metadaten aus Fotos entfernen"),
        ("remove-gps/", "Standort aus Foto entfernen (im Browser)"),
        ("remove-exif/", "Metadaten / EXIF entfernen (im Browser)"),
        ("exif-viewer/", "EXIF-Daten anzeigen (im Browser)"),
        ("how-to/remove-location-from-photos-iphone/", "Standort aus iPhone-Fotos entfernen"),
        ("learn/does-whatsapp-remove-exif/", "Entfernt WhatsApp Metadaten?"),
    ],
}
LOCALES["de"]["pages"] = [
    {
        "slug": "",
        "title": "Standort & Metadaten aus Fotos entfernen – kostenlos, ohne Upload | EXIF+",
        "description": "Standort (GPS) und EXIF-Metadaten aus Fotos kostenlos prüfen und entfernen. Das Foto bleibt im Browser, kein Upload. Mit der iPhone-App EXIF+ auch für viele Fotos auf einmal.",
        "h1": "Standort und Metadaten aus Fotos entfernen (kostenlos, ohne Upload)",
        "lead": "EXIF+ zeigt und entfernt versteckte Daten in Fotos: Standort (GPS), Aufnahmedatum, Kamera. Kostenlos im Browser oder als iPhone-App. Alles läuft auf Ihrem Gerät, das Original bleibt unverändert.",
        "crumb": "",
        "tool": None,
        "og": "home.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>Das Wichtigste</h2></div>
        <ul>
          <li><strong>Was:</strong> Standort (GPS), Aufnahmedatum und Kameradaten in Fotos anzeigen und entfernen.</li>
          <li><strong>Wo:</strong> im Browser-Tab oder auf dem iPhone. Nichts geht an einen Server.</li>
          <li><strong>Original:</strong> bleibt unverändert; das bereinigte Foto wird als neues Foto gespeichert.</li>
          <li><strong>Preis:</strong> Download kostenlos. Einzelne Fotos kostenlos, Stapelverarbeitung Premium.</li>
        </ul>
      </section>
      <section class="section">
        <div class="section-head"><h2>Werkzeuge</h2></div>
        <div class="tiles">
          <a class="tile" href="{L}remove-gps/"><h3>Standort entfernen</h3><p>GPS-Daten löschen, bevor Sie ein Foto teilen oder verkaufen.</p></a>
          <a class="tile" href="{L}remove-exif/"><h3>Metadaten entfernen</h3><p>Alle EXIF-Daten löschen und ein sauberes Foto speichern.</p></a>
          <a class="tile" href="{L}exif-viewer/"><h3>EXIF-Daten anzeigen</h3><p>Sehen, was in einem Foto gespeichert ist.</p></a>
          <a class="tile" href="{L}how-to/remove-location-from-photos-iphone/"><h3>Auf dem iPhone</h3><p>Standort aus Fotos der Mediathek entfernen.</p></a>
        </div>
      </section>
      <section class="section">
        <div class="section-head"><h2>Wann das sinnvoll ist</h2></div>
        <ul>
          <li>Bevor Sie Fotos auf Kleinanzeigen oder eBay hochladen – damit niemand Ihre Wohnadresse sieht.</li>
          <li>Vor dem Posten auf Instagram, in Foren oder im Blog.</li>
          <li>Bevor Sie Fotos per <a href="{L}learn/does-whatsapp-remove-exif/">WhatsApp als Dokument</a> verschicken.</li>
        </ul>
      </section>""",
        "faqs": [
            ("Was ist EXIF+?", "EXIF+ ist eine App für iPhone und iPad, mit der Sie EXIF-, IPTC- und Standortdaten (GPS) von Fotos anzeigen, bearbeiten und entfernen. Auf dieser Website gibt es außerdem kostenlose Werkzeuge, die nur im Browser laufen."),
            ("Werden meine Fotos hochgeladen?", "Nein. Die Browser-Werkzeuge verarbeiten das Foto nur in diesem Tab. Die App verarbeitet Fotos auf dem iPhone."),
            ("Wird das Originalfoto verändert?", "Nein. Bearbeitete oder bereinigte Fotos werden als neues Foto in der Mediathek gespeichert. Das Original bleibt, bis Sie es selbst löschen."),
            ("Ist EXIF+ kostenlos?", "Der Download ist kostenlos. Metadaten anzeigen sowie einzelne Fotos bearbeiten und bereinigen ist kostenlos. Mehrere Fotos auf einmal und automatisches Entfernen beim Teilen sind Premium."),
            ("Funktioniert das auch mit Videos?", "Nein. Video-Metadaten werden nicht unterstützt, nur Fotos."),
        ],
    },
    {
        "slug": "remove-gps",
        "title": "Standort aus Foto entfernen – GPS-Daten kostenlos löschen | EXIF+",
        "description": "Standort (GPS, Geotag) aus Fotos kostenlos im Browser entfernen. Kein Upload: Koordinaten löschen und ein sauberes Foto speichern. Auf dem iPhone mit EXIF+.",
        "h1": "Standort aus Foto entfernen (GPS-Daten löschen)",
        "lead": "Bevor Sie ein Foto teilen oder online verkaufen: prüfen, ob es Standortdaten enthält, und sie entfernen. Das Foto verlässt den Browser nicht.",
        "crumb": "Standort entfernen",
        "tool": ("gps", "Standort entfernen (im Browser)", "Prüfen Sie, ob das Foto GPS-Daten enthält, und speichern Sie eine Kopie ohne Standort."),
        "og": "remove-gps.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>Warum Fotos einen Standort enthalten</h2></div>
        <p>Ist in der iPhone-Kamera der Ortungsdienst aktiv, speichert jedes Foto Breiten- und Längengrad des Aufnahmeorts. Wer das Foto bekommt, kann so Ihre Wohnung oder Ihren Arbeitsplatz sehen.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>Vor dem Teilen prüfen</h2></div>
        <ul>
          <li>Fotos von zu Hause, Arbeit oder Schule: Standort vorher entfernen.</li>
          <li>Genauso bei Kleinanzeigen und Fotos an Fremde.</li>
          <li>Auch Datum und Kamera löschen: <a href="{L}remove-exif/">Metadaten entfernen</a>.</li>
          <li>Fotos aus der iPhone-Mediathek: <a href="{L}how-to/remove-location-from-photos-iphone/">Standort auf dem iPhone entfernen</a>.</li>
        </ul>
      </section>""",
        "faqs": [
            ("Wie entferne ich den Standort aus einem Foto?", "Legen Sie das Foto in das Werkzeug oben. Es zeigt, ob GPS-Daten vorhanden sind, und speichert eine Kopie ohne Standort. Auf dem iPhone geht das mit der App EXIF+."),
            ("Ist der Ort danach gar nicht mehr erkennbar?", "Die gespeicherten Koordinaten sind weg. Der Ort kann aber trotzdem am Bildinhalt erkennbar sein, etwa an Gebäuden oder Schildern."),
            ("Entfernen soziale Netzwerke den Standort automatisch?", "Das hängt vom Dienst ab. Sicher ist nur, den Standort vor dem Hochladen selbst zu entfernen."),
            ("Geht das auch mit HEIC-Fotos?", "Die meisten Browser können HEIC nicht lesen. HEIC-Fotos aus der iPhone-Mediathek bereinigen Sie mit der App EXIF+."),
        ],
    },
    {
        "slug": "remove-exif",
        "title": "Metadaten entfernen – EXIF aus Fotos kostenlos löschen | EXIF+",
        "description": "Foto-Metadaten (EXIF) kostenlos im Browser entfernen: Aufnahmedatum, Kamera und Standort löschen, ohne Upload. Mit der iPhone-App auch viele Fotos auf einmal.",
        "h1": "Metadaten aus Fotos entfernen (EXIF löschen, ohne Upload)",
        "lead": "EXIF-Metadaten eines Fotos direkt im Browser anzeigen und entfernen. Das Foto wird nicht an einen Server geschickt.",
        "crumb": "Metadaten entfernen",
        "tool": ("remove", "Metadaten entfernen (im Browser)", "Foto auswählen, enthaltene Metadaten ansehen und eine bereinigte Kopie speichern."),
        "og": "remove-exif.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>Was sind EXIF-Daten?</h2></div>
        <p>EXIF-Daten speichert jede Kamera und jedes Smartphone automatisch im Foto: Gerät, Aufnahmedatum und -zeit, Belichtung und oft den Standort (GPS). Wer die Datei erhält, kann sie auslesen.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>So geht’s</h2></div>
        <ol>
          <li>Foto in das Werkzeug oben ziehen oder anklicken.</li>
          <li>Angezeigte Metadaten prüfen.</li>
          <li>Bereinigtes Foto herunterladen.</li>
        </ol>
        <p>Nur den Standort löschen: <a href="{L}remove-gps/">Standort entfernen</a>. Erst einmal nur ansehen: <a href="{L}exif-viewer/">EXIF-Daten anzeigen</a>.</p>
      </section>""",
        "faqs": [
            ("Wird mein Foto beim Entfernen hochgeladen?", "Nein. Das Foto wird nur in diesem Tab verarbeitet und nicht an einen Server gesendet."),
            ("Verliert das Foto an Qualität?", "Die Metadaten selbst beeinflussen das Bild nicht. Beim erneuten Speichern wird das Foto aber neu kodiert und kann sich minimal ändern. Bewahren Sie das Original auf."),
            ("Was wird beim Entfernen der EXIF-Daten gelöscht?", "Gerät, Objektiv, Aufnahmedatum, Standort (GPS) und weitere Aufnahmedaten im Foto."),
            ("Kann ich viele Fotos auf einmal bereinigen?", "Im Browser geht es Foto für Foto. Mit EXIF+ Premium auf dem iPhone bereinigen Sie mehrere Fotos auf einmal."),
        ],
    },
    {
        "slug": "exif-viewer",
        "title": "EXIF-Daten anzeigen – Foto-Metadaten online auslesen | EXIF+",
        "description": "EXIF-Daten kostenlos anzeigen: Aufnahmedatum, Kamera, Objektiv, ISO und Standort (GPS) eines Fotos auslesen. Kein Upload. Auf dem iPhone mit EXIF+.",
        "h1": "EXIF-Daten anzeigen (Foto-Metadaten auslesen)",
        "lead": "Sehen Sie, was in einem Foto steckt: Aufnahmedatum, Kamera und Objektiv, Belichtung und Standort (GPS). Kostenlos, das Foto wird nicht hochgeladen.",
        "crumb": "EXIF anzeigen",
        "tool": ("view", "EXIF-Viewer (im Browser)", "Foto auswählen und lesbare EXIF-, IPTC- und GPS-Felder anzeigen."),
        "og": "exif-viewer.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>Was Sie sehen</h2></div>
        <p>Aufnahmedatum und -zeit, Kamera- oder Handymodell, Objektiv, ISO, Blende, Belichtungszeit, Software, Copyright und – falls gespeichert – den Standort als Breiten- und Längengrad.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>Und danach?</h2></div>
        <p>Steht ein Standort drin, den Sie nicht teilen wollen: <a href="{L}remove-gps/">Standort entfernen</a>. Alles löschen: <a href="{L}remove-exif/">Metadaten entfernen</a>. Fotos aus der iPhone-Mediathek sehen und bearbeiten Sie direkt in der App EXIF+.</p>
      </section>""",
        "faqs": [
            ("Wie kann ich EXIF-Daten eines Fotos sehen?", "Wählen Sie auf dieser Seite ein JPEG-, PNG- oder WebP-Foto aus, die Felder werden angezeigt. Für Fotos aus der iPhone-Mediathek und HEIC nutzen Sie die App EXIF+."),
            ("Warum wird kein Standort angezeigt?", "Der Ortungsdienst war bei der Aufnahme aus, die Daten wurden schon entfernt oder eine andere App hat das Foto ohne GPS gespeichert."),
            ("Ist das Auslesen sicher?", "Die Datei wird nur im Browser gelesen und angezeigt, nicht hochgeladen."),
            ("Kann ich die Daten hier bearbeiten?", "Im Browser nicht. Bearbeiten können Sie in der iPhone-App EXIF+, löschen mit dem Werkzeug „Metadaten entfernen“."),
        ],
    },
    {
        "slug": "how-to/remove-location-from-photos-iphone",
        "title": "iPhone: Standort aus Fotos entfernen – so geht’s | EXIF+",
        "description": "Standort aus iPhone-Fotos entfernen: beim Teilen über „Optionen“ ausschalten oder mit EXIF+ eine Kopie ohne GPS speichern. Original bleibt, mehrere Fotos per Stapel.",
        "h1": "Standort aus iPhone-Fotos entfernen",
        "lead": "Auf dem iPhone gibt es zwei Wege: den Standort nur beim Teilen weglassen (iOS-Bordmittel) oder mit EXIF+ eine Kopie ohne Standort speichern.",
        "crumb": "iPhone: Standort entfernen",
        "tool": None,
        "og": "on-iphone.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>Weg 1: Beim Teilen ausschalten (iOS)</h2></div>
        <ol>
          <li>In der Fotos-App das Foto wählen und auf Teilen tippen.</li>
          <li>Oben auf „Optionen“ tippen.</li>
          <li>„Ort“ ausschalten, „Fertig“ tippen und teilen.</li>
        </ol>
        <p>Das gilt nur für dieses eine Teilen; in der Mediathek behält das Foto seinen Standort. Je nach App und Versandweg fehlt die Option.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>Weg 2: Kopie ohne Standort mit EXIF+</h2></div>
        <ol>
          <li>EXIF+ aus dem App Store laden und Zugriff auf Fotos erlauben.</li>
          <li>Foto öffnen und den Bereich Standort / GPS prüfen.</li>
          <li>Standort löschen oder alle Metadaten entfernen und speichern.</li>
          <li>Das neue Foto teilen. Das Original bleibt unverändert.</li>
        </ol>
        <p>Für eine einzelne Datei am Computer: <a href="{L}remove-gps/">Standort im Browser entfernen</a>.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>Künftig keinen Standort speichern</h2></div>
        <p>Einstellungen → Datenschutz &amp; Sicherheit → Ortungsdienste → Kamera → „Nie“. Neue Fotos bekommen dann keinen Standort; bereits aufgenommene Fotos behalten ihn.</p>
      </section>""",
        "faqs": [
            ("Entfernt „Optionen → Ort“ den Standort auch im Original?", "Nein. Der Standort fehlt nur in der geteilten Kopie; das Foto in der Mediathek behält ihn."),
            ("Ist Standort entfernen dasselbe wie alle Metadaten entfernen?", "Nein. In EXIF+ können Sie nur den Standort löschen oder alles inklusive Kamera und Datum."),
            ("Kann ich viele Fotos auf einmal bearbeiten?", "Ja, mit der Mehrfachauswahl in EXIF+ Premium."),
            ("Funktioniert das mit HEIC?", "Ja, in der iPhone-App direkt aus der Mediathek."),
        ],
    },
    {
        "slug": "learn/does-whatsapp-remove-exif",
        "title": "Entfernt WhatsApp Metadaten und Standort aus Fotos? | EXIF+",
        "description": "WhatsApp komprimiert normale Fotos, dabei gehen EXIF und Standort meist verloren. Als Dokument gesendet bleibt das Original samt Metadaten. So senden Sie sicher.",
        "h1": "Entfernt WhatsApp Metadaten aus Fotos?",
        "lead": "Kurz: Normal gesendete Fotos werden komprimiert und kommen meist ohne EXIF und Standort an. Als Dokument gesendet bleibt das Originalfoto erhalten – mit allen Metadaten.",
        "crumb": "WhatsApp und Metadaten",
        "tool": None,
        "og": "home.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>Welcher Versandweg die Metadaten behält</h2></div>
        <ul>
          <li><strong>Normal aus Galerie oder Kamera (auch HD):</strong> neu kodiert, EXIF und GPS meist entfernt.</li>
          <li><strong>Als Dokument:</strong> Originaldatei, EXIF und GPS bleiben meist erhalten.</li>
          <li><strong>Ihre eigene Kopie und Backups:</strong> das Original auf Ihrem Handy hat weiterhin alle Metadaten.</li>
        </ul>
        <p>„Als Dokument senden“ ist ein beliebter Trick gegen Komprimierung – und genau dabei geht der Standort mit. Das Entfernen bei normalen Fotos ist eine Nebenwirkung der Komprimierung, keine Datenschutzfunktion.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>Sicher senden</h2></div>
        <p>Erst bereinigen, dann senden: <a href="{L}remove-gps/">Standort im Browser entfernen</a> oder auf dem iPhone <a href="{L}how-to/remove-location-from-photos-iphone/">Standort aus iPhone-Fotos entfernen</a>. EXIF+ speichert eine neue Kopie, das Original bleibt.</p>
      </section>""",
        "faqs": [
            ("Entfernt WhatsApp EXIF-Daten aus Fotos?", "Bei normal gesendeten Fotos meist ja, weil WhatsApp sie komprimiert. Als Dokument gesendete Fotos behalten ihre EXIF-Daten."),
            ("Entfernt WhatsApp den Standort aus Fotos?", "Bei normalem Versand meist ja, als Dokument meist nicht. Wenn Sie unsicher sind, entfernen Sie den Standort vorher selbst."),
            ("Behält WhatsApp in HD-Qualität die Metadaten?", "HD-Fotos werden ebenfalls neu kodiert, die Metadaten gehen meist verloren. Nur der Dokument-Versand liefert das unveränderte Original."),
            ("Kann jemand meinen Standort aus einem WhatsApp-Foto auslesen?", "Aus einem normal gesendeten Foto meist nicht. Aus einem als Dokument gesendeten Foto ja, wenn bei der Aufnahme ein Standort gespeichert wurde."),
        ],
    },
]

# ======================================================================== es
LOCALES["es"] = {
    "store": "es",
    "lang_name": "Español",
    "ui": {
        "appstore_aria": "Descargar en el App Store",
        "appstore_small": "Descárgalo en el",
        "nav_aria": "Menú",
        "nav": [("remove-gps/", "Quitar ubicación"), ("remove-exif/", "Eliminar metadatos"), ("exif-viewer/", "Ver EXIF")],
        "nav_app": "App",
        "footer_aria": "Pie de página",
        "home": "Inicio",
        "privacy": "Privacidad",
        "tagline": "Ver, editar y eliminar metadatos de fotos en iPhone.",
        "crumb_aria": "Ruta",
        "faq": "Preguntas frecuentes",
        "drop_strong": "Arrastra una foto aquí",
        "drop_span": "o haz clic para elegirla (JPEG / PNG / WebP)",
        "download": "Descargar foto limpia",
        "local_note": "La foto se procesa solo en esta pestaña y no se envía a ningún servidor.",
        "cta_h": "Más fácil con la app para iPhone",
        "cta_p": "EXIF+ es una app para iPhone que muestra, edita y elimina los datos EXIF, IPTC y de ubicación (GPS) de tus fotos. Todo se hace en el dispositivo. La foto limpia se guarda como una foto nueva, así que el original no cambia. La descarga es gratis; editar y limpiar fotos de una en una es gratis y el procesamiento por lotes es Premium.",
        "related": "Más información",
    },
    "llms": [
        ("", "Inicio: quitar ubicación y metadatos de fotos"),
        ("remove-gps/", "Quitar ubicación de una foto (en el navegador)"),
        ("remove-exif/", "Eliminar metadatos / EXIF (en el navegador)"),
        ("exif-viewer/", "Ver datos EXIF (en el navegador)"),
        ("how-to/remove-location-from-photos-iphone/", "Quitar la ubicación de fotos en iPhone"),
        ("learn/does-whatsapp-remove-exif/", "¿WhatsApp elimina los metadatos?"),
    ],
}
LOCALES["es"]["pages"] = [
    {
        "slug": "",
        "title": "Quitar ubicación y metadatos de fotos – gratis, sin subirlas | EXIF+",
        "description": "Revisa y elimina gratis la ubicación (GPS) y los metadatos EXIF de tus fotos. La foto no sale del navegador. Con la app EXIF+ para iPhone, también muchas fotos a la vez.",
        "h1": "Quitar la ubicación y los metadatos de tus fotos (gratis, sin subirlas)",
        "lead": "EXIF+ muestra y elimina los datos ocultos de una foto: ubicación (GPS), fecha y cámara. Gratis en el navegador o como app para iPhone. Todo se procesa en tu dispositivo y el original no cambia.",
        "crumb": "",
        "tool": None,
        "og": "home.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>Lo esencial</h2></div>
        <ul>
          <li><strong>Qué hace:</strong> muestra y elimina la ubicación (GPS), la fecha y los datos de la cámara de una foto.</li>
          <li><strong>Dónde:</strong> en la pestaña del navegador o en el iPhone. Nada se envía a un servidor.</li>
          <li><strong>Original:</strong> no cambia; la foto limpia se guarda como una foto nueva.</li>
          <li><strong>Precio:</strong> descarga gratis. Fotos de una en una gratis, por lotes con Premium.</li>
        </ul>
      </section>
      <section class="section">
        <div class="section-head"><h2>Herramientas</h2></div>
        <div class="tiles">
          <a class="tile" href="{L}remove-gps/"><h3>Quitar ubicación</h3><p>Borra el GPS antes de compartir o vender una foto.</p></a>
          <a class="tile" href="{L}remove-exif/"><h3>Eliminar metadatos</h3><p>Borra todos los datos EXIF y guarda una foto limpia.</p></a>
          <a class="tile" href="{L}exif-viewer/"><h3>Ver datos EXIF</h3><p>Mira qué información guarda una foto.</p></a>
          <a class="tile" href="{L}how-to/remove-location-from-photos-iphone/"><h3>En iPhone</h3><p>Quitar la ubicación de las fotos de tu fototeca.</p></a>
        </div>
      </section>
      <section class="section">
        <div class="section-head"><h2>Cuándo te sirve</h2></div>
        <ul>
          <li>Antes de subir fotos a Wallapop, Mercado Libre o Vinted, para no mostrar dónde vives.</li>
          <li>Antes de publicar en Instagram, en foros o en un blog.</li>
          <li>Antes de enviar fotos por <a href="{L}learn/does-whatsapp-remove-exif/">WhatsApp como documento</a>.</li>
        </ul>
      </section>""",
        "faqs": [
            ("¿Qué es EXIF+?", "EXIF+ es una app para iPhone y iPad que muestra, edita y elimina los datos EXIF, IPTC y de ubicación (GPS) de las fotos. En esta web también hay herramientas gratis que funcionan solo en el navegador."),
            ("¿Se suben mis fotos a algún servidor?", "No. Las herramientas del navegador procesan la foto solo en esta pestaña. La app procesa las fotos en el iPhone."),
            ("¿Se modifica la foto original?", "No. Las fotos editadas o limpias se guardan como fotos nuevas en la fototeca. El original sigue ahí hasta que lo borres tú."),
            ("¿Es gratis?", "La descarga es gratis. Ver metadatos y editar o limpiar fotos de una en una es gratis. Procesar varias fotos a la vez y quitar metadatos al compartir es Premium."),
            ("¿Funciona con vídeos?", "No. Los metadatos de vídeo no son compatibles; solo fotos."),
        ],
    },
    {
        "slug": "remove-gps",
        "title": "Quitar ubicación de una foto – borrar GPS gratis | EXIF+",
        "description": "Quita la ubicación (GPS, geoetiqueta) de tus fotos gratis en el navegador. Sin subirlas: borra las coordenadas y guarda una foto limpia. En iPhone, con EXIF+.",
        "h1": "Quitar la ubicación de una foto (borrar el GPS)",
        "lead": "Antes de compartir o vender en línea una foto, comprueba si guarda la ubicación y quítala. La foto no sale de tu navegador.",
        "crumb": "Quitar ubicación",
        "tool": ("gps", "Quitar ubicación (en el navegador)", "Comprueba si la foto tiene datos GPS y guarda una copia sin ubicación."),
        "og": "remove-gps.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>Por qué una foto guarda la ubicación</h2></div>
        <p>Si la cámara del iPhone tiene activada la localización, cada foto guarda la latitud y longitud del lugar donde se tomó. Quien recibe el archivo puede ver dónde vives o trabajas.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>Antes de compartir</h2></div>
        <ul>
          <li>Fotos tomadas en casa, en el trabajo o en la escuela: quita antes la ubicación.</li>
          <li>Lo mismo con fotos para vender en línea o para desconocidos.</li>
          <li>Para borrar también la fecha y la cámara: <a href="{L}remove-exif/">eliminar metadatos</a>.</li>
          <li>Fotos de la fototeca del iPhone: <a href="{L}how-to/remove-location-from-photos-iphone/">quitar la ubicación en iPhone</a>.</li>
        </ul>
      </section>""",
        "faqs": [
            ("¿Cómo quito la ubicación de una foto?", "Pon la foto en la herramienta de arriba. Verás si tiene datos GPS y podrás guardar una copia sin ubicación. En iPhone se hace con la app EXIF+."),
            ("¿Ya no se podrá saber dónde se tomó?", "Las coordenadas guardadas desaparecen. Aun así, el lugar puede reconocerse por lo que se ve en la imagen, como edificios o carteles."),
            ("¿Las redes sociales quitan la ubicación automáticamente?", "Depende del servicio. Lo seguro es quitarla tú antes de publicar."),
            ("¿Funciona con fotos HEIC?", "La mayoría de los navegadores no leen HEIC. Las fotos HEIC de la fototeca del iPhone se limpian con la app EXIF+."),
        ],
    },
    {
        "slug": "remove-exif",
        "title": "Eliminar metadatos de una foto – borrar EXIF gratis | EXIF+",
        "description": "Elimina gratis los metadatos (EXIF) de tus fotos en el navegador: fecha, cámara y ubicación, sin subir nada. Con la app para iPhone, también muchas fotos a la vez.",
        "h1": "Eliminar los metadatos de una foto (borrar EXIF sin subirla)",
        "lead": "Mira y elimina los metadatos EXIF de una foto directamente en el navegador. La foto no se envía a ningún servidor.",
        "crumb": "Eliminar metadatos",
        "tool": ("remove", "Eliminar metadatos (en el navegador)", "Elige una foto, revisa sus metadatos y guarda una copia limpia."),
        "og": "remove-exif.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>¿Qué son los datos EXIF?</h2></div>
        <p>Los datos EXIF son la información que la cámara o el móvil guarda automáticamente en cada foto: modelo del dispositivo, fecha y hora, ajustes de exposición y a menudo la ubicación (GPS). Cualquiera que reciba el archivo puede leerlos.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>Cómo hacerlo</h2></div>
        <ol>
          <li>Arrastra la foto a la herramienta de arriba o haz clic para elegirla.</li>
          <li>Revisa los metadatos que aparecen.</li>
          <li>Descarga la foto limpia.</li>
        </ol>
        <p>Si solo quieres borrar la ubicación: <a href="{L}remove-gps/">quitar ubicación</a>. Si solo quieres mirar: <a href="{L}exif-viewer/">ver datos EXIF</a>.</p>
      </section>""",
        "faqs": [
            ("¿Se sube mi foto al eliminar los metadatos?", "No. La foto se procesa solo en esta pestaña y no se envía a ningún servidor."),
            ("¿Pierde calidad la foto?", "Los metadatos no afectan a la imagen, pero al guardarla de nuevo se vuelve a codificar y puede cambiar un poco. Conserva el original."),
            ("¿Qué se borra al eliminar los datos EXIF?", "El modelo de cámara, el objetivo, la fecha de captura, la ubicación (GPS) y otros datos de la toma."),
            ("¿Puedo limpiar muchas fotos a la vez?", "En el navegador, de una en una. Con EXIF+ Premium en el iPhone puedes limpiar varias fotos a la vez."),
        ],
    },
    {
        "slug": "exif-viewer",
        "title": "Ver datos EXIF de una foto – visor de metadatos gratis | EXIF+",
        "description": "Visor EXIF gratis: mira la fecha, la cámara, el objetivo, el ISO y la ubicación (GPS) de una foto. Sin subirla. En iPhone, con EXIF+.",
        "h1": "Ver los datos EXIF de una foto",
        "lead": "Descubre qué guarda una foto: fecha, cámara y objetivo, exposición y ubicación (GPS). Gratis y sin subir la foto.",
        "crumb": "Ver EXIF",
        "tool": ("view", "Visor EXIF (en el navegador)", "Elige una foto para ver sus campos EXIF, IPTC y GPS."),
        "og": "exif-viewer.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>Qué puedes ver</h2></div>
        <p>Fecha y hora, modelo de cámara o móvil, objetivo, ISO, apertura, velocidad de obturación, software, copyright y, si existe, la ubicación en latitud y longitud.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>Y después</h2></div>
        <p>Si aparece una ubicación que no quieres compartir: <a href="{L}remove-gps/">quitar ubicación</a>. Para borrarlo todo: <a href="{L}remove-exif/">eliminar metadatos</a>. Las fotos de la fototeca del iPhone se ven y editan directamente en la app EXIF+.</p>
      </section>""",
        "faqs": [
            ("¿Cómo veo los datos EXIF de una foto?", "Elige en esta página una foto JPEG, PNG o WebP y verás sus campos. Para fotos de la fototeca del iPhone y HEIC, usa la app EXIF+."),
            ("¿Por qué no aparece la ubicación?", "La localización estaba desactivada al tomarla, ya se borró o la guardó otra app sin GPS."),
            ("¿Es seguro ver los EXIF aquí?", "El archivo se lee solo en tu navegador para mostrarlo; no se sube."),
            ("¿Puedo editar los datos aquí?", "En el navegador no. Puedes editarlos en la app EXIF+ para iPhone o borrarlos con «Eliminar metadatos»."),
        ],
    },
    {
        "slug": "how-to/remove-location-from-photos-iphone",
        "title": "Cómo quitar la ubicación de una foto en iPhone | EXIF+",
        "description": "Quita la ubicación de tus fotos en iPhone: desactívala al compartir en «Opciones» o guarda con EXIF+ una copia sin GPS. El original no cambia; varias fotos por lotes.",
        "h1": "Cómo quitar la ubicación de una foto en iPhone",
        "lead": "En iPhone hay dos formas: quitar la ubicación solo al compartir (función de iOS) o guardar con EXIF+ una copia de la foto sin ubicación.",
        "crumb": "Quitar ubicación en iPhone",
        "tool": None,
        "og": "on-iphone.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>Forma 1: al compartir (iOS)</h2></div>
        <ol>
          <li>En la app Fotos, elige la foto y toca Compartir.</li>
          <li>Toca «Opciones» arriba.</li>
          <li>Desactiva «Ubicación», toca OK y comparte.</li>
        </ol>
        <p>Solo vale para ese envío; la foto de tu fototeca conserva la ubicación. Según la app o la forma de envío, la opción puede no aparecer.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>Forma 2: copia sin ubicación con EXIF+</h2></div>
        <ol>
          <li>Instala EXIF+ desde el App Store y permite el acceso a Fotos.</li>
          <li>Abre la foto y revisa la sección Ubicación / GPS.</li>
          <li>Borra la ubicación o elimina todos los metadatos y guarda.</li>
          <li>Comparte la foto nueva. El original no cambia.</li>
        </ol>
        <p>Para un solo archivo en el ordenador: <a href="{L}remove-gps/">quitar la ubicación en el navegador</a>.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>Que las próximas fotos no guarden la ubicación</h2></div>
        <p>Ajustes → Privacidad y seguridad → Localización → Cámara → «Nunca». Las fotos nuevas no tendrán ubicación; las que ya tomaste la conservan.</p>
      </section>""",
        "faqs": [
            ("¿«Opciones → Ubicación» la borra también del original?", "No. Solo se quita de la copia que compartes; la foto de la fototeca la conserva."),
            ("¿Quitar la ubicación es lo mismo que eliminar todos los metadatos?", "No. En EXIF+ puedes borrar solo la ubicación o todo, incluidas la cámara y la fecha."),
            ("¿Puedo hacerlo con muchas fotos a la vez?", "Sí, con la selección múltiple de EXIF+ Premium."),
            ("¿Funciona con fotos HEIC?", "Sí, en la app para iPhone directamente desde la fototeca."),
        ],
    },
    {
        "slug": "learn/does-whatsapp-remove-exif",
        "title": "¿WhatsApp elimina los metadatos y la ubicación de las fotos? | EXIF+",
        "description": "WhatsApp comprime las fotos normales y suele borrar el EXIF y la ubicación. Enviadas como documento conservan el original con sus metadatos. Cómo enviarlas seguro.",
        "h1": "¿WhatsApp elimina los metadatos de las fotos?",
        "lead": "Respuesta corta: las fotos enviadas de forma normal se comprimen y suelen llegar sin EXIF ni ubicación. Enviadas como documento llegan como el archivo original, con todos sus metadatos.",
        "crumb": "WhatsApp y metadatos",
        "tool": None,
        "og": "home.png",
        "main": """      <section class="section">
        <div class="section-head"><h2>Qué forma de envío conserva los metadatos</h2></div>
        <ul>
          <li><strong>Normal desde la galería o la cámara (también HD):</strong> se vuelve a codificar; el EXIF y el GPS suelen desaparecer.</li>
          <li><strong>Como documento:</strong> archivo original; el EXIF y el GPS suelen conservarse.</li>
          <li><strong>Tu copia y las copias de seguridad:</strong> el original en tu móvil sigue con todos sus metadatos.</li>
        </ul>
        <p>«Enviar como documento» es un truco habitual para evitar la compresión, y es justo la forma en que se filtra la ubicación. Que WhatsApp borre los datos en envíos normales es un efecto de la compresión, no una función de privacidad.</p>
      </section>
      <section class="section">
        <div class="section-head"><h2>Cómo enviar seguro</h2></div>
        <p>Primero limpia, luego envía: <a href="{L}remove-gps/">quita la ubicación en el navegador</a> o, en iPhone, sigue <a href="{L}how-to/remove-location-from-photos-iphone/">cómo quitar la ubicación en iPhone</a>. EXIF+ guarda una copia nueva y el original no cambia.</p>
      </section>""",
        "faqs": [
            ("¿WhatsApp elimina los datos EXIF de las fotos?", "En los envíos normales, normalmente sí, porque WhatsApp las comprime. Las fotos enviadas como documento conservan su EXIF."),
            ("¿WhatsApp quita la ubicación de las fotos?", "En envíos normales suele quitarla; como documento, no. Si no estás seguro, quítala tú antes de enviar."),
            ("¿La calidad HD de WhatsApp conserva los metadatos?", "Las fotos HD también se vuelven a codificar, así que los metadatos suelen perderse. Solo el envío como documento entrega el original intacto."),
            ("¿Alguien puede saber mi ubicación por una foto de WhatsApp?", "Por una foto enviada de forma normal, normalmente no. Por una enviada como documento, sí, si se guardó la ubicación al tomarla."),
        ],
    },
]


# ---------------------------------------------------------------- helpers used by _build


def llms_section(base: str) -> str:
    """Markdown block for llms.txt listing the localized pages."""
    out = []
    for lang, loc in LOCALES.items():
        out.append(f"## {loc['lang_name']} ({lang})")
        for path, label in loc["llms"]:
            out.append(f"- [{label}]({base}/{lang}/{path})")
        out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------- builder


def register_i18n(ctx: dict) -> None:
    page_shell = ctx["page_shell"]
    register = ctx["register"]
    esc = ctx["esc"]
    BASE = ctx["BASE"]
    NAME = ctx["NAME"]
    PRIVACY = ctx["PRIVACY"]

    for lang, loc in LOCALES.items():
        ui = loc["ui"]
        app_url = ctx["APP"].replace("/us/", f"/{loc['store']}/")

        def appstore_btn(ui=ui, app_url=app_url) -> str:
            return (
                f'<a class="appstore" href="{app_url}" target="_blank" rel="noopener noreferrer" '
                f'aria-label="{esc(ui["appstore_aria"])}">{ctx["APPSTORE_SVG"]}'
                f'<span class="appstore__text"><span class="appstore__small">{esc(ui["appstore_small"])}</span>'
                '<span class="appstore__big">App Store</span></span></a>'
            )

        def nav(prefix: str, lang=lang, ui=ui, app_url=app_url) -> str:
            links = "".join(f'<a href="{prefix}{lang}/{href}">{esc(label)}</a>' for href, label in ui["nav"])
            return (
                f'<nav class="nav-links" aria-label="{esc(ui["nav_aria"])}">{links}'
                f'<a href="{app_url}" rel="noopener noreferrer">{esc(ui["nav_app"])}</a>'
                f'<a href="{prefix}" hreflang="en">English</a>'
                "</nav>"
            )

        def footer(prefix: str, lang=lang, ui=ui) -> str:
            links = "".join(f'<a href="{prefix}{lang}/{href}">{esc(label)}</a>' for href, label in ui["nav"])
            return (
                f'<footer class="site-footer"><nav aria-label="{esc(ui["footer_aria"])}">'
                f'<a href="{prefix}{lang}/">{esc(ui["home"])}</a>{links}'
                f'<a href="{prefix}" hreflang="en">English</a>'
                f'<a href="{PRIVACY}" rel="noopener noreferrer">{esc(ui["privacy"])}</a>'
                f"</nav><p>© {NAME} — {esc(ui['tagline'])}</p></footer>"
            )

        def tool_panel(mode: str, title: str, blurb: str, ui=ui) -> str:
            download = ""
            if mode in ("remove", "gps"):
                download = f'<button type="button" class="btn btn-primary tool-download" hidden>{esc(ui["download"])}</button>'
            return f"""      <section class="tool-panel" data-exif-tool data-mode="{mode}" aria-label="{esc(title)}">
        <h2 style="margin:0 0 6px;font-family:var(--display);font-size:1.35rem;">{esc(title)}</h2>
        <p class="lead-sm">{esc(blurb)} {esc(ui["local_note"])}</p>
        <div class="dropzone" role="button" tabindex="0">
          <strong>{esc(ui["drop_strong"])}</strong>
          <span>{esc(ui["drop_span"])}</span>
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
      </section>
"""

        for pg in loc["pages"]:
            rel = f"{lang}/{pg['slug']}".rstrip("/")
            prefix = "../" * len(rel.split("/"))
            lang_root = prefix + f"{lang}/"
            faqs = pg["faqs"]
            crumb = pg["crumb"]

            crumb_html = (
                f'<nav class="breadcrumbs" aria-label="{esc(ui["crumb_aria"])}">'
                f'<a href="{lang_root}">{esc(ui["home"])}</a>'
                + (
                    f'<span class="crumb-sep" aria-hidden="true">›</span><span aria-current="page">{esc(crumb)}</span>'
                    if crumb
                    else ""
                )
                + "</nav>"
            )
            tool_html = tool_panel(*pg["tool"]) if pg["tool"] else ""
            main_inner = tool_html + pg["main"].replace("{L}", lang_root)
            faq_items = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faqs)
            body = f"""    {crumb_html}
    <main>
      <section class="hero">
        <h1>{esc(pg["h1"])}</h1>
        <p class="lead">{esc(pg["lead"])}</p>
        <div class="actions">{appstore_btn()}</div>
      </section>
{main_inner}
      <section class="section faq"><div class="section-head"><h2>{esc(ui["faq"])}</h2></div>{faq_items}</section>
      <section class="section cta-band">
        <div class="section-head"><h2>{esc(ui["cta_h"])}</h2></div>
        <p class="lead-sm">{esc(ui["cta_p"])}</p>
        <div class="actions">{appstore_btn()}</div>
      </section>
    </main>"""

            url = f"{BASE}/{rel}/"
            crumb_items = [(ui["home"], f"{BASE}/{lang}/")] + ([(crumb, url)] if crumb else [])
            faq_schema = ctx["faq_ld"](faqs) | {"inLanguage": lang}
            schemas = [ctx["org_ld"](), ctx["breadcrumb_ld"](crumb_items), faq_schema]
            if pg["slug"] == "":
                schemas.append(ctx["software_ld"]() | {"inLanguage": lang, "url": app_url, "downloadUrl": app_url})
            elif pg["tool"]:
                schemas.append(ctx["webapp_ld"](pg["tool"][1], pg["description"], url) | {"inLanguage": lang})

            html = page_shell(
                rel=rel,
                title=pg["title"],
                description=pg["description"],
                canonical_path=f"{rel}/",
                body=body,
                schemas=schemas,
                nav_current=None,
                og_image=pg["og"],
                include_tool=bool(pg["tool"]),
                lang=lang,
            )
            # swap English chrome (nav/footer/brand) for the localized one
            html = re.sub(r'<nav class="nav-links".*?</nav>', lambda m: nav(prefix), html, count=1, flags=re.S)
            html = re.sub(r'<footer class="site-footer">.*?</footer>', lambda m: footer(prefix), html, count=1, flags=re.S)
            html = html.replace(f'<a class="brand" href="{prefix}">', f'<a class="brand" href="{lang_root}">')
            register({"rel": rel, "html": html, "title": pg["h1"], "priority": True})
