from HCheol import HCheol_Level1 as FBHS

RollGun_Probability = 0.01
RollGun_AllNum = 10

def Pylab_Info():
    FBHS.pyl.title("The probability of the RollGun development by success number")
    FBHS.pyl.xlabel("Frequency of the RollGun's success number")
    FBHS.pyl.ylabel("Probability of RollGun's probability")

def Singel_Test(rp):
    rpl = []
    rpl.clear()
    for i in FBHS.Helper_Range(1, RollGun_AllNum):
        rpl.append(FBHS.Probability_RollGun_Continuation(i, RollGun_AllNum, rp))
    return rpl

while RollGun_Probability <= 0.49:
    #FBHS.Pylab_Plot(FBHS.Helper_MakeList_A_To_B(1, RollGun_AllNum), Singel_Test(RollGun_Probability))
    FBHS.Pylab_Plot(FBHS.Helper_MakeList_A_To_B(1, RollGun_AllNum), Singel_Test(RollGun_Probability), ".")
    RollGun_Probability += 0.01
    #print(Singel_Test(RollGun_Probability))
#FBHS.Pylab_Plot(FBHS.Helper_MakeList_A_To_B(1, RollGun_AllNum), Singel_Test(RollGun_Probability) , ".")
#FBHS.Pylab_Plot(FBHS.Helper_MakeList_A_To_B(0, RollGun_AllNum), FBHS.Probability_RollGun_Single(RollGun_AllNum , RollGun_Probability))
Pylab_Info()
FBHS.Pylab_Show()