'''
Python Script to parse Json files.
'''

import json

with open('report/test.json') as jsonData:
    parsedJson = json.load(jsonData) 
    allScanResults=parsedJson['scans']
    for antiVirusNames in allScanResults:
    	results=allScanResults[str(antiVirusNames)]
    	if results['detected']==True:
    		print('True')
    		break 
