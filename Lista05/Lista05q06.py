"""
6. Escreva um programa que leia um vetor de N números inteiros (N será lido),
inverta a ordem dos elementos do vetor e exiba o vetor invertido.
Ex: V = [1, 3, 5, 7], após a inversão: V = [7, 5, 3, 1].
"""

n = int(input('Informe a quantidade de elementos do vetor: '))
vetor = [None] * n

print(f'A seguir, informe {n} números inteiros.')

for i in range(n):
    vetor[i] = int(input())
print(vetor)
print()

indice_primeira_metade = 0
auxiliar = 0

for i in range(n-1, (n // 2), -1):
    auxiliar = vetor[indice_primeira_metade]
    vetor[indice_primeira_metade] = vetor[i]
    vetor[i] = auxiliar
    indice_primeira_metade += 1
print(vetor)
