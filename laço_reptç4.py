import os 
os.system("cls || clear")

login_correto = "teste"
senha_correta = "1234"

while True:
    login = input("Digite seu login: ")
    senha = input("Digite a senha: ")

    login_esta_correto = login == login_correto
    senha_esta_correto = senha == senha_correta

    if login == login_correto and senha == senha_correta:
        print("Acesso permitido! Bem-vindo.")
        break 
    else:
        print("Login ou senha incorretos. tente novamente!\n")
