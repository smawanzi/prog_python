#Somme de Gauss    
n = int(input("Saissez un nombre entier naturel :"))
k = 2
S = 1
while k <= n :
   S = S + k
   k = k+1
print ("La somme de Gauss de rang n vaut : ",S)
