nbbonnereponse = float(input("Entrez le nombre de bonne réponses: "))

if nbbonnereponse <= 10:
    print("Appréciation : faible")
elif 10 < nbbonnereponse <=20:
    print("Appréciation : passable")
else:
    print("appréciation : bien")