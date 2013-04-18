def getPoints(listx):
	listw=[]
	for i in range(len([listx])):
		tup1=()
		if [listx][i][2]>[listx][0][3]:
			tup1=tup1+([listx][i][0],)
			tup1=tup1+(3,)
			listw=listw+[(tup1)]

			tup1=()
			tup1=tup1+([listx][i][1],)
			tup1=tup1+(0,)
			listw=listw+[(tup1)]

		if [listx][i][2]<[listx][0][3]:
			tup1=tup1+([listx][i][1],)
			tup1=tup1+(3,)
			listw=listw+[(tup1)]

			tup1=()
			tup1=tup1+([listx][i][0],)
			tup1=tup1+(0,)
			listw=listw+[(tup1)]
		if [listx][i][2]==[listx][0][3]:
			tup1=tup1+([listx][i][0],)
			tup1=tup1+(1,)
			listw=listw+[(tup1)]
			tup1=()
			tup1=tup1+([listx][i][1],)
			tup1=tup1+(1,)
			listw=listw+[(tup1)]
	return listw


list1=["g","i",2,44]
print getPoints(list1)
