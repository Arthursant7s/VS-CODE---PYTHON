import os
os.system("cls")


# Função sem parâmetros e sem retorno
def logo():
    print("=======")
    print("  SENAI  ")
    print("=======")


# Função com parâmetros e com retorno 
def subtração(n1, n2):
    return n1 - n2

# Função com parâmetro e com retorno
def soma(n1, n2):
    return n1 + n2

def multiplicar(n1, n2):
    return n1 * n2

def divisão(n1, n2):
    return n1 / n2

print("= Solicitando dados =")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

subtração = subtração(n1, n2)
soma = soma(n1, n2)
multiplicar = multiplicar(n1, n2)
divisão = divisão(n1, n2)


logo()
print("= Exibindo dados =")
print(f"Subtração: {subtração}")
print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicar}")
print(f"Divisão: {divisão}")