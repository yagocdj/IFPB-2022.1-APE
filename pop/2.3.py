# Questão 2.3

n = int(input())  # representa o número de nomes a serem lidos
names = [input().upper() for i in range(n)]
names_norepeat = []

# adicionando os nomes a uma nova lista sem nomes repetidos
for i in range(n):
    if names[i] not in names_norepeat:
        names_norepeat.append(names[i])

# exibindo a nova lista sem nomes repetidos
for name in names_norepeat:
    print(name)
