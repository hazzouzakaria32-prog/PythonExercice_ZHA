#Exercice corrigé n°10 : Programme qui calcule la distance entre deux points A et B sur le plan
Xa = float(input("Veuillez saisir l'abscisse de A : "))
Ya = float(input("Veuillez saisir l'ordonnée de A : "))


Xb = float(input("Veuillez saisir l'abscisse de B : "))
Yb = float(input("Veuillez saisir l'ordonnée de B :" ))
# les coordonnées de vecteur AB
Xab = Xb - Xa
Yab = Yb - Ya
# les coordonnées de vecteur BA
Xba = -Xab
Yba = -Yab
# la distances
AB = ( (Xab)**2 + (Yab)**2 )**0.5
print(f"soit le point A({Xa};{Ya})")
print(f"soit le point B({Xb};{Yb})")
print(f"le vecteur AB({Xab};{Yab})")
print(f"le vecteur BA({Xba};{Yba})")
print(f"la distance AB = {AB}")