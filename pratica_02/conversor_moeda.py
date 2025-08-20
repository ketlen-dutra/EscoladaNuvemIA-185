#Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
#Valor em reais: R$ 100.00
#Taxa do dólar: R$ 5.60
#Taxa do euro: R$ 6.60 
#O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f"R$100.00 reais em dólares valem: US${valor_dolar:.2f}")
print(f"R$100.00 reais em euros valem: EUR{valor_euro:.2f}")
print("Valor em euro: EUR", round(valor_euro, 2))