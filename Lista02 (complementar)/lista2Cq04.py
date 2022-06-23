# 4. Escreva um programa que leia a hora de início de um jogo e a hora do final do jogo (considerando
# apenas horas inteiras), calcula a duração do jogo em horas, sabendo-se que o tempo máximo de
# duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.
# O programa deve mostrar o resultado obtido.

horaInicio = int(input('Digite a hora de início do jogo (nº inteiro): '))
horaFinal = int(input('Digite a hora do final do jogo (nº inteiro): '))
duracao = int()

if horaInicio < horaFinal:
    duracao = horaFinal - horaInicio
else:
    duracao = 24 - horaInicio + horaFinal  # a mesma coisa de "24 - (horaInicio - horaFinal)

print(f'Duração do jogo: {duracao}h.')
