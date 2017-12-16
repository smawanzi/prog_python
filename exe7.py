chaine = input("Veuillez saisir votre phrase: ")
phrase = ""
for car in chaine:
    n=ord(car)
    print (n)

    if car!=" ":
        n=n-32
        phrase = phrase+chr(n)
    else:
        phrase = phrase+" "
    
print(phrase)
