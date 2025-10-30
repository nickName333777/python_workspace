import streamlit as st

st.title("Session State")

st.header("Counter")

count: int = 0 # 초기화

if st.button('버튼'):# 클릭 이벤트 발생하면, 초기화 시키고 다시 실행 
                    # => 따라서 count값이 증가하지 않는다.
                    # => 따라서, 웹서버안에 session state로 count변수값을 사용자별 관리가 필요
                    # => 여기세 count 넣어놓고, 기억된 count값을 계속사용
    count += 1
    print(count)
    
st.write(f'누른 횟수 : {count}')

st.header("Session State의 Counter")
# session_state : 서버 컴퓨터의 메모리 영역에 
#                 사용자별 객체 공간

if "count" not in st.session_state:
    st.session_state["count"] = 0
    print(f'session state[count]가 초기화 되었습니다.')
    
    
if st.button("Button") :
    st.session_state["count"] += 1 # count += 1 가 아니다..
    
st.write(f'누른 횟수 : {st.session_state["count"]}')


if st.button("Reset"):
    st.session_state["count"] = 0
    st.rerun()  # 값을 바꾸고 나서 최신 상태로 갱신 (화면(입력)값을 바꾸는 이벤트있을때(count값 변화)는 자동 실행되는데, 
                # 여기서 session값(session_state["count"])을 바꾸는 것처럼 화면에 있는(입력)값(count같은 화면에 있는값) 바꾸는게 아닐때는 자동 재실행 않되므로,
                # st.rerun()해서 강제 재실행 해주어야함)
                
