"""
4. Faça um programa que leia uma string S e um valor inteiro N, e exiba na
tela a
string S com as suas vogais repetidas N vezes.
Exemplo:
Entrada: S: Hoje tem aula de Python

N: 3

Saída: Hooojeee teeem aaauuulaaa deee Pythooon
"""

string = input('Digite uma string: ').lower()
n = int(input('Digite um inteiro qualquer: '))
formated_s = ''
# Achar e multiplicar as vogais por n
formated_s = string.replace('a', 'a' * n).replace(
    'e', 'e' * n).replace(
    'i', 'i' * n).replace(
    'o', 'o' * n).replace(
    'u', 'u' * n)

print(f'\nSaída:\n{formated_s}')

# Outra maneira
string = input('Digite uma string: ')
n = int(input('Digite um inteiro qualquer: '))
formated_s = ''

for character in string:
    character_lower = character.lower()
    if character_lower == 'a' or character_lower == 'e' \
            or character_lower == 'i' or character_lower == 'o' \
            or character_lower == 'u':
        formated_s += character * n
    else:
        formated_s += character

print(f'\nSaída:\n{formated_s}')

# Versão usando find
string = input('Digite uma string: ')
n = int(input('Digite um inteiro qualquer: '))

vogais = 'AaEeIiOoUu'
formated_s = ''

for character in string:
    if vogais.find(character) >= 0:  # Se eu achar uma vogal na string,
        formated_s += character * n  # adicione essa mesma vogal multiplicada
        # por n
    else:
        formated_s += character

print(f'\nSaída:\n{formated_s}')
