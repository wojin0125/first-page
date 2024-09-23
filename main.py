import streamlit as st

# 타이틀 적용 예시
st.title('서민재를 소개합니다.')

# 특수 이모티콘 삽입 예시
#emoji: httpsL://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title('스마일 :sunglasses')

#Header 적용
st.header('헤더는 섹션의 제목 :sparkles:')

#Subheader 적용
st.subheader('subheader는 섹션의 부제목')

#캡션 적용
st.caption('캡션은 짧은 설명을 추가하는 것!')

#코드 표시
sample_code = '''
def function():
    print('hello, world')
'''
st.code(sample_code, language="python")

#일반 텍스트
st.text('일반적인 텍스트를 입력해 보았습니다.')
