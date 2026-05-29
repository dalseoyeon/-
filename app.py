import streamlit as st

st.set_page_config(page_title="MBTI 테스트", page_icon="🧠")

st.title("🧠 간단 MBTI 테스트")
st.write("20개의 질문에 답하고 내 MBTI를 확인해보세요!")

questions = [
    ("사람들과 함께 있으면 에너지가 생긴다", "E"),
    ("혼자 있는 시간이 더 편하다", "I"),
    ("새로운 사람 만나는 걸 좋아한다", "E"),
    ("생각할 시간을 충분히 가져야 한다", "I"),

    ("현실적인 것이 중요하다", "S"),
    ("상상과 아이디어를 좋아한다", "N"),
    ("경험을 더 믿는 편이다", "S"),
    ("미래 가능성을 자주 생각한다", "N"),

    ("논리적으로 판단하는 편이다", "T"),
    ("감정을 중요하게 생각한다", "F"),
    ("사실이 더 중요하다", "T"),
    ("사람 기분을 먼저 생각한다", "F"),

    ("계획적으로 움직인다", "J"),
    ("즉흥적인 편이다", "P"),
    ("미리 준비하는 걸 좋아한다", "J"),
    ("상황에 따라 유연하게 행동한다", "P"),

    ("활동적인 모임을 좋아한다", "E"),
    ("조용한 환경이 좋다", "I"),
    ("결정을 빠르게 내린다", "J"),
    ("선택 전에 오래 고민한다", "P"),
]

scores = {
    "E": 0,
    "I": 0,
    "S": 0,
    "N": 0,
    "T": 0,
    "F": 0,
    "J": 0,
    "P": 0,
}

answers = []

# 질문 출력
for i, (question, mbti_type) in enumerate(questions):

    answer = st.radio(
        f"{i+1}. {question}",
        ["예", "아니오"],
        key=i
    )

    answers.append((answer, mbti_type))

# 결과 버튼
if st.button("결과 보기"):

    for answer, mbti_type in answers:

        if answer == "예":
            scores[mbti_type] += 1

    result = ""

    result += "E" if scores["E"] >= scores["I"] else "I"
    result += "S" if scores["S"] >= scores["N"] else "N"
    result += "T" if scores["T"] >= scores["F"] else "F"
    result += "J" if scores["J"] >= scores["P"] else "P"

    st.subheader(f"🎉 당신의 MBTI는: {result}")

    # 간단 설명
    descriptions = {
        "INTJ": "전략적이고 독립적인 성향",
        "INFP": "감성적이고 이상주의적인 성향",
        "ENTP": "창의적이고 아이디어가 많은 성향",
        "ESFP": "사교적이고 밝은 성향",
    }

    st.write(descriptions.get(result, "당신만의 특별한 성향을 가진 타입입니다 😊"))
