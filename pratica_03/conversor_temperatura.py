#Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
#O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

temperatura_inicial = float(input("Informe a temperatura: "))
unidade_inicial = (input("Informe a unidade de demperatura: "))
unidade_final = (input("Informe a unidade para qual deseja converter: "))

if unidade_inicial == "C" and unidade_final == "F":
    conversao = ((temperatura_inicial * 1.8) + 32)
    print(f"Resultado: {conversao:.2f} F°")
elif unidade_inicial == "C" and unidade_final == "K":
    conversao = (temperatura_inicial + 273.15)
    print(f"Resultado: {conversao:.2f} K")
elif unidade_inicial == "F" and unidade_final == "C":
    conversao = ((temperatura_inicial - 32) / 1.8)
    print(f"Resultado: {conversao:.2f} C°")
elif unidade_inicial == "F" and unidade_final == "K":
    conversao = ((temperatura_inicial - 32) * 0.55 + 273)
    print(f"Resultado: {conversao:.2f} K")
elif unidade_inicial == "K" and unidade_final == "C":
    conversao = (temperatura_inicial - 273.15)
    print(f"Resultado: {conversao:.2f} C°")
elif unidade_inicial == "K" and unidade_final == "F":
    conversao = ((temperatura_inicial - 273.15) * 1.8 + 32)
    print(f"Resultado: {conversao:.2f} F°")    
else: print("Entrada inválida")




