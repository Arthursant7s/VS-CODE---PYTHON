import os
#Limpa o terminal

os.system("cls")

print("Digite as notas")

primeira_nota = float(input("Digite a primeria nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota) / 2
# COMDICIONAL

if media >= 7:
    resultado = "Aprovado"
else: 
    resultado = "Reprovado"
# Mostre o nome e a media 
    print("\n- Exibindo dados -")
    print(f"Média: {media} do aluno")
    print(f"Resultado: {resultado}.")

print("FIM")




