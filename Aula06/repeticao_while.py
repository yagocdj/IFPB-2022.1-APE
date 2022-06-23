"""
Faça um programa que solicite do usuário vários números até que seja informado
o
número 0. Sempre que o usuário informar um número o programa deverá mostrar o
dobro desse número
"""
dobro = int()
msg = 'Informe o número: '

n = int(input(msg))

while n != 0:
    dobro = n * 2
    print(f'O dobro de {n} é {dobro}.')
    n = int(input(msg))
print('Fim do programa')

# Exibir 10 vezes o nome "IFPB"

contador = 1

while contador <= 10:
    print(contador, 'IFPB')
    contador = contador + 1

# Exibir os números de 1 a 50

contador = 1

while contador <= 50:
    print(contador, end=' ')
    contador += 1

# Solicitar N números do usuário, verificar e exibir se o número lido é par ou
# ímpar

n = int(input('Quantos números? '))

contador = 0

while contador < n:
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        print('Par')
    else:
        print('Impar')
    contador += 1
print('Fim do programa')

# Solicitar N números do usuário (até que o usuário digite o número zero ou a
# soma dos
# números lidos seja maior do que 100) e ao final da leitura mostrar a soma de
# todos os
# números lidos

n = int(input('Informe a quantidade de números: '))
flag = 0
soma = 0
numero = int(input('Digite um número: '))

while numero != flag and soma <= 100:
    soma += numero
    print(f'Soma = {soma}')
    if soma <= 100:
        numero = int(input('Digite um número: '))
print('Fim do programa')
