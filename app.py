import streamlit as st

# ── 페이지 설정 ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="허수영 | 자기소개",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── 세션 상태 초기화 (다크 모드 기본값 True) ─────────────────────────────────
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

IS_DARK = st.session_state.dark_mode

# ══════════════════════════════════════════════════════════════════════════════
#  테마 팔레트
# ══════════════════════════════════════════════════════════════════════════════
if IS_DARK:
    T = dict(
        bg        = "linear-gradient(135deg,#0f2027 0%,#203a43 50%,#2c5364 100%)",
        card_bg   = "rgba(255,255,255,0.07)",
        card_bd   = "rgba(255,255,255,0.15)",
        card_shd  = "0 4px 24px rgba(0,0,0,0.35)",
        text      = "#e0e0e0",
        sub       = "#b0bec5",
        muted     = "#cfd8dc",
        accent    = "#00c6ff",
        accent2   = "#90caf9",
        strong    = "#e0f7fa",
        tl_date   = "#80cbc4",
        tl_line   = "#0072ff",
        link      = "#64b5f6",
        hero_g1   = "#00c6ff",
        hero_g2   = "#0072ff",
        hero_sub  = "#90caf9",
        hero_p    = "#b0bec5",
        c_bdr     = "rgba(255,255,255,0.08)",
        shd       = "rgba(0,0,0,0.40)",
        divider   = "rgba(255,255,255,0.12)",
        tog       = "☀️",
        tog_lbl   = "라이트 모드",
        btn_bg    = "rgba(255,255,255,0.10)",
        btn_hov   = "#00c6ff",
    )
else:
    T = dict(
        bg        = "linear-gradient(135deg,#dbeafe 0%,#f0f9ff 60%,#f8fafc 100%)",
        card_bg   = "rgba(255,255,255,0.92)",
        card_bd   = "rgba(0,114,255,0.18)",
        card_shd  = "0 4px 24px rgba(0,114,255,0.10)",
        text      = "#0f172a",
        sub       = "#334155",
        muted     = "#475569",
        accent    = "#0055d4",
        accent2   = "#1565c0",
        strong    = "#0d47a1",
        tl_date   = "#0284c7",
        tl_line   = "#0072ff",
        link      = "#0055d4",
        hero_g1   = "#0055d4",
        hero_g2   = "#00a8ff",
        hero_sub  = "#1565c0",
        hero_p    = "#334155",
        c_bdr     = "rgba(0,0,0,0.07)",
        shd       = "rgba(0,0,0,0.12)",
        divider   = "rgba(0,0,0,0.10)",
        tog       = "🌙",
        tog_lbl   = "다크 모드",
        btn_bg    = "rgba(0,114,255,0.08)",
        btn_hov   = "#0072ff",
    )

# ── 섹션 카드 기본 스타일 ─────────────────────────────────────────────────────
CARD = (
    f"background:{T['card_bg']};"
    f"border:1px solid {T['card_bd']};"
    f"border-radius:16px;"
    f"padding:1.6rem 1.4rem;"
    f"margin-bottom:1rem;"
    f"box-shadow:{T['card_shd']};"
)

# ══════════════════════════════════════════════════════════════════════════════
#  전역 CSS 주입  (테마 + 반응형)
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<style>
/* ── 배경 · 텍스트 기본 ── */
.stApp {{
    background: {T['bg']} !important;
    color: {T['text']} !important;
}}
.stApp p, .stApp li, .stApp span, .stApp label {{
    color: {T['text']};
}}
/* Streamlit 기본 UI 숨기기 */
section[data-testid="stSidebar"]  {{ display: none !important; }}
footer                             {{ visibility: hidden !important; }}
#MainMenu                          {{ visibility: hidden !important; }}
[data-testid="stToolbar"]          {{ display: none !important; }}
.stDeployButton                    {{ display: none !important; }}

/* ── 토글 버튼 ── */
div[data-testid="stButton"] > button {{
    background: {T['btn_bg']} !important;
    border: 1px solid {T['card_bd']} !important;
    color: {T['text']} !important;
    border-radius: 20px !important;
    padding: 0.3rem 1.1rem !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    transition: all 0.25s ease !important;
    white-space: nowrap !important;
    width: 100% !important;
}}
div[data-testid="stButton"] > button:hover {{
    background: {T['btn_hov']} !important;
    color: #fff !important;
    border-color: {T['btn_hov']} !important;
}}

/* ── 스크롤바 ── */
::-webkit-scrollbar               {{ width: 5px; height: 5px; }}
::-webkit-scrollbar-thumb         {{ background: {T['accent']}; border-radius: 3px; }}
::-webkit-scrollbar-track         {{ background: transparent; }}

/* ══════════════════════════════════════════════════════
   모바일 반응형
   ══════════════════════════════════════════════════════ */

/* 태블릿 이하 (≤768px): 2열 → 1열 */
@media screen and (max-width: 768px) {{

    /* 컨테이너 패딩 축소 */
    .block-container {{
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 1rem !important;
    }}

    /* Streamlit 컬럼 세로 스택 */
    [data-testid="stHorizontalBlock"] {{
        flex-wrap: wrap !important;
        gap: 0 !important;
    }}
    [data-testid="stColumn"] {{
        width: 100% !important;
        flex: 1 1 100% !important;
        min-width: 0 !important;
    }}

    /* 히어로 이름 크기 */
    .hero-title {{ font-size: 2rem !important; }}

    /* 히어로 카드 패딩 */
    .hero-card {{ padding: 1.5rem 1rem !important; }}
}}

/* 소형 모바일 (≤480px) */
@media screen and (max-width: 480px) {{
    .block-container {{
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }}
    .hero-title {{ font-size: 1.7rem !important; }}
}}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  헬퍼 함수
# ══════════════════════════════════════════════════════════════════════════════
def section_title(icon: str, title: str) -> str:
    return (
        f"<p style='font-size:1.15rem;font-weight:700;color:{T['accent']};"
        f"border-bottom:2px solid {T['accent']}33;"
        f"padding-bottom:0.4rem;margin:0 0 1rem 0;'>"
        f"{icon}&nbsp;{title}</p>"
    )

def badge(text: str, c1: str = "#0072ff", c2: str = "#1565c0") -> str:
    return (
        f"<span style='display:inline-block;"
        f"background:linear-gradient(135deg,{c2},{c1});"
        f"border-radius:8px;padding:0.28rem 0.72rem;"
        f"font-size:0.81rem;font-weight:600;color:#fff;"
        f"margin:0.22rem 0.18rem;"
        f"box-shadow:0 2px 8px {T['shd']};'>{text}</span>"
    )

def timeline_item(date: str, title: str, detail: str) -> str:
    return (
        f"<div style='border-left:3px solid {T['tl_line']};"
        f"padding:0.45rem 0 0.45rem 1rem;margin-bottom:0.85rem;'>"
        f"<div style='font-size:0.76rem;color:{T['tl_date']};margin-bottom:0.1rem;'>{date}</div>"
        f"<div style='font-weight:700;color:{T['strong']};font-size:0.95rem;'>{title}</div>"
        f"<div style='font-size:0.84rem;color:{T['sub']};margin-top:0.18rem;'>{detail}</div>"
        f"</div>"
    )

def contact_row(label: str, value: str) -> str:
    return (
        f"<div style='display:flex;gap:0.6rem;padding:0.5rem 0;"
        f"border-bottom:1px solid {T['c_bdr']};font-size:0.91rem;flex-wrap:wrap;'>"
        f"<span style='color:{T['accent2']};font-weight:600;min-width:90px;'>{label}</span>"
        f"<span style='color:{T['muted']};'>{value}</span></div>"
    )

github_link = (
    f'<a href="https://github.com/hssu0" '
    f'style="color:{T["link"]};text-decoration:none;">github.com/hssu0</a>'
)


# ══════════════════════════════════════════════════════════════════════════════
#  상단 네비 바 (로고 + 토글 버튼)
# ══════════════════════════════════════════════════════════════════════════════
nav_l, nav_r = st.columns([7, 3])

with nav_l:
    st.markdown(
        f"<p style='color:{T['accent']};font-size:1rem;font-weight:700;"
        f"margin:0;padding:0.4rem 0;'>⚡ 허수영 포트폴리오</p>",
        unsafe_allow_html=True,
    )

with nav_r:
    if st.button(f"{T['tog']}  {T['tog_lbl']}", key="theme_toggle"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

st.markdown(
    f"<hr style='border:none;border-top:1px solid {T['divider']};"
    f"margin:0.2rem 0 1rem;'>",
    unsafe_allow_html=True,
)


# ══════════════════════════════════════════════════════════════════════════════
#  ① 히어로 섹션
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="hero-card" style='{CARD} text-align:center; padding:2.5rem 2rem;'>
  <p class="hero-title" style='
      font-size:2.6rem;font-weight:800;line-height:1.2;
      background:linear-gradient(90deg,{T["hero_g1"]},{T["hero_g2"]});
      -webkit-background-clip:text;-webkit-text-fill-color:transparent;
      margin-bottom:0.2rem;'>🙋 허수영</p>
  <p style='font-size:1.05rem;color:{T["hero_sub"]};font-weight:500;margin-bottom:0.9rem;'>
    한전KDN · 미터링시스템부</p>
  <div style='margin-bottom:0.4rem;line-height:2;'>
    {badge("⚡ 전력 IT 전문가","#1976d2","#0d47a1")}
    {badge("📊 데이터 분석","#0288d1","#01579b")}
    {badge("🌐 웹 개발","#00838f","#006064")}
    {badge("🤖 AI 활용","#6a1b9a","#4a148c")}
  </div>
  <p style='color:{T["hero_p"]};font-size:0.93rem;line-height:1.85;margin-top:1rem;'>
    안녕하세요! 한전KDN 미터링시스템부에서 근무 중인
    <strong style='color:{T["strong"]}'>허수영</strong>입니다.<br>
    전력 계량 시스템 운영·개발 업무를 담당하며, AI와 웹 기술을 업무에 접목하는 데<br>
    큰 관심을 갖고 끊임없이 배우고 있습니다. 🚀
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  ② 2열 — 소개·기술 / 경력·연락처
# ══════════════════════════════════════════════════════════════════════════════
left_col, right_col = st.columns(2, gap="large")

with left_col:

    # 나를 소개합니다
    st.markdown(f"""
<div style='{CARD}'>
  {section_title("👤", "나를 소개합니다")}
  <ul style='line-height:2.1;color:{T["muted"]};padding-left:1.2rem;margin:0;'>
    <li>🏢 <strong style='color:{T["strong"]}'>소속</strong>: 한국전력KDN (한전KDN)</li>
    <li>🏷️ <strong style='color:{T["strong"]}'>부서</strong>: 미터링시스템부</li>
    <li>📌 <strong style='color:{T["strong"]}'>담당</strong>: 전력 계량 시스템 운영 및 개발</li>
    <li>🎯 <strong style='color:{T["strong"]}'>목표</strong>: AI·데이터 기술로 스마트한 전력망 구현</li>
    <li>💡 <strong style='color:{T["strong"]}'>관심사</strong>: 바이브코딩, 데이터 분석, 자동화</li>
  </ul>
</div>
""", unsafe_allow_html=True)

    # 기술 스택
    st.markdown(f"""
<div style='{CARD}'>
  {section_title("🛠️", "기술 스택")}
  <p style='color:{T["accent2"]};font-size:0.8rem;margin:0 0 0.25rem;font-weight:600;'>▸ 언어</p>
  {badge("Python")}
  {badge("SQL")}
  {badge("JavaScript")}
  {badge("HTML / CSS")}
  <p style='color:{T["accent2"]};font-size:0.8rem;margin:0.75rem 0 0.25rem;font-weight:600;'>▸ 데이터 · AI</p>
  {badge("Pandas",   "#2e7d32","#1b5e20")}
  {badge("NumPy",    "#2e7d32","#1b5e20")}
  {badge("Matplotlib","#2e7d32","#1b5e20")}
  {badge("Streamlit","#2e7d32","#1b5e20")}
  <p style='color:{T["accent2"]};font-size:0.8rem;margin:0.75rem 0 0.25rem;font-weight:600;'>▸ 웹 프레임워크</p>
  {badge("React",      "#7b1fa2","#4a148c")}
  {badge("Vite",       "#7b1fa2","#4a148c")}
  {badge("TypeScript", "#7b1fa2","#4a148c")}
  <p style='color:{T["accent2"]};font-size:0.8rem;margin:0.75rem 0 0.25rem;font-weight:600;'>▸ 도구 · 협업</p>
  {badge("Git / GitHub","#ef6c00","#e65100")}
  {badge("VS Code",     "#ef6c00","#e65100")}
  {badge("Claude AI",   "#00796b","#004d40")}
  {badge("Cursor",      "#00796b","#004d40")}
</div>
""", unsafe_allow_html=True)

with right_col:

    # 주요 경력·활동
    st.markdown(f"""
<div style='{CARD}'>
  {section_title("📅", "주요 경력 · 활동")}
  {timeline_item("2026 · 현재",
      "KDN 풀스택 바이브코딩 웹 실습 3기",
      "AI 협업 개발(바이브코딩) 역량 강화 과정 수료 중")}
  {timeline_item("2025",
      "KDN 개발 일정 관리 대시보드 개발",
      "Vite + React + TypeScript 기반 사내 대시보드 직접 개발")}
  {timeline_item("2023 · 현재",
      "한전KDN 미터링시스템부",
      "스마트미터 및 AMI 시스템 운영·유지보수")}
  {timeline_item("학습 중",
      "데이터 분석 · AI 자동화",
      "Python 기반 데이터 파이프라인 구축 및 Claude AI 활용 업무 자동화 연구")}
</div>
""", unsafe_allow_html=True)

    # 연락처
    st.markdown(f"""
<div style='{CARD}'>
  {section_title("📬", "연락처")}
  {contact_row("✉️ 사내 메일", "heosy_208@kdn.com")}
  {contact_row("📧 개인 메일", "heoeo9587@gmail.com")}
  {contact_row("🐙 GitHub", github_link)}
  {contact_row("🏢 소속", "한국전력KDN · 미터링시스템부")}
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  ③ 하단 3카드
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("<div style='height:0.3rem'></div>", unsafe_allow_html=True)
b1, b2, b3 = st.columns(3, gap="medium")

with b1:
    st.markdown(f"""
<div style='{CARD} text-align:center;'>
  {section_title("🎭", "성격 유형")}
  <p style='font-size:2rem;margin:0.2rem 0;'>🧩</p>
  <p style='font-size:1.45rem;font-weight:800;color:{T["accent"]};margin:0.15rem 0;'>ISTP</p>
  <p style='color:{T["sub"]};font-size:0.86rem;margin-top:0.35rem;line-height:1.6;'>
    책임감 강하고 꼼꼼한<br>팀플레이어
  </p>
</div>
""", unsafe_allow_html=True)

with b2:
    st.markdown(f"""
<div style='{CARD} text-align:center;'>
  {section_title("🎯", "관심사 · 취미")}
  <p style='font-size:0.95rem;color:{T["muted"]};line-height:2.3;margin:0;'>
    📊 데이터 시각화<br>
    🤖 AI 활용 실험<br>
    🏃 러닝 · 등산<br>
    📚 IT 기술서 독서
  </p>
</div>
""", unsafe_allow_html=True)

with b3:
    st.markdown(f"""
<div style='{CARD} text-align:center;'>
  {section_title("💬", "한마디")}
  <p style='font-size:1.7rem;margin:0.2rem 0;'>✨</p>
  <p style='color:{T["strong"]};font-size:0.9rem;line-height:1.95;font-style:italic;margin:0;'>
    "기술은 사람을 위해 존재합니다.<br>
    더 스마트한 에너지 세상을<br>
    함께 만들어 나가고 싶습니다."
  </p>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  푸터
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
st.markdown(
    f"<p style='text-align:center;color:{T['sub']};font-size:0.78rem;'>"
    f"© 2026 허수영 &nbsp;·&nbsp; Built with ❤️ &amp; Streamlit "
    f"&nbsp;·&nbsp; KDN 풀스택 바이브코딩 3기</p>",
    unsafe_allow_html=True,
)
