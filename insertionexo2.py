#Exercice 2
#des tableau et echange#
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

#le tri#
from random import*
n=int(input("entrer l'entier naturel n: "))
tab =[randrange(1,100)for i in range(n)]
print("\n")
print ("Tableau aléatoire initial: ','\n")
tableau(tab)

for k in range(n):
    for l in range(n-1):
        if tab[l]>tab[l+1]:
            c=tab[l]
            d=tab[l+1]
            tab[l]=d
            tab[l+1]=c
            
print("\n")
print("Tableau trié par bulle :","\n")
tableau(tab)        
