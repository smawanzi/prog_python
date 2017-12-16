#exercice 1 tri l'insertion                                                   

from random import *

n = int(input("entrer le nb a tier : "))
tab = []
i = int(input(""))
for k in range(i,n):
    print ("Tableau aléatoire initial: ','\n")
    for i in range(k):
        if tab[i]>tab[k]:
            for j in range(i,k):
                tab[i] = tab[j] - tab [k]
                tab[k] = tab[j] - tab [k]
                tab[j] = tab[j] - tab [k]
    print(tab[k])
tableau(tab[k])    

#Exercice 2 tri par bulle

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
