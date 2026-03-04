import os

os.system

#ENTRADA DE DADOS

print("Solicitando dados")
num_faltas = int(input("Digite suas faltas:"))
media = float(input("Digite sua media: "))


if media >= 7 or num_faltas <= 40:
    print("Aluno aprovado!")

else: 
    print("Você está reprovado com execesso de faltas!")






