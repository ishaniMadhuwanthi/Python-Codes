#arrange String characters such that lowercase letters should come first

inputStr= "PyNaTive"
words = inputStr.split()
lower=[]
upper=[]
for char in inputStr:
	if char.islower():
		lower.append(char)
	else:
	    upper.append(char)

newStr=''.join(lower+upper)

#print(words)
print('input_String:'+inputStr)
print('arranging characters giving precedence to lowercase letters:')
print('output_string: '+newStr)