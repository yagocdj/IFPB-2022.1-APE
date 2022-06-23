"""
1. Faça um programa que leia 30 números inteiros, calcule e mostre a soma deles
Obs: não use o comando for, use while.
"""

texto_input = 'Digite um número inteiro: '
soma = 0
contador = 1  # "i" do "for i in range()"
qtd = 3

while contador <= qtd:
    numero = int(input(texto_input))
    soma = soma + numero
    contador += 1
    print(f'valor atual da soma: {soma}')
print()
print('Fim da soma!')
