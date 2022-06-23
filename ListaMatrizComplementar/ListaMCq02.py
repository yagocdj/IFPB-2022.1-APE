"""
Uma matriz quadrada contendo valores inteiros é denominada quadrado
mágico quando a soma dos elementos de cada linha, a soma dos elementos
de cada coluna e a soma dos elementos das diagonais principal e secundária
são todos iguais. Por exemplo, a matriz seguinte é um quadrado mágico.

Escreva um programa que preencha uma matriz com valores fornecidos pelo
usuário, determine e mostre se ela é um quadrado mágico.
"""

ordem = int(input('\nInforme a ordem da matriz: '))
matriz = [[0] * ordem for i in range(ordem)]

print()

# Preenchendo a matriz (com input)

for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = int(input(f'Linha {i} /coluna {j}: '))

print()

# Imprimindo a matriz

for vetor in matriz:
    for elemento in vetor:
        print(elemento, end=' ')
    print()

# Verificando se ela é um quadrado mágico

quadrado_magico = True
soma_diagonal_principal = 0
soma_diagonal_secundaria = 0

for i in range(ordem):
    soma_diagonal_principal += matriz[i][i]

for i in range(ordem):
    soma_linha = 0
    soma_coluna = 0
    for j in range(ordem):
        soma_linha += matriz[i][j]
        soma_coluna += matriz[j][i]
    if (soma_linha != soma_diagonal_principal) or \
            (soma_coluna != soma_diagonal_principal):
        quadrado_magico = False
        break

for i in range(ordem):
    for j in range(ordem):
        if i + j == ordem - 1:
            soma_diagonal_secundaria += matriz[i][j]

if soma_diagonal_principal != soma_diagonal_secundaria:
    quadrado_magico = False

# Resultado das análises

if quadrado_magico:
    print('\nEssa matriz é um quadrado mágico')
else:
    print('\nEssa matriz não é um quadrado mágico')
