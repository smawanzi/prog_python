C = float(input("entrer un capital: "))
n = float(input("entrer un taux de i: "))
i = int(input("entrer une année : "))
d = 2*C
for k in range(1,n+1):
    C = C*(1+i)
    if C>=d:
            print("Le taux capital double",k,"années")
            print("Il vaut alors",round(C,2),"euros")
            break
