cityname=raw_input("name of city")
population=raw_input("what is the population")
capital=raw_input("is this city a Capital? yes or no")
income=raw_input("what is the income")

if capital=="yes":
	if int(population) > 100000:
		print cityname, "is a metropoly"
	elif int(population) < 100000:
		print cityname, "is not a metropoly because population is less than 100000 "
if capital=="no":
	if int(population) > 200000:
		if income>= 720000000:
			print cityname, "is a metropoly"
		elif income< 720000000:
			print cityname, "is not a metropoly because income is less than 720000000"
	elif int(population)< 200000:
		print cityname, "is not a metropoly because population is less than 200000 for a non-capital city"
