#Exercice corrigé n° 9 : Programme convertissant une durée en heures, minutes et secondes | Python
s = int(input("Saisir la durée en secondes : "))
min = None 
h = None

h = s//3600
min = (s % 3600) // 60
s = (s % 3600) % 60
print(f"La durée est {h}h {min}min {s}s")

