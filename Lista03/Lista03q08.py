"""
8. Faça um programa que leia um número inteiro N, calcule e mostre o maior
quadrado perfeito menor ou igual a N. Por exemplo, se N for igual a 38, o
resultado é 36.
"""

n = int(input('Digite um número inteiro: '))
maior_quadrado = int()

for i in range(n + 1):
    if i ** 2 < n:
        quadrado_perfeito = i ** 2
        if quadrado_perfeito > maior_quadrado:
            maior_quadrado = quadrado_perfeito
print()
print(f'Maior quadrado perfeito menor ou igual a {n}: {maior_quadrado}.')
