import streamlit as st
import random

st.set_page_config(page_title="오늘의 운세", page_icon="🔮")

st.title("🔮 오늘의 운세")

# 생일 입력
birthday = st.text_input("생일 입력 (예: 1999-03-21)")

# 운세 데이터
fortunes = [
    "오늘은 좋은 소식이 들어올 수 있어요 😊",
    "새로운 인연이 생길 가능성이 있습니다 💘",
    "금전운이 좋은 하루입니다 💰",
    "오늘은 휴식을 우선하세요 🌿",
    "작은 기회가 큰 행운으로 이어질 수 있어요 ✨",
    "주변 사람과의 대화에서 힌트를 얻을 수 있습니다 🗣️",
    "자신감을 가지면 좋은 결과가 생겨요 🔥"
]

# 운세 보기 버튼
if st.button("운세 보기"):

    if birthday.strip() == "":
        st.warning("생일을 입력해주세요.")
    else:
        # 생일 기준 랜덤 고정
        random.seed(birthday)

        today_fortune = random.choice(fortunes)

        st.subheader("🌟 오늘의 운세")
        st.success(today_fortune)
