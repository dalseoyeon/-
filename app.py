import streamlit as st
import random

st.set_page_config(page_title="오늘의 노래 추천", page_icon="🎵")

st.title("🎵 오늘의 노래 추천")
st.write("2010~2020 인기 노래 중 랜덤 추천 ✨")

songs = [

    # 아이유
    {"title":"좋은날","artist":"아이유","year":"2010"},
    {"title":"밤편지","artist":"아이유","year":"2017"},
    {"title":"에잇","artist":"아이유","year":"2020"},
    {"title":"Blueming","artist":"아이유","year":"2019"},

    # BTS
    {"title":"Dynamite","artist":"BTS","year":"2020"},
    {"title":"봄날","artist":"BTS","year":"2017"},
    {"title":"DNA","artist":"BTS","year":"2017"},
    {"title":"작은 것들을 위한 시","artist":"BTS","year":"2019"},

    # EXO
    {"title":"으르렁","artist":"EXO","year":"2013"},
    {"title":"LOVE SHOT","artist":"EXO","year":"2018"},
    {"title":"CALL ME BABY","artist":"EXO","year":"2015"},
    {"title":"Ko Ko Bop","artist":"EXO","year":"2017"},

    # BLACKPINK
    {"title":"뚜두뚜두","artist":"BLACKPINK","year":"2018"},
    {"title":"Kill This Love","artist":"BLACKPINK","year":"2019"},
    {"title":"붐바야","artist":"BLACKPINK","year":"2016"},
    {"title":"How You Like That","artist":"BLACKPINK","year":"2020"},

    # TWICE
    {"title":"CHEER UP","artist":"TWICE","year":"2016"},
    {"title":"TT","artist":"TWICE","year":"2016"},
    {"title":"FANCY","artist":"TWICE","year":"2019"},
    {"title":"LIKEY","artist":"TWICE","year":"2017"},

    # Red Velvet
    {"title":"빨간 맛","artist":"Red Velvet","year":"2017"},
    {"title":"Psycho","artist":"Red Velvet","year":"2019"},
    {"title":"러시안 룰렛","artist":"Red Velvet","year":"2016"},
    {"title":"Bad Boy","artist":"Red Velvet","year":"2018"},

    # AKMU
    {"title":"200%","artist":"악뮤","year":"2014"},
    {"title":"DINOSAUR","artist":"악뮤","year":"2017"},
    {"title":"어떻게 이별까지 사랑하겠어","artist":"악뮤","year":"2019"},
    {"title":"Give Love","artist":"악뮤","year":"2014"},

    # 태연
    {"title":"I","artist":"태연","year":"2015"},
    {"title":"사계","artist":"태연","year":"2019"},
    {"title":"Rain","artist":"태연","year":"2016"},
    {"title":"Why","artist":"태연","year":"2016"},

    # 볼빨간사춘기
    {"title":"우주를 줄게","artist":"볼빨간사춘기","year":"2016"},
    {"title":"썸 탈꺼야","artist":"볼빨간사춘기","year":"2017"},
    {"title":"나만 안되는 연애","artist":"볼빨간사춘기","year":"2016"},
    {"title":"여행","artist":"볼빨간사춘기","year":"2018"},

    # 버스커버스커
    {"title":"벚꽃 엔딩","artist":"버스커버스커","year":"2012"},
    {"title":"여수 밤바다","artist":"버스커버스커","year":"2012"},
    {"title":"처음엔 사랑이란게","artist":"버스커버스커","year":"2012"},

    # 태양
    {"title":"눈, 코, 입","artist":"태양","year":"2014"},
    {"title":"링가링가","artist":"태양","year":"2013"},
    {"title":"WAKE ME UP","artist":"태양","year":"2017"},

    # WINNER
    {"title":"REALLY REALLY","artist":"WINNER","year":"2017"},
    {"title":"LOVE ME LOVE ME","artist":"WINNER","year":"2017"},
    {"title":"AH YEAH","artist":"WINNER","year":"2019"},

    # iKON
    {"title":"사랑을 했다","artist":"iKON","year":"2018"},
    {"title":"취향저격","artist":"iKON","year":"2015"},
    {"title":"죽겠다","artist":"iKON","year":"2018"},

    # 헤이즈
    {"title":"비도 오고 그래서","artist":"헤이즈","year":"2017"},
    {"title":"널 너무 모르고","artist":"헤이즈","year":"2018"},
    {"title":"We don't talk together","artist":"헤이즈","year":"2019"},

    # 폴킴
    {"title":"모든 날 모든 순간","artist":"폴킴","year":"2018"},
    {"title":"너를 만나","artist":"폴킴","year":"2018"},
    {"title":"비","artist":"폴킴","year":"2016"},

    # 마마무
    {"title":"HIP","artist":"마마무","year":"2019"},
    {"title":"넌 is 뭔들","artist":"마마무","year":"2016"},
    {"title":"별이 빛나는 밤","artist":"마마무","year":"2018"},

    # 청하
    {"title":"벌써 12시","artist":"청하","year":"2019"},
    {"title":"롤러코스터","artist":"청하","year":"2018"},
    {"title":"Snapping","artist":"청하","year":"2019"},

    # 여자친구
    {"title":"시간을 달려서","artist":"여자친구","year":"2016"},
    {"title":"오늘부터 우리는","artist":"여자친구","year":"2015"},
    {"title":"밤","artist":"여자친구","year":"2018"},

    # 세븐틴
    {"title":"아주 NICE","artist":"세븐틴","year":"2016"},
    {"title":"예쁘다","artist":"세븐틴","year":"2016"},
    {"title":"독 : Fear","artist":"세븐틴","year":"2019"},

    # NCT
    {"title":"영웅","artist":"NCT 127","year":"2020"},
    {"title":"Cherry Bomb","artist":"NCT 127","year":"2017"},
    {"title":"BOSS","artist":"NCT U","year":"2018"},

    # 기타 인기곡
    {"title":"한숨","artist":"이하이","year":"2016"},
    {"title":"LOVE DAY","artist":"양요섭, 정은지","year":"2012"},
    {"title":"좋니","artist":"윤종신","year":"2017"},
    {"title":"가을 타나 봐","artist":"바이브","year":"2018"},
    {"title":"취중고백","artist":"김민석","year":"2020"},
    {"title":"Way Back Home","artist":"숀","year":"2018"},
    {"title":"METEOR","artist":"창모","year":"2019"},
    {"title":"아무노래","artist":"지코","year":"2020"},
    {"title":"에라 모르겠다","artist":"BIGBANG","year":"2016"},
    {"title":"Palette","artist":"아이유","year":"2017"},
    {"title":"SOLO","artist":"제니","year":"2018"},
    {"title":"첫눈처럼 너에게 가겠다","artist":"에일리","year":"2017"},
    {"title":"Stay With Me","artist":"찬열, 펀치","year":"2016"},
    {"title":"고백","artist":"멜로망스","year":"2017"},
    {"title":"선물","artist":"멜로망스","year":"2017"},
    {"title":"흔들리는 꽃들 속에서","artist":"장범준","year":"2019"},
    {"title":"주지마","artist":"로꼬, 화사","year":"2018"},
    {"title":"TOMBOY","artist":"혁오","year":"2017"},
    {"title":"오래된 노래","artist":"스탠딩에그","year":"2012"},
    {"title":"Atlantis Princess","artist":"보아","year":"2020 리메이크"},
]

if st.button("🎧 오늘의 노래 추천받기"):

    song = random.choice(songs)

    st.subheader(f"🎶 {song['title']}")
    st.write(f"👤 가수: {song['artist']}")
    st.write(f"📅 발매년도: {song['year']}")

    st.success("오늘 이 노래 한번 들어보세요 😊")
