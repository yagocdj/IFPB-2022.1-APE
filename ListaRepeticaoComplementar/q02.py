"""
2. Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele
próprio. Faça um programa que mostre todos os números primos de 1 a N
(obs: N será lido).
"""

# números primos de 1 até n
n = int(input('Digite um número: '))
primos = []

print(f'Números primos de 1 até {n}:')
# percorrendo cada número de 1 até n
for numero in range(1, n + 1):
    contador = 0
    # testando se o número "numero" é primo
    for divisor in range(numero, 0, -1):
        if numero % divisor == 0:
            contador += 1
    if contador == 2:  # número só divisivel por dois valores: 1 e ele mesmo
        primos.append(numero)

print(f'\n{primos}')
