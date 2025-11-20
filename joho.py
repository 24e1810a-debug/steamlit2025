import streamlit as st
st.title("こんばんは")
option = st.selectbox('好きな数字を教えてください',list(['元気oっぱい','ちょっと疲れた','さっぱりしたい','こってりしたい',"落ち込んでい"]))
st.write(option)
