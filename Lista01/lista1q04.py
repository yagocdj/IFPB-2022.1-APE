"""Escreva um programa para calcular a área de um triângulo, dados os valores de
base e altura.
"""

base = float(input('Digite um valor para a base:'))
alt = float(input('Digite um valor para a altura:'))
s = (base * alt) / 2
print(f'Para um triângulo de base {base} e altura {alt}, a área é igual a {s:.1f}')
