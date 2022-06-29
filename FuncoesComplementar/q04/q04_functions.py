# Biblioteca de funções para a questão 4

# função para gerar e ler uma matriz, sendo passados como parâmetros a
# ordem da matriz.


def ler_matriz(linhas=3, colunas=3):
    matriz = []  # Vetor que receberá "linhas" vetores
    for i in range(linhas):
        vetor = []
        for j in range(colunas):
            vetor.append(int(input()))
        matriz.append(vetor)
    return matriz


# função para exibir uma matriz em sua representação clássica (linhas e
# colunas).


def exibir_matriz(matriz):
    for vetor in matriz:
        for elemento in vetor:
            print(elemento, end='  ')
        print()


# função para somar duas matrizes.


def soma_matriz(matriz1, matriz2):
    linhas = len(matriz1)
    colunas = len(matriz1[0])
    matriz_resultante = [[0] * colunas for i in range(linhas)]
    for linha in range(linhas):
        for coluna in range(colunas):
            matriz_resultante[linha][coluna] = matriz1[linha][coluna] + \
                matriz2[linha][coluna]
    return matriz_resultante
