import streamlit as st
import random

# ----------------------------
# 初期化
# ----------------------------
if "mode" not in st.session_state:
    st.session_state.mode = "game"

if "stage" not in st.session_state:
    st.session_state.stage = 1

if "enemy_hp" not in st.session_state:
    st.session_state.enemy_hp = 5

if "life" not in st.session_state:
    st.session_state.life = 3

if "wrong_questions" not in st.session_state:
    st.session_state.wrong_questions = []

if "current_question" not in st.session_state:
    st.session_state.current_question = None

# ----------------------------
# クイズデータ
# ----------------------------
stage1_quiz = [
    {
        "q": "x = 5\nif x > 3:\n    print(?)",
        "choices": ["x", "5", "True", "3"],
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
        "choices": ["OK", "True", "10", "エラー"],
        "answer": "OK",
        "explanation": "条件がTrueなのでOKが出力される"
    }
]

stage2_quiz = [
    {
        "q": "nums = [1,2,3]\nprint(len(nums))",
        "choices": ["2", "3", "4", "エラー"],
        "answer": "3",
        "explanation": "要素は3つ"
    },
    {
        "q": "for i in range(1,5,2):\n    print(i)\n最初に出る数は？",
        "choices": ["0", "1", "2", "5"],
        "answer": "1",
        "explanation": "range(1,5,2)は1,3"
    },
    {
        "q": "x = 3\nif x != 5:\n    print('A')",
        "choices": ["A", "5", "False", "何も出ない"],
        "answer": "A",
        "explanation": "xは5ではないので条件成立"
    }
]

quiz_data = stage1_quiz if st.session_state.stage == 1 else stage2_quiz

# ----------------------------
# ゲームクリア画面
# ----------------------------
if st.session_state.mode == "clear":
    st.title("🏆 ゲームクリア！")
    st.success("全ステージを制覇しました！")

    if st.session_state.wrong_questions:
        st.subheader("📘 復習リスト（間違えた問題）")
        for w in st.session_state.wrong_questions:
            st.write("❓ 問題")
            st.code(w["q"])
            st.write(f"✅ 正解：{w['answer']}")
            st.write(f"📝 解説：{w['explanation']}")
            st.divider()
    else:
        st.success("全問正解！素晴らしい 🎉")

    if st.button("🔄 もう一度遊ぶ"):
        st.session_state.stage = 1
        st.session_state.enemy_hp = 5
        st.session_state.life = 3
        st.session_state.wrong_questions = []
        st.session_state.current_question = None
        st.session_state.mode = "game"
        st.rerun()

    st.stop()

# ----------------------------
# ゲーム画面
# ----------------------------
st.title(f"🧙‍♂️ PythonクイズRPG（Stage {st.session_state.stage}）")

st.image("fantasy_orc.png", width=250)

st.write(f"👾 敵HP：{st.session_state.enemy_hp}")
st.write(f"❤️ ライフ：{st.session_state.life}")

# 問題をランダムに取得
if st.session_state.current_question is None:
    st.session_state.current_question = random.choice(quiz_data)

q = st.session_state.current_question

st.subheader("❓ 問題")
st.code(q["q"])

choice = st.radio("選択肢", q["choices"], key="choice")

if st.button("回答する"):
    if choice == q["answer"]:
        st.session_state.result_message = "⭕ 正解！敵にダメージ！"
        st.session_state.result_type = "correct"
        st.session_state.enemy_hp -= 1
    else:
        st.session_state.result_message = "❌ 不正解… ライフが減った"
        st.session_state.result_type = "wrong"
        st.session_state.life -= 1
        st.session_state.wrong_questions.append(q)


    
    st.session_state.current_question = None


    # ライフチェック
    if st.session_state.life <= 0:
        st.session_state.mode = "clear"

    # 敵撃破チェック
    if st.session_state.enemy_hp <= 0:
        if st.session_state.stage == 1:
            st.success("👾 敵を倒した！Stage2へ！")
            st.session_state.stage = 2
            st.session_state.enemy_hp = 7
        else:
            st.session_state.mode = "clear"

    st.rerun()
