import streamlit as st
import streamlit as st

st.title("🍽️ 今日何食べる？ AI料理提案アプリ")

# ----------------------------
# ① ユーザー入力
# ----------------------------
st.subheader("1. 今日の気分")
mood = st.selectbox(
    "今の気分は？",
    ["元気いっぱい", "ちょっと疲れた", "さっぱりしたい", "こってりしたい", "落ち込んでいる"]
)

st.subheader("2. 外の気温")
temp = st.slider("今の外の気温は？（℃）", min_value=-5, max_value=40, value=20)

st.subheader("3. 今の時間帯")
time = st.radio("今は何時ごろ？", ["朝", "昼", "夜"])


# ----------------------------
# ② 料理を決めるロジック
# ----------------------------

def choose_food(mood, temp, time):
    # 気温によるタイプ分類
    if temp >= 28:
        temp_type = "hot"
    elif temp <= 10:
        temp_type = "cold"
    else:
        temp_type = "normal"

    # ロジックによる料理提案
    # --------------------------

    # 元気いっぱい
    if mood == "元気いっぱい":
        if time == "朝":
            return "エナジー卵かけご飯", "https://www.kurashiru.com/recipes/cd88c1e8-e123-4d08-8a96-32a8237c4df8"
        elif time == "昼":
            return "スタミナ焼肉丼", "https://www.kurashiru.com/recipes/4edb9df3-8e2b-4acd-8a28-8fd0b35a262b"
        else:  # 夜
            return "がっつり豚キムチ", "https://www.kurashiru.com/recipes/25da8c13-4e31-4eec-87f4-e489f813b812"

    # ちょっと疲れた
    if mood == "ちょっと疲れた":
        if temp_type == "hot":
            return "冷やしうどん", "https://www.kurashiru.com/recipes/3ee6bd61-08d1-4e8a-b5f3-e02db1e62ce0"
        else:
            return "とろろご飯", "https://www.kurashiru.com/recipes/0e7f63c6-ec62-4bfc-a9de-313d695f41c3"

    # さっぱりしたい
    if mood == "さっぱりしたい":
        if temp_type == "hot":
            return "冷やし中華", "https://www.kurashiru.com/recipes/aeb1d432-9554-4ecf-9da3-c4e91a3f432a"
        else:
            return "サラダチキンと野菜スープ", "https://www.kurashiru.com/recipes/67d9f60d-ae60-44bf-b29a-46fcd521463d"

    # こってりしたい
    if mood == "こってりしたい":
        if time == "夜":
            return "濃厚カルボナーラ", "https://www.kurashiru.com/recipes/9f8fc102-7cb8-4e33-96df-d1a3b70f79d6"
        else:
            return "から揚げ定食", "https://www.kurashiru.com/recipes/921d63c4-6ebf-4188-bdbd-f4d1e391fdfc"

    # 落ち込んでいる
    if mood == "落ち込んでいる":
        if temp_type == "cold":
            return "あったか味噌汁と焼きおにぎり", "https://www.kurashiru.com/recipes/3c42ac12-8a33-4bd8-b0b1-cafcffc9e483"
        else:
            return "優しいおかゆ", "https://www.kurashiru.com/recipes/341d0bc5-3096-45e7-a7c0-71bdd226e52c"


# ----------------------------
# ③ 提案結果を表示
# ----------------------------

food, url = choose_food(mood, temp, time)

st.subheader("🔽 あなたにおすすめの料理は…")
st.markdown(f"## **{food}** 🍴")
st.markdown(f"[レシピを詳しく見る]({url})")
