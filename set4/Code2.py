#Random Lottery Pick

import random

ticketList=[]
print('create 100 ticket list................')
for i in range(100):
	ticketList.append(random.randrange(1000000000,9999999999))

winners=random.sample(ticketList,2)
print('lucky 2 winners:',winners)	