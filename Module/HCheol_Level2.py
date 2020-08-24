import HCheol.HCheol_Level1
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

#Trans函数
def Trans_StrList_To_IntList(nums):
    temp = ''
    rt = []

    Flag_FirstOrNot = True

    for i in nums:
        try:
            i = int(i)
        except BaseException:
            if not Flag_FirstOrNot:
                rt.append(int(temp))
                temp = ''
        else:
            temp += str(i)
            Flag_FirstOrNot = False

    return list(rt)

#Math函数
def Math_Bucket_Sort(lst):
    buckets = [0] * ((max(lst) - min(lst)) + 1)
    for i in range(len(lst)):
        buckets[lst[i] - min(lst)] += 1
    res = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i + min(lst)] * buckets[i]
    return res
def Math_Fibonacci(n):
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
def Math_Average_IncreaseNum(List):
    Average_Increase_Num = 0
    for i in range(1 , len(List)):
        Increase_Num = List[i + 1 - 1] - List[i - 1]
        Average_Increase_Num += Increase_Num / (len(List) - 1)
        #print("第%d次增加的数：%d" %(i + 1 , Increase_Num))
    #print(Average_Increase_Num)
    return Average_Increase_Num
def Math_Predict_NextNum(List):
    return List[len(List) - 1] + Math_Average_IncreaseNum(List)
def Math_Urinal_Problem(Urinal_Number):
    if Urinal_Number % 2 == 0:
        Man_Number = Urinal_Number / 2
        return Man_Number
    elif Urinal_Number % 2 == 1:
        #Man_Number = ((Urinal_Number - 1) / 2) + 1
        Man_Number = (Urinal_Number + 1) / 2
        return Man_Number
def Math_PillsProblem(TimeCircle , Pills_PerBox , PillsNum_PerDay , Times = 3 , Circle_Limite_Flag = False , Circle_Limite_Num = 5):
    #TimeCircle = 365  # 多少 天一个循环
    #Pills_PerBox = 12  # 一个药盒里有 多少 个药
    #PillsNum_PerDay = 1  # 一天吃 多少 个

    ExtraDays = 0  # 吃够一个循环后多出的天数
    NotEnoughDays = 0  # 还剩多少天
    DayNum_PerBox = Pills_PerBox * PillsNum_PerDay  # 一盒药能吃 多少 天

    Box_Num_List = []

    Circle_Limite = 0

    for i in HCheol.HCheol_Level1.Helper_Range(1, Times):
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

#CZS函数
def Chinese_Zodiac_Signs_Calc(Year):
    Year = int(Year)
    if 1996 <= Year <= 2007:
        if Year == 1996:
            return Chinese_Zodiac_Signs_List[1 - 1]
        elif Year == 1997:
            return Chinese_Zodiac_Signs_List[2 - 1]
        elif Year == 1998:
            return Chinese_Zodiac_Signs_List[3 - 1]
        elif Year == 1999:
            return Chinese_Zodiac_Signs_List[4 - 1]
        elif Year == 2000:
            return Chinese_Zodiac_Signs_List[5 - 1]
        elif Year == 2001:
            return Chinese_Zodiac_Signs_List[6 - 1]
        elif Year == 2002:
            return Chinese_Zodiac_Signs_List[7 - 1]
        elif Year == 2003:
            return Chinese_Zodiac_Signs_List[8 - 1]
        elif Year == 2004:
            return Chinese_Zodiac_Signs_List[9 - 1]
        elif Year == 2005:
            return Chinese_Zodiac_Signs_List[10 - 1]
        elif Year == 2006:
            return Chinese_Zodiac_Signs_List[11 - 1]
        elif Year == 2007:
            return Chinese_Zodiac_Signs_List[12 - 1]
    else:
        if Year < 1996:
            while Year < 1996:
                Year += 12
        else:
            while Year > 2007:
                Year += 12
        return Chinese_Zodiac_Signs_Calc(Year)
def Chinese_Zodiac_Signs_Judge_Num(CZS , StartYear , Number = 10):
    StartYear = int(StartYear)
    Number = int(Number)
    for i in Chinese_Zodiac_Signs_List:
        if CZS == i:
            RightFlag = True
    if RightFlag:
        Returm_Temp_List = []
        while True:
            if Chinese_Zodiac_Signs_Calc(StartYear) == CZS:
                Returm_Temp_List.append(StartYear)
                for i in Range(1 , Number):
                    Returm_Temp_List.append(StartYear)
                    StartYear += 12
                return Returm_Temp_List
            StartYear += 1
    else:
        exit("输入了错误的生肖信息")
def Chinese_Zodiac_Signs_Judge_SEYear(CZS , StartYear , EndYear):
    StartYear = int(StartYear)
    EndYear = int(EndYear)
    RightFlag = False
    for i in Chinese_Zodiac_Signs_List:
        if CZS == i:
            RightFlag = True
    if RightFlag:
        Returm_Temp_List = []
        while True:
            if Chinese_Zodiac_Signs_Calc(StartYear) == CZS:
                Returm_Temp_List.append(StartYear)
                while StartYear <= EndYear:
                    Returm_Temp_List.append(StartYear)
                    StartYear += 12
                return Returm_Temp_List
            StartYear += 1
    else:
        exit("输入了错误的生肖信息")

#Probility函数
def Probability_Coin_HeadOrTail(Frequency , Mode = "H"):
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
def Probability_RollGun_Continuation(RollGun_SuccessNum , RollGun_AllNum , RollGun_Probability):
    RollGun_SuccessNum = int(RollGun_SuccessNum)
    RollGun_AllNum = int(RollGun_AllNum)
    # 组合C(n,m)=P(n,m)/P(m,m) =n!/m!（n-m）!； n为底数，m为抽取数
    nJ = HCheol.HCheol_Level1.Math_MultAll_Int(RollGun_AllNum , 1)
    mJ = HCheol.HCheol_Level1.Math_MultAll_Int(RollGun_SuccessNum , 1)
    n_mJ = HCheol.HCheol_Level1.Math_MultAll_Int(RollGun_AllNum - RollGun_SuccessNum , 1)
    mp = RollGun_Probability ** RollGun_SuccessNum
    n_mp = (1 - RollGun_Probability) ** (RollGun_AllNum - RollGun_SuccessNum)
    if RollGun_SuccessNum == 0:
        return 0
    elif RollGun_SuccessNum == RollGun_AllNum:
        return mp * n_mp
    else:
        return (nJ / (mJ * n_mJ)) * mp * n_mp
def Probability_RollGun_Single(RollGun_AllNum , RollGun_Probability):
    RG_P_List = []
    for f in HCheol.HCheol_Level1.Helper_Range(0 , RollGun_AllNum):
        RG_P_List.append(RollGun_Probability * ((1 - RollGun_Probability) ** f))
    return RG_P_List

#内部函数
def Auto_Return_DelayMSG(Function_Name_Old = "" , Function_Name_New = ""):
    print("#######################################")
    print(Function_Name_Old , end="")
    print(" 函数名已过期 , 请使用 " , end="")
    print(Function_Name_New)
    print("#######################################")