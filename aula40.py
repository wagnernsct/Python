# Calculadora com while
while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite um operador (+-/*): ")
    ###########
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None


    if numeros_validos is None:
        print("Um ou ambos dos números são inválidos")
        continue

    operadores_permitidos = "+-*/"
    if operador not in operadores_permitidos:
        print("Você não está digitando corretamente os operadores permitidos!")
        continue
    if len(operador) > 1:
        print("Você não está digitando corretamente os operadores permitidos!")
        continue
    
    print("Realizando sua conta, confira abaixo: ")
    if operador == "+":
        print(num_1_float + num_2_float)
    elif operador == "-":
        print(num_1_float - num_2_float)
    elif operador == "/":
        print(num_1_float / num_2_float)
    elif operador == "*":
        print(num_1_float * num_2_float)
    else:
        print("Não deveria chegar aqui.")

    sair = input("Quer sair? [s/n]").lower().startswith("s")
    
    if sair is True:
        break

