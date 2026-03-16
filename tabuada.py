import os 

os.system("cls || clear")


# Solicitando dados 
número = int(input("Digite um numero para ver sua tabuada: "))

#Gerar tabuada de 1 a 10 
for i in range(1, 11): 
    resultado = numero * i 
    print(f{numero} x {i} = {resultado}") 