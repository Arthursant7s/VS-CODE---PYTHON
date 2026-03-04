import os

os.system

primeiro_numero = int(input("Digite um numero: "))
operador = input("Digite a operação desejada (+ - * /): ")
segundo_numero = int(input("Digite um numero: "))

match operador:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
      print("Opção inválida")
      resultado = 0 
    
print(f"Resultado: {resultado}")


