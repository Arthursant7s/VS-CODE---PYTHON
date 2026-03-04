import os

os.system("cls")

# MENU
print ("MENU")
print ("""
    ======= MENU ======= 
    Codigo    Prato         valor 
       1    Picanha         25,00
       1    Lasanha         20,00
       3    Strogonoff      18,00
       4    Bife Acebolado  15,00
       5    Pão com ovo     5,00
       """)

cardapio = input("Digite a opção de sua preferência: ")

match cardapio: 
    case "1":
        print("Picanha")
        print("25,00")
    case "2":
        print("Lasanha")
        print("20,00")
    case "3":
        print("Strogonoff")
        print("18,00")
    case "4":
        print("Bife Acebolado")
        print("15,00")
    case "5":
        print("Pão com ovo")
        print("5,00")
    case _:
        print("Pedido inválido")




    
    
    
    