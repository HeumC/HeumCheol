import pylab as pyl
from Module import helper

def Pylab_Plot(y , type = '-'):
    length = len(y)
    pyl.plot(helper.MakeList(1, length), y, type)
def Pylab_Plot_Show(y , type = '-'):
    length = len(y)
    pyl.plot(helper.MakeList(1, length), y, type)
    pyl.show()
def Pylab_Hist(data):
    pyl.hist(data)
def Pylab_Hist_Show(data):
    pyl.hist(data)
    pyl.show()
def Pylab_Show():
    pyl.show()