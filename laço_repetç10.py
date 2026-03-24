import os 
os.system("cls || clear")

pares = 0
impares = 0
soma_geral = 0 
soma_pares = 0 
contador_geral = 0


while True:
    numero = int(input("Digite um número: "))
    if numero > 0:
        contador_geral += 1
        soma_geral = numero
        if numero % 2 == 0:
            pares += 1
            soma_pares += numero
        else:
            impares += 1
    if numero == 0:
        break

media_pares = soma_pares / pares
media_geral = soma_geral / contador_geral


print(f"\n Quantidade de pares: {pares}")
print(f"\n Quantidade de impares: {impares}")
print(f"\n Quantidade de numeros pares: {media_pares}")
print(f"\n Média geral: {media_geral}")

























# qtd_pares = 0 
# qtd_impares = 0 
# soma_pares = 0
# soma_total = 0 
# qtd_total = 0 

# print("Digite numeros inteiros positivos:")

# while True:
#         num = int(input("Numero: "))

#         if num == 0:
#             break
    
#         if num < 0:
#             print("Digite um numero positivo.")

#         qtd_total += 1
#         soma_pares += num

# else:
#     qtd_impares += 1


# if qtd_total > 0:
#     media_pares = soma_pares / qtd_pares
#     print(f"Média dos valores pares: {media_pares: .2f}")
# else: 
#     print("Média dos valores pares: N/A")

# if qtd_total > 0:
#     media_geral = soma_total / qtd_total
#     print(f"Média geral: {media_geral: .2f}")

# else:
#     print("Nenhum número foi digitado.")