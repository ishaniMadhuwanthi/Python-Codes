# Given two sets, Checks if One Set is Subset or superset of Another Set. if the subset is found delete all elements from that set
listOne={57,83,29}
listTwo={57,83,29,67,73,43,48}

print('list one:',listOne)
print('list two:',listTwo)

print('list one is subset of list two:',listOne.issubset(listTwo))
print('list two is subset of listOne:',listTwo.issubset(listOne))

print('list one is superset of list two:',listOne.issuperset(listTwo))
print('list two is superset of listOne:',listTwo.issuperset(listOne))

if(listOne.issubset(listTwo)):
	listOne.clear()

if(listTwo.issubset(listOne)):
    listTwo.clear()

print('list one:',listOne)
print('list two:',listTwo)    