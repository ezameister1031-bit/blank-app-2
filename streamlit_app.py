import streamlit as st
import random
from quiz_data import stage1_quiz,stage2_quiz
# ----------------------------
# 初期化
# ----------------------------
from supabase import create_client
from openai import OpenAI


SUPABASE_URL = "https://uidimomhqldplhtvbchz.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVpZGltb21ocWxkcGxodHZiY2h6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjkwMjAyOTksImV4cCI6MjA4NDU5NjI5OX0.mzoug_p5WpFFQTUq-TTsffA8n7uRI77IqdZpAR5pTYg"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "ai_hint" not in st.session_state:
    st.session_state.ai_hint = None

if "hint_requested" not in st.session_state:
    st.session_state.hint_requested = False
    
if "hint_used" not in st.session_state:
    st.session_state.hint_used = False

if "current_question_id" not in st.session_state:
    st.session_state.current_question_id = None

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
        "bgm_on": True,
        "ai_hint": None,
        "hint_requested": False,

    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()
#モード選択（左側に表示）
st.sidebar.title("📚 メニュー")

if st.sidebar.button("🎮 ゲームに戻る"):
    st.session_state.mode = "game"
    st.rerun()

if st.sidebar.button("📖 復習モード"):
    st.session_state.mode = "review"
    st.rerun()


def save_wrong_answer(q):
    res = supabase.table("wrong_answers") \
        .select("*") \
        .eq("question_id", q["id"]) \
        .execute()

    if res.data:
        supabase.table("wrong_answers") \
            .update({
                "wrong_count": res.data[0]["wrong_count"] + 1
            }) \
            .eq("question_id", q["id"]) \
            .execute()
    else:
        supabase.table("wrong_answers") \
            .insert({
                "question_id": q["id"],
                "question_text": q["q"],
                "stage": st.session_state.stage,
                "wrong_count": 1
            }) \
            .execute()



def load_ranking():
    res = supabase.table("wrong_answers") \
        .select("*") \
        .order("wrong_count", desc=True) \
        .limit(10) \
        .execute()
    return res.data
#AIからのヒント表示
from openai import RateLimitError

def generate_hint(question):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful tutor."},
                {"role": "user", "content": f"Give a short hint for this question:\n{question}"}
            ],
            max_tokens=80
        )
        return response.choices[0].message.content

    except RateLimitError:
        return "⚠️ ヒントの取得回数が上限に達しました。しばらく待ってからもう一度試してください。"


quiz_data = stage1_quiz if st.session_state.stage == 1 else stage2_quiz


#ステージ１クリア画面
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
    
#ゲームクリア画面
if st.session_state.mode == "clear":
    st.title("🏆 ゲームクリア！")
    st.balloons()
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

    if st.button("📖 復習モードへ"):
        st.session_state.mode = "review"
        st.rerun()

    st.stop()
#ゲームオーバー画面

if st.session_state.mode == "game_over":
    st.title("💀 GAME OVER")
    st.error("ライフがなくなってしまった…")

    st.write("でも大丈夫。間違えた問題を復習して、もう一度挑戦しよう🔥")

    st.subheader("📘 復習（間違えた問題）")
    for w in st.session_state.wrong_questions:
        st.code(w["q"])
        st.write(f"✅ 正解：{w['answer']}")
        st.write(f"📝 解説：{w['explanation']}")
        st.divider()

    if st.button("🔁 最初からやり直す"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    if st.button("📖 復習モードへ"):
        st.session_state.mode = "review"
        st.rerun()

    st.stop()

#復習モード
if st.session_state.mode == "review":
    st.title("📖 復習モード")
    st.write("間違えた回数が多い問題から優先的に復習しよう🔥")

    ranking = load_ranking()

    if not ranking:
        st.info("まだ間違えた問題がありません")
        st.stop()

    for i, r in enumerate(ranking, 1):
        with st.expander(f"{i}位｜{r['wrong_count']}回ミス（Stage {r['stage']}）"):
            st.code(r["question_text"])

            if st.button(f"🧠 この問題を復習する", key=r["question_id"]):
                st.session_state.current_question = {
                    "id": r["question_id"],
                    "q": r["question_text"],
                }
                st.session_state.mode = "review_question"
                st.rerun()

    st.stop()
    
if st.session_state.mode == "review_question":
    q = st.session_state.current_question

    st.title("🧠 復習問題")
    st.code(q["q"])

    # 元のクイズデータから完全な問題を取得
    all_quiz = stage1_quiz + stage2_quiz
    full_q = next(item for item in all_quiz if item["id"] == q["id"])

    choice = st.radio("選択肢", full_q["choices"])

    if st.button("答える"):
        if choice == full_q["answer"]:
            st.success("⭕ 正解！")
        else:
            st.error("❌ 不正解")
            st.write(f"✅ 正解：{full_q['answer']}")

        st.info(f"📝 解説：{full_q['explanation']}")

    if st.button("⬅ 復習一覧に戻る"):
        st.session_state.mode = "review"
        st.rerun()

    st.stop()

# ----------------------------
# ゲーム画面
# ----------------------------
if st.session_state.stage == 2:
    st.title("🔥 BOSS BATTLE 🔥 PythonクイズRPG")
else:
    st.title(f"🧙‍♂️ PythonクイズRPG（Stage {st.session_state.stage}）")

# ----------------------------
# BGM（Stageごと）
# ----------------------------
col1, col2 = st.columns(2)

#BGMのONOFF選択
with col1:
    if st.button("🔊 BGM ON"):
        st.session_state.bgm_on = True

with col2:
    if st.button("🔇 BGM OFF"):
        st.session_state.bgm_on = False

#BGM選択（ステージごとに違う）
if st.session_state.bgm_on:
    if st.session_state.stage == 1:
        st.audio("maou_game_medley02.mp3", loop=True)
    elif st.session_state.stage == 2:
        st.audio("maou_game_lastboss04.mp3", loop=True)


# 敵画像の表示（ステージごとに変更）
if st.session_state.stage == 1:
    st.image("fantasy_orc.png", width=250)
else:
    st.image("fantasy_maou_devil.png", width=300)


if st.session_state.stage == 2:
    st.write(f"😈 魔王HP：{st.session_state.enemy_hp}")
else:
    st.write(f"👾 敵HP：{st.session_state.enemy_hp}")

st.write(f"❤️ ライフ：{st.session_state.life}")

# 問題をランダム取得
if st.session_state.current_question is None:
    st.session_state.current_question = random.choice(quiz_data)
    st.session_state.ai_hint = None
    st.session_state.hint_used = False

q = st.session_state.current_question

# ⑤ 問題が変わったらリセット
if st.session_state.get("prev_q_id") != q["id"]:
    st.session_state.ai_hint = None
    st.session_state.hint_requested = False
    st.session_state.prev_q_id = q["id"]
st.subheader("❓ 問題")
st.code(q["q"])
#ヒントボタン

if st.button("ヒントを見る") and not st.session_state.hint_generating:
    st.session_state.hint_requested = True
    st.session_state.hint_generating = True

    # --- AIヒント生成（API呼び出しはここだけ）---
if (
    st.session_state.hint_requested
    and st.session_state.ai_hint is None
    and st.session_state.hint_generating
):
    st.session_state.ai_hint = generate_hint(q["q"])
    st.session_state.hint_generating = False



if st.session_state.ai_hint:
    st.info(f"🤖 ヒント：{st.session_state.ai_hint}")

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

        # 🔥 Supabaseに保存
        save_wrong_answer(q)

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
        st.session_state.ai_hint = None
        st.session_state.hint_requested = False
                # 🔥 ヒントをリセット
        st.session_state.ai_hint = None
        st.session_state.hint_used = False



        if st.session_state.life <= 0:
            st.session_state.mode = "game_over"


        if st.session_state.enemy_hp <= 0:
            if st.session_state.stage == 1:
                st.session_state.mode = "stage_clear"
                st.session_state.next_stage = 2
            else:
                st.session_state.mode = "clear"

        st.rerun()
