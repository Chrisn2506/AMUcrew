import datetime as dt
import pylab as lab
import numpy as np
#Theoretically, one reading was taken every 3 seconds. However, realistically there will be a small amount of processing time for every reading. 
#We developed this code to find out how long the raspberry pi took to process every reading by using the timestamps.
#This code will output the average processing time for every loop, which was 45480 microseconds.
#This makes the average time between each reading 3.04548 seconds.
data = lab.loadtxt('Value_file.csv', skiprows=1, usecols=[6], dtype=np.datetime64, delimiter=',')

x=0
y=1
tot = 0

for i in range(len(data)-1):
    t = data[x]
    t2 = data[y]
    delay = t2-t
    deviation = delay-3000000
    x=x+1
    y=y+1
    if deviation > dt.timedelta(microseconds = 0): 
        tot = tot + deviation
    elif deviation < dt.timedelta(microseconds = 0): 
        tot = tot - deviation

avg = tot/len(data) 
print(avg) 
        
