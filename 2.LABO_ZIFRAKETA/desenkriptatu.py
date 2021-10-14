def estatistika (mezua) :
	agerpen = ['e', 'a', 'o', 'l','s', 'n', 'd','r', 'u', 'i', 't', 'c', 'p', 'm', 'y', 'q', 'b', 'h', 'g', 'f', 'v', 'j', 'ñ', 'z', 'x', 'k', 'w']
	estat = []
	kont = 0
	luzera = len(mezua.replace(" ", ""))
	print (str(luzera) + " karaketereko luzeera du! ")
	for i in range (65, 91):
		ch = chr(i)
		zenbat = mezua.count(ch)
		estat.append(((zenbat/luzera)*100, ch))

	estat.sort(reverse = True)

	for x in range (0, len(estat)) :
		mezua = mezua.replace(estat[x][1] , agerpen[x])

	#print (estat)
	print ("\n")
	print ("METODO MONOALFABETIKOAREKIN DESZIFRATUTAKO MEZUA : \n")
	mezua = mezua.lower()
	print (mezua)
	menu (mezua)


def menu (mezua) :
	print ("\n")
	print("\n           *TEXTUA ESTATISTIKAK JARRAITUZ DESZIFRATUA IZAN DA*      ")
	print("--------------------------------------------------------------------------------")
	jarraitu = input("\n Eskuz ordezkatu nahiko zenuke? (Y/N) : ")

	#Jarraitu nahi du
	if (jarraitu == 'Y' or jarraitu == 'y') :
		print ("\n")
		print ("\t\nOngi, jarraitu dezagun!")
		print ("\n")

		chZ = 'x'

		while (chZ != "quit" or chB != "quit") :
			print ("\t *Irten nahi baduzu, 'quit' idatzi ")
			chZ = input ("Zein karaktere ordezkatu nahi duzu? : \n")
			if (chZ == "quit" or chZ == "QUIT") :
				break
			chB = input ("Zein jarriko zenuke? : \n")
			if (chB == "quit" or chB == "QUIT") :
				break

			mezua = mezua.replace (chZ, chB)

			print ("\n" + chZ + "------->" + chB + "\n")
			print ("\tMEZUA: \n")
			print (mezua)
			print ("\n")


	print ("\n--> MEZU FINALA! : \n")
	print (mezua. upper())


katea = input("Sartu deszifratu nahi duzun mezua: \n")
estatistika(katea)
