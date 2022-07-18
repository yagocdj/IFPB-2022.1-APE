# ID 2728

import sys

cobol_letters = 'cobol'

for line in sys.stdin:
    string_list = line.lower().split('-')
    sum_value = 0
    for i in range(len(string_list)):
        if i < (len(string_list) - 1):
            if (
                string_list[i][0] == cobol_letters[i]
                or string_list[i][-1] == cobol_letters[i]
            ):
                sum_value += 1
        else:
            if (
                string_list[i][0] == cobol_letters[i]
                or string_list[i][-2] == cobol_letters[i]
            ):
                sum_value += 1

    if sum_value >= 5:
        print('GRACE HOPPER')
    else:
        print('BUG')
