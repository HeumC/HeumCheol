from Module import helper
from enum import Enum , unique
@unique

class Enum(Enum):
    SEX_MALE = 0
    SEX_FEMALE = 1

    MORPHY_ECTOMORPHY = 2
    MORPHY_MESOMORPHY = 3
    MORPHY_ENDOMORPHY = 4

    MIS_LEVEL_1 = 5
    MIS_LEVEL_2 = 6
    MIS_LEVEL_3 = 7
    MIS_LEVEL_4 = 8
    MIS_LEVEL_5 = 9
    MIS_LEVEL_6 = 10

    TARGET_DEFAULT = 11
    TARGET_REDUCE_FAT = 12
    TARGET_INCREASE_MUSCLE = 13

    INFORMATION_PPRECISON_DEFAULT = 14
    INFORMATION_PPRECISON_HIGH = 15

###Exercise函数
#枚举转换函数
def MIS_EnumToMath(MIS_Enum):
    """此函数所接受的变量：
                                       MIS_Enum：枚举类型
                       此函数的作用：
                                       通过运动系数级别枚举，返回其相对应的运动系数，为int型


                       此函数返回值：
                                       MIS：int型"""
    if type(MIS_Enum) != Enum:
        helper.ExitMSG_Return("Exercise_MIS_EnumToMath(MIS_Enum)", "MIS_Enum必须为Exercise_Enum类型")
    if MIS_Enum == Enum.MIS_LEVEL_1:
        return 1.0
    elif MIS_Enum == Enum.MIS_LEVEL_2:
        return 1.2
    elif MIS_Enum == Enum.MIS_LEVEL_3:
        return 1.4
    elif MIS_Enum == Enum.MIS_LEVEL_4:
        return 1.6
    elif MIS_Enum == Enum.MIS_LEVEL_5:
        return 1.8
    elif MIS_Enum == Enum.MIS_LEVEL_6:
        return 2.0
def Sex_EnumToCN(Sex_Enum):
    """此函数所接受的变量：
                                           Sex_Enum：枚举类型
                           此函数的作用：
                                           通过性别枚举，返回其相对应的str型性别，为汉字
                           此函数返回值：
                                           Sex：str型"""
    if type(Sex_Enum) != Enum:
        helper.ExitMSG_Return("Exercise_Sex_EnumToCN(Sex_Enum)", "Sex_Enum必须为Exercise_Enum类型")
    if Sex_Enum == Enum.SEX_MALE:
        return "男"
    elif Sex_Enum == Enum.SEX_FEMALE:
        return "女"
def Morphy_EnumToCN(Morphy_Enum):
    """此函数所接受的变量：
                                               Morpy_Enum：枚举类型
                               此函数的作用：
                                               通过胚型枚举，返回其相对应的str型胚型，为汉字
                               此函数返回值：
                                               Morphy：str型"""
    if type(Morphy_Enum) != Enum:
        helper.ExitMSG_Return("Exercise_Morphy_EnumToCN(Morphy_Enum)", "Morphy_Enum必须为Exercise_Enum型")
    if Morphy_Enum == Enum.MORPHY_ECTOMORPHY:
        return "外胚型"
    elif Morphy_Enum == Enum.MORPHY_MESOMORPHY:
        return "中胚型"
    elif Morphy_Enum == Enum.MORPHY_ENDOMORPHY:
        return "内胚型"

#判断函数
def Healthy_Weight_Judge_By_BMI(BMI , Language = 'Chinese'):
    """此函数所接受的变量：
                                                   BMI：float型
                                                   Language：str型
                                   此函数的作用：
                                                   通过BMI数值判断其体重判断，并返回
                                                   若Language为Chinese，则返回汉字
                                                   若Language为English，则返回英文
                                                   Language默认值为Chinese
                                   此函数返回值：
                                                   BMI_Judge：str型"""
    if type(BMI) == int:
        BMI = float(BMI)
    if type(BMI) != float:
        helper.ExitMSG_Return("Exercise_Healthy_Weight_Judge_By_BMI(BMI , Language = 'Chinese')", "BMI必须为float型或int型")
    if Language == 'Chinese':
        if BMI <= 0:
            return 'BMI数值错误'
        elif BMI < 18.5:
            return '过轻'
        elif 18.5 <= BMI <= 23.9:
            return '正常'
        elif 24 <= BMI <= 27:
            return '过重'
        elif 28 <= BMI <= 32:
            return '肥胖'
        else:
            return '非常肥胖'
    elif Language == 'English':
        if BMI <= 0:
            return 'BMI Error'
        elif BMI < 18.5:
            return 'Underweight'
        elif 18.5 <= BMI <= 23.9:
            return 'Normal'
        elif 24 <= BMI <= 27:
            return 'Overweight'
        elif 28 <= BMI <= 32:
            return 'Fat'
        else:
            return 'Veryfat'
    else:
        return helper.ExitMSG_Return("Exercise_Healthy_Weight_Judge_By_BMI(BMI , Language = 'Chinese')",
                                     "Language必须为Chinese或English")

#初步计算函数
def BMI_Calc(Height_CM, Weight_KG):
    Height_CM /= 100
    BMI = Weight_KG / (Height_CM ** 2)
    return BMI
def BFR_Calc(Height_CM, Weight_KG, Age_Year, Sex):
    BMI = BMI_Calc(Height_CM, Weight_KG)
    BFR_Sex_Factor = 0
    if Sex == Enum.SEX_MALE:
        BFR_Sex_Factor = 1
    elif Sex == Enum.SEX_FEMALE:
        BFR_Sex_Factor = 0

    BFR = 1.2 * BMI + 0.23 * Age_Year - 5.4 - 10.8 * BFR_Sex_Factor
    return BFR
def Heart_Rate_Of_Burning_Fat(Age):
    Max_Heart_Rate = (220-Age)
    return [Max_Heart_Rate * 0.7, Max_Heart_Rate * 0.8]

def Healthy_Weight_Calc_By_Height(Height_CM):
    Height_CM /= 100
    Weight_List = []
    Weight_List.append(18.5 * (Height_CM ** 2))
    Weight_List.append(23.9 * (Height_CM ** 2))
    return Weight_List
def BasalMetabolism_Calc(Height_CM , Weight_KG , Age_Year , Sex):
    if Sex == Enum.SEX_MALE:
        BM = 66 + 13.7 * Weight_KG + 5 * Height_CM - 6.8 * Age_Year
        return BM
    elif Sex == Enum.SEX_FEMALE:
        BM = 655 + 9.6 * Weight_KG + 1.7 * Height_CM - 4.7 * Age_Year
        return BM
    else:
        return 'Sex Unknown'

#次步计算函数
def DailyEnergyExpenditure_Calc(Height_CM , Weight_KG , Age_Year , MIS , Sex):
    BM = float(BasalMetabolism_Calc(Height_CM , Weight_KG , Age_Year , Sex))
    if MIS == Enum.MIS_LEVEL_1:
        return BM * 1.0
    elif MIS == Enum.MIS_LEVEL_2:
        return BM * 1.2
    elif MIS == Enum.MIS_LEVEL_3:
        return BM * 1.4
    elif MIS == Enum.MIS_LEVEL_4:
        return BM * 1.6
    elif MIS == Enum.MIS_LEVEL_5:
        return BM * 1.8
    elif MIS == Enum.MIS_LEVEL_6:
        return BM * 2.0
def DailyCalorieIntake_Reducedfat_Calc(Height_CM , Weight_KG , Age_Year , MIS , Morphy, Sex):
    if Morphy == Enum.MORPHY_ECTOMORPHY:
        return DailyEnergyExpenditure_Calc(Height_CM, Weight_KG, Age_Year, MIS, Sex) * 0.9
    elif Morphy == Enum.MORPHY_MESOMORPHY:
        return DailyEnergyExpenditure_Calc(Height_CM, Weight_KG, Age_Year, MIS, Sex) * 0.8
    elif Morphy == Enum.MORPHY_ENDOMORPHY:
        return DailyEnergyExpenditure_Calc(Height_CM, Weight_KG, Age_Year, MIS, Sex) * 0.8
def DailyCalorieIntake_IncreaseMuscle_Calc(Height_CM , Weight_KG , Age_Year , MIS , Sex):
    return DailyEnergyExpenditure_Calc(Height_CM, Weight_KG, Age_Year, MIS, Sex) + 300
def CalorieIntake_Distribution_Of_Three_Meals(DailyCalorieIntake , MIS):
    DailyCalorieIntake_List = []
    if MIS == Enum.MIS_LEVEL_1:
        CalorieIntake_Breakfast = DailyCalorieIntake * (4 / 10)
        DailyCalorieIntake_List.append(CalorieIntake_Breakfast)
        CalorieIntake_Lunch = DailyCalorieIntake * (4 / 10)
        DailyCalorieIntake_List.append(CalorieIntake_Lunch)
        CalorieIntake_Dinner = DailyCalorieIntake * (2 / 10)
        DailyCalorieIntake_List.append(CalorieIntake_Dinner)
    else:
        CalorieIntake_Breakfast = DailyCalorieIntake * (3 / 10)
        DailyCalorieIntake_List.append(CalorieIntake_Breakfast)
        CalorieIntake_Lunch = DailyCalorieIntake * (4 / 10)
        DailyCalorieIntake_List.append(CalorieIntake_Lunch)
        CalorieIntake_Dinner = DailyCalorieIntake * (3 / 10)
        DailyCalorieIntake_List.append(CalorieIntake_Dinner)
    return DailyCalorieIntake_List
def RecommendedWeight_Ratio(RecommendedWeight_Average , Weight):
    return ((Weight - RecommendedWeight_Average) / RecommendedWeight_Average) * 100

#详细信息展示函数
def Morphy_Show():
    print('外胚型 : Ectomorphy')
    print('中胚型 : Mesomorphy')
    print('内胚型 : Endomorphy')
def MIS_Show():
    print('MIS = 1.0 : 什么都不干（睡觉看电视打游戏）')
    print('MIS = 1.2 : 只进行正常的学习工作，不运动')
    print('MIS = 1.4 : 学习工作外，适量运动（跑步溜完）')
    print('MIS = 1.6 : 非体力活职业，但每天规律举铁训练')
    print('MIS = 1.8 : 体力活职业 + 规律训练或一天两练')
    print('MIS = 2.0 : 超繁重体力活职业 + 高强度训练')

class Human:
    def __init__(self , Name , Height_CM , Weight_KG , Age_Year , Sex , MIS , Morphy , Target = 'Default'):
        self.Name = Name
        self.Height = Height_CM
        self.Weight = Weight_KG
        self.Age = Age_Year
        self.Sex = Sex
        self.MIS = MIS
        self.Morphy = Morphy
        self.Target = Target

        self.BMI = BMI_Calc(self.Height, self.Weight)
        self.BFR = BFR_Calc(self.Height, self.Weight, self.Age, self.Sex)
        self.HealthyWeightJudge = Healthy_Weight_Judge_By_BMI(self.BMI)
        self.BasalMetabolism = BasalMetabolism_Calc(self.Height, self.Weight, self.Age, self.Sex)
        self.DailyEnergyExpenditure = DailyEnergyExpenditure_Calc(self.Height, self.Weight, self.Age, self.MIS,
                                                                           self.Sex)
        if self.Target == Enum.TARGET_DEFAULT:
            self.DailyCalorieIntake = DailyEnergyExpenditure_Calc(self.Height, self.Weight, self.Age, self.MIS,
                                                                           self.Sex)
        elif self.Target == Enum.TARGET_REDUCE_FAT:
            self.DailyCalorieIntake = DailyCalorieIntake_Reducedfat_Calc(self.Height, self.Weight, self.Age, self.MIS,
                                                                           self.Morphy, self.Sex)
        elif self.Target == Enum.TARGET_INCREASE_MUSCLE:
            self.DailyCalorieIntake = DailyCalorieIntake_IncreaseMuscle_Calc(self.Height, self.Weight,
                                                                                      self.Age, self.MIS, self.Sex)

        self.RecommendedWeight_Lowest = Healthy_Weight_Calc_By_Height(self.Height)[0]
        self.RecommendedWeight_Highest = Healthy_Weight_Calc_By_Height(self.Height)[1]
        self.RecommendedWeight_Average = (Healthy_Weight_Calc_By_Height(self.Height)[0] +
                                          Healthy_Weight_Calc_By_Height(self.Height)[1]) / 2

        self.RecommendeWeight_Ratio = RecommendedWeight_Ratio(self.RecommendedWeight_Average , self.Weight)

        if self.Weight < self.RecommendedWeight_Lowest:
            self.Weight_NeedToChange = -(self.RecommendedWeight_Lowest - self.Weight)
        elif self.Weight > self.RecommendedWeight_Highest:
            self.Weight_NeedToChange = self.Weight - self.RecommendedWeight_Highest
        else:
            self.Weight_NeedToChange = 0

        self.Weight_RecommendToChange = self.Weight - self.RecommendedWeight_Average

        self.CalorieIntake_Breakfast = \
            CalorieIntake_Distribution_Of_Three_Meals(self.DailyCalorieIntake, self.MIS)[0]
        self.CalorieIntake_Lunch = \
            CalorieIntake_Distribution_Of_Three_Meals(self.DailyCalorieIntake, self.MIS)[1]
        self.CalorieIntake_Dinner = \
            CalorieIntake_Distribution_Of_Three_Meals(self.DailyCalorieIntake, self.MIS)[2]
        self.Heart_Rate_Of_Burning_Fat_Min = Heart_Rate_Of_Burning_Fat(self.Age)[0]
        self.Heart_Rate_Of_Burning_Fat_Max = Heart_Rate_Of_Burning_Fat(self.Age)[1]

    def Information(self, Precision = Enum.INFORMATION_PPRECISON_DEFAULT):
        if Precision == Enum.INFORMATION_PPRECISON_DEFAULT:
            print("姓名：%s" % self.Name)
            print("性别：%s" % Sex_EnumToCN(self.Sex))
            print("年龄：%d岁" % self.Age)

            if int(self.Weight) == self.Weight:
                print("体重：%d公斤" % self.Weight)
            else:
                print("体重：%.1f公斤" % self.Weight)

            if int(self.Height) == self.Height:
                print("身高：%d厘米" % self.Height)
            else:
                print("身高：%.1f厘米" % self.Height)

            print("胚型：%s" % Morphy_EnumToCN(self.Morphy))
            print("运动系数：%.1f" % MIS_EnumToMath(self.MIS))
            print("身体质量指数(BMI)：%.1f" % self.BMI)
            print("体脂率：%.1f%%" % self.BFR)
            print("基础代谢：%d卡路里" % self.BasalMetabolism)
            print("日常代谢：%d卡路里" % self.DailyEnergyExpenditure)
            print("每日摄取：%d卡路里" % self.DailyCalorieIntake)
            print("早餐应摄入：%d卡路里" % self.CalorieIntake_Breakfast)
            print("午餐应摄入：%d卡路里" % self.CalorieIntake_Lunch)
            print("晚餐应摄入：%d卡路里" % self.CalorieIntake_Dinner)
            print("体重诊断：", self.HealthyWeightJudge)

            if self.RecommendeWeight_Ratio > 0:
                print("体重偏移率：%.2f%%↗" % self.RecommendeWeight_Ratio)
                print("推荐饮食方案：减脂")
            elif self.RecommendeWeight_Ratio < 0:
                print("体重偏移率：%.2f%%↘" % abs(self.RecommendeWeight_Ratio))
                print("推荐饮食方案：增肌")
            else:
                print("体重偏移率：%.2f%%" % self.RecommendeWeight_Ratio)

            print("推荐燃脂心率区间：%d次/分钟~%d次/分钟" %(self.Heart_Rate_Of_Burning_Fat_Min, self.Heart_Rate_Of_Burning_Fat_Max))

            print("推荐体重：%.1f公斤~%.1f公斤" % (self.RecommendedWeight_Lowest, self.RecommendedWeight_Highest))
            print("推荐平均体重：%.1f公斤" % self.RecommendedWeight_Average)

            if self.Weight_NeedToChange > 0:
                print("至少需要减少的体重：%.1f公斤" % self.Weight_NeedToChange)
            elif self.Weight_NeedToChange < 0:
                print("至少需要增加的体重：%.1f公斤" % abs(self.Weight_NeedToChange))
            else:
                print("至少需要增加的体重：%.1f公斤" % self.Weight_NeedToChange)

            if self.Weight_RecommendToChange > 0:
                print("推荐需要减少的体重：%.1f公斤" % self.Weight_RecommendToChange)
            elif self.Weight_RecommendToChange < 0:
                print("推荐需要增加的体重：%.1f公斤" % abs(self.Weight_RecommendToChange))
            else:
                print("推荐需要增加的体重：%.1f公斤" % self.Weight_NeedToChange)
        elif Precision == Enum.INFORMATION_PPRECISON_HIGH:
            print("姓名：%s" % self.Name)
            print("性别：%s" % Sex_EnumToCN(self.Sex))
            print("年龄：%d岁" % self.Age)

            if int(self.Weight) == self.Weight:
                print("体重：%d公斤" % self.Weight)
            else:
                print("体重：%f公斤" % self.Weight)

            if int(self.Height) == self.Height:
                print("身高：%f厘米" % self.Height)
            else:
                print("身高：%f厘米" % self.Height)

            print("胚型：%s" % Morphy_EnumToCN(self.Morphy))
            print("运动系数：%f" % MIS_EnumToMath(self.MIS))
            print("身体质量指数(BMI)：%f" % self.BMI)
            print("体脂率：%f%%" % self.BFR)
            print("基础代谢：%f卡路里" % self.BasalMetabolism)
            print("日常代谢：%f卡路里" % self.DailyEnergyExpenditure)
            print("每日摄取：%f卡路里" % self.DailyCalorieIntake)
            print("早餐应摄入：%f卡路里" % self.CalorieIntake_Breakfast)
            print("午餐应摄入：%f卡路里" % self.CalorieIntake_Lunch)
            print("晚餐应摄入：%f卡路里" % self.CalorieIntake_Dinner)
            print("体重诊断：", self.HealthyWeightJudge)

            if self.RecommendeWeight_Ratio > 0:
                print("体重偏移率：%f%%↗" % self.RecommendeWeight_Ratio)
                print("推荐饮食方案：减脂")
            elif self.RecommendeWeight_Ratio < 0:
                print("体重偏移率：%f%%↘" % abs(self.RecommendeWeight_Ratio))
                print("推荐饮食方案：增肌")
            else:
                print("体重偏移率：%f%%" % self.RecommendeWeight_Ratio)

            print("推荐燃脂心率区间：%d次/分钟~%d次/分钟" % (self.Heart_Rate_Of_Burning_Fat_Min, self.Heart_Rate_Of_Burning_Fat_Max))

            print("推荐体重：%f公斤~%f公斤" % (self.RecommendedWeight_Lowest, self.RecommendedWeight_Highest))
            print("推荐平均体重：%f公斤" % self.RecommendedWeight_Average)

            if self.Weight_NeedToChange > 0:
                print("至少需要减少的体重：%f公斤" % self.Weight_NeedToChange)
            elif self.Weight_NeedToChange < 0:
                print("至少需要增加的体重：%f公斤" % abs(self.Weight_NeedToChange))
            else:
                print("至少需要增加的体重：%f公斤" % self.Weight_NeedToChange)

            if self.Weight_RecommendToChange > 0:
                print("推荐需要减少的体重：%f公斤" % self.Weight_RecommendToChange)
            elif self.Weight_RecommendToChange < 0:
                print("推荐需要增加的体重：%f公斤" % abs(self.Weight_RecommendToChange))
            else:
                print("推荐需要增加的体重：%f公斤" % self.Weight_NeedToChange)