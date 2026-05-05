import os 
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    cnpj : int
    telefone : int

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")


QUANTIDADE_EMPRESAS = 1
lista_empresas = []

print("- Solicitando dados -")
for i in range(1):
    novo_funcionario = Funcionario(
        nome=input(f'Digite o nome do funcionario: '),
    
    )
    print('')
    lista_empresas.append(novo_funcionario)


print("\n- Salvando dados -")
with open('lista_funcionarios.csv', 'a', encoding='utf-8') as arquivo:
    for funcionario in lista_empresas:
        arquivo.write(f"{funcionario.nome}\n")
    print('Salvo com Sucesso!')