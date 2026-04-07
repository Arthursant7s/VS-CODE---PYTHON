
import os
os.system("cls")

def calcular_media(n1, n2):
    media = (n1 + n2)  / 2
    return media 

def verificar_resultados(media):
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"
    
print("------ Sistema de Notas -------")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite o segundo nota: "))

resultado_media = calcular_media(nota1, nota2)
status_final = verificar_resultados(resultado_media)

print(f"\nMédia final: {resultado_media}")
print(f"Situação do aluno: {status_final}")