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

# Lendo a ordem das matrizes
ordem = int(input('Informe a ordem das matrizes: '))

# Lendo e exibindo a matriz_a
print('\nPreencha a matriz A:')
matriz_a = q04f.gerar_matriz(ordem)
print()
q04f.exibir_matriz(matriz_a)

# Lendo e exibindo a matriz_b
print('\nPreencha a matriz B:')
matriz_b = q04f.gerar_matriz(ordem)
print()
q04f.exibir_matriz(matriz_a)

# Somando matriz_a com matriz_b e exibindo uma matriz_c com o resultado
print('\nMatriz resultante C:')
matriz_c = q04f.somar_matriz(matriz_a, matriz_b, ordem)
q04f.exibir_matriz(matriz_c)
