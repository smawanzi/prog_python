#Le compte sur  Livret 
c = int(input("Saissez un la valeur de votre capital initial sur le compte :"))
i = float(input("Saissez un la valeur des intérêts composés par an :", ))
n = int(input("Saisissez la durée de placement :"))
for k in range(n+1):
   c = c*(1+i/100)
print (round(c,2))
for k in range(n*2):
   c = (c*(1+i/100))*2
print (round(c,2))
