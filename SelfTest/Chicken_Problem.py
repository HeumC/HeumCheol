from HCheol import HCheol_Level1 as FBHS

Before_Data = []

DataNum_Old = 100
DataNum_Predict = 100
DataNum = DataNum_Old + DataNum_Predict

Sell_Lowest_Line = 80
Sell_Highest_Line = 100

ErrorNum_Low = -3
ErrorNum_High = 3


for i in FBHS.Helper_Range(1 , DataNum_Old):
    Before_Data.append(FBHS.random.randint(Sell_Lowest_Line , Sell_Highest_Line))
#print(Before_Data)]
for i in FBHS.Helper_Range(1 , DataNum_Predict):
    Before_Data.append(round(FBHS.Math_Predict_NextNum(Before_Data)) + FBHS.random.randint(ErrorNum_Low, ErrorNum_High))
    #print(Before_Data)
    #print(round(FBHS.Math_Predict_NextNum(Before_Data)))
#$print(Before_Data)
FBHS.Pylab_Plot_Show(FBHS.Helper_MakeList_A_To_B(1 , DataNum) , Before_Data)