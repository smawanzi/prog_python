a1=int(input("Saisir un entier a: "))
b1=int(input("Saisir un entier b: "))
a,b=a1,b1
while a%b!=0:
    a,b=b,a%b
print ("Le PGCD de {} par {} est {}".format(a1, b1, b))
