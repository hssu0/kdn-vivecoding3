import streamlit as st

# ── 페이지 설정 ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="허수영 · Portfolio",
    page_icon="◻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════════════════════
#  전역 CSS — 미니멀 디자인 스튜디오 스타일
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
/* ── Google Fonts 임포트 ── */
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');

/* ── 기본 리셋 ── */
*, *::before, *::after { box-sizing: border-box; }

/* ── 앱 전체 ── */
.stApp {
    background-color: #F7F7F5 !important;
    font-family: 'Noto Sans KR', -apple-system, BlinkMacSystemFont,
                 'Helvetica Neue', Arial, sans-serif !important;
    color: #1A1A1A !important;
}

/* ── Streamlit 기본 UI 완전 제거 ── */
#MainMenu, footer, header,
.stDeployButton,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
section[data-testid="stSidebar"]   { display: none !important; }

/* ── 블록 컨테이너 여백 ── */
.block-container {
    max-width: 1080px !important;
    padding: 0 3rem 6rem !important;
    margin: 0 auto !important;
}

/* ── 컬럼 갭 초기화 ── */
[data-testid="stHorizontalBlock"] {
    gap: 3rem !important;
    align-items: flex-start !important;
}

/* ══════════════════════════════════════
   입력 컴포넌트 — 언더라인 스타일
   ══════════════════════════════════════ */
[data-testid="stTextInput"] input,
[data-testid="stTextInput"] input:focus {
    background: transparent !important;
    border: none !important;
    border-bottom: 1.5px solid #1A1A1A !important;
    border-radius: 0 !important;
    padding: 0.5rem 0 !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    font-size: 0.9rem !important;
    color: #1A1A1A !important;
    box-shadow: none !important;
    outline: none !important;
}
[data-testid="stTextInput"] label,
[data-testid="stTextArea"] label {
    font-size: 0.65rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    color: #888888 !important;
}
[data-testid="stTextArea"] textarea {
    background: transparent !important;
    border: 1.5px solid #D4D4D2 !important;
    border-radius: 0 !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    font-size: 0.9rem !important;
    color: #1A1A1A !important;
    box-shadow: none !important;
    resize: vertical !important;
}
[data-testid="stTextArea"] textarea:focus {
    border-color: #1A1A1A !important;
    box-shadow: none !important;
}

/* ══════════════════════════════════════
   버튼 — 다크 필드 미니멀
   ══════════════════════════════════════ */
[data-testid="stButton"] > button {
    background: #1A1A1A !important;
    color: #F7F7F5 !important;
    border: 1.5px solid #1A1A1A !important;
    border-radius: 0 !important;
    padding: 0.75rem 2.5rem !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    font-size: 0.72rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    width: auto !important;
    transition: all 0.25s ease !important;
}
[data-testid="stButton"] > button:hover {
    background: #F7F7F5 !important;
    color: #1A1A1A !important;
}

/* 성공 알림 */
[data-testid="stAlert"] {
    background: transparent !important;
    border: 1px solid #1A1A1A !important;
    border-radius: 0 !important;
    color: #1A1A1A !important;
}

/* ══════════════════════════════════════
   모바일 반응형
   ══════════════════════════════════════ */
@media screen and (max-width: 768px) {
    .block-container {
        padding: 0 1.5rem 4rem !important;
    }
    [data-testid="stHorizontalBlock"] {
        flex-wrap: wrap !important;
        gap: 0 !important;
    }
    [data-testid="stColumn"] {
        width: 100% !important;
        flex: 1 1 100% !important;
        min-width: 0 !important;
    }
}
@media screen and (max-width: 480px) {
    .block-container { padding: 0 1rem 3rem !important; }
}
</style>
""", unsafe_allow_html=True)


# ── 헬퍼: 섹션 구분선 ────────────────────────────────────────────────────────
def divider(mt: str = "3rem", mb: str = "3rem") -> None:
    st.markdown(
        f"<hr style='border:none;border-top:1px solid #D4D4D2;"
        f"margin:{mt} 0 {mb};'>",
        unsafe_allow_html=True,
    )

# ── 헬퍼: 섹션 레이블 ────────────────────────────────────────────────────────
def label(text: str) -> str:
    return (
        f"<p style='font-size:0.65rem;font-weight:700;"
        f"letter-spacing:0.2em;text-transform:uppercase;"
        f"color:#888888;margin:0 0 1.8rem;'>{text}</p>"
    )

# ── 헬퍼: 스킬 태그 ──────────────────────────────────────────────────────────
def tag(text: str, filled: bool = False) -> str:
    if filled:
        return (
            f"<span style='display:inline-block;"
            f"background:#1A1A1A;color:#F7F7F5;"
            f"border:1px solid #1A1A1A;"
            f"padding:0.25rem 0.75rem;margin:0.2rem 0.15rem;"
            f"font-size:0.75rem;font-weight:500;"
            f"letter-spacing:0.04em;'>{text}</span>"
        )
    return (
        f"<span style='display:inline-block;"
        f"border:1px solid #C8C8C6;color:#1A1A1A;"
        f"padding:0.25rem 0.75rem;margin:0.2rem 0.15rem;"
        f"font-size:0.75rem;font-weight:400;"
        f"letter-spacing:0.04em;'>{text}</span>"
    )

# ── 헬퍼: 타임라인 항목 ──────────────────────────────────────────────────────
def timeline(year: str, title: str, detail: str) -> str:
    return f"""
<div style='display:grid;grid-template-columns:90px 1fr;
     gap:1.5rem;padding:1.4rem 0;border-bottom:1px solid #EBEBEA;'>
  <span style='font-size:0.7rem;font-weight:700;color:#888888;
       letter-spacing:0.06em;padding-top:0.15rem;'>{year}</span>
  <div>
    <p style='font-size:0.95rem;font-weight:700;color:#1A1A1A;
         margin:0 0 0.25rem;'>{title}</p>
    <p style='font-size:0.85rem;color:#6B6B6B;line-height:1.7;margin:0;'>{detail}</p>
  </div>
</div>"""


# ══════════════════════════════════════════════════════════════════════════════
#  ① 헤더 네비게이션
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style='display:flex;justify-content:space-between;align-items:center;
     padding:2.2rem 0 2rem;border-bottom:1px solid #D4D4D2;
     margin-bottom:5rem;'>
  <span style='font-size:0.85rem;font-weight:900;letter-spacing:0.18em;
       color:#1A1A1A;text-transform:uppercase;'>HSY</span>
  <div style='display:flex;gap:2.5rem;'>
    <span style='font-size:0.68rem;font-weight:700;letter-spacing:0.16em;
         text-transform:uppercase;color:#888888;cursor:default;'>About</span>
    <span style='font-size:0.68rem;font-weight:700;letter-spacing:0.16em;
         text-transform:uppercase;color:#888888;cursor:default;'>Skills</span>
    <span style='font-size:0.68rem;font-weight:700;letter-spacing:0.16em;
         text-transform:uppercase;color:#888888;cursor:default;'>Career</span>
    <span style='font-size:0.68rem;font-weight:700;letter-spacing:0.16em;
         text-transform:uppercase;color:#888888;cursor:default;'>Contact</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  ② 히어로
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style='padding-bottom:5rem;'>

  <p style='font-size:0.68rem;font-weight:700;letter-spacing:0.22em;
       text-transform:uppercase;color:#888888;margin:0 0 2rem;'>
    Power Engineer &nbsp;/&nbsp; Developer &nbsp;/&nbsp; Lifelong Learner
  </p>

  <h1 style='font-size:clamp(4.5rem, 11vw, 8rem);font-weight:900;
       letter-spacing:-0.03em;line-height:0.92;color:#1A1A1A;
       margin:0 0 2rem;word-break:keep-all;'>
    허수영
  </h1>

  <div style='display:flex;align-items:center;gap:1.5rem;flex-wrap:wrap;'>
    <p style='font-size:1rem;font-weight:300;color:#6B6B6B;
         letter-spacing:0.01em;margin:0;'>
      한전KDN&nbsp;·&nbsp;미터링시스템부
    </p>
    <span style='width:1px;height:1rem;background:#C8C8C6;display:inline-block;'></span>
    <p style='font-size:0.85rem;font-weight:400;color:#9B9B9B;margin:0;'>
      전력 IT · 데이터 분석 · AI 활용
    </p>
  </div>

</div>
""", unsafe_allow_html=True)

divider("0", "5rem")


# ══════════════════════════════════════════════════════════════════════════════
#  ③ About + 핵심 정보
# ══════════════════════════════════════════════════════════════════════════════
about_l, about_r = st.columns([3, 2])

with about_l:
    st.markdown(label("About"), unsafe_allow_html=True)
    st.markdown("""
<p style='font-size:1.35rem;font-weight:500;line-height:1.7;
     color:#1A1A1A;word-break:keep-all;margin:0 0 1.5rem;'>
  전력 계량 시스템을 운영하며, 기술로 더 스마트한 에너지 세상을
  만들어 가고자 하는 엔지니어입니다.
</p>
<p style='font-size:0.9rem;font-weight:300;line-height:1.9;
     color:#6B6B6B;word-break:keep-all;margin:0;'>
  한전KDN 미터링시스템부에서 스마트미터 및 AMI 시스템 운영·유지보수를 담당합니다.
  AI와 웹 기술을 업무에 접목하는 데 관심을 갖고, 바이브코딩 실습 과정을 통해
  Python · React · Streamlit 기반의 실전 개발 역량을 키우고 있습니다.
</p>
""", unsafe_allow_html=True)

with about_r:
    st.markdown(label("Info"), unsafe_allow_html=True)
    for item in [
        ("소속", "한국전력KDN"),
        ("부서", "미터링시스템부"),
        ("직무", "전력 계량 시스템 운영 · 개발"),
        ("관심사", "AI 활용 · 데이터 분석 · 자동화"),
        ("MBTI", "ISTP"),
    ]:
        st.markdown(f"""
<div style='display:flex;gap:1.5rem;padding:0.9rem 0;
     border-bottom:1px solid #EBEBEA;align-items:baseline;'>
  <span style='font-size:0.65rem;font-weight:700;letter-spacing:0.14em;
       text-transform:uppercase;color:#888888;min-width:52px;'>{item[0]}</span>
  <span style='font-size:0.88rem;font-weight:400;color:#1A1A1A;'>{item[1]}</span>
</div>""", unsafe_allow_html=True)

divider()


# ══════════════════════════════════════════════════════════════════════════════
#  ④ 기술 스택
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(label("Skills & Tools"), unsafe_allow_html=True)

skill_l, skill_r, skill_s = st.columns([1, 1, 1])

with skill_l:
    st.markdown("""
<p style='font-size:0.68rem;font-weight:700;letter-spacing:0.14em;
     text-transform:uppercase;color:#C8C8C6;margin:0 0 0.8rem;'>Language</p>
""" + tag("Python", True) + tag("SQL") + tag("JavaScript") + tag("HTML / CSS"),
    unsafe_allow_html=True)

with skill_r:
    st.markdown("""
<p style='font-size:0.68rem;font-weight:700;letter-spacing:0.14em;
     text-transform:uppercase;color:#C8C8C6;margin:0 0 0.8rem;'>Data · AI</p>
""" + tag("Pandas", True) + tag("NumPy") + tag("Matplotlib") + tag("Streamlit"),
    unsafe_allow_html=True)

with skill_s:
    st.markdown("""
<p style='font-size:0.68rem;font-weight:700;letter-spacing:0.14em;
     text-transform:uppercase;color:#C8C8C6;margin:0 0 0.8rem;'>Web · Tools</p>
""" + tag("React", True) + tag("Vite") + tag("TypeScript")
  + tag("Git") + tag("VS Code") + tag("Claude AI"),
    unsafe_allow_html=True)

divider()


# ══════════════════════════════════════════════════════════════════════════════
#  ⑤ 경력 타임라인
# ══════════════════════════════════════════════════════════════════════════════
career_l, career_r = st.columns([1, 2])

with career_l:
    st.markdown(label("Career"), unsafe_allow_html=True)
    st.markdown("""
<p style='font-size:0.88rem;font-weight:300;color:#6B6B6B;
     line-height:1.8;margin:0;word-break:keep-all;'>
  전력 IT 현장 운영부터<br>바이브코딩·AI 개발까지,<br>
  끊임없이 성장 중입니다.
</p>""", unsafe_allow_html=True)

with career_r:
    st.markdown(
        timeline("2026 —", "KDN 풀스택 바이브코딩 웹 실습 3기",
                 "AI 협업 개발(바이브코딩) 역량 강화 과정 수료 중") +
        timeline("2025", "KDN 개발 일정 관리 대시보드",
                 "Vite + React + TypeScript 기반 사내 대시보드 직접 개발") +
        timeline("2023 —", "한전KDN 미터링시스템부",
                 "스마트미터 및 AMI(Advanced Metering Infrastructure) 시스템 운영 · 유지보수") +
        timeline("진행 중", "데이터 분석 · AI 자동화 연구",
                 "Python 기반 데이터 파이프라인 구축 및 Claude AI 활용 업무 자동화"),
        unsafe_allow_html=True,
    )

divider()


# ══════════════════════════════════════════════════════════════════════════════
#  ⑥ Contact — 연락처 + 메시지 폼
# ══════════════════════════════════════════════════════════════════════════════
contact_l, contact_r = st.columns([1, 1])

with contact_l:
    st.markdown(label("Contact"), unsafe_allow_html=True)
    st.markdown("""
<p style='font-size:1.15rem;font-weight:500;line-height:1.7;
     color:#1A1A1A;margin:0 0 2.5rem;word-break:keep-all;'>
  새로운 아이디어나 협업 제안이 있으시면<br>언제든 연락해 주세요.
</p>""", unsafe_allow_html=True)

    for lbl, val, href in [
        ("사내 메일", "heosy_208@kdn.com",  "mailto:heosy_208@kdn.com"),
        ("개인 메일", "heoeo9587@gmail.com", "mailto:heoeo9587@gmail.com"),
        ("GitHub",   "github.com/hssu0",    "https://github.com/hssu0"),
        ("소속",     "한국전력KDN · 미터링시스템부", None),
    ]:
        val_html = (
            f'<a href="{href}" target="_blank" '
            f'style="color:#1A1A1A;text-decoration:none;">'
            f'{val}</a>'
        ) if href else f'<span>{val}</span>'

        st.markdown(f"""
<div style='display:flex;gap:1.5rem;padding:0.85rem 0;
     border-bottom:1px solid #EBEBEA;align-items:baseline;'>
  <span style='font-size:0.65rem;font-weight:700;letter-spacing:0.14em;
       text-transform:uppercase;color:#888888;min-width:56px;'>{lbl}</span>
  <span style='font-size:0.88rem;color:#1A1A1A;'>{val_html}</span>
</div>""", unsafe_allow_html=True)

with contact_r:
    st.markdown(label("Send a Message"), unsafe_allow_html=True)

    sender_name = st.text_input("이름  NAME", placeholder="홍길동")
    sender_email = st.text_input("이메일  EMAIL", placeholder="example@email.com")
    message = st.text_area("메시지  MESSAGE", placeholder="안녕하세요, ...", height=130)

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    if st.button("SEND MESSAGE"):
        if sender_name and sender_email and message:
            st.success(f"✓  메시지가 전달되었습니다. 감사합니다, {sender_name}님.")
        else:
            st.warning("모든 항목을 입력해 주세요.")


# ══════════════════════════════════════════════════════════════════════════════
#  ⑦ 푸터
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style='display:flex;justify-content:space-between;align-items:center;
     padding:2.5rem 0 0;border-top:1px solid #D4D4D2;margin-top:4rem;
     flex-wrap:wrap;gap:0.5rem;'>
  <span style='font-size:0.7rem;font-weight:700;letter-spacing:0.14em;
       color:#1A1A1A;text-transform:uppercase;'>HSY · 허수영</span>
  <span style='font-size:0.7rem;color:#9B9B9B;letter-spacing:0.04em;'>
    © 2026 &nbsp;·&nbsp; Built with Streamlit &nbsp;·&nbsp; KDN 풀스택 바이브코딩 3기
  </span>
</div>
""", unsafe_allow_html=True)
