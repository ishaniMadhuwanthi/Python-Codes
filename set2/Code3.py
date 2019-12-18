#Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string

def getWord(s1,s2):
	midIndex1=int(len(s1) /2)
	midIndex2=int(len(s2) /2)
	newWord=s1[0]+s2[0]+s1[midIndex1]+s2[midIndex2]+s1[len(s1)-1]+s2[len(s2)-1]
	#new=s1[1]
	print(newWord)

s1="America"
s2="Japan"
getWord(s1,s2)
