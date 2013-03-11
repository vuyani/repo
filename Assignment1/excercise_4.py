def y(m,x,b):
	y= m * x + b
	return y
m=raw_input("enter m")#m value is 1
b=raw_input("enter b")#b value is 0
print "The results for the linear equation Y=mX+b with m=1 and b=0 are:","\n" "X","\t","Y"
for i in range(1,11):
	yint=y(m,i,b)
	
	print i,"\t",yint
