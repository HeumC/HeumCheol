import time
import math
import matplotlib.pylab as pyl
import random
import fractions
import sys
import numpy as npy
import sympy
from sympy import *
from collections import Counter

sys.setrecursionlimit(9000000)  # 递归深度提高

FunctionBase_HaS1n_Version = 1.02

MathConstant_Pi = math.pi
MathConstant_e = math.e
MathConstant_UltiLowNum = 0.00000000000000000000000000000000000000000000000000000000001
MathConstant_UltiHighNum = 999999999999999999999999999999999999999999999999999999999999

Coin_HeadOrTail_Probability_Result_HeadList = []
Coin_HeadOrTail_Probability_Result_TailList = []

Chinese_Zodiac_Signs_List = ['鼠' , '牛' , '虎' , '兔' , '龙' , '蛇' , '马' , '羊' , '猴' , '鸡' , '狗' , '猪']
ChineseTime_List = ['子' , '丑' , '寅' , '卯' , '辰' , '巳' , '午' , '未' , '申' , '酉' , '戌' , '亥']

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

#Math函数
def Math_Odd_Judge(Number):
    if Number % 2 == 0:
        return False
    elif Number % 2 == 1:
        return True
    else:
        print("无法判断奇偶")
def Math_Even_Judge(Number):
    if Number % 2 == 0:
        return True
    elif Number % 2 == 1:
        return False
    else:
        print("无法判断奇偶")
def Math_SumAll_Int(start , end):
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
def Math_SumAll_Float(start , end , addNum = 1.0):
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
def Math_MultAll_Int(start , end):
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
def Math_MultAll_Float(start , end , addNum = 1.0):
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
def Math_Circle_Calc_Circumference(r , Precision = 2):
    #Math_Circle_Calc_Circumference(r , Precision = 2):函数：输入半径r值来计算圆的周长
    #使用其Precision所相对应的精度（如为1则pi使用3.1 ， 为2则pi使用3.14）
    #Precision最大为15，超过不报错
    #Precision的默认值为2
    Precision = int(Precision)
    if Precision >= 0:
        Circumference = round(MathConstant_Pi, Precision) * (2 * r)
    else:
        print("Precision无效数字，应大于等于0")
        Circumference = -1
    return Circumference
def Math_Circle_Calc_Space(r , Precision = 2):
    #Math_Circle_Calc_Space(r , Precision = 2)函数：输入半径r值来计算圆的面积
    #使用其Precision所相对应的精度（如为1则pi使用3.1 ， 为2则pi使用3.14）
    #Precision最大为15，超过不报错
    #Precision的默认值为2
    Precision = int(Precision)
    if Precision >= 0:
        Space = round(MathConstant_Pi, Precision) * (r ** 2)
    else:
        print("Precision无效数字，应大于等于0")
        Space = -1
    return Space
def Math_Average_Number(List):
    return sum(List) / len(List)
def Math_Median(List):
    List = sorted(List)
    if len(List) % 2 == 0:
        return (List[int(len(List) / 2 - 1)] + List[int(len(List) / 2 + 1 - 1)]) / 2
    else:
        return List[int((len(List) + 1) / 2) - 1]
def Math_Mode(List):
    x = dict((a, List.count(a)) for a in List)
    y = [k for k, v in x.items() if max(x.values()) == v]
    return y
def Math_Variance(List):
    temp_List = []
    ave = Math_Average_Number(List)
    for num in List:
        temp_List.append(((num - ave) ** 2) / len(List))
    return sum(temp_List)

#Time函数
def Time_Clocks(timeBT):
    #Time_Clocks(timeBT)函数：输入需要多少秒的时钟输出，来输出当前时间
    timeBT = int(timeBT)
    for t in range(timeBT):
        print(time.ctime(time.time()))
        time.sleep(1)
def Time_CountDown(timeBT):
    #Time_CountDown(timeBT)函数，输入需要倒计时多少秒，来进行倒计时
    timeBT = int(timeBT)
    for t in range(timeBT , 0 , -1):
        print(t)
        time.sleep(1)
    print("倒计时结束！")
def Time_CurrentTime():
    #Time_CurrentTime()函数：输出当前时间
    return time.ctime(time.time())
def Time_CurrentTime_CN():
    DayInWeek = Time_CurrentTime()[0] + Time_CurrentTime()[1] + Time_CurrentTime()[2]
    DayInWeek_CN = ""
    Day = Time_CurrentTime()[8] + Time_CurrentTime()[9]
    Month = Time_CurrentTime()[4] + Time_CurrentTime()[5] + Time_CurrentTime()[6]
    Month_Num = 0
    Year = Time_CurrentTime()[20] + Time_CurrentTime()[21] + Time_CurrentTime()[22] + Time_CurrentTime()[23]
    Time = Time_CurrentTime()[11] + Time_CurrentTime()[12] + Time_CurrentTime()[13] + Time_CurrentTime()[14] + \
           Time_CurrentTime()[15] + Time_CurrentTime()[16] + Time_CurrentTime()[17] + Time_CurrentTime()[18]
    if Month == "Jan":
        Month_Num = 1
    elif Month == "Feb":
        Month_Num = 2
    elif Month == "Mar":
        Month_Num = 3
    elif Month == "Apr":
        Month_Num = 4
    elif Month == "May":
        Month_Num = 5
    elif Month == "Jun":
        Month_Num = 6
    elif Month == "Jul":
        Month_Num = 7
    elif Month == "Aug":
        Month_Num = 8
    elif Month == "Sep":
        Month_Num = 9
    elif Month == "Oct":
        Month_Num = 10
    elif Month == "Nov":
        Month_Num = 11
    elif Month == "Dec":
        Month_Num = 12

    if DayInWeek == "Mon":
        DayInWeek_CN = "周一"
    elif DayInWeek == "Tue":
        DayInWeek_CN = "周二"
    elif DayInWeek == "Wed":
        DayInWeek_CN = "周三"
    elif DayInWeek == "Thu":
        DayInWeek_CN = "周四"
    elif DayInWeek == "Fri":
        DayInWeek_CN = "周五"
    elif DayInWeek == "Sat":
        DayInWeek_CN = "周六"
    elif DayInWeek == "Sun":
        DayInWeek_CN = "周日"

    Temp = Year + "年 " + str(Month_Num) + "月 " + Day + "日 " + Time + " " + DayInWeek_CN
    return Temp
def Time_ChineseTime_Transform(Hour , Minute , Second):
    Hour = int(Hour)
    Return_Temp_List = []
    if Hour == 24:
        Hour = 0
    if Hour == 23 or 0 <= Hour < 1:
        Return_Temp_List.append(ChineseTime_List[1 - 1] + "时")
    elif 1 <= Hour < 3:
        Return_Temp_List.append(ChineseTime_List[2 - 1] + "时")
    elif 3 <= Hour < 5:
        Return_Temp_List.append(ChineseTime_List[3 - 1] + "时")
    elif 5<= Hour < 7:
        Return_Temp_List.append(ChineseTime_List[4 - 1] + "时")
    elif 7 <= Hour < 9:
        Return_Temp_List.append(ChineseTime_List[5 - 1] + "时")
    elif 9 <= Hour < 11:
        Return_Temp_List.append(ChineseTime_List[6 - 1] + "时")
    elif 11 <= Hour < 13:
        Return_Temp_List.append(ChineseTime_List[7 - 1] + "时")
    elif 13 <= Hour < 15:
        Return_Temp_List.append(ChineseTime_List[8 - 1] + "时")
    elif 15 <= Hour < 17:
        Return_Temp_List.append(ChineseTime_List[9 - 1] + "时")
    elif 17 <= Hour < 19:
        Return_Temp_List.append(ChineseTime_List[10 - 1] + "时")
    elif 19 <= Hour < 21:
        Return_Temp_List.append(ChineseTime_List[11 - 1] + "时")
    elif 21 <= Hour < 23:
        Return_Temp_List.append(ChineseTime_List[12 - 1] + "时")

    Ke = Minute // 15
    if Ke != 0:
        Return_Temp_List.append(str(Ke) + "刻")
    Zi = (Minute % 15) // 5
    if Zi != 0:
        Return_Temp_List.append(str(Zi) + "字")
    Miao = (Minute % 15) % 5
    if Miao != 0:
        Return_Temp_List.append(str(Miao) + "秒")

    Return_Temp_List.append(str(Second) + "忽")

    return Return_Temp_List

#Date函数
def Date_DayInWeek_ENTransToMath(Day):
    if Day == "Mon":
        return 1
    elif Day == "Tue":
        return 2
    elif Day == "Wed":
        return 3
    elif Day == "Thur":
        return 4
    elif Day == "Fri":
        return 5
    elif Day == "Sat":
        return 6
    elif Day == "Sun":
        return 7
def Date_DayInWeek_MathTransToCN(Day_Num):
    if Day_Num == 1:
        return ["周1" , "星期1"]
    elif Day_Num == 2:
        return ["周2" , "星期2"]
    elif Day_Num == 3:
        return ["周3" , "星期3"]
    elif Day_Num == 4:
        return ["周4" , "星期4"]
    elif Day_Num == 5:
        return ["周5" , "星期5"]
    elif Day_Num == 6:
        return ["周6" , "星期6"]
    elif Day_Num == 7:
        return ["周末" , "星期日"]
def Date_Month_TransToMath(Month = ""):
    if Month == "Jan":
        return 1
    elif Month == "Feb":
        return 2
    elif Month == "Mar":
        return 3
    elif Month == "Apr":
        return 4
    elif Month == "May":
        return 5
    elif Month == "Jun":
        return 6
    elif Month == "Jul":
        return 7
    elif Month == "Aug":
        return 8
    elif Month == "Sep":
        return 9
    elif Month == "Oct":
        return 10
    elif Month == "Nov":
        return 11
    elif Month == "Dec":
        return 12
def Date_Leap_Year_Judge(Year):
    if (Year % 4) == 0:
        if (Year % 100) == 0:
            if (Year % 400) == 0:
                return True # 整百年能被400整除的是闰年
            else:
                return False
        else:
            return True # 非整百年能被4整除的为闰年
    else:
        return False
def Date_CalcDays_InMonth(Month , Year = 1999):
    if Month == 2:
        if Date_Leap_Year_Judge(Year):
            return 29
        else:
            return 28
    elif 1 <= Month <= 7:
        if Math_Odd_Judge(Month):
            return 31
        elif Math_Even_Judge(Month):
            return 30
    elif 8 <= Month <= 12:
        if Math_Odd_Judge(Month):
            return 30
        elif Math_Even_Judge(Month):
            return 31
def Date_CalcDays_BTwen_TwoDatas(Year1 , Month1 , Day1 , Year2 , Month2 , Day2):
    if Year1 == Year2 and Month1 == Month2 and Day1 == Day2:
        return 0
    BTwenDays = 0
    if Year1 == Year2:
        if Month1 == Month2:
            BTwenDays += Day2 - Day1
            return BTwenDays
        else:
            BTwenDays += Date_CalcDays_InMonth(Month1 , Year1) - Day1
            if Month2 == Month1 + 1:
                BTwenDays += Day2
            else:
                for M in Helper_Range(Month1 + 1, Month2 - 1):
                    BTwenDays += Date_CalcDays_InMonth(M, Year1)
                BTwenDays += Day2
            return BTwenDays
    else:
        BTwenDays += Date_CalcDays_InMonth(Month1, Year1) - Day1
        if Month1 == 12:
            pass
        else:
            for M1 in Helper_Range(Month1 + 1, 12):
                BTwenDays += Date_CalcDays_InMonth(M1, Year1)
            if Year2 == Year1 + 1:
                pass
            else:
                for Y1 in Helper_Range(Year1 + 1, Year2 - 1):
                    if Date_Leap_Year_Judge(Y1):
                        BTwenDays += 366
                    else:
                        BTwenDays += 365
        if Month2 == 1:
            pass
        else:
            for M2 in Helper_Range(1, Month2 - 1):
                BTwenDays += Date_CalcDays_InMonth(M2, Year2)
            BTwenDays += Day2
        return BTwenDays
def Date_CalcDays_InLifeTime(Birthday_Y , Birthday_M , Birthday_D):
    Now_Year = int(Time_CurrentTime()[20] + Time_CurrentTime()[21] + Time_CurrentTime()[22] + Time_CurrentTime()[23])
    Now_Month = Date_Month_TransToMath(Time_CurrentTime()[4] + Time_CurrentTime()[5] + Time_CurrentTime()[6])
    Now_Day = int(Time_CurrentTime()[8] + Time_CurrentTime()[9])

    BTwenDays = Date_CalcDays_BTwen_TwoDatas(Birthday_Y , Birthday_M , Birthday_D , Now_Year , Now_Month , Now_Day)
    return BTwenDays

#Pylab函数
def Pylab_Plot(x , y , type = '-'):
    pyl.plot(x, y, type)
def Pylab_Plot_Show(x , y , type = '-'):
    pyl.plot(x, y, type)
    pyl.show()
def Pylab_Hist(data):
    pyl.hist(data)
def Pylab_Hist_Show(data):
    pyl.hist(data)
    pyl.show()
def Pylab_Show():
    pyl.show()

#内部函数
def Auto_Return_DelayMSG(Function_Name_Old = "" , Function_Name_New = ""):
    print("#######################################")
    print(Function_Name_Old , end="")
    print(" 函数名已过期 , 请使用 " , end="")
    print(Function_Name_New)
    print("#######################################")


#下面的函数均为不用的函数，但还是可以使用，只不过会输出此函数名已过期的字样
def Auto_MakeList_AToB(a , b):
    Auto_Return_DelayMSG("Auto_MakeList_AToB(a , b)", "Helper_MakeList_A_To_B(a , b)")
    List = []
    for i in range(a , b + 1):
        List.append(i)
    return List
def Coin_HeadOrTail_Probability(Frequency , Mode = "H"):
    Auto_Return_DelayMSG('Coin_HeadOrTail_Probability(Frequency , Mode = "H")', 'Probability_Coin_HeadOrTail(Frequency , Mode = "H")')
    Zero_Num = 0
    One_Num = 0

    for i in range(1, Frequency + 1):
        rr = random.randint(0, 1)
        if rr == 0:
            Zero_Num += 1.0
            Coin_HeadOrTail_Probability_Result_TailList.append(Zero_Num / i)
            Coin_HeadOrTail_Probability_Result_HeadList.append((One_Num / i))
        elif rr == 1:
            One_Num += 1.0
            Coin_HeadOrTail_Probability_Result_TailList.append(Zero_Num / i)
            Coin_HeadOrTail_Probability_Result_HeadList.append((One_Num / i))

    if Mode == "H":
        return Coin_HeadOrTail_Probability_Result_HeadList
    elif Mode == "T":
        return Coin_HeadOrTail_Probability_Result_TailList