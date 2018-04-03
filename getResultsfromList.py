'''
Copies the list of virus totals results for the list of files in a text file. 
'''

import sys
import os


fileName=sys.argv[1]
sourceFolder=sys.argv[2]
destFolder=sys.argv[3]

f=open(fileName)

for lines in f:
    lines=lines.split(',')
    apk=lines[0]
    jsonFile=apk.replace('.apk','.json')
    os.system('cp'+' '+sourceFolder+'/'+jsonFile+' '+destFolder+'/'+jsonFile)


