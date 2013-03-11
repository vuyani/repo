def y(m,x,b):
	y= m * x + b
	return y

print "The results for the linear equation Y=mX+b with m=1 and b=0 are:","\n" "X","\t","Y"
for i in range(1,11):
	yint=y(1,i,0)
	
	print i,"\t",yint
