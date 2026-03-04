import os

os.system("cls")

#ENTRADA DE DADOS

login_cadastrado = "Arthur"
senha_cadastrada = "12345"

print("-Solicitando dados-")
login = input("Seu nome de usuario é: ")
senha = int(input("Sua senha é: "))

login_correto = login == login_cadastrado
senha_correta = senha == senha_cadastrada


if  login_correto and senha == senha_correta:
    print("Bem-vindo!")
else:
    print("Login or senha inválidos.")













