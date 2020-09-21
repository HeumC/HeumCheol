import math
from Module import helper

MathConstant_Pi = math.pi
MathConstant_e = math.e
MathConstant_UltiLowNum = 0.00000000000000000000000000000000000000000000000000000000001
MathConstant_UltiHighNum = 999999999999999999999999999999999999999999999999999999999999

from enum import Enum, unique
@unique

class Relevance_BT_Two_List_Enum(Enum):
    calc_way_math = 0
    calc_way_angle = 1
class Arithmetic_Progression_Enum(Enum):
    Sn = 0
    an = 1
class Geometric_Progression_Enum(Enum):
    Sn = 0
    an = 1

def Odd_Judge(number):
    """此函数所接受的变量：
                number：int型
此函数的作用：
                判断数字number是否为奇数，若是则返回True，反之则返回False
此函数返回值：
                布尔类型（True or False）"""

    if type(number) != int:
        helper.ExitMSG_Return("Odd_Judge(number)", "number必须为int型")
    return number % 2 == 1
def Even_Judge(number):
    """此函数所接受的变量：
                number：int型
此函数的作用：
                判断数字number是否为偶数，若是则返回True，反之则返回False
此函数返回值：
                布尔类型（True or False）"""
    if type(number) != int:
        helper.ExitMSG_Return("Even_Judge(number)", "number必须为int型")
    return number % 2 == 0
def Number_Figure(number):
    number = round(number)
    number_str = str(number)
    number_length = len(number_str)
    return number_length
def NumberPrint(number, oneRange):
    lst = helper.Number_Separate(number)
    number_list = lst[0]
    number_intRange_length = lst[1]
    highest_range_number_account = number_intRange_length % oneRange
    comma_counter = 0
    frequency_counter = 0
    first_flag = True
    for num in number_list:
        frequency_counter += 1
        if first_flag and comma_counter == highest_range_number_account and highest_range_number_account != 0:
            first_flag = False
            comma_counter = 0
            print(',', end='')
        elif frequency_counter == number_intRange_length + 1:
            print('.', end='')
        elif comma_counter == oneRange:
            comma_counter = 0
            print(',', end='')
        print(num, end='')
        comma_counter += 1
def NumberPrint_UNStyle(number):
    NumberPrint(number, 3)
def NumberPrint_CNStyle(number):
    NumberPrint(number, 4)
def Arithmetic_Progression(a1, d, n, result_flag):
    if result_flag == Arithmetic_Progression_Enum.Sn:
        Sn = n * a1 + (n * d * (n - 1)) / 2
        if round(Sn) == Sn:
            return round(Sn)
        else:
            return Sn
    elif result_flag == Arithmetic_Progression_Enum.an:
        an = a1 + (n - 1) * d
        return an
    else:
        helper.ExitMSG_Return("Arithmetic_Progression(a1, n, d, result_flag=)", "错误")
def Arithmetic_Progression_List(a1, d, n):
    lSt = []
    for temp_n in range(1, n+1):
        lSt.append(Arithmetic_Progression(a1, d, temp_n, result_flag=Arithmetic_Progression_Enum.an))
    return lSt
def Geometric_Progression(a1, q, n, result_flag):
    if result_flag == Geometric_Progression_Enum.Sn:
        if q != 1:
            Sn = a1 * (1 - q ** n) / (1 - q)
            if round(Sn) == Sn:
                return round(Sn)
            else:
                return Sn
        else:
            helper.ExitMSG_Return("Arithmetic_Progression(a1, n, d, result_flag=)", "q不能等于1")
    elif result_flag == Geometric_Progression_Enum.an:
        an = a1 * q ** (n - 1)
        return an
    else:
        helper.ExitMSG_Return("Arithmetic_Progression(a1, n, d, result_flag=)", "错误")
def Geometric_Progression_List(a1, q, n):
    lSt = []
    for temp_n in range(1, n+1):
        lSt.append(Geometric_Progression(a1, q, temp_n, result_flag=Geometric_Progression_Enum.an))
    return lSt
def SumAll_Int(start , end):
    """此函数所接受的变量：
                start：int型
                end：int型
此函数的作用：
                在[start,end]区间内的所有int型数字都相加起来，并返回总值
此函数返回值：
                int型"""
    if type(start) != int and type(end) != int:
        helper.ExitMSG_Return("SumAll_Int(start , end)", "start必须为int型，end必须为int型")
    elif type(start) != int:
        helper.ExitMSG_Return("SumAll_Int(start , end)", "start必须为int型")
    elif type(end) != int:
        helper.ExitMSG_Return("SumAll_Int(start , end)", "end必须为int型")
    elif start >= end:
        helper.ExitMSG_Return("SumAll_Int(start , end)", "开头的数值不能大于末尾的数值")
    Sum = Arithmetic_Progression(start, 1, end - start + 1, result_flag=Arithmetic_Progression_Enum.Sn)
    return round(Sum)
def SumAll_Float(start, end, addNum = 1.0):
    """此函数所接受的变量：
                start：float型
                end：float型
                add_num：float型（add_num若不给它赋值，则默认是1.0）
此函数的作用：
                把[start,end)区间内的所有数字,间隔为addNum的数字加起来，并返回总值
此函数返回值：
                float型"""
    if type(start) != float and type(end) != float and type(addNum) != float:
        helper.ExitMSG_Return("SumAll_Float(start, end, addNum = 1.0)",
                              "\n\t\t\t\t\t\t\t\t\t\t\t1.start必须为float型"
                              "\n\t\t\t\t\t\t\t\t\t\t\t2.end必须为float型"
                              "\n\t\t\t\t\t\t\t\t\t\t\t3.add_num必须为float型")
    elif type(start) != float and type(end) != float:
        helper.ExitMSG_Return("SumAll_Float(start, end, addNum = 1.0)",
                              "\n\t\t\t\t\t\t\t\t\t\t\t1.start必须为float型"
                              "\n\t\t\t\t\t\t\t\t\t\t\t2.end必须为float型")
    elif type(start) != float and type(addNum) != float:
        helper.ExitMSG_Return("SumAll_Float(start, end, addNum = 1.0)",
                              "\n\t\t\t\t\t\t\t\t\t\t\t1.start必须为float型"
                              "\n\t\t\t\t\t\t\t\t\t\t\t2.add_num必须为float型")
    elif type(end) != float and type(addNum) != float:
        helper.ExitMSG_Return("SumAll_Float(start, end, addNum = 1.0)",
                              "\n\t\t\t\t\t\t\t\t\t\t\t1.end必须为float型"
                              "\n\t\t\t\t\t\t\t\t\t\t\t2.add_num必须为float型")
    elif type(start) != float:
        helper.ExitMSG_Return("SumAll_Float(start, end, addNum = 1.0)",
                              "start必须为float型")
    elif type(end) != float:
        helper.ExitMSG_Return("SumAll_Float(start, end, addNum = 1.0)",
                              "end必须为float型")
    elif type(addNum) != float:
        helper.ExitMSG_Return("SumAll_Float(start, end, addNum = 1.0)",
                              "add_num必须为float型")
    elif start >= end:
        helper.ExitMSG_Return("SumAll_Float(start, end, addNum = 1.0)",
                              "开头的数值不能大于末尾的数值")
    elif addNum > end - start:
        helper.ExitMSG_Return("SumAll_Float(start, end, addNum = 1.0)",
                              "间隔的数值不能超过末尾的数值减去开头的数值")
    Sum = Arithmetic_Progression(start, addNum, (end - start) / addNum,
                                 result_flag=Arithmetic_Progression_Enum.Sn)
    return Sum
def MultAll_Int(start , end):
    """此函数所接受的变量：
                    start：int型
                    end：int型
    此函数的作用：
                    在[start,end]区间内的所有int型数字都相乘起来，并返回相乘数值
    此函数返回值：
                    int型"""
    if type(start) != int and type(end) != int:
        helper.ExitMSG_Return("MultAll_Int(start , end)", "\n\t\t\t\t\t\t\t1.start必须为int型"
                                                          "\n\t\t\t\t\t\t\t2.end必须为int型")
    elif type(start) != int:
        helper.ExitMSG_Return("MultAll_Int(start , end)", "start必须为int型")
    elif type(end) != int:
        helper.ExitMSG_Return("MultAll_Int(start , end)", "end必须为int型")
    elif start >= end:
        helper.ExitMSG_Return("MultAll_Int(start , end)", "开头的数值不能大于末尾的数值")

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
def Biggest_Number(lst):
    lst = sorted(lst)
    return lst[len(lst) - 1]
def Minimun_Number(lst):
    lst = sorted(lst)
    return lst[0]
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
def Standard_Deviation(List):
    return Variance(List) ** (1/2)
def Gi(number, lst):
    if len(lst) <= 17:
        average = Average_Number(lst)
        SD = Standard_Deviation(lst)
        gi = (abs(number - average)) / SD
        return gi
    else:
        helper.ExitMSG_Return("Gi(number, lst)", "Gi值检测现阶段只允许长度小于等于17的列表")
def Grubbs_Table(n):
    if n == 3:
        return [1.148, 1.153, 1.155, 1.155, 1.155]
    elif n == 4:
        return [1.425, 1.463, 1.481, 1.492, 1.496]
    elif n == 5:
        return [1.602, 1.672, 1.715, 1.749, 1.764]
    elif n == 6:
        return [1.729, 1.822, 1.887, 1.944, 1.973]
    elif n == 7:
        return [1.828, 1.938, 2.020, 2.097, 2.139]
    elif n == 8:
        return [1.909, 2.032, 2.126, 2.220, 2.274]
    elif n == 9:
        return [1.977, 2.110, 2.215, 2.323, 2.387]
    elif n == 10:
        return [2.036, 2.176, 2.290, 2.410, 2.482]
    elif n == 11:
        return [2.088, 2.234, 2.355, 2.485, 2.564]
    elif n == 12:
        return [2.134, 2.285, 2.412, 2.550, 2.636]
    elif n == 13:
        return [2.175, 2.331, 2.462, 2.607, 2.699]
    elif n == 14:
        return [2.213, 2.371, 2.507, 2.659, 2.755]
    elif n == 15:
        return [2.247, 2.409, 2.549, 2.705, 2.806]
    elif n == 16:
        return [2.279, 2.443, 2.585, 2.747, 2.852]
    elif n == 17:
        return [2.309, 2.475, 2.620, 2.785, 2.894]
def Outliers_Remover(lst):
    length = len(lst)
    lst = lst
    mark = []
    for i in range(0, length):
        n = Gi(lst[i], lst)
        if n > Grubbs_Table(len(lst))[0]:
            mark.append(i)
    for j in mark:
        lst.pop(j)
    return lst
def azimuthAngle( x1,  y1,  x2,  y2):
    # 计算方位角函数
    angle = 0.0
    dx = x2 - x1
    dy = y2 - y1
    if  x2 == x1:
        angle = math.pi / 2.0
        if  y2 == y1 :
            angle = 0.0
        elif y2 < y1 :
            angle = 3.0 * math.pi / 2.0
    elif x2 > x1 and y2 > y1:
        angle = math.atan(dy / dx)
    elif  x2 > x1 and  y2 < y1 :
        angle = math.pi / 2 + math.atan(-dy / dx)
    elif  x2 < x1 and y2 < y1 :
        angle = math.pi + math.atan(dy / dx)
    elif  x2 < x1 and y2 > y1 :
        angle = 3.0 * math.pi / 2.0 + math.atan(dy / -dx)
    return angle * 180 / math.pi
def Converter_Radian_To_Angle(radian):
    return radian / 2 / math.pi * 360
def Converter_Gradient_To_Angle(gradient):
    return Converter_Radian_To_Angle(math.atan(gradient))
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
def Narcissistic_Number_Judge(number):
    if type(number) != int:
        helper.ExitMSG_Return("Narcissistic_Number_Judge(number)", "number必须为int型")

    number_length = Number_Figure(number)
    number_lst = helper.Number_Separate(number)
    for i in range(0, len(number_lst)):
        number_lst[i] = number_lst[i] ** number_length
    return sum(number_lst) == number
def Average_IncreaseNum(List):
    Average_Increase_Num = 0
    for i in range(0 , len(List)-1):
        Increase_Num = List[i + 1] - List[i]
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
    # NotEnoughDays = 0  # 还剩多少天
    DayNum_PerBox = Pills_PerBox * PillsNum_PerDay  # 一盒药能吃 多少 天

    Box_Num_List = []

    Circle_Limite = 0

    for i in helper.Range(1, Times):
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
def Relevance_BT_Two_List_HanStyle(list_1, list_2, calc_way = Relevance_BT_Two_List_Enum.calc_way_math, outliers_remove = True):
    lst_1 = list_1
    lst_2 = list_2
    gradient_list_1 = []
    gradient_list_2 = []
    gradient_1_angel = 0
    gradient_2_angel = 0
    relevance = 0

    if outliers_remove:
        for j1 in range(0, len(lst_1)):
            gi_n_1 = Gi(lst_1[j1], lst_1)
            if gi_n_1 > Grubbs_Table(len(lst_1))[0]:
                lst_1.pop(j1)
        for j2 in range(0, len(lst_2)):
            gi_n_1 = Gi(lst_2[j2], lst_2)
            if gi_n_1 > Grubbs_Table(len(lst_2))[0]:
                lst_2.pop(j2)

    for i1 in helper.Range(0, len(lst_1)-2):
        gradient_single_1 = lst_1[i1 + 1] - lst_1[i1]
        gradient_list_1.append(gradient_single_1)
    for i2 in helper.Range(0, len(lst_2)-2):
        gradient_single_2 = lst_2[i2 + 1] - lst_2[i2]
        gradient_list_2.append(gradient_single_2)

    gradient_1 = Average_Number(gradient_list_1)
    gradient_2 = Average_Number(gradient_list_2)

    if calc_way == Relevance_BT_Two_List_Enum.calc_way_math:
        if gradient_1 == 0:
            gradient_1 = MathConstant_UltiLowNum
        if gradient_2 == 0:
            gradient_2 = MathConstant_UltiLowNum
        g1_abs = abs(gradient_1)
        g2_abs = abs(gradient_2)
        biggest = Biggest_Number([g1_abs, g2_abs])
        minimun = Minimun_Number([g1_abs, g2_abs])
        relevance = 1 - ((biggest - minimun) / biggest)
    elif calc_way == Relevance_BT_Two_List_Enum.calc_way_angle:
        gradient_1_angel = Converter_Gradient_To_Angle(gradient_1)
        gradient_2_angel = Converter_Gradient_To_Angle(gradient_2)
        if gradient_1_angel > 270:
            gradient_1_angel -= 360
        elif gradient_1_angel > 90:
            gradient_1_angel -= 180
        if gradient_2_angel > 270:
            gradient_2_angel -= 360
        elif gradient_2_angel > 90:
            gradient_2_angel -= 180

        relevance = 1 - (abs(gradient_1_angel - gradient_2_angel) / 360)

    if outliers_remove:
        print("去除极端值的列表1：", lst_1)
        print("去除极端值的列表2：", lst_2)
    else:
        print("列表1：", lst_1)
        print("列表2：", lst_2)
    print("列表1的各位之间的斜率列表", gradient_list_1)
    print("列表2的各位之间的斜率列表", gradient_list_2)
    print("列表1的平均斜率：%.2f" %gradient_1)
    print("列表2的平均斜率：%.2f" %gradient_2)
    if calc_way == Relevance_BT_Two_List_Enum.calc_way_angle:
        print("列表1的平均斜率的角度：%.2f" % gradient_1_angel)
        print("列表2的平均斜率的角度：%.2f" % gradient_2_angel)

    return relevance
def Pearson_Correlation_Coefficient(list_1, list_2):
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

    X_A = Average_Number(X)
    Y_A = Average_Number(Y)
    XY_A = Average_Number(XY)
    X2_A = Average_Number(X2)
    Y2_A = Average_Number(Y2)

    R = (XY_A - X_A*Y_A) / ((X2_A - X_A**2)**(1/2) * (Y2_A - Y_A**2)**(1/2))

    return R
def Similarity_BTwen_Two_Number(num1, num2, rAnge):
    rAnge = 10 ** rAnge
    if rAnge < abs(num1 - num2):
        helper.ExitMSG_Return("Similarity_BTwen_Two_Number(num1, num2, range)", "range的数值必须大于（num1-num2）的绝对值")
    distance = abs(num1 - num2)
    return (rAnge - distance) / rAnge
def Pearson_Correlation_Coefficient_Judge_CN(r):
    if 0.8 <= r <= 1.0:
        return "极强正相关"
    elif 0.6 <= r < 0.8:
        return "强正相关"
    elif 0.4 <= r < 0.6:
        return "中等程度正相关"
    elif 0.2 <= r < 0.4:
        return "弱正相关"
    elif 0.0 < r < 0.2:
        return "极弱正相关"
    elif r == 0.0:
        return "无相关"
    elif -0.2 <= r < 0.0:
        return "极弱负相关"
    elif -0.4 <= r < -0.2:
        return "弱负相关"
    elif -0.6 <= r < -0.4:
        return "中等程度弱负相关"
    elif -0.8 <= r < -0.6:
        return "强负相关"
    elif -1.0 <= r < -0.8:
        return "极强负相关"
def cosine_similarity(list_1, list_2):
    length = len(list_1)
    upper = 0

    for i in range(0, length):
        upper += list_1[i] * list_2[i]
        # print(upper)

    lower_left = 0
    for num in list_1:
        lower_left += num ** 2
        # print(lower_left)

    lower_right = 0
    for num in list_2:
        lower_right += num ** 2
        # print(lower_right)

    lower_left = lower_left ** (1 / 2)
    lower_right = lower_right ** (1 / 2)

    return upper / (lower_left * lower_right)
def Quadratic_Equation_Solve(a, b, c):
    x1 = (((b ** 2) - (4 * a * c)) ** (1 / 2) - b) / (2 * a)
    x2 = -(((b ** 2) - (4 * a * c)) ** (1 / 2) + b) / (2 * a)
    if x1 == x2:
        return x1
    return [x1, x2]


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
        # self.sort = Bucket_Sort(hclist)
        self.sort = sorted(hclist)
class ArithmeticProgressionList:
    def __init__(self, a1, d):
        self.a1 = a1
        self.d = d
        self.tempMap_an = {}
        self.tempMap_Sn = {}
    def an(self, n):
        for key in self.tempMap_an.keys():
            getValue = self.tempMap_an.get(key)
            if key == n:
                return getValue
        an = Arithmetic_Progression(self.a1, self.d, n, result_flag=Arithmetic_Progression_Enum.an)
        self.tempMap_an.update({n: an})
        return an
    def Sn(self, n):
        for key in self.tempMap_Sn.keys():
            getValue = self.tempMap_Sn.get(key)
            if key == n:
                return getValue
        an = Arithmetic_Progression(self.a1, self.d, n, result_flag=Arithmetic_Progression_Enum.Sn)
        self.tempMap_Sn.update({n: an})
        return an
class GeometricProgressionList:
    def __init__(self, a1, q):
        self.a1 = a1
        self.q = q
        self.tempMap_an = {}
        self.tempMap_Sn = {}
    def an(self, n):
        for key in self.tempMap_an.keys():
            getValue = self.tempMap_an.get(key)
            if key == n:
                return getValue
        an = Geometric_Progression(self.a1, self.q, n, result_flag=Geometric_Progression_Enum.an)
        self.tempMap_an.update({n: an})
        return an
    def Sn(self, n):
        for key in self.tempMap_Sn.keys():
            getValue = self.tempMap_Sn.get(key)
            if key == n:
                return getValue
        Sn = Geometric_Progression(self.a1, self.q, n, result_flag=Geometric_Progression_Enum.Sn)
        self.tempMap_Sn.update({n: Sn})
        return Sn
