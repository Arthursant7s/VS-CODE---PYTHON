import os
from dataclasses import dataclass

@dataclass
class Comida:
    Nome: str
    Cozinheiro: str
    Categoria: str
    Preço: float

    def mostrar_dados(self):
        print(f'Nome: {self.Nome}')
        print(f'Cozinheiro: {self.Cozinheiro}')
        print(f'Categoria: {self.Categoria}')
        print(f'Preço: R${self.Preço:.2f}\n')

NOME_DO_ARQUIVO = 'catalogo_comidas.csv'

def salvar_no_arquivo(comida: Comida):
    with open(NOME_DO_ARQUIVO, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{comida.Nome}, {comida.Cozinheiro}, {comida.Categoria}, {comida.Preço}\n')
    print('Comida salva com sucesso!')

def ler_arquivo():
    try:
        print('=========== LISTA DE COMIDAS ===========')
        lista_auxiliar = [] # Lista local para evitar duplicados globais
        with open(NOME_DO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome, cozinheiro, categoria, preco = linha.strip().split(', ')
                nova = Comida(Nome=nome, Cozinheiro=cozinheiro, Categoria=categoria, Preço=float(preco))
                lista_auxiliar.append(nova)
        
        for item in lista_auxiliar:
            item.mostrar_dados()
    except FileNotFoundError:
        print('Arquivo ainda não existe. Cadastre algo primeiro!')
    except Exception as e:
        print(f'Erro ao ler arquivo: {e}')

# --- Menu Principal ---
while True:
    os.system("cls || clear")
    print("""
    ============ Sistema de Cadastro ============
    Código       Opção
    1            Adicionar comida
    2            Listar comidas
    3            Sair
    =============================================
    """)
    
    opcao = input('Digite a opção desejada: ')
    
    match opcao:
        case '1':
            print('\n--- Cadastrar Comida ---')
            try:
                nova_comida = Comida(
                    Nome=input('Nome da comida: '),
                    Cozinheiro=input('Nome do Cozinheiro: '),
                    Categoria=input('Categoria: '),
                    Preço=float(input('Preço: R$'))
                )
                salvar_no_arquivo(nova_comida)
            except ValueError:
                print("Erro: Digite um valor numérico válido para o preço!")

        case '2':
            os.system("cls || clear")
            ler_arquivo()
            input("\nPressione Enter para voltar ao menu...")

        case '3':
            print('Saindo do programa...')
            break
            
        case _:
            print('Opção inválida!')

    if input('\nDeseja realizar outra operação? (s/n): ').lower() != 's':
        print('Encerrando...')
        break