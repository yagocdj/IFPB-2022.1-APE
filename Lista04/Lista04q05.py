"""
5. Faça um programa que leia um número inteiro e determine se ele é par ou
ímpar. Ao final, o programa deve perguntar se o usuário deseja continuar
(digitar outro número) ou sair. Se o usuário quiser continuar, o programa deve
repetir tudo de novo, caso contrário o programa deve ser encerrado.
"""

tipo = str()
escolha = 'S'

while escolha == 'S':  # controle por pergunta
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        tipo = 'par'
    else:
        tipo = 'ímpar'
    print(f'{numero} é {tipo}.')
    print('Deseja Continuar? Se sim, digite "S".'
          + 'Caso contrário, digite "N".')
    escolha = input().upper()

print('O usuário encerrou o programa.')
