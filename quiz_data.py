# ----------------------------
# クイズデータ
# ----------------------------
stage1_quiz = [
    {
        "id": "S1-001",
        "q": "x = 5\nif x > 3:\n    print(x)",
        "choices": ["3", "5", "True", "x"],
        "answer": "5",
        "explanation": "xは5なのでprint(x)で5が出力される"
    },
    {
        "id": "S1-002",
        "q": "for i in range(3):\n    print(i)\n最後に出力される数は？",
        "choices": ["0", "1", "2", "3"],
        "answer": "2",
        "explanation": "range(3)は0,1,2"
    },
    {
        "id": "S1-003",
        "q": "x = 10\nif x == 10:\n    print('OK')",
        "choices": ["OK", "10", "True", "エラー"],
        "answer": "OK",
        "explanation": "条件がTrueなのでOKが表示される"
    },

    # ① 条件分岐（if）
    {
        "id": "S1-004",
        "q": "x = 5\nif x > 0:\n    print('positive')",
        "choices": ["positive", "zero", "negative", "エラー"],
        "answer": "positive",
        "explanation": "xは正の数なのでpositiveが表示される"
    },
    {
        "id": "S1-005",
        "q": "x = 0\nif x > 0:\n    print('positive')\nelif x == 0:\n    print('zero')",
        "choices": ["positive", "zero", "negative", "何も表示されない"],
        "answer": "zero",
        "explanation": "xは0なのでelifが実行される"
    },
    {
        "id": "S1-006",
        "q": "x = -3\nif x >= 0:\n    print('A')\nelse:\n    print('B')",
        "choices": ["A", "B", "-3", "エラー"],
        "answer": "B",
        "explanation": "xは0以上ではないためelseが実行される"
    },

    # ② 繰り返し（for / range）
    {
        "id": "S1-007",
        "q": "for i in range(3):\n    print(i)",
        "choices": ["0 1 2", "1 2 3", "0 1 2 3", "エラー"],
        "answer": "0 1 2",
        "explanation": "range(3)は0,1,2"
    },
    {
        "id": "S1-008",
        "q": "for i in range(1,5):\n    print(i)\n最後に出力される数は？",
        "choices": ["3", "4", "5", "1"],
        "answer": "4",
        "explanation": "range(1,5)は1,2,3,4"
    },
    {
        "id": "S1-009",
        "q": "for i in range(1,10):\n    if i % 3 == 0:\n        print(i)",
        "choices": ["3 6 9", "1 2 3", "0 3 6 9", "エラー"],
        "answer": "3 6 9",
        "explanation": "3の倍数だけが表示される"
    },

    # ③ while
    {
        "id": "S1-010",
        "q": "i = 0\nwhile i < 3:\n    print(i)\n    i += 1",
        "choices": ["0 1 2", "1 2 3", "0 1 2 3", "無限ループ"],
        "answer": "0 1 2",
        "explanation": "iが0から2まで繰り返される"
    },
    {
        "id": "S1-011",
        "q": "i = 5\nwhile i > 0:\n    i -= 1\nprint(i)",
        "choices": ["0", "1", "5", "エラー"],
        "answer": "0",
        "explanation": "iは0になるまで減る"
    },

    # ④ リスト操作
    {
        "id": "S1-012",
        "q": "nums = [3, 10, 7, 1, 9]\nprint(max(nums))",
        "choices": ["10", "9", "7", "1"],
        "answer": "10",
        "explanation": "最大値は10"
    },
    {
        "id": "S1-013",
        "q": "nums = [3, 10, 7, 1, 9]\nprint(sum(nums))",
        "choices": ["30", "29", "20", "エラー"],
        "answer": "30",
        "explanation": "合計は30"
    },
    {
        "id": "S1-014",
        "q": "nums = [1,2,3]\nnums.append(4)\nprint(nums)",
        "choices": ["[1,2,3,4]", "[4,1,2,3]", "[1,2,3]", "エラー"],
        "answer": "[1,2,3,4]",
        "explanation": "appendで末尾に追加される"
    },
    {
        "id": "S1-015",
        "q": "nums = [5,3,1]\nnums.sort()\nprint(nums)",
        "choices": ["[1,3,5]", "[5,3,1]", "[3,1,5]", "エラー"],
        "answer": "[1,3,5]",
        "explanation": "sortは昇順に並び替える"
    },

    # ⑤ 関数
    {
        "id": "S1-016",
        "q": "def add(a, b):\n    return a + b\nprint(add(3, 5))",
        "choices": ["8", "35", "3+5", "エラー"],
        "answer": "8",
        "explanation": "3+5の結果が返される"
    },
    {
        "id": "S1-017",
        "q": "def bigger(a, b):\n    if a > b:\n        return a\n    else:\n        return b\nprint(bigger(4, 7))",
        "choices": ["4", "7", "True", "False"],
        "answer": "7",
        "explanation": "大きい方の値が返る"
    },
    {
        "id": "S1-018",
        "q": "def f(x):\n    return x * 2\nprint(f(3))",
        "choices": ["6", "9", "3", "エラー"],
        "answer": "6",
        "explanation": "3×2で6"
    },

    # ⑥ 総合（流れ理解）
    {
        "id": "S1-019",
        "q": "x = 4\nif x % 2 == 0:\n    print('even')\nelse:\n    print('odd')",
        "choices": ["even", "odd", "4", "エラー"],
        "answer": "even",
        "explanation": "4は偶数"
    },
    {
        "id": "S1-020",
        "q": "total = 0\nfor i in range(1,4):\n    total += i\nprint(total)",
        "choices": ["6", "10", "3", "エラー"],
        "answer": "6",
        "explanation": "1+2+3=6"
    },
    {
        "id": "S1-021",
        "q": "nums = [1,2,3]\nfor n in nums:\n    print(n * 2)",
        "choices": ["2 4 6", "1 2 3", "3 6 9", "エラー"],
        "answer": "2 4 6",
        "explanation": "各要素を2倍して表示"
    },
]

stage2_quiz = [
    {
        "id": "S2-001",
        "q": "nums = [1,2,3]\nprint(len(nums))",
        "choices": ["2", "3", "4", "エラー"],
        "answer": "3",
        "explanation": "リストの要素数は3"
    },
    {
        "id": "S2-002",
        "q": "for i in range(1,6,2):\n    print(i)\n出力されない数は？",
        "choices": ["1", "3", "5", "2"],
        "answer": "2",
        "explanation": "range(1,6,2)は1,3,5"
    },
    {
        "id": "S2-003",
        "q": "x = 3\nif x != 5:\n    print('A')",
        "choices": ["A", "5", "False", "何も出ない"],
        "answer": "A",
        "explanation": "xは5ではないので条件成立"
    },
    {
    "id": "S2-004",
    "q": "nums = [2, 4, 6, 8]\ntotal = 0\nfor n in nums:\n    if n > 4:\n        total += n\nprint(total)",
    "choices": ["6", "8", "14", "20"],
    "answer": "14",
    "explanation": "6と8を足すので14"
    },

    # 2
    {
        "id": "S2-005",
    "q": "count = 0\nx = 1\nwhile x < 20:\n    x *= 2\n    count += 1\nprint(count)",
    "choices": ["3", "4", "5", "6"],
    "answer": "5",
    "explanation": "1→2→4→8→16→32 の5回"
    },

    # 3
    {
        "id": "S2-006",
    "q": "data = [1, 3, 5]\ndata.append(7)\ndata.pop(1)\nprint(data)",
    "choices": ["[1,3,5,7]", "[1,5,7]", "[3,5,7]", "[1,3,7]"],
    "answer": "[1,5,7]",
    "explanation": "index1の3が削除される"
    },

    # 4
    {
        "id": "S2-007",
    "q": "scores = {'A':70,'B':55,'C':90}\nfor k,v in scores.items():\n    if v < 60:\n        print(k)",
    "choices": ["A", "B", "C", "何も表示されない"],
    "answer": "B",
    "explanation": "60未満はBのみ"
    },

# 5
    {
        "id": "S2-008",
    "q": "nums = [1,2,3,4,5]\nresult = []\nfor n in nums:\n    if n % 2 == 0:\n        result.append(n)\nprint(result)",
    "choices": ["[1,3,5]", "[2,4]", "[1,2,3,4,5]", "[]"],
    "answer": "[2,4]",
    "explanation": "偶数のみ抽出"
    },

# 6
    {
        "id": "S2-009",
    "q": "nums = [1,2,3]\nprint(nums[3])",
    "choices": ["3", "None", "エラー", "0"],
    "answer": "エラー",
    "explanation": "存在しないインデックス"
    },

# 7
    {
        "id": "S2-010",
    "q": "for i in range(1,6):\n    print(i)\n何回表示される？",
    "choices": ["4", "5", "6", "無限"],
    "answer": "5",
    "explanation": "6は含まれない"
    },

# 8
    {
        "id": "S2-011",
    "q": "for i in range(5):\n    if i == 3:\n        break\n    print(i)",
    "choices": ["0 1 2", "0 1 2 3", "1 2 3", "0 1 2 3 4"],
    "answer": "0 1 2",
    "explanation": "3でbreak"
    },

# 9
    {
        "id": "S2-012",
    "q": "for i in range(4):\n    if i == 2:\n        continue\n    print(i)",
    "choices": ["0 1 2 3", "0 1 3", "2", "1 3"],
    "answer": "0 1 3",
    "explanation": "2はスキップ"
    },

# 10
{
    "id": "S2-013",
    "q": "def f(x):\n    return x * 2\nprint(f(3))",
    "choices": ["3", "6", "None", "エラー"],
    "answer": "6",
    "explanation": "returnの値が表示される"
},

# 11
{
    "id": "S2-014",
    "q": "def f():\n    x = 10\nprint(f())",
    "choices": ["10", "None", "エラー", "何も表示されない"],
    "answer": "None",
    "explanation": "returnがない関数はNone"
},

# 12
{
    "id": "S2-015",
    "q": "a = [1,2,3]\ndef add(lst):\n    lst.append(4)\nadd(a)\nprint(a)",
    "choices": ["[1,2,3]", "[4]", "[1,2,3,4]", "エラー"],
    "answer": "[1,2,3,4]",
    "explanation": "リストは変更される"
},

# 13
{
    "id": "S2-016",
    "q": "a = [1,2]\nb = a\na.append(3)\nprint(b)",
    "choices": ["[1,2]", "[1,2,3]", "[3]", "エラー"],
    "answer": "[1,2,3]",
    "explanation": "同じ参照"
},

# 14
{
    "id": "S2-017",
    "q": "data = {'x':1}\ndata['y'] = data['x'] + 2\nprint(data)",
    "choices": ["{'x':1}", "{'y':3}", "{'x':3,'y':2}", "{'x':1,'y':3}"],
    "answer": "{'x':1,'y':3}",
    "explanation": "yが追加される"
},

# 15
{
    "id": "S2-018",
    "q": "count = 0\nfor i in range(3):\n    for j in range(2):\n        count += 1\nprint(count)",
    "choices": ["3", "5", "6", "9"],
    "answer": "6",
    "explanation": "3×2"
},

# 16
{
    "id": "S2-019",
    "q": "nums = [5,12,20,3]\ncount = 0\nfor n in nums:\n    if n > 10:\n        count += 1\nprint(count)",
    "choices": ["1", "2", "3", "4"],
    "answer": "2",
    "explanation": "12と20"
},

# 17
{
    "id": "S2-020",
    "q": "nums = [3,7,2]\nm = nums[0]\nfor n in nums:\n    if n > m:\n        m = n\nprint(m)",
    "choices": ["3", "7", "2", "エラー"],
    "answer": "7",
    "explanation": "最大値探索"
},

# 18
{
    "id": "S2-021",
    "q": "x = 5\nif x > 3 and x < 10:\n    print('OK')",
    "choices": ["OK", "5", "True", "何も出ない"],
    "answer": "OK",
    "explanation": "両条件成立"
},

# 19
{
    "id": "S2-022",
    "q": "x = 2\nif x < 3 or x > 10:\n    print('YES')",
    "choices": ["YES", "2", "False", "何も出ない"],
    "answer": "YES",
    "explanation": "or条件"
},

# 20
{
    "id": "S2-023",
    "q": "data = {'a':1,'b':2,'c':3}\nprint(len(data))",
    "choices": ["2", "3", "4", "エラー"],
    "answer": "3",
    "explanation": "キー数"
},

# 21〜50（少しテンポ良く難易度UP）
# ※ 実際の授業・ゲームでちょうど良い引っかけレベル

{
    "id": "S2-024",
    "q": "print(bool(0))",
    "choices": ["True", "False", "0", "エラー"],
    "answer": "False",
    "explanation": "0はFalse"
},

{
    "id": "S2-025",
    "q": "print(bool(''))",
    "choices": ["True", "False", "None", "エラー"],
    "answer": "False",
    "explanation": "空文字はFalse"
},

{
    "id": "S2-026",
    "q": "x = [1,2,3]\nprint(2 in x)",
    "choices": ["True", "False", "2", "エラー"],
    "answer": "True",
    "explanation": "含まれている"
},

{
    "id": "S2-027",
    "q": "x = [1,2,3]\nx.remove(2)\nprint(x)",
    "choices": ["[1,2,3]", "[1,3]", "[2]", "エラー"],
    "answer": "[1,3]",
    "explanation": "値2を削除"
},

{
    "id": "S2-028",
    "q": "print('A' * 3)",
    "choices": ["AAA", "A3", "エラー", "None"],
    "answer": "AAA",
    "explanation": "文字列の繰り返し"
},

{
    "id": "S2-029",
    "q": "print(5 // 2)",
    "choices": ["2", "2.5", "3", "エラー"],
    "answer": "2",
    "explanation": "整数除算"
},

{
    "id": "S2-030",
    "q": "print(5 % 2)",
    "choices": ["1", "2", "0", "エラー"],
    "answer": "1",
    "explanation": "余り"
},

{
    "id": "S2-031",
    "q": "x = 10\nx += 3\nprint(x)",
    "choices": ["10", "13", "7", "エラー"],
    "answer": "13",
    "explanation": "加算代入"
},

{
    "id": "S2-032",
    "q": "print(type(3.0))",
    "choices": ["int", "float", "str", "エラー"],
    "answer": "float",
    "explanation": "小数はfloat"
},

{
    "id": "S2-033",
    "q": "print(len('Python'))",
    "choices": ["5", "6", "7", "エラー"],
    "answer": "6",
    "explanation": "6文字"
},

{
        "id": "BOSS-01",
        "q": "nums = [1, 2, 3, 4, 5]\nresult = 0\nfor n in nums:\n    if n % 2 == 0:\n        result += n\n    else:\n        result -= n\nprint(result)",
        "choices": ["-3", "-1", "1", "3"],
        "answer": "-3",
        "explanation": "偶数:+2,+4 奇数:-1,-3,-5 → -3"
    },
    {
        "id": "BOSS-02",
        "q": "x = 1\ncount = 0\nwhile x < 50:\n    x *= 3\n    count += 1\nprint(count)",
        "choices": ["3", "4", "5", "6"],
        "answer": "4",
        "explanation": "1→3→9→27→81（4回）"
    },
    {
        "id": "BOSS-03",
        "q": "data = [10,20,30,40]\nfor i in range(len(data)):\n    if data[i] == 30:\n        data[i] = 99\nprint(data)",
        "choices": ["[10,20,30,40]", "[10,20,99,40]", "[99,20,30,40]", "エラー"],
        "answer": "[10,20,99,40]",
        "explanation": "30だけ99に置き換え"
    },
    {
        "id": "BOSS-04",
        "q": "scores = {'A':50,'B':80,'C':65}\npassed = []\nfor k,v in scores.items():\n    if v >= 70:\n        passed.append(k)\nprint(passed)",
        "choices": ["['A']", "['B']", "['B','C']", "[]"],
        "answer": "['B']",
        "explanation": "70以上はBのみ"
    },
    {
        "id": "BOSS-05",
        "q": "def f(nums):\n    total = 0\n    for n in nums:\n        if n < 0:\n            continue\n        total += n\n    return total\n\nprint(f([1, -2, 3, -4, 5]))",
        "choices": ["3", "6", "9", "エラー"],
        "answer": "9",
        "explanation": "負の数は無視 → 1+3+5"
    },
    {
        "id": "BOSS-06",
        "q": "def g(x):\n    if x == 0:\n        return 1\n    return x * g(x-1)\n\nprint(g(4))",
        "choices": ["4", "12", "24", "エラー"],
        "answer": "24",
        "explanation": "再帰で4! = 24"
    },
    {
        "id": "BOSS-07",
        "q": "nums = [1,2,3]\nnew = []\nfor n in nums:\n    new.append(n*2)\nnums.append(4)\nprint(new)",
        "choices": ["[2,4,6,8]", "[2,4,6]", "[1,2,3,4]", "エラー"],
        "answer": "[2,4,6]",
        "explanation": "newはnums追加前に作成"
    },
    {
        "id": "BOSS-08",
        "q": "x = 0\nfor i in range(5):\n    for j in range(5):\n        if i == j:\n            x += 1\nprint(x)",
        "choices": ["5", "10", "15", "25"],
        "answer": "5",
        "explanation": "i==jは5回"
    },
    {
        "id": "BOSS-09",
        "q": "def f(a, b=2):\n    return a * b\n\nprint(f(3) + f(3, 4))",
        "choices": ["12", "18", "24", "エラー"],
        "answer": "18",
        "explanation": "6 + 12"
    },
    {
        "id": "BOSS-10",
        "q": "nums = [1,2,3,4,5]\nresult = []\nfor i in range(len(nums)):\n    if i % 2 == 0:\n        result.append(nums[i])\nprint(result)",
        "choices": ["[1,2,3,4,5]", "[1,3,5]", "[2,4]", "[0,2,4]"],
        "answer": "[1,3,5]",
        "explanation": "偶数インデックス"
    },
]
