import os
os.system("cls || clear")

vetor = []

print("Digite 5 numeros: ")

for i in range(5):
    while True:
        numero = float(input(f"Digite o {i+1}º número: "))
        break
    print("Entrada inválida! Digite um número: ")

    if numero < 0:
        vetor.append(0.0)
    else:
        vetor.append(numero)

print("\nValores armazenados no vetor: ")
print(vetor)