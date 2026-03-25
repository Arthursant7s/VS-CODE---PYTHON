import os

os.system("cls || clear")

vetor_num = []
QUANTIDADE_NUMEROS = 2
pares = 0 
impares = 0

print(f"Adicionado {QUANTIDADE_NUMEROS} numeros.")
for i in range( QUANTIDADE_NUMEROS):
    numero = float(input(f"Digte a {i+1}º número: "))
    vetor_num.append(numero)

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

for i, uma_nota in enumerate(vetor_num, start= +1):
    print(f"{i}ª nota: {uma_nota}")

print(f"Pares: {pares}")

print(f"Impares: {impares}")