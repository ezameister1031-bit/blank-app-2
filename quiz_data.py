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

    # ① 条件分岐（if）
    {
        "q": "x = 5\nif x > 0:\n    print('positive')",
        "choices": ["positive", "zero", "negative", "エラー"],
        "answer": "positive",
        "explanation": "xは正の数なのでpositiveが表示される"
    },
    {
        "q": "x = 0\nif x > 0:\n    print('positive')\nelif x == 0:\n    print('zero')",
        "choices": ["positive", "zero", "negative", "何も表示されない"],
        "answer": "zero",
        "explanation": "xは0なのでelifが実行される"
    },
    {
        "q": "x = -3\nif x >= 0:\n    print('A')\nelse:\n    print('B')",
        "choices": ["A", "B", "-3", "エラー"],
        "answer": "B",
        "explanation": "xは0以上ではないためelseが実行される"
    },

    # ② 繰り返し（for / range）
    {
        "q": "for i in range(3):\n    print(i)",
        "choices": ["0 1 2", "1 2 3", "0 1 2 3", "エラー"],
        "answer": "0 1 2",
        "explanation": "range(3)は0,1,2"
    },
    {
        "q": "for i in range(1,5):\n    print(i)\n最後に出力される数は？",
        "choices": ["3", "4", "5", "1"],
        "answer": "4",
        "explanation": "range(1,5)は1,2,3,4"
    },
    {
        "q": "for i in range(1,10):\n    if i % 3 == 0:\n        print(i)",
        "choices": ["3 6 9", "1 2 3", "0 3 6 9", "エラー"],
        "answer": "3 6 9",
        "explanation": "3の倍数だけが表示される"
    },

    # ③ while
    {
        "q": "i = 0\nwhile i < 3:\n    print(i)\n    i += 1",
        "choices": ["0 1 2", "1 2 3", "0 1 2 3", "無限ループ"],
        "answer": "0 1 2",
        "explanation": "iが0から2まで繰り返される"
    },
    {
        "q": "i = 5\nwhile i > 0:\n    i -= 1\nprint(i)",
        "choices": ["0", "1", "5", "エラー"],
        "answer": "0",
        "explanation": "iは0になるまで減る"
    },

    # ④ リスト操作
    {
        "q": "nums = [3, 10, 7, 1, 9]\nprint(max(nums))",
        "choices": ["10", "9", "7", "1"],
        "answer": "10",
        "explanation": "最大値は10"
    },
    {
        "q": "nums = [3, 10, 7, 1, 9]\nprint(sum(nums))",
        "choices": ["30", "29", "20", "エラー"],
        "answer": "30",
        "explanation": "合計は30"
    },
    {
        "q": "nums = [1,2,3]\nnums.append(4)\nprint(nums)",
        "choices": ["[1,2,3,4]", "[4,1,2,3]", "[1,2,3]", "エラー"],
        "answer": "[1,2,3,4]",
        "explanation": "appendで末尾に追加される"
    },
    {
        "q": "nums = [5,3,1]\nnums.sort()\nprint(nums)",
        "choices": ["[1,3,5]", "[5,3,1]", "[3,1,5]", "エラー"],
        "answer": "[1,3,5]",
        "explanation": "sortは昇順に並び替える"
    },

    # ⑤ 関数
    {
        "q": "def add(a, b):\n    return a + b\nprint(add(3, 5))",
        "choices": ["8", "35", "3+5", "エラー"],
        "answer": "8",
        "explanation": "3+5の結果が返される"
    },
    {
        "q": "def bigger(a, b):\n    if a > b:\n        return a\n    else:\n        return b\nprint(bigger(4, 7))",
        "choices": ["4", "7", "True", "False"],
        "answer": "7",
        "explanation": "大きい方の値が返る"
    },
    {
        "q": "def f(x):\n    return x * 2\nprint(f(3))",
        "choices": ["6", "9", "3", "エラー"],
        "answer": "6",
        "explanation": "3×2で6"
    },

    # ⑥ 総合（流れ理解）
    {
        "q": "x = 4\nif x % 2 == 0:\n    print('even')\nelse:\n    print('odd')",
        "choices": ["even", "odd", "4", "エラー"],
        "answer": "even",
        "explanation": "4は偶数"
    },
    {
        "q": "total = 0\nfor i in range(1,4):\n    total += i\nprint(total)",
        "choices": ["6", "10", "3", "エラー"],
        "answer": "6",
        "explanation": "1+2+3=6"
    },
    {
        "q": "nums = [1,2,3]\nfor n in nums:\n    print(n * 2)",
        "choices": ["2 4 6", "1 2 3", "3 6 9", "エラー"],
        "answer": "2 4 6",
        "explanation": "各要素を2倍して表示"
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
