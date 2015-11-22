import json
infile = open('palin.txt', 'r')
#data = json.load(outfile)
#print data
combine = ""
startpoints = []
for line in infile:
	if len(line.strip(' \t\n\r'))!=0:
		kk = line.split()
		try:
			startpoints.append(kk[0].lower()+" "+kk[1].lower())
		except:
			kk = []
		combine=combine +" " + line

combine.replace("\n", " ")
combine = combine.split()
combine = [x for x in combine if "http" not in x]
#a = [x for x in a if x != 2]
combine = ' '.join(combine)
#print combine
#another = open('lalala1.txt', 'w')
#another.write(combine.encode('utf-8'))
combine = combine.split()
for i in xrange(len(combine)):
	combine[i]=combine[i].lower()
triplet = []
for i in xrange(len(combine)-3):
	triplet.append([combine[i],combine[i+1],combine[i+2]])

doubledict = {}

for l in triplet:
	duet = l[0]+" "+l[1]
	if duet in doubledict:
		doubledict[duet].append(str(l[2]))
	else:
		doubledict[duet]=[str(l[2])]

#print doubledict


with open('palincombined.json', 'w') as fp:
    json.dump(doubledict, fp)
with open('palinstartpoints.txt', 'w') as st:
	for item in startpoints:
  		print>>st, item

