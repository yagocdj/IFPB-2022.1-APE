"""
3. Faça um programa que leia vários números, determine e mostre o maior e o
menor deles.
Obs: a leitura do número 0 (zero) encerra o programa.
"""

numero = float(input('Digite um número: '))
flag = 0

maior_numero = numero
menor_numero = numero

while numero != flag:
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero
    numero = float(input('Digite um número: '))
print()
print(f'Maior número: {maior_numero}; menor número: {menor_numero}.')
