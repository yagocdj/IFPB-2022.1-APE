# Correção da prova 2 de APE

from random import randint

# Criando a matriz e os vetores

ordem = 5
matriz = [[0] * ordem for i in range(ordem)]
diagonal_principal = [0] * ordem
diagonal_secundaria = [0] * ordem

# Gerando a matriz e armazenado as diagonais nos vetores

for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = randint(1, 30)
        if i == j:
            diagonal_principal[i] = matriz[i][j]
        if i + j == ordem - 1:
            diagonal_secundaria[i] = matriz[i][j]

# Exibindo a matriz

for vetor in matriz:
    for elemento in vetor:
        print(elemento, end=' ')
    print()

# Exibindo os vetores

print(f'\nDiagonal principal: {diagonal_principal}')
print(f'\nDiagonal secundária: {diagonal_secundaria}')
