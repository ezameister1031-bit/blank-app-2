import streamlit as st

# -----------------------
# 初期設定
# -----------------------
if "enemy_hp" not in st.session_state:
    st.session_state.enemy_hp = 3
    st.session_state.life = 3
    st.session_state.q_index = 0
    st.session_state.message = ""

# クイズデータ
quiz = [
    {
        "question": "x = 5\nif x > 3:\n    print(?)",
        "choices": ["x", "True", "5"],
        "answer": "5"
    },
    {
        "question": "for i in range(3):\n    print(i)\n出力される最後の値は？",
        "choices": ["1", "2", "3"],
        "answer": "2"
    },
    {
        "question": "if x == 10:\n    print('OK')\nこれは何の処理？",
        "choices": ["繰り返し", "条件分岐", "代入"],
        "answer": "条件分岐"
    }
]

# -----------------------
# タイトル
# -----------------------
st.title("⚔️ Python Quiz RPG")

# -----------------------
# 敵表示
# -----------------------
st.image("fantasy_orc.png", width=250)
st.write("👾 敵HP")
st.progress(st.session_state.enemy_hp / 3)

# -----------------------
# ライフ表示
# -----------------------
st.write("❤️ ライフ:", "❤️" * st.session_state.life)

# -----------------------
# ゲーム終了判定
# -----------------------
if st.session_state.life == 0:
    st.error("ゲームオーバー...")
    st.stop()

if st.session_state.enemy_hp == 0:
    st.success("🎉 敵を倒した！クリア！")
    st.stop()

# -----------------------
# 問題表示
# -----------------------
q = quiz[st.session_state.q_index]

st.code(q["question"], language="python")

for choice in q["choices"]:
    if st.button(choice):
        if choice == q["answer"]:
            st.session_state.enemy_hp -= 1
            st.session_state.message = "⭕ 正解！敵にダメージ！"
        else:
            st.session_state.life -= 1
            st.session_state.message = "❌ 不正解…ライフが減った"

        st.session_state.q_index = (st.session_state.q_index + 1) % len(quiz)
        st.rerun()

# -----------------------
# メッセージ
# -----------------------
st.info(st.session_state.message)

