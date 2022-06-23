"""
3. O algoritmo de Euclides para determinar o MDC entre dois números inteiros
consiste em formar uma sequência de inteiros cujos dois primeiros
elementos são os números dados. Cada elemento seguinte é o resto da
divisão dos dois anteriores. A sequência terminará quando um elemento dela
for nulo. O MDC entre os números dados é o elemento anterior ao zero. Faça
uma implementação deste programa.
Ex: Dados os números 12 e 15, será formada a sequência: 12, 15, 12, 3, 0 e o
MDC entre 12 e 15 é 3.
"""

print('Digite dois números para que seja calculado o MDC entre eles.')

numero1 = int(input('Número 1: '))
numero2 = int(input('Número 2: '))

resto_divisao = numero1 % numero2

flag = 0

while resto_divisao != flag:
    print(f'Valor atual do resto da divisão: {resto_divisao}.')
    numero1 = numero2
    numero2 = resto_divisao
    resto_divisao = numero1 % numero2
    if resto_divisao == flag:
        print(f'Valor atual do resto da divisão: {resto_divisao}.')
