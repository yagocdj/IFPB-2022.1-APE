"""Escreva um programa para calcular e exibir a média ponderada de 2 notas dadas. Sabe-
se que nota1 possui peso 6 e nota2 possui peso 4.
"""
peso1 = 6
peso2 = 4

nota1 = float(input('Digite a nota 1:'))
nota2 = float(input('Digite a nota 2:'))

mediaPonderada = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

print(f'A média ponderada das suas notas é igual a {mediaPonderada:.1f}.')
