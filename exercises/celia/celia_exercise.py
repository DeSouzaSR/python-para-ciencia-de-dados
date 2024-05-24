"""
Exercício de Python para Ciência de Dados

link:
https://youtu.be/ILMx2seV2hM?si=c0bq3ELItaFyhjOf

Celia faz uma viagem regular de carro para o trabalho que, anteriormente levava uma média de 42 minutos. O conselho local alterou recentemente o layout da estrada e Celia está convencida de que isso aumentou o tempo de viagem. Para investigar, ela registra o tempo de 12 viagens. As 12 viagens têm um tempo médio de 50 minutos e um desvio padrão de 15 minutos.

Realize um teste de hipótese adequado no nível de 5% para identificar se há evidências de sua discordância de que o tempo médio de viagem aumentou.

H0: mu = 42
H1: mu > 42

Este é um teste unicaudal porque mu deve ser maior que 42 min. Portanto, a área de rejeição é de 0.05 ou 5%.

df = n - 1 = 12 - 1 = 11$ graus de liberdade da amostra

Olhando na tabela de distribuições t:

Valor crítico = 1.796
"""
import math

def t_test(mu_0, mu, xbar, s):
    return (xbar - mu_0) / (s / math.sqrt(mu))

def main():
    #  Inputs
    t_critico = 1.796
    mu_0 = 42
    mu = 12
    xbar = 50
    s = 15

    # Computation
    t = t_test( mu_0, mu, xbar, s)

    # Write out results
    if t > t_critico:
        print("Como t > valor crítico, rejeitamos H0")
    else:
        print("Como t <= valor crítico, aceitamos H0")

if __name__ == '__main__':
    main()