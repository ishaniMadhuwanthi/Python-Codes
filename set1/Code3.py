#Accept string from the user and display only those characters which are present at an even index

word = str(input("Enter String: "))
print('Original String is',word)
print('Printing only even index chars ')
l = len(word)
for i in range (l):
	print(word[i])