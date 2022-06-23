"""
5. Escreva um programa que:
• Crie uma matriz de ordem 20 x 4 e armazene nela as 3 notas dos 20 alunos de
uma
turma e a média de cada um deles.
o As notas serão lidas e armazenadas nas 3 primeiras colunas da matriz;
o As médias serão calculadas e armazenadas na 4a coluna da matriz.
• Imprima as notas dos alunos e suas respectivas médias (no formato de matriz).
• Calcule e imprima a média geral da turma.
• Calcule e imprima o número de alunos com média superior à média geral da
turma.
"""

from random import uniform

numero_alunos = 20  # Número de linhas
numero_notas = 3  # Número de colunas menos um

# Definindo a matriz que comportará as notas
notas = [ [None] * (numero_notas + 1) for i in range(numero_alunos) ]

# Preencher a matriz e calcular as médias dos alunos
print('Para fins de teste, as notas dos alunos estão sendo geradas.')
for linha in range(numero_alunos):
    soma_alunos = 0.0
    for coluna in range(numero_notas):
        notas[linha][coluna] = round(uniform(1, 10), 1)
        soma_alunos += notas[linha][coluna]
        media_aluno = soma_alunos / (numero_notas)
    notas[linha][numero_notas] = media_aluno

# Exibindo as notas dos alunos e suas respectivas médias
print('\n          1ª NOTA  2ª NOTA  3ª NOTA    MÉDIA')
for linha in range(numero_alunos):
    print(f'Aluno {linha + 1}:', end='')
    for coluna in range(numero_notas + 1):
        print(f'{notas[linha][coluna]:9.1f}', end='')
    print()

# Calculando a média geral da turma
print()
soma_geral = 0

for linha in range(numero_alunos):
    soma_geral += notas[linha][numero_notas]
media_geral = soma_geral / numero_alunos
print(f'\nMédia geral da turma: {media_geral:.1f}')

# Alunos com média superior à média geral
print()
alunos_acima = 0

for linha in range(numero_alunos):
    if notas[linha][numero_notas] > media_geral:
        alunos_acima += 1

print(f'Quantidade de alunos acima da média: {alunos_acima}.')
