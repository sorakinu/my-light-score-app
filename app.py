import streamlit as st
import pandas as pd

# ===========================
# 光スコア計算関数
# ===========================
def calculate_light_score(stress, focus, calm, poem):
    # スコア計算ロジック
    # (focus + calm - stress) の範囲は -5 〜 10 になるため、3で割って正規化
    raw_score = ((focus + calm) - stress) / 3
    
    # スコアを1〜5に収める処理
    score = round(max(1, min(5, raw_score)), 2)

    # 詩に反応したアドバイス生成
    if len(poem.strip()) > 0:
        advice = "外に向けて一つ行動する日です。最初5分動いてみてください。"
    else:
        advice = "静けさが今日の味方です。ひとつだけ軽い行動を選んでみてください。"

    return score, advice

# ===========================
# Streamlit アプリ設定
# ===========================
st.set_page_config(page_title="光スコア診断アプリ", page_icon="✨", layout="centered")

# スタイル調整（見た目を少し整える）
st.markdown("""...
    """, unsafe_allow_html=True)

st.title("✨ 光スコア診断アプリ")
st.write("ストレス・集中・静けさ・詩から、今日の“光の度合い”を算出します。")

# 入力フォーム
st.subheader("■ 今日の状態を入力してください")

# スライダーを直感的に配置
col1, col2, col3 = st.columns(3)
with col1:
    stress = st.slider("ストレス", 0, 5, 2, help="0:なし 〜 5:非常に高い")
with col2:
    focus = st.slider("集中", 0, 5, 3, help="0:散漫 〜 5:没頭")
with col3:
    calm = st.slider("静けさ", 0, 5, 3, help="0:騒がしい 〜 5:穏やか")

poem = st.text_area("今日の詩、または感じた言葉（任意）", placeholder="今の心境を言葉にしてみましょう...")

# 計算実行
if st.button("✨ 光スコアを計算する", use_container_width=True):
    score, advice = calculate_light_score(stress, focus, calm, poem)

    st.divider()
    
    # 結果表示
    st.subheader("■ 診断結果")
    st.metric(label="今日の光スコア（1〜5）", value=f"{score} / 5.0")
    
    st.info(f"**メッセージ:** \n\n {advice}")

st.write("---")
st.caption("© 2024 Singularity Education")
