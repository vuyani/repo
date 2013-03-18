#3.(10%) Extend the previous exercise to print your results in the next way

nucleotides =[]
inputseq=" "
numbers=[]
while inputseq != "":
	inputseq=raw_input("Enter sequences")
	if inputseq !="":
		nucleotides.append(inputseq)	#storage of raw sequences
 
for seq in nucleotides:	
	lower=seq.lower()	#each sequence converted to lower case
	a=lower.count("a")
	t=lower.count("t")
	g=lower.count("g")
	c=lower.count("c")
	unknown=len(seq)-(a+t+g+c)	
	numbers =numbers+[(a,t,g,c,unknown)]	

for tup in range(0,len(numbers)):
	print "SEQUENCE", tup+1,"\b:", nucleotides[tup]
	bases=["A","T","G","C","*"]
	counter=0
	for nuc in bases:
		if nuc!="*":
			print "",nuc,"|",numbers[tup][counter],"\n","-"*7		#output for the first four bases including dash lines
		else:
			print "",nuc,"|",numbers[tup][counter]				#output for the last base excluding dash lines
		counter=counter+1
