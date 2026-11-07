#Exercice corrigé n° 8 : Programme qui échange le contenu de deux variables | Python
a = int(input("La valuer de a : "))
b = int(input("La valuer de b : "))
temp = a
a = b
b = temp
a = a + b #la somme
b = a - b #b = la somme  - b = a_
a = a - b #a = la somme - a_ = b_
print(f"a = {a} et b = {b}") #echange 2 fois revient a la valeur intiale