"""
2. Escreva um programa que:
• Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N contendo elementos
inteiros (N será lido);
• Exiba a matriz lida (no formato de matriz);
• Exiba os elementos da diagonal principal, isto é, os elementos onde I = J.
"""

import random

ordem_n = int(input('Informe a ordem N da matriz: '))

# Definindo as linhas da matriz
matriz = [None] * ordem_n

# Definindo as colunas da matriz
for i in range(ordem_n):
    matriz[i] = [None] * ordem_n

# Preenchendo a matriz
for i in range(ordem_n):
    for j in range(ordem_n):
        matriz[i][j] = random.randint(1, 20)

# Exibindo a matriz
for i in range(ordem_n):
    for j in range(ordem_n):
        print(f'{matriz[i][j]:4}', end=' ')
    print()

# Exibir os números da diagonal principal
print('Elementos da diagonal principal:')

for i in range(ordem_n):
    for j in range(ordem_n):
        if i == j:
            print(f'{matriz[i][j]}')
