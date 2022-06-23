"""
5. Faça um programa que, leia a temperatura dos 30 dias do mês de abril diga
qual o dia mais quente e o dia mais frio do mês (obs: suponha que não haja
empates).
"""

dias = 3
temp_mais_alta = float()
temp_mais_baixa = float()

for i in range(1, dias + 1):
    temperatura = float(input('Digite a temperatura do dia em graus: '))
    if i == 1:
        temp_mais_alta = temperatura
        temp_mais_baixa = temperatura
    if temperatura > temp_mais_alta:
        temp_mais_alta = temperatura
        dia_mais_quente = i
    if temperatura < temp_mais_baixa:
        temp_mais_baixa = temperatura
        dia_mais_frio = i
print(f'Dia mais quente do mês de abril: {dia_mais_quente}.')
print(f'Dia mais frio do mês de abril: {dia_mais_frio}.')

# CONSERTAR
