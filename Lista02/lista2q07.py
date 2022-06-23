# 7. Escreva um programa que leia o peso (kg) e a altura (m) de uma pessoa, determine e mostre o
# seu grau de obesidade, de acordo com a tabela seguinte. O grau de obesidade é determinado
# pelo índice de massa corpórea, cujo cálculo é realizado dividindo-se o peso da pessoa pelo
# quadrado da sua altura.

print('Informe o seu peso(Kg) e a sua altura(m): ')

peso = float(input('Peso: '))
altura = float(input('Altura: '))

imc = peso / altura ** 2

if imc < 26:
    situacao = 'normal'
elif imc < 30:
    situacao = 'obeso'
else:
    situacao = 'obeso mórbido'

print(f'Seu grau de obesidade é {situacao}.')