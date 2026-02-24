import os 

# Limpa o Terminal. 
os.system("cls")

print("- Solicitando dados -")
nome = input("Digite seu nome: ")

primeira_nota = float(("Digite a primera nota: "))
segunda_nota = float(("Digite sua segunda nota: "))

#Calcule 

#Mostre o nome e a media 

media = (primeira_nota + segunda_nota) / 2
print("\n- Exibindo dados -")
print("Nome: ", nome)
print(f"Média: {media} do aluno.")