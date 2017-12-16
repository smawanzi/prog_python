#while

n = int(input("Entrer n = "))
k = int(input("Combien de multiples ? k="))
i=1
while i<=k:
    print(i,'x',n,'=',i*n)
    i+=1
#For
n = int(input("Entrer n = "))
k = int(input("Combien de multiples ? k="))
for i in range(1,k+1):
    print(i,'x',n,'=',i*n)
