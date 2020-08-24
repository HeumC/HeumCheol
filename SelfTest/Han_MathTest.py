from HCheol import HCheol_Level1 as FBHS

Num_Test = 4000
'''a = []
for n in range(1 , Num_Test + 1):
    a.append(((n + 1) / n) ** n)
print(a)
FBHS.Pylab_Plot_Show(FBHS.Auto_MakeList_AToB(1 , Num_Test) , a)'''

'''b = []
temp = 19990517 ** (1/2)
b.append(temp)
Break_Flag = 0
for i in range(1 , Num_Test + 1):
    temp = temp ** (1 / 2)
    b.append(temp)
    if temp == 1.0:
        Break_Flag += 1
    if Break_Flag == 100:
        break
FBHS.Pylab_Plot_Show(FBHS.Auto_MakeList_AToB(1 , Num_Test + 1) , b)'''

c = []
d = []
HM_temp = 0
for num in range(1 , Num_Test + 1):
    temp = num ** (1/2)
    HM = 0
    while True:
        if temp == 1.0:
            break
        temp = temp ** (1/2)
        HM += 1
    if HM != HM_temp:
        d.append(num)
    HM_temp = HM
    c.append(HM)
    #print(HM)
print(c)
print(d)
#FBHS.Pylab_Plot(FBHS.Auto_MakeList_AToB(1 , Num_Test) , c)
FBHS.Pylab_Plot(FBHS.Auto_MakeList_AToB(1 , len(d)) , d)
FBHS.Pylab_Show()

'''e = []
for num in range(1 , Num_Test + 1):
    print(FBHS.math.factorial(num))
    e.append(FBHS.math.factorial(num))
FBHS.Pylab_Plot_Show(FBHS.Auto_MakeList_AToB(1 , Num_Test) , e)'''
