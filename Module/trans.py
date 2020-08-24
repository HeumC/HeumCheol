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

# print(StrList_To_IntList("[1, 2, 3, 4]"))
# print(type(StrList_To_IntList("[1,2,3,4]")))
# for num in StrList_To_IntList("[1,2,3,4]"):
#     print(type(num))