from random import*
n= int(input("entrez le nombre n d'�l�ments de la liste � trier: "))
tab = []
for k in range(n) :
    tab = tab + [randrange(1,100)]
    if k%10 == 9:
        print (tab[k])
    else:
        print (tab[k],"\t",end=" ")