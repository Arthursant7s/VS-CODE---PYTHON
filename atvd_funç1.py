import os 

os.system("cls")

def converter_para_centimetros(metros):
    return metros * 100

valor_metros = float(input("Digite o valor em metros: "))
resultado = converter_para_centimetros(valor_metros)

print(f"{valor_metros} metros equivalem a {resultado} em centímetros")