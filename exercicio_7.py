import os 

os.system("cls || clear")

print("- Solicitando dados -")
primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite um numero: "))


menor = min(primeiro_numero,segundo_numero)
maior = max(primeiro_numero, segundo_numero)


print("\n- Exibindo dados -")
print(f"Maior: {maior}")
print(f"Menor: {menor}")