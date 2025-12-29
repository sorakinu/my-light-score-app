# ✨ 光スコア診断アプリ (Light Score Diagnostic)

今の心の状態を「光」として数値化し、今日を過ごすための小さなヒントを提案するメンタルセルフケア・アプリです。

## 🌟 概要
ストレス、集中力、静けさの3つの指標と、今の気持ち（詩・言葉）を組み合わせ、独自のアルゴリズムで「光スコア」を算出します。

## 🚀 使い方
1. スライダーで現在の「ストレス」「集中」「静けさ」を選択します。
2. 今感じている言葉や詩をテキストエリアに入力します（任意）。
3. 「光スコアを計算する」ボタンを押すと、診断結果とメッセージが表示されます。

## 🛠️ 技術スタック
- Python 3.x
- Streamlit (UI Framework)
- Pandas (Data Processing)

## 📦 インストールと実行
ローカル環境で実行する場合：
```bash
git clone [https://github.com/あなたのユーザー名/light-score-app.git](https://github.com/あなたのユーザー名/light-score-app.git)
cd light-score-app
pip install -r requirements.txt
streamlit run app.py
