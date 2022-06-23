"""
4. Uma análise dos acidentes de trânsito está sendo realizada em Manhattan,
New York. Os cruzamentos das ruas 30 a 38 com as avenidas 1a a 10a foram
estudadas.
Faça um programa para, a partir da informação acima, processar a matriz de
acidentes resultante desse estudo.
Para cada acidente, será informado o local do cruzamento (Avenida x Rua). O
programa deverá ler um número desconhecido de acidentes (utilize qualquer
condição de parada a sua escolha).
Ao final da leitura dos dados, o programa deverá gerar e exibir a matriz de
acidentes (obs: exiba na matriz os cabeçalhos de linha e de coluna mostrando
a identificação das ruas e das avenidas)
"""

quantidade_avenidas = 10  # Linhas
quantidade_ruas = 9  # Colunas
avenida = int()
rua = int()
linha = int()
coluna = int()

matriz = [[0] * quantidade_ruas for i in range(quantidade_avenidas)]

flag = 0
contador = 0

# Preenchendo a matriz com o local do cruzamento em que aconteceu cada acidente

print('\nA seguir, informe a localização do cruzamento em que ocorreu'
      'o acidente (Avenida x Rua ou "0" para encerrar o programa).')

while True:
    avenida = int(input('\nNº da avenida: '))
    if avenida == flag:
        break
    linha = avenida - 1
    rua = int(input('Nº da rua: '))
    coluna = rua - 30
    matriz[linha][coluna] += 1

# Exibição: criando o cabeçalho das colunas.

print('\nMapa dos acidentes')
print('\nRua/Av.', end='')
for i in range(quantidade_ruas):
    print(f'{i + 30:4}', end='')
print()

# Exbibição: exibindo a matriz

for i in range(quantidade_avenidas):
    print(f'{i + 1:4}   ', end='')
    for j in range(quantidade_ruas):
        print(f'{matriz[i][j]:>4}', end='')
    print('')

print('\nFim do programa.')
