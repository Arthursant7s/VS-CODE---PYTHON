import os
from dataclasses import dataclass


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

NOME_DO_ARQUIVO = 'catalogo_livros.csv'

def salvar_no_arquivo(livro: livro):
    with open(NOME_DO_ARQUIVO, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{livro.Nome}, {livro.Autor}, {livro.Categoria}, R${livro.Preço:.2f}\n')
        print('livro salvo com sucesso!')

def ler_arquivo():
    # Tratamento de exeção!
    try:
        print('= LISTA DE LIVROS =')
        with open(NOME_DO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome, autor, categoria, preco = linha.strip().split(', ')
                lista_livros.append(livro(Nome=nome, Autor=autor, Categoria=categoria, Preço=float(preco.replace('R$', ''))))
                
        for livro in lista_livros:
            livro.mostrar_dados()
    except FileNotFoundError:
        print(f'Arquivo não encontrado...')
        
lista_livros = []

while True:
    os.system("cls || clear")
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
            print('-Cadadstrar livro-')
            novo_livro = livro(
                Nome=input('Nome do livro: '),
                Autor=input('Autor do livro: '),
                Categoria=input('Categoria do livro: '),
                Preço=float(input('Preço do livro: R$'))
            )
            salvar_no_arquivo(novo_livro)

        case '2':
            os.system("cls || clear")
            ler_arquivo()
            input("Pressione Enter para voltar para o menu!")
            os.system("cls")

        case '3':
            print('-Sair do programa-')
            break
        case _:
            print('Opção inválida. Tente novamente.')
    
    mais = input('Deseja realizar outro cadastro? (s/n): ')
    if mais.lower() != 's':
        print('Saindo do programa...')
        break

