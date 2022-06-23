"""
1. Uma matriz de permutação é uma matriz quadrada cujos elementos são 0's
ou 1's, tal que em cada linha e em cada coluna exista apenas um elemento
igual a 1. Por exemplo, a matriz seguinte é uma matriz de permutação.

Com base na definição apresentada, escreva um programa que preencha uma
matriz quadrada com valores fornecidos pelo usuário, determine e mostre se
ela é uma matriz de permutação.
"""

ordem = int(input('Informe a ordem da matriz: '))
matriz = [[0] * ordem for i in range(ordem)]

# Preenchendo a matriz

print(f'Digite {ordem * ordem} inteiros para a matriz a seguir.')

for linha in range(ordem):
    for coluna in range(ordem):
        matriz[linha][coluna] = int(input(f'Linha {linha} /coluna {coluna}: '))

# Verificar se é uma matriz de permutação

permutacao = True

for linha in range(ordem):
    soma_linha = 0
    soma_coluna = 0
    for coluna in range(ordem):
        soma_linha += matriz[linha][coluna]
        soma_coluna += matriz[coluna][linha]
    if (soma_linha != 1) or (soma_coluna != 1):
        permutacao = False
        break
    else:
        permutacao = True

# Exibindo a matriz e a verificação (permutacao = True ou permutacao = False)

print()

for vetor in matriz:
    for elemento in vetor:
        print(elemento, end='  ')
    print()

print()

if permutacao:
    print('Essa matriz é de permutção.')
else:
    print('Essa matriz não é de permutação.')
