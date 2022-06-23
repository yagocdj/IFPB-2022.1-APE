# Multiplicando matrizes

from random import randint

# Lendo as quantidades de linhas e colunas da matriz A
linhas_a = int(input('Informe o número de linhas da primeira matriz: '))
colunas_a = int(input('Informe o número de colunas da primeira matriz: '))

matriz_a = [[0] * colunas_a for i in range(linhas_a)]

print('\nO número de linhas da segunda matriz deve ser igual ao número '
      'de colunas da primeira.')

# Lendo as quantidades de linhas e colunas da matriz B
linhas_b = colunas_a
colunas_b = int(input('\nInforme o número de colunas da segunda matriz: '))

matriz_b = [[0] * colunas_b for i in range(linhas_b)]

# Criando a matriz resultante C

linhas_c = linhas_a
colunas_c = colunas_b

matriz_c = [[0] * colunas_c for i in range(linhas_c)]

# Preenchendo as matrizes A e B

for i in range(linhas_a):
    for j in range(colunas_a):
        matriz_a[i][j] = randint(1, 9)

for i in range(linhas_b):
    for j in range(colunas_b):
        matriz_b[i][j] = randint(1, 9)

# Multiplicando as matrizes A e B e armazenando os resultados na matriz C

# PROGRAMA EM CONSTRUÇÃO
