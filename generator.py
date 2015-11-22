import json
import random


outfile = open('palincombined.json', 'r')
start = open('palinstartpoints.txt','r')
start = random.choice(start.readlines())
data = json.load(outfile)
#start = random.choice(data.keys())
#print start
length = random.randint(3,20)

listsofar = start.split()
while len(listsofar)<=length:
	prev = listsofar[-2]+" "+ listsofar[-1]
	#print prev
	get = data[prev]
	string = random.choice(get)
	listsofar.append(string)
	if len(listsofar)==length and ("." not in listsofar[-1] and length<40):
		length+=1
listsofar.pop()
listsofar = ' '.join(listsofar)
print listsofar