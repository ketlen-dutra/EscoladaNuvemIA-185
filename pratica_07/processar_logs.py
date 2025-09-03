"""Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. 
Calcule a média e o desvio padrão do tempo de exercução constantes.
"""

import pandas as pd

def processar_logs_treinamento(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        media_tempo = df['tempo_execucao'].mean()
        desvio_padrao = df['tempo_execucao'].std()
        print(f"Média do tempo de execução: {media_tempo:.2f}")
        print(f"DP tempo de execução: {desvio_padrao:.2f} segundos")
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as e:
        print(f"Erro {e} ao processar arquivo")

nome_arquivo = input("\nDigite o nome do arquivo: \n")
processar_logs_treinamento(nome_arquivo)                