import os
os.system("cls")

vetor = []
nota1 = ()
nota2 = ()
nota3 = ()

while True:
    nota1 = float(input("Digite a primeira nota: "))
    if 0 <= nota1 <= 10:
        break
    else: 
        print("Nota inválida! A nota deve ser entre (0 e 10)")

while True:
    nota2