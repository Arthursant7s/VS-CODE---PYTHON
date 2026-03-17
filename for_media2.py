import os 

os.system ("cls || clear") 

soma_notas = 0 

# Solicitar 3 notas 
for i in range(1, 4):
    nota = float(input(f"Digite a {i}° nota: "))
    soma_notas += nota 
  
    # Calculando notas
    media = soma_notas  / 3 
    print(f"\nMédia final é: {media: .2f}")

if media >= 7:
    print("Você foi aprovado!") 

else: 
    print("Você foi reprovado.")
    
