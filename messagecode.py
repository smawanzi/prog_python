def phraseCodée(message):
    messageCodé = ''
    aplhabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for car in message:
        if trouveLettre(car)!=1:
            messageCodé = messageCodé + alphabet[trouveLettre(car) + 13 %26]
        else:
            messageCodé = messageCodé+car
    return(messageCodé)        
message=input("entrer un message a coder :").upper()
print("apres ROT13, le message devient : ",phraseCodée(message))
