#Given a list of ints, return True if first and last number of a list is same

def isEqual(numList):
	firstElement=numList[0]
	lastElement= numList[len(numList)-1]
	return 'true' if(firstElement == lastElement) else 'false'


numList = str(input('enter list of numbers: '))
print(isEqual(numList))