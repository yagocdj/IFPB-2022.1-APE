"""
5. Faça um programa que leia uma frase e a exiba na tela conforme o exemplo
abaixo.
Exemplo:
Entrada: ABCDE
Saída: A
BB
CCC
DDDD
EEEEEE
DDDD
CCC
BB
A
"""

frase = input('Digite uma string: ')

# Exibição formatada
for i in range(len(frase)):
    print(frase[i] * (i + 1))

for i in range(-2, -(len(frase)) - 1, -1):
    print(frase[i] * (len(frase) + (i + 1)))
