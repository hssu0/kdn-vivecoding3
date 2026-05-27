import streamlit as st
import requests

# ── 페이지 기본 설정 ──────────────────────────────────────────────────────────
st.set_page_config(
    page_title="허수영 | 자기소개",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── 전역 CSS (배경·폰트 등 레이아웃 전체에 적용) ─────────────────────────────
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
}
section[data-testid="stSidebar"] { display: none; }
footer { visibility: hidden; }
h1, h2, h3, p, li, span, div { color: inherit; }
</style>
""", unsafe_allow_html=True)


# ── 헬퍼: 섹션 카드 래퍼 ─────────────────────────────────────────────────────
CARD = (
    "background:rgba(255,255,255,0.07);"
    "border:1px solid rgba(255,255,255,0.15);"
    "border-radius:16px;"
    "padding:1.6rem 1.4rem;"
    "margin-bottom:1rem;"
)

def section_title(icon: str, title: str) -> str:
    return (
        f"<p style='font-size:1.25rem;font-weight:700;color:#00c6ff;"
        f"border-bottom:2px solid rgba(0,198,255,0.3);"
        f"padding-bottom:0.4rem;margin-bottom:1rem;'>"
        f"{icon} {title}</p>"
    )

def badge(text: str, color: str = "#0072ff", bg: str = "#1565c0") -> str:
    return (
        f"<span style='display:inline-block;"
        f"background:linear-gradient(135deg,{bg},{color});"
        f"border-radius:8px;padding:0.3rem 0.75rem;"
        f"font-size:0.82rem;font-weight:600;color:#fff;"
        f"margin:0.25rem 0.2rem;"
        f"box-shadow:0 2px 8px rgba(0,0,0,0.35);'>{text}</span>"
    )

def timeline_item(date: str, title: str, detail: str) -> str:
    return (
        f"<div style='border-left:3px solid #0072ff;"
        f"padding:0.5rem 0 0.5rem 1.1rem;margin-bottom:0.9rem;'>"
        f"<div style='font-size:0.78rem;color:#80cbc4;margin-bottom:0.1rem;'>{date}</div>"
        f"<div style='font-weight:700;color:#e0f7fa;font-size:0.97rem;'>{title}</div>"
        f"<div style='font-size:0.86rem;color:#b0bec5;margin-top:0.2rem;'>{detail}</div>"
        f"</div>"
    )

def contact_row(label: str, value: str) -> str:
    return (
        f"<div style='display:flex;gap:0.6rem;padding:0.55rem 0;"
        f"border-bottom:1px solid rgba(255,255,255,0.08);font-size:0.93rem;'>"
        f"<span style='color:#90caf9;font-weight:600;min-width:90px;'>{label}</span>"
        f"<span style='color:#cfd8dc;'>{value}</span></div>"
    )


# ══════════════════════════════════════════════════════════════════════════════
#  ① 히어로 섹션
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style='{CARD} text-align:center; padding:2.5rem 2rem;'>
  <p style='font-size:2.6rem;font-weight:800;
     background:linear-gradient(90deg,#00c6ff,#0072ff);
     -webkit-background-clip:text;-webkit-text-fill-color:transparent;
     margin-bottom:0.2rem;'>🙋 허수영</p>
  <p style='font-size:1.1rem;color:#90caf9;margin-bottom:0.9rem;'>
    한전KDN · 미터링시스템부</p>
  {badge("⚡ 전력 IT 전문가","#1976d2","#0d47a1")}
  {badge("📊 데이터 분석","#0288d1","#01579b")}
  {badge("🌐 웹 개발","#00838f","#006064")}
  {badge("🤖 AI 활용","#6a1b9a","#4a148c")}
  <p style='color:#b0bec5;font-size:0.95rem;line-height:1.8;margin-top:1.2rem;'>
    안녕하세요! 한전KDN 미터링시스템부에서 근무 중인 <strong style='color:#e0f7fa'>허수영</strong>입니다.<br>
    전력 계량 시스템 운영·개발 업무를 담당하며, AI와 웹 기술을 업무에 접목하는 데<br>
    큰 관심을 갖고 끊임없이 배우고 있습니다. 🚀
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  ② 좌·우 2열 레이아웃
# ══════════════════════════════════════════════════════════════════════════════
left_col, right_col = st.columns([1, 1], gap="large")

# ── 왼쪽 열 ──────────────────────────────────────────────────────────────────
with left_col:

    # 나를 소개합니다
    st.markdown(f"""
<div style='{CARD}'>
  {section_title("👤", "나를 소개합니다")}
  <ul style='line-height:2.1;color:#cfd8dc;padding-left:1.2rem;'>
    <li>🏢 <strong style='color:#e0f7fa'>소속</strong>: 한국전력KDN (한전KDN)</li>
    <li>🏷️ <strong style='color:#e0f7fa'>부서</strong>: 미터링시스템부</li>
    <li>📌 <strong style='color:#e0f7fa'>담당</strong>: 전력 계량 시스템 운영 및 개발</li>
    <li>🎯 <strong style='color:#e0f7fa'>목표</strong>: AI·데이터 기술로 스마트한 전력망 구현</li>
    <li>💡 <strong style='color:#e0f7fa'>관심사</strong>: 바이브코딩, 데이터 분석, 자동화</li>
  </ul>
</div>
""", unsafe_allow_html=True)

    # 기술 스택
    st.markdown(f"""
<div style='{CARD}'>
  {section_title("🛠️", "기술 스택")}
  <p style='color:#90caf9;font-size:0.82rem;margin:0 0 0.3rem;'>▸ 언어</p>
  {badge("Python")}
  {badge("SQL")}
  {badge("JavaScript")}
  {badge("HTML / CSS")}
  <p style='color:#90caf9;font-size:0.82rem;margin:0.8rem 0 0.3rem;'>▸ 데이터 · AI</p>
  {badge("Pandas", "#2e7d32", "#1b5e20")}
  {badge("NumPy", "#2e7d32", "#1b5e20")}
  {badge("Matplotlib", "#2e7d32", "#1b5e20")}
  {badge("Streamlit", "#2e7d32", "#1b5e20")}
  <p style='color:#90caf9;font-size:0.82rem;margin:0.8rem 0 0.3rem;'>▸ 웹 프레임워크</p>
  {badge("React", "#7b1fa2", "#4a148c")}
  {badge("Vite", "#7b1fa2", "#4a148c")}
  {badge("TypeScript", "#7b1fa2", "#4a148c")}
  <p style='color:#90caf9;font-size:0.82rem;margin:0.8rem 0 0.3rem;'>▸ 도구 · 협업</p>
  {badge("Git / GitHub", "#ef6c00", "#e65100")}
  {badge("VS Code", "#ef6c00", "#e65100")}
  {badge("Claude AI", "#00796b", "#004d40")}
  {badge("Cursor", "#00796b", "#004d40")}
</div>
""", unsafe_allow_html=True)

# ── 오른쪽 열 ────────────────────────────────────────────────────────────────
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
  {contact_row("🐙 GitHub",
      '<a href="https://github.com/hssu0" style="color:#64b5f6;text-decoration:none;">github.com/hssu0</a>')}
  {contact_row("🏢 소속", "한국전력KDN · 미터링시스템부")}
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  ③ 하단 3카드
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
b1, b2, b3 = st.columns(3, gap="medium")

with b1:
    st.markdown(f"""
<div style='{CARD} text-align:center;'>
  {section_title("🎭", "성격 유형")}
  <p style='font-size:2.2rem;margin:0.3rem 0;'>🧩</p>
  <p style='font-size:1.5rem;font-weight:800;color:#80deea;margin:0.2rem 0;'>ISFJ</p>
  <p style='color:#b0bec5;font-size:0.88rem;margin-top:0.4rem;'>
    책임감 강하고 꼼꼼한<br>팀플레이어
  </p>
</div>
""", unsafe_allow_html=True)

with b2:
    st.markdown(f"""
<div style='{CARD} text-align:center;'>
  {section_title("🎯", "관심사 · 취미")}
  <p style='font-size:1rem;color:#cfd8dc;line-height:2.2;'>
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
  <p style='font-size:1.8rem;margin:0.3rem 0;'>✨</p>
  <p style='color:#e0f7fa;font-size:0.92rem;line-height:1.9;font-style:italic;'>
    "기술은 사람을 위해 존재합니다.<br>
    더 스마트한 에너지 세상을<br>
    함께 만들어 나가고 싶습니다."
  </p>
</div>
""", unsafe_allow_html=True)

# ── 푸터 ─────────────────────────────────────────────────────────────────────
st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:#546e7a;font-size:0.8rem;'>"
    "© 2026 허수영 · Built with ❤️ &amp; Streamlit · KDN 풀스택 바이브코딩 3기"
    "</p>",
    unsafe_allow_html=True,
)
