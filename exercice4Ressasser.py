phrase , phrase1 = input("Entrer une phrase à tester: ").upper(),""
phrase_inversée = ""
for lettre in phrase:
    if lettre != " ":
        phrase1 = phrase1 + lettre
        phrase_inversée = lettre + phrase_inversée
print(phrase1)
print(phrase_inversée)

if phrase1 == phrase_inversée:
    print("la phrase,",phrase,"est un palindrome.")
else:
    print("la phrase,",phrase,"n'est un palindrome.")
    for K in range(len(phrase1)):
        if phrase1[K]!= phrase_inversée[K]:
            print("la première lettre different est celle en position: ",K)
            break

#exo6
#Monsieur Jack, vous dactylographiez bien mieux que votre ami Wolf
#Buvez de ce Whisky que le patron juge Fameux
