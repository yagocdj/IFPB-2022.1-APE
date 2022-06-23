# Expressão lógica

print(1 > 2)
print(2 >= 1)
print(1 != 2)
print('abacate' == 'abacaxi')
print('a' == 'a')
print('a' == 'A')
print('a' > 'b')
print('a' < 'b')
print('joao' > 'joaquim')
print('1' < '2')
print('110' < '12')
print()

# Operadores lógicos

print(5 > 8 and 10 != 20)
print(5 > 8 or 10 != 20)
print(not 2 == 2)

a = 5
b = 4
c = 3

print(a > b and a > c)
print()
# Decisão simples

nota = float(input('Digite a sua nota: '))

if nota >= 7:
    print('Aprovado.')
    print('Boas férias')
print()

# Decisão composta

if nota >= 7:
    print('Aprovado.')
    print('Boas férias')
else:
    print('Reprovado.')
    print('Estude mais.')
print()

# Decisão aninhada

nota = float(input('Digite a sua nota novamente: '))

if nota >= 7:
    print('Aprovado')
else:
    if nota >= 4:
        print('Prova final.')
    else:
        print('Reprovado.')
print()

# elif: else + if

if nota >= 7:
    print('Aprovado')
elif nota >= 4:
    print('Prova final.')
else:
    print('Reprovado')
