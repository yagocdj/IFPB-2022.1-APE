# 1. Escreva um programa que solicite a digitação de um número (de 1 a 7) correspondente a um dia
# da semana e imprima o nome do dia da semana e se é dia útil (de segunda a sexta) ou final de
# semana (sábado e domingo). Considere que o dia 1 é o domingo.

print('Digite abaixo um número de 1 a 7 correspondente a um dia da semana.')
numeroDia = int(input('Dia da semana: '))
dia = str()
tipoDia = str()

if (1 < numeroDia) and (numeroDia < 7):
    tipoDia = 'útil'
    if numeroDia == 2:
        dia = 'segunda-feira'
    elif numeroDia == 3:
        dia = 'terça-feira'
    elif numeroDia == 4:
        dia = 'quarta-feira'
    elif numeroDia == 5:
        dia = 'quinta-feira'
    else:
        dia = 'sexta-feira'
if (numeroDia == 1) or (numeroDia == 7):
    tipoDia = 'final de semana'
    if numeroDia == 1:
        dia = 'domingo'
    else:
        dia = 'sábado'

# Considera-se que o usuário digitará um número de 1 a 7.

print(f'Dia da semana: {dia}.\nTipo do dia: {tipoDia}.')
