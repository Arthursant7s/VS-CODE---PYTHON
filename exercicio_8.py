import os 

os.system("cls || clear")


primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite um numero: "))
terceiro_numero = int(input("Digite um numero: "))

menor = min(primeiro_numero,segundo_numero, terceiro_numero)
maior = max(primeiro_numero, segundo_numero, terceiro_numero)


print("\n- Exibindo dados -")
print(f"Maior: {maior}")
print(f"Menor: {menor}")