x=raw_input("Enter a number: ")

li=[]
w=1

for i in range(1,int(x)):
	
	
	if i%2!=0:
		w=w+2
		li.append(w)
		
	if i%2==0:
		w=w+3
		li.append(w)

print "the first "+str(x)+"items in the sequence are"
print "1"
for i in li:
	print i
