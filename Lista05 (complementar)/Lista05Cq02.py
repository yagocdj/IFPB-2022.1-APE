"""
2. Dados dois vetores A e B contendo N elementos inteiros cada (N, A e B serão
lidos), gerar e exibir um vetor C (de tamanho N*2) cujos elementos sejam a
intercalação dos elementos de A e B.
Ex: N = 3, A = [18, 12, 20], B = [15, 10, 7], C = [18, 15, 12, 10, 20, 7]
"""

n = int(input('Digite a quantidade de elementos dos vetores: '))
a = [None] * n
b = [None] * n
c = [None] * (n * 2)

print(f'Digite {n} inteiros para o vetor a.')

# Ler o vetor a

for i in range(n):
    a[i] = int(input())

print(f'Digite {n} inteiros para o vetor a.')

# Ler o vetor b

for i in range(n):
    b[i] = int(input())

# Intercalar os vetores a e b no vetor c

for i in range(n * 2):
    if i % 2 == 0:
        c[i] = a[i // 2]
    else:
        c[i] = b[i // 2]

print(f'Vetor a: {a}')
print(f'Vetor b: {b}')
print(f'Vetor intercalado de a e b (c): {c}')
