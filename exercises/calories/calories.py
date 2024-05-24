"""
Este programa trata do exercício proposto no curso de Fundamentos para Ciência de Dados da Pós-graduação em Mineração de Dados Educacionais do IFES Serra - ES

A quantidade de calorias de um produto é uma variável aleatória de distribuição normal. Para a industria mu_0 = 31. Verificar se este valor condiz com um nível de aceitação de 5%.

H0: mu = 31 # igual
H1: mu != 31 # diferente
"""

#import modules
import pandas as pd
import numpy as np
import math

def t_test(mu_0, n, xbar, sd):
    return (xbar - mu_0) / (sd / math.sqrt(n))

def main():
    # Read data from a plain text and create dataframe
    data_array = np.genfromtxt('../../data/raw_data/Amostras-Industria.csv', delimiter=',')

    # Create dataframe from numpy array calories
    df = pd.DataFrame({'calories':data_array})
    print('Sample')
    print(df.head(3))

    # Inputs
    mu_0 = 31 # Média dos comprimidos alegada pela fábrica [g]
    n = len(df['calories']) # nº de observações
    t_critico = 2.064 # t crítico bicaudal obtido na tabela t de student para
                    # alfa = 0.05 = 5%
    xbar = df['calories'].mean() # média da amostra [g]
    sd = df['calories'].std() # desvio padrão [g]
    #alpha = 0.05 # nível de significância de 5%


    # Computation
    t = t_test( mu_0, n, xbar, sd)

    # Write out results
    if t > t_critico or t < -t_critico:
        print("Como t diferente valor crítico, rejeitamos H0")
        print('A média de calorias é diferente de 31')
    else:
        print("Como t <= valor crítico, aceitamos H0")
        print('De fato, a média de calorias  é 31')

if __name__ == '__main__':
    main()