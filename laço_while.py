import os 

os.system("cls || clear")

while True:
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        print("Acesso negado!")
        print("Tente novamente... \n")
    else:
        print("Acesso permitido.")
        break
        
print("Fim do programa")        