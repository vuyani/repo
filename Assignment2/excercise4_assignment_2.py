#3.(60%)Create a program that receive as many sequences as the user wants and calculates the GC ratio of each sequence. It should displays the sequences in order of its GC ratio, with the G's and C's in upper case and the T's and A's in lower case and in front of the sequence the calculated GC ratio. Finally it should show was the avarage GC ration among all the sequences

nucleotides =[]
inputseq=" "
numbers=[]
	
while inputseq != "":
	inputseq=raw_input("Enter sequences : ")
	if inputseq !="":
		nucleotides.append(inputseq)

for seq in nucleotides:
	lower=seq.lower()
	g=lower.count("g")		#counting the number of G
	c=lower.count("c")		#counting the number of C
	gc=g+c				#Summing the number of G and C
	gcr=float(gc)/len(seq)		#gcr is the gc ratio calculated by deviding the number of G and C by the total number of bases

	cap=lower
	caplist=list(cap)			#this converts each sequence to a list
	for i in range(0,len(caplist)):
		if caplist[i]=="g":		#search for lowercase g
		        caplist[i]="G"		#if g is found it is converted to uppercase G
		if caplist[i]=="c":		#search for lowercase g
		        caplist[i]="C"		#if g is found it is converted to uppercase G
		cap="".join(caplist)		#the list is converted to a string again
                

	numbers =numbers+[(gcr,cap)]		#a list of tuples containg the gc ratio and the modified sequences

gc_and_sequence=sorted(numbers,key=lambda x: x[0])	#sorts tuples arcoding to their gc ratio
total=0

for tup in gc_and_sequence:
	print  "Sequence : ",tup[1],"GC ratio : ", "%.2f" % tup[0]	#print gc ratio to 2 decimal places
	total=total+tup[0]
	average_gc=total/len(gc_and_sequence) 
print "The average GC ratio : ", "%.2f" % average_gc #the overall gc ratio
	
