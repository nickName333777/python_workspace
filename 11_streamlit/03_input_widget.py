import streamlit as st

# 실행 시키기: streamlit run 파일명.py 
# (해당 파일 경로에서 실행해야함)
# 종료는 streamlit run 파일명.py실행시킨 터미널에서 ctrl + C


###### input과 관련된것들

st.title("Input Widget")

st.header('button')

#st.button('Click Me')

clicked = st.button('Click Me')
print(f'clicked = {clicked}')

if clicked:
    st.write("버튼을 클릭했습니다.")
else:
    st.write("버튼을 클릭해주세요!!!")
    
st.header('Text Input')
input = st.text_input(
    label='가고 싶은 여행지가 있나요??!!!!',
    placeholder='여행지를 입력하세요.'
)
print(f'input= {input}')

if input:
    st.write(f' :blue[{input}]에 가고 싶으시군요~')
    
st.header("Checkbox")
agree = st.checkbox("I agree")
print(f'agree = {agree}')

st.header("SelectBox")
mbti = st.selectbox(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ', 'ISFJ', 'INFJ', 'INTJ',
     'ISTP', 'ISFP', 'INFP', 'INTP',
     'ESTP', 'ESFP', 'ENFP', 'ENTP',
     'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ',
     '모름'),
    index=7
)

if mbti:
    st.write(f'선택한 MBTI는 :red[{mbti}]입니다')