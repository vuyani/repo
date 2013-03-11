def converter(celsius):
	fahrenheit=1.8*celsius + 32
	print celsius,"\t", float(fahrenheit)

temp1=raw_input("Input a value in Celsius: ")
temp2=raw_input("Input another value in Celsius: ")
if int(temp1)<=int(temp2):
	print "C","\t","F"
	for i in range(int(temp1),int(temp2)+1):
		converter(i)
elif int(temp1)>int(temp2):
	print "C","\t","F"
	for i in range(int(temp2),int(temp1)+1):
		converter(i)

