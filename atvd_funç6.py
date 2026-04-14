import os
os.system("cls || clear") 

def ler_nota(ordem):
    print("= Solicitando dados =")
    while True:
        try:
            nota = float(input(f"Digite a nota do aluno {ordem} (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def calcular_media(n1,n2):
    "A média é: {media:.2f}"
    media = (n1 + n2) / 2
    return media

def verificar_aprovacao(media):
    if media >= 7:
        return "Aluno aprovado!"
    else:
        return "Aluno reprovado!"

n1 = ler_nota(1)
n2 = ler_nota(2)

media = calcular_media(n1, n2)
print("-" * 20)
print(f"A média é: {media:.2f}")