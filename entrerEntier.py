#While
n,i = int(input("Entrer un entier n: ")), 0
while (i<=n):
    print(i)
    i += 1


#For

n = int(input("Entrer un entier n: "))
for i in range(0,n+1):
    print(i,end=' ')

#Compte à rebours WHILE
    
n= int(input("Entrer un entier n: "))
i = n
while i>=0:
    print(i,end=' ')
    i -= 1
    print('BIIIM')    

#Compte à rebours FOR

n= int(input("Entrer un entier n: "))
i = n
for i in range(0,n+1):
    print(i,end=' ')
    i -= 1
    print('BIIIM')      


#Table de Multiplication

nb = int (input("entrer un nombre : "))
valeur = int(input("entrer un nombre : "))
resultat =  0

while (nb <= 10):
    print(resultat = nb*valeur)
    resultat =nb*valeur
    nb += 1
