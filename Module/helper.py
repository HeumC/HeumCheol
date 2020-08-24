#Helper函数
def Helper_MakeList_FullZero(Num):
    List = []
    for i in range(0, Num):
        List.append(0)
    return List
def Helper_MakeList_A_To_B(a , b):
    #Helper_MakeList_A_To_B(a , b)函数是生成并返回一个从Int型a到Int型b的前闭后闭数组
    if type(a) == int and type(b) == int:
        if a <= b:
            List = []
            for i in range(a, b + 1):
                List.append(i)
            return List
        else:
            print("Error:开头的数值不能大于末尾的数值")
    else:
        print("Error:函数参数类型有误")
def Helper_Range(a , b):
    #Helper_Range(a , b)是for循环中range函数的升级版，从原先的前闭后开变成了前闭后闭
    if type(a) == int and type(b) == int:
        if a <= b:
            List = []
            for i in range(a, b + 1):
                List.append(i)
            return List
        else:
            print("Error:开头的数值不能大于末尾的数值")
    else:
        print("Error:函数参数类型有误")