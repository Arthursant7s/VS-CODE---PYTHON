import os

os.system("cls|| clear")

numeros = []

for i in range(5):
    num = float(input(f"Digite o {i+1}º numero: "))
    numeros.append(num)

    print("\nNúmeros informados:", numeros)

    print(f"O maior numero é: {max(numeros)}")
    print(f"O menor numero é: {min(numeros)}")