C = float(input("\nVeuillez saisir le capital initial : "))
t = float(input("\nVeuillez saisir le taux d'intérêt annuel: "))
d = int(input("\nVeuillez saisir la durée du placement : "))
c = C
for k in range(1,d+1) :
    c = c*(1+t/100)
print("\nLe capital dont vous disposerez au bout de",d,"années de placement sera de",round(c,2),"€\n")


