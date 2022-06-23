"""Escreva um programa que leia duas variáveis inteiras e troque o conteúdo entre elas,
mostrando o resultado.
"""

variavel1 = int(input('Digite um valor inteiro para variável um:'))
variavel2 = int(input('Digite um valor inteiro para a variavel dois:'))

print('\nAntes da troca')
print(variavel1, variavel2)

variavelAuxiliar = variavel1  # variavelAuxiliar -> "guarda" o valor da variavel1
variavel1 = variavel2
variavel2 = variavelAuxiliar

print('\nDepois da troca')
print(variavel1, variavel2)
