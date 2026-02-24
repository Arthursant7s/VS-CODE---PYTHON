import os
#Limpa o terminal

os.system("cls")

primeiro_numero = int(input("Digite o primerio numero: "))
segundo_numero = int(input("Digite o segundo numero: "))

media = (primeiro_numero + segundo_numero) / 2

print("A media é:", media)

soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
media = soma / 2

# if primeiro_numero > segundo_numero:
#     maior = primeiro_numero
#     menor = segundo_numero
# else:
#     maior = primeiro_numero
#     menor = segundo_numero 

menor = min(primeiro_numero, segundo_numero)
maior = max(primeiro_numero, segundo_numero)


print("\n- Exibindo dados -")
print(f"Soma: {soma}")
print(f"Media: {media}")
print(f"Produto: {produto}")
print(f"Maior número: {maior}")
print(f"Menor numero: {menor}")


 



