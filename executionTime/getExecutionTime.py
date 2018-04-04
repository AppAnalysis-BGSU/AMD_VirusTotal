'''
Walks through the directory recursively and returns the list of files. 

Example, python getFileList.py $folder. 

If you want to store the result in a text file, python getFileList.py $folder >>amdFileList.py
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


