import os 
os.system("cls")

# Função com parãmetros
def tabuada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} x {numero * i}")


# Exemplo de uso da função
numero = int(input("Digite um numero da tabuada: "))



# Chamando a função
# Enviando parâmetros

tabuada(numero)