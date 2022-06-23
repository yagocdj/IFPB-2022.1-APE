"""
1. Faça um programa que leia uma frase e determine a quantidade de brancos
contidos na mesma.
"""
frase = input('Digite uma frase: ')
quantidade_blank = frase.count(' ')

print(f'A frase digitada possui {quantidade_blank}.')

# Do jeito que Thiago gosta
# print(input('Digite um frase: ').count(' '))
# O código acima faz tudo que as outras três linhas fazem em uma só
