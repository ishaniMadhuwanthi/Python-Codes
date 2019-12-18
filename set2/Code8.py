#Find all occurrences of “USA” in given string ignoring the case

inputString="Welcome to USA. usa awesome, isn't it?"
subString="USA"
new_subString=subString.lower()
tempString=inputString.lower()
count=tempString.count(new_subString)
print('The '+subString+' count is:',count)