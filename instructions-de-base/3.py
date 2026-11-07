#Exercice corrigé n° 3 : Programme qui calcule le périmètre et l'aire d'un rectangle | Python
largeur = float(input("la largeur : "))
longueur = float(input("la longueur : "))

perimetre = (largeur + longueur) * 2
surface = largeur * longueur

print(f"Périmètre  = {perimetre:.2f}")
print(f"Surface  = {surface:.2f}")