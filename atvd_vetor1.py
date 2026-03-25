import os 
os.system("cls || clear")

vetor_notas = []
QUANTIDADE_NOTAS = 4


for i in range( QUANTIDADE_NOTAS):
    nota = float(input(f"Digte a {i+1}ª nota: "))
    vetor_notas.append(nota)

media = sum(vetor_notas) / QUANTIDADE_NOTAS
print("\nExibindo as notas informadas.")

for i in range(QUANTIDADE_NOTAS):
   
    print(f"Média: {media}")
    
for uma_nota in vetor_notas:
    print(f"{i}ª nota: {uma_nota}")

if media >= 7: 
    resultado ="provado!"
elif media <= 5:
    resultado = "Recuperação."
else:
    print("Reprovado")

print(f"\nMédia: {media}")
print(f"\nResultado: {resultado}")
