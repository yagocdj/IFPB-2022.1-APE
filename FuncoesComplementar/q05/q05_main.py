"""
5. Escreva um programa que calcule o valor do cosseno de X através de 20 termos
da série abaixo:

Observações:
• O valor de X será lido.
• Escreva uma função para o cálculo do fatorial e outra para o cálculo da
potência.
• Compare o resultado do seu programa com o resultado da função:
math.cos(numero): retorna o cosseno do número em radiano (da biblioteca
math).
"""

import q05_functions as q05f
import math

# MAIN

x = int(input('Digite um número: '))

# Exibindo o cosseno
math_cosseno = math.cos(x)
meu_cosseno = q05f.cosseno(x)
print(f'\nCosseno da minha função:\n{meu_cosseno}')
print(f'\nCosseno da função math:\n{math_cosseno}')
