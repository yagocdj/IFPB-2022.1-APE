"""
3. Escreva um programa que leia N números inteiros (máximo 20) e armazene em
um vetor X. Calcule a média dos elementos do vetor e informe quantos elementos
estão abaixo da média do conjunto.
Crie as seguintes funções:
• Uma função que faça a leitura dos elementos de um vetor.
• Uma função que retorne a média dos elementos de um vetor.
• Uma função que receba um vetor e um número, e retorne quantos elementos
do vetor estão abaixo desse número.
"""

import q03_functions

# MAIN

# "n" é a quantidade de inteiros
n = int(input('Digite a quantidade de inteiros a serem lidos: '))

# Preenchendo um vetor com n inteiros
print(f'\nAgora, preencha um vetor com {n} inteiros:')
vetor = q03_functions.int_ler_vetor(n)

# Calculando a média dos elementos do vetor
media_vetor = q03_functions.media_vetor(vetor)

# Vendo quais o elementos do vetor que estão abaixo da média
elementos_abaixo_media = q03_functions.comparar_vetor(vetor, media_vetor)

print(f'\nMédia aritmética dos elementos do vetor: {media_vetor:.2f}')
print('Qunatidade de elementos do vetor que estão abaixo dessa média:',
      elementos_abaixo_media)
