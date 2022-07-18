# ID 1234

import sys

for string in sys.stdin:

    dancing_string = ''
    counter = 1

    for character in string:
        if character != ' ':
            if counter % 2 != 0:
                dancing_string += character.upper()
            else:
                dancing_string += character.lower()
            counter += 1
        else:
            dancing_string += character
    print(dancing_string, end='')
