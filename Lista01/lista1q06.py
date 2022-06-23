"""Faça um programa que efetue a apresentação do valor da conversão em real (R$)
de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do
dólar e também a quantidade de dólares disponíveis com o usuário.
"""

cotacao = float(input('Digite o valor da cotação atual do dólar:'))
qtdUsd = float(input('Informe quantos dólares você possui:'))
qtdReal = qtdUsd * cotacao
print(f'Você possui R${qtdReal:.2f}.')
