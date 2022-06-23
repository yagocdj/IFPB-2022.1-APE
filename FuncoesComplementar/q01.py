"""
1. Escreva uma função chamada vogal que receba uma letra e verifique se a
letra é
uma vogal, retornando o valor True nesse caso, ou o valor False caso contrário.
Escreva também um programa que leia uma frase e, usando a função vogal
criada, imprima a quantidade de vogais existentes na frase lida.
"""

# criando a função vogal


def vogal(letter):
    vogais = 'AaEeIiOoUu'
    if letter in vogais:
        return True
    else:
        return False


# lendo uma string e verificando quantas vogais há nela
string = input('Digite uma frase:\n')
contador_vogal = 0

for letra in string:
    if vogal(letra):
        contador_vogal += 1

print(f'A string digitada possui {contador_vogal} vogais.')
