import streamlit as st
import streamlit as st

st.title("こんばんは")

option = st.selectbox(
    '今の気分を選択してね',
    ['元気いっぱい', 'ちょっと疲れた', 'さっぱりしたい', 'こってりしたい', '落ち込んでいる']
)

st.write("あなたの今の気分は：", option)

# 気分に合わせた料理とレシピURL
recipes = {
    "元気いっぱい": ("スタミナ焼肉丼", "https://tenhoo.jp/menu/"),
    "ちょっと疲れた": ("とろろご飯", "http://www.konshinya.com/"),
    "さっぱりしたい": ("冷やしうどん", "https://www.yamaokaya.com/"),
    "こってりしたい": ("カルボナーラ", "https://www.costco.co.jp/"),
    "落ち込んでいる": ("あったか味噌汁", "https://www.nintendo.com/jp/index.html?srsltid=AfmBOorQLQ0LQj60hVZQuzS0A9GY7cB4zprMU6dZTmahE3EYcklkkZV63")
}

# 選択された料理を取得
food, url = recipes[option]

st.subheader(f"おすすめ料理：{food}")

# Markdownでリンク表示
st.markdown(f"[レシピを見る]({url})")

