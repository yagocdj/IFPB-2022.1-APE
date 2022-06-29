# Questão "Criptografia"

N = int(input())  # quantidade de strings a serem criptografadas

# Lista contendo as strings a serem criptografadas

words_list = [input() for i in range(N)]
encrypted_words_list = []

# Passada 1 - deslocar os caracteres

transform_to_unicode = int()
transform_to_character = str()
shift_position = int()

for word in words_list:
    encrypted_word = str()

    for character in word:
        if (character >= 'a' and character <= 'z') or \
                (character >= 'A' and character <= 'Z'):
            transform_to_unicode = ord(character)
            shift_position = transform_to_unicode + 3
            transform_to_character = chr(shift_position)
            encrypted_word += transform_to_character
    encrypted_words_list.append(encrypted_word)

print(encrypted_words_list)

# Passada 2 - inverter as palavras

for i in range(len(encrypted_words_list)):
    encrypted_words_list[i] = encrypted_words_list[i][::-1]

print(encrypted_words_list)

# Passada 3 - caracteres da metade para frente serão deslocados uma posição
# para a esquerda
# de acordo com a tabela ASCII

for word in encrypted_words_list:
    shift_index = len(word) // 2

    # TERMINAR ESTE PROGRAMA
