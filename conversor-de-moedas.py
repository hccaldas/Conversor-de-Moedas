# requests para buscar a cotação atual.

# importar a biblioteca resquests - pip install requests
# import requests



import requests

def cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    response = requests.get(url)
    data = response.json()
    cotacao = float(data['USDBRL']['high'])
    return cotacao

def cotacao_euro():
    url = "https://economia.awesomeapi.com.br/json/last/EUR-BRL"
    response = requests.get(url)
    data = response.json()
    cotacao = float(data['EURBRL']['high'])
    return cotacao

def cotacao_bitcoin():
    url = "https://economia.awesomeapi.com.br/json/last/BTC-BRL"
    response = requests.get(url)
    data = response.json()
    cotacao = float(data['BTCBRL']['high'])
    return cotacao

def conversor_dolar_real(valor_dolar):
    cotacao = cotacao_dolar()
    valor_real = valor_dolar * cotacao
    return valor_real

def conversor_euro_real(valor_euro):
    cotacao = cotacao_euro()
    valor_real = valor_euro * cotacao
    return valor_real

def conversor_bitcoin_real(valor_bitcoin):
    cotacao = cotacao_bitcoin()
    valor_real = valor_bitcoin * cotacao
    return valor_real

print("Selecione a moeda de origem:")
print("1 - Dólar")
print("2 - Euro")
print("3 - Bitcoin")

moeda_origem = input("Digite sua opção (1/2/3): ")
valor_moeda_origem = float(input("Digite o valor da moeda de origem: "))
valor_moeda_real = 0

if moeda_origem == '1':
    valor_moeda_real = conversor_dolar_real(valor_moeda_origem)
    print(f"O valor em reais é R${valor_moeda_real:.2f}")
elif moeda_origem == '2':
    valor_moeda_real = conversor_euro_real(valor_moeda_origem)
    print(f"O valor em reais é R${valor_moeda_real:.2f}")
elif moeda_origem == '3':
    valor_moeda_real = conversor_bitcoin_real(valor_moeda_origem)
    print(f"O valor em reais é R${valor_moeda_real:.2f}")
else:
    print("Opção inválida")