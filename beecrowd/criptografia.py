# Questão "Criptografia"

N = int(input())  # quantidade de strings a serem criptografadas

# Lista contendo as strings a serem criptografadas

words_list = [input() for i in range(N)]
encrypted_words_list = []

# Passada 1 - deslocar os caracteres que sejam letras minúsculas e maiúsculas

transform_to_unicode = int()
transform_to_character = str()
shift_position = int()

# Percorrendo cada palavra da lista de palavras
for word in words_list:
    encrypted_word = str()
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Percorrendo cada carácter da palavra
    for character in word:
        if character in letters:
            # Transformando o carácter em código unicode
            transform_to_unicode = ord(character)
            # Deslocando o carácter 3 posições para direita
            shift_position = transform_to_unicode + 3
            # Transformando o código unicode no seu respectivo carácter
            transform_to_character = chr(shift_position)
            # Adicionando o carácter à nova string criptografada
            encrypted_word += transform_to_character
        # Caso o carácter não seja uma letra maiúscula ou minúscula
        else:
            encrypted_word += character
    # Adicionando a string criptografada a uma nova lista
    encrypted_words_list.append(encrypted_word)

# Passada 2 - inverter as palavras
for i in range(len(encrypted_words_list)):
    encrypted_words_list[i] = encrypted_words_list[i][::-1]

# Passada 3 - caracteres da metade para frente serão deslocados uma posição
# para a esquerda
# de acordo com a tabela ASCII

# Percorrendo a lista de palavras criptografadas
for word in encrypted_words_list:
