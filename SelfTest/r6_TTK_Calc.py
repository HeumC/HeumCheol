import xlrd
import xlwt
from Module import RainBowSixSeage as r6


def set_style(name, height, bold=False, format_str=''):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.height = height

    borders = xlwt.Borders()  # 为样式创建边框
    borders.left = 6
    borders.right = 6
    borders.top = 6
    borders.bottom = 6

    style.font = font
    style.borders = borders
    style.num_format_str = format_str

    return style

data = xlrd.open_workbook('R6.xlsx')
table = data.sheets()[0]

def getNames():
    names = []
    for name in table.col(0, start_rowx=1):
        names.append(name.value)
    return names
def getTypes():
    types = []
    for tYpe in table.col(1, start_rowx=1):
        types.append(tYpe.value)
    return types
def getDamages():
    damages = []
    for damage in table.col(2, start_rowx=1):
        damages.append(damage.value)
    return damages
def getFiringRatePerMinute_list():
    firing_rate_perMinute_list = []
    for firing_rate_perMinute in table.col(3, start_rowx=1):
        firing_rate_perMinute_list.append(firing_rate_perMinute.value)
    return firing_rate_perMinute_list

def get_ttk_for_armor_level_one_without_rookArmor_list():
    ttk_for_armor_level_one_without_rookArmor_list = []
    for i in range(0, len(names)):
        ttk_for_armor_level_one_without_rookArmor_list.append(
            r6.Gun(names[i], types[i], damages[i],
                   firing_rate_perMinute_list[i]).TTK_For_Armor_Level_One_Without_RookArmor)
    return ttk_for_armor_level_one_without_rookArmor_list
def get_ttk_for_armor_level_two_without_rookArmor_list():
    ttk_for_armor_level_two_without_rookArmor_list = []
    for i in range(0, len(names)):
        ttk_for_armor_level_two_without_rookArmor_list.append(
            r6.Gun(names[i], types[i], damages[i],
                   firing_rate_perMinute_list[i]).TTK_For_Armor_Level_Two_Without_RookArmor)
    return ttk_for_armor_level_two_without_rookArmor_list
def get_ttk_for_armor_level_three_without_rookArmor_list():
    ttk_for_armor_level_three_without_rookArmor_list = []
    for i in range(0, len(names)):
        ttk_for_armor_level_three_without_rookArmor_list.append(
            r6.Gun(names[i], types[i], damages[i],
                   firing_rate_perMinute_list[i]).TTK_For_Armor_Level_Three_Without_RookArmor)
    return ttk_for_armor_level_three_without_rookArmor_list
def get_ttk_for_armor_level_one_with_rookArmor_list():
    ttk_for_armor_level_one_with_rookArmor_list = []
    for i in range(0, len(names)):
        ttk_for_armor_level_one_with_rookArmor_list.append(
            r6.Gun(names[i], types[i], damages[i],
                   firing_rate_perMinute_list[i]).TTK_For_Armor_Level_One_With_RookArmor)
    return ttk_for_armor_level_one_with_rookArmor_list
def get_ttk_for_armor_level_two_with_rookArmor_list():
    ttk_for_armor_level_two_with_rookArmor_list = []
    for i in range(0, len(names)):
        ttk_for_armor_level_two_with_rookArmor_list.append(
            r6.Gun(names[i], types[i], damages[i],
                   firing_rate_perMinute_list[i]).TTK_For_Armor_Level_Two_With_RookArmor)
    return ttk_for_armor_level_two_with_rookArmor_list
def get_ttk_for_armor_level_three_with_rookArmor_list():
    ttk_for_armor_level_three_with_rookArmor_list = []
    for i in range(0, len(names)):
        ttk_for_armor_level_three_with_rookArmor_list.append(
            r6.Gun(names[i], types[i], damages[i],
                   firing_rate_perMinute_list[i]).TTK_For_Armor_Level_Three_With_RookArmor)
    return ttk_for_armor_level_three_with_rookArmor_list



names = getNames()
types = getTypes()
damages = getDamages()
firing_rate_perMinute_list = getFiringRatePerMinute_list()

ttk_for_armor_level_one_without_rookArmor_list = get_ttk_for_armor_level_one_without_rookArmor_list()
ttk_for_armor_level_two_without_rookArmor_list = get_ttk_for_armor_level_two_without_rookArmor_list()
ttk_for_armor_level_three_without_rookArmor_list = get_ttk_for_armor_level_three_without_rookArmor_list()
ttk_for_armor_level_one_with_rookArmor_list = get_ttk_for_armor_level_one_with_rookArmor_list()
ttk_for_armor_level_two_with_rookArmor_list = get_ttk_for_armor_level_two_with_rookArmor_list()
ttk_for_armor_level_three_with_rookArmor_list = get_ttk_for_armor_level_three_with_rookArmor_list()

wb = xlwt.Workbook()
ws = wb.add_sheet('枪械TTK')
ws.col(0).width = 200*30

ws.write(0, 0, '名字')
ws.write(0, 1, '类型')
ws.write(0, 2, '伤害')
ws.write(0, 3, '射速')
ws.write(0, 4, 'TTK_1_F')
ws.write(0, 5, 'TTK_2_F')
ws.write(0, 6, 'TTK_2_F')
ws.write(0, 7, 'TTK_1_T')
ws.write(0, 8, 'TTK_2_T')
ws.write(0, 9, 'TTK_3_T')
ws.write(0, 10, '平均TTK')

# for row in range(1, len(names) + 1):
#     ttk_ave = (ttk_for_armor_level_one_without_rookArmor_list[row - 1] + ttk_for_armor_level_two_without_rookArmor_list[
#         row - 1] + ttk_for_armor_level_three_without_rookArmor_list[row - 1] +
#               ttk_for_armor_level_one_with_rookArmor_list[row - 1] + ttk_for_armor_level_two_with_rookArmor_list[
#                   row - 1] + ttk_for_armor_level_three_with_rookArmor_list[row - 1]) / 6
#     ws.write(row, 0, names[row-1])
#     ws.write(row, 1, types[row-1])
#     ws.write(row, 2, damages[row-1])
#     ws.write(row, 3, firing_rate_perMinute_list[row-1])
#     ws.write(row, 4, str(round(ttk_for_armor_level_one_without_rookArmor_list[row-1], 2)) + 'ms')
#     ws.write(row, 5, str(round(ttk_for_armor_level_two_without_rookArmor_list[row-1], 2)) + 'ms')
#     ws.write(row, 6, str(round(ttk_for_armor_level_three_without_rookArmor_list[row-1], 2)) + 'ms')
#     ws.write(row, 7, str(round(ttk_for_armor_level_one_with_rookArmor_list[row-1], 2)) + 'ms')
#     ws.write(row, 8, str(round(ttk_for_armor_level_two_with_rookArmor_list[row-1], 2)) + 'ms')
#     ws.write(row, 9, str(round(ttk_for_armor_level_three_with_rookArmor_list[row-1], 2)) + 'ms')
#     ws.write(row, 10, str(round(ttk_ave, 2)) + 'ms')

for row in range(1, len(names) + 1):
    ttk_ave = (ttk_for_armor_level_one_without_rookArmor_list[row - 1] + ttk_for_armor_level_two_without_rookArmor_list[
        row - 1] + ttk_for_armor_level_three_without_rookArmor_list[row - 1] +
               ttk_for_armor_level_one_with_rookArmor_list[row - 1] + ttk_for_armor_level_two_with_rookArmor_list[
                   row - 1] + ttk_for_armor_level_three_with_rookArmor_list[row - 1]) / 6
    ws.write(row, 0, names[row-1])
    ws.write(row, 1, types[row-1])
    ws.write(row, 2, damages[row-1])
    ws.write(row, 3, firing_rate_perMinute_list[row-1])
    ws.write(row, 4, round(ttk_for_armor_level_one_without_rookArmor_list[row-1], 2))
    ws.write(row, 5, round(ttk_for_armor_level_two_without_rookArmor_list[row-1], 2))
    ws.write(row, 6, round(ttk_for_armor_level_three_without_rookArmor_list[row-1], 2))
    ws.write(row, 7, round(ttk_for_armor_level_one_with_rookArmor_list[row-1], 2))
    ws.write(row, 8, round(ttk_for_armor_level_two_with_rookArmor_list[row-1], 2))
    ws.write(row, 9, round(ttk_for_armor_level_three_with_rookArmor_list[row-1], 2))
    ws.write(row, 10, round(ttk_ave, 2))

wb.save('R6_TTk.xls')






