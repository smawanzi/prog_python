mot = input("Veuillez saisir votre phrase: ")
mot = mot.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
a=0
motLettre = " "
for car in mot:
    for char in alphabet:
        if car == char and char not in motLettre:
            motLettre += car
for car in motLettre:
    for char in alphabet:
        if car == char:
            a += 1
if a==26:
    print("cette phrase est un pangramme")
else:
    print("cette phrase n'est pas un pangramme")
