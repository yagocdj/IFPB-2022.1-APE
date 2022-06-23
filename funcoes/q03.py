"""
3. Escreva uma função chamada vertical que receba como parâmetro uma string e
a exiba na vertical, ou seja, com uma letra em cada linha. Faça também um
programa para testar a função.
"""


def vertical(string):
    for letra in string:
        print(letra)


palavra = input('Digite uma palavra:\n')
print('\nSaída:')
palavra_vertical = vertical(palavra)
