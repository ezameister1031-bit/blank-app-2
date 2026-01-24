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
