from HCheol import HCheol_Level1 as FBHS

Times = 10000
TimeCircle = 365  # 多少 天一个循环
Pills_PerBox = 1300  # 一个药盒里有 多少 个药
PillsNum_PerDay = 1  # 一天吃 多少 个

'''FBHS.Pylab_Plot(FBHS.Helper_MakeList_A_To_B(1 , Times) ,
                     FBHS.Math_PillsProblem(TimeCircle , Pills_PerBox , PillsNum_PerDay , Times))
FBHS.Pylab_Show()'''

FBHS.Math_PillsProblem(TimeCircle, Pills_PerBox, PillsNum_PerDay, Times, Circle_Limite_Flag=True,
                       Circle_Limite_Num=1)
print()