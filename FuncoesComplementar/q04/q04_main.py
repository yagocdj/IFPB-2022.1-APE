"""
4. Faça um programa que leia duas matrizes de inteiros e gere uma terceira
matriz
que corresponderá a soma das duas matrizes lidas. A ordem das matrizes também
será lida.
O programa deverá conter as seguintes funções:
• Uma função para gerar e ler uma matriz, sendo passados como parâmetros a
ordem da matriz.
• Uma função para exibir uma matriz em sua representação clássica (linhas e
colunas).
• Uma função para somar duas matrizes.
"""

import q04_functions as q04f

# MAIN

# Lendo a ordem das duas matrizes
linhas = int(input('\nInforme a quantidade de linhas das matrizes: '))
colunas = int(input('Informe a quantidade de colunas das matrizes: '))

# Lendo a matriz_a
print('\nPreencha a matriz A:\n')
matriz_a = q04f.ler_matriz(linhas, colunas)

# Lendo a matriz_b
print('\nPreencha a matriz B:\n')
matriz_b = q04f.ler_matriz(linhas, colunas)

# Gerando uma matriz_c cujos elementos representam a soma das duas outras
# matrizes
print('\nMatriz que corresponde à soma das outras duas matrizes:\n')
matriz_resultante = q04f.soma_matriz(matriz_a, matriz_b)
q04f.exibir_matriz(matriz_resultante)
print()
