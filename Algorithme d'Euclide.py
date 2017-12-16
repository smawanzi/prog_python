a = int(input("Veuillez saisir l'entier a : "))
b = int(input("Veuillez saisir l'entier b : "))
while a%b != 0 :
    a,b = b,a%b
print("Le PGCD de",a,"et de",b,"est :",b)
