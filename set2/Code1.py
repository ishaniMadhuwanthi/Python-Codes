def getMidThree(word):
   midIndex = int(len(word) /2)
   print('original word: ', word)
   midThree = word[midIndex-1:midIndex+2]
   print('midlle three letters: ',midThree)
   


word="ishnaitrghq"
getMidThree(word)
