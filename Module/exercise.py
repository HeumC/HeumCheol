from enum import Enum , unique
@unique

class Exercise_Enum(Enum):
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
def Exercise_MIS_EnumToMath(MIS_Enum):
    if MIS_Enum == Exercise_Enum.MIS_LEVEL_1:
        return 1.0
    elif MIS_Enum == Exercise_Enum.MIS_LEVEL_2:
        return 1.2
    elif MIS_Enum == Exercise_Enum.MIS_LEVEL_3:
        return 1.4
    elif MIS_Enum == Exercise_Enum.MIS_LEVEL_4:
        return 1.6
    elif MIS_Enum == Exercise_Enum.MIS_LEVEL_5:
        return 1.8
    elif MIS_Enum == Exercise_Enum.MIS_LEVEL_6:
        return 2.0
def Exercise_Sex_EnumToCN(Sex_Enum):
    if Sex_Enum == Exercise_Enum.SEX_MALE:
        return "男"
    elif Sex_Enum == Exercise_Enum.SEX_FEMALE:
        return "女"
def Exercise_Morphy_EnumToCN(Morpy_Enum):
    if Morpy_Enum == Exercise_Enum.MORPHY_ECTOMORPHY:
        return "外胚型"
    elif Morpy_Enum == Exercise_Enum.MORPHY_MESOMORPHY:
        return "中胚型"
    elif Morpy_Enum == Exercise_Enum.MORPHY_ENDOMORPHY:
        return "内胚型"

#判断函数
def Exercise_Healthy_Weight_Judge_By_BMI(BMI , Language = 'Chinese'):
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
    return 'Unknown Error'

#初步计算函数
def Exercise_BMI_Calc(Height_CM, Weight_KG):
    Height_CM /= 100
    BMI = Weight_KG / (Height_CM ** 2)
    return BMI
def Exercise_BFR_Calc(Height_CM, Weight_KG, Age_Year, Sex):
    BMI = Exercise_BMI_Calc(Height_CM, Weight_KG)
    BFR_Sex_Factor = 0
    if Sex == Exercise_Enum.SEX_MALE:
        BFR_Sex_Factor = 1
    elif Sex == Exercise_Enum.SEX_FEMALE:
        BFR_Sex_Factor = 0

    BFR = 1.2 * BMI + 0.23 * Age_Year - 5.4 - 10.8 * BFR_Sex_Factor
    return BFR

def Exercise_Healthy_Weight_Calc_By_Height(Height_CM):
    Height_CM /= 100
    Weight_List = []
    Weight_List.append(18.5 * (Height_CM ** 2))
    Weight_List.append(23.9 * (Height_CM ** 2))
    return Weight_List
def Exercise_BasalMetabolism_Calc(Height_CM , Weight_KG , Age_Year , Sex):
    if Sex == Exercise_Enum.SEX_MALE:
        BM = 66 + 13.7 * Weight_KG + 5 * Height_CM - 6.8 * Age_Year
        return BM
    elif Sex == Exercise_Enum.SEX_FEMALE:
        BM = 655 + 9.6 * Weight_KG + 1.7 * Height_CM - 4.7 * Age_Year
        return BM
    else:
        return 'Sex Unknown'

#次步计算函数
def Exercise_DailyEnergyExpenditure_Calc(Height_CM , Weight_KG , Age_Year , MIS , Sex):
    BM = float(Exercise_BasalMetabolism_Calc(Height_CM , Weight_KG , Age_Year , Sex))
    if MIS == Exercise_Enum.MIS_LEVEL_1:
        return BM * 1.0
    elif MIS == Exercise_Enum.MIS_LEVEL_2:
        return BM * 1.2
    elif MIS == Exercise_Enum.MIS_LEVEL_3:
        return BM * 1.4
    elif MIS == Exercise_Enum.MIS_LEVEL_4:
        return BM * 1.6
    elif MIS == Exercise_Enum.MIS_LEVEL_5:
        return BM * 1.8
    elif MIS == Exercise_Enum.MIS_LEVEL_6:
        return BM * 2.0
def Exercise_DailyCalorieIntake_Reducedfat_Calc(Height_CM , Weight_KG , Age_Year , MIS , Morphy, Sex):
    if Morphy == Exercise_Enum.MORPHY_ECTOMORPHY:
        return Exercise_DailyEnergyExpenditure_Calc(Height_CM, Weight_KG, Age_Year, MIS, Sex) * 0.9
    elif Morphy == Exercise_Enum.MORPHY_MESOMORPHY:
        return Exercise_DailyEnergyExpenditure_Calc(Height_CM, Weight_KG, Age_Year, MIS, Sex) * 0.8
    elif Morphy == Exercise_Enum.MORPHY_ENDOMORPHY:
        return Exercise_DailyEnergyExpenditure_Calc(Height_CM, Weight_KG, Age_Year, MIS, Sex) * 0.8
def Exercise_DailyCalorieIntake_IncreaseMuscle_Calc(Height_CM , Weight_KG , Age_Year , MIS , Sex):
    return Exercise_DailyEnergyExpenditure_Calc(Height_CM, Weight_KG, Age_Year, MIS, Sex) + 300
def Exercise_CalorieIntake_Distribution_Of_Three_Meals(DailyCalorieIntake , MIS):
    DailyCalorieIntake_List = []
    if MIS == Exercise_Enum.MIS_LEVEL_1:
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
def Exercise_RecommendedWeight_Ratio(RecommendedWeight_Average , Weight):
    return ((Weight - RecommendedWeight_Average) / RecommendedWeight_Average) * 100

#详细信息展示函数
def Exercise_Morphy_Show():
    print('外胚型 : Ectomorphy')
    print('中胚型 : Mesomorphy')
    print('内胚型 : Endomorphy')
def Exercise_MIS_Show():
    print('MIS = 1.0 : 什么都不干（睡觉看电视打游戏）')
    print('MIS = 1.2 : 只进行正常的学习工作，不运动')
    print('MIS = 1.4 : 学习工作外，适量运动（跑步溜完）')
    print('MIS = 1.6 : 非体力活职业，但每天规律举铁训练')
    print('MIS = 1.8 : 体力活职业 + 规律训练或一天两练')
    print('MIS = 2.0 : 超繁重体力活职业 + 高强度训练')

class Exercise_Human:
    def __init__(self , Name , Height_CM , Weight_KG , Age_Year , Sex , MIS , Morphy , Target = 'Default'):
        self.Name = Name
        self.Height = Height_CM
        self.Weight = Weight_KG
        self.Age = Age_Year
        self.Sex = Sex
        self.MIS = MIS
        self.Morphy = Morphy
        self.Target = Target

        self.BMI = Exercise_BMI_Calc(self.Height, self.Weight)
        self.BFR = Exercise_BFR_Calc(self.Height, self.Weight, self.Age, self.Sex)
        self.HealthyWeightJudge = Exercise_Healthy_Weight_Judge_By_BMI(self.BMI)
        self.BasalMetabolism = Exercise_BasalMetabolism_Calc(self.Height, self.Weight, self.Age, self.Sex)
        self.DailyEnergyExpenditure = Exercise_DailyEnergyExpenditure_Calc(self.Height, self.Weight, self.Age, self.MIS,
                                                                           self.Sex)
        if self.Target == Exercise_Enum.TARGET_DEFAULT:
            self.DailyCalorieIntake = Exercise_DailyEnergyExpenditure_Calc(self.Height, self.Weight, self.Age, self.MIS,
                                                                           self.Sex)
        elif self.Target == Exercise_Enum.TARGET_REDUCE_FAT:
            self.DailyCalorieIntake = Exercise_DailyCalorieIntake_Reducedfat_Calc(self.Height, self.Weight, self.Age, self.MIS,
                                                                           self.Morphy, self.Sex)
        elif self.Target == Exercise_Enum.TARGET_INCREASE_MUSCLE:
            self.DailyCalorieIntake = Exercise_DailyCalorieIntake_IncreaseMuscle_Calc(self.Height, self.Weight,
                                                                                      self.Age, self.MIS, self.Sex)

        self.RecommendedWeight_Lowest = Exercise_Healthy_Weight_Calc_By_Height(self.Height)[0]
        self.RecommendedWeight_Highest = Exercise_Healthy_Weight_Calc_By_Height(self.Height)[1]
        self.RecommendedWeight_Average = (Exercise_Healthy_Weight_Calc_By_Height(self.Height)[0] +
                                          Exercise_Healthy_Weight_Calc_By_Height(self.Height)[1]) / 2

        self.RecommendeWeight_Ratio = Exercise_RecommendedWeight_Ratio(self.RecommendedWeight_Average , self.Weight)

        if self.Weight < self.RecommendedWeight_Lowest:
            self.Weight_NeedToChange = -(self.RecommendedWeight_Lowest - self.Weight)
        elif self.Weight > self.RecommendedWeight_Highest:
            self.Weight_NeedToChange = self.Weight - self.RecommendedWeight_Highest
        else:
            self.Weight_NeedToChange = 0

        self.Weight_RecommendToChange = self.Weight - self.RecommendedWeight_Average

        self.CalorieIntake_Breakfast = \
            Exercise_CalorieIntake_Distribution_Of_Three_Meals(self.DailyCalorieIntake, self.MIS)[0]
        self.CalorieIntake_Lunch = \
            Exercise_CalorieIntake_Distribution_Of_Three_Meals(self.DailyCalorieIntake, self.MIS)[1]
        self.CalorieIntake_Dinner = \
            Exercise_CalorieIntake_Distribution_Of_Three_Meals(self.DailyCalorieIntake, self.MIS)[2]

    def Information(self , Precision = Exercise_Enum.INFORMATION_PPRECISON_DEFAULT):
        if Precision == Exercise_Enum.INFORMATION_PPRECISON_DEFAULT:
            print("姓名：%s" % self.Name)
            print("性别：%s" % Exercise_Sex_EnumToCN(self.Sex))
            print("年龄：%d岁" % self.Age)

            if int(self.Weight) == self.Weight:
                print("体重：%d公斤" % self.Weight)
            else:
                print("体重：%.1f公斤" % self.Weight)

            if int(self.Height) == self.Height:
                print("身高：%d厘米" % self.Height)
            else:
                print("身高：%.1f厘米" % self.Height)

            print("胚型：%s" % Exercise_Morphy_EnumToCN(self.Morphy))
            print("运动系数：%.1f" % Exercise_MIS_EnumToMath(self.MIS))
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
        elif Precision == Exercise_Enum.INFORMATION_PPRECISON_HIGH:
            print("姓名：%s" % self.Name)
            print("性别：%s" % Exercise_Sex_EnumToCN(self.Sex))
            print("年龄：%d岁" % self.Age)

            if int(self.Weight) == self.Weight:
                print("体重：%d公斤" % self.Weight)
            else:
                print("体重：%f公斤" % self.Weight)

            if int(self.Height) == self.Height:
                print("身高：%f厘米" % self.Height)
            else:
                print("身高：%f厘米" % self.Height)

            print("胚型：%s" % Exercise_Morphy_EnumToCN(self.Morphy))
            print("运动系数：%f" % Exercise_MIS_EnumToMath(self.MIS))
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