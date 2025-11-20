import streamlit as st
import streamlit as st

st.title("今日の気分に合わせた料理紹介")

# 気分を選択
option = st.selectbox(
    '今の気分を選択してね',
    ['元気いっぱい', 'ちょっと疲れた', 'さっぱりしたい', 'こってりしたい', '落ち込んでいる']
)

# 気分ごとの料理データ（料理名、画像URL、レシピURL）
recipes = {
    "元気いっぱい": {
        "name": "スタミナ焼肉丼",
        "img": "https://cdn.pixabay.com/photo/2016/06/27/22/38/beef-bowl-1481611_1280.jpg",
        "url": "https://kurashiru.com/recipes/4edb9df3-8e2b-4acd-8a28-8fd0b35a262b"
    },
    "ちょっと疲れた": {
        "name": "とろろご飯",
        "img": "https://cdn.pixabay.com/photo/2015/02/25/17/54/japanese-food-649423_1280.jpg",
        "url": "https://www.kurashiru.com/recipes/0e7f63c6-ec62-4bfc-a9de-313d695f41c3"
    },
    "さっぱりしたい": {
        "name": "冷やしうどん",
        "img": "https://cdn.pixabay.com/photo/2017/07/16/22/23/udon-2518930_1280.jpg",
        "url": "https://www.kurashiru.com/recipes/3ee6bd61-08d1-4e8a-b5f3-e02db1e62ce0"
    },
    "こってりしたい": {
        "name": "カルボナーラ",
        "img": "https://cdn.pixabay.com/photo/2020/03/07/19/09/pasta-4914158_1280.jpg",
        "url": "https://www.kurashiru.com/recipes/9f8fc102-7cb8-4e33-96df-d1a3b70f79d6"
    },
    "落ち込んでいる": {
        "name": "あったか味噌汁",
        "img": "https://cdn.pixabay.com/photo/2016/03/05/22/40/miso-soup-1238617_1280.jpg",
        "url": "https://www.kurashiru.com/recipes/3c42ac12-8a33-4bd8-b0b1-cafcffc9e483"
    }
}

# 選ばれたデータ取得
data = recipes[option]

# 画面にその場で表示
st.subheader(f"おすすめ料理：{data['name']}")
st.image(data['img'], width=400)
st.markdown(f"[レシピを見る]({data['url']})", unsafe_allow_html=True)

