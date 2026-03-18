import os 
os.system("cls || clear")

soma = 0 
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i}º nota: "))

        if nota >= 0 and nota <= 10:
            soma += nota
            break
        else:
            print("Nota inválida!: ")

media = soma / QUANTIDADE_NOTAS


if media >= 7:
    resultado = "Aluno aprovado!"

elif  5 <= media < 7: 
    resultado = "Você está de recuperação."

else: 
    resultado = "Aluno reprovado!"

print(f"Média: {media}")
print(f"Resultado: {resultado}")