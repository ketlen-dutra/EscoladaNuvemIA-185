""""
Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

produto = "Cadeira Infantil"
preco = 12.40
quantidade = 3

total = preco * quantidade
print(f"Resumo da compra\n Produto: {produto}\n Preço unitário: R${preco:.2f}\n Quantidade: {quantidade}\n Valor total da compra: R${total:.2f}")