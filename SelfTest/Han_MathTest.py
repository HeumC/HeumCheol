
from Module import pylabHelper
from Module import helper
from Module import mAth
num1 = 0
num2 = 7
for r in range(1, 100):
    print("%.2f 与 %.2f 在范围为 10的%d次方 数量级下的宏观距离比率为：%.3f%%" % (
        num1, num2, r, mAth.Similarity_BTwen_Two_Number(num1, num2, r) * 100))