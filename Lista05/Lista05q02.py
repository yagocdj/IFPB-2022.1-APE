"""
2. Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor
inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.
"""

n = 5
v = [None] * n
k = int(input('Informe um valor inteiro: '))
contador = 0

print(f'Digite {n} inteiros a seguir.')

for i in range(n):
    v[i] = int(input())

for j in v:
    if j == k:
        print(j)
        contador += 1
print()
print(f'O número {k} aparece {contador} vezes no vetor v.')
