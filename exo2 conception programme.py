#Conception d'un programme

from random import*
n=randrange(1,100)
GG=False
nc=0

while GG==False and nc<10:
    nc+=1
    i=int(input("Saisisser un entier :"))

    if i==n:
        GG=True
        print("Vous avez Gagné !")
    else:
        if i>n:
            print("le nombre est plus petit")
        else:
            print("le nombre est plus grand")
