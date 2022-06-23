"""
1. Faça um programa que leia um número N, calcule e mostre os N primeiros
termos da sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13, ...). O valor lido
para
N sempre será maior ou igual a 2.
"""

# n primeiros termos da sequência de Fibonacci
n = int(input('Digite um número maior ou igual a 2: '))

termo_anterior = 0
termo_atual = 1
proximo_termo = int()

if n >= 2:
    # Calculando os n primeiros termos da sequência
    print(f'Exibindo os {n} primeiros termos da sequência de Fibonacci:\n')

    for i in range(n):
        if i == 0:
            print(termo_anterior, end=',')
            print(termo_atual, end=',')
        proximo_termo = termo_atual + termo_anterior
        if i == n - 1:
            print(proximo_termo, end='')
        else:
            print(proximo_termo, end=',')
        termo_anterior = termo_atual
        termo_atual = proximo_termo

print('\nFim do programa.')
