# 1. Escreva um programa que leia um número inteiro e determine se ele é par ou ímpar.

numeroInteiro = int(input('Digite um número inteiro: '))
paridade = numeroInteiro % 2  # Se numeroInteiro possuir resto igual a 0, então ele é par. Caso contrário, ele é ímpar.

if paridade == 0:
    resultado = 'par'
else:
    resultado = 'ímpar'

print(f'{numeroInteiro} é {resultado}.')
