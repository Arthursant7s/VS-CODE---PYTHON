import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass 
class Funcionario:
    nome: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")

lista_funcionarios = []

print("- Solicitando dados -")
with open('lista_funcionarios.csv', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        nome = linha.strip().split(', ')
        lista_funcionarios.append(Funcionario(
        nome=nome
        ))
for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()