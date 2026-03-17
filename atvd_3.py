import os 

os.system("cls || clear")


#Inicializar a variável da soma com 0 
soma = 0 

print("Digite 5 numeros inteiros: ")

# Laço para repetir 5 vezes 
for i in range(1, 6):
    numero = int(input(f"Digite o {i}° numero: "))
    soma += numero 
                                      
# Apresentar a soma final 
print("-") 
print(f"A soma dos 5 numeros é: {soma}")




# soma = 0 

# for i in range(1, 6):
#     numero = int(input("Digite um numero: "))
#     soma = soma + numero 
    
# print(f"Soma: {soma}")

