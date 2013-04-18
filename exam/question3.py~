d={}
interaction=" "
li=[]
query=" "
while interaction!="":
	interaction=raw_input("input an interaction: ")
	if "," in str(interaction):
		li=li+[(interaction.split(","),)]
	else:
		print "ERROR: the inputed text is not in the correct format: P1, P2"
print li
for i in range(len(li)):
	for q in range(len(li[i])):
	
		d[li[i][q][0]]=li[i][q][1]
		d[li[i][q][1]]=li[i][q][0]

while query !='':
	query=raw_input("which protein do you want to query")
	if query in d:
		print "the protein interactions with "+str(query)+ "are"
		print "     ",d[query]

