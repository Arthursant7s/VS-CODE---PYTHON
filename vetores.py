import os 
os.system("cls || clear")

# Criando um vetor
vetor_notas = []
QUANTIDADE_NOTAS = 2

print(f"Adicionando {QUANTIDADE_NOTAS} notas.")
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a {i+1}ª nota:"))
    # Adicionar nota no vetor.
    vetor_notas.append(nota)

# sum (vetor) = soma todos os valores no vetor
media = sum(vetor_notas) / QUANTIDADE_NOTAS

print("\nExibindo as notas informadas.")
# forEach = percorre o vetor informando a quantidade.
# enumerate = atraves da variavel i, numera a quantidade de repeticoes.
for i, uma_nota in enumerate(vetor_notas, start= +1):
    print(f"{i}ª nota: {uma_nota}")
    
print(f"Média: {media}")