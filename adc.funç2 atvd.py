import os 

os.system("cls || clear")

def calcular_estatisticas(numeros):
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    positivos = [n for n in numeros if n > 0]
    negativos = [n for n in numeros if n < 0]

    return {
        "quantidade_pares": len(pares),
        "quantidade_impares": len(impares),
        "soma_impares": sum(impares),
        "soma_geral": sum(numeros),
        "soma_pares": sum(pares),
        "quantidade_positivos": len(positivos),
        "quantidade_negativos": len(negativos),
        "maior_numero": max(numeros),
        "menor_numero": min(numeros)
    }

lista_numeros = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

estatisticas = calcular_estatisticas(lista_numeros)

print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {estatisticas['quantidade_pares']}")
print(f"Quantidade de ímpares: {estatisticas['quantidade_impares']}")
print(f"Quantidade de positivos: {estatisticas['quantidade_positivos']}")   
print(f"Quantidade de negativos: {estatisticas['quantidade_negativos']}")
print(f"Maior número: {estatisticas['maior_numero']}")
print(f"Menor número: {estatisticas['menor_numero']}")
print(f"Soma dos números: {estatisticas['soma_geral']}")

    
