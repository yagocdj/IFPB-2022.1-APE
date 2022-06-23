"""
4. Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
• Os números que estão nos índices pares;
• Os números que estão nos índices ímpares.
"""

quantidade_numero = 10
vetor = [None] * quantidade_numero

print(f'Informe {quantidade_numero} inteiros a seguir.')

for i in range(quantidade_numero):
    vetor[i] = int(input())

for i in range(quantidade_numero):
    if i % 2 == 0:
        print(f'Número em índice par: {vetor[i]}.')
    else:
        print(f'Número em índice ímpar: {vetor[i]}.')
