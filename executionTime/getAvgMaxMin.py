'''
Calculates average, Min and max. 
Example,. python getAvgMinMax.py $textFile 

'''

import numpy as np 
import math
import sys 

def roundOff(number):
    return (math.ceil(number*100))/100

resultFile=sys.argv[1] 
execTimeList=[]

fileContent=open(resultFile)

for line in fileContent:
    try:
        print(line)
        line=line.strip().split(',')
        execTime=float(line[1])
        execTime=roundOff(execTime) # Round off to two decimal digits. 
        execTimeList.append(execTime)
    except IndexError:
        print("Invalid line")

execTimeList.sort()
fileContent.close()

#print(execTimeList)
total=0
for times in execTimeList:
    total=total+times

avg=roundOff(total/len(execTimeList))
minimum=execTimeList[0]
maximum=execTimeList[len(execTimeList)-1]

print("Total apps:"+ str(len(execTimeList)))
print("Average: " + str(avg))
print("Minimum: "+ str(minimum))
print("Maximum: "+ str(maximum))



