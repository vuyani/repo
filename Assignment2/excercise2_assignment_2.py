#2.(15%) Modify the previous code in such a way that the user can input as many sequences as he desires, and the tuples now have a 5th position that counts any other character different to a valid nucleotide. For example, if the user inputs 2 sequences: 

nucleotides =[]
inputseq=" "
numbers=[]
while inputseq != "":
	inputseq=raw_input("Enter sequences : ")
	if inputseq !="":
		nucleotides.append(inputseq)
 
for seq in nucleotides:
	lower=seq.lower()
	a=lower.count("a")
	t=lower.count("t")
	g=lower.count("g")
	c=lower.count("c")
	unknown=len(seq)-(a+t+g+c)		#subtracting the number of a,t,c and g should give the total number of unknown characters
	numbers =numbers+[(a,t,g,c,unknown)]	#storing the number of bases in a tuple in a list

print numbers


