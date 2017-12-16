#Table de Multiplication
n = int(input("Saissez un nombre entier naturel non nul :"))
m = int(input("Saissez la table de multiplication que vous voulez :"))
for k in range(n+1):
    print ("La multiplication est de : ",m,"x",k,"=",m*k)
