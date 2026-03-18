import os 

os.system("cls || clear")

nota1 = ()
nota2 = ()

while True:

    nota = float(input("Digite a primeira nota: "))
    if 0 <= nota1 <= 10:
        break 

    else:
        print("Nota inválida! A nota deve ser entre (0 e 10)")

while True:
    nota = float(input("Digite a segunda nota: "))
    if 0 <= nota2 <= 10:
        break 

    else:
        print("Nota inválida! A nota deve ser entre (0 e 10) ")

media = (nota1 + nota2) / 2

print(f"A media aritimetica é: {media: .2f}")