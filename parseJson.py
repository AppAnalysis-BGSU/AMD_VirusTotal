'''
Python Script to parse Json files.
Give the folder name containing virusTotal results as the first argument. 
For example, python parseJson.py report. 
Checks if at least one antivirus has scanned the APK as malicious. 

Created By: Shiva Bhusal, BGSU 
'''

import os
import sys
import json

directory=sys.argv[1]
jsonResultList=[]

'''
Walk through the directory
and get all the json files with complete path. 
Store file info in a list. 
'''

for root, dirs, files in os.walk(directory):
    for myfile in files:
        if myfile.endswith(".json"):
            jsonResultList.append(os.path.join(root, myfile))

#print(jsonResultList)

print('Sha256'+','+'Result') # Print the header 

'''
Gets all the json file paths from the List.
Parses the json files. 
and Prints the result. 
'''
for filePath in jsonResultList:
	with open(filePath) as jsonData:
		parsedJson = json.load(jsonData) 
		allScanResults=parsedJson['scans']
		#trueCount=0 ## Use this count if the assumption is at least N antiviruses should complain the APK as malicious. 
		for antiVirusNames in allScanResults:
			results=allScanResults[str(antiVirusNames)]
			if results['detected']==True:
				jsonFileName=os.path.basename(filePath)
				apkName=jsonFileName.replace('.json','') # Remove .json 
				print(apkName+','+'True')
				break
	jsonData.close()
