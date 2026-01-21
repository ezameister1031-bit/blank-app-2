import streamlit as st

# =====================
# session_state 初期化（最重要）
# =====================
if "enemy_hp" not in st.session_state:
    st.session_state.enemy_hp = 3

if "life" not in st.session_state:
    st.session_state.life = 3

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "message" not in st.session_state:
    st.session_state.message = ""

if "wrong_questions" not in st.session_state:
    st.session_state.wrong_questions = []

if "mode" not in st.session_state:
    st.session_state.mode = "game"   # game / review


# =====================
# クイズデータ
# =====================
quiz = [
    {
        "question": "x = 5\nif x > 3:\n    print(?)",
        "choices": ["x", "True", "5"],
        "answer": "5"
    },
    {
        "question": "for i in range(3):\n    print(i)\n最後に出力される値は？",
        "choices": ["1", "2", "3"],
        "answer": "2"
    },
    {
        "question": "if x == 10:\n    print('OK')\nこれは何の処理？",
        "choices": ["条件分岐", "繰り返し", "代入"],
        "answer": "条件分岐"
    }
]

# =====================
# タイトル
# =====================
st.title("⚔️ Python Quiz RPG")

# =====================
# モード切り替え
# =====================
col_a, col_b = st.columns(2)

with col_a:
    if st.button("⚔️ バトルモード"):
        st.session_state.mode = "game"

with col_b:
    if st.button("📘 復習モード"):
        st.session_state.mode = "review"

st.divider()

# =====================
# 敵画像（中央配置）
# =====================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("fantasy_orc.png", width=250)

# =====================
# ステータス表示
# =====================
st.write("👾 敵HP")
st.progress(st.session_state.enemy_hp / 3)

st.write("❤️ ライフ:", "❤️" * st.session_state.life)

# =====================
# ゲーム終了判定（バトルモード）
# =====================
if st.session_state.mode == "game":
    if st.session_state.life <= 0:
        st.error("💀 ゲームオーバー")
        st.stop()

    if st.session_state.enemy_hp <= 0:
        st.success("🎉 敵を倒した！ゲームクリア！")
        st.stop()

# =====================
# 出題モードの決定
# =====================
if st.session_state.mode == "game":
    current_quiz = quiz
    st.subheader("⚔️ バトルクイズ")
else:
    current_quiz = st.session_state.wrong_questions
    st.subheader("📘 復習クイズ")

    if not current_quiz:
        st.info("復習する問題はありません")
        st.stop()

# =====================
# 問題表示
# =====================
q = current_quiz[st.session_state.q_index % len(current_quiz)]
st.code(q["question"], language="python")

# =====================
# 回答ボタン
# =====================
for choice in q["choices"]:
    if st.button(choice):
        if choice == q["answer"]:
            st.session_state.message = "⭕ 正解！"

            if st.session_state.mode == "game":
                st.session_state.enemy_hp -= 1
            else:
                if q in st.session_state.wrong_questions:
                    st.session_state.wrong_questions.remove(q)

        else:
            st.session_state.message = "❌ 不正解…"

            if st.session_state.mode == "game":
                st.session_state.life -= 1

            if q not in st.session_state.wrong_questions:
                st.session_state.wrong_questions.append(q)

        st.session_state.q_index += 1
        st.rerun()

# =====================
# メッセージ表示
# =====================
st.info(st.session_state.message)

# =====================
# 間違えた問題一覧
# =====================
st.divider()
st.subheader("📝 間違えた問題一覧")

if st.session_state.wrong_questions:
    for i, wq in enumerate(st.session_state.wrong_questions, 1):
        st.write(f"{i}. {wq['question']}")
        st.write(f"✅ 正解：{wq['answer']}")
        st.divider()
else:
    st.write("まだ間違えた問題はありません")
