# Questão 2.4

lines_number = 4
# armazenar os 4 versos do poema
poems_list = [input() for index in range(lines_number)]

# soma que representa a beleza do poema
counter = 0

# comparar os versos dois a dois
for i in range(lines_number // 2):

    verse_last_word = poems_list[i].split()[-1]
    rime_last_word = poems_list[i+2].split()[-1]

    verse_last_letters = verse_last_word[-3:]
    rime_last_letters = rime_last_word[-3:]

    for j in range(len(verse_last_letters)):
        if verse_last_letters[j] == rime_last_letters[j]:
            counter += 1

print(counter)
