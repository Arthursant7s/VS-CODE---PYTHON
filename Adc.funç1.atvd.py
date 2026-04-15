import os
os.system("cls || clear")    

import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Definindo listas vazias para armazenar os dados dos usuários

def cadastro():
    nome = input("Digite o nome do usuário: ")
    sobrenome = input("Digite o seu sobrenome: ")
    nome = nome + " " + sobrenome
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
  

    return nome, idade, altura, peso
def exibir_dados(nomes, idades, alturas, pesos):
    logoSenai()
    print("\nDados dos usuários:")
    for i in range(len(nomes)):
        print(f"Usuário {i+1}:")
        print("Nome:", nomes[i])
        print("Idade:", idades[i])
        print("Altura:", alturas[i], "metros")
        print("Peso:", pesos[i], "quilogramas")
        print()

        break



# Solicitando os dados dos usuários em um loop
# while True:
#     logoSenai()
#     nome = input("Digite o nome do usuário: ")
#     sobrenome = input("Digite o seu sobrenome: ")
#     nome = nome + " " + sobrenome
    
#     # Verificando se o usuário quer sair
#     if nome.lower() == 'sair':
#         break
    
#     idade = int(input("Digite a idade do usuário: "))
#     altura = float(input("Digite a altura do usuário (em metros): "))
#     peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # # Adicionando os dados às listas
    # nomes.append(nome)
    # idades.append(idade)
    # alturas.append(altura)
    # pesos.append(peso)

# Exibindo os dados armazenados
# logoSenai()
# print("\nDados dos usuários:")
# for i in range(len(nomes)):
#     print(f"Usuário {i+1}:")
#     print("Nome:", nomes[i])
#     print("Idade:", idades[i])
#     print("Altura:", alturas[i], "metros")
#     print("Peso:", pesos[i], "quilogramas")
#     print()