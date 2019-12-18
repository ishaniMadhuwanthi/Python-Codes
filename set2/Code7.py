#String characters balance Test



def balCheck(s1,s2):
	flag = True
	for char in s1:
		if char in s2:
			continue
		else:
		    flag=False
	return flag	    	

s1="yn"
s2="Pynative"
flag = balCheck(s1,s2)
print("s1 qnd s2 are balanced : ", flag)
