a=int(input("saisir un entier:"))
b=int(input("saisir un entier:"))

while (a%b!=0) :
    a= b
    b= a%b

print("afficher le PGCD: ",b)
