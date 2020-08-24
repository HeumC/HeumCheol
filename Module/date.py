from Module import mAth
from Module import time
from Module import helper

Chinese_Zodiac_Signs_List = ['鼠' , '牛' , '虎' , '兔' , '龙' , '蛇' , '马' , '羊' , '猴' , '鸡' , '狗' , '猪']

#Date函数
def DayInWeek_ENTransToMath(Day):
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
def DayInWeek_MathTransToCN(Day_Num):
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
def Month_TransToMath(Month = ""):
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
def Leap_Year_Judge(Year):
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
def CalcDays_InMonth(Month , Year = 1999):
    if Month == 2:
        if Leap_Year_Judge(Year):
            return 29
        else:
            return 28
    elif 1 <= Month <= 7:
        if (Month):
            return 31
        elif mAth.Even_Judge(Month):
            return 30
    elif 8 <= Month <= 12:
        if mAth.Odd_Judge(Month):
            return 30
        elif mAth.Even_Judge(Month):
            return 31
def CalcDays_BTwen_TwoDatas(Year1 , Month1 , Day1 , Year2 , Month2 , Day2):
    if Year1 == Year2 and Month1 == Month2 and Day1 == Day2:
        return 0
    BTwenDays = 0
    if Year1 == Year2:
        if Month1 == Month2:
            BTwenDays += Day2 - Day1
            return BTwenDays
        else:
            BTwenDays += CalcDays_InMonth(Month1 , Year1) - Day1
            if Month2 == Month1 + 1:
                BTwenDays += Day2
            else:
                for M in helper.Helper_Range(Month1 + 1, Month2 - 1):
                    BTwenDays += CalcDays_InMonth(M, Year1)
                BTwenDays += Day2
            return BTwenDays
    else:
        BTwenDays += CalcDays_InMonth(Month1, Year1) - Day1
        if Month1 == 12:
            pass
        else:
            for M1 in helper.Helper_Range(Month1 + 1, 12):
                BTwenDays += CalcDays_InMonth(M1, Year1)
            if Year2 == Year1 + 1:
                pass
            else:
                for Y1 in helper.Helper_Range(Year1 + 1, Year2 - 1):
                    if Leap_Year_Judge(Y1):
                        BTwenDays += 366
                    else:
                        BTwenDays += 365
        if Month2 == 1:
            pass
        else:
            for M2 in helper.Helper_Range(1, Month2 - 1):
                BTwenDays += CalcDays_InMonth(M2, Year2)
            BTwenDays += Day2
        return BTwenDays
def CalcDays_InLifeTime(Birthday_Y , Birthday_M , Birthday_D):
    Now_Year = int(time.CurrentTime()[20] + time.CurrentTime()[21] + time.CurrentTime()[22] + time.CurrentTime()[23])
    Now_Month = Month_TransToMath(time.CurrentTime()[4] + time.CurrentTime()[5] + time.CurrentTime()[6])
    Now_Day = int(time.CurrentTime()[8] + time.CurrentTime()[9])

    BTwenDays = CalcDays_BTwen_TwoDatas(Birthday_Y , Birthday_M , Birthday_D , Now_Year , Now_Month , Now_Day)
    return BTwenDays

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
    RightFlag = False
    for i in Chinese_Zodiac_Signs_List:
        if CZS == i:
            RightFlag = True
    if RightFlag:
        Returm_Temp_List = []
        while True:
            if Chinese_Zodiac_Signs_Calc(StartYear) == CZS:
                Returm_Temp_List.append(StartYear)
                for i in range(1 , Number + 1):
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