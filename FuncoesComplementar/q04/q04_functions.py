# Biblioteca de funções da questão 4

"""
Função para gerar e ler uma matriz, tendo a ordem como parâmetro
"""


def gerar_matriz(ordem):
    matriz = []
    for i in range(ordem):
        vetor = []
        for j in range(ordem):
            vetor.append(int(input()))
        matriz.append(vetor)
    return matriz


"""
Função para exibir a matriz em sua representação clássica (linhas e colunas)
"""


def exibir_matriz(matriz):
    for vetor in matriz:
        for elemento in vetor:
            print(elemento, end=' ')
        print()


"""
Função para somar duas matrizes
"""

# Obs.: as matrizes devem possuir a mesma ordem


def somar_matriz(matriz1, matriz2, ordem):
    matriz_resultante = [[0] * ordem for i in range(ordem)]
    for i in range(ordem):
        for j in range(ordem):
            matriz_resultante[i][j] = matriz1[i][j] + matriz2[i][j]
    return matriz_resultante


""" n = int(input('Ordem: '))
matrix = gerar_matriz(n)
exibir_matriz(matrix) """
