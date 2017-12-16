#Exercice 3
phrase=input("Entrez une phrase: ")
voyelles="aeiouyAEIOUY"
k=0
for car in phrase:
        if car in voyelles:
            k = k+1
print("La phrase saisie contient ", k," voyelle(s).")

