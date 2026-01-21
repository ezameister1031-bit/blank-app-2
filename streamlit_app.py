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
        st.session_state.m_
