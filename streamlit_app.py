import streamlit as st

# =========================
# 初期化
# =========================
if "stage" not in st.session_state:
    st.session_state.stage = 1
    st.session_state.q_index = 0
    st.session_state.life = 3
    st.session_state.wrong_questions = []
    st.session_state.mode = "game"

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
    },
    {
        "question": "for i in range(3):\n    print(i)\nelse:\n    print('end')",
        "choices": ["2", "end", "何も出ない"],
        "answer": "end"
    },
    {
        "question": "x = [i for i in range(5) if i % 2 == 0]\nprint(x)",
        "choices": ["[1,3,5]", "[0,2,4]", "[2,4,6]"],
        "answer": "[0,2,4]"
    },
    {
        "question": "x = {'a':1}\nx['b']=2\nprint(len(x))",
        "choices": ["1", "2", "エラー"],
        "answer": "2"
    }
]

quiz_stage2 = [
    {
        "question": "class A:\n    def __init__(self, x):\n        self.x = x\n\na = A(5)\nprint(a.x)",
        "choices": ["5", "x", "エラー"],
        "answer": "5"
    },
    {
        "question": "x = [1,2,3]\ny = list(map(lambda n: n*2, x))\nprint(y)",
        "choices": ["[1,2,3]", "[2,4,6]", "エラー"],
        "answer": "[2,4,6]"
    },
    {
        "question": "def f(x):\n    try:\n        return 10/x\n    except ZeroDivisionError:\n        return 'error'\nprint(f(0))",
        "choices": ["0", "error", "例外"],
        "answer": "error"
    },
    {
        "question": "x = [1,2,3]\nprint(list(enumerate(x)))",
        "choices": [
            "[(1,1),(2,2),(3,3)]",
            "[(0,1),(1,2),(2,3)]",
            "エラー"
        ],
        "answer": "[(0,1),(1,2),(2,3)]"
    },
    {
        "question": "def f(x):\n    return lambda y: x + y\nadd5 = f(5)\nprint(add5(3))",
        "choices": ["8", "5", "3"],
        "answer": "8"
    }
]

quiz = quiz_stage1 if st.session_state.stage == 1 else quiz_stage2

# =========================
# UI
# =========================
st.title("🧙 PythonクイズRPG")
st.subheader(f"Stage {st.session_state.stage}")

# ライフ表示
st.write("❤️ ライフ：" + "❤️" * st.session_state.life)

# 敵画像（中央）
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.image("fantasy_orc.png", width=250)

# =========================
# ゲーム処理
# =========================
if st.session_state.mode == "game":

    if st.session_state.q_index >= len(quiz):
        if st.session_state.stage == 1:
            st.success("🎉 Stage 1 クリア！ Stage 2へ進みます")
            st.session_state.stage = 2
            st.session_state.q_index = 0
            st.rerun()
        else:
            st.balloons()
            st.success("🏆 全ステージクリア！")
            st.session_state.mode = "review"
            st.rerun()

    q = quiz[st.session_state.q_index]
    st.code(q["question"], language="python")

    choice = st.radio("答えを選択", q["choices"], key=st.session_state.q_index)

    if st.button("決定"):
        if choice == q["answer"]:
            st.success("正解！⚔️ 敵にダメージ！")
        else:
            st.error("不正解…💥 ダメージ！")
            st.session_state.life -= 1
            st.session_state.wrong_questions.append(q)

        st.session_state.q_index += 1

        if st.session_state.life <= 0:
            st.error("💀 ゲームオーバー")
            st.session_state.mode = "review"

        st.rerun()

# =========================
# 復習モード
# =========================
if st.session_state.mode == "review":
    st.header("📘 復習モード")

    if not st.session_state.wrong_questions:
        st.write("間違えた問題はありません 🎉")
    else:
        for i, q in enumerate(st.session_state.wrong_questions, 1):
            st.markdown(f"### 問題 {i}")
            st.code(q["question"], language="python")
            st.write(f"✅ 正解：**{q['answer']}**")

    if st.button("最初からやり直す"):
        st.session_state.clear()
        st.rerun()
