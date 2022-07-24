# Questão 2.5

melon_counter = 0
current_position = 0

# Tirando as fotos e tomando as decisões
while True:
    photo = input()
    win_condition = 'O' * len(photo)
    # Caso alcancemos a condição de vitória
    if photo in win_condition:
        print(f'Vitória com {melon_counter} melões!')
        break
    # Caso estejamos no esconderijo 0
    if current_position == 0:
        if photo[0] == 'X':
            print('Silêncio...')
        if photo[0] == 'O' and photo[1] == 'X':
            print('Tiro de Melão!!!')
            melon_counter += 1
        if photo[0] == 'O' and photo[1] == 'O':
            current_position += 1
            print(f'Correndo pro esconderijo {current_position}!')
    # Caso estejamos no esconderijo de maior posição
    elif current_position == len(photo) - 1:
        if photo[current_position] == 'X':
            print('Silêncio...')
        if photo[current_position] == 'O' and photo[current_position-1] == 'X':
            print('Tiro de Melão!!!')
            melon_counter += 1
        if photo[current_position] == 'O' and photo[current_position-1] == 'O':
            current_position -= 1
            print(f'Correndo pro esconderijo {current_position}!')
    # Caso estejamos em qualquer outro esconderijo
    else:
        # print(current_postion)
        if photo[current_position] == 'X':
            print('Silêncio...')
        if photo[current_position] == 'O':
            if (
                (photo[current_position + 1] == 'X') and
                (photo[current_position - 1] == 'X')
            ):
                print('Tiro de Melão!!!')
                melon_counter += 1
            elif (
                (photo[current_position + 1] == 'O') and
                (photo[current_position - 1] == 'O')
            ):
                print('Tiro de Melão!!!')
                melon_counter += 1
            elif (
                (photo[current_position + 1] == 'O') and
                (photo[current_position - 1] == 'X')
            ):
                current_position += 1
                print(f'Correndo pro esconderijo {current_position}!')
            else:
                current_position -= 1
                print(f'Correndo pro esconderijo {current_position}!')
