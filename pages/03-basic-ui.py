import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

#버튼 클릭
button = st.button('버튼을 눌러보세요')
if button:
    st.write(':blue[버튼]이 눌렸습니다 :sparkles:')

# 파일 다운로드 버튼
# 샘플 데이터 생성
# Dataframe이란, pandas라이브러리에서 제공하는 2차원 데잍터 구조(엑셀과 유사)
dataframe = pd.DataFrame({
    'first column': ['korea','english','math','society','science','history'],
    'second column': [92, 97, 84, 95, 94, 98]
})

#다운로드 버튼 연결
st.download_button(
    label='서민재 성적표 다운로드',
    data=dataframe.to_csv(),      # dataframe을 csv 형태로 변환
    file_name='sample.csv',
    mime='text/csv'               #데이터 유형
)

agree = st.checkbox('동의 하십니까?')
if agree:
    st.write('동의 해주셔서 감사합니다 :100:')

mbti = st.radio(
    '당신이 가장 좋아하는 과목은 무엇입니까?',
    ('국어', '영어', '수학', '사회', '과학', '역사', '그 외'))
if mbti == '국어':
    st.write('당신은 :red[국어]을 잘하나보네요')
elif mbti == '영어':
    st.write('당신은 :red[영어]를 잘하나보네요')
elif mbti == '수학':
    st.write('당신은 :red[수학]을 잘하나보네요')
elif mbti == '사회':
    st.write('당신은 :red[사회]를 잘하나보네요')
elif mbti == '과학':
    st.write('당신은 :red[과학]을 잘하나보네요')
elif mbti == '역사':
    st.write('당신은 :red[역사]를 잘하나보네요')
else:
    st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")

title = st.text_input(
    label='가고싶은 대학교가 있나요?',
    placeholder='대학교를 입력해 주세요'
)
st.write(f'당신이 선택한 대학교: :violet[{title}]')

values = slider(
    '당신의 시험점수의 평균을 선택하세요 :sparkles:',
    0.0, 100.0, (25.0, 75.0))
st.write('선택 범위:', values)
