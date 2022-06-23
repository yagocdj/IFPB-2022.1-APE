"""Escreva um programa que, dado um número inteiro representando uma quantidade de
segundos, calcule quantas horas, minutos e segundos estão contidos nesta quantidade.
Ex: 7388 segundos = 2 horas, 3 minutos e 8 segundos.
"""

segundos = int(input('Informe o tempo em segundos:'))

tempoHoras = segundos // 3600
resto = segundos % 3600
tempoMinutos = resto // 60
tempoSegundos = resto % 60

print(f'{segundos} segundos = {tempoHoras} horas, {tempoMinutos} minutos e {tempoSegundos} segundos.')
