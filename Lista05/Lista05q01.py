"""
1. Escreva um programa que leia um vetor A de N números inteiros (N será lido) e
um outro inteiro K, construa e exiba um outro vetor B cujos elementos são os
respectivos elementos de a multiplicados por K.
Ex: A = [1,2,3], K = 5, B = [5,10,15].
"""

n = int(input('Informe a quantidade de números do vetor: '))
a = [None] * n
k = int(input('Informe o valor que multiplicará os elementos do vetor: '))
b = [None] * n

for i in range(n):
    a[i] = int(input('Digite um número inteiro: '))
    b[i] = a[i] * k
print()
print(f'Vetor a: {a}')
print(f'Vetor b (resultante da multiplicação de a por k): {b}')
