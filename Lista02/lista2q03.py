# 3. Escreva um programa que leia 3 números inteiros, determine e mostre o maior deles.

print('Digite três números inteiros:')
numeroInteiro1 = int(input('-> '))
numeroInteiro2 = int(input('-> '))
numeroInteiro3 = int(input('-> '))

if numeroInteiro1 >= numeroInteiro2 and numeroInteiro1 >= numeroInteiro3:
    maior = numeroInteiro1
    print(f'O maior número é {maior}.')
if numeroInteiro2 >= numeroInteiro1 and numeroInteiro2 >= numeroInteiro3:
    maior = numeroInteiro2
    print(f'O maior número é {maior}.')
if numeroInteiro3 >= numeroInteiro2 and numeroInteiro3 >= numeroInteiro1:
    maior = numeroInteiro3
    print(f'O maior número é {maior}.')

# If...else

print('Digite três números inteiros:')
numeroInteiro1 = int(input('-> '))
numeroInteiro2 = int(input('-> '))
numeroInteiro3 = int(input('-> '))

if (numeroInteiro1 > numeroInteiro2) and (numeroInteiro1 > numeroInteiro3):
    maior = numeroInteiro1
else:
    if numeroInteiro2 > numeroInteiro3:
        maior = numeroInteiro2
    else:
        maior = numeroInteiro3

print(f'O maior número é {maior}.')

# Elif

print('Digite três números inteiros:')
numeroInteiro1 = int(input('-> '))
numeroInteiro2 = int(input('-> '))
numeroInteiro3 = int(input('-> '))

if (numeroInteiro1 > numeroInteiro2) and (numeroInteiro1 > numeroInteiro3):
    maior = numeroInteiro1
elif numeroInteiro2 > numeroInteiro3:
    maior = numeroInteiro2
else:
    maior = numeroInteiro3

print(f'O maior número é {maior}.')
