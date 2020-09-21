HeumCheol模块
===========================

###########部署步骤
1. 将HeumCheol文件夹下的Module部分放在您所创建的Python工程源文件夹下
2. 然后用过正常导入模块，来使用本模块

###########注意事项
1. Module文件夹下的文件才是模块文件，SelfTest下的文件则是为了测试模块所写的代码  
2. 由于本模块处于第一次测试阶段，所以会有一些意想不到的bug，请谅解，之后会排除掉这些
    bug并优化模块

###########目录结构描述

* Module
  * date
  * helper
  * mAth
  * probability
  * pylabHelper
  * RainBowSixSeage
  * time
  * trans
* SelfTest
  * Chicken_Problem
  * Coin_Simulation
  * CreatePY
  * CZS_Test1
  * deciphering
  * Drug_Test1
  * Exercise_Test1
  * FirstPY
  * Han_Math_Pi
  * Han_MathTest
  * Predict_Number_Correct
  * RollGun
  * Urinal_Problem
* README



###########V1.0.0 版本内容  
1. date模块
   * DayInWeek_ENTransToMath(Day)[^date1]
   * DayInWeek_MathTransToCN(Day_Num)[^date2]
   * Month_TransToMath(Month = "")[^date3]
   * Leap_Year_Judge(Year)[^date4]
   * CalcDays_InMonth(Month, Year=1999)[^date5]
   * CalcDays_BTwen_TwoDatas(Year1 , Month1 , Day1 , Year2 , Month2 , Day2)[^date6]
   * CalcDays_InLifeTime(Birthdat_Y, Birthday_M, Birthday_D)[^date7]
   * Chinese_Zodiac_Signs_Calc(Year)[^date8]
   * Chinese_Zodiac_Signs_Judge_Num(CZS , StartYear , Number = 10)[^date9]
   * Chinese_Zodiac_Signs_Judge_SEYear(CZS , StartYear , EndYear)[^date10]







[^date1]:输入英语的str型的周几英文简写，输出周几的int型 
[^date2]:输入周几的int型，输出汉语的str型数组。  
数组的第一个数据是“周”系列，第二个数据是“星期”系列
[^date3]:输入英语的str型英文月份简写，输出int型的月份数字
[^date4]:输入int型的年份数字，输出Boolean型的True或False。若为闰年则是True，否则是False
[^date5]:输入想要计算的某年下的某月的天数的int型月份，输出int型的天数。默认年份为创作者的生日的年份
[^date6]:输入想要计算从Year1:Month1:Day1到Year2:Month2:Day2中间有多少天，并返回int型变量。
[^date7]:输入生日的年月日，计算你一共活了多少天，返回int型
[^date8]:输入年份，计算该年份的生肖。返回str型
[^date9]:输入生肖，起始年份，多少次，三个变量后，输出从起始年份开始  
计算该年生肖。若是，则把该年份放入int型数组，否则不放。然后年份加一，并循环，直到放入指定的数值后，返回int型数组
[^date10]:输入生肖，起始年份，终止年份，三个变量后，输出从起始年份开始  
计算该年生肖。若是，则把该年份放入int型数组，否则不放。然后年份加一，并循环，直到年份加到终止年份后，返回int型数组