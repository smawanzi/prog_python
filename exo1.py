#exercice 1:"Le résultat affiché"

n=int(input("entrer un entier naturel non nul : "))
k=0
while k<n:
    
    print(3*k+1,end="")
    
    if k!=n-1:
        print(" - ",end="")   
