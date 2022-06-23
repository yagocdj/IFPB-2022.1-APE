"""
4. Faça um programa que leia 20 números inteiros, determine e mostre o maior
deles.
"""

n = 20
maior_numero = int()

print(f'Digite {n} números inteiros:')

for i in range(n):
    numero = int(input(''))
    if i == 0:
        maior_numero = numero
    else:
        if numero > maior_numero:
            maior_numero = numero

print('\n o maior número é:', maior_numero)
