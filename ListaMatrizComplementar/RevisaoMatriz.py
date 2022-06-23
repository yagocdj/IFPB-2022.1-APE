"""
Faça um programa que receba o nome e as 3 notas dos 20 alunos de uma turma e:
a) calcule:
- a média aritmética de cada aluno;
- a situação de cada aluno; (aprovado se média superior ou igual a 7.0)
- o número de alunos aprovados;
- a média geral da turma;
b) exiba:
- o nome e a situação de cada aluno;
- o número de alunos aprovados;
- a média geral da turma;
- o nome e a média dos alunos com média superior ou igual à média geral da
turma.
-> Use vetores para armazenar nome, média e situação, e uma matriz para
armazenar as notas.
"""

from random import randint

# Gerar a matriz das notas

quantidade_alunos = 20  # Linhas
quantidade_notas = 3  # Colunas

notas = [[0] * quantidade_notas for i in range(quantidade_alunos)]

# Gerar os vetores dos nomes, das médias e da situação de cada aluno

nomes = [0] * quantidade_alunos
medias = [0] * quantidade_alunos
situacao = [0] * quantidade_alunos

# Ler os dados

media_aluno = 0.0
soma_medias = 0.0

print('\nInforme os nomes dos alunos.')
print()

for i in range(quantidade_alunos):
    # Receber o nome de cada aluno
    nomes[i] = input('Nome: ')
    soma_aluno = 0
    for j in range(quantidade_notas):
        # Gerar as 3 notas para cada aluno
        notas[i][j] = randint(1,10)
        soma_aluno += notas[i][j]
    media_aluno = soma_aluno / quantidade_notas
    medias[i] = media_aluno
    soma_medias += medias[i]
    # Armazenando a situação de cada aluno
    if media_aluno >= 7:
        situacao[i] = 'aprovado'
    else:
        situacao[i] = 'reprovado'

# Cálculo do número de alunos aprovados

quantidade_aprovados = 0

for i in range(quantidade_alunos):
    if situacao[i] == 'aprovado':
        quantidade_aprovados += 1

# Cálculo da média geral

media_geral = soma_medias / quantidade_alunos

print(f'\nMédia geral da turma: {media_geral:.1f}.')

# Exibindo o nome e a situação de cada aluno

for i in range(quantidade_alunos):
    print(f'\nNome do aluno: {nomes[i]}.')
    print(f'Situação: {situacao[i]}.')

# Exibindo o nome e a média dos alunos com média superior a média geral

print(f'\nAlunos com média superior ou igual à média geral da turma:')
print()

for i in range(quantidade_alunos):
    if medias[i] >= media_geral:
        print(f'{nomes[i]} com média {medias[i]:.1f}.')

print('\nFim do programa.')
