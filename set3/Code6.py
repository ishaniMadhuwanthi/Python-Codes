#Given a following two sets find the intersection and remove those elements from the first set

listOne={23,42,65,57,78,83,29}
listTwo={57,83,29,67,73,43,48}

print('First list:',listOne)
print('Second list:',listTwo)

findInter=listOne.intersection(listTwo)
print('intersection list:',findInter)
for item in findInter:
	listOne.remove(item)

print('List One after remove intersection:',listOne)	