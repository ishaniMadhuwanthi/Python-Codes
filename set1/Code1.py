def getProduct(num1,num2):
   product = num1*num2;
   return product;

def getSum(num1,num2):
   additon = num1 + num2;
   return additon;   

num1 = int(input("enter first number:"))
num2 = int(input("enter secomd number:"))


print(getSum(num1,num2) if(getProduct(num1,num2)>1000) else getProduct(num1,num2))


