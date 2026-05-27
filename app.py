import streamlit as st

# ── 페이지 설정 ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="허수영 · Portfolio",
    page_icon="◻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════════════════════
#  고정 팔레트 상수
# ══════════════════════════════════════════════════════════════════════════════
PUNCH_RED    = "#e63946"
HONEYDEW     = "#f1faee"
FROSTED_BLUE = "#a8dadc"
CERULEAN     = "#457b9d"
OXFORD_NAVY  = "#1d3557"

# ══════════════════════════════════════════════════════════════════════════════
#  다크 모드 세션 초기화 (기본값: False → 라이트)
# ══════════════════════════════════════════════════════════════════════════════
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False

IS_DARK: bool = st.session_state["dark_mode"]

# ══════════════════════════════════════════════════════════════════════════════
#  테마 딕셔너리  (라이트 / 다크)
# ══════════════════════════════════════════════════════════════════════════════
if IS_DARK:
    T = dict(
        # 배경 · 표면
        bg          = "#0d1b2a",          # 깊은 다크 네이비
        surface     = "#152238",          # 카드/섹션 표면
        # 텍스트: 다크 → 밝게
        text        = HONEYDEW,
        text_sub    = FROSTED_BLUE,
        text_muted  = f"{FROSTED_BLUE}cc",
        # UI 구조색
        border      = CERULEAN,
        divider     = f"{CERULEAN}44",
        nav_clr     = FROSTED_BLUE,
        label_clr   = FROSTED_BLUE,
        # 히어로
        hero_bg     = f"-45deg,#0d1b2a,{OXFORD_NAVY},{OXFORD_NAVY}cc,#0d1b2a,{OXFORD_NAVY}",
        name_grad   = f"{HONEYDEW},{FROSTED_BLUE},{CERULEAN},{FROSTED_BLUE},{HONEYDEW}",
        hero_label  = FROSTED_BLUE,
        hero_sub_p  = HONEYDEW,
        hero_sub_s  = FROSTED_BLUE,
        glow_a      = f"{FROSTED_BLUE}2e",
        glow_b      = f"{PUNCH_RED}1e",
        # About
        about_strong= HONEYDEW,
        about_body  = FROSTED_BLUE,
        info_lbl    = CERULEAN,
        info_val    = HONEYDEW,
        info_bdr    = f"{CERULEAN}30",
        # 타임라인
        tl_year     = CERULEAN,
        tl_title    = HONEYDEW,
        tl_detail   = FROSTED_BLUE,
        tl_bdr      = f"{CERULEAN}30",
        # 연락처
        ct_lbl      = CERULEAN,
        ct_val      = HONEYDEW,
        ct_bdr      = f"{CERULEAN}30",
        ct_link_hov = PUNCH_RED,
        # 기술 태그 (모두 Punch Red)
        tag_bg      = PUNCH_RED,
        tag_text    = HONEYDEW,
        sk_cat      = FROSTED_BLUE,
        # 버튼
        btn_bg      = PUNCH_RED,
        btn_text    = HONEYDEW,
        btn_hov_bg  = "#c1121f",
        # 입력 폼
        input_bdr   = CERULEAN,
        input_text  = HONEYDEW,
        input_ph    = f"{CERULEAN}88",
        ta_bg       = "#152238",
        # 푸터
        footer_txt  = FROSTED_BLUE,
        footer_bdr  = f"{CERULEAN}44",
        # 토글
        tog_lbl     = "☀️ 라이트 모드",
    )
else:
    T = dict(
        # 배경 · 표면
        bg          = HONEYDEW,
        surface     = HONEYDEW,
        # 텍스트: 라이트 → 어둡게
        text        = OXFORD_NAVY,
        text_sub    = CERULEAN,
        text_muted  = f"{CERULEAN}cc",
        # UI 구조색
        border      = CERULEAN,
        divider     = f"{CERULEAN}55",
        nav_clr     = CERULEAN,
        label_clr   = CERULEAN,
        # 히어로
        hero_bg     = f"-45deg,{HONEYDEW},{FROSTED_BLUE}55,{HONEYDEW},{CERULEAN}22,{HONEYDEW}",
        name_grad   = f"{OXFORD_NAVY},{CERULEAN},{FROSTED_BLUE},{CERULEAN},{OXFORD_NAVY}",
        hero_label  = CERULEAN,
        hero_sub_p  = OXFORD_NAVY,
        hero_sub_s  = CERULEAN,
        glow_a      = f"{FROSTED_BLUE}44",
        glow_b      = f"{PUNCH_RED}22",
        # About
        about_strong= OXFORD_NAVY,
        about_body  = CERULEAN,
        info_lbl    = CERULEAN,
        info_val    = OXFORD_NAVY,
        info_bdr    = f"{CERULEAN}33",
        # 타임라인
        tl_year     = CERULEAN,
        tl_title    = OXFORD_NAVY,
        tl_detail   = CERULEAN,
        tl_bdr      = f"{CERULEAN}33",
        # 연락처
        ct_lbl      = CERULEAN,
        ct_val      = OXFORD_NAVY,
        ct_bdr      = f"{CERULEAN}33",
        ct_link_hov = PUNCH_RED,
        # 기술 태그 (모두 Punch Red)
        tag_bg      = PUNCH_RED,
        tag_text    = HONEYDEW,
        sk_cat      = FROSTED_BLUE,
        # 버튼
        btn_bg      = PUNCH_RED,
        btn_text    = HONEYDEW,
        btn_hov_bg  = OXFORD_NAVY,
        # 입력 폼
        input_bdr   = CERULEAN,
        input_text  = OXFORD_NAVY,
        input_ph    = f"{CERULEAN}88",
        ta_bg       = HONEYDEW,
        # 푸터
        footer_txt  = CERULEAN,
        footer_bdr  = f"{CERULEAN}55",
        # 토글
        tog_lbl     = "🌙 다크 모드",
    )


# ══════════════════════════════════════════════════════════════════════════════
#  전역 CSS + 애니메이션
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');

*, *::before, *::after {{ box-sizing: border-box; }}

/* ── 전체 배경 · 텍스트 ── */
.stApp {{
    background-color: {T['bg']} !important;
    font-family: 'Noto Sans KR', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: {T['text']} !important;
}}
.stApp, .stApp .stMarkdown,
.stApp [data-testid="stMarkdown"],
.stApp [data-testid="stMarkdown"] *,
.stApp .element-container,
.stApp .element-container * {{
    color: {T['text']} !important;
}}

/* ── Streamlit 기본 UI 제거 ── */
#MainMenu, footer, header, .stDeployButton,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
section[data-testid="stSidebar"] {{ display: none !important; }}

/* ── 컨테이너 여백 ── */
.block-container {{
    max-width: 1080px !important;
    padding: 0 3rem 6rem !important;
    margin: 0 auto !important;
}}
[data-testid="stHorizontalBlock"] {{
    gap: 2.5rem !important;
    align-items: flex-start !important;
}}

/* ── st.toggle 스타일 ── */
[data-testid="stToggle"] label p,
[data-testid="stWidgetLabel"] p {{
    color: {T['nav_clr']} !important;
    font-size: 0.68rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    white-space: nowrap !important;
}}

/* ══════════════════════════════════════
   히어로 애니메이션 키프레임
   ══════════════════════════════════════ */
@keyframes heroBgShift {{
    0%   {{ background-position: 0% 50%; }}
    50%  {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}
@keyframes nameColorCycle {{
    0%   {{ background-position: 0% 50%; }}
    50%  {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}
@keyframes underlineGrow {{
    from {{ transform: scaleX(0); }}
    to   {{ transform: scaleX(1); }}
}}
@keyframes fadeUp {{
    from {{ opacity: 0; transform: translateY(28px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}
@keyframes dotPulse {{
    0%, 100% {{ transform: scale(1);   opacity: 1; }}
    50%       {{ transform: scale(1.7); opacity: 0.5; }}
}}
@keyframes slideInLeft {{
    from {{ opacity: 0; transform: translateX(-16px); }}
    to   {{ opacity: 1; transform: translateX(0); }}
}}

/* ── 히어로 래퍼 ── */
.hero-wrapper {{
    background: linear-gradient({T['hero_bg']});
    background-size: 400% 400%;
    animation: heroBgShift 10s ease infinite;
    padding: 4.5rem 3rem 5.5rem;
    margin: 0 -3rem;
    border-bottom: 2px solid {T['divider']};
    position: relative;
    overflow: hidden;
}}
.hero-wrapper::before {{
    content: '';
    position: absolute;
    top: -80px; right: -80px;
    width: 300px; height: 300px;
    border-radius: 50%;
    background: radial-gradient(circle, {T['glow_a']} 0%, transparent 70%);
    animation: dotPulse 6s ease-in-out infinite;
    pointer-events: none;
}}
.hero-wrapper::after {{
    content: '';
    position: absolute;
    bottom: -60px; left: 10%;
    width: 200px; height: 200px;
    border-radius: 50%;
    background: radial-gradient(circle, {T['glow_b']} 0%, transparent 70%);
    animation: dotPulse 8s ease-in-out 2s infinite;
    pointer-events: none;
}}

/* ── 히어로 이름 ── */
.hero-name {{
    font-size: clamp(4.5rem, 11vw, 8rem);
    font-weight: 900;
    letter-spacing: -0.03em;
    line-height: 0.92;
    margin: 0 0 1.2rem;
    word-break: keep-all;
    display: inline-block;
    background: linear-gradient(270deg, {T['name_grad']});
    background-size: 400% 400%;
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent !important;
    color: transparent !important;
    animation: nameColorCycle 7s ease infinite,
               fadeUp 0.9s ease 0.1s both;
}}
.hero-underline {{
    height: 3px;
    width: 60px;
    background: linear-gradient(90deg, {PUNCH_RED}, {FROSTED_BLUE});
    margin: 0 0 2rem;
    transform-origin: left;
    animation: underlineGrow 0.8s ease 0.7s both;
}}
.hero-label {{
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: {T['hero_label']} !important;
    margin: 0 0 2rem;
    animation: slideInLeft 0.7s ease forwards;
}}
.hero-sub {{
    animation: fadeUp 0.7s ease 0.5s both;
}}

/* ── 구분선 ── */
.divider {{
    border: none;
    border-top: 1.5px solid {T['divider']};
    margin: 3.5rem 0;
}}

/* ── 섹션 레이블 ── */
.section-label {{
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: {T['label_clr']} !important;
    margin: 0 0 1.8rem;
}}

/* ── 기술 태그 (모두 Punch Red) ── */
.tag-red {{
    display: inline-block;
    background: {T['tag_bg']};
    border: 1.5px solid {T['tag_bg']};
    color: {T['tag_text']} !important;
    padding: 0.25rem 0.78rem;
    margin: 0.22rem 0.15rem;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    transition: opacity 0.2s;
}}
.tag-red:hover {{ opacity: 0.85; }}

/* ── 타임라인 ── */
.tl-item {{
    display: grid;
    grid-template-columns: 90px 1fr;
    gap: 1.5rem;
    padding: 1.4rem 0;
    border-bottom: 1px solid {T['tl_bdr']};
}}
.tl-year  {{ font-size:0.7rem; font-weight:700;
            color:{T['tl_year']} !important;
            letter-spacing:0.06em; padding-top:0.15rem; }}
.tl-title {{ font-size:0.95rem; font-weight:700;
            color:{T['tl_title']} !important; margin:0 0 0.25rem; }}
.tl-detail{{ font-size:0.85rem;
            color:{T['tl_detail']} !important;
            line-height:1.7; margin:0; }}

/* ── 연락처 ── */
.ct-row {{
    display:flex; gap:1.5rem; padding:0.85rem 0;
    border-bottom:1px solid {T['ct_bdr']};
    align-items:baseline; flex-wrap:wrap;
}}
.ct-lbl {{ font-size:0.65rem; font-weight:700;
           letter-spacing:0.14em; text-transform:uppercase;
           color:{T['ct_lbl']} !important; min-width:56px; }}
.ct-val {{ font-size:0.88rem; color:{T['ct_val']} !important; }}
.ct-val a {{ color:{T['ct_val']} !important; text-decoration:none;
             border-bottom:1px solid {T['ct_bdr']}; }}
.ct-val a:hover {{ color:{T['ct_link_hov']} !important;
                   border-color:{T['ct_link_hov']}; }}

/* ══════════════════════════════════════
   Streamlit 입력 컴포넌트
   ══════════════════════════════════════ */
[data-testid="stTextInput"] input,
[data-testid="stTextInput"] input:focus {{
    background: transparent !important;
    border: none !important;
    border-bottom: 1.5px solid {T['input_bdr']} !important;
    border-radius: 0 !important;
    padding: 0.5rem 0 !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    font-size: 0.9rem !important;
    color: {T['input_text']} !important;
    box-shadow: none !important;
}}
[data-testid="stTextInput"] input::placeholder {{
    color: {T['input_ph']} !important;
}}
[data-testid="stTextInput"] label,
[data-testid="stTextArea"]  label {{
    font-size: 0.65rem !important; font-weight: 700 !important;
    letter-spacing: 0.18em !important; text-transform: uppercase !important;
    color: {T['label_clr']} !important;
}}
[data-testid="stTextArea"] textarea {{
    background: {T['ta_bg']} !important;
    border: 1.5px solid {T['input_bdr']}66 !important;
    border-radius: 0 !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    font-size: 0.9rem !important;
    color: {T['input_text']} !important;
    box-shadow: none !important;
    resize: vertical !important;
}}
[data-testid="stTextArea"] textarea:focus {{
    border-color: {T['input_bdr']} !important;
    box-shadow: none !important;
}}
[data-testid="stTextArea"] textarea::placeholder {{
    color: {T['input_ph']} !important;
}}

/* ── 버튼 ── */
[data-testid="stButton"] > button {{
    background: {T['btn_bg']} !important;
    color: {T['btn_text']} !important;
    border: 1.5px solid {T['btn_bg']} !important;
    border-radius: 0 !important;
    padding: 0.75rem 2.5rem !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    font-size: 0.72rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    width: auto !important;
    transition: all 0.25s ease !important;
}}
[data-testid="stButton"] > button:hover {{
    background: {T['btn_hov_bg']} !important;
    border-color: {T['btn_hov_bg']} !important;
    transform: translateY(-2px) !important;
}}

/* ── 알림 ── */
[data-testid="stAlert"] {{
    background: {FROSTED_BLUE}22 !important;
    border: 1px solid {CERULEAN} !important;
    border-radius: 0 !important;
    color: {T['text']} !important;
}}

/* ══════════════════════════════════════
   모바일 반응형
   ══════════════════════════════════════ */
@media screen and (max-width: 768px) {{
    .block-container {{
        padding: 0 1.5rem 4rem !important;
    }}
    .hero-wrapper {{
        padding: 3rem 1.5rem 4rem;
        margin: 0 -1.5rem;
    }}
    [data-testid="stHorizontalBlock"] {{
        flex-wrap: wrap !important;
        gap: 0 !important;
    }}
    [data-testid="stColumn"] {{
        width: 100% !important;
        flex: 1 1 100% !important;
        min-width: 0 !important;
    }}
}}
@media screen and (max-width: 480px) {{
    .block-container {{
        padding: 0 1rem 3rem !important;
    }}
    .hero-wrapper {{
        margin: 0 -1rem;
        padding: 2.5rem 1rem 3.5rem;
    }}
}}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  헬퍼 함수
# ══════════════════════════════════════════════════════════════════════════════
def divider() -> None:
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

def label(text: str) -> None:
    st.markdown(f"<p class='section-label'>{text}</p>", unsafe_allow_html=True)

def tag(text: str) -> str:
    """모든 태그: Punch Red 채움"""
    return f"<span class='tag-red'>{text}</span>"

def sk_cat(text: str) -> str:
    return (
        f"<p style='font-size:0.65rem;font-weight:700;letter-spacing:0.14em;"
        f"text-transform:uppercase;color:{T['sk_cat']} !important;"
        f"margin:0 0 0.8rem;'>{text}</p>"
    )

def tl(year: str, title: str, detail: str) -> str:
    return (
        f"<div class='tl-item'>"
        f"<span class='tl-year'>{year}</span>"
        f"<div><p class='tl-title'>{title}</p>"
        f"<p class='tl-detail'>{detail}</p></div>"
        f"</div>"
    )

def ct_row(lbl: str, val: str, href: str = "") -> str:
    v = (f'<a href="{href}" target="_blank">{val}</a>'
         if href else f"<span>{val}</span>")
    return (
        f"<div class='ct-row'>"
        f"<span class='ct-lbl'>{lbl}</span>"
        f"<span class='ct-val'>{v}</span>"
        f"</div>"
    )


# ══════════════════════════════════════════════════════════════════════════════
#  ① 헤더 — 로고 / 네비 / 토글
# ══════════════════════════════════════════════════════════════════════════════
hdr_logo, hdr_nav, hdr_tog = st.columns([2, 5, 2])

with hdr_logo:
    st.markdown(
        f"<div style='padding:2rem 0 1.8rem;'>"
        f"<span style='font-size:0.85rem;font-weight:900;letter-spacing:0.18em;"
        f"color:{T['text']} !important;text-transform:uppercase;'>HSY</span></div>",
        unsafe_allow_html=True,
    )

with hdr_nav:
    st.markdown(
        f"<div style='padding:2.2rem 0 1.8rem;display:flex;gap:2rem;flex-wrap:wrap;'>"
        + "".join(
            f"<span style='font-size:0.68rem;font-weight:700;letter-spacing:0.16em;"
            f"text-transform:uppercase;color:{T['nav_clr']} !important;cursor:default;'>{n}</span>"
            for n in ["About", "Skills", "Career", "Contact"]
        )
        + "</div>",
        unsafe_allow_html=True,
    )

with hdr_tog:
    st.markdown("<div style='padding-top:1.6rem;'>", unsafe_allow_html=True)
    st.toggle(T["tog_lbl"], key="dark_mode")
    st.markdown("</div>", unsafe_allow_html=True)

# 헤더 하단 구분선
st.markdown(
    f"<hr style='border:none;border-top:1.5px solid {T['divider']};"
    f"margin:0 0 0;'>",
    unsafe_allow_html=True,
)


# ══════════════════════════════════════════════════════════════════════════════
#  ② 히어로 — 색상 애니메이션
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="hero-wrapper">

  <p class="hero-label">
    Power Engineer &nbsp;/&nbsp; Developer &nbsp;/&nbsp; Lifelong Learner
  </p>

  <h1 class="hero-name">허수영</h1>

  <div class="hero-underline"></div>

  <div class="hero-sub" style='display:flex;align-items:center;
       gap:1.2rem;flex-wrap:wrap;'>
    <p style='font-size:1rem;font-weight:400;
         color:{T["hero_sub_p"]} !important;
         letter-spacing:0.01em;margin:0;'>
      한전KDN&nbsp;·&nbsp;미터링시스템부
    </p>
    <span style='width:1px;height:1rem;
         background:{T["border"]}88;display:inline-block;'></span>
    <p style='font-size:0.85rem;font-weight:300;
         color:{T["hero_sub_s"]} !important;margin:0;'>
      전력 IT &nbsp;·&nbsp; 데이터 분석 &nbsp;·&nbsp; AI 활용
    </p>
  </div>

  <div style='display:flex;gap:0.5rem;margin-top:2.5rem;'>
    <span style='width:8px;height:8px;border-radius:50%;
         background:{PUNCH_RED};display:inline-block;
         animation:dotPulse 2s ease-in-out infinite;'></span>
    <span style='width:8px;height:8px;border-radius:50%;
         background:{FROSTED_BLUE};display:inline-block;
         animation:dotPulse 2s ease-in-out 0.4s infinite;'></span>
    <span style='width:8px;height:8px;border-radius:50%;
         background:{CERULEAN};display:inline-block;
         animation:dotPulse 2s ease-in-out 0.8s infinite;'></span>
    <span style='width:8px;height:8px;border-radius:50%;
         background:{T["text"]};display:inline-block;
         animation:dotPulse 2s ease-in-out 1.2s infinite;'></span>
  </div>

</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:4rem'></div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  ③ About + 핵심 정보
# ══════════════════════════════════════════════════════════════════════════════
about_l, about_r = st.columns([3, 2])

with about_l:
    label("About")
    st.markdown(f"""
<p style='font-size:1.3rem;font-weight:500;line-height:1.75;
     color:{T["about_strong"]} !important;word-break:keep-all;margin:0 0 1.5rem;'>
  전력 계량 시스템을 운영하며, 기술로 더 스마트한 에너지 세상을
  만들어 가고자 하는 엔지니어입니다.
</p>
<p style='font-size:0.9rem;font-weight:300;line-height:1.95;
     color:{T["about_body"]} !important;word-break:keep-all;margin:0;'>
  한전KDN 미터링시스템부에서 스마트미터 및 AMI 시스템 운영·유지보수를 담당합니다.
  AI와 웹 기술을 업무에 접목하는 데 관심을 갖고, 바이브코딩 실습 과정을 통해
  Python · React · Streamlit 기반의 실전 개발 역량을 키우고 있습니다.
</p>
""", unsafe_allow_html=True)

with about_r:
    label("Info")
    for k, v in [
        ("소속",  "한국전력KDN"),
        ("부서",  "미터링시스템부"),
        ("직무",  "전력 계량 시스템 운영 · 개발"),
        ("관심사","AI 활용 · 데이터 분석 · 자동화"),
        ("MBTI",  "ISTP"),
    ]:
        st.markdown(f"""
<div style='display:flex;gap:1.5rem;padding:0.9rem 0;
     border-bottom:1px solid {T["info_bdr"]};align-items:baseline;'>
  <span style='font-size:0.65rem;font-weight:700;letter-spacing:0.14em;
       text-transform:uppercase;color:{T["info_lbl"]} !important;
       min-width:52px;'>{k}</span>
  <span style='font-size:0.88rem;font-weight:400;
       color:{T["info_val"]} !important;'>{v}</span>
</div>""", unsafe_allow_html=True)

divider()


# ══════════════════════════════════════════════════════════════════════════════
#  ④ 기술 스택 — 모두 Punch Red 태그
# ══════════════════════════════════════════════════════════════════════════════
label("Skills & Tools")

sk1, sk2, sk3 = st.columns(3)

with sk1:
    st.markdown(
        sk_cat("Language")
        + tag("Python") + tag("SQL") + tag("JavaScript") + tag("HTML/CSS"),
        unsafe_allow_html=True)

with sk2:
    st.markdown(
        sk_cat("Data · AI")
        + tag("Pandas") + tag("NumPy") + tag("Matplotlib") + tag("Streamlit"),
        unsafe_allow_html=True)

with sk3:
    st.markdown(
        sk_cat("Web · Tools")
        + tag("React") + tag("Vite") + tag("TypeScript")
        + tag("Git") + tag("VS Code") + tag("Claude AI"),
        unsafe_allow_html=True)

divider()


# ══════════════════════════════════════════════════════════════════════════════
#  ⑤ 경력 타임라인
# ══════════════════════════════════════════════════════════════════════════════
car_l, car_r = st.columns([1, 2])

with car_l:
    label("Career")
    st.markdown(f"""
<p style='font-size:0.88rem;font-weight:300;
     color:{T["about_body"]} !important;
     line-height:1.85;margin:0;word-break:keep-all;'>
  전력 IT 현장 운영부터<br>바이브코딩·AI 개발까지,<br>
  끊임없이 성장 중입니다.
</p>""", unsafe_allow_html=True)

with car_r:
    st.markdown(
        tl("2026 —",  "KDN 풀스택 바이브코딩 웹 실습 3기",
           "AI 협업 개발(바이브코딩) 역량 강화 과정 수료 중")
      + tl("2025",    "KDN 개발 일정 관리 대시보드",
           "Vite + React + TypeScript 기반 사내 대시보드 직접 개발")
      + tl("2023 —",  "한전KDN 미터링시스템부",
           "스마트미터 및 AMI(Advanced Metering Infrastructure) 시스템 운영 · 유지보수")
      + tl("진행 중", "데이터 분석 · AI 자동화 연구",
           "Python 기반 데이터 파이프라인 구축 및 Claude AI 활용 업무 자동화"),
        unsafe_allow_html=True)

divider()


# ══════════════════════════════════════════════════════════════════════════════
#  ⑥ Contact — 연락처 + 메시지 폼
# ══════════════════════════════════════════════════════════════════════════════
ct_l, ct_r = st.columns([1, 1])

with ct_l:
    label("Contact")
    st.markdown(f"""
<p style='font-size:1.1rem;font-weight:500;line-height:1.75;
     color:{T["about_strong"]} !important;margin:0 0 2.5rem;word-break:keep-all;'>
  새로운 아이디어나 협업 제안이 있으시면<br>언제든 연락해 주세요.
</p>""", unsafe_allow_html=True)

    st.markdown(
        ct_row("사내 메일", "heosy_208@kdn.com",   "mailto:heosy_208@kdn.com")
      + ct_row("개인 메일", "heoeo9587@gmail.com",  "mailto:heoeo9587@gmail.com")
      + ct_row("GitHub",   "github.com/hssu0",      "https://github.com/hssu0")
      + ct_row("소속",     "한국전력KDN · 미터링시스템부"),
        unsafe_allow_html=True)

with ct_r:
    label("Send a Message")

    name_val  = st.text_input("이름  NAME",    placeholder="홍길동")
    email_val = st.text_input("이메일  EMAIL", placeholder="example@email.com")
    msg_val   = st.text_area("메시지  MESSAGE", placeholder="안녕하세요, ...", height=130)

    st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)

    if st.button("SEND MESSAGE"):
        if name_val and email_val and msg_val:
            st.success(f"✓  메시지를 전달했습니다. 감사합니다, {name_val}님.")
        else:
            st.warning("모든 항목을 입력해 주세요.")


# ══════════════════════════════════════════════════════════════════════════════
#  ⑦ 푸터
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style='display:flex;justify-content:space-between;align-items:center;
     padding:2.5rem 0 0;border-top:1.5px solid {T["footer_bdr"]};
     margin-top:4rem;flex-wrap:wrap;gap:0.5rem;'>
  <span style='font-size:0.7rem;font-weight:900;letter-spacing:0.18em;
       color:{T["text"]} !important;text-transform:uppercase;'>HSY · 허수영</span>
  <div style='display:flex;align-items:center;gap:0.5rem;'>
    <span style='width:7px;height:7px;border-radius:50%;
         background:{PUNCH_RED};display:inline-block;'></span>
    <span style='width:7px;height:7px;border-radius:50%;
         background:{FROSTED_BLUE};display:inline-block;'></span>
    <span style='width:7px;height:7px;border-radius:50%;
         background:{CERULEAN};display:inline-block;'></span>
  </div>
  <span style='font-size:0.7rem;color:{T["footer_txt"]} !important;letter-spacing:0.04em;'>
    © 2026 &nbsp;·&nbsp; Built with Streamlit &nbsp;·&nbsp; KDN 풀스택 바이브코딩 3기
  </span>
</div>
""", unsafe_allow_html=True)
