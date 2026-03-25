import os 
os.system("cls || clear")

vetor_num = []
QUANTIDADE_NUMEROS = 5

for i in range( QUANTIDADE_NUMEROS):
    nota = float(input(f"Digte o {i+1}º número: "))
    vetor_num.append(nota)

if len(vetor_num) > 0:
    maoir_numero = max(vetor_num)
    menor_numero = min(vetor_num)

    print(f"O maior numero é: {maoir_numero}")
    print(f"O menor numero é: {menor_numero}")