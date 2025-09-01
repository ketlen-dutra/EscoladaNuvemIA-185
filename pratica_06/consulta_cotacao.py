"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). 
O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, 
máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os 
dados de cotação.

   "USDBRL": {
        "code": "USD",
        "codein": "BRL",
        "name": "Dólar Americano/Real Brasileiro",
        "high": "5.734",
        "low": "5.7279",
        "varBid": "-0.0054",
        "pctChange": "-0.09",
        "bid": "5.7276",
        "ask": "5.7282",
        "timestamp": "1618315045",
        "create_date": "2021-04-13 08:57:27"
"""

import requests

def cotacao_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        cotacao = dados[f"{moeda}BRL"]
        return f"""
        Moeda: {moeda} para BRL
        Valor atual: R${float(cotacao['bid']):.2f}
        Máximo: R${float(cotacao['high']):.2f}
        Mínimo: R${float(cotacao['low']):.2f}
        Data/Hora: {cotacao['create_date']}
        """
    except requests.RequestException as e:
        return f"Erro {e} ao obter a cotação."
    except KeyError:
        return f"Moeda não suportada ou não encontrada."
    
def main():
    moeda = input("Digite o código da moeda para cotação (ex: USD, EUR, GBP): ").upper().strip()
    print("\nObtendo cotação...\n")
    resultado = cotacao_moeda(moeda)
    print(resultado)

if __name__ == "__main__":
    main() 

