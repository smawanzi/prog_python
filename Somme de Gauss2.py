n = int(input("Veuillez saisir un entier naturel n non nul : "))
S = 0
for k in range (1,n+1) :
    S = S + (k*k)
print ("La somme de Gauss de rang n vaut : ", S)
