import os

os.system("cls || clear")

número = int(input("Digite um numero para ver sua tabuada: "))

for i in range(1, 11): 
    resultado = número * i 
    print(f"{número} x {i} = {resultado}") 
    
    
