# 2. Escreva um programa que solicite a digitação de um caractere qualquer do teclado e imprima
# sua classificação: vogal, consoante, número e caractere especial.

caractere = input('Digite um caractere qualquer do teclado: ').lower()
classificacao = str()

if ('a' <= caractere) and (caractere <= 'z'):
    if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u':
        classificacao = 'vogal'
    else:
        classificacao = 'consoante'
elif ('0' <= caractere) and (caractere <= '9'):  # o "elif" pode ser separado em "else" com "if...else" identado nele
    classificacao = 'número'
else:
    classificacao = 'caractere especial'

print(f'Classificação: {classificacao}.')
