import os 

os.system ("cls")
#ENTRADA DE DADOS

matricula =  input("Digite a sua matricula: ")

ano_nascimento = int(input("Digite seu ano de nascimento: "))

tempo_de_trabalho = int(input("Digite o tempo de trabalho: "))

#PROCESSAMENTO 

idade = 2026 - ano_nascimento 

if idade >= 65 or  tempo_de_trabalho >= 30:
    resultado = "Requer aposentadoria"
else:
    resultado = "Não requerer aposentadoria"

#SAIDA DE DADOS

print("\n- Resultado -")
print(f"Idade: {idade}")
print(f"Tempo de trabalho: {tempo_de_trabalho}")
print(f"Resultado:{resultado}")


