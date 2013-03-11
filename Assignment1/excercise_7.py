mlp=[]
mi=[]
mp=[]
mostpop=[0,0,0,0]
richest=[0,0,0,0]
smallest=[0,100000000000000000000000000,0,0]
counter=1
while counter <= 7:
	cityname=raw_input("name of city?: ")
	population=raw_input("what is the population?: ")
	capital=raw_input("is this city a Capital? yes or no?: ")
	income=raw_input("what is the income?: ")


	if capital=="yes":
		mp.append(cityname)
		mp.append(population)
		mp.append(capital)
		mp.append(income)
		if int(mp[1])>int(mostpop[1]):
				mostpop=mp[:]
		if int(population) >= 100000:
			mlp.append(cityname)
			mlp.append(population)
			mlp.append(capital)
			mlp.append(income)

			if int(mlp[1])<int(smallest[1]):
				smallest=mlp[:]
		elif int(population) < 100000:
			mi.append(cityname)
			mi.append(population)
			mi.append(capital)
			mi.append(income)
			
			if int(mi[3])>int(richest[3]):
				richest=mi[:]
			
	if capital=="no":
		if int(population) > 200000:
			if income>= 720000000:
				mlp.append(cityname)
				mlp.append(population)
				mlp.append(capital)
				mlp.append(income)

				if int(mlp[1])<int(smallest[1]):
					smallest=mlp[:]
		elif int(population) <= 200000 or income < 720000000:
			mi.append(cityname)
			mi.append(population)
			mi.append(capital)
			mi.append(income)
			
			if int(mi[3])>int(richest[3]):
				richest=mi[:]
					
	counter = counter +1
print "the richest non metropoly is", richest[0], "with an income of", richest[3]
print "the smallest metropoly is", smallest[0], "with a population of", smallest[1]
print "the capital city with the most population is", mostpop[0], "with a population of",mostpop[1]

