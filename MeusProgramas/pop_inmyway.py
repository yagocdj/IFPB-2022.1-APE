# Fazendo a questão 2.3 do G4M3 utilizando funções

# Função que gera uma lista sem repetição de elementos


def list_norepeat(list):

    norepeat_list = []
    for element in list:
        if element not in norepeat_list:
            norepeat_list.append(element)
    return norepeat_list


# MAIN
n = int(input())  # Número de nomes a serem lidos
names = [input().upper() for i in range(n)]

# Exibindo a lista "names" sem repetição
norepeat_names = list_norepeat(names)

for name in norepeat_names:
    print(name)
