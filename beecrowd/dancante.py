# ID 1234

import sys

for string in sys.stdin:

    # variável que armazenará a sentença dançante
    dancing_string = ''

    # variável contador
    counter = 1

    # percorrendo cada letra da string
    for character in string:
        # se o carácter for diferente de blank space (' ')
        if character != ' ':
            # se o valor armazenado no contador for ímpar
            if counter % 2 != 0:
                dancing_string += character.upper()
            # se o valor armazenado no contador for par
            else:
                dancing_string += character.lower()
            # incrementar o contador caso a letra atual não seja ' '
            counter += 1
        # se for ' ', apenas adicione o carácter à string dançante
        else:
            dancing_string += character
    print(dancing_string, end='')
