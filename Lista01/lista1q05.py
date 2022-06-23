""" Escreva um programa para ler o nome e o sobrenome de uma pessoa e escrevê-los na seguinte forma: sobrenome seguido
por uma vírgula e pelo nome.
"""

nome = input('Digite o seu nome:')
sobrenome = input('Digite o seu sobrenome:')
print()
print(f'{sobrenome}, {nome}.')

"""ou
"""


nome = input('Digite o seu nome:')
sobrenome = input('Digite o seu sobrenome:')
print()
print(sobrenome, ',', nome, sep='')

"""ou
"""

nome = input('Digite o seu nome:')
sobrenome = input('Digite o seu sobrenome:')
saida = sobrenome + ',' + nome
print(saida)
