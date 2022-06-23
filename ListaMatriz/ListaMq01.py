"""
1. Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com
valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente). O programa
deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C).
Ao final, exiba as 3 matrizes (no formato de matriz).
"""

numero_linhas = 2
numero_colunas = 3

matriz_A = [None] * numero_linhas
matriz_B = [None] * numero_linhas
matriz_C = [None] * numero_linhas

# Definindo as colunas das matrizes A, B e C
for i in range(numero_linhas):
    matriz_A[i] = [None] * numero_colunas
    matriz_B[i] = [None] * numero_colunas
    matriz_C[i] = [None] * numero_colunas

# Lendo a matriz A
for i in range(numero_linhas):
    for j in range(numero_colunas):
        matriz_A[i][j] = int(input(f'Matriz A [{i}][{j}]: '))
print(matriz_A)

# Lendo a matriz B
for i in range(numero_linhas):
    for j in range(numero_colunas):
        matriz_B[i][j] = int(input(f'Matriz B [{i}][{j}]: '))
print(matriz_B)

# Somando a matriz A com a matriz B
for i in range(numero_linhas):
    for j in range(numero_colunas):
        matriz_C[i][j] = matriz_A[i][j] + matriz_B[i][j]

#  Imprimindo a matriz resultante C

print('Matriz resultante C:')

for i in range(numero_linhas):
    for j in range(numero_colunas):
        print(f'{matriz_C[i][j]:4}', end='')
    print()
