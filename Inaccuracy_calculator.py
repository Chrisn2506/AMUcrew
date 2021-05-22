import datetime as dt
import pylab as lab
import numpy as np

#This line reads the part of the csv i specified, which is the column with timestamps of all the readings.
data = lab.loadtxt('Value_file.csv', skiprows=1, usecols=[6], dtype=np.datetime64, delimiter=',')

#Defining variables for later.
x=0
y=1
tot = 0

#Loop that repeats the same amount of times as there are rows in the csv-1. The -1 is there so that y doesn't go higher than the number of rows, because it starts at 1.
#t is always 1 row behind t2, which is important because i want to find the time difference between every row.
#For every time it loops, it calculates the difference between the next 2 rows.
#delay is the time difference between the two rows.
#deviation is delay-3seconds because i want to find the biggest deviation from the 3 seconds we specified in the code that created the csv.

for i in range(len(data)-1):
    t = data[x]
    t2 = data[y]
    delay = t2-t
    deviation = delay-3000000
    x=x+1
    y=y+1
    if deviation > dt.timedelta(microseconds = 0): #This if statement is for adding all the deviations together to get the average at the end.
        tot = tot + deviation
    elif deviation < dt.timedelta(microseconds = 0): #The reason i had to add an if statement here is because some og the deviations are negative, and i need the absolute value for the average to make sense.
        tot = tot - deviation
    if deviation>dt.timedelta(microseconds = 288000): #This if statement is for finding the biggest deviation from 3 seconds. I just kept increasing the number of microseconds until it only printed the biggest instance.
        print(x, deviation) #It also prints x to show what reading this happened at.
    elif deviation<dt.timedelta(microseconds = -170000): #This one is the same, only for negative deviations, which means it read before three seconds had passed.
        print(x, deviation)

avg = tot/len(data) #Dividing the total by the number of rows gives me the average.
print(avg) #Prints it
        
