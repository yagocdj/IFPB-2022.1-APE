"""
5. Escreva um programa que receba um vetor V de N números inteiros (N será lido),
determine e exiba o maior e o menor elemento deste vetor e seus respectivos
índices.
Obs: suponha a inexistência de valores repetidos.
"""

n = int(input('Informe a quantidade de elementos do vetor: '))
v = [None] * n
maior_valor = int()
menor_valor = int()
indice_maior = 0
indice_menor = 0

print(f'Informe um número inteiro para cada posição do vetor.')

for i in range(n):
    v[i] = int(input())
    if i == 0:
        maior_valor = v[i]
        menor_valor = v[i]

for i in range(1, n):
    if maior_valor < v[i]:
        maior_valor = v[i]
        indice_maior = i
    if menor_valor > v[i]:
        menor_valor = v[i]
        indice_menor = i

print()
print(f'Maior valor: {maior_valor}; índice: {indice_maior}.')
print(f'Menor valor: {menor_valor}; índide: {indice_menor}.')
