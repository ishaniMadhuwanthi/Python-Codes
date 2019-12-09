#Given a string and an int n, remove characters from string starting from zero up to n and return a new string

def removeChars(word,num):
   return word[num:]

word =str(input("enter string: "))
num = int(input("enter number: "))

print(removeChars(word,num))
