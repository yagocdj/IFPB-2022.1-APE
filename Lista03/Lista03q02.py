"""
2. Faça um programa que leia um número N, inteiro, e some todos os números
de 1 até N, mostrando o resultado.
"""

n = int(input('Digite um número inteiro: '))
soma = 0

for i in range(1, n + 1):  # de 1 até n, já que n + 1 não é incluído
    soma = soma + i
    if i < n:
        print(f'{i} + ', end='')
    else:
        print(f'{i} = ', end='')

print(soma)
