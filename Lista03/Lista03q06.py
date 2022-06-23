"""
6. Faça um programa que leia 3 números inteiros (N, X, Y) e mostre todos os
números múltiplos de N entre X e Y.
"""

n = int(input('Número inteiro n: '))
x = int(input('Número inteiro x: '))
y = int(input('Número inteiro y: '))

print(f'Múltiplos de {n} entre {x} e {y}:')

for i in range(x, y + 1):
    if i % n == 0:
        print(i)

"""
exemplo: n = 5, x = 10, y = 20:

Casos em que o resto da divisão de i por 5 (i % 5) resulta em 0:
10, 15 e 20.

Portanto, o programa só vai exibir esses valores apresentados anteriormente.
"""