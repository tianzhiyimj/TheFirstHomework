"""
整数 气温 等于 十
气温 减少 三
气温 增加 二
看看 气温
如果 气温 大于 八 则 看看 费玉清 否则 看看 费翔

整数 年龄 等于 八
整数 钱 等于 二
年龄 增加 一 / (年龄 减少 一)
如果 年龄 大于 八 则 钱 增加 一 否则 无 / (如果 年龄 大于 八 则 钱 增加 一 否则 钱 减少 一)
看看 钱
"""

no = {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10}  # 中文数目字
inputs = []     # 输入流
data = {}       # 数据流
state = None    # 业务状态


def get():
    # 用户输入流
    i = input().split(" ")
    inputs.append(i)
    # print(inputs)


def get_key(v):
    for k, val in no.items():
        if v == val:
            return k


while True:
    get()                                        # 输入存到数据流

    # 状态机
    if not state:
        cur = inputs[-1]                        # 最新输入流
        if cur[0] == '整数':
            state = '定义业务'
        elif cur[0] in list(data.keys()):
            state = '运算业务'
        elif cur[0] == '看看':
            state = '看看业务'
        elif cur[0] == '如果':
            state = '正则业务'
        elif cur[0] == '结束':
            exit()
        else:
            print("状态错误")

    if state == '定义业务':
        cur = inputs[-1]                        # 最新输入流
        key = cur[1]                            # 变量
        if cur[2] == '等于':                    # 赋值
            data[key] = no[cur[3]]
        else:
            print("定义错误")
        state = None                            # 业务结束
        print('定义业务完成')
        continue

    if state == '运算业务':
        cur = inputs[-1]                        # 最新输入流
        key = cur[0]
        if cur[1] == '减少':                    # 负
            data[key] = data[key] - no[cur[2]]
        elif cur[1] == '增加':                  # 增
            data[key] = data[key] + no[cur[2]]
        else:
            print("运算错误")
        state = None
        print('运算业务完成')
        continue

    if state == '看看业务':
        cur = inputs[-1]  # 最新输入流
        if cur[1] in list(data.keys()):                   # 找值
            key = cur[1]
            print(get_key(data[key]))
        else:
            print("变最错误")
        state = None
        print('看看业务完成')
        continue

    if state == '正则业务':
        cur = inputs[-1]                    # 最新输入流
        if cur[1] in list(data.keys()):     # 找值
            if cur[2] == '大于':            # 条件
                condition = no[cur[3]]
            else:
                print("条件错误")

            # 正条件
            if cur[4] == '则' and data[cur[1]] > condition:
                if cur[5] == '看看':
                    print(cur[6])
                elif cur[6] == '增加' and cur[5] in list(data.keys()):
                    data[cur[5]] = data[cur[5]] + no[cur[7]]
                elif cur[6] == '减少' and cur[5] in list(data.keys()):
                    data[cur[5]] = data[cur[5]] - no[cur[7]]
                elif cur[5] == '无' or cur[6] == '无':
                    pass
                else:
                    print('正条件错误')
            # 负条件
            elif (cur[7] == '否则' or cur[8] == '否则') and data[cur[1]] < condition:
                if cur[8] == '看看':
                    print(cur[9])
                elif cur[10] == '增加' and cur[9] in list(data.keys()):
                    data[cur[9]] = data[cur[9]] + no[cur[11]]
                elif cur[10] == '减少' and cur[9] in list(data.keys()):
                    data[cur[9]] = data[cur[9]] - no[cur[11]]
                elif cur[9] == '无' or cur[10] == '无':
                    pass
                else:
                    print('负条件错误')
            else:
                print("条件错误")
        else:
            print("变量错误")
        state = None
        print('正则业务完成')
        continue
