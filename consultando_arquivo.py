import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass 
class Empresa:
    nome: str
    cnpj: str
    telefone: str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'CPNJ: {self.cnpj}')
        print(f'Telefone: {self.telefone}\n')

QUANTIDADE_FUNCIONARIOS = 1
lista_empresas = []

print('= Solicitnado dados =')
for i in range(QUANTIDADE_FUNCIONARIOS):
    nova_empresa = Empresa(
        nome=input('Digite o nome da sua empresa: '),
        cnpj=input('Digite o CNPJ: '),
        telefone=input('Digite o telefone: ')
    )
    print('')
    lista_empresas.append(nova_empresa)

print('= Salvando dados =')
with open('contato_empresas.csv', 'a', encoding='utf-8') as arquivo:
    for empresa in lista_empresas:
        arquivo.write(f'{empresa.nome}, {empresa.cnpj}, {empresa.telefone}\n')
    print('Salvo com sucesso!')

print('= Fim do programa. =')

print("======= Consultando dados salvos =======")
lista_contatos = []
with open('contato_empresas.csv', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        nome, cnpj, telefone = linha.strip().split(', ')
        empresa = Empresa(nome=nome, cnpj=cnpj, telefone=telefone)
        lista_contatos.append(empresa)

for empresa in lista_contatos:
    empresa.mostrar_dados()

print('= Fim do programa. =')
