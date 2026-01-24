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
    {
    "q": "nums = [2, 4, 6, 8]\ntotal = 0\nfor n in nums:\n    if n > 4:\n        total += n\nprint(total)",
    "choices": ["6", "8", "14", "20"],
    "answer": "14",
    "explanation": "6と8を足すので14"
    },

    # 2
    {
    "q": "count = 0\nx = 1\nwhile x < 20:\n    x *= 2\n    count += 1\nprint(count)",
    "choices": ["3", "4", "5", "6"],
    "answer": "5",
    "explanation": "1→2→4→8→16→32 の5回"
    },

    # 3
    {
    "q": "data = [1, 3, 5]\ndata.append(7)\ndata.pop(1)\nprint(data)",
    "choices": ["[1,3,5,7]", "[1,5,7]", "[3,5,7]", "[1,3,7]"],
    "answer": "[1,5,7]",
    "explanation": "index1の3が削除される"
    },

    # 4
    {
    "q": "scores = {'A':70,'B':55,'C':90}\nfor k,v in scores.items():\n    if v < 60:\n        print(k)",
    "choices": ["A", "B", "C", "何も表示されない"],
    "answer": "B",
    "explanation": "60未満はBのみ"
    },

# 5
    {
    "q": "nums = [1,2,3,4,5]\nresult = []\nfor n in nums:\n    if n % 2 == 0:\n        result.append(n)\nprint(result)",
    "choices": ["[1,3,5]", "[2,4]", "[1,2,3,4,5]", "[]"],
    "answer": "[2,4]",
    "explanation": "偶数のみ抽出"
    },

# 6
    {
    "q": "nums = [1,2,3]\nprint(nums[3])",
    "choices": ["3", "None", "エラー", "0"],
    "answer": "エラー",
    "explanation": "存在しないインデックス"
    },

# 7
    {
    "q": "for i in range(1,6):\n    print(i)\n何回表示される？",
    "choices": ["4", "5", "6", "無限"],
    "answer": "5",
    "explanation": "6は含まれない"
    },

# 8
    {
    "q": "for i in range(5):\n    if i == 3:\n        break\n    print(i)",
    "choices": ["0 1 2", "0 1 2 3", "1 2 3", "0 1 2 3 4"],
    "answer": "0 1 2",
    "explanation": "3でbreak"
    },

# 9
    {
    "q": "for i in range(4):\n    if i == 2:\n        continue\n    print(i)",
    "choices": ["0 1 2 3", "0 1 3", "2", "1 3"],
    "answer": "0 1 3",
    "explanation": "2はスキップ"
    },

# 10
{
    "q": "def f(x):\n    return x * 2\nprint(f(3))",
    "choices": ["3", "6", "None", "エラー"],
    "answer": "6",
    "explanation": "returnの値が表示される"
},

# 11
{
    "q": "def f():\n    x = 10\nprint(f())",
    "choices": ["10", "None", "エラー", "何も表示されない"],
    "answer": "None",
    "explanation": "returnがない関数はNone"
},

# 12
{
    "q": "a = [1,2,3]\ndef add(lst):\n    lst.append(4)\nadd(a)\nprint(a)",
    "choices": ["[1,2,3]", "[4]", "[1,2,3,4]", "エラー"],
    "answer": "[1,2,3,4]",
    "explanation": "リストは変更される"
},

# 13
{
    "q": "a = [1,2]\nb = a\na.append(3)\nprint(b)",
    "choices": ["[1,2]", "[1,2,3]", "[3]", "エラー"],
    "answer": "[1,2,3]",
    "explanation": "同じ参照"
},

# 14
{
    "q": "data = {'x':1}\ndata['y'] = data['x'] + 2\nprint(data)",
    "choices": ["{'x':1}", "{'y':3}", "{'x':3,'y':2}", "{'x':1,'y':3}"],
    "answer": "{'x':1,'y':3}",
    "explanation": "yが追加される"
},

# 15
{
    "q": "count = 0\nfor i in range(3):\n    for j in range(2):\n        count += 1\nprint(count)",
    "choices": ["3", "5", "6", "9"],
    "answer": "6",
    "explanation": "3×2"
},

# 16
{
    "q": "nums = [5,12,20,3]\ncount = 0\nfor n in nums:\n    if n > 10:\n        count += 1\nprint(count)",
    "choices": ["1", "2", "3", "4"],
    "answer": "2",
    "explanation": "12と20"
},

# 17
{
    "q": "nums = [3,7,2]\nm = nums[0]\nfor n in nums:\n    if n > m:\n        m = n\nprint(m)",
    "choices": ["3", "7", "2", "エラー"],
    "answer": "7",
    "explanation": "最大値探索"
},

# 18
{
    "q": "x = 5\nif x > 3 and x < 10:\n    print('OK')",
    "choices": ["OK", "5", "True", "何も出ない"],
    "answer": "OK",
    "explanation": "両条件成立"
},

# 19
{
    "q": "x = 2\nif x < 3 or x > 10:\n    print('YES')",
    "choices": ["YES", "2", "False", "何も出ない"],
    "answer": "YES",
    "explanation": "or条件"
},

# 20
{
    "q": "data = {'a':1,'b':2,'c':3}\nprint(len(data))",
    "choices": ["2", "3", "4", "エラー"],
    "answer": "3",
    "explanation": "キー数"
},

# 21〜50（少しテンポ良く難易度UP）
# ※ 実際の授業・ゲームでちょうど良い引っかけレベル

{
    "q": "print(bool(0))",
    "choices": ["True", "False", "0", "エラー"],
    "answer": "False",
    "explanation": "0はFalse"
},

{
    "q": "print(bool(''))",
    "choices": ["True", "False", "None", "エラー"],
    "answer": "False",
    "explanation": "空文字はFalse"
},

{
    "q": "x = [1,2,3]\nprint(2 in x)",
    "choices": ["True", "False", "2", "エラー"],
    "answer": "True",
    "explanation": "含まれている"
},

{
    "q": "x = [1,2,3]\nx.remove(2)\nprint(x)",
    "choices": ["[1,2,3]", "[1,3]", "[2]", "エラー"],
    "answer": "[1,3]",
    "explanation": "値2を削除"
},

{
    "q": "print('A' * 3)",
    "choices": ["AAA", "A3", "エラー", "None"],
    "answer": "AAA",
    "explanation": "文字列の繰り返し"
},

{
    "q": "print(5 // 2)",
    "choices": ["2", "2.5", "3", "エラー"],
    "answer": "2",
    "explanation": "整数除算"
},

{
    "q": "print(5 % 2)",
    "choices": ["1", "2", "0", "エラー"],
    "answer": "1",
    "explanation": "余り"
},

{
    "q": "x = 10\nx += 3\nprint(x)",
    "choices": ["10", "13", "7", "エラー"],
    "answer": "13",
    "explanation": "加算代入"
},

{
    "q": "print(type(3.0))",
    "choices": ["int", "float", "str", "エラー"],
    "answer": "float",
    "explanation": "小数はfloat"
},

{
    "q": "print(len('Python'))",
    "choices": ["5", "6", "7", "エラー"],
    "answer": "6",
    "explanation": "6文字"
},
]
