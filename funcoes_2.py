import os 
os.system("cls || clear")

# Função com parâmetros
def saudacao(nome):
   print(f"Olá, {nome}!")
   print("Bem-vindo(a) ao nosso site!")

# Exemplo de uso da função
nome_visitante = input("Digite seu nome: ")
saudacao(nome=nome_visitante)