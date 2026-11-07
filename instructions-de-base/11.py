# Exercice corrigé n° 11 : Programme de calcul de la résistance en série et en parallèle | Python
R1 = float(input("Veuillez Entrer la valuer de R1 : "))
R2 = float(input("Veuillez Entrer la valuer de R2 : "))
R3 = float(input("Veuillez Entrer la valuer de R3 : "))
Req_serie = R1 + R2 + R3
Req_parallel = (R1 * R2 * R3)/(R1*R2 + R1*R3 + R2*R3)
print(f"En serie : Rea = {Req_serie:.2f}")
print(f"En prallèle : Req = {Req_parallel:.2f}")