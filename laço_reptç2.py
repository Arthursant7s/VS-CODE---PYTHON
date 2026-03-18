import os 

os.system("cls || clear")

soma = 0 
QUANTIDADE_NOTAS = 3

for i in range(2):

    #CONDIÇÃO VERDADEIRA 
    while True:
        nota = float(input(f"Digite a {i+1}° nota: "))

        # if nota >= 0 and nota <= 10:
        #     soma += nota
        #     break
        # else:
        #     print("Nota inválida")
        #     print("Tente novamente...\n")

        #TROCA DE SINAIS 
        if nota < 0 or nota > 10:
            print("Nota inválida.")
            print("Tente novamente...\n")
    
#CALCULO DE MÉDIA 
media = soma / QUANTIDADE_NOTAS

print(f"Média: {media}")