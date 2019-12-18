#Given an input string, count occurrences of all characters within a string

inputString="pynativepynvepynative"
countDict = dict()
for char in inputString:
	count=inputString.count(char)
	countDict[char]=count
print(countDict)	