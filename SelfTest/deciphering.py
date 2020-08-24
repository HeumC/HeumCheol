import random

def JiaMi(msg , ch):

    if ch <= -1 or ch >= 11:
        return -1
    msgList = list(msg)

    j = 0
    for i in msgList:
        if i == " ":
            msgList[j] = "X"
        j += 1


    for b in range(len(msgList)):
        msgList[b] = chr(ord(msgList[b]) + ch)

    return msgList

def JieMi(msg , ch):
    msgList = list(msg)

    for b in range(len(msgList)):
        msgList[b] = chr(ord(msgList[b]) - ch)

    j = 0
    for i in msgList:
        if i == "X":
            msgList[j] = " "
        j += 1

    return msgList

print("（加密频道的数字选择在0~10之间，0为不加密）")
ch = input("请输入加密频道）:")

if ch.isdigit():
    ch = int(ch)
else:
    print("请输入纯数字！")
    exit(0)
msg = input("请输入加密内容：")

#ch = 1
#msg = "I Love You"

if JiaMi(msg , ch) == -1:
    print("频道数不存在！加密失败！")
    exit(0)

print("加密后%s频道下的内容为：" % ch, end="")
msg2 = JiaMi(msg , ch)
for a in msg2:
    print(a , end="")

print()

print("解密后%s频道下的内容为：" % ch, end="")
for a in JieMi(msg2 , ch):
    print(a , end="")




