import math
from Module import helper
from Module import mAth

lst1 = helper.MakeList_RandomNumber(2, 0, 100)
lst2 = helper.MakeList_RandomNumber(2, 0, 100)

print(lst1)
print(lst2)
print("皮尔逊相关系数：%.2f" %mAth.Pearson_Correlation_Coefficient(lst1, lst2))
print("皮尔逊相关系数判断：",end="")
print(mAth.Pearson_Correlation_Coefficient_Judge_CN(mAth.Pearson_Correlation_Coefficient(lst1, lst2)))
print("余弦相似度：%.2f" %mAth.cosine_similarity(lst1, lst2))
angel = mAth.Converter_Radian_To_Angle(math.acos(mAth.cosine_similarity(lst1, lst2)))
print("角度：%.2f°" % angel)
