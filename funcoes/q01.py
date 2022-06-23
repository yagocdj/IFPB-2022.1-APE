"""
1. Escreva uma função chamada menor que receba 3 números e retorne o menor
deles. Faça também um programa para testar a função.
"""


def menor(numero1, numero2, numero3):
    if numero1 <= numero2 and numero1 <= numero3:
        return numero1
    elif numero2 <= numero3:
        return numero2
    else:
        return numero3


valores = []
for i in range(3):
    valores.append(int(input('Digite um inteiro: ')))
numero_menor = menor(valores[0], valores[1], valores[2])
print('Menor valor: ', numero_menor)
