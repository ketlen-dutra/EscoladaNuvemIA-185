#Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, 
#utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP 
#consultado.

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        if "erro" in dados:
            return "CEP não encontrado."
        return f"""
        CEP: {cep}
        Logradouro: {dados['logradouro']}
        Baiiro: {dados['bairro']}
        Cidade: {dados['localidade']}
        Estado: {dados['uf']}
        """
    except requests.RequestException as e:
        return f"Erro {e} na consulta"
    
def main():
    cep = input("Digite um CEP para consulta (apenas números):")
    print("\nConsultando CEP...\n")
    resultado = consultar_cep(cep)
    print(resultado)    

if __name__ == "__main__":
    main()    