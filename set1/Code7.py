#Return the number of times that the string “Emma” appears 
#anywhere in the given string

def isFind(statement):
  count =0 
  for i in range(len(statement)-1):
  	 count += statement[i:i+4] == 'Emma'
  return count
  
  			

#word = str('Emma is a good developer. Emma is also a writer')
count=isFind("Emma is a good developer. Emma is also a writer")
print(count)