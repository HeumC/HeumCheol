from HCheol import HCheol_Level1 as FBHS

Test_Num = 100
FBHS.Coin_HeadOrTail_Probability(Test_Num)
#FBHS.Pylab_Plot_Show(FBHS.Auto_MakeList_AToB(1 , Test_Num) , FBHS.Coin_HeadOrTail_Probability_Result_HeadList)
#FBHS.Pylab_Plot_Show(FBHS.Auto_MakeList_AToB(1 , Test_Num) , FBHS.Coin_HeadOrTail_Probability_Result_TailList)
FBHS.Pylab_Plot(FBHS.Auto_MakeList_AToB(1 , Test_Num) , FBHS.Coin_HeadOrTail_Probability_Result_HeadList)
FBHS.Pylab_Plot(FBHS.Auto_MakeList_AToB(1 , Test_Num) , FBHS.Coin_HeadOrTail_Probability_Result_TailList)
FBHS.pyl.title("The Probability of the Head and Tail of Coin")
FBHS.pyl.xlabel("Frequency of Flipping Coin")
FBHS.pyl.ylabel("Probability of Head and Tail of Coin")
FBHS.Pylab_Show()
