"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Wagner'
preco = 1000.95897643
variavel = "%s, o preço total R$%.2f" % (nome, preco)
print(variavel)
print("O hexadecimal de %d é %08x" % (1500,1500))
