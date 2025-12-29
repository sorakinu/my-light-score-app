import streamlit as st
import random

# --- ページ設定 ---
st.set_page_config(page_title="光スコア診断", page_icon="✨")

# --- タイトル ---
st.title("✨ 光スコア診断アプリ")
st.write("今のあなたの状態を診断し、おまじないを届けます。")

# --- 入力フォーム ---
st.subheader("今の状態を教えてください")
# ここで数字を入力してもらうので、計算エラーが起きなくなります
stress = st.slider("心の余裕（1:余裕なし 〜 10:余裕あり）", 1, 10, 5)
sleep = st.slider("睡眠の質（1:眠い 〜 10:スッキリ）", 1, 10, 5)
exercise = st.slider("体の軽さ（1:重い 〜 10:軽い）", 1, 10, 5)

# --- 診断ボタン ---
if st.button("診断する"):
    # --- 計算ロジック ---
    total_score = stress + sleep + exercise
    display_score = round((total_score / 30) * 5, 2)

    # --- 結果表示 ---
    st.markdown("---")
    st.subheader("■ 診断結果")
    st.write(f"今日の光スコア：  **{display_score} / 5.0**")

    if display_score >= 4.0:
        msg = "素晴らしい！今のあなたは光り輝いています。そのままのあなたで進んでください。"
        st.balloons()
    elif display_score >= 2.5:
        msg = "まずまずの調子です。少しだけ自分のための時間を作ってみましょう。"
    else:
        # あなたが考えた4つのアドバイス
        advices = [
            "【おまじない】一番、深呼吸してリラックス。ゆっくり息を吐いてみて。",
            "【おまじない】二番、自分の好きな食べ物や音楽など、好きなものを何でもいいから身につけてみて！",
            "【おまじない】三番、魔法の言葉だよ。「大丈夫」。声に出してみて。",
            "【おまじない】四番、ふぅーっと一息ついて、空を見上げてごらん。"
        ]
        msg = random.choice(advices)

    st.info(f"**今のあなたへのメッセージ:** \n\n {msg}")


