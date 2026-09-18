import streamlit as st
from ui_v2 import card, empty_state, hero


def render_dashboard():
    hero(
        "오늘도 성공적인 투자를 응원합니다!",
        "시장 흐름과 관심종목을 한눈에 확인하고, 기업 분석으로 이어지는 StockDash 홈입니다.",
        "STOCK DASHBOARD",
    )

    st.subheader("시장 스냅샷")
    cols = st.columns(4)
    for col, title, value, note in [
        (cols[0], "KOSPI", "데이터 연결 필요", "market.index"),
        (cols[1], "KOSDAQ", "데이터 연결 필요", "market.index"),
        (cols[2], "KOSPI200", "데이터 연결 필요", "market.index"),
        (cols[3], "원/달러", "데이터 연결 필요", "macro.fx"),
    ]:
        with col:
            card(title, value, "공식 API 연결 후 표시", note)

    left, right = st.columns([2.1, 1], gap="large")
    with left:
        with st.container(border=True):
            st.subheader("주요 종목 차트")
            st.caption("실제 가격 데이터가 연결되면 선택 종목의 가격·거래량 차트를 표시합니다.")
            empty_state("시세 데이터 연결 대기", "현재 저장소는 일별 공식 시세를 지원합니다. 연결된 종목을 선택하면 실제 데이터로 확장할 수 있습니다.")
    with right:
        with st.container(border=True):
            st.subheader("상승률 / 하락률")
            empty_state("시장 랭킹 API 대기", "상승률·하락률 상위 종목은 시장 랭킹 Capability 연결 후 표시합니다.")

    st.subheader("업종별 등락률")
    with st.container(border=True):
        empty_state("업종 데이터 연결 대기", "KRX 등 공식 시장 데이터 연결 후 업종별 상승·하락을 시각화합니다.")

    st.subheader("내 투자 현황")
    a, b, c = st.columns([1.25, 1, 1])
    with a:
        with st.container(border=True):
            st.subheader("보유 종목 현황")
            empty_state("계좌 연결 전", "한국투자증권 API를 연결하면 보유종목·평가액·수익률을 표시합니다.")
    with b:
        with st.container(border=True):
            st.subheader("포트폴리오 비중")
            empty_state("계좌 연결 전", "실제 보유 평가액을 기준으로 비중을 계산합니다.")
    with c:
        with st.container(border=True):
            st.subheader("오늘의 주요 뉴스")
            empty_state("뉴스 API 대기", "실시간 뉴스는 연결된 공식/신뢰 가능한 데이터 소스가 있을 때 표시합니다.")


render_dashboard()
