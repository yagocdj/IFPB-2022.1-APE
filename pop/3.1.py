# Questão 3.1

# Quantidade de pessoas que querem ajuda com algum problema
n = int(input())
# Lista com os níveis de prioridade
priority_lvl = [int(input()) for i in range(n)]
priority_lvl.sort()

# Exibindo as prioridades em ordem crescente
for value in priority_lvl:
    print(value)
