from random import*
n=randrange(1,100)
gagne=False
inc=0

while gagne==False and inc<10:
    inc+=1
    s=int(input(""))

    if s==n:
        gagne=True
        print(" Gagné!!")
    else:
        if s>n:
            print("le nombre est plus petit")
        else:
            print("le nombre est plus grand")
            
