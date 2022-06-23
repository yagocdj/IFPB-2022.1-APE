# for <variável> in <coleção>

# o i itera em cima do range(). Ele receberá os valores do range()

# o i é como um contador

for i in range(0, 10):  # intervalo aberto no 10
    print(i, 'IFPB')

print()  # Só para separar
for i in range(0, 10, 2):  # o número 2 define que o step será de 2 em 2.
    print(i, end=',')

print()
for i in range(10, 0, -1):  # decrescente
    print(i, end='')

print()
for i in range(5):  # equivale a range(0, 5, 1)
    print(i, end='-')

print()
n = 5
for i in range(n):
    if i < n - 1:
        print(i, end=',')
    else:
        print(i)

# exemplo 1

print()
n = int(input('Digite a quantidade de números: '))
for i in range(n):
    numero = int(input('Digite um número: '))
    dobro = numero * 2
    print(f'o dobro de {numero} é {dobro}.')
print('Fim do programa.')

# exemplo 2

print()
n = int(input('Digite a quantidade de números: '))
soma = 0

for i in range(n):
    numero = int(input('Digite um número: '))
    soma = soma + numero  # variável do tipo somador
print(f'Soma = {soma}')

# exemplo 3

print()
n = 5
contador = 0

for i in range(n):
    nota = int(input('Nota: '))
    if nota >= 70:
        contador = contador + 1  # contador += contador
print(f'{contador} aluno(s) aprovado(s).')

# mais demonstrações

n = int(input('Numero de repetições: '))

for i in range(0, n+1):
    print(i)
