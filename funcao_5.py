import os
os.system("cls")


def par_ou_impar(numero):

    os.system("cls")
    if numero % 2 == 0:
        print(f"O numero {numero} é par.")
    else:
        
        print(f"O numero {numero} é impar.")

numero = int(input("Digite um numero: "))

par_ou_impar(numero)