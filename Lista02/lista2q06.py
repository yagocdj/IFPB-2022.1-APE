# 6. Recomendam-se estudantes para bolsas de estudo em função de seu desempenho.
# A natureza das recomendações é baseada na seguinte tabela:
#  TABELA
# Escreva um programa que leia o nome e o conceito de um estudante e exiba o nome do
# estudante e sua respectiva recomendação.

nome = input('Digite o nome do estudante: ')
conceito = input('Digite o conceito do estudante: ').upper()

if conceito == 'A':
    recomendacao = 'fortemente recomendado'
elif conceito == 'B' or conceito == 'C':
    recomendacao = 'recomendado'
else:
    recomendacao = 'não recomendado'

print(f'Nome: {nome}; recomendação: {recomendacao}.')
