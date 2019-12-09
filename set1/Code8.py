#Print the following pattern
#1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5

num=int(input('enter number: '))
for n in range(num+1):
    for i in range(n):
        print (n, end=" ") 
    
    print("\n")
       
