"""
3. Escreva um programa para ler 6 números. Após a leitura dos números,
verifique,
para cada um deles, se é distinto, ou seja, não possui repetição.
"""

quantidade = 6
numeros = [None] * quantidade

print(f'Digite {quantidade} inteiros a seguir.')

numeros[0] = int(input())

# Ler o vetor "numeros" e verificando se cada número se repete

for i in range(1, quantidade):
    numeros[i] = int(input())
    for j in range(0, i):
        if numeros[i] == numeros[j]:
            numero_repetido = numeros[i]
            print(f'O número {numero_repetido} se repete.')

""" 
contador = 0
repete = bool()

for i in range(quantidade):
    for j in range(quantidade):
        if j != i:
            if numeros[i] == numeros[j]:
                contador += 1
                repete = True
    if contador >= 2:
        print(f'O número {numeros[i]} repete-se {contador} vezes.')
        contador -= contador
    else:
        print(f'O número {numeros[i]} não se repete.')
 """
