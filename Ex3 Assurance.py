montant = int(input("Saisir un montant"))
montant = montant*(10/100)
if (montant<15):
    print('Votre franchise est à 15€')
elif (montant>50):
    print('Votre franchise est à 50€')
