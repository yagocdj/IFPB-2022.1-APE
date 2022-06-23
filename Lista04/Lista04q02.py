"""
2. Faça um programa que leia vários números, calcule e exiba a média desses
números.
Obs: a leitura do número 999 indica o fim dos dados de entrada e não deve ser
computado na média)
"""

contador = 0
soma = 0.0
flag = 999

print(f'Digite um número por vez (ou {flag} para encerrar): ')
# input fora e dentro do laço serve para controle com flag
numero = float(input())
media = float()

while numero != flag:
    soma = soma + numero
    contador = contador + 1
    media = soma / contador
    numero = float(input())

print(f'Média: {media:.1f}')
print('O usuário encerrou o programa!')
