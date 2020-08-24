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


class Gun():
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

Gun("SMG-11", "自动手枪", 35, 1270).Information()
print()
