#Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:
#Nota 1: 7.5
#Nota 2: 8.0
# #Nota 3: 6.5 
#O programa deve calcular a média e exibir todas as notas e o resultado final, 
# arredondando para duas casas decimais.

nota01, nota02, nota03 = 7.5, 8.0, 6.5

media = (nota01 + nota02 + nota03) / 3

print(f"Notas do primeiro bimestre: \n Nota 1: {nota01} \n Nota 2: {nota02} \n Nota 3: {nota03}")
print(f"Media final do primeiro bimestre: {media:.2f}")
print("Media final do primeiro bimestre:",round(media,2))