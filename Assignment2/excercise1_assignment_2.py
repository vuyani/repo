#1. (15%) Given the following list of nucleotide sequences, create a list of tuples where each tuple contains the number of A,T,G and C. (case insensitive)

nucleotides =["tttacgatcgatgtATCATTgtgatcgtagcgatgtatTATggcggcc","tttgggta","tgactgtagcagtcaTATCGATG","TTTTTGGTTGTGTGCAAGCTCGGCAGACTTt","ACTGATCGTCGATGCATGTCAGTAGCTAGCCATGTCAGTCAT"]
numbers=[]
 
for seq in nucleotides:
	lower=seq.lower()
	a=lower.count("a")		#counting the number of A
	t=lower.count("t")		#counting the number of T
	g=lower.count("g")		#counting the number of G
	c=lower.count("c")		#counting the number of C
	numbers =numbers+[(a,t,g,c)]	#storing each number of bases in a tuple and storing that tuple in a list
print numbers


