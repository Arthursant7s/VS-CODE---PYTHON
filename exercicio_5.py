import os 

os.system("cls || clear")

primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite um numero: "))

media = (primeiro_numero + segundo_numero ) / 2

soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero 
media = soma / 2 

menor = min(primeiro_numero,segundo_numero)
maior = max(primeiro_numero, segundo_numero)

if primeiro_numero == segundo_numero:
    print("Eles são iguais!")

if primeiro_numero != segundo_numero:
     print("Eles não são iguais!")

print("\n- Exibindo dados -")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Produto: {produto}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")