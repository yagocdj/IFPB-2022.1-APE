"""
4. Escreva uma função chamada soma que receba um vetor e retorne a soma dos
seus elementos (obs: não use a função sum).
Escreva também um programa que, dado o vetor V = [ 6,3,8,7,2,5 ] e usando a
função soma criada, informe a soma dos elementos do vetor V.
"""


def soma(vetor):
    soma_vetor = 0
    for i in range(len(vetor)):
        soma_vetor += vetor[i]
    return soma_vetor


# lendo a quantidade de números do vetor
quantidade = int(input('Digite a quantidade de números: '))
# lendo os números do vetor
lista = [int(input()) for i in range(quantidade)]
resultado = soma(lista)
print(f'A soma dos valores é: {resultado}')
