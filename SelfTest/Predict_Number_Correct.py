from HCheol import HCheol_Level1 as FBHS

CrrList = []
Ave_Crr_List = []

Calc_Num = 1000
for i in FBHS.Helper_Range(1 , Calc_Num):
    for j in FBHS.Helper_Range(1, 100):
        Before_Data = []
        for k in FBHS.Helper_Range(1, 100):
            Before_Data.append(FBHS.random.randint(50, 70))
        PN = round(FBHS.Math_Predict_NextNum(Before_Data))
        RI = FBHS.random.randint(50, 70)
        Crr = 1 - (abs(PN - RI) / RI)
        CrrList.append(Crr)
        # print("第%d次预测数字：%d" %(i , PN))
        # print("第%d次真正数字：%d" %(i , RI))
        # print("第%d次正确率：%f%%" %(i , Crr * 100))
        # print()

    Ave_Crr = sum(CrrList) / len(CrrList)
    Ave_Crr_List.append(Ave_Crr)
    print("第%d次平均相似率：%f%%" % (i , Ave_Crr * 100))

print("%d次平均相似率的方差：%f" %(Calc_Num , FBHS.Math_Variance(Ave_Crr_List)))
#FBHS.Pylab_Plot_Show(FBHS.Helper_MakeList_A_To_B(1 , len(CrrList)) , CrrList)
FBHS.Pylab_Plot_Show(FBHS.Helper_MakeList_A_To_B(1 , len(Ave_Crr_List)) , Ave_Crr_List)
