import random
import time
from time import perf_counter

#Helper函数
def ExitMSG_Return(funcName, MSG):
    """此函数所接受的变量：
                   funcName：str型
                   MSG：str型
   此函数的作用：
                   输出funcName该函数的错误信息MSG，并结束程序
   此函数返回值：
                   None"""
    if type(funcName) != str and type(MSG) != str:
        ExitMSG_Return("ExitMSG_Return(funcName, MSG)", "\n\t\t\t\t\t\t\t\t\t1.funcName必须为str型"
                                                        "\n\t\t\t\t\t\t\t\t\t2.MSG必须为str型")
    if type(funcName) != str:
        ExitMSG_Return("ExitMSG_Return(funcName, MSG)", "funcName必须为str型")
    if type(MSG) != str:
        ExitMSG_Return("ExitMSG_Return(funcName, MSG)", "MSG必须为str型")
    exit("函数错误：\n%s错误：%s" %(funcName, MSG))
def isString(judged_object):
    return type(judged_object) == str
def isInt(judged_object):
    return type(judged_object) == int
def isFloat(judged_object):
    return type(judged_object) == float
def isDict(judged_object):
    return type(judged_object) == dict
def Start(funcName):
    if isString(funcName):
        print('{:=^70}'.format('%s运行中' %funcName))
    else:
        ExitMSG_Return("Start(funcName)", "funcName必须为str型")
def Done(funcName):
    if isString(funcName):
        print('{:=^70}'.format('%s运行完成' % funcName))
    else:
        ExitMSG_Return("Start(funcName)", "funcName必须为str型")
def MakeList(a , b):
    """此函数所接受的变量：
                       a：int型
                       b：int型
       此函数的作用：
                       生成并返回一个从Int型a到Int型b的前闭后闭数组
       此函数返回值：
                       List：int型数组"""
    if type(a) != int and type(b) != int:
        ExitMSG_Return("MakeList(a , b)", "\n\t\t\t\t\t1.a必须为int型"
                                          "\n\t\t\t\t\t2.b必须为int型")
    if type(a) != int:
        ExitMSG_Return("MakeList(a , b)", "a必须为int型")
    if type(b) != int:
        ExitMSG_Return("MakeList(a , b)", "b必须为int型")
    if a <= b:
        List = []
        for i in range(a, b + 1):
            List.append(i)
        return List
    else:
        ExitMSG_Return("MakeList(a , b)", "开头的数值不能大于末尾的数值")
def MakeList_FullZero(Num):
    """此函数所接受的变量：
                           Num：int型
           此函数的作用：
                           生成并返回一个长度为Num的全零数组
           此函数返回值：
                           List：int型数组"""
    if type(Num) != int:
        ExitMSG_Return("MakeList_FullZero(Num)", "Num必须为int型")
    if Num < 0:
        ExitMSG_Return("MakeList_FullZero(Num)", "Num不能低于0（数组的长度不能为负数）")
    List = []
    for i in range(0, Num):
        List.append(0)
    return List
def MakeList_RandomNumber(Num, a, b):
    """此函数所接受的变量：
                               Num：int型
                               a：int型
                               b：int型
               此函数的作用：
                               生成并返回一个长度为Num，每个数为【a，b】的随机取值的数组
               此函数返回值：
                               lst1：int型数组"""
    if type(Num) != int:
        ExitMSG_Return("MakeList_RandomNumber(Num, a, b)", "Num必须为int型")
    if type(a) != int:
        ExitMSG_Return("MakeList_RandomNumber(Num, a, b)", "a必须为int型")
    if type(b) != int:
        ExitMSG_Return("MakeList_RandomNumber(Num, a, b)", "b必须为int型")
    if a > b:
        ExitMSG_Return("MakeList_RandomNumber(Num, a, b)", "a不能大于b")
    lst1 = []
    for i in range(0, Num):
        lst1.append(random.randint(a, b))
    return lst1
def MakeList_RandomIncrease(Num, a, b):
    """此函数所接受的变量：
                                   Num：int型
                                   a：int型
                                   b：int型
                   此函数的作用：
                                   每次生成一个数ri，下一个数的取值范围为【a+ri，b+ri】，以此类推共生成Num长度的int型数组


                   此函数返回值：
                                   lst：int型数组"""
    if type(Num) != int:
        ExitMSG_Return("MakeList_RandomIncrease(Num, a, b)", "Num必须为int型")
    if type(a) != int:
        ExitMSG_Return("MakeList_RandomIncrease(Num, a, b)", "a必须为int型")
    if type(b) != int:
        ExitMSG_Return("MakeList_RandomIncrease(Num, a, b)", "b必须为int型")
    if a > b:
        ExitMSG_Return("MakeList_RandomNumber(Num, a, b)", "a不能大于b")
    lst = []
    aTemp = a
    bTemp = b
    for i in range(0, Num):
        ri = random.randint(aTemp, bTemp)
        lst.append(ri)
        aTemp += ri
        bTemp += ri
    return lst
def Range(a , b):
    """此函数所接受的变量：
                                       a：int型
                                       b：int型
                       此函数的作用：
                                       range函数的升级版，从原先的前闭后开变成了前闭后闭


                       此函数返回值：
                                       List：int型数组"""
    if type(a) != int:
        ExitMSG_Return("Range(a , b)", "a必须为int型")
    if type(b) != int:
        ExitMSG_Return("Range(a , b)", "b必须为int型")
    if a <= b:
        List = []
        for i in range(a, b + 1):
            List.append(i)
        return List
    else:
        ExitMSG_Return("Range(a , b)", "开头的数值不能大于末尾的数值")
def Number_Separate(number):
    number_lst = []
    change_flag = False
    intRange_length = 0
    for num_str in str(number):
        if num_str == '.':
            change_flag = True
            continue
        if change_flag:
            number_lst.append(int(num_str))
        else:
            intRange_length += 1
            number_lst.append(int(num_str))
    return [number_lst, intRange_length]
def Probabilistic_Operation(probability):
    upper = round(probability * 100)
    random_Num = random.randint(0, 100)
    if 0 <= random_Num <= upper:
        return True
    else:
        return False
def Probabilistic_Operation_Function_Judge(probability):
    base_List = MakeList(1, 100)
    list_1 = base_List + [probability]
    # print(list_1)

    t_account = 0
    for i in range(0, 10000):
        if Probabilistic_Operation(probability):
            t_account += 1
    list_2 = base_List + [t_account / 10000]
    # print(list_2)

    length = len(list_1)
    X = list_1
    Y = list_2
    XY = []
    for i in range(0, length):
        XY.append(list_1[i] * list_2[i])
    X2 = []
    for i in list_1:
        X2.append(i ** 2)
    Y2 = []
    for i in list_2:
        Y2.append(i ** 2)

    X_A = sum(X) / len(X)
    Y_A = sum(Y) / len(Y)
    XY_A = sum(XY) / len(XY)
    X2_A = sum(X2) / len(X2)
    Y2_A = sum(Y2) / len(Y2)

    R = (XY_A - X_A * Y_A) / ((X2_A - X_A ** 2) ** (1 / 2) * (Y2_A - Y_A ** 2) ** (1 / 2))

    return R
class Watcher:
    def __init__(self, funcName):
        self.funcName = funcName
    def Start(self):
        Start(self.funcName)
    def Done(self):
        Done(self.funcName)