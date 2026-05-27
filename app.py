import streamlit as st

# ── 페이지 설정 ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="허수영 · Portfolio",
    page_icon="◻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════════════════════
#  컬러 팔레트
# ══════════════════════════════════════════════════════════════════════════════
PUNCH_RED    = "#e63946"   # 포인트 레드
HONEYDEW     = "#f1faee"   # 배경
FROSTED_BLUE = "#a8dadc"   # 보조 포인트
CERULEAN     = "#457b9d"   # 경계선 / 레이블
OXFORD_NAVY  = "#1d3557"   # 텍스트

# ══════════════════════════════════════════════════════════════════════════════
#  전역 CSS + 애니메이션
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');

/* ── 기본 리셋 ── */
*, *::before, *::after {{ box-sizing: border-box; }}

/* ── 앱 전체 ── */
.stApp {{
    background-color: {HONEYDEW} !important;
    font-family: 'Noto Sans KR', -apple-system, BlinkMacSystemFont,
                 'Helvetica Neue', Arial, sans-serif !important;
    color: {OXFORD_NAVY} !important;
}}

/* ── Streamlit 기본 UI 제거 ── */
#MainMenu, footer, header,
.stDeployButton,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
section[data-testid="stSidebar"] {{ display: none !important; }}

/* ── 텍스트 색 전체 적용 ── */
.stApp, .stApp .stMarkdown,
.stApp [data-testid="stMarkdown"],
.stApp [data-testid="stMarkdown"] *,
.stApp .element-container,
.stApp .element-container * {{
    color: {OXFORD_NAVY} !important;
}}

/* ── 컨테이너 ── */
.block-container {{
    max-width: 1080px !important;
    padding: 0 3rem 6rem !important;
    margin: 0 auto !important;
}}
[data-testid="stHorizontalBlock"] {{
    gap: 3rem !important;
    align-items: flex-start !important;
}}

/* ══════════════════════════════════════
   히어로 섹션 애니메이션
   ══════════════════════════════════════ */

/* 배경 그라디언트 유동 */
@keyframes heroBgShift {{
    0%   {{ background-position: 0% 50%; }}
    50%  {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}

/* 이름 텍스트 색상 순환 */
@keyframes nameColorCycle {{
    0%   {{ background-position: 0% 50%; }}
    50%  {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}

/* 밑줄 확장 */
@keyframes underlineGrow {{
    from {{ transform: scaleX(0); }}
    to   {{ transform: scaleX(1); }}
}}

/* 페이드업 등장 */
@keyframes fadeUp {{
    from {{ opacity: 0; transform: translateY(28px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}

/* 점 펄스 */
@keyframes dotPulse {{
    0%, 100% {{ transform: scale(1);   opacity: 1; }}
    50%       {{ transform: scale(1.6); opacity: 0.6; }}
}}

/* 슬라이드 인 (레이블) */
@keyframes slideInLeft {{
    from {{ opacity: 0; transform: translateX(-16px); }}
    to   {{ opacity: 1; transform: translateX(0); }}
}}

/* 히어로 래퍼 */
.hero-wrapper {{
    background: linear-gradient(
        -45deg,
        {HONEYDEW},
        {FROSTED_BLUE}55,
        {HONEYDEW},
        {CERULEAN}22,
        {HONEYDEW}
    );
    background-size: 400% 400%;
    animation: heroBgShift 10s ease infinite;
    padding: 4.5rem 3rem 5.5rem;
    margin: 0 -3rem;
    border-bottom: 2px solid {CERULEAN}55;
    position: relative;
    overflow: hidden;
}}

/* 히어로 배경 장식 원 */
.hero-wrapper::before {{
    content: '';
    position: absolute;
    top: -80px; right: -80px;
    width: 300px; height: 300px;
    border-radius: 50%;
    background: radial-gradient(circle, {FROSTED_BLUE}44 0%, transparent 70%);
    animation: dotPulse 6s ease-in-out infinite;
    pointer-events: none;
}}
.hero-wrapper::after {{
    content: '';
    position: absolute;
    bottom: -60px; left: 10%;
    width: 200px; height: 200px;
    border-radius: 50%;
    background: radial-gradient(circle, {PUNCH_RED}22 0%, transparent 70%);
    animation: dotPulse 8s ease-in-out 2s infinite;
    pointer-events: none;
}}

/* 히어로 레이블 */
.hero-label {{
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: {CERULEAN} !important;
    margin: 0 0 2rem;
    animation: slideInLeft 0.7s ease forwards;
}}

/* 히어로 이름 - 그라디언트 색상 순환 */
.hero-name {{
    font-size: clamp(4.5rem, 11vw, 8rem);
    font-weight: 900;
    letter-spacing: -0.03em;
    line-height: 0.92;
    margin: 0 0 1.2rem;
    word-break: keep-all;
    display: inline-block;

    background: linear-gradient(
        270deg,
        {OXFORD_NAVY},
        {PUNCH_RED},
        {CERULEAN},
        {FROSTED_BLUE},
        {PUNCH_RED},
        {OXFORD_NAVY}
    );
    background-size: 400% 400%;
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent !important;
    color: transparent !important;

    animation:
        nameColorCycle 7s ease infinite,
        fadeUp 0.9s ease 0.1s both;
}}

/* 히어로 이름 밑줄 장식 */
.hero-underline {{
    height: 3px;
    width: 60px;
    background: linear-gradient(90deg, {PUNCH_RED}, {FROSTED_BLUE});
    margin: 0 0 2rem;
    transform-origin: left;
    animation: underlineGrow 0.8s ease 0.7s both;
}}

/* 히어로 부제 */
.hero-sub {{
    animation: fadeUp 0.7s ease 0.5s both;
}}

/* ══════════════════════════════════════
   컴포넌트 스타일
   ══════════════════════════════════════ */

/* 구분선 */
.divider {{
    border: none;
    border-top: 1.5px solid {CERULEAN}55;
    margin: 3.5rem 0;
}}

/* 섹션 레이블 */
.section-label {{
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: {CERULEAN} !important;
    margin: 0 0 1.8rem;
}}

/* 태그 - 기본 (아웃라인) */
.tag {{
    display: inline-block;
    border: 1.5px solid {CERULEAN}88;
    color: {OXFORD_NAVY} !important;
    padding: 0.25rem 0.75rem;
    margin: 0.2rem 0.15rem;
    font-size: 0.75rem;
    font-weight: 400;
    letter-spacing: 0.04em;
    transition: all 0.2s ease;
}}
/* 태그 - 채움 */
.tag-filled {{
    display: inline-block;
    background: {PUNCH_RED};
    border: 1.5px solid {PUNCH_RED};
    color: {HONEYDEW} !important;
    padding: 0.25rem 0.75rem;
    margin: 0.2rem 0.15rem;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.04em;
}}
/* 태그 - 보조 채움 */
.tag-secondary {{
    display: inline-block;
    background: {FROSTED_BLUE}44;
    border: 1.5px solid {CERULEAN}66;
    color: {OXFORD_NAVY} !important;
    padding: 0.25rem 0.75rem;
    margin: 0.2rem 0.15rem;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.04em;
}}

/* 타임라인 */
.tl-item {{
    display: grid;
    grid-template-columns: 90px 1fr;
    gap: 1.5rem;
    padding: 1.4rem 0;
    border-bottom: 1px solid {CERULEAN}33;
}}
.tl-year {{
    font-size: 0.7rem;
    font-weight: 700;
    color: {CERULEAN} !important;
    letter-spacing: 0.06em;
    padding-top: 0.15rem;
}}
.tl-title {{
    font-size: 0.95rem;
    font-weight: 700;
    color: {OXFORD_NAVY} !important;
    margin: 0 0 0.25rem;
}}
.tl-detail {{
    font-size: 0.85rem;
    color: {CERULEAN} !important;
    line-height: 1.7;
    margin: 0;
}}

/* 연락처 행 */
.ct-row {{
    display: flex;
    gap: 1.5rem;
    padding: 0.85rem 0;
    border-bottom: 1px solid {CERULEAN}33;
    align-items: baseline;
    flex-wrap: wrap;
}}
.ct-lbl {{
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: {CERULEAN} !important;
    min-width: 56px;
}}
.ct-val {{
    font-size: 0.88rem;
    color: {OXFORD_NAVY} !important;
}}
.ct-val a {{
    color: {OXFORD_NAVY} !important;
    text-decoration: none;
    border-bottom: 1px solid {CERULEAN}66;
    transition: border-color 0.2s;
}}
.ct-val a:hover {{
    border-color: {PUNCH_RED};
    color: {PUNCH_RED} !important;
}}

/* ══════════════════════════════════════
   Streamlit 입력 컴포넌트
   ══════════════════════════════════════ */
[data-testid="stTextInput"] input,
[data-testid="stTextInput"] input:focus {{
    background: transparent !important;
    border: none !important;
    border-bottom: 1.5px solid {CERULEAN} !important;
    border-radius: 0 !important;
    padding: 0.5rem 0 !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    font-size: 0.9rem !important;
    color: {OXFORD_NAVY} !important;
    box-shadow: none !important;
    outline: none !important;
}}
[data-testid="stTextInput"] input::placeholder {{
    color: {CERULEAN}88 !important;
}}
[data-testid="stTextInput"] label,
[data-testid="stTextArea"] label {{
    font-size: 0.65rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    color: {CERULEAN} !important;
}}
[data-testid="stTextArea"] textarea {{
    background: {HONEYDEW} !important;
    border: 1.5px solid {CERULEAN}66 !important;
    border-radius: 0 !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    font-size: 0.9rem !important;
    color: {OXFORD_NAVY} !important;
    box-shadow: none !important;
    resize: vertical !important;
}}
[data-testid="stTextArea"] textarea:focus {{
    border-color: {CERULEAN} !important;
    box-shadow: none !important;
}}
[data-testid="stTextArea"] textarea::placeholder {{
    color: {CERULEAN}88 !important;
}}

/* 버튼 — Punch Red */
[data-testid="stButton"] > button {{
    background: {PUNCH_RED} !important;
    color: {HONEYDEW} !important;
    border: 1.5px solid {PUNCH_RED} !important;
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
    background: {OXFORD_NAVY} !important;
    border-color: {OXFORD_NAVY} !important;
    color: {HONEYDEW} !important;
    transform: translateY(-2px) !important;
}}

/* 알림 */
[data-testid="stAlert"] {{
    background: {FROSTED_BLUE}33 !important;
    border: 1px solid {CERULEAN} !important;
    border-radius: 0 !important;
    color: {OXFORD_NAVY} !important;
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
    .block-container {{ padding: 0 1rem 3rem !important; }}
    .hero-wrapper {{ margin: 0 -1rem; padding: 2.5rem 1rem 3.5rem; }}
}}
</style>
""", unsafe_allow_html=True)


# ── 헬퍼 함수 ────────────────────────────────────────────────────────────────
def divider() -> None:
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

def label(text: str) -> None:
    st.markdown(f"<p class='section-label'>{text}</p>", unsafe_allow_html=True)

def tag(text: str, style: str = "outline") -> str:
    cls = {"fill": "tag-filled", "secondary": "tag-secondary"}.get(style, "tag")
    return f"<span class='{cls}'>{text}</span>"

def tl(year: str, title: str, detail: str) -> str:
    return (
        f"<div class='tl-item'>"
        f"<span class='tl-year'>{year}</span>"
        f"<div>"
        f"<p class='tl-title'>{title}</p>"
        f"<p class='tl-detail'>{detail}</p>"
        f"</div></div>"
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
#  ① 헤더 네비게이션
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style='display:flex;justify-content:space-between;align-items:center;
     padding:2.2rem 0 2rem;border-bottom:1.5px solid {CERULEAN}55;
     margin-bottom:0;'>
  <span style='font-size:0.85rem;font-weight:900;letter-spacing:0.18em;
       color:{OXFORD_NAVY};text-transform:uppercase;'>HSY</span>
  <div style='display:flex;gap:2.5rem;'>
    {''.join(
        f'<span style="font-size:0.68rem;font-weight:700;letter-spacing:0.16em;'
        f'text-transform:uppercase;color:{CERULEAN};cursor:default;">{n}</span>'
        for n in ["About","Skills","Career","Contact"]
    )}
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  ② 히어로 — 애니메이션 구간
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
    <p style='font-size:1rem;font-weight:400;color:{OXFORD_NAVY};
         letter-spacing:0.01em;margin:0;'>
      한전KDN&nbsp;·&nbsp;미터링시스템부
    </p>
    <span style='width:1px;height:1rem;background:{CERULEAN}88;
         display:inline-block;'></span>
    <p style='font-size:0.85rem;font-weight:300;
         color:{CERULEAN};margin:0;'>
      전력 IT &nbsp;·&nbsp; 데이터 분석 &nbsp;·&nbsp; AI 활용
    </p>
  </div>

  <!-- 포인트 장식 도트 -->
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
         background:{OXFORD_NAVY};display:inline-block;
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
     color:{OXFORD_NAVY};word-break:keep-all;margin:0 0 1.5rem;'>
  전력 계량 시스템을 운영하며, 기술로 더 스마트한 에너지 세상을
  만들어 가고자 하는 엔지니어입니다.
</p>
<p style='font-size:0.9rem;font-weight:300;line-height:1.95;
     color:{CERULEAN};word-break:keep-all;margin:0;'>
  한전KDN 미터링시스템부에서 스마트미터 및 AMI 시스템 운영·유지보수를 담당합니다.
  AI와 웹 기술을 업무에 접목하는 데 관심을 갖고, 바이브코딩 실습 과정을 통해
  Python · React · Streamlit 기반의 실전 개발 역량을 키우고 있습니다.
</p>
""", unsafe_allow_html=True)

with about_r:
    label("Info")
    rows = [
        ("소속",  "한국전력KDN"),
        ("부서",  "미터링시스템부"),
        ("직무",  "전력 계량 시스템 운영 · 개발"),
        ("관심사","AI 활용 · 데이터 분석 · 자동화"),
        ("MBTI",  "ISTP"),
    ]
    for k, v in rows:
        st.markdown(f"""
<div style='display:flex;gap:1.5rem;padding:0.9rem 0;
     border-bottom:1px solid {CERULEAN}33;align-items:baseline;'>
  <span style='font-size:0.65rem;font-weight:700;letter-spacing:0.14em;
       text-transform:uppercase;color:{CERULEAN};min-width:52px;'>{k}</span>
  <span style='font-size:0.88rem;font-weight:400;color:{OXFORD_NAVY};'>{v}</span>
</div>""", unsafe_allow_html=True)

divider()


# ══════════════════════════════════════════════════════════════════════════════
#  ④ 기술 스택
# ══════════════════════════════════════════════════════════════════════════════
label("Skills & Tools")

sk1, sk2, sk3 = st.columns(3)

with sk1:
    st.markdown(
        f"<p style='font-size:0.65rem;font-weight:700;letter-spacing:0.14em;"
        f"text-transform:uppercase;color:{FROSTED_BLUE};margin:0 0 0.8rem;'>Language</p>"
        + tag("Python","fill") + tag("SQL") + tag("JavaScript") + tag("HTML/CSS"),
        unsafe_allow_html=True)

with sk2:
    st.markdown(
        f"<p style='font-size:0.65rem;font-weight:700;letter-spacing:0.14em;"
        f"text-transform:uppercase;color:{FROSTED_BLUE};margin:0 0 0.8rem;'>Data · AI</p>"
        + tag("Pandas","fill") + tag("NumPy") + tag("Matplotlib") + tag("Streamlit","secondary"),
        unsafe_allow_html=True)

with sk3:
    st.markdown(
        f"<p style='font-size:0.65rem;font-weight:700;letter-spacing:0.14em;"
        f"text-transform:uppercase;color:{FROSTED_BLUE};margin:0 0 0.8rem;'>Web · Tools</p>"
        + tag("React","fill") + tag("Vite") + tag("TypeScript")
        + tag("Git","secondary") + tag("VS Code") + tag("Claude AI","secondary"),
        unsafe_allow_html=True)

divider()


# ══════════════════════════════════════════════════════════════════════════════
#  ⑤ 경력 타임라인
# ══════════════════════════════════════════════════════════════════════════════
car_l, car_r = st.columns([1, 2])

with car_l:
    label("Career")
    st.markdown(f"""
<p style='font-size:0.88rem;font-weight:300;color:{CERULEAN};
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
     color:{OXFORD_NAVY};margin:0 0 2.5rem;word-break:keep-all;'>
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
     padding:2.5rem 0 0;border-top:1.5px solid {CERULEAN}55;margin-top:4rem;
     flex-wrap:wrap;gap:0.5rem;'>
  <span style='font-size:0.7rem;font-weight:900;letter-spacing:0.18em;
       color:{OXFORD_NAVY};text-transform:uppercase;'>HSY · 허수영</span>
  <div style='display:flex;align-items:center;gap:0.6rem;'>
    <span style='width:8px;height:8px;border-radius:50%;
         background:{PUNCH_RED};display:inline-block;'></span>
    <span style='width:8px;height:8px;border-radius:50%;
         background:{FROSTED_BLUE};display:inline-block;'></span>
    <span style='width:8px;height:8px;border-radius:50%;
         background:{CERULEAN};display:inline-block;'></span>
  </div>
  <span style='font-size:0.7rem;color:{CERULEAN};letter-spacing:0.04em;'>
    © 2026 &nbsp;·&nbsp; Built with Streamlit &nbsp;·&nbsp; KDN 풀스택 바이브코딩 3기
  </span>
</div>
""", unsafe_allow_html=True)
