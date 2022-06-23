# Biblioteca de funções da questão 3

# Função para ler n inteiros e armazená-los em um vetor

def int_ler_vetor(quantidade_elementos):
    vetor = []
    for i in range(quantidade_elementos):
        vetor.append(int(input()))
    return vetor

# Função para retornar a média dos elementos de um vetor


def media_vetor(vetor):
    media_aritmetica = sum(vetor) / len(vetor)
    return media_aritmetica


"""
Função para receber um vetor e um número e retornar quantos
quantos elementos desse vetor estão abaixo daquele número
"""


def comparar_vetor(vetor, numero):
    contador = 0
    for elemento in vetor:
        if elemento < numero:
            contador += 1
    return contador
