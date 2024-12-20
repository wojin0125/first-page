import streamlit as st

# 타이틀 적용 예시
st.title('★학생회장 서민재 팬카페★')

# 특수 이모티콘 삽입 예시
#emoji: httpsL://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title('')

#Header 적용
st.header(':sparkles:동대문중 학생회장 서민재:sparkles:')

#Subheader 적용
st.subheader('09_minjae_seo')

#캡션 적용
st.caption('인스타 팔로우부탁해요')

#코드 표시
sample_code = '''
def function():
    print('hello, minjae')
'''
st.code(sample_code, language="python")

#일반 텍스트
st.text('문의는 DM으로 보탁드립니다')

# 마크다운 문법 지원
st.markdown('민재에게 **학교에대한 건의사항**을 보내주세요')
#컬러코드: blue, green, orange, red, violet
st.markdown("민재가 :green[DM을 확인] 하면 :blue[서민재]가 여러분의 의견을 반영하여 학교를 바꾸어드립니다.")
