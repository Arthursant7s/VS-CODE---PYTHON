import os

os.system

dia = input("Digite o dia da semana: ")

match dia: 
    case "segunda":
        print("Hoje é segumda_feira")
    case "terça":
        print("Hoje é terça_feira")
    case "quarta":
        print("Hoje é quarta_feira")
    case "quinta":
        print("Hoje é quinta_feira")
    case "sexta":
        print("Hoje é sexta_feira")
    case "sabado | domingo":
        print("Hoje é fim de semana")
    case _: 
        print("dia inválido")

print(dia)


print("=== FIM ===")