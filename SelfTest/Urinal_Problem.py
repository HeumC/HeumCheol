from HCheol import HCheol_Level1 as FBHS

Man_Number_List = []
Ratio_List = []

Urinal_Last_Number = 50

for i in FBHS.Helper_Range(1 , Urinal_Last_Number):
    #Man_Number_List.append(FBHS.Math_Urinal_Problem(i))
    Ratio_List.append(FBHS.Math_Urinal_Problem(i) / i)
#print(Man_Number_List)
#FBHS.Pylab_Plot_Show(FBHS.Helper_MakeList_A_To_B(1 , Urinal_Last_Number) , Man_Number_List)
FBHS.Pylab_Plot_Show(FBHS.Helper_MakeList_A_To_B(1 , Urinal_Last_Number) , Ratio_List)