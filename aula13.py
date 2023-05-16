# Formatação de Strings

nome = "Wagner Mesquita"
altura = 1.71
peso = 55
imc = peso / (altura * altura)

linha_1 = f"{nome} tem {altura:.2f} de altura"
linha_2 = f"pesa {peso} quilos e seu imc é"
linha_3 = f"{imc:.2f}"

print(linha_1)
print(linha_2)
print(linha_3)

print(nome,"tem um imc de: ", imc)

"""
if imc <= 18.5
    print("Sua classificação é magreza ")
"""
