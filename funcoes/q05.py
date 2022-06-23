"""
5. Escreva um programa que leia as 3 notas de um aluno, determine e exiba a sua
média e seu conceito.
O programa deve conter as seguintes funções:
• Uma função que recebe como parâmetros as 3 notas do aluno e retorne a sua
média (aritmética).
• Uma função que receba como parâmetro a média do aluno e retorne o seu
conceito, de acordo com a tabela abaixo:

MÉDIA CONCEITO
>= 8,0    A
>= 5,0 e < 8,0 B
< 5,0 C
"""

# função da média aritmética


def media(vetor_valores, quantidade_valores):
    soma_valores = 0
    for i in range(quantidade_valores):
        soma_valores += vetor_valores[i]
    media_aritmetica = soma_valores / quantidade_valores
    return media_aritmetica

# função do conceito


def conceito(media):
    if media >= 8.0:
        return 'A'
    elif media >= 5.0:
        return 'B'
    else:
        return 'C'


# exibindo média e conceito
quantidade_notas = int(input('Informe a quantidade de notas: '))
print(f'\nAgora digite as {quantidade_notas} notas do aluno:')
notas = [float(input(f'nota {i + 1}: ')) for i in range(quantidade_notas)]

media_aluno = media(notas, quantidade_notas)
conceito_aluno = conceito(media_aluno)

print(f'Média do aluno: {media_aluno:.1f}')
print('Conceito do aluno:', conceito_aluno)
