#Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
#O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
#calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.
#< 18.5: classificacao = "Abaixo do peso" 
#< 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite sua altura em metros:"))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else: classificacao = "Obeso"

print(f"Seu IMC é de: {imc:.1f}")
print(f"A sua classificação na tabela de IMC é: {classificacao}")