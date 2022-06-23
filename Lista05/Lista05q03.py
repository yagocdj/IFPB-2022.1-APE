"""
3. Escreva um programa que leia um vetor V contendo N elementos inteiros (N será
lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver,
informe em que posição (índice).
Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K
aparece.
"""

n = int(input('Informe a quantidade de elementos do vetor: '))
v = [None] * n
k = int(input('Informe um valor inteiro: '))

print(f'Informe {n} elementos inteiros para o vetor v.')

for i in range(n):
    v[i] = int(input())
print()
print(f'O número {k} aparece no(s) seguinte(s) índice(s):')
for i in range(n):
    if v[i] == k:
        print(f'Índice {i}.')
print('Fim do programa.')
