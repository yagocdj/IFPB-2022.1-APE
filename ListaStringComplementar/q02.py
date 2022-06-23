"""
2. Faça um programa que leia uma frase e a exiba criptografada. O método de
criptografia será baseado na seguinte regra: trocar alguns caracteres por
outros,
conforme a tabela abaixo:

CARACTER ORIGINAL CARACTER CRIPTOGRAFADO

A branco
E U
I O
O I
U E
branco A
Exemplo: "BOA NOITE" criptografado fica "BI ANIOTU"
"""

frase = input('Digite uma frase:\n').upper()
frase_criptografada = ''

# Substituindo os valores de acordo com a tabela
for i in range(len(frase)):
    if frase[i] == 'A':
        frase_criptografada += ' '
    elif frase[i] == 'E':
        frase_criptografada += 'U'
    elif frase[i] == 'I':
        frase_criptografada += 'O'
    elif frase[i] == 'O':
        frase_criptografada += 'I'
    elif frase[i] == 'U':
        frase_criptografada += 'E'
    elif frase[i] == ' ':
        frase_criptografada += 'A'
    else:
        frase_criptografada += frase[i]

print('\nFrase criptografada:')
print(frase_criptografada)
