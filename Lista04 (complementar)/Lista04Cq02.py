"""
2. Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele
próprio. Faça um programa que mostre todos os números primos de 1 a N
(obs: N será lido).
"""

numero = int(input('Digite um número inteiro: '))
print(f'Números primos de 1 até {numero}:')

for i in range(1, numero + 1):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
    if primo:
        print(i, end=' ')
