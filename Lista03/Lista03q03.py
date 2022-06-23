"""
3. Faça um programa que calcule e mostre o fatorial de um número N, fornecido
pelo usuário. A definição de fatorial é mostrada a seguir:
"""

n = int(input('Digite um número: '))
fatorial = 1  # 1 é o elemento neutro da multiplicação

for i in range(1, n + 1):
    fatorial = fatorial * i

print(f'{n}! = {fatorial}.')
