#Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. 
# Calcule o salário do funcionário e exiba o resultado formatado corretamente.
#Entrada:
#O programa recebe 2 números inteiros e 1 número com duas casas decimais, representando:
#Número do funcionário (numero_funcionario).
#Quantidade de horas trabalhadas (horas_trabalhadas).
#Valor recebido por hora (valor_por_hora).
#Saída:
#Imprima o número do funcionário e o salário calculado com duas casas decimais. 
#Deve haver um espaço em branco antes e depois do sinal de igualdade, 
# e no caso do salário, também um espaço em branco após o R$

funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite quanto recebe por hora: "))

calculo_salario = horas_trabalhadas * valor_hora

print(f"Número do funcionário: {funcionario}")
print(f"Salário = R${calculo_salario:.2f}")