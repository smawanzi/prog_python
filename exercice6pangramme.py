phrase=input("Entrer une phrase : ").upper
alphabet = "abcdefghijklmnopqrstuvwxyz"
phraseLetters = ""
for letter in alphabet:
    if alphabet == 26:
        print("c'est un pangrame",phraseLetters,alphabet)
    else:
        print ("ce n'est pas un pangramme",phraseLetters,alphabet)
