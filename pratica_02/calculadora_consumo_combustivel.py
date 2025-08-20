# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:
#Distância percorrida: 300 km
#Combustível gasto: 25 litros 
#O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, 
# incluindo o resultado final arredondado para duas casas decimais.

distancia = 300
combustivel_gasto = 25

consumo_medio = 300 / 25

print(f"Distância percorrida: {distancia}Km \nCombustível gasto: {combustivel_gasto}L")
print(f"Consumo médio: {consumo_medio:.2f}Km/L")