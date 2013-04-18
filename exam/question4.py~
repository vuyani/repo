lines=[]
lines2=[]
a=[]
b=[]
c=[]
d=[]
protein_average=[]
protein_average1=[]
protein_averages=[]
protein_averages1=[]
deltas=[]
overex=[]
underex=[]
normal=[]
thresh_hold=""
file_path=raw_input("path of the expression levels for healthy individuals")

file1=open(file_path, 'r+')
for i in file1:
	lines=lines+[i]
file1.close()
for line in lines:
	a=line[6:].split(" ")
	c=c+[(line.split(" "),)]

print "for healthy samples"
print "there are ", len(a), "indivials"
print "there are ", len(lines), "proteins"
count=0
for i in range(1, len(a)):
	count=count+int(a[i])
protein_average=count/len(a)
protein_averages=protein_averages+[(c[1],protein_average,)]


file_path2=raw_input("path of the expression levels for infected individuals")

file2=open(file_path2, 'r+')
for i in file2:
	lines2=lines2+[i]
file2.close()
for line in lines2:
	b=line[6:].split(" ")
	d=d+[(line.split(" "),)]
print "for infected individuals"
print "there are ",len(b), "individualsls"
print "there are ",len(lines2), "proteins"
count=0
for i in range(1, len(a)):
	count=count+int(b[i])
protein_average=count/len(b)
protein_average1=count/(len(b))
protein_averages1=protein_averages1+[(d[1],protein_average1,)]
select=""
predix=""
while select!="X":
	select=raw_input("select option:,"+"\n"+"[T] select a threshold value"+"\n"+"[D] Display categorised proteins ordered by delta"+"\n"+"[F] create three file with thhe different categories"+"\n"+"[X] exit"+"\n"+":")
	if select=="T":

		thresh_hold=raw_input("new value for the threshold(th): ")
		print "the thresh hold has been successfully changed to"+thresh_hold
	if select=="D":

		for i in range(len(protein_averages)):
			delt=protein_averages[i][1]-protein_averages[i][1]
			deltas=deltas+[(protein_averages[i][1],delt)]
		for i in range(len(protein_averages)):

			if int(protein_averages[i][1])+int(thresh_hold) < int(protein_averages1[i][1]):
				overex=overex+[protein_averages[i][0][0][0]]
			if int(protein_averages[i][1])-int(thresh_hold) > int(protein_averages1[i][1]):
				normal=underex+[protein_averages[i][0][0][0]]
			if int(protein_averages[i][1])-int(thresh_hold) > int(protein_averages1[i][1]) and int(protein_averages1[i][1]) < int(protein_averages[i][1])+int(thresh_hold) :
				underex=underex+[protein_averages[i][0][0][0]]
		print "list using a threshold of"+thresh_hold

		print "overexpressed proteins"
		for i in overex:
			if len(overex)>0:
		 		print i
		print "normal expression"
		for i in normal:
			if len(normal)>0:
		 		print i
		print "under expressed"
		for i in underex:
			if len(underex)>0:
		 		print i
	if select=="F":
		import os
		import os.path
		f=os.path.exists(predix)
		W=os.path.exists(predix)
		X=os.path.exists(predix)
		predix=raw_input("what is the predix of the files")
		if f==True:
			
			with open(predix+str(UNDER.txt),"w") as f:
					f.write("".join(underex))
			with open(predix+str(NORMAL.txt),"w") as W:
					W.write("".join(normal))
			with open(predix+str(OVER.txt),"w") as X:
					X.write("".join(overex))


		print "the files "+predix+"_OVER.txt",predix+"_NORMAL.txt",predix+"_UNDER.txt have been successfully created"








