# Questão 3.2

# quantidade de casas do tabuleiro (sempre ímpar)
n = int(input())
coins_number = list(map(int, (input().split())))
# buraco
middle_place = n // 2

# quantidade mínima de turnos
minimum_shift = middle_place * 2

print(minimum_shift)
