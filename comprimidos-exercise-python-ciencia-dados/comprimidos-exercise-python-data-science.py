"""
Pesos dos comprimidos: exercícios retirado de material didático
do professor de Fundamentos de Ciência de Dados

link
https://youtu.be/ILMx2seV2hM?si=y5aytfLPSmc78KIg&t=328

Numa fábrica, o peso dos comprimidos deve ser 5g. De uma amostra de
12 comprimidos foi obtida uma média de 5.05g, com um desvio padrão
de 0.1g. Considereando um nível de significância alpha de 0.05 = 5%,
vamos verificar se de fato os comprimidos em média têm 5g

H0: mu_0 = 5, a média dos comprimidos é 5g
H1: mu_0 > 5, a média dos comprimidos é maior que cinco gramas
"""

import math

def t_test(mu_0, n, xbar, sd):
    return (xbar - mu_0) / (sd / math.sqrt(n))

def main():
    # Inputs
    mu_0 = 5 # Média dos comprimidos alegada pela fábrica [g]
    n = 12 # nº de observações
    t_critico = 1.796 # t crítico calculado pela tabela t de student
    xbar = 5.05 # média da amostra [g]
    sd = 0.1 # desvio padrão [g]
    alpha = 0.05 # nível de significância de 5%

    # Computation
    t = t_test( mu_0, n, xbar, sd)

    # Write out results
    if t > t_critico:
        print("Como t > valor crítico, rejeitamos H0")
        print('A média dos comprimidos é maior que 5g')
    else:
        print("Como t <= valor crítico, aceitamos H0")
        print('De fato, a média dos comprimidos é 5g')

if __name__ == '__main__':
    main()