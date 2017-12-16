def tableau(tab):
    for k in range(len(tab)):
        if k%10==9:
            print(tab[k])
        else:
            print(tab[k],"\t",end=" ")


def échange (a,b):
    a = a + b
    b = a - b
    a = a - b
    return(a,b)



from random import*

n=int(input("ebtrer le nombre d'éléments de la liste : "))
tab=[randrange(1,100)for i in range(n)]
print("\n")
print("Tableau aléatoire initial :\n")
tableau(tab)
print ("\n")
print("Tableau trié par sélection :")
for k in range (n-1,-1,-1):
    p=tab.index(max(tab[:k+1]))
    if p!=k:
        (tab[k],tab[p])=échange(tab[k],tab[:p])
print("\n")
tableau(tab)
