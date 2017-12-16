nom = input('Nom :')
prenom = input('Prenom :')
age = int(input('Age :'))
if age >= 18:
    print("Votre nom est {},votre prénom est {} vous avez {} ans, vous êtes majeur".format(nom, prenom, age))
else:
    print("Votre nom est {},votre prénom est {} vous avez {} ans, vous êtes mineur".format(nom, prenom, age))
