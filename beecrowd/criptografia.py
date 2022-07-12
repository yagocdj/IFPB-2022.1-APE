# Questão "Criptografia"

def first_position_shift(word):
    # Passada 1 - deslocar os caracteres que sejam letras minúsculas/maiúsculas
    transform_to_unicode = int()
    transform_to_character = str()
    shift_position = int()
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

    return encrypted_word


def reverse_string(word):
    # Passada 2 - inverter a palavra
    word = word[::-1]
    return word


def second_position_shift(word):
    # Passada 3 - caracteres da metade para frente serão deslocados uma posição
    # para a esquerda
    # de acordo com a tabela ASCII
    encrypted_word = str()

    # Percorrendo os caracteres da palavra
    for index in range(len(word)):

        # Deslocar a posição do carácter 1 unidade para esquerda
        # caso o carácter esteja na metade pra frente
        if index >= len(word) // 2:

            # Transformando o carácter em código unicode
            transform_to_unicode = ord(word[index])

            # Deslocando o carácter uma unidade para esquerda (ASCII)
            shift_position = transform_to_unicode - 1

            # Transformando o código unicode no seu respectivo carácter
            transform_to_character = chr(shift_position)
            encrypted_word += transform_to_character

        # Apenas adicionar o carácter como está
        else:
            encrypted_word += word[index]

    return encrypted_word


# MAIN
N = int(input())  # quantidade de strings a serem criptografadas

for index in range(N):

    # Ler a palavra a ser criptografada
    word = input()

    # Criptografar a palavra aplicando as funções anteriormente definidas
    encrypted_word = second_position_shift(
        reverse_string(first_position_shift(word)))

    # Exibir a palavra criptografada
    print(encrypted_word)
