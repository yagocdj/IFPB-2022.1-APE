# Questão 3 da prova 3 de APE

def criptografar(string):
    nova_string = ''
    for caracter in string:
        if caracter == 'A' or caracter == 'a':
            nova_string += '@'
        elif caracter == 'E' or caracter == 'e':
            nova_string += '3'
        elif caracter == 'I' or caracter == 'i':
            nova_string += '!'
        else:
            nova_string += caracter
    return nova_string


# MAIN
frase = input('Digite uma frase:\n')
frase_criptografada = criptografar(frase)
print(f'Frase criptografada: {frase_criptografada}')
