nombre=int(input("Saisissez un nombre entier que vous souhaitez: "))

nombre_decimal=nombre
if nombre==0:

    print("Le nombre 0 en base 10 équivaut à 0 en base 2.")

else:

    while nombre!=0:

        quotient=nombre//2

        reste=nombre%2

        print(quotient)

        print(reste)

        nombre=quotient

print("\nLe nombre",nombre_decimal,"")
