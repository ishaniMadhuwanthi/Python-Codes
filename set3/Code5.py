# Given a two list of equal size create a set such that it shows the element from both lists in the pair
listOne=[2,3,4,5,6,7,8]
listTwo=[4,9,16,25,36,79,68]
print('First List:',listOne)
print('Second List:',listTwo)

result=zip(listOne,listTwo)
resultList=set(result)
print('Result pairs:',resultList)
