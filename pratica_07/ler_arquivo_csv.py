"""
Crie um script en Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter 
informações de pessoas, com colunas Nome, Idade e Cidade.
"""

import csv

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print("Arquivo não encontrado")

if __name__ == "__main__":
    nome_arquivo = input("\nDigite o nome do arquivo: \n").strip()
    ler_csv(nome_arquivo)        
