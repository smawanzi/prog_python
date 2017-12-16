montantdesdommages = int (input("saisir le montant des reparations:"))
franchise = int (montantdesdommages * 0.1)


if (franchise <= 15):
	franchise=15
elif franchise >=500:
	franchise=500
print ("il reste à votre charge :",franchise)
print ("le montant rembourser est donc :",montantdesdommages-franchise)
