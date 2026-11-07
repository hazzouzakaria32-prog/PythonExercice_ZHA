#Exercice corrigé n° 13 : Programme qui modifie le contenu de deux variables en fonction d’une condition...
a = int(input("Entrez un nombre entier : "))
b = int(input("Entrez un nombre entier : "))

cas = 0
#has_samesign = False
if a * b >= 0 :
    #has_samesign = True
    cas = 1
    a = a + b
    b = a - b
    a = a - b
else :
    cas = 2
    a = a + b
    b = ( a - b ) * b
if cas == 1 :
    print(f"la nouvelle valuer de a = {a} ")
    print(f"la nouvelle valuer de b = {b} ")
elif cas == 2 :
    print(f"la nouvelle valuer de a = {a} ")
    print(f"la nouvelle valuer de b = {b} ")
else :
    print("######")