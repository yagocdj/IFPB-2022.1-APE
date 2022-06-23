"""
3. Escreva um programa que gere aleatoriamente uma matriz quadrada A (cuja
ordem
será lida) e gere uma matriz B (da mesma ordem de A), onde cada elemento de
B
corresponderá ao respectivo elemento de A somado a ele os seus índices, sendo
que se
o elemento for de alguma diagonal (principal ou secundária) deverá ser 
colocado 0
(zero).
Veja o exemplo a seguir:

Ao final, imprima as duas matrizes (no formato de matriz).
"""

from random import randint

ordem_n = int(input('Informe a ordem N da matriz: '))

# Definindo as matrizes A e B
matriz_a = [[None] * ordem_n for i in range(ordem_n)]
matriz_b = [[None] * ordem_n for i in range(ordem_n)]

# Preenchendo a matriz A
for i in range(ordem_n):
    for j in range(ordem_n):
        matriz_a[i][j] = randint(1, 20)

# Criando a matriz B
for i in range(ordem_n):
    for j in range(ordem_n):
        if (i == j) or (i + j == (ordem_n - 1)):
            matriz_b[i][j] = 0
        else:
            matriz_b[i][j] = matriz_a[i][j] + (i + j)

# Exibindo as matrizes
print('Matriz A:')

for i in range(ordem_n):
    for j in range(ordem_n):
        print(f'{matriz_a[i][j]:4}', end=' ')
    print()

print('Matriz B:')

for i in range(ordem_n):
    for j in range(ordem_n):
        print(f'{matriz_b[i][j]:4}', end=' ')
    print()
