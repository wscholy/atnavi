import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

# 페이지 기본 설정
st.set_page_config(
    page_title="AT-Navi: AI-Teacher Navigator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 스타일 커스터마이징 (CSS)
st.markdown("""
    <style>
        .main {
            background-color: #f8fafc;
        }
        .stButton>button {
            width: 100%;
            border-radius: 8px;
            height: 3em;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            border: 1px solid #e2e8f0;
        }
        .highlight {
            color: #4f46e5;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# 사이드바 설정
with st.sidebar:
    st.header("🧠 AT-Navi")
    st.caption("AI-Teacher Navigator")
    
    st.markdown("---")
    
    # 메뉴 선택
    menu = st.radio(
        "메뉴 이동",
        ["1. 수업 계획 (AiTOM)", "2. 교실 진단 (C-AiTOM)", "3. 실시간 내비 (P-AiTOM)", "4. 교수활동 프로파일", "5. 시스템 활용 가이드"],
        index=0
    )
    
    st.markdown("---")
    
    # 사용자 프로필
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown(
            """<div style='background-color:#a5b4fc; width:40px; height:40px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold; color:#312e81;'>김</div>""", 
            unsafe_allow_html=True
        )
    with col2:
        st.write("**김STEM 선생님**")
        st.caption("한국과학중학교")

# 헤더 영역
col_header_1, col_header_2 = st.columns([3, 1])
with col_header_1:
    if "1." in menu:
        st.title("수업 시뮬레이션 및 리스크 예측")
    elif "2." in menu:
        st.title("교실 환경 진단 및 프로필")
    elif "3." in menu:
        st.title("실시간 수업 내비게이션")
    elif "4." in menu:
        st.title("교수활동 프로파일 및 포트폴리오")
    elif "5." in menu:
        st.title("시스템 활용 가이드")

with col_header_2:
    st.success("✅ 시스템 정상 작동 중")

st.markdown("---")

# 1. 수업 계획 (AiTOM)
if "1." in menu:
    with st.container():
        st.subheader("📖 수업 시나리오 입력")
        scenario = st.text_area(
            "수업 계획을 입력하세요",
            value="이번 STEM 수업에서 학생들이 생성형 AI(ChatGPT)를 활용하여 파이썬 코드를 직접 짜고 미니 자율주행차를 제어하도록 하겠다.",
            height=150
        )
        
        if st.button("▶️ 시뮬레이션 및 리스크 예측", type="primary"):
            with st.spinner('베이지안 확률 계산 중...'):
                time.sleep(1.5)
            
            st.divider()
            
            col_risk, col_prescription = st.columns(2)
            
            with col_risk:
                st.error("⚠️ 주의 경보: AI 의존도 과다")
                st.markdown("""
                ### 🚨 오개념 발생 확률: **45%**
                
                **원인 분석:**
                - 코딩 초보 학습자가 생성형 AI의 코드를 맹목적으로 수용할 가능성이 높습니다.
                - 할루시네이션(환각)으로 인한 치명적 오류를 스스로 식별하기 어렵습니다.
                """)
                
            with col_prescription:
                st.success("💊 AiTOM 처방: 개입 전략 변경")
                st.markdown("""
                ### 📈 예상 수업 성공 확률: **92%**
                
                **처방 내용:**
                > 수업 중반에 **'교사의 크로스 체크(Cross-check)'** 단계를 반드시 추가하세요.
                > 학생이 AI에게 코드를 받기 전, 프롬프트를 교사에게 먼저 검사받는 능동적 개입 모드를 권장합니다.
                """)

# 2. 교실 진단 (C-AiTOM)
elif "2." in menu:
    col_main, col_desc = st.columns([1, 2])
    
    with col_main:
        st.image("https://via.placeholder.com/300x300.png?text=C2+Cluster", caption="Cluster C2: 균형 잡힌 AI 활용형")
        
    with col_desc:
        st.info("✅ 진단 완료")
        st.markdown("""
        ### 선생님의 교실은 <span class='highlight'>[C2: 균형 잡힌 AI 활용형]</span> 입니다.
        
        학생들의 기본적인 디지털 리터러시가 갖춰져 있으며, 교사의 AI 활용 능력도 우수한 편입니다.
        이 군집(Cluster)에서는 **'교사 주도 후 AI 검증'** 방식의 협업이 수업 질을 최고 수준(80% 이상)으로 보장하는 것으로 분석되었습니다.
        """, unsafe_allow_html=True)
        
    st.divider()
    
    m1, m2, m3 = st.columns(3)
    m1.metric(label="교사 AI 역량", value="우수", delta="상위 22%")
    m2.metric(label="교실 디지털 환경", value="보통", delta="1인 1기기 80%", delta_color="off")
    m3.metric(label="학생 AI 친숙도", value="높음", delta="90% 경험")

# 3. 실시간 내비 (P-AiTOM)
elif "3." in menu:
    # 세션 상태 초기화
    if 'class_status' not in st.session_state:
        st.session_state.class_status = 'normal'

    # 상단 대시보드
    st.markdown("""
    <div style='background-color:#1e293b; color:white; padding:15px; border-radius:10px; margin-bottom:20px; display:flex; justify-content:space-between; align-items:center;'>
        <div style='display:flex; align-items:center; gap:10px;'>
            <div style='width:12px; height:12px; background-color:#ef4444; border-radius:50%;'></div>
            <strong>Live Class: STEM 코딩 실습</strong>
        </div>
        <div style='font-size:0.9em;'>
            🕒 진행: 25분 | 👤 학생: 24명
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_control, col_display = st.columns([1, 2])

    with col_control:
        st.subheader("👁️ 현장 상황 입력")
        st.caption("수업 중 특이사항 발생 시 클릭하세요.")
        
        if st.button("⚠️ 학생 집중력/동기 저하"):
            st.session_state.class_status = 'warning'
        if st.button("🛡️ AI 답변 오류/할루시네이션"):
            st.session_state.class_status = 'action'
        if st.button("✅ 목표 달성 순항 중"):
            st.session_state.class_status = 'normal'

    with col_display:
        st.subheader("🧭 P-AiTOM 실시간 내비게이션")
        
        status = st.session_state.class_status
        
        if status == 'normal':
            st.success("현재 최적의 상태를 유지하고 있습니다.")
            st.info("💡 지금처럼 AI 주도 학습 모드를 유지하며 순회 지도 하세요.")
        elif status == 'warning':
            st.warning("부분적 개입이 필요한 시점입니다.")
            st.markdown("""
            **권장 조치:**
            학생들의 집중력이 저하되었습니다. AI 활용을 잠시 멈추고,
            **5분간 교사가 주도하여 지금까지의 핵심 개념을 요약**하는 스캐폴딩(Scaffolding)을 제공하세요.
            """)
        elif status == 'action':
            st.error("즉각 대응 필요 (DBN 예측)")
            st.markdown("""
            ### 🚨 현재 AI의 답변 정확도가 떨어지고 있습니다!
            
            👉 **즉시 '적극적 개입 모드'로 전환하세요.**
            AI 사용을 중지시키고 교사가 직접 칠판이나 화면을 통해 올바른 코딩 구조와 개념을 설명해야 합니다.
            """)

        # Matplotlib 그래프 그리기
        st.markdown("##### 📊 DBN 실시간 확률 궤적 및 예측")
        
        fig, ax = plt.subplots(figsize=(10, 4))
        
        # 데이터 생성
        x_past = np.linspace(0, 50, 50)
        
        if status == 'normal':
            y_past = 60 - 0.5 * x_past + np.random.normal(0, 2, 50) # 완만한 하락
            x_future = np.linspace(50, 100, 50)
            y_future_good = np.linspace(y_past[-1], 90, 50) # 상승
        elif status == 'warning':
            y_past = 60 - 0.8 * x_past + np.random.normal(0, 2, 50) # 좀 더 빠른 하락
            x_future = np.linspace(50, 100, 50)
            y_future_good = np.linspace(y_past[-1], 85, 50) # 회복
            y_future_bad = np.linspace(y_past[-1], 30, 50)  # 추락
        else: # action
            y_past = 60 - 1.2 * x_past + np.random.normal(0, 2, 50) # 급격한 하락
            x_future = np.linspace(50, 100, 50)
            y_future_good = np.linspace(y_past[-1], 80, 50) # 급격한 회복
            y_future_bad = np.linspace(y_past[-1], 5, 50)   # 완전 실패

        # 그래프 스타일링
        ax.plot(x_past, y_past, label='현재까지 궤적', color='#4f46e5', linewidth=2)
        ax.axvline(x=50, color='gray', linestyle='--', label='현재 시점 (t)')
        
        if status == 'normal':
             ax.plot(x_future, y_future_good, label='예측 경로', color='#10b981', linestyle='--')
        else:
             ax.plot(x_future, y_future_good, label='조치 시 (권장)', color='#10b981', linestyle='--')
             ax.plot(x_future, y_future_bad, label='유지 시 (위험)', color='#f87171', linestyle='--')

        ax.set_ylim(0, 100)
        ax.set_xlim(0, 100)
        ax.set_ylabel("수업 성공 확률 (%)")
        ax.set_xlabel("수업 시간")
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # 테두리 제거 등 깔끔하게
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        st.pyplot(fig)

# 4. 교수활동 프로파일
elif "4." in menu:
    st.balloons()
    st.info("🎉 김STEM 선생님, 훌륭한 수업이었습니다! (C2 → C3 성장 중)")
    
    col_chart, col_feed = st.columns(2)
    
    with col_chart:
        st.subheader("📉 수업 시간 흐름에 따른 질 변화")
        
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        x = np.linspace(0, 10, 100)
        y = np.sin(x) * 20 + 60 + np.random.normal(0, 5, 100)
        y = np.clip(y, 0, 100)
        
        ax2.plot(x, y, color='#6366f1', linewidth=2)
        ax2.fill_between(x, y, alpha=0.2, color='#6366f1')
        ax2.set_ylim(0, 100)
        ax2.set_title("수업 몰입도 변화 그래프")
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        
        st.pyplot(fig2)
        
    with col_feed:
        st.subheader("📈 P-AiTOM 성장 제안")
        with st.expander("상세 분석 결과 보기", expanded=True):
            st.write("""
            최근 5번의 수업에서 선생님의 AI 도구 활용 중재 능력이 크게 향상되었습니다.
            모델 분석 결과, 현재 **[C3: 고숙련 협업 전문가]** 군집으로 이동하고 있습니다.
            """)
            st.markdown("---")
            st.markdown("**다음 수업을 위한 추천:**")
            st.markdown("- ✅ 교사 주도 검증 비율을 20% 줄여보세요.")
            st.markdown("- ✅ 학생들에게 AI 프롬프트 작성 자율성을 부여해도 좋습니다.")

# 5. 시스템 활용 가이드
elif "5." in menu:
    st.subheader("ℹ️ AT-Navi 시스템 활용 가이드")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("#### 📖 1. 수업 계획 (AiTOM)")
            st.caption("수업 시나리오를 입력하고 시뮬레이션하세요.")
            st.write("AI 의존도로 인한 오개념 발생 리스크를 예측하고, 최적의 개입 전략을 처방받습니다.")
            
        with st.container(border=True):
            st.markdown("#### 🧭 3. 실시간 내비 (P-AiTOM)")
            st.caption("수업 중 발생하는 상황에 실시간으로 대응하세요.")
            st.write("DBN 기반 확률 궤적을 통해 교사가 취해야 할 즉각적인 조치를 안내받습니다.")
            
    with col2:
        with st.container(border=True):
            st.markdown("#### ⚙️ 2. 교실 진단 (C-AiTOM)")
            st.caption("교실 환경과 역량을 진단받으세요.")
            st.write("선생님과 학생의 역량을 분석하여 가장 적합한 AI 협업 군집(Cluster)을 배정합니다.")
            
        with st.container(border=True):
            st.markdown("#### 📊 4. 교수활동 프로파일")
            st.caption("데이터 기반으로 성장하세요.")
            st.write("누적된 수업 데이터를 분석하여 선생님의 성장을 시각화하고 다음 단계를 제안합니다.")
