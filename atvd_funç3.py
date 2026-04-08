import os 
from datetime import date
os.system("cls || clear")


def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    return ano_atual - ano_nascimento

ano = int(input("Digite o seu ano de nascimaento: "))

idade_usuario = calcular_idade(ano)

print(f"Você tem {idade_usuario} anos")



