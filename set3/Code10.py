#Remove duplicate from a list and create a tuple and find the minimum and maximum numbe

sampleList = [87, 52, 44, 53, 54, 87, 52, 53]
print('original list:',sampleList)

sampleList=list(set(sampleList))
print('unique list:',sampleList)

tuple=tuple(sampleList)
print('tuple:',tuple)

print('max:',max(tuple))
print('min:',min(tuple))