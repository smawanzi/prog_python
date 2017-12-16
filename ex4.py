#Exercice 4
phrase=input("Entrez une phrase: ")
phrase1="RESSASSER"
phrase2="ESOPE RESTE ICI ET SE REPOSE"
palin1=""
palin2=""
i=0
j=0
k=len(phrase1)-1
l=len(phrase2)-1

for i in range(0,len(phrase1)):
    palin1 = palin1 + phrase1 [k]
    k = k-1

print("",palin1,"")
print("RESSASSER")
print("")

for j in range(0,len(phrase2)):
    palin2 = palin2 + phrase2 [l]
    l = l-1

print("",palin2,"")
print("ESOPE RESTE ICI ET SE REPOSE")
print("")    
