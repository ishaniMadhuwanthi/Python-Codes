#Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element

sampleList=[11, 45, 8, 11, 23, 45, 23, 45, 89]
print('original list:',sampleList)

countDict=dict()
for item in sampleList:
	if(item in countDict):
		countDict[item]=countDict[item]+1
	else:
	    countDict[item]=1

print('each counts:',countDict)	    	