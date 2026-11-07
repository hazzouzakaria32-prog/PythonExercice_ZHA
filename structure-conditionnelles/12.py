#Exercice corrigé n° 12 : Programme qui indique si deux nombres sont de même signe ou non | Python
a = int(input("Entrez un nombre entier : "))
b = int(input("Entrez un nombre entier : "))
if a==0 or b == 0:
    print("Ont le meme signe")
elif abs(a+b) == abs(a)+abs(b) :
    print("Ont le meme signe")
else : # L < R
    print("Les signes différents")
