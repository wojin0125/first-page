import streamlit as st
import random
import datetime

st.title(':star: 일일 운세 및 조언 :star:')

# 운세 및 조언 목록
fortunes = [
    "오늘은 새로운 시작에 좋은 날입니다.",
    "작은 일에도 감사하는 마음을 가지세요.",
    "주변 사람들과의 소통이 중요합니다.",
    "미소를 잃지 마세요. 좋은 일이 생길 것입니다.",
    "오늘은 자신감을 가지고 도전하세요.",
    "주어진 기회를 놓치지 마세요.",
    "작은 변화가 큰 결과를 가져옵니다.",
    "휴식을 취하는 것도 중요합니다.",
]

# 버튼 클릭 시 운세 및 조언 생성
if st.button('운세 보기'):
    fortune = random.choice(fortunes)
    st.subheader('오늘의 운세:')
    st.write(fortune)
    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
