"""
nomes = ["João", "Wagner", "Anderson"]
for n in nomes:
    print(n)
    if "João" in nomes:
        print("Tem Jõao nos nomes")
    elif "Wagner" in nomes:
        print("Tem Wagner nos nomes")
    elif "Anderson" in nomes:
        print("Tem Anderson nos nomes")
    else:
        print("Alguns nomes não foram encontrados")
    break

print("Saia")
"""


"""
while True:
    pessoas = int(input("Qual é o seu idade? "))
    if pessoas > 500:
        print("Você chegou no idade máxima que foi pedida")
        break
print("Sai do programa")
"""
idade =  str(print("Informe a sua idade: "))
condicao = True
while condicao:
    if idade >= "18":
     print("Você já completou a maioridade")
    break
