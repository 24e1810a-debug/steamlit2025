import streamlit as st
st.title("こんばんは")
option = st.selectbox('好きな数字を教えてください',list(['元気いっぱい','ちょっと疲れた','さっぱりしたい','こってりしたい',"落ち込んでい"]))
input("あなたが選択したのは,") + option + 'です'

