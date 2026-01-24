import streamlit as st
import random

# ----------------------------
# 初期化
# ----------------------------
def init_state():
    defaults = {
        "mode": "game",
        "stage": 1,
        "enemy_hp": 5,
        "life": 3,
        "wrong_questions": [],
        "current_question": None,
        "result_message": "",
        "result_type": "",
        "answered": False,
        "next_stage": 2,

    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ----------------------------
# クイズデータ
# ----------------------------
stage1_quiz = [
    {
        "q": "x = 5\nif x > 3:\n    print(x)",
        "choices": ["3", "5", "True", "x"],
        "answer": "5",
        "explanation": "xは5なのでprint(x)で5が出力される"
    },
    {
        "q": "for i in range(3):\n    print(i)\n最後に出力される数は？",
        "choices": ["0", "1", "2", "3"],
        "answer": "2",
        "explanation": "range(3)は0,1,2"
    },
    {
        "q": "x = 10\nif x == 10:\n    print('OK')",
        "choices": ["OK", "10", "True", "エラー"],
        "answer": "OK",
        "explanation": "条件がTrueなのでOKが表示される"
    },
]

stage2_quiz = [
    {
        "q": "nums = [1,2,3]\nprint(len(nums))",
        "choices": ["2", "3", "4", "エラー"],
        "answer": "3",
        "explanation": "リストの要素数は3"
    },
    {
        "q": "for i in range(1,6,2):\n    print(i)\n出力されない数は？",
        "choices": ["1", "3", "5", "2"],
        "answer": "2",
        "explanation": "range(1,6,2)は1,3,5"
    },
    {
        "q": "x = 3\nif x != 5:\n    print('A')",
        "choices": ["A", "5", "False", "何も出ない"],
        "answer": "A",
        "explanation": "xは5ではないので条件成立"
    },
]

quiz_data = stage1_quiz if st.session_state.stage == 1 else stage2_quiz

# ----------------------------
# ゲームクリア画面
# ----------------------------
# ----------------------------
# ステージクリア画面
# ----------------------------
if st.session_state.mode == "stage_clear":
    st.title("🎉 Stage1 クリア！")
    st.success("おめでとうございます！Stage1を突破しました！")

    st.write("次はさらに難しい問題が待っています…🔥")

    if st.button("➡ Stage2へ進む"):
        st.session_state.stage = st.session_state.next_stage
        st.session_state.enemy_hp = 7
        st.session_state.current_question = None
        st.session_state.result_message = ""
        st.session_state.result_type = ""
        st.session_state.answered = False
        st.session_state.mode = "game"
        st.rerun()

    st.stop()

if st.session_state.mode == "clear":
    st.title("🏆 ゲームクリア！")
    st.success("全ステージを制覇しました！")

    if st.session_state.wrong_questions:
        st.subheader("📘 復習（間違えた問題）")
        for w in st.session_state.wrong_questions:
            st.code(w["q"])
            st.write(f"✅ 正解：{w['answer']}")
            st.write(f"📝 解説：{w['explanation']}")
            st.divider()
    else:
        st.success("全問正解！すばらしい！")

    if st.button("🔄 もう一度遊ぶ"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    st.stop()

# ----------------------------
# ゲーム画面
# ----------------------------
st.title(f"🧙‍♂️ PythonクイズRPG（Stage {st.session_state.stage}）")

st.image("fantasy_orc.png", width=250)

st.write(f"👾 敵HP：{st.session_state.enemy_hp}")
st.write(f"❤️ ライフ：{st.session_state.life}")

# 問題をランダム取得
if st.session_state.current_question is None:
    st.session_state.current_question = random.choice(quiz_data)

q = st.session_state.current_question

st.subheader("❓ 問題")
st.code(q["q"])

choice = st.radio("選択肢", q["choices"], key="choice")

# ----------------------------
# 正解・不正解の表示
# ----------------------------
if st.session_state.result_message:
    if st.session_state.result_type == "correct":
        st.success(st.session_state.result_message)
    else:
        st.error(st.session_state.result_message)

# ----------------------------
# 回答ボタン
# ----------------------------
if st.button("回答する") and not st.session_state.answered:
    if choice == q["answer"]:
        st.session_state.result_message = "⭕ 正解！敵にダメージ！"
        st.session_state.result_type = "correct"
        st.session_state.enemy_hp -= 1
    else:
        st.session_state.result_message = "❌ 不正解… ライフが減った"
        st.session_state.result_type = "wrong"
        st.session_state.life -= 1
        st.session_state.wrong_questions.append(q)

    st.session_state.answered = True
    st.rerun()

# ----------------------------
# 次の問題へ
# ----------------------------
if st.session_state.answered:
    if st.button("➡ 次の問題へ"):
        st.session_state.current_question = None
        st.session_state.result_message = ""
        st.session_state.result_type = ""
        st.session_state.answered = False

        if st.session_state.life <= 0:
            st.session_state.mode = "clear"

        if st.session_state.enemy_hp <= 0:
            if st.session_state.stage == 1:
                st.session_state.mode = "stage_clear"
                st.session_state.next_stage = 2
            else:
                st.session_state.mode = "clear"

        st.rerun()
