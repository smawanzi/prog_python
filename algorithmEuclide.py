# algo d'euclide
c=int(input("saisir un entier a : "))
b=int(input("saisir en entier b : "))
while c%b != 0 :
    c , b= b,c%b
print ("le PGCD est : ",b)


