note = float(input("Entrez votre note: "))
if note >= 10:
    print ("Vous avez {} de moyenne,vous êtes Admis".format(note))
elif note < 8:
     print("Vous avez {} de moyenne,vous êtes Ajourné".format(note))
else:
    print ("Votre note est de {},vous devez passer l'Oral de rattrapage".format(note))
