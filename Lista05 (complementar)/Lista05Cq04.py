"""
4. Escreva um programa para ler 6 números distintos, ou seja, não podem
repetir.
Exiba os números lidos.
"""

quantidade = 6
numeros = [0] * quantidade
contador = 0

print(f'Digite {quantidade} inteiros a seguir.')

# Preencher o vetor, verificando se o número digitado é repetido ou não

for i in range(quantidade):
    while True:
        existe_repeticao = False
        numero_atual = int(input())
        for j in range(i):
            if numero_atual == numeros[j]:
                existe_repeticao = True
                break
            else:
                numero_atual
        if existe_repeticao:
            print('Numero repetido! Digite outro.')
            continue
        numeros[i] = numero_atual  # O número só será armazenado na posição i
        contador += 1              # caso não seja repetido
        break

print(f'\nNúmeros lidos: {numeros}')

""" quantidade = 6
numeros = [None] * quantidade
numero_repetido = bool()

# Ler o primeiro número fora do loop para que seja possível comparar o numero
# atual com os outros números do vetor

print(f'Digite {quantidade} números distintos abaixo.')

numeros[0] = int(input())

# Ler os números e verificar se já há algum número igual

for i in range(1, quantidade):
    numeros[i] = int(input())
    for j in range(i):
        if numeros[i] == numeros[j]:
            print('Esse número já foi digitado!')
            numero_repetido = True
    if numero_repetido:
        break

if numero_repetido:
    print('Fim do programa')
else:
    print(numeros)
 """
