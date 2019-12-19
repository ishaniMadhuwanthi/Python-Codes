#Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list

sampleList=[34, 54, 67, 89, 11, 43, 94]
print("Original list:",sampleList)

element=sampleList.pop(4)
print("list after removing index 4:",sampleList)

sampleList.insert(2,element)
print('list after adding index 2:',sampleList)

sampleList.append(element)
print("list after adding at the end:",sampleList)
