import streamlit as st
import streamlit as st
import streamlit.components.v1 as components

st.title("今日の気分に合わせた料理紹介")

option = st.selectbox(
    '今の気分を選択してね',
    ['元気いっぱい', 'ちょっと疲れた', 'さっぱりしたい', 'こってりしたい', '落ち込んでいる']
)

# 気分ごとの料理データ（料理名、レシピURL）
recipes = {
    "元気いっぱい": {
        "name": "スタミナ焼肉丼",
        "url": "https://tenhoo.jp/menu/%e3%82%bf%e3%83%b3%e3%82%bf%e3%83%b3%e3%83%a1%e3%83%b3/"
    },
    "ちょっと疲れた": {
        "name": "とろろご飯",
        "url": "https://www.kurashiru.com/recipes/0e7f63c6-ec62-4bfc-a9de-313d695f41c3"
    },
    "さっぱりしたい": {
        "name": "冷やしうどん",
        "url": "https://www.kurashiru.com/recipes/3ee6bd61-08d1-4e8a-b5f3-e02db1e62ce0"
    },
    "こってりしたい": {
        "name": "カルボナーラ",
        "url": "https://www.kurashiru.com/recipes/9f8fc102-7cb8-4e33-96df-d1a3b70f79d6"
    },
    "落ち込んでいる": {
        "name": "あったか味噌汁",
        "url": "https://www.kurashiru.com/recipes/3c42ac12-8a33-4bd8-b0b1-cafcffc9e483"
    }
}

# 選ばれたデータ取得
data = recipes[option]

# 料理名を表示
st.subheader(f"おすすめ料理：{data['name']}")

# Webページを埋め込む (iframe)
components.iframe(data["url"], height=800, scrolling=True)

