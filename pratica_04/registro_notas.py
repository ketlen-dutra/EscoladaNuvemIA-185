#Crie um programa que permita a um professor registrar as notas de uma turma. 
#O programa deve continuar solicitando notas até que o professor digite 'fim'. 
#Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. 
#No final, deve exibir a média da turma.

notas = []
while True:
    try:
        entrada_notas = input("Digite a nota do aluno ou digite 'fim' para encerrar: ")
        if entrada_notas.lower() == "fim":
            break
        nota = float(entrada_notas)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida, digite um valor de 0 à 10")  
            continue
    except ValueError:
        print("Entrada inválida. Digite um número válido ou 'fim' para encerrar")

if notas:
    media = sum(notas) / len(notas)
    print(f"A média da turma é: {media:.2f}")
    print(f"Total de notas válidas: {len(notas)}") 
else:
    print("Dados insuficientes")             


