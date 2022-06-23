"""
Hex to dec converter.
"""

while True:
    base = int(input('Informe em qual base está o número: '))
    valor_base = input(
        'Digite um número na base escolhida'
        + '("FIM" para parar o programa): ').upper()
    if valor_base == 'FIM':
        print('Fim do programa.')
        break
    valor_decimal = int(valor_base, base)
    print(f'{valor_base} é igual a {valor_decimal} em decimal.')
