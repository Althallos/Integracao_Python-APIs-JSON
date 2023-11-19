import requests
import json
import pandas as pd

#       API da Cotação Atual de Todas as Moedas

#   Pegar a cotação atual de todas as moedas
"""cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacoes_dict = cotacoes.json()
cotacao_df = pd.DataFrame(cotacoes_dict)
print(cotacao_df)"""


#   Pegar cotação dos ultimos 30 dias do Dólar
"""cotacoes_dolar30d = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
cotacoes_dolar_dict = cotacoes_dolar30d.json()
cotacoes_dolar_df = pd.DataFrame(cotacoes_dolar_dict)
print(cotacoes_dolar_df)"""


#   Pegar as cotações do BitCoin de Jan/20 a Out/20
"""import matplotlib.pyplot as plt
cotacao_btc = requests.get('https://economia.awesomeapi.com.br/BTC-BRL/200?start_date=20200101&end_date=20201031')
cotacao_btc_dict = cotacao_btc.json()
lista_cotacao_btc = [float(item['bid']) for item in cotacao_btc_dict]

#   Inverte a ordem
lista_cotacao_btc.reverse()

plt.figure(figsize=(15, 5))
plt.plot(lista_cotacao_btc)
plt.show()"""