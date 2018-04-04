'''
First argument: Directory. Walks through the directory recursively and gets the path to APK files. 
Second Argument: path to resultFile: The file where result of LockScreen plugin is stored. 
Third Argument: Path to the file where execution time is stored. 

Example, python getExecutionTime.py $Path_to_apkFolder $Path_to_resultFile.txt $Path_to_execTimeFile 
'''

import os
import sys
import time as t

directory=sys.argv[1]
resultFile=sys.argv[2]
execTimeFile=sys.argv[3]

for root, dirs, files in os.walk(directory):
    for myfile in files:
        if myfile.endswith(".apk"):
            fullPath=os.path.join(root,myfile)
            print('APK being scanned:'+fullPath)
            startTime=t.time()
            os.system('java -jar lockScreen.jar '+fullPath+' '+resultFile)
            endTime=t.time()
            execTime=endTime-startTime
            createdFolder=fullPath.replace('.apk','')
            os.system('rm -r '+createdFolder)
            fileToStoreTime=open(execTimeFile,"a")
            fileToStoreTime.write('\n'+myfile+','+str(execTime))
            fileToStoreTime.close()


