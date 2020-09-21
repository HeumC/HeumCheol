def StrList_To_IntList(nums):
    temp = ''
    rt = []

    Flag_First = True

    for i in nums:
        try:
            i = int(i)
        except BaseException:
            if not Flag_First:
                try:
                    rt.append(int(temp))
                except BaseException:
                    pass
                else:
                    temp = ''
        else:
            temp += str(i)
            Flag_First = False

    return list(rt)
def Int_To_CNNum(integer_str):
    length = len(integer_str)
    temp = ""
    j = 0
    for i in range(length - 1, -1, -1):
        if i == 9 - 1:
            temp += integer_str[j] + "亿"
        elif i == 8 - 1:
            temp += integer_str[j] + "千"
        elif i == 7 - 1:
            temp += integer_str[j] + "百"
        elif i == 6 - 1:
            temp += integer_str[j] + "十"
        elif i == 5 - 1:
            temp += integer_str[j] + "万"
        elif i == 4 - 1:
            temp += integer_str[j] + "千"
        elif i == 3 - 1:
            temp += integer_str[j] + "百"
        elif i == 2 - 1:
            temp += integer_str[j] + "十"
        elif i == 1 - 1:
            temp += integer_str[j]
        j += 1
    return temp

# print(StrList_To_IntList("[1, 2, 3, 4]"))
# print(StrList_To_IntList("[1, 2, 3, 4123,"))
# print(type(StrList_To_IntList("[1,2,3,4]")))
# for num in StrList_To_IntList("[1,2,3,4]"):
#     print(type(num))