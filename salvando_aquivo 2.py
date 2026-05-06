import os
from dataclasses import dataclass

os.system("cls || clear")

while True:

    print("""
    ============ Sistema de Cadastro ============
    Codigo       Livros
    1            Adiocionar livro
    2            Listar livros
    3            Sair

""")

    opcao = input('Digite a opção desejada: ')
    match opcao:
        case '1':
            livos="Adiocionar livro"
        case '2':
            livros="Listar livros"
        case '3':
            print('Sair')
            break
        case _:
            print('Opção inválida. Tente novamente.')
    
mais = input('Deseja realizar outro cadastro? (s/n): ')
if mais.lower() != 's':
    print('Saindo do programa...')

@dataclass
class livro:
        Nome: str
        Autor: str
        Categoria: str
        Preço: float
def mostrar_dados(self):
        print(f'Nome: {self.Nome}')
        print(f'Autor: {self.Autor}')
        print(f'Categoria: {self.Categoria}')
        print(f'Preço: R${self.Preço:.2f}\n')

QUANTIDADE_LIVROS = 3
lista_livros = []

print('=========== Solicitando dados ============')
for i in range(QUANTIDADE_LIVROS):
    novo_livro = livro(
        Nome=input('Digite o nome do livro: '),
        Autor=input('Digite o nome do autor: '),
        Categoria=input('Digite a categoria do livro: '),
        Preço=float(input('Digite o preço do livro: R$'))
    )
    print('')
    lista_livros.append(novo_livro)

print('=========== Salvando dados ============')
with open('catalogo_livros.csv', 'a', encoding='utf-8') as arquivo:
    for livro in lista_livros:
        arquivo.write(f'{livro.Nome}, {livro.Autor}, {livro.Categoria}, R${livro.Preço:.2f}\n')
    print('Salvo com sucesso!')

print('= Fim do programa. =')


