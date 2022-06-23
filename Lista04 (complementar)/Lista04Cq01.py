"""
1. Faça um programa que leia um número N, calcule e mostre os N primeiros
termos da sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13, ...). O valor lido
para
N sempre será maior ou igual a 2.
"""

numero_repeticao = int(input('Digite um número inteiro maior ou igual a 2: '))
antecessor = 0
atual = 1

print(f'Os {numero_repeticao} primeiros termos da sequência de Fibonacci.')

for i in range(2, numero_repeticao + 1):
    sucessor = atual + antecessor
    antecessor = atual
    atual = sucessor
    if i == numero_repeticao:
        print(sucessor, end='.')
    else:
        print(sucessor, end=',')
