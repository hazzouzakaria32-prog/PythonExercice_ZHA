#Exercice corrigé n° 5 : Programme d'opérations : somme, produit, soustraction et division | Python
def doNothing():
    pass
a = float(input("Veuillez entrez la valeur de a : "))
b = float(input("Veuillez entrez la valeur de b : "))

somme = a + b
diffrence = a - b
produit =  a * b
qutient = None 
qutient =  a / b if b != 0 else doNothing()
print(f"{a} + {b} = {somme:.2f}")
print(f"{a} - {b} = {diffrence:.2f}")
print(f"{a} * {b} = {produit:.2f}")
print(f"{a} / {b} = {"FI" if qutient == None else qutient:.2f}")
