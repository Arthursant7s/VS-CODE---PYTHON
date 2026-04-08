import os
os.system("cls")

# Função sem parâmetros e sem retorno
def logo():
    print("=======")
    print("  SENAI  ")
    print("=======")

# Função com parâmetros e com retorno 
def somar(lista_numeros):
    soma = lista_numeros[0] + lista_numeros[1]
    return soma

# Função com parâmetro e com retorno
def subtrair(lista_numeros):
    subtração = lista_numeros[0] - lista_numeros[1]
    return subtração

def multiplicar(lista_numeros):
    multiplicar = lista_numeros[0] * lista_numeros[1]
    return multiplicar

def divição(lista_numeros):
    divisão = lista_numeros[0] / lista_numeros[1]
    return divisão

lista_numeros = []
QUANTIDADE_NUMEROS = 2


print("= Solicitando dados =")

logo()
print("= Solicitando dados =")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista_numeros.append(numero)
    
soma = somar(lista_numeros)
subtração = subtrair(lista_numeros)


print("= Exibindo dados =")
print(f"Subtração: {subtração}")
print(f"Soma: {soma}")
print(f"Multiplicação: {lista_numeros}")
print(f"Divisão: {lista_numeros}")