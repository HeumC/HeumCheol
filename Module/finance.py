from Module import date
from Module import trans
from Module import pylabHelper

def Profit_Calculator(Capital, Increase_Rate_Per_Year, End_Year = 10):
    lst = []
    for i in range(0, End_Year + 1):
        temp = round(Capital * (1 + Increase_Rate_Per_Year) ** i, 2)
        lst.append(temp)
    return lst
def Profit_Double_Capital_Calculator(Increase_Rate_Per_Year):
    lst = []
    Capital = 1
    i = 0
    while True:
        lst.append(Capital * (1 + Increase_Rate_Per_Year) ** i)
        if lst[i] >= Capital * 2 >= lst[i - 1]:
            return i
        i += 1


for Increase_Rate_Per_Year in range(5, 16):
    Increase_Rate_Per_Year /= 100
    Capital = 3000
    Year = int((date.CalcDays_BTwen_TwoDatas(1999, 5, 17, 2059, 5, 17) - date.CalcDays_InLifeTime(1999, 5, 17)) / 365)
    m_lst = Profit_Calculator(Capital, Increase_Rate_Per_Year, Year)
    print("%.2f元的本金，%.2f%%的年化率，在%d年后一共获得：%.2f元" % (Capital, Increase_Rate_Per_Year * 100, Year, m_lst[len(m_lst) - 1]))

    pylabHelper.Pylab_Plot(m_lst)
pylabHelper.Pylab_Show()

# lst = []
# for i in range(1, 167):
#     year = Profit_Double_Capital_Calculator(i/100)
#     lst.append(year)
#     if year == 1:
#         print("%.2f年化率为翻倍仅需1年" %(i/100))
#         break
# pylabHelper.Pylab_Plot_Show(lst)
