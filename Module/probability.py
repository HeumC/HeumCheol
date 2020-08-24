import random
from module import mAth
from module import helper

Coin_HeadOrTail_Probability_Result_HeadList = []
Coin_HeadOrTail_Probability_Result_TailList = []

#Probility函数
def Probability_Coin_HeadOrTail(Frequency , Mode = "H"):
    Zero_Num = 0
    One_Num = 0

    for i in range(1, Frequency + 1):
        rr = random.randint(0, 1)
        if rr == 0:
            Zero_Num += 1.0
            Coin_HeadOrTail_Probability_Result_TailList.append(Zero_Num / i)
            Coin_HeadOrTail_Probability_Result_HeadList.append((One_Num / i))
        elif rr == 1:
            One_Num += 1.0
            Coin_HeadOrTail_Probability_Result_TailList.append(Zero_Num / i)
            Coin_HeadOrTail_Probability_Result_HeadList.append((One_Num / i))

    if Mode == "H":
        return Coin_HeadOrTail_Probability_Result_HeadList
    elif Mode == "T":
        return Coin_HeadOrTail_Probability_Result_TailList
def Probability_RollGun_Continuation(RollGun_SuccessNum , RollGun_AllNum , RollGun_Probability):
    RollGun_SuccessNum = int(RollGun_SuccessNum)
    RollGun_AllNum = int(RollGun_AllNum)
    # 组合C(n,m)=P(n,m)/P(m,m) =n!/m!（n-m）!； n为底数，m为抽取数
    nJ = mAth.MultAll_Int(RollGun_AllNum , 1)
    mJ = mAth.MultAll_Int(RollGun_SuccessNum , 1)
    n_mJ = mAth.MultAll_Int(RollGun_AllNum - RollGun_SuccessNum , 1)
    mp = RollGun_Probability ** RollGun_SuccessNum
    n_mp = (1 - RollGun_Probability) ** (RollGun_AllNum - RollGun_SuccessNum)
    if RollGun_SuccessNum == 0:
        return 0
    elif RollGun_SuccessNum == RollGun_AllNum:
        return mp * n_mp
    else:
        return (nJ / (mJ * n_mJ)) * mp * n_mp
def Probability_RollGun_Single(RollGun_AllNum , RollGun_Probability):
    RG_P_List = []
    for f in helper.Helper_Range(0 , RollGun_AllNum):
        RG_P_List.append(RollGun_Probability * ((1 - RollGun_Probability) ** f))
    return RG_P_List