import os
os.system("cls || clear")


cardapio = {
    
    "1": ("Picanha", 25,00),
    "2": ("Lasanha", 20,00),
    "3": ("Picanha", 25,00),
    "4": ("Picanha", 25,00),
    "5": ("Lasanha", 20,00),
    
}

pedidos = []
total = 0 

while True:
    print("\n---MENU DO RESTAURANTE---")
    for codigo, item in cardapio.itens():
        print(f"{codigo} - {item['nome']}: R$ {item['preco']: .2f}")

    escolha = int(input("\nDigite o numero do prato desejado: "))

    if escolha in cardapio:
        prato = cardapio[escolha]
        pedidos.append(prato)
        total += prato['preco']
        print(f"{prato['nome']} Adicionado ao pedido!")

    else:
        print("Opção inválida!")

    continuar = input("Deseja escoçher outro prato? (s/n): ").lower()
    if continuar != 's':
        break

    for item in pedidos:
        print(f"- {item['nome']}: R$ {item['preco']: .2f}")

    print("-" * 25)
    print(f"VALOR TOTAL DA CONTA: R$ {total: .2f}")