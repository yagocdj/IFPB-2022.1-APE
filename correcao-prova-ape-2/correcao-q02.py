# Correção prova 2 de APE

quantidade_times = 10  # Linhas
quantidade_jogadores = 12  # Colunas
alturas = [[0] * quantidade_jogadores for i in range(quantidade_times)]

# Preenchendo a matriz com as alturas dos jogadores de cada time e calculando as médias

print('\nDigite as alturas dos jogadores de cada time.')

media_time = 0.0
maior_media = 0.0
time_maior = 0

for i in range(quantidade_times):
    print(f'\nTime {i + 1}')
    soma_altura = 0
    for j in range(quantidade_jogadores):
        alturas[i][j] = float(input(f'Jogador {j + 1}: '))
        soma_altura += alturas[i][j]
    media_time = soma_altura / quantidade_jogadores
    if maior_media < media_time:
        maior_media = media_time
        time_maior = i + 1
    print(f'Média de altura do time {i + 1}: {media_time:.2f}m.')

# Exibindo qual é o time com maior média

print(f'\nO time com a maior média de altura é o time {time_maior}.')
