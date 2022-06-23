n = int(input())
# Seu programa deve imprimir todas as triplas pitagóricas
# que não possuam nenhum número maior que "n"
lista = []
counter = 0
for c in range(1, n + 1):
    for b in range(1, c + 1):
        for a in range(1, b + 1):
            if (a**2 + b**2 == c**2):
                lista.append((a, b, c))
                counter += 1
lista.sort()
for i in lista:
    print(i[0], i[1], i[2])
if counter == 0:
    print('nenhuma tripla')
