import os

os.system("cls || clear")

soma_notas = 0 
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite uma nota: "))
    soma_notas += nota
    
media = soma_notas / QUANTIDADE_NOTAS

print(f"\nMédia: {media}")

# # Solicitando 4 notas 
# for i in range(1, 5):
#     nota = float(input(f"Digite a {i}° nota: "))
#     soma_notas += nota 

#     # Calculando a média 
#     media = soma_notas / 4 
#     print(f"\nA média final é: {media: .2f}")

