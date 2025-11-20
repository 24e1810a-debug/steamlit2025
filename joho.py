
import streamlit as st
import google.generativeai as genai
import os

# --- Gemini API 認証 ---
genai.configure(api_key=os.getenv("AIzaSyBYjd3f0JhxlhfP3o08lpkYy6HMiveBtIo"))

model = genai.GenerativeModel("gemini-pro")

# --- Streamlit UI ---
st.title("🍽️ 今日何食べる？ AIレシピ提案アプリ")

# 選択肢
feeling = st.selectbox(
    "今の気分を選んでね",
    ["元気いっぱい", "ちょっと疲れた", "さっぱりしたい", "こってりしたい", "落ち込んでいる"]
)

temperature = st.slider("今の気温（°C）", min_value=-5, max_value=40, value=20)

time_zone = st.selectbox(
    "今の時間帯",
    ["朝", "昼", "夜", "深夜"]
)

# --- レシピ生成ボタン ---
if st.button("レシピを提案して！"):

    prompt = f"""
    ユーザーの条件に合わせて料理レシピを1つ提案してください。

    ▼ 条件
    ・気分: {feeling}
    ・気温: {temperature}℃
    ・時間帯: {time_zone}

    ▼ 書き方
    ・料理名
    ・おすすめポイント（なぜ今の条件に合うか）
    ・材料（箇条書き）
    ・作り方（簡潔に）
    ・一言アドバイス

    日本語で書いてください。
    """

    with st.spinner("AIがレシピを考えています…🍳"):
        response = model.generate_content(prompt)

    st.subheader("📖 今日のおすすめレシピ")
    st.write(response.text)

