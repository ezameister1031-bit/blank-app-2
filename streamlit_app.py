import streamlit as st

# =========================
# session_state 初期化
# =========================
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "life" not in st.session_state:
    st.session_state.life = 3
if "enemy_hp" not in st.session_state:
    st.session_state.enemy_hp = 5
if "mode" not in st.session_state:
    st.session_state.mode = "game"
if "wrong_questions" not in st.session_state:
    st.session_state.wrong_questions = []
if "message" not in st.session_state:
    st.session_state.message = ""

# =========================
# 問題データ
# =========================
quiz_stage1 = [
    {
        "question": "x = [1, 2, 3]\nprint(len(x))",
        "choices": ["2", "3", "エラー"],
        "answer": "3"
    },
    {
        "question": "x = [1,2,3]\nprint(x[-1])",
        "choices": ["1", "3", "エラー"],
        "answer": "3"
    }
]

quiz_stage2 = [
    {
        "question": "class A:\n    def __init__(self, x):\n        self.x = x\n\na = A(5)\nprint(a.x)",
        "choices": ["5", "x", "エラー"],
        "answer": "5"
    }
]

quiz = quiz_stage1 if st.session_state.stage == 1 else quiz_stage2

# =========================
# 復習画面
# =========================
if st.session_state.mode == "review":
    st.title("📘 復習ノート")

    if not st.session_state.wrong_questions:
        st.info("まだ間違えた問題はありません")
    else:
        for i, q in enumerate(st.session_state.wrong_questions, 1):
            st.markdown(f"### 問題 {i}")
            st.code(q["question"], language="python")
            st.write(f"✅ 正解：**{q['answer']}**")

    if st.button("⬅ ゲームに戻る"):
        st.session_state.mode = "game"
        st.rerun()

    st.stop()

# =========================
# ゲーム画面
# =========================
st.title("🧙 PythonクイズRPG")
st.subheader(f"Stage {st.session_state.stage}")

st.write("❤️ ライフ：" + "❤️" * st.session_state.life)
st.write(f"👾 敵HP：{st.session_state.enemy_hp}")

c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.image("fantasy_orc.png", width=250)

# 復習ボタン（常設）
if st.button("📘 復習する"):
    st.session_state.mode = "review"
    st.rerun()

# メッセージ表示
if st.session_state.message:
    st.info(st.session_state.message)
    st.session_state.message = ""

# =========================
# 問題表示
# =========================
q = quiz[st.session_state.q_index]
st.code(q["question"], language="python")
choice = st.radio("答えを選択", q["choices"], key=f"q{st.session_state.stage}_{st.session_state.q_index}")

if st.button("決定"):
    if choice == q["answer"]:
        st.session_state.enemy_hp -= 1
        st.session_state.message = "⚔️ 正解！敵にダメージ！"
    else:
        st.session_state.life -= 1
        st.session_state.message = "💥 不正解…"
        st.session_state.wrong_questions.append(q)

    st.session_state.q_index += 1

    if st.session_state.enemy_hp <= 0:
        if st.session_state.stage == 1:
            st.success("👾 敵を倒した！ Stage2へ！")
            st.session_state.stage = 2
            st.session_state.q_index = 0
            st.session_state.enemy_hp = 7
        else:
            st.success("🏆 全ステージクリア！")

    st.rerun()
