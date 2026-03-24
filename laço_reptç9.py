import os 
os.system("cls || clear")

soma = 0 
quantidade = 0
valor = 0

print("Digite valores inteiros positivos: ")

while valor >= 0:
    valor = int(input("Digite um valor: "))

    if valor < 0: 
        break

    soma += valor
    quantidade = +1

    if quantidade > 0:
        media = soma / quantidade 
    print("A media aritimetica dos numeros é: {media: .2f}")
    
else: 
    print("um valor negativo foi encontrado!")