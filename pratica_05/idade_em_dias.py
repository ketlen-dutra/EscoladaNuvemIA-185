#Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

import datetime

def calcular_idade_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade_dias = calcular_idade_dias(ano_nascimento)
print(f"Sua idade aproximada em dias é: {idade_dias} dias")