# Questão 2.3

n = int(input())  # representa o número de nomes a serem lidos
names = [input().upper() for i in range(n)]

for name in names:
    name_counter = names.count(name)
