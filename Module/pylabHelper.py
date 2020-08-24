import pylab as pyl

def Pylab_Plot(x , y , type = '-'):
    pyl.plot(x, y, type)
def Pylab_Plot_Show(x , y , type = '-'):
    pyl.plot(x, y, type)
    pyl.show()
def Pylab_Hist(data):
    pyl.hist(data)
def Pylab_Hist_Show(data):
    pyl.hist(data)
    pyl.show()
def Pylab_Show():
    pyl.show()