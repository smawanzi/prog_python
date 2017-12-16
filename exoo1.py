salut = input("Écrire votre phrase : ")
slt = len(salut)

print(slt)

for caractere in phrase:
    if slt<len(phrase)-1:
        print (caractere,"+",)
        slt=slt+1
    else:
        print (caractere,)
