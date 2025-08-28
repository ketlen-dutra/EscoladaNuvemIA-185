#Crie uma função que verifique se uma palavra ou frase é um palíndromo 
#(lê-se igual de trás para frente, ignorando espaços e pontuação). 
#Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

def palindromo(frase):
    #removendo espaços e convertendo para minúsculo
    texto_limpo = ''.join(char.lower()
                          for char in frase
                          if char.isalnum())
    return texto_limpo == texto_limpo[::-1] #comparando o texto limpo com a versão invertida

texto = input("Digite uma frase ou palavra para verificar se é um palíndromo ou não: ")
resultado = palindromo(texto)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"  

print(f"'{texto}' é um palíndromo? {resposta}")      