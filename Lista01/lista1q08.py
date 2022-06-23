"""Faça um programa que leia o nome de um aluno e as notas das três provas que ele
obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).
"""
# o \n vai quebrar a linha

aluno = input('Informe o seu nome:')
nota1 = float(input('Informe a sua primeira nota:'))
nota2 = float(input('Informe a sua segunda nota:'))
nota3 = float(input('informe a sua terceira nota:'))
media = (nota1 + nota2 + nota3) / 3
print(f'\nO aluno de nome {aluno} obteve média aritimética igual a {media:.1f}.')

"""Utilizando a função round()
"""

aluno = input('Informe o seu nome:')
nota1 = float(input('Informe a sua primeira nota:'))
nota2 = float(input('Informe a sua segunda nota:'))
nota3 = float(input('informe a sua terceira nota:'))
media = (nota1 + nota2 + nota3) / 3
media = round(media, 1)
print(f'\nO aluno de nome {aluno} obteve média aritimética igual a {media}.')
