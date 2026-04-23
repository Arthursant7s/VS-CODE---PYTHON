import os 

os.system("cls || clear")

def matricula():
    return input("Digite a matrícula do funcionário: ")

def senha():
    return input("Digite a senha de funcionário: ")

def main():
    print("----Bem-vindo ao sistema de cadastro!----")
    matricula_funcionario = matricula()
    senha_funcionario = senha()

    # Aqui você pode adicionar a lógica para verificar a matrícula e senha
    # Por exemplo, você pode comparar com valores pré-definidos ou consultar um banco de dados

    print(f"Matrícula: {matricula_funcionario}")
    print(f"Senha: {senha_funcionario}")

if __name__ == "__main__": main()


def calcular_folha():
    # Entradas de dados
    inss = float(input("INSS (R$): "))
    salario_base = float(input("Salário Base (R$): "))
    opta_vt = input("Opção Vale Transporte? (s/n): ").lower() == 's'
    valor_vr = float(input("Valor do Vale Refeição pago pela empresa (R$): "))
    dependentes = int(input("Quantidade de dependentes: "))

    # Cálculos
    desc_vt = (salario_base * 0.06) if opta_vt else 0.0
    desc_vr = valor_vr * 0.20  # 20% do VR
    desc_saude = dependentes * 150.0 # R$ 150 fixo por dependente
    
    total_descontos = desc_vt + desc_vr + desc_saude
    salario_liquido = salario_base - total_descontos

    # Resultado
    print("-" * 30)
    print("FOLHA DE PAGAMENTO")
    print(f"INSS: R$ {inss:.2f}")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"(-) V.T. (6%): R$ {desc_vt:.2f}")
    print(f"(-) V.R. (20%): R$ {desc_vr:.2f}")
    print(f"(-) Plano (Dep.): R$ {desc_saude:.2f}")
    print(f"(=) Salário Líquido: R$ {salario_liquido:.2f}")
    print("-" * 30)

# Executar
calcular_folha()
