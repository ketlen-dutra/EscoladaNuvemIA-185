#Leia quatro valores inteiros A, B, C e D. 
# A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
#Entrada: O arquivo de entrada contém 4 valores inteiros. 
#Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.

valor_a = int(input("Digite um número inteiro para A: "))
valor_b = int(input("Digite um número inteiro para B: "))
valor_c = int(input("Digite um número inteiro para C: "))
valor_d = int(input("Digite um número inteiro para D: "))

diferenca = valor_a * valor_b - valor_c * valor_d

print(f"DIFERENÇA = {diferenca}")