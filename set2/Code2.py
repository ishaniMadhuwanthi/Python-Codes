def getMid(s1, s2):
  midIndex = int(len(s1) /2)
  print("Original word: ", s1,"and" ,s2)
  midword = s1[:midIndex:]+ s2 +s1[midIndex-1:]
  print("edited word: ",midword)

s1=  "ishanim"
s2= "madhu"
getMid(s1,s2 )

