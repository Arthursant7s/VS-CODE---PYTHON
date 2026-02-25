import os 

os.system("cls || clear")

# maçãs R$ 1,30 cada menos de 1 duzia
# 1 duzia completa R$ 1,00 cada.

print("- Solicitando dados -")
quantidade = int(input("Digite a quantidade de maçães desejadas: "))


if quantidade <= 12: 
    preco = 1.30

else: 
    preco = 1

preco_final = quantidade * preco

print("\n- Exibindo dados -")
print(f"Preço pro maçã : R$ {preco:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")

