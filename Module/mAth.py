import math
from module import helper

MathConstant_Pi = math.pi
MathConstant_e = math.e
MathConstant_UltiLowNum = 0.00000000000000000000000000000000000000000000000000000000001
MathConstant_UltiHighNum = 999999999999999999999999999999999999999999999999999999999999

def Odd_Judge(Number):
    if Number % 2 == 0:
        return False
    elif Number % 2 == 1:
        return True
    else:
        print("无法判断奇偶")
def Even_Judge(Number):
    if Number % 2 == 0:
        return True
    elif Number % 2 == 1:
        return False
    else:
        print("无法判断奇偶")
def SumAll_Int(start , end):
    #Math_SumAll_Int(start , end)函数：把从start到end的所有前闭后闭的Int型数字加起来，并返回Int型。
    if type(start) == int and type(end) == int:
        if start <= end:
            a = []
            for i in range(start, end + 1):
                a.append(i)
            Sum = sum(a)
            return Sum
        else:
            print("Error:开头的数值不能大于末尾的数值")
    else:
        print("Error:函数参数类型有误")
def SumAll_Float(start , end , addNum = 1.0):
    #Math_SumAll_Float(start , end , addNum = 1.0)函数：
    # 把从start到end的所有前闭后闭的Float型数字,间隔为addNum的数字加起来，并返回Float型。
    #注：如果不输入addNum的值，则默认为1.0
    if type(start) == int or type(start) == float:
        if type(end) == int or type(start) == float:
            if type(addNum) == int or type(addNum) == float:
                if start <= end:
                    if addNum <= end - start:
                        sum_List = []
                        while start <= end:
                            sum_List.append(start)
                            start += addNum
                        return sum(sum_List)
                    else:
                        print("Error:间隔的数值不能超过末尾的数值减去开头的数值")
                else:
                    print("Error:开头的数值不能大于末尾的数值")
            else:
                print("Error:函数参数类型有误")
        else:
            print("Error:函数参数类型有误")
    else:
        print("Error:函数参数类型有误")
def MultAll_Int(start , end):
    #Math_MultAll_Int(start , end)函数：把从start到end的所有前闭后闭的Int型数字相乘起来，并返回Int型。
    #注：如果输入进Math_MultAll_Int(start , end)函数里的是Float类型，则强制转换为Int型
    a = []
    start = int(start)
    end = int(end)
    for i in range(start , end + 1):
        a.append(i)
    MultList = 1
    for j in a:
        MultList *= j
    return MultList
def MultAll_Float(start , end , addNum = 1.0):
    #Math_MultAll_Float(start , end , addNum = 1.0)函数：
    # 把从start到end的所有前闭后闭的Float型数字,间隔为addNum的数字相乘起来，并返回Float型。
    #注：如果不输入addNum的值，则默认为1.0
    MultList = 1.0
    while True:
        MultList *= start
        start += addNum
        if start >= end + MathConstant_UltiLowNum:
            break
    return MultList
def Circle_Calc_Circumference(radius):
    #Math_Circle_Calc_Circumference(radius):函数：输入半径radius值来计算圆的周长
    circumference = MathConstant_Pi * 2 * radius
    return circumference
def Circle_Calc_Space(radius):
    #Math_Circle_Calc_Space(r , Precision = 2)函数：输入半径r值来计算圆的面积
    #使用其Precision所相对应的精度（如为1则pi使用3.1 ， 为2则pi使用3.14）
    space = MathConstant_Pi * radius ** 2
    return space
def Average_Number(List):
    return sum(List) / len(List)
def Median(List):
    List = sorted(List)
    if len(List) % 2 == 0:
        return (List[int(len(List) / 2 - 1)] + List[int(len(List) / 2 + 1 - 1)]) / 2
    else:
        return List[int((len(List) + 1) / 2) - 1]
def Mode(List):
    x = dict((a, List.count(a)) for a in List)
    y = [k for k, v in x.items() if max(x.values()) == v]
    return y
def Variance(List):
    temp_List = []
    ave = Average_Number(List)
    for num in List:
        temp_List.append(((num - ave) ** 2) / len(List))
    return sum(temp_List)

class Circle:
    def __init__(self, radius):
        self.Radius = radius
        self.Circumference = Circle_Calc_Circumference(radius)
        self.Space = Circle_Calc_Space(radius)
class HCList:
    def __init__(self, hclist):
        self.hclist = hclist
        self.averageNumber = Average_Number(hclist)
        self.median = Median(hclist)
        self.mode = Mode(hclist)
        self.variance = Variance(hclist)

def Bucket_Sort(lst):
    buckets = [0] * ((max(lst) - min(lst)) + 1)
    for i in range(len(lst)):
        buckets[lst[i] - min(lst)] += 1
    res = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i + min(lst)] * buckets[i]
    return res
def Fibonacci(n):
    #Math_Fibonacci(n)函数：输入想得到几项斐波那契数列，以数组的形式返回得到的n项斐波那契数列
    res = [1 , 1]
    if n <= 0:
        print("项数不能小于1")
        exit("FIBO_NOE_LRTONE")
    elif n == 1:
        res = [1]
        return res
    elif n == 2:
        return res
    else:
        for i in range(2, n):
            res.append(res[i - 1] + res[i - 2])
        return res
def Average_IncreaseNum(List):
    Average_Increase_Num = 0
    for i in range(1 , len(List)):
        Increase_Num = List[i + 1 - 1] - List[i - 1]
        Average_Increase_Num += Increase_Num / (len(List) - 1)
        #print("第%d次增加的数：%d" %(i + 1 , Increase_Num))
    #print(Average_Increase_Num)
    return Average_Increase_Num
def Predict_NextNum(List):
    return List[len(List) - 1] + Average_IncreaseNum(List)
def Urinal_Problem(Urinal_Number):
    if Urinal_Number % 2 == 0:
        Man_Number = Urinal_Number / 2
        return Man_Number
    elif Urinal_Number % 2 == 1:
        #Man_Number = ((Urinal_Number - 1) / 2) + 1
        Man_Number = (Urinal_Number + 1) / 2
        return Man_Number
def PillsProblem(TimeCircle , Pills_PerBox , PillsNum_PerDay , Times = 3 , Circle_Limite_Flag = False , Circle_Limite_Num = 5):
    #TimeCircle = 365  # 多少 天一个循环
    #Pills_PerBox = 12  # 一个药盒里有 多少 个药
    #PillsNum_PerDay = 1  # 一天吃 多少 个

    ExtraDays = 0  # 吃够一个循环后多出的天数
    NotEnoughDays = 0  # 还剩多少天
    DayNum_PerBox = Pills_PerBox * PillsNum_PerDay  # 一盒药能吃 多少 天

    Box_Num_List = []

    Circle_Limite = 0

    for i in helper.Helper_Range(1, Times):
        Box_Num = int((TimeCircle - ExtraDays) / DayNum_PerBox)
        NotEnoughDays = (TimeCircle - ExtraDays) % DayNum_PerBox
        if NotEnoughDays != 0:
            if Circle_Limite_Flag:
                Circle_Limite = 0
            Box_Num_List.append(Box_Num + 1)
            ExtraDays = DayNum_PerBox - NotEnoughDays
            print("第%d次 %d天 需要 %d盒（一盒有%d个药，一天吃%d个药）超出%d天"
                  % (i, TimeCircle ,Box_Num + 1 , Pills_PerBox , PillsNum_PerDay , ExtraDays))
        else:
            if Circle_Limite_Flag:
                if Circle_Limite >= Circle_Limite_Num:
                    break
                Circle_Limite += 1
            Box_Num_List.append(Box_Num)
            print("第%d次 %d天 需要 %d盒（一盒有%d个药，一天吃%d个药）超出0天"
                  % (i, TimeCircle, Box_Num , Pills_PerBox, PillsNum_PerDay))

    return Box_Num_List