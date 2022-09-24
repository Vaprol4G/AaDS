import math
import numpy
import matplotlib.pyplot as plt

def mft():
    GFun()
    PFun()
def GFun():
    val = 0.0
    f = open('out.dat', 'w')
    for i in numpy.arange(-2*math.pi, 2.1*math.pi, 0.1):
        val = math.sin(2*i)+math.cos(i/2)
        print(str(i)+ " " + str(val))
        f.write(str(i)+ " " + str(val)+'\n')
    f.close()
    print()
def PFun():
    x_list = []
    y_list = []
    f = open('out.dat')
    line = f.readline()
    while(line != ""):
        x_list += [float(line.split(" ")[0])]
        y_list += [float(line.split(" ")[1])]
        line = f.readline()
    plt.plot(x_list, y_list)
    plt.show()
