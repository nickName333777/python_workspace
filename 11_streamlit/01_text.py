import streamlit as st

# 실행 시키기: streamlit run 파일명.py 
# (해당 파일 경로에서 실행해야함)
# 종료는 streamlit run 파일명.py실행시킨 터미널에서 ctrl + C

st.title("Hello Streamlit")

st.write("streamlit은 **markdown**을 지원합니다. :smile:")

st.markdown("`write`또는 `markdown` 메소드를 사용하세요." )

st.html("<h3> 심지어 HTML도 지원합니다. </h3>")


############### data element
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,228 원", delta="-12.00 원")
col2.metric(label="일본JPY(100엔)", value="958.63 원", delta="-7.44 원")
col3.metric(label="유럽연합EUR", value="1,335.82 원", delta="11.44 원")

############### 수식
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')