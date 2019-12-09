#Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

def findDivisible(numberList):
  for num in numberList:
    if (num % 5 == 0):
      print(num)

numList = [10, 20, 33, 46, 55]
print("Finding divisible of 5 in a list")
findDivisible(numList)