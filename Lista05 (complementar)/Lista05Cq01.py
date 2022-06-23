"""
1. Escreva um programa que leia um vetor contendo N elementos inteiros (N será
lido), calcule e exiba:
• A quantidade de elementos pares;
• A quantidade de elementos ímpares;
• A soma de todos os elementos;
• A média dos elementos do vetor.
"""

n = int(input('Informe a quantidade de elementos do vetor: '))
vetor = [None] * n
contador_par = 0
contador_impar = 0
soma = 0

print(f'A seguir, digite {n} inteiros para compor o vetor.')

for i in range(n):
    vetor[i] = int(input())

print(vetor)

for j in vetor:
    if j % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1
    soma += j

media = soma / (contador_par + contador_impar)

print()
print(f'Quantidade de elementos pares: {contador_par}.')
print(f'Quantidade de elementos impares: {contador_impar}.')
print(f'Soma de todos os elementos: {soma}.')
print(f'Média dos elementos do vetor: {media}.')
