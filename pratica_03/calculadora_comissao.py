#Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
#efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
#sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais. 

#Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de
#dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e
#montante total das vendas efetuadas por este vendedor, respectivamente. 

#Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

nome = input("Insira o nome do vendedor: ")

salario_fixo = float(input("Informe o salário fixo: "))
total_vendas = float(input("Informe o total de vendas: "))

percentual_comissao = 0.15

comissao = total_vendas * percentual_comissao

salario_total = salario_fixo + comissao

print(f"Nome do funcionário: {nome}")
print(f"Salário fixo: R${salario_fixo:.2f}")
print(f"Total de vendas: {total_vendas}")
print(f"Comissão: R${comissao:.2F}")
print(f"Salário total: R${salario_total:.2f}")