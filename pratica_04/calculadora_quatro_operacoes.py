""" enunciado questão 01
Desenvolva uma calculadora em Python que realize as quatro operações básicas 
(adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos 
tipos de erros de entrada e operação. Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.

As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

O programa deve continuar solicitando entradas até que uma operação válida seja concluída.

Trate os seguintes erros:

Entrada inválida (não numérica) para os números

Divisão por zero

Operação inválida

Use try/except para capturar e tratar os erros apropriadamente.

Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.

Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.
"""

while True:

    try: 

        numero_01 = float(input("Digite o primeiro número: "))
        numero_02 = float(input("Digite o segundo número: "))
        operacao = input("Digite uma das operações (+, -, * ou /): ")

        if operacao == "+":
            resultado = numero_01 + numero_02
        elif operacao == "-":
            resultado = numero_01 - numero_02
        elif operacao == "*":
            resultado = numero_01 * numero_02
        elif operacao == "/":
            resultado = numero_01 / numero_02
        else: 
            raise ValueError ("Entrada errada")                

        print(f"O resultado da operação é: {resultado}")
        break

    except ValueError as e:
        print(f"Erro: {e}.Digite apenas números")
    except ZeroDivisionError:
        print("Não é possível dividir por zero")         
