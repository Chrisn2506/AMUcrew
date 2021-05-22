import datetime as dt
import pylab as lab
import numpy as np

data = lab.loadtxt('Value_file.csv', skiprows=1, usecols=[6], dtype=np.datetime64, delimiter=',')

x=0
y=1

for i in range(len(data)-1):
    t = data[x]
    t2 = data[y]
    delay = t2-t
    deviation = delay-3000000
    x=x+1
    y=y+1
    if deviation>dt.timedelta(microseconds=288000):
        print(x, deviation)
    elif deviation<dt.timedelta(microseconds = -170000):
        print(x, deviation)