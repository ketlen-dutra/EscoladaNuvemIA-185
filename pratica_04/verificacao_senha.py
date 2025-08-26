#Crie um programa que verifique se uma senha é forte. 
#Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 
#O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.

while True:

    senha = input("\nDigite uma senha ou digite 'fim': ")
    
    if senha.lower() == "fim":
        print("Programa encerrado")
        break

    if len(senha) < 8:
        print("Senha fraca. A senha precisa ter pelo 8 caracteres")
        continue

    if not any(caractere.isdigit() for caractere in senha):
        print("Senha fraca. A senha precisa ter pelo menos um número")
        continue

    if not any(caractere.isalpha() for caractere in senha):
        print("Senha fraca. A senha precisa ter pelo menos uma letra")
        continue

    if not any(caractere.isupper() for caractere in senha):
        print("Senha fraca. A senha precisa ter pelo menos uma letra maiúscula")
        continue

    simbolos = "!@#$%&"
    if not any(caractere in simbolos for caractere in senha):
        print("Senha fraca. A senha precisa ter pelo menos uma caractere especial '!@#$%&'")
        continue

    print("Senha válida")
    break    