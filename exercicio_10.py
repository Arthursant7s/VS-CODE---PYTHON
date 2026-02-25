import os 

os.system("cls || clear")

print("- Solicitando dados -")

peso = float(input("Digite seu peso corporal (Em kg): "))
altura = float(input("Digite sua altura (Em cm): "))

imc = peso / (altura * altura)

print(f"IMC é: {imc:.2f}")

if peso < 18.5: 
   print("Abaixo do peso")

elif imc == 18.6 and 24.9:
   print("peso ideal(parabéns)")

elif imc == 25.0 and 29.9: 
   print("Levemente a cima do peso")

elif imc == 30.0 and 34.9:
   print("Obesidade grau 1")

elif imc == 35.0 and 39.9: 
   print("Obesidade grau 2 (severa)")

elif imc >= 40: 
   print("Obesidade grau 3 (mórbida)")

