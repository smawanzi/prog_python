#Exercice 1

from random import *

nbn = int(input("entrer le nb a trier : "))
tab = []
for k in range(nbn):
    tab=tab+[randrange(1,100)]
    if k%10==9:
        print(tab[k])
    else:
        print(tab[k],"\t",end=" ")                
#Exercice 2
print("tableau définit")
def tableau(tab):
    for k in range(len(tab)):
        if k%10==9:
            print(tab[k])
        else:
            print(tab[k],"\t",end=" ")


def échange (a,b):
    a=a+b
    b=a-b
    a=a-b
    return (a,b)

from random import*
n=int(input("entrer l'entier naturel n: "))
tab =[randrange(1,100)for i in range(n)]
print("\n")
print ("Tableau aléatoire initial: ','\n")
tableau(tab)
l=0
for k in range(n):
    for l in range(n-1):
        if tab[l]>tab[l+1]:
            c=tab[l]
            d=tab[l+1]
            tab[l]=d
            tab[l+1]=c
            d=0
            c=0
print("\n")
print("Tableau trié par bulle :","\n")
tableau(tab)   
