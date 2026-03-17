import os 
 
os.system ("cls || clear") 


soma = 0 
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite uma nota: "))
    soma += nota


media = soma / QUANTIDADE_NOTAS

if media >= 7:
    resultado = "Aprovado"
elif media <= 4:
    resultado = "Reprovado"
else:
    resultado = "Recuperação"

print(f"\nMédia: {media: .2f}")         
print(f"Resultado: {resultado}")


# soma_notas = 0 

# # Solicitar 3 notas 
# for i in range(1, 4):
#     nota = float(input(f"Digite a {i}° nota: "))
#     soma_notas += nota 
  
#     # Calculando notas
#     media = soma_notas  / 3 
#     print(f"\nMédia final é: {media: .2f}")

# if media >= 7:
#     print("Você foi aprovado!") 

# else: 
#     print("Você foi reprovado.")

