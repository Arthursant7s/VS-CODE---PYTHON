import os

os.system

nota = int(input("Digite sua nota: "))


if nota >= 0 and nota <= 10 : 

 print(f"Nota: {nota} do aluno ")

else:
    print("A nota deve estar entre 0 e 10")