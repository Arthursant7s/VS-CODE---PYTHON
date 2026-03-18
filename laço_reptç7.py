import os 

preço_total = 0
pratos_solicitados = ""

while True:
    os.system("cls || clear")

    print ("""
        ======= MENU ======= 
        Codigo    Prato         valor 
        1    Picanha         25,00
        1    Lasanha         20,00
        3    Strogonoff      18,00
        4    Bife Acebolado  15,00
        5    Pão com ovo     5,00
        """)

    opcao = input("Digite a opção de sua preferência: ")

    match opcao: 
            case "1":
                prato ="Picanha"
                preco = 25
            case "2":
                prato = "Lasanha"
                preco = 20
            case "3":
                prato = "Strogonoff"
                preco = 18
            case "4":
                prato = "Bife Acebolado"
                preco = 15
            case "5":
                prato = "Pão com ovo"
                preco = 5
            case _:
                prato = "" \
                "preco = 0"
                print("Pedido inválido")
                print("Tente novamente... \n")
            

    preco_total += preco
    pratos_solicitados += ", " + prato if pratos_solicitados else prato 

    mais_pedidos = input("Deseja fazer um novo pedido?\nUse S ou N: ").lower()

    if mais_pedidos == "n":
        break

    print("\n == Nota fiscal ==")
    print(f"Pratos solicitados: {pratos_solicitados}")
    print(f"Total da compra: {preço_total}")