import os 
os.system("cls || clear")


login_correto = "teste"
senha_correto = "1234"




for tentativa in range(1, 4):

    while True:
        usuario = input(f"Tentativa {tentativa} Digite seu login: ")
        senha = input("Digite a senha: ")

        if usuario == login_correto and senha == senha_correto:
            print("Acesso permitido! Bem-vindo.")
            break 
        else:
            if tentativa < 3: 
                print("Login ou senha incorretos! ")
            else:
                print("Acesso negado! Fim!\n")



                
# while True:

#     login = input("Digite seu login: ")
#     senha = input("Digite sua senha: ")

#     login_esta_correto = login == login_correto
#     senha_esta_correto = senha == senha_correto
#     contador += 1

#     if contador == 3
#     break

#     if login_esta_correto and senha_esta_correto

            