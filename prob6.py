def prob6 (mylist):
	longitud = len(mylist)
	for i in range (longitud):
		for j in range (i + 1, longitud):
			if mylist[i] < mylist[j]:
				variable = mylist[j]
				mylist[j] = mylist[i]
				mylist[i] = variable
	return mylist

