#Instalação dos pacotes utilizados
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Convertendo arquivo 'csv' em datafra pandas
price_gas = pd.read_csv('gasolina.csv', sep=',') 
price_gas.head()


#Visualização gráfica dos dados e salvando imagem em png
with sns.axes_style('darkgrid'):
  plt.figure(figsize=(9, 5)) # Altere a largura e a altura para ajustar o tamanho do gráfico
  grafico_price_gas = sns.lineplot(data=price_gas, x='dia', y='venda', palette='pastel')
  grafico_price_gas.set(title='Preço da Gasolina, de 1 a 10/07/2021, na cidade de São Paulo', xlabel='dia', ylabel='preço')
  grafico_price_gas.grid(False) #retirando o grid visando deixar melhor a visualização
  grafico_price_gas.set_title('Preço da Gasolina, de 1 a 10/07/2021, na cidade de São Paulo', fontsize=15)
  grafico_price_gas.set_xlabel('Dia', fontsize=14) 
  grafico_price_gas.set_ylabel('Preço', fontsize=14)
  plt.savefig('grafico_gasolina.png')
plt.show()