import os
os.system("cls || clear")

total_familias = 0
soma_salario = 0 
soma_filhos = 0
maior_salario = 0 
menor_salrio = 0


while True:
    print("\n1 Adicionar familia")
    print("2 Sair e exibir resultados")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        salario = float("Digite o salrio da familia: ")
        filhos = int(input("Digite o numero de filhos: "))

        total_familias += 1
        soma_salario += salario
        soma_filhos += filhos

        if salario > maior_salario:
            maior_salario = salario
        if salario < menor_salrio:
            menor_salrio = salario

    elif opcao == 2:
        if total_familias > 0:
            media_salario = soma_salario / total_familias
            media_filhos = soma_filhos / total_familias
            print(f"\n Resultados: ")
            print(f"a) Total familias: {total_familias}")
            print(f"Média filhos: ")
            print(f"Maior Salario")