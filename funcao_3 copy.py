import os
os.system("cls || clear")

# Função com parãmetros
def somar(n1, n2):
    soma = n1 + n2
    return soma


# Exemplo de uso da função
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))


# Chamando a função
# Enviando parâmetros
resultado = somar(n1, n2)

print(f"Soma: {resultado}")
