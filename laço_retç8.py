import os 
os.system("cls || clear")

soma_notas = 0 
contador = 0 

print("Digite valores inteiros positivos {ou num negativo para sair}")

while True:
    valor = float(input("Digite a {contador + 1}°nota valor: "))

    if valor < 0:
        break

    soma += valor
    contador += 1 

if contador > 0:
    media = soma / contador