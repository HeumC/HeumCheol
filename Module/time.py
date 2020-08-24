import time
ChineseTime_List = ['子' , '丑' , '寅' , '卯' , '辰' , '巳' , '午' , '未' , '申' , '酉' , '戌' , '亥']

def Clocks(timeBT):
    #Time_Clocks(timeBT)函数：输入需要多少秒的时钟输出，来输出当前时间
    timeBT = int(timeBT)
    for t in range(timeBT):
        print(time.ctime(time.time()))
        time.sleep(1)
def CountDown(timeBT):
    #Time_CountDown(timeBT)函数，输入需要倒计时多少秒，来进行倒计时
    timeBT = int(timeBT)
    for t in range(timeBT , 0 , -1):
        print(t)
        time.sleep(1)
    print("倒计时结束！")
def CurrentTime():
    #Time_CurrentTime()函数：输出当前时间
    return time.ctime(time.time())
def CurrentTime_CN():
    DayInWeek = CurrentTime()[0] + CurrentTime()[1] + CurrentTime()[2]
    DayInWeek_CN = ""
    Day = CurrentTime()[8] + CurrentTime()[9]
    Month = CurrentTime()[4] + CurrentTime()[5] +CurrentTime()[6]
    Month_Num = 0
    Year = CurrentTime()[20] + CurrentTime()[21] + CurrentTime()[22] + CurrentTime()[23]
    Time = CurrentTime()[11] + CurrentTime()[12] + CurrentTime()[13] + CurrentTime()[14] + \
           CurrentTime()[15] + CurrentTime()[16] + CurrentTime()[17] + CurrentTime()[18]
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
def ChineseTime_Transform(Hour , Minute , Second):
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
