'''
Walks through the directory recursively and returns the list of files. 

Example, python getFileList.py $folder. 

If you want to store the result in a text file, python getFileList.py $folder >>amdFileList.py
'''

import os
import sys

directory=sys.argv[1]

for root, dirs, files in os.walk(directory):
    for myfile in files:
        if myfile.endswith(".apk"):
            print(myfile)


