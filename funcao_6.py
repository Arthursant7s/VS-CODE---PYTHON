import os
os.system("cls")


def positivo_ou_negativo(numero):

    os.system("cls")
    if numero > 0:
        print(f"O numero {numero} é positivo.")
    elif numero < 0: 
        print(f"O numero {numero} é negativo.")
    else: 
        print("Valor não encontrado.")
        
numero = int(input("Digite um numero: "))

positivo_ou_negativo(numero)