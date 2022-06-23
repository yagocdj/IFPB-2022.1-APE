# Exemplo 1: ler n idades e determinar a maior e a menor delas

# Utiliza-se maior e/ou menor

n = 3
maior = 0  # menor valor possível
menor = 1000  # maior valor possível

print(f'Digite as {n} idades:')

for i in range(n):
    idade = int(input())
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade

print(f'Maior idade: {maior}')
print(f'Menor idade: {menor}')

# Exemplo 2: ler n números e determinar o maior e o menor deles

n = 5

print(f'Digite os {n} números:')

for i in range(n):
    numero = int(input())

    if i == 0:  # i == 0 -> primeira execução
        maior = numero
        menor = numero

    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')

# Exemplo 3: ler o nome e a idade de n pessoas e determinar a pessoa mais
# velha e a pessoa mais nova
# (obs: suponha a existência de empates)

n = 5
idade_maior = 0  # menor valor possível
idade_menor = 1000  # maior valor possível
nome = str()
nome_maior = str()
nome_menor = str()

print(f'Digite o nome e a idade das {n} pessoas:')

for i in range(n):
    nome = input('Nome: ')
    idade = int(input('Idade: '))

    if idade > idade_maior:
        nome_maior = nome
        idade_maior = idade

    if idade < idade_menor:
        nome_menor = nome
        idade_menor = idade

print(f'Maior idade: {nome_maior} com {idade_maior} anos.')
print(f'Menor idade: {nome_menor} com {idade_menor} anos.')
