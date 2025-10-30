import streamlit as st
import pandas as pd

# 실행 시키기:
#   02_data.py 안에서 streamlit임포트해주고: import streamlit as st
#  (pystudy_env) C:\workspace\7_Python\11_streamlit>streamlit run 02_data.py 
# (해당 파일 경로에서 실행해야함)
# 종료는 streamlit run 파일명.py실행시킨 터미널에서 ctrl + C

st.title("Data")


st.header("pandas DataFrame")
# 정형데이터 (행/열) => 표형식
# - dict 전달 (컬럼명:컬럼값{})
student_df = pd.DataFrame({
    'Name' : ['홍길동', '신사임당', '이순신'],
    'Age': [34, 48, 21],
    'Score': [88, 90, 79]  
})

print(student_df.head()) # 터미널로 출력

st.dataframe(student_df)

sample_df = pd.read_csv('./data/annual-enterprise-survey-2023.csv')
print(sample_df.head(3))

st.dataframe(sample_df)