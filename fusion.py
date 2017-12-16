from random import*
n1 = int(input("Entrez le nombre de nombres qui composent la liste 1: "))
tab1 = []
for k in range(0, n1):
        tab1 = tab1 + [randrange(1,100)]
        if k%10==9:
                print(tab1[k])
        else:
                print(tab1[k],"\t",end=" ")
print("La liste 1 triée donne: ")
tab1.sort()
for k in range(0, n1):
        if k%10==9:
                print(tab1[k])
        else:
                print(tab1[k],"\t",end=" ")
print("")
n2 = int(input("Entrez le nombre de nombres qui composent la liste 2: "))
tab2 = []
for k in range(0, n2):
        tab2 = tab2 + [randrange(1,100)]
        if k%10==9:
                print(tab2[k])
        else:
                print(tab2[k],"\t",end=" ")
print("")
print("La liste 2 triée donne: ")
tab2.sort()
for k in range(0, n2):
        if k%10==9:
                print(tab2[k])
        else:
                print(tab2[k],"\t",end=" ")
print("")
tab1 = tab1 + tab2
tab1.sort()
n3 = n1 + n2
for k in range(0, n3):
    if k%10==9:
        print(tab1[k])
    else:
        print(tab1[k],"\t",end=" ")
