import time
from Module import mAth
from Module import helper
from enum import Enum, unique

ChineseTime_List = ['子' , '丑' , '寅' , '卯' , '辰' , '巳' , '午' , '未' , '申' , '酉' , '戌' , '亥']
Chinese_Zodiac_Signs_List = ['鼠' , '牛' , '虎' , '兔' , '龙' , '蛇' , '马' , '羊' , '猴' , '鸡' , '狗' , '猪']
# 甲乙丙丁戊己庚辛壬癸
Heavenly_Stems = ["辛", "壬", "癸", "甲", "乙", "丙", "丁", "戊", "己", "庚"]
# 子丑寅卯辰巳午未申酉戌亥
Earthly_Branches = ["酉", "戌", "亥", "子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申"]

@unique

class DayInWeek(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6
class Month(Enum):
    January = 0
    February = 1
    March = 2
    April = 3
    May = 4
    June = 5
    July = 6
    August = 7
    September = 8
    October = 9
    November = 10
    December = 11


#tIme函数
def CurrentTime():
    #Time_CurrentTime()函数：输出当前时间
    return time.ctime(time.time())
def Clocks(timeBT):
    #Time_Clocks(timeBT)函数：输入需要多少秒的时钟输出，来输出当前时间
    if type(timeBT) == int:
        for t in range(timeBT):
            print("第%d次计时：" % (t + 1), end="")
            print(time.ctime(time.time()))
            time.sleep(1)
    else:
        exit("函数错误：\nClocks(timeBT)错误：timeBT必须为int类型")
def CountDown(timeBT):
    #Time_CountDown(timeBT)函数，输入需要倒计时多少秒，来进行倒计时
    if type(timeBT) == int:
        for t in range(timeBT, 0, -1):
            print(t)
            time.sleep(1)
        print("倒计时结束！")
    else:
        exit("函数错误：\nCountDown(timeBT)错误：timeBT必须为int类型")
def NowTime():
    Time = ""
    for i in range(11, 19):
        Time += CurrentTime()[i]
    return Time
def ChineseTime_Transform(Hour , Minute=0 , Second=0):
    if type(Hour) == int and type(Minute) == int and type(Second) == int:
        if Hour < 0 or Hour > 24:
            exit("函数错误：\nChineseTime_Transform(Hour, Minute, Second)错误：Hour的取值范围为[0,24]")
        elif Minute < 0 or Minute > 60:
            exit("函数错误：\nChineseTime_Transform(Hour, Minute, Second)错误：Minute的取值范围为[0,60]")
        elif Second < 0 or Second > 60:
            exit("函数错误：\nChineseTime_Transform(Hour, Minute, Second)错误：Second的取值范围为[0,60]")
        Return_Temp_List = []
        if Hour == 24:
            Hour = 0
        if Hour == 23 or 0 <= Hour < 1:
            Return_Temp_List.append(ChineseTime_List[1 - 1] + "时")
        elif 1 <= Hour < 3:
            Return_Temp_List.append(ChineseTime_List[2 - 1] + "时")
        elif 3 <= Hour < 5:
            Return_Temp_List.append(ChineseTime_List[3 - 1] + "时")
        elif 5 <= Hour < 7:
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

        if Second != 0:
            Return_Temp_List.append(str(Second) + "忽")

        return Return_Temp_List
    elif type(Hour) != int:
        exit("函数错误：\nChineseTime_Transform(Hour, Minute, Second)错误：Hour必须为int型")
    elif type(Minute) != int:
        exit("函数错误：\nChineseTime_Transform(Hour, Minute, Second)错误：Minute必须为int型")
    elif type(Second) != int:
        exit("函数错误：\nChineseTime_Transform(Hour, Minute, Second)错误：Second必须为int型")
    else:
        exit("函数错误：\nChineseTime_Transform(Hour, Minute, Second)错误：未知错误")

#Date函数
def NowYear():
    Year = ""
    for i in range(20, 24):
        Year += CurrentTime()[i]
    return Year
def NowMonth():
    Month = ""
    for i in range(4, 7):
        Month += CurrentTime()[i]
    return Month
def NowDay():
    Day = ""
    for i in range(8, 10):
        Day += CurrentTime()[i]
    return Day
def NowDayInWeek():
    DayInWeek = ""
    for i in range(0, 3):
        DayInWeek += CurrentTime()[i]
    return DayInWeek
def DayInWeek_ENTransToMath_ByEnum(Day):
    if Day == DayInWeek.Monday:
        return 1
    elif Day == DayInWeek.Tuesday:
        return 2
    elif Day == DayInWeek.Wednesday:
        return 3
    elif Day == DayInWeek.Thursday:
        return 4
    elif Day == DayInWeek.Friday:
        return 5
    elif Day == DayInWeek.Saturday:
        return 6
    elif Day == DayInWeek.Sunday:
        return 7
def DayInWeek_ENTransToMath_ByStringType(String_Day):
    if String_Day == "Mon":
        return 1
    elif String_Day == "Tue":
        return 2
    elif String_Day == "Wed":
        return 3
    elif String_Day == "Thu":
        return 4
    elif String_Day == "Fri":
        return 5
    elif String_Day == "Sat":
        return 6
    elif String_Day == "Sun":
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
def Month_TransToMath_ByEnum(month =""):
    if month == Month.January:
        return 1
    elif month == Month.February:
        return 2
    elif month == Month.March:
        return 3
    elif month == Month.April:
        return 4
    elif month == Month.May:
        return 5
    elif month == Month.June:
        return 6
    elif month == Month.July:
        return 7
    elif month == Month.August:
        return 8
    elif month == Month.September:
        return 9
    elif month == Month.October:
        return 10
    elif month == Month.November:
        return 11
    elif month == Month.December:
        return 12
def Month_TransToNum_ByStringType(String_Month):
    if String_Month == "Jan":
        return 1
    elif String_Month == "Feb":
        return 2
    elif String_Month == "Mar":
        return 3
    elif String_Month == "Apr":
        return 4
    elif String_Month == "May":
        return 5
    elif String_Month == "Jun":
        return 6
    elif String_Month == "Jul":
        return 7
    elif String_Month == "Aug":
        return 8
    elif String_Month == "Sep":
        return 9
    elif String_Month == "Oct":
        return 10
    elif String_Month == "Nov":
        return 11
    elif String_Month == "Dec":
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
def YearType_TransToCN(Year):
    if Leap_Year_Judge(Year):
        return "闰"
    elif not Leap_Year_Judge(Year):
        return "平"
def Years_Designated_By_Heavenly_Stems_And_Earthly_Branches(Year):
    heavenly_stems = Heavenly_Stems[(Year % 10) - 1]
    earthly_branches = Earthly_Branches[(Year % 12) - 1]
    return heavenly_stems + earthly_branches
def CurrentTime_CN():
    day_in_week = NowDayInWeek()
    DayInWeek_CN = DayInWeek_MathTransToCN(DayInWeek_ENTransToMath_ByStringType(day_in_week))[1]
    Day = NowDay()
    month = NowMonth()
    Month_Num = Month_TransToNum_ByStringType(month)
    Year = NowYear()
    Time = NowTime()
    Year_Type = YearType_TransToCN(int(Year))
    HSEB_YearType = Years_Designated_By_Heavenly_Stems_And_Earthly_Branches(int(Year))

    Temp = Year + "年(" + Year_Type + ") " + HSEB_YearType + "年 " + str(Month_Num) + "月 " + Day + "日 " + Time + " " + DayInWeek_CN
    return Temp
def CalcDays_InMonth(month, Year = 1999):
    if month == 2:
        if Leap_Year_Judge(Year):
            return 29
        else:
            return 28
    elif 1 <= month <= 7:
        if mAth.Odd_Judge(month):
            return 31
        elif mAth.Even_Judge(month):
            return 30
    elif 8 <= month <= 12:
        if mAth.Odd_Judge(month):
            return 30
        elif mAth.Even_Judge(month):
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
                for M in helper.Range(Month1 + 1, Month2 - 1):
                    BTwenDays += CalcDays_InMonth(M, Year1)
                BTwenDays += Day2
            return BTwenDays
    else:
        BTwenDays += CalcDays_InMonth(Month1, Year1) - Day1
        if Month1 == 12:
            pass
        else:
            for M1 in helper.Range(Month1 + 1, 12):
                BTwenDays += CalcDays_InMonth(M1, Year1)
            if Year2 == Year1 + 1:
                pass
            else:
                for Y1 in helper.Range(Year1 + 1, Year2 - 1):
                    if Leap_Year_Judge(Y1):
                        BTwenDays += 366
                    else:
                        BTwenDays += 365
        if Month2 == 1:
            pass
        else:
            for M2 in helper.Range(1, Month2 - 1):
                BTwenDays += CalcDays_InMonth(M2, Year2)
            BTwenDays += Day2
        return BTwenDays
def CalcDays_InLifeTime(Birthday_Y , Birthday_M , Birthday_D):
    Now_Year = int(NowYear())
    Now_Month = Month_TransToNum_ByStringType(NowMonth())
    Now_Day = int(NowDay())

    BTwenDays = CalcDays_BTwen_TwoDatas(Birthday_Y , Birthday_M , Birthday_D , Now_Year , Now_Month , Now_Day)
    return BTwenDays

#CZS函数
def Chinese_Zodiac_Signs_Calc(Year):
    if type(Year) != int:
        exit("函数错误：\nChinese_Zodiac_Signs_Calc(Year)错误：Year须为Int型")
    elif 1996 <= Year <= 2007:
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
