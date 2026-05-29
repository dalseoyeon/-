import streamlit as st
import random

st.set_page_config(page_title="연애 코치", page_icon="💘")

st.title("💘 AI 연애 코치")

# 간단한 답변들
responses = [
    "조금 더 천천히 다가가보세요 😊",
    "상대방의 행동을 잘 관찰해보는 게 좋아요.",
    "너무 조급해하지 마세요.",
    "솔직한 대화가 가장 중요해요.",
    "지금은 기다리는 것도 방법일 수 있어요."
]

# 입력창
user_input = st.text_input("연애 고민을 입력하세요")

# 버튼 클릭
if st.button("상담받기"):

    if user_input.strip() == "":
        st.warning("고민을 입력해주세요.")
    else:
        answer = random.choice(responses)

        st.subheader("💡 AI 답변")
        st.write(answer)
