import os
from dataclasses import dataclass

os.system("cls")

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