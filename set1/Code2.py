def getSum(prevNum):
	prevNum=0;
	for i in range(num):
	   sum =prevNum+i
	   print(sum)
	   prevNum=i

num = int(input("Enter number: "))
print(getSum(num))
