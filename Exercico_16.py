import os

os.system


ano_nascimento = int(input("Digite o ano do seu nascimento: "))
sexo = input("Digite seu sexo: ").lower()


idade = 2026 - ano_nascimento 

idade_obrigatório = idade >= 18
sexo_obrigatório  = sexo == "masculino"


if idade_obrigatório and sexo_obrigatório:
    print("Deve se apresenatar ao serviço militar obrigatório!")
else:
    print("Não é necessário apresentar-se.")

    




