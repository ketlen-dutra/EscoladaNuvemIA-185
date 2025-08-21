#Crie um programa que solicite a idade do usuário e classifique-o
#em uma das seguintes categorias:
#Criança (0-12 anos),
#Adolescente (13-17 anos),
#Adulto (18-59 anos)
#Idoso (60 anos ou mais).

idade = int(input("Digite a sua idade: "))

if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:print("Idoso")



