# 3. Escreva um programa que solicite a digitação de um ano e imprima sua classificação como
# bissexto ou não bissexto.
# Obs: um ano é bissexto se for divisível por 4, mas não por 100. Um ano também é bissexto se
# for divisível por 400.

ano = int(input('Digite o ano: '))
classificacao = str()

if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):  # "(ano % 100 != 0)" é equivalente a "(not ano % 100 == 0)"
    classificacao = 'bissexto'
else:
    classificacao = 'não bissexto'

print(f'Classificação: {classificacao}.')
