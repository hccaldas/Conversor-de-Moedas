# Conversor de Moedas em Python

Este repositório contém um script em Python que converte valores de Dólar, Euro e Bitcoin para Reais (BRL) usando cotações atualizadas da internet.

## Funcionalidades

- Conversão de Dólar (USD) para Real (BRL)
- Conversão de Euro (EUR) para Real (BRL)
- Conversão de Bitcoin (BTC) para Real (BRL)
- Obtenção das cotações atualizadas através da API [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas).

## Pré-requisitos

- Python 3.x
- Biblioteca `requests` instalada. Você pode instalar essa biblioteca usando o comando:
  ```bash
  pip install requests

  Como usar
  
1.Clone este repositório ou copie o código para o seu ambiente local.
2.Certifique-se de ter o Python 3.x instalado no seu sistema.
3.Instale a biblioteca requests se ainda não estiver instalada.
4.Execute o script.
5.Selecione a moeda de origem digitando o número correspondente:
(1) Dólar
(2) Euro
(3) Bitcoin
6.Digite o valor da moeda de origem quando solicitado.
7.O valor convertido em Reais será exibido na tela.

Exemplo de Uso

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
