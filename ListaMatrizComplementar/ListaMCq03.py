"""
3. Escreva um programa que preencha uma matriz quadrada de ordem 3 com
valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente),
calcule e exiba:
• A soma dos elementos de cada linha;
• A soma dos elementos de cada coluna;
• A soma dos elementos da diagonal principal da matriz;
• A soma dos elementos da diagonal secundária da matriz;
• A soma de todos os elementos da matriz.
"""

from random import randint

ordem = 3
matriz = [ [None] * ordem for i in range(ordem) ]

# Preenchendo a matriz

for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = randint(1,10)

# Exibindo a matriz gerada

for vetor in matriz:
    for elemento in vetor:
        print(elemento, end='  ')
    print()

# Calculando as somas dos elementos de cada linha e dos elementos de cada
# coluna

print()
print('Soma dos elementos de cada linha:')

for i in range(ordem):
    soma_linha = 0
    for j in range(ordem):
        soma_linha += matriz[i][j]
    print(f'Linha {i}: {soma_linha}.')

print()
print('Soma dos elementos de cada coluna:')

for j in range(ordem):
    soma_coluna = 0
    for i in range(ordem):
        soma_coluna += matriz[i][j]
    print(f'Coluna {j}: {soma_coluna}.')

# Calculando a soma dos elementos da diagonal principal

print()
print('Soma dos elementos das diagonais principal e secundária:')

soma_diagonal_principal = 0
soma_diagonal_secundaria = 0

for i in range(ordem):
    for j in range(ordem):
        if i == j:
            soma_diagonal_principal += matriz[i][j]
        if i + j == ordem - 1:
            soma_diagonal_secundaria += matriz[i][j]

print('Diagonal principal:', soma_diagonal_principal)
print('Diagonal secundária', soma_diagonal_secundaria)
