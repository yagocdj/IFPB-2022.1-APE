"""
2. Escreva uma função chamada primo para determinar se um número é primo ou
não. A função deve receber um número inteiro, retornar True se o número for
primo, ou False caso contrário.
Escreva também um programa que, usando a função primo criada, exiba os
números primos entre 1 e 100.
"""

# Criando a função para verificar se o número é primo


def primo(number):
    valor_primo = True
    for i in range(2, number):
        if number % i == 0:
            valor_primo = False
            break
    return valor_primo


# Programa para exibir os números primos entre 1 e 100
for i in range(1, 101):
    if primo(i):
        print(i)
