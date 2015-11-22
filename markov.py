import json
outfile = open('lalala2.json', 'r')
data = json.load(outfile)
#print data
combine = ""
for data1 in data:
	for key, value in data1.iteritems():
		for j in value:
			combine=combine +" " + j
		combine.replace("\n", " ")
		combine = combine.split()
		combine = [x for x in combine if "http" not in x]
		#a = [x for x in a if x != 2]
		combine = ' '.join(combine)
print combine
another = open('lalala1.txt', 'w')
another.write(combine.encode('utf-8'))


