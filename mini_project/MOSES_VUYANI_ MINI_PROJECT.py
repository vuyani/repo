inputfile=["none"]
main_menu=" "
alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pdbfile="none"
title=""
b1=0
c1=0
CL=[]
A_numofaa=0
B_numofaa=0
ltrlist=[]
histlist=[]
lines=[]
tp=()
tps=()
collection1=[]
collection2=[]
collection3=[]
new_line='HELIX                                    \n'
new_sheet='SHEET                                  \n'
options=""
aminot={"V":"VAL","I":"ILE","L":"LEU","E":"GLU","Q":"GLN","D":"ASP","N":"ASN","H":"HIS","W":"TRP","F":"PHE","Y":"TYR","R":"ARG","K":"LYS","S":"SER","T":"THR","M":"MET","A":"ALA","G":"GLY","P":"PRO","C":"CYS"}
helix_class = {1:'Right-handed alpha (default)', 2:'Right-handed omega', 3:'Right-handed pi', 4:'Right-handed gamma', 5:'Right-handed 3 - 10', 6:'Left-handed alpha', 7:'Left-handed omega', 8:'Left-handed gamma', 9:'2 - 7 ribbon/helix', 10:'Polyproline'}

while main_menu!="Q":
	print 80*'*',"\n",'*','PDB FILE ANALYZER',58*" ","*","\n",80*'*',"\n","*","Select an option from below:",47*" ","*","\n","*",76*" ","*","\n","*",3*" ","1) Open a PDB File",21*" ","(O)",27*" ","*","\n","*",3*" ","2) Information",25*" ","(I)",27*" ","*","\n","*",3*" ","3) Show histogram of amino acids",7*" ","(H)",27*" ","*","\n","*",3*" ","4) Display Secondary structure",9*" ","(S)",27*" ","*","\n","*",3*" ","5) Manipulate Helix or Sheet",11*" ","(M)",27*" ","*","\n","*",3*" ","6) Export PDB File",21*" ","(X)",27*" ","*","\n","*",3*" ","7) Exit",32*" ","(Q)",27*" ","*","\n""*",76*" ","*"
	if pdbfile !="none":
		print '*',54*" ",'Current PDB:',pdbfile,"*","\n", 80*'*'
	else:
		print '*',58*" ",'Current PDB:',pdbfile,"*","\n", 80*'*'
	main_menu=raw_input(": ").upper()

#file input	
	if main_menu=="O":
		pdbfile=raw_input("Enter a Valid PATH for a PDB File: ")
		import os.path
		f=os.path.exists(pdbfile)
		
	
		if f==True: # test if file exists
			
			if pdbfile in inputfile:
				print "the File", pdbfile, "is already loaded"					


			else:

				file1=open(pdbfile, 'r+')
				inputfile=inputfile[:]+[pdbfile] # if file doesnt exist the previously uploaded file is overwrtten
				print "The File", pdbfile, "has been successfully loaded"
				for i in file1:
					lines=lines+[i]
				file1.close()
				one_letter ={'VAL':'V', 'ILE':'I', 'LEU':'L', 'GLU':'E', 'GLN':'Q', \
				'ASP':'D', 'ASN':'N', 'HIS':'H', 'TRP':'W', 'PHE':'F', 'TYR':'Y',    \
				'ARG':'R', 'LYS':'K', 'SER':'S', 'THR':'T', 'MET':'M', 'ALA':'A',    \
				'GLY':'G', 'PRO':'P', 'CYS':'C'}


				for i in lines:
					if "DBREF" in i:
						if i[12] not in CL:
							CL.append(i[12])#storage of the number of chains
				for a in CL:
					ltrlist=[]
					for i in lines:
						if "SEQRES" in i:
							if i[11]==a:
								aseq=i[19:70]
								ltr=aseq.split(" ")
								ltrlist=ltrlist+ltr # protein sequences
					tp=tp+(ltrlist,) # protein in each chain stored as a list in a tuple
				for a in range(len(tp)):
					x=""
					for c in tp[a]:
						for b in one_letter:
							if c==b:
								x=x+one_letter[c]
					tps=tps+(x,)	#generation of one letter anmino acid sequence

		else:
			print "Error", pdbfile, "does not exist"
			pdbfile="none"

		
	if main_menu=="I":   # information
		title=""			
		for alph in CL:
			for i in lines:
				if "TITLE" in i:
					title=title+ str(i[10:]).rstrip('\n').rstrip() # title creation
				a=0
				if "SEQRES" in i:                                       #getting the total amino acids in each chain
						if i[11]==alph:
							chaint=i[13:18]
							a=chaint
							if a in collection1:          #eliminating redudancy
								continue
							else:
								collection1.append(a)
		for alph in CL:
			b1=0
			for i in lines:
				if "HELIX" == i[0:5]:			
					if i[19]==alph:
						b1=b1+1			
			if b1 in collection2 and b1!=0:
				b1=b1
			else:		
				collection2.append(b1)

		for alph in CL:
			c1=0
			for i in lines:

				if "SHEET" in i: 			#getting total number of helices in each chain
						if i[21]==alph:
							c1=c1+1
			
			if c1 in collection3 and c1!=0:
				c1=c1
			else:
				collection3.append(c1)
		
		print "PDB File:",pdbfile,"\n","TITLE",title
		for chain in range(0,len(CL)):
			print "Chain: ","\n","-Chain ",CL[chain]+":","\n", "   Number of amino acids: ","\t","%3s"%collection1[chain],"\n", "   Number of helix:","\t","\t","%3s"%int(collection2[chain]),"\n","   Number of sheet:","\t","\t","%3s"%int(collection3[chain])
			print "   Sequence:",
			for v in range(len(tps[chain])): # outputting protein sequence with 50 char line limit

					if v%50==0:
						print  "           ",tps[chain][a:v]
						a=v
			print "           ",tps[chain][a:]
			

	if main_menu=="H":
		
			histlist=[]

			histoptions=raw_input("Choose an option to order by:"+"\n"+"  number of amino acids - ascending  (an)"+"\n"+"  number of amino acids - descending (dn)"+"\n"+"  alphabetically - ascending         (aa)"+"\n"+"  alphabetically - descending        (da)"+"\n"+"order by: ").lower()
			print
			amino=["V","I","L","E","Q","D","N","H","W","F","Y","R","K","S","T","M","A","G","P","C"]
			amin0=["Val","Ile","Leu","Glu","Gln","Asp","Asn","His","Trp","Phe","Tyr","Arg","Lys","Ser","Thr","Met","Ala","Gly","Pro","Cys"]
			w="".join(tps)
			for aa in range(0,len(amino)):
				numa=w.count(amino[aa])
				histlist=histlist[:]+[(amin0[aa],numa)]
										#generates histograms
			if histoptions=="an": 
				histlist=sorted(histlist,key=lambda x:(x[1]))
				for i in range(len(histlist)):
							if histlist[i][1]==0:
								continue    # DOESNT SHOW AMINO ACID WITH 0 OCCURENCE
							else:
								print  histlist[i][0],'(',"%3i"%histlist[i][1],'\b)',":",histlist[i][1]*"*"	
			if histoptions=="dn":
				histlist=sorted(histlist,key=lambda x:(x[1]),reverse=True)
				for i in range(len(histlist)):
							if histlist[i][1]==0:
								continue
							else:
								print  histlist[i][0],'(',"%3i"%histlist[i][1],'\b)',":",histlist[i][1]*"*"			
			if histoptions=="aa":
				histlist=sorted(histlist,key=lambda x:(x[0]))
				for i in range(len(histlist)):
							if histlist[i][1]==0:
								continue
							else:
								print  histlist[i][0],'(',"%3i"%histlist[i][1],'\b)',":",histlist[i][1]*"*"		
			if histoptions=="da":
				histlist=sorted(histlist,key=lambda x:(x[0]),reverse=True)
				for i in range(len(histlist)):
							if histlist[i][1]==0:
								continue
							else:
								print  histlist[i][0],'(',"%3i"%histlist[i][1],'\b)',":",histlist[i][1]*"*"	
	
			
	if main_menu=="S": #visualising secondary structures

		print "Secondary Structure of the PDB id "+str(pdbfile)	
		for q in range(len(tps)):
			blanksec=len(tps[q])*"-" #creating a list of dashes as long the chain length to insert secondary stucturs
			blankseclist=list(blanksec)
			identifier=len(tps[q])*' '#creating a list of spaces as long the chain length to insert identifier
			identifierlist=list(identifier)	
			
			for line in lines:
				
				if "HELIX" in line: 
					for num in NUMBERS:
						if int(line[8:10])==num :
							if line[19]==CL[q]:
								for X in range(int(line[22:25]),int(line[34:38])+1):
									if X > len(tps[q]):
										continue #prevents program from crashing if the are amino acids in secodary structures that are not on the range of the sequence"
									else:
										blankseclist[X-1]='/'#helix
										identifierlist[int(line[22:25])]=str(num) #IDENTIFYING THE HELIX
						

				if "SHEET" in line:
					for num in NUMBERS:
						if int(line[8:10])==num:
							for alph2 in alpha:
								if line[13]==alph2:
									if line[32]==CL[q]:
										for w in range(int(line[23:26]),int(line[34:37])+1):
											if w > len(tps[q]):
												continue 
											else:
												blankseclist[w-1]='|' #sheet
												identifierlist[int(line[23:26])]=str(num) #IDENTIFYING BETA SHEET
												identifierlist[int(line[23:26])+1]=str(alph2) 
						
			blanksec="".join(blankseclist)
			identifier="".join(identifierlist)
			a=0
			print "Chain "+str(CL[q])+":"
			print "(1)",
			for v in range(len(tps[q])):
					if v%80==0:
						print tps[q][a:v],"\b","\n",blanksec[a:v],"\b","\n",identifier[a+1:v]
						a=v
			print tps[q][a:],"\b","\n",blanksec[a:],"\b","\n",identifier[a+1:]
			print "("+str(len(tps[q]))+")"


	if main_menu=="M": # file manipulation
		while options!= "M":
			print "Choose one of the Manipulation Options:","\n","List(L)   Edit(E)   New(N)   Remove(R)   Main Menu(M)"
			options=raw_input(": ").upper()
			if options=="L":
				helixorsheet=raw_input("Do you want to list the Helix (H) or the Sheet (S): ").upper()
				a=0
				for i in lines:
					if "HELIX" in i:
					
						a=a+1
				if helixorsheet=="H":
					Q=1
					#obtaining positions 
					for line in lines:
						if "HELIX" in line:
					
							strip=line[8:10]
							strip=strip.strip(" ")
							if int(strip)==Q:
								serNum=line[7:10].strip(" ")
								helixID=line[11:14].strip(" ")
								initResName=line[15:18].strip(" ")
								initChainID=line[19].strip(" ")
								initSeqNum=line[21:25].strip(" ")
								initICode=line[25].strip(" ")
								endResName=line[27:30].strip(" ")
								endChainID=line[31].strip(" ")
								endSeqNum=line[33:37].strip(" ")
								endICode=line[37].strip(" ")
								helixClass=int(line[38:40])
								if helixClass==1:
									helixClass="Right-handed alpha"
								if helixClass==2:
									helixClass="Right-handed omega"
								if helixClass==3:
									helixClass="Right-handed pi"
								if helixClass==4:
									helixClass="Right-handed gamma"
								if helixClass==5:
									helixClass="Right-handed 3-10"
								if helixClass==6:
									helixClass="Left-handed alpha"
								if helixClass==7:
									helixClass="Left-handed omega"
								if helixClass==8:
									helixClass="Right-handed gamma"
								if helixClass==9:
									helixClass="2 - 7 ribbon/helix"
								if helixClass==1:
									helixClass="Polyproline"
								comment=line[40:70].strip(" ")
								length=line[71:76].strip(" ")
					

								print "Helix",Q,"of",a,":","\n"," serNum:     ",serNum,"\n"," helixID:    ",helixID,"\n"," initResName:",initResName,"\n"," initChainID:",initChainID,"\n"," initSeqNum: ",initSeqNum,"\n"," initICode:  ",initICode,"\n"," endResName: ",endResName,"\n"," endChainID: ",endChainID,"\n"," endSeqNum:  ",endSeqNum,"\n"," endICode:   ",endICode,"\n"," helixClass: ",helixClass,"\n"," comment:  ",comment,"\n"," length:     ",length
								Q=Q+1

				if helixorsheet=="S":
		
							Q=1
							for line in lines:

								if "SHEET" in line:
									strip=line[7:10]
									strip=strip.strip(" ")
									if int(strip)==Q:
										strand=line[7:10].strip(" ")
										sheetID=line[11:14].strip(" ")
										numStrands=line[14:16].strip(" ")
										initResName=line[17:20].strip(" ")
										initChainID=line[21].strip(" ")
										initSeqNum=line[22:26].strip(" ")
										initICode=line[27].strip(" ")
										endResName=line[27:31].strip(" ")
										endChainID=line[32].strip(" ")
										endSeqNum=line[33:37].strip(" ")
										endICode=line[37].strip(" ")
										sense=line[38:40].strip(" ")
										curAtom=line[45:48].strip(" ")
										curResName=line[33:37].strip(" ")
										curChainId=line[49].strip(" ")
										curResSeq=line[50:54].strip(" ")
										curICode=line[55].strip(" ")
										prevAtom=line[56:60].strip(" ")
										prevResName=line[60:63].strip(" ")
										prevChainId=line[64].strip(" ")
										prevResSeq=line[65:69].strip(" ")
										prevICode=line[69].strip(" ")
										a=0
										for i in lines:
											if "SHEET" in i:
					
												a=a+1

										print "Sheet",Q,"of",a,"\n"," strand:     ",strand,"\n"," sheetID:    ",sheetID,"\n"," numStrands: ",numStrands,"\n"," initResName:",initResName,"\n"," initChainID:",initChainID,"\n"," initSeqNum: ",initSeqNum,"\n"," initICode:   ",initICode,"\n"," endResName: ",endResName,"\n"," endChainID: ",endChainID,"\n"," endSeqNum:  ",endSeqNum,"\n"," endICode:  ",endICode,"\n"," sense:      ",sense,"\n"," curAtom:    ",curAtom,"\n"," curResName: ",curResName,"\n"," curChainId: ",curChainId,"\n"," curResSeq:  ",curResSeq,"\n"," curICode:   ",curICode,"\n"," prevAtom:   ",prevAtom,"\n"," prevResName:",prevResName,"\n"," prevChainId:",prevChainId,"\n"," prevResSeq: ",prevResSeq,"\n"," prevICode:  ",prevICode
										Q=Q+1

			if options=="E": # EDITING
				helixorsheet2=raw_input("Do you want to edit a Helix (H) or the Sheet (S): ").upper()
				if helixorsheet2=="H":
						hel=0
						for line in lines:
							if "HELIX" in line:
								hel=hel+1
								
						edit_options=raw_input("Which Helix do you want to edit (1-"+ str(hel)+"):")
						for line in lines:
							if "HELIX" in line:
								z=lines.index(line) #OBTAINING INDEX OF LINES WITH HELIX
								
								strip=line[8:10]
								strip=strip.strip(" ")
								if int(strip)==int(edit_options):
										if "HELIX" in line:
											initChainID=line[19].strip(" ")
											initSeqNum=line[21:25].strip(" ")
											endSeqNum=line[33:37].strip(" ")
											helixClass=int(line[38:40])
											comment=line[40:70].strip(" ")
									
						
											chain=raw_input(" Chain ["+str(initChainID)+"]:        ").upper()
											for w in range(len(CL)):
												if chain==CL[w]:
													#TO SAVE MODIFICATIONS MADE TO LINE, line is store in the variable a
													a=line[:19]+chain+line[20:]
													a=a[:31]+chain+a[32:]
													initSeq=raw_input(" initSeqNum ["+str(initSeqNum)+"]:  ")
													a=a[:15]+"%3s"%(aminot[tps[w][int(initSeq)]])+a[18:]
													print "That position correspond to the amino acid", aminot[tps[w][int(initSeq)]]
													a=a[:22]+"%3s"%(initSeq)+a[25:]
													endSeq=raw_input(" endSeqNum ["+str(endSeqNum)+"]:   ")
													zx=aminot[tps[w][int(initSeq)]]
													b= "%3s"%(zx,)
													a=a[:27]+b+a[30:]
													print "That position correspond to the amino acid", aminot[tps[w][int(endSeq)]]
													a=a[:34]+"%3s"%(endSeq)+a[37:]
													hclass=raw_input(" helixClass ["+str(helixClass)+"]:    ")
													print "The selected class was:", helix_class[int(hclass)]

													a=a[:40]+hclass+a[41:]
													com=raw_input(" comment:          ")
													a=a[:40]+"%31s"%com+a[40:70]
													lines[z]=a # a is inserted back in to the list of lines
											print "The Helix"+str(edit_options)+"has been successfully edited."

				if helixorsheet2=="S":
						sht=0
						shttup=[]
						A=""
						for line in lines:
							if "SHEET" in line:
								sht=sht+1
								shttup=shttup+[(sht,line[9],line[13])] # shit positions, plus identifiers
						print "Choose sheet you want to Edit: "
						for i in shttup:
							print str(i[0])+".",   str(i[1])+str(i[2])
						edit_options=raw_input("   :")
						for s in shttup:
							for line in lines:
								if "SHEET" in line and A!=1:
									z=lines.index(line)
									strip=line[8:10]
									strip=strip.strip(" ")
									if int(strip)==int(edit_options) and line[13]==shttup[int(edit_options)][2]: # using unique sheet nomeclature to pick out sheet
											if "SHEET" in line:
												initChainID=line[21].strip(" ")
												initSeqNum=line[22:26].strip(" ")
												endSeqNum=line[33:37].strip(" ")
												sheet=raw_input(" Sheet ["+str(initChainID)+"]:        ")
												for w in range(len(CL)):
													if sheet==CL[w]:

														a=line[:21]+sheet+line[22:]
														a=a[:32]+sheet+a[33:]
														initSeq=raw_input(" initSeqNum ["+str(initSeqNum)+"]:  ")
														a=a[:17]+"%3s"%(aminot[tps[w][int(initSeq)]])+a[20:]
														print "That position correspond to the amino acid", aminot[tps[w][int(initSeq)]]
														a=a[:23]+"%3i"%(int(initSeq))+a[26:]
														endSeq=raw_input(" endSeqNum ["+str(endSeqNum)+"]:   ")
														print "That position correspond to the amino acid", aminot[tps[w][int(endSeqNum)]]
														a=a[:28]+"%3s"%(aminot[tps[w][int(endSeq)]])+a[31:]
														a=a[:34]+"%3i"%int(endSeq)+a[37:]
														lines[z]=a
														A=1 # FOR BREAKING LOOP
												print "The Helix"+str(edit_options)+"has been successfully edited."



			if options=="N": # two blank lis were created to act as templates for cfreating either helices or shets
				helixorsheet2=raw_input("Do you want to Add a Helix (H) or the Sheet (S): ")
				a=0

				if helixorsheet2=="H":
						chain=raw_input(" Chain:           ").upper()
						for w in range(len(CL)):
							if chain==CL[w]:
								a=new_line[:19]+chain+new_line[20:]
								a=a[:31]+chain+a[32:]
								initSeq=raw_input(" initSeqNum:      ")
								a=a[:15]+"%3s"%(aminot[tps[w][int(initSeq)]])+a[18:]
								print "That position correspond to the amino acid", aminot[tps[w][int(initSeq)]]
								a=a[:22]+"%3s"%(initSeq)+a[25:]
								endSeq=raw_input(" endSeqNum:       ")
								zx=aminot[tps[w][int(endSeq)]]
								b= "%3s"%(zx,)
								a=a[:27]+b+a[30:]
								print "That position correspond to the amino acid", aminot[tps[w][int(endSeq)]]
								a=a[:34]+"%3s"%(endSeq)+a[37:]
								hclass=raw_input(" helixClass:      ")
								print "The selected class was:", helix_class[int(hclass)]
								a=a[:39]+hclass+a[40:]
								com=raw_input(" comment:      ")
								a=a[:40]+"%31s"%com+a[40:70] #new line inserted into lines

						helix=0
						z=0
						for line in lines:
							if "HELIX"== line[0:5]:
								helix=helix+1
						helix=helix+1
						a=a[:9]+str(helix)+a[10:]
						a=a[:13]+str(helix)+a[14:]
						for line in lines:
							if "HELIX" == line[0:5]:
								z=lines.index(line)
					
						lines=lines[:z+1]+[a]+lines[z+1:]

						print "The Helix "+str(helix) +" has been successfully created."


				if helixorsheet2=="S":
					a=""

					sheet=raw_input(" Sheet chain:")
					for w in range(len(CL)):
						if sheet==CL[w]:
							a=new_sheet[:21]+sheet+new_sheet[22:]
							a=a[:32]+sheet+a[33:]
							strand=raw_input("strand Number: ")
							a=a[:9]+str(strand)+a[10:]
							sheetid=raw_input("enter Sheet ID: ")
							a=a[:13]+(sheetid)+a[14:]
							initSeq=raw_input(" initSeqNum :  ")
							print "That position correspond to the amino acid", aminot[tps[w][int(initSeq)]]
							a=a[:17]+"%3s"%(aminot[tps[w][int(initSeq)]])+a[20:]
							a=a[:23]+"%3i"%int(initSeq)+a[26:]
							endSeq=raw_input(" endSeqNum:   ")
							print "That position correspond to the amino acid", aminot[tps[w][int(endSeq)]]
							a=a[:28]+"%3s"%(aminot[tps[w][int(endSeq)]])+a[31:]
							a=a[:34]+"%3i"%int(endSeq)+a[35:]
		
		
					z=0
					sheet=0
					for line in lines:
						if "SHEET"== line[0:5]:
							z=lines.index(line)
					
					lines=lines[:z+1]+[a]+lines[z+1:]
					for line in lines:
						if "SHEET"== line[0:5]:
							sheet=sheet+1
					print "The sheet"+str(sheet)+" has been successfully created."

			if options=="R":
				helixorsheet3=raw_input("Do you want to remove a Helix (H) or the Sheet (S): ").upper()
				if helixorsheet3=="H":
					hel1=0
					for line in lines:
							if "HELIX" in line:
								hel1=hel1+1
					edit_options=raw_input("Which Helix do you want to delete (1-"+ str(hel1)+"):").upper()

					sure=""
					for line in lines:
						if "HELIX" in line:
							strip=line[8:10]
							strip=strip.strip(" ")
							if int(strip)==int(edit_options):
								sure=raw_input("Are you sure you want to delete the helix?"+"\n"+str(line)+"Y/N? ").upper()
			
					if sure=="Y":
						for line in lines:
							if "HELIX" in line:
								strip=line[8:10]
								strip=strip.strip(" ")
								if int(strip)==int(edit_options):
									z=lines.index(line)
									lines[z]= "" # deleting helics
									print "The helix "+ str(edit_options)+" has been successfully removed"

				if helixorsheet3=="S":
					SHT=0
					for line in lines:
							if "SHEET" in line:
								SHT=SHT+1
					sure=""
					sht=0
					shttup=[]
					for line in lines:
						if "SHEET" in line:
							sht=sht+1
							shttup=shttup+[(sht,line[9],line[13])]
					print "Choose sheet you want to Edit: "
					for i in shttup:
						print i[0],".",str(i[1])+str(i[2])
					edit_options=raw_input("enter sheet number   :")
					for s in shttup:
						for line in lines:
							if "SHEET" in line:
								z=lines.index(line)
								strip=line[8:10]
								strip=strip.strip(" ")
								if int(strip)==int(edit_options):
									if line[13]==shttup[int(edit_options)][2]:
										sure=raw_input("Are you sure you want to delete the sheet?"+"\n"+str(line)+"Y/N? ").upper()
			
										if sure=="Y":
											z=lines.index(line)
											lines[z]= ""
											print "The sheet "+ str(edit_options)+" has been successfully removed"


	if main_menu=="X":
			import datetime
			v=''
			for line in lines:
				if "HEADER" == line[:6]:

					k=str(datetime.datetime.today()) # generates date
					v = line[:50]+k[0:10]+line[60:]
			lines[0]=v

			import os
			expfpath=""
			import os.path
			
		
			while expfpath=="":
				expfpath=raw_input("File path: ")
				f=os.path.exists(expfpath)
				if f==True:
					print "the file "+expfpath+" already exists"
					overwrite=raw_input("Do you want to over write file "+expfpath+" \n"+"Y/N?").upper()
					if overwrite=="Y":
						with open(expfpath,"w") as f:
							f.write("".join(lines)) #writing output file
							print "File SAVED."
					if overwrite=="N":
						expfpath=""

				else:
					if expfpath !="":
						with open(expfpath,"w") as f:
							f.write("".join(lines)) #writing output file
							print "File SAVED."
					options=raw_input("Press [enter] to go back to the main menu")
					if options=="":
						options="M"


	
		
		
	






				
				
