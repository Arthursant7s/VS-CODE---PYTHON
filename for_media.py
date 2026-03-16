import os 

os.system("cls || clear") 

soma_notas = 0 

# Solicitando 4 notas 
for i in range(1, 5);
    nota = float(input(f"Digite a {i}° nota: "))
    soma_notas += nota 

    # Calculando a média 
    media = soma_notas / 4 
    print(f"\nA média final é: {media: .2f}")