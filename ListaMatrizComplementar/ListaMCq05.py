"""
5. A distância entre várias cidades é dada pela tabela abaixo (em km).

Faça um programa que:
• Armazene estas informações em uma matriz;
• Mostre a distância percorrida para um determinado percurso (informado
pelo usuário).
Exemplo: Dado o percurso 1, 2, 3, 2, 5, 1, 4, a distância percorrida é
15+10+10+28+12+5 = 80km.
"""

# Definindo a matriz

matriz = [[0, 15, 30, 5, 12], [15, 0, 10, 17, 28], [30, 10, 0, 3, 11],
          [5, 17, 3, 0, 80], [12, 28, 11, 80, 0]]

# Mostrando a distância para um percurso informado pelo usuário

cidade_origem = 0  # Linha
cidade_destino = 0  # Coluna
linha = 0
coluna = 0
distancia = 0
flag = 0
contador = 1  # Começa na 1ª repetição

print('\nA seguir, informe o percurso que você realizou (digite "0" na cidade '
      'de destino para encerrar o programa).')

cidade_origem = int(input('\nCidade de origem: '))

while True:
    cidade_destino = int(input('Cidade de destino: '))
    # Corrigindo a linha para que o valor fique compatível com a indexação
    # Obs.: A linha deve ser corrigida antes da cidade de origem ser atualizada
    linha = cidade_origem - 1
    # A nova cidade de origem é a antiga cidade de destino
    cidade_origem = cidade_destino
    if cidade_destino == flag:
        break
    print('\nCidade de origem: ', cidade_origem)
    # Corrigindo a coluna para que o valor fique compatível com a indexação
    coluna = cidade_destino - 1
    distancia += matriz[linha][coluna]

# Exibindo a distância percorrida pelo usuário

print(f'\nA distância percorrida é igual a {distancia}km.')
