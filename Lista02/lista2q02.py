# 2. Escreva um programa que leia dois números e exiba-os em ordem crescente.

numero1 = float(input('Digite um número qualquer: '))
numero2 = float(input('Agora digite outro número qualquer: '))

if numero2 < numero1:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1

print(f'Numeros em ordem crescente: {menor}, {maior}.')