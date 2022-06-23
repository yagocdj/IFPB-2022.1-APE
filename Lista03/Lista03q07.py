"""
7. Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele
próprio. Faça um programa que leia um número e determine se ele é ou não
primo.
"""

numero = int(input('Digite um número inteiro: '))
primo = True

for i in range(2, numero):
    if numero % i == 0:
        primo = False

if primo:
    print(numero, 'é primo')
else:
    print(numero, 'não é primo')
