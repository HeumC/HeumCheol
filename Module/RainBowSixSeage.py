import math

from enum import Enum, unique
@unique

class Gun_Enum(Enum):
    Armor_Level_One = 0
    Armor_Level_Two = 1
    Armor_Level_Three = 2

Armor_Level_One_Reduce_Damage_Ratio = 0.0
Armor_Level_Two_Reduce_Damage_Ratio = 0.1
Armor_Level_Three_Reduce_Damage_Ratio = 0.2
RookArmor_Reduce_Damge_Ratio = 0.2

def Bullet_Damege_Reduce_Ratio_By_RookArmor(Armor_Level):
    BDRR_R = -1
    if Armor_Level == Gun_Enum.Armor_Level_One:
        BDRR_R = (1 - Armor_Level_One_Reduce_Damage_Ratio) * 0.2
    elif Armor_Level == Gun_Enum.Armor_Level_Two:
        BDRR_R = (1 - Armor_Level_Two_Reduce_Damage_Ratio) * 0.2
    elif Armor_Level == Gun_Enum.Armor_Level_Three:
        BDRR_R = (1 - Armor_Level_Three_Reduce_Damage_Ratio) * 0.2
    return BDRR_R
def Bullet_Damege_Reduce_Ratio(Armor_Level, RookArmor):
    BDRR = -1
    if RookArmor == False:
        if Armor_Level == Gun_Enum.Armor_Level_One:
            BDRR = Armor_Level_One_Reduce_Damage_Ratio
        elif Armor_Level == Gun_Enum.Armor_Level_Two:
            BDRR = Armor_Level_Two_Reduce_Damage_Ratio
        elif Armor_Level == Gun_Enum.Armor_Level_Three:
            BDRR = Armor_Level_Three_Reduce_Damage_Ratio
    else:
        BDRR_R = Bullet_Damege_Reduce_Ratio_By_RookArmor(Armor_Level)
        if Armor_Level == Gun_Enum.Armor_Level_One:
            BDRR = Armor_Level_One_Reduce_Damage_Ratio + BDRR_R
        elif Armor_Level == Gun_Enum.Armor_Level_Two:
            BDRR = Armor_Level_Two_Reduce_Damage_Ratio + BDRR_R
        elif Armor_Level == Gun_Enum.Armor_Level_Three:
            BDRR = Armor_Level_Three_Reduce_Damage_Ratio + BDRR_R
    return BDRR
def Firing_Rate_Second_Calc(Firing_Rate_Minute):
    return Firing_Rate_Minute / 60
def Kill_Bullet_Calc(Damage, Armor_Level, RookArmor, Health_Point = 100):
    BDRR = Bullet_Damege_Reduce_Ratio(Armor_Level, RookArmor)
    return math.ceil(Health_Point / (Damage * (1- BDRR)))
def Time_To_Kill_Calc(Damage, Armor_Level, RookArmor, Firing_Rate_Minute, Health_Point = 100):
    Kill_Bullet = Kill_Bullet_Calc(Damage, Armor_Level, RookArmor, Health_Point)
    Firing_Rate_Second = Firing_Rate_Second_Calc(Firing_Rate_Minute)

    TTK = (Kill_Bullet - 1) / Firing_Rate_Second
    return TTK * 1000
def Head_Of_List():
    print("|%12s|%12s|%12s|%12s" % ("名称".center(12), "类型".center(12), "伤害".center(12), "射速".center(12)), end="")
    print("|%12s|%12s|%12s|%12s|%12s|%12s|" % ("TTK(1-RAF)".center(12), "TTK(2-RAF)".center(12), "TTK(3-RAF)".center(12)
                                               , "TTK(1-RAT)".center(12), "TTK(1-RAT)".center(12),
                                               "TTK(1-RAT)".center(12)))

class Gun:
    def __init__(self, Name, Type,  Damage, Firing_Rate_Minute):
        self.Name = Name
        self.Type = Type
        self.Damage = Damage
        self.Firing_Rate_Minute = Firing_Rate_Minute

        self.KB_For_Armor_Level_One_Without_RookArmor = Kill_Bullet_Calc(self.Damage,
                                                                                   Gun_Enum.Armor_Level_One,
                                                                                   RookArmor=False)
        self.KB_For_Armor_Level_Two_Without_RookArmor = Kill_Bullet_Calc(self.Damage,
                                                                                   Gun_Enum.Armor_Level_Two,
                                                                                   RookArmor=False)
        self.KB_For_Armor_Level_Three_Without_RookArmor = Kill_Bullet_Calc(self.Damage,
                                                                                     Gun_Enum.Armor_Level_Three,
                                                                                     RookArmor=False)
        self.KB_For_Armor_Level_One_With_RookArmor = Kill_Bullet_Calc(self.Damage,
                                                                                Gun_Enum.Armor_Level_One,
                                                                                RookArmor=True)
        self.KB_For_Armor_Level_Two_With_RookArmor = Kill_Bullet_Calc(self.Damage,
                                                                                Gun_Enum.Armor_Level_Two,
                                                                                RookArmor=True)
        self.KB_For_Armor_Level_Three_With_RookArmor = Kill_Bullet_Calc(self.Damage,
                                                                                  Gun_Enum.Armor_Level_Three,
                                                                                  RookArmor=True)

        self.TTK_For_Armor_Level_One_Without_RookArmor = Time_To_Kill_Calc(
            self.Damage,
            Gun_Enum.Armor_Level_One,
            False, self.Firing_Rate_Minute)

        self.TTK_For_Armor_Level_Two_Without_RookArmor = Time_To_Kill_Calc(
            self.Damage,
            Gun_Enum.Armor_Level_Two,
            False, self.Firing_Rate_Minute)

        self.TTK_For_Armor_Level_Three_Without_RookArmor = Time_To_Kill_Calc(
            self.Damage,
            Gun_Enum.Armor_Level_Three,
            False, self.Firing_Rate_Minute)

        self.TTK_For_Armor_Level_One_With_RookArmor = Time_To_Kill_Calc(
            self.Damage,
            Gun_Enum.Armor_Level_One,
            True, self.Firing_Rate_Minute)

        self.TTK_For_Armor_Level_Two_With_RookArmor = Time_To_Kill_Calc(
            self.Damage,
            Gun_Enum.Armor_Level_Two,
            True, self.Firing_Rate_Minute)

        self.TTK_For_Armor_Level_Three_With_RookArmor = Time_To_Kill_Calc(
            self.Damage,
            Gun_Enum.Armor_Level_Three,
            True, self.Firing_Rate_Minute)

    def Information(self):
        print("枪械名称：%s" %self.Name)
        print("枪械类型：%s" % self.Type)
        print("伤害：%d" % self.Damage)
        print("射速(每分钟子弹数)：%s" % self.Firing_Rate_Minute)
        print()
        print("杀死（一甲）（无Rook甲）干员所需的子弹数：%d发" % self.KB_For_Armor_Level_One_Without_RookArmor)
        print("杀死（一甲）（无Rook甲）干员所需的时间：%.2fms" % self.TTK_For_Armor_Level_One_Without_RookArmor)
        print()
        print("杀死（二甲）（无Rook甲）干员所需的子弹数：%d发" % self.KB_For_Armor_Level_Two_Without_RookArmor)
        print("杀死（二甲）（无Rook甲）干员所需的时间：%.2fms" % self.TTK_For_Armor_Level_Two_Without_RookArmor)
        print()
        print("杀死（三甲）（无Rook甲）干员所需的子弹数：%d发" % self.KB_For_Armor_Level_Three_Without_RookArmor)
        print("杀死（三甲）（无Rook甲）干员所需的时间：%.2fms" % self.TTK_For_Armor_Level_Three_Without_RookArmor)
        print()
        print("杀死（一甲）（有Rook甲）干员所需的子弹数：%d发" % self.KB_For_Armor_Level_One_With_RookArmor)
        print("杀死（一甲）（有Rook甲）干员所需的时间：%.2fms" % self.TTK_For_Armor_Level_One_With_RookArmor)
        print()
        print("杀死（二甲）（有Rook甲）干员所需的子弹数：%d发" % self.KB_For_Armor_Level_Two_With_RookArmor)
        print("杀死（二甲）（有Rook甲）干员所需的时间：%.2fms" % self.TTK_For_Armor_Level_Two_With_RookArmor)
        print()
        print("杀死（三甲）（有Rook甲）干员所需的子弹数：%d发" % self.KB_For_Armor_Level_Three_With_RookArmor)
        print("杀死（三甲）（有Rook甲）干员所需的时间：%.2fms" % self.TTK_For_Armor_Level_Three_With_RookArmor)
        print()

    def ArrayInformation(self):
        print("|%13s|%11s|%13s|%12s" % (self.Name.center(13), self.Type.center(11), str(self.Damage).center(13),
                                        str(self.Firing_Rate_Minute).center(14)), end="")
        print("|%12s|%12s|%12s|%12s|%12s|%12s|" % (
            (str(round(self.TTK_For_Armor_Level_One_Without_RookArmor, 2)) + "ms").center(12),
            (str(round(self.TTK_For_Armor_Level_Two_Without_RookArmor, 2)) + "ms").center(12),
            (str(round(self.TTK_For_Armor_Level_Three_Without_RookArmor, 2)) + "ms").center(12)
            , (str(round(self.TTK_For_Armor_Level_One_With_RookArmor, 2)) + "ms").center(12),
            (str(round(self.TTK_For_Armor_Level_Two_With_RookArmor, 2)) + "ms").center(12),
            (str(round(self.TTK_For_Armor_Level_Three_With_RookArmor, 2)) + "ms").center(12)))

def Old_ADS_Trans_To_Y5S3_ADS(oldAds):
    # 1倍镜:原有ADS灵敏度x0.7
    # 1.5倍镜:原有ADS灵敏度x0.9
    # 2.0倍镜:原有ADS灵敏度x1.0
    # 2.5倍镜:原有ADS灵敏度x1.05
    # 3.0倍镜:原有ADS灵敏度x 1.075
    # 4.0倍镜:原有ADS灵敏度x 1.094 
    # 5.0倍镜:原有ADS灵敏度x 1.098 
    # 12.0倍镜:原有ADS灵敏度x 1.099
    scope_10 = oldAds * 0.7
    scope_15 = oldAds * 0.9
    scope_20 = oldAds * 1.0
    scope_25 = oldAds * 1.05
    scope_30 = oldAds * 1.075
    scope_40 = oldAds * 1.094
    scope_50 = oldAds * 1.098
    scope_120 = oldAds * 1.099

    lst = [scope_10, scope_15, scope_20, scope_25, scope_30, scope_40, scope_50, scope_120]
    j = 0
    for i in [1, 1.5, 2.0, 2.5, 3.0, 4.0, 12.0]:
        print("%.1f倍镜的新ADS的值：" %i, end="")
        print(lst[j])
        j += 1
    return lst
# print(Old_ADS_Trans_To_Y5S3_ADS(81))










# Head_Of_List()
# Gun("SMG-11", "自动手枪", 35, 1270).ArrayInformation()
# Gun("C75 Auto", "自动手枪", 35, 1000).ArrayInformation()
#
# Gun("LFP586", " 单发手枪", 78, 450).ArrayInformation()
# Gun("D-50", " 单发手枪", 71, 450).ArrayInformation()
# Gun("PMM", "单发手枪", 61, 450).ArrayInformation()
# Gun("Q-929", "单发手枪", 60, 450).ArrayInformation()
# Gun("M45 MEUSOC", "单发手枪", 58, 450).ArrayInformation()
# Gun("1911 TACOPS", "单发手枪", 55, 450).ArrayInformation()
# Gun("P229", "单发手枪", 51, 450).ArrayInformation()
# Gun("P226 Mk 25", "单发手枪", 50, 450).ArrayInformation()
# Gun(".44麦格农", "单发手枪", 61, 450).ArrayInformation()
# print()
# Gun("L85A2", "突击步枪", 47, 670).ArrayInformation()
# Gun("F2", "突击步枪", 37, 980).ArrayInformation()
# Gun("R4-c", "突击步枪", 39, 860).ArrayInformation()
# Gun("AK12", "突击步枪", 45, 850).ArrayInformation()
# print()
# Gun("417", "精确步枪", 69, 450).ArrayInformation()
# Gun("CAMRS", "精确步枪", 69, 450).ArrayInformation()
# Gun("AR-15 50", "精确步枪", 62, 450).ArrayInformation()
# Gun("SR-25", "精确步枪", 61, 450).ArrayInformation()
# Gun("MK 14 EBR", "精确步枪", 60, 450).ArrayInformation()
# print("###目前写到AK12###")
