#Given a dictionary get all values from the dictionary and add it in a list but don’t add duplicates

myList={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53,
          'july':54, 'Aug':44, 'Sept':54}

print('values of the dictionary:',myList.values())

newList=list()
for item in myList.values():
	if item not in newList:
		newList.append(item)
print('new List:',newList)		

