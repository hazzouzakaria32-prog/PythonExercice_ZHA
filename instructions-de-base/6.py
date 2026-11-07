#Exercice résolu n° 6 : Programme permettant de calculer et d'afficher la somme et la moyenne de notes | Python

Note1 = float(input("Entrez la première note numéro 1 : "))
Note2 = float(input("Entrez la deuxième note numéro 2 : "))
Note3 = float(input("Entrez la troizème note numéro 3 : "))
Note4 = float(input("Entrez la quatrème note numéro 4 : "))
Note5 = float(input("Entrez la cinquème note numéro 5 : "))

Somme = Note1+ Note2 + Note3 + Note4 + Note5
Moyenne = Somme / 5
print(f"La somme des notes est {Somme:.2f}")
print(f"La Moyenne des notes est {Moyenne:.2f}")
