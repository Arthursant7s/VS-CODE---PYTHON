import os
os.system("cls || clear")

salarios = []
filhos = []

while True:
    print("\n1 - Adicionar familia | 2 - Sair e exibir resultados")
    opcao = input("Digite uma opção: ")

    if opcao == 1:
        salarios.append(int(float("Digite o salario: ")))
        filhos.append(int(input("Digite a quantidade de filhos: ")))
    elif opcao == 2: 
        break
    else: 
        print("Opção inválida!")

if salarios: 
    total_familias = len(salarios)
    media_salario = sum(salarios) / total_familias
    media_filhos = sum(salarios) / total_familias
    maior_salrio = max(salarios)
    menor_salrio = min(salarios)


    print(f"\na) Total de familias: {total_familias}")
    print(f"b) Média salarial: R$ {media_salario: .2f}")
    print(f"c) Média de filhos: {media_filhos: .1f} ")
    print(f"d) Maior salário: R$ {maior_salrio: .2f}")
    print(f"d) Menor salário: R$ {menor_salrio: .2f}")

else: 
    print("Nenhum dado foi encontrado. ")