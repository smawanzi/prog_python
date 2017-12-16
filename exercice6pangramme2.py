Alpha = "abcdefghijklmnopqrstuvwxyz"
phrase = input("Entrer une phrase : ").lower()
compteur= 0
for lettre in Alpha:
    if lettre in phrase:
        compteur+=1
if compteur == 26:
    print("la phrase",phrase,"c'est un pangramme il y a 26 lettre")
else:
    print("la phrase",phrase,"ce n'est pas un pangramme",compteur,"parmi les 26 lettre de l'alphabet",26-compteur)
    
