n = int(input("saisir le nb : "))
bin,q = [],n
while n//2 !=0:
    bin = [q%2] + bin
    q = q//2
bin = [q%2] + bin
print("l'écriture binaire de l'entier",n,"est ")
for k in range(len(bin)):
    print(bin[k],end='')

print()
print()
bin= input("entrer l'écriture binaire a convertir en entier: ")
for k in range(len(bin)):
    p = int(bin(len(bin)
