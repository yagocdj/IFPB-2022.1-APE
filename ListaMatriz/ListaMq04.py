"""
4. Uma matriz transposta é a matriz que se obtém da troca de linhas por
colunas de uma
dada matriz.
Assim, dada uma matriz C de ordem m x n, a matriz transposta dela será
representada
por Ct de ordem n x m, onde cada elemento de Ct[i,j] = C[j,i].

Escreva um programa que preencha uma matriz 3x5 com valores inteiros fornecidos
pelo usuário (ou gerados aleatoriamente) e gere a sua transposta. Ao final,
imprima as
duas matrizes (no formato de matriz).
"""

from random import randint

numero_linhas = int(input('Informe o número de linhas: '))
numero_colunas = int(input('Informe o número de colunas: '))

# Definindo a matriz e sua transposta
matriz = [ [None] * numero_colunas for i in range(numero_linhas) ]
transposta = [ [None] * numero_linhas for i in range(numero_colunas) ]

for linha in range(numero_linhas):
    for coluna in range(numero_colunas):
        matriz[linha][coluna] = randint(1, 30)
        transposta[coluna][linha] = matriz[linha][coluna]

# Imprimindo a matriz
print(f'\033[1;36m Matriz:')
print()

for linha in range(numero_linhas):
    for coluna in range(numero_colunas):
        print(f'\033[1;36m{matriz[linha][coluna]:4}', end=' ')
    print()

# Imprimindo a transposta
print(f'\033[1;35m Transposta:')
print()

for linha in range(numero_colunas):
    for coluna in range(numero_linhas):
        print(f'\033[1;35m{transposta[linha][coluna]}', end=' ')
    print()
