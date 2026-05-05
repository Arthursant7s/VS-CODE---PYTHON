import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    idade: int

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}\n")


QUANTIDADE_FUNCIONARIOS = 2
lista_funcionarios = []

for i in range(QUANTIDADE_FUNCIONARIOS):
    novo_funcionario = Funcionario(
        nome=input(f'Digite seu nome: '),
        idade=int(input(f'Digite sua idade: '))
    )
    print('')
    lista_funcionarios.append(novo_funcionario)

print('= Exibindo dados = ')
for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()

print("\n- Salvando dados -")
with open('lista_funcionarios.csv', 'a', encoding='utf-8') as arquivo:
    for funcionario in lista_funcionarios:
        arquivo.write(f"{funcionario.nome}, {funcionario.idade}\n")
    print('Salvo com Sucesso!')

print('= Fim do programa. = ')