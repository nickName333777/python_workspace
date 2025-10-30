import streamlit as st
import os

st.title("Media")

st.header("Image")

st.write(f'{os.getcwd()}')

# 서버이미지
st.image("cute.jpg", caption="Sunrise by the mountains")

# 웹이미지
st.image('https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80')