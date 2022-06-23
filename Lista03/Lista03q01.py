"""
1. Faça um programa que calcule e mostre os números múltiplos de 5 do
intervalo 50 a 300, juntamente com suas raízes e seus cubos.
"""

import math

multiplo = int()
raiz = float()
cubo = int()

nome1 = 'i'
nome2 = 'raiz(i)'  # Cabeçalho
nome3 = 'cubo(i)'

tamanho1 = 5
tamanho2 = 10  # Cabeçalho e organização
tamanho3 = 10

print(f'{nome1:>{tamanho1}}{nome2:>{tamanho2}}{nome3:>{tamanho3}}')

for i in range(50, 301):
    if i % 5 == 0:
        multiplo = i
        raiz = math.sqrt(i)
        cubo = i ** 3
        print(f'{multiplo:{tamanho1}}{raiz:{tamanho2}.1f}{cubo:{tamanho3}}.')
