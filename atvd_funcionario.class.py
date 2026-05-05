import os 
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Empresa:
    nome: str
    cnpj : int
    telefone : int

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Telefone: {self.telefone}\n")

QUANTIDADE_EMPRESAS = 1
lista_empresas = []

print("- Solicitando dados -")
for i in range(1):
    nova_empresa = Empresa(
        nome=input(f'Digite o nome da empresa: '),
        cnpj=int(input(f'Digite o CNPJ da empresa: ')),
        telefone=int(input(f'Digite o telefone da empresa: '))
    )
    print('')
    lista_empresas.append(nova_empresa)


print("\n- Salvando dados -")
with open('lista_empresas.csv', 'a', encoding='utf-8') as arquivo:
    for empresa in lista_empresas:
        arquivo.write(f"{empresa.nome}, {empresa.cnpj}, {empresa.telefone}\n")
    print('Salvo com Sucesso!')