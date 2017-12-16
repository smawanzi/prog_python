def rang(lettre):
    rg=alphabet.index(lettre)
    return(rg)
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
phrase1=input("phrase à coder").upper()
decal=int(input("decalage choisi"))
phrase2=""
for lettre in phrase1:
        if lettre!=" ":
            x=rang(lettre)
            y=(x+decal)%26
            phrase2=phrase2+alphabet[y]
        else:
                phrase2=phrase2+lettre

print("la phrase qui sera saisie sera codée en:",phrase2) 
