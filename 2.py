no = {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10}  # 中文数目字
inputs = []     # 输入流
var = []        # 变量流
data = []       # 数据流
regexp = []     # 正则流
state = None    # 业务状态


def get():
    # 用户输入流
    inputs.append(input().split()[-1])
    print(inputs)


def get_key(v):
    for k, val in no.items():
        if v == val:
            return k


while True:
    inputs.append(input().split()[-1])         # 输入存到数据流
    # 状态机
    if not state:
        if inputs[-1] == '整数':
            state = '定义'
        elif inputs[-1] in var:
            state = '运算'
        elif inputs[-1] == '看看':
            state = '看看'
        elif inputs[-1] == '如果':
            state = '正则'

    if state == '定义':
        print('到达定义')
        get()                                   # 变量
        var.append(inputs[-1])
        get()
        if inputs[-1] == '等于':                # 赋值
            get()
            data.append(no[inputs[-1]])
        state = None                            # 业务结束
        continue

    if state == '运算':
        print('到达运算')
        get()
        if inputs[-1] == '减少':                # 负
            get()
            data[-1] = get_key(data[-1]-no[inputs[-1]])
        elif inputs[-1] == '增加':              # 增
            get()
            data[-1] = get_key(data[-1]+no[inputs[-1]])
        state = None
        continue

    if state == '看看':
        print('到达看看')
        get()
        if inputs[-1] in var:                   # 找值
            print(data[-1])
        state = None
        continue
