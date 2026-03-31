vetor = []
negativos = 0
soma_positivos = 0

for i in range(5):
    num = float(input(f"Digite o {i+1}º numero: "))
    vetor.append(num)

    if num < 0:
        negativos += 1
    elif num > 0:
        soma_positivos += num

print(f"Vetor: {vetor}")
print(f"Quantidade de numeros negativos: {negativos}")
print(f"Soma dos positivos: {soma_positivos}")