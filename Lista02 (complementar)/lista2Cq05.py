# 5. Escreva um programa para determinar as raízes de uma equação de segundo grau, dados os
# seus coeficientes. Fórmulas:
#
# Obs: se Δ for negativo, não existem as raízes da equação.
# Dica: use a função sqrt do módulo math.

import math

print('Digite os coeficientes da equação do segundo grau:')
a = float(input('Coeficiente a: '))
b = float(input('Coeficiente b: '))
c = float(input('Coeficiente c: '))

x1 = float()
x2 = float()

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print('Não há raízes (delta < 0).')
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'Raízes: {x1:.2f}, {x2:.2f}.')
