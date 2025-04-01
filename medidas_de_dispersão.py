# -*- coding: utf-8 -*-
"""Medidas_de_dispersão.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ukGDexeZbfLQvg184IhZXtWQzdCP3KvM
"""

import numpy as np # funções

#Cálculo de Amplitude
#12, 15, 20, 22
dados = np.array([12, 15, 20, 22])
amplitude = np.max(dados) - np.min(dados)
print(f'A amplitude dos dados é {amplitude}')

"""'''Variância e desvio padrão

Dados: 5,7,9,11,13
Calcule a variânicia e o desvio padrão dos dados, considerando que se trata
de uma população e quando se trata de uma amostra'''
"""

'''Variância e desvio padrão

Dados: 5,7,9,11,13 Calcule a variânicia e o desvio padrão dos dados, considerando
que se trata de uma população e quando se trata de uma amostra'''

dados2 = np.array([5, 7, 9, 11, 13])

#variância e desvio padrão populacional
variancia_populacional = np.var(dados2, ddof=0) # var = variância
desvio_padrao_populacional = np.std(dados2, ddof=0) #std = Standard Deviation

#variância e desvio padrão amostral
variancia_amostra1 = np.var(dados2, ddof=1) # var = variância
desvio_padrao_amostra1 = np.std(dados2, ddof=1) #std = Standard Deviation

print(f'A variância populacional é {variancia_populacional}')
print(f'O desvio padrão populacional é {desvio_padrao_populacional}')
print(f'A variância populacional é {variancia_amostra1}')
print(f'O desvio padrão populacional é {desvio_padrao_amostra1}')

''' Comparação de dispersão'''

# compara a dispersão dps dois conuntos de dados usando amplitude, variância e desvio padrão.

dados1_comparação = np.array([5, 5, 5, 5])
dados2_comparação = np.array([1, 3, 5, 7, 9])


#amplitude
amplitude1 = np.max(dados1_comparação) - np.min(dados1_comparação)
amplitude2 = np.max(dados2_comparação) - np.min(dados2_comparação)

#variância e desvio padrão populacional
variancia1 = np.var(dados1_comparação, ddof=0) # var = variância
desvio_padrao1 = np.std(dados1_comparação, ddof=0) #std = Standard Deviation

variancia2 = np.var(dados2_comparação, ddof=0) # var = variância
desvio_padrao2 = np.std(dados2_comparação, ddof=0) #std = Standard Deviation

print(f'A amplitude dos dados1 é {amplitude1}')
print(f'A amplitude dos dados2 é {amplitude2}')
print(f'A variância dos dados1 é {variancia1}')
print(f'A variância dos dados2 é {variancia2}')
print(f'O desvio padrão dos dados1 é {desvio_padrao1}')
print(f'O desvio padrão dos dados2 é {desvio_padrao2}')