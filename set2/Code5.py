#Given a string input Count all lower case, upper case, digits, and special symbols

input_str="P@#yn26at^&i5ve"
words=input_str.split()
letters= []
digits= []
symbols= []

for char in input_str:
 if(char.islower()):
    letters.append(char)
 elif(char.isupper()):
 	letters.append(char)
 elif(char.isnumeric()) : 
 	digits.append(char)  	
 else:
 	symbols.append(char)    

x= len(letters)
y=len(digits)
z=len(symbols)

print(x)
print(y)
print(z)