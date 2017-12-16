Débutheure=int (input("*Heures de début: "))
Débutminute=int (input("*Minutes de début: "))
Finheure=int (input("*Heures de fin: "))
Finminute=int (input("*Minutes de fin: "))
Débuttemps=float (Débutheure+(Débutminute/60))
Fintemps=float (Finheure+(Finminute/60))
if Débuttemps>Fintemps:
    print("erreur: changement de journée")
else:
    Minute=float((Fintemps-Débuttemps)*60)
    Heure=int(0)
    while Minute>=60:
        Minute=Minute-60
        Heure=Heure+1
    Minute=int (Minute)
    print("La durée est de {}h{}".format(Heure, Minute))

