#Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.

listOne=[3,6,9,12,15,18,21]
listTwo=[4,8,12,16,20,24,28]
listThree=list()

odd=listOne[1::2]
print("odd index array:",odd)
even=listTwo[0::2]
print("even index array:",even)

listThree.extend(odd)
listThree.extend(even)
print("final array: ",listThree)

