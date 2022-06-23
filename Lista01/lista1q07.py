"""O restaurante a quilo Bem-Bão cobra R$25,00 por cada quilo de refeição. Faça um
programa que leia o peso do prato montado pelo cliente (em quilos) e exiba o valor
a pagar. Assuma que a balança já desconte o peso do prato.
"""

precoKg = 25.0
peso = float(input('Informe o peso do seu prato em quilogramas:'))
valor = peso * precoKg
print('O valor a ser pago é: R$', valor)
