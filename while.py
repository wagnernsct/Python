# r = "Y"
# while r == "Y":
#     n = int(input("Digite um valor: "))
#     r = str(input("Do you want to continue? [Y/N] ")).upper()
# print("Fim")

# c = 1 
# while c < 10:
#     print(c)
#     c+= 1
# print("Fim")

# n = 1
# par = impar = 0
# while n !=0:
#     if n != 0:
#         n = int(input("Enter a value: "))
#         if n % 2 == 0:
#             par +=1
#         else:
#             impar +=1

# print(f"You typed {par} numbers pair and {impar} numbers odds!")
# print("End")

"""
sexo = str(input("Informe seu sexo: ")).upper()
# sexo_m = "m".upper() # Não precisava
# sexo_f = "f".upper() # Não precisava

while sexo != "M" and  sexo != "F": 
        print("Entrada inválida, Digite novamente.")
        sexo = str(input("Digite o seu sexo [M/F]: ")).upper()

print("Sexo:", sexo)
"""
# Escreva um programa que leia vários num int pelo teclado. O programa só vai parar quando o usuário digitar "999".
n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print(f"A soma é de: {s} ")




    

         



# str(input("Informe seu sexo: "))