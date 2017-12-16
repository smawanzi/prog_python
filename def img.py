def image(n):
liste_s =[[randrange(1,100)] for i in range (1,n)]
    for liste_s in range(1,n):
        if liste_s > n:
            print(n,"est compris dans la liste succesive")
        else:
            print("cette entier",n,"n'est pas dans la liste")
n=int(input("entrer un eaturel non nul : "))
return (image(n))            
