#Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:
#Nome do produto: "Camiseta"
#Preço original: R$ 50.00
#Porcentagem de desconto: 20% 
#O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

nome_produto = 'Camiseta'
preço_original = 50.00
desconto = 0.20

calculo_desconto = preço_original * desconto
preco_final = preço_original - calculo_desconto

print(f"Nome do produto: {nome_produto}\nPreço: R$ {preço_original:.2f}")
print(f"Porcentagem de desconto: 20%")
print(f"Preço final: R$ {preco_final:.2f}")