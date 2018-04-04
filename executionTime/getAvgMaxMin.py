'''
Calculates average, Min and max. 
Example,. python getAvgMinMax.py $textFile 

'''

import numpy as np 
import math
import sys 

resultFile=sys.argv[1] 
execTimeList=[]

fileContent=open(resultFile)

for line in fileContent:
    try:
        line=line.strip().split(',')
        execTime=float(line[1])
        execTime=(math.ceil(execTime*100))/100
        print(execTime)
    except IndexError:
        print("Invalid line")

