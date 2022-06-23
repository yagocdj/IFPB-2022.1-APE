"""
6. Faça um programa que leia uma frase e a exiba invertida.
"""

frase = input('Digite uma frase: ')
frase_invertida = frase[::-1]

# Outra maneira
"""
for i in range(len(frase) - 1, -1, -1):
    print(frase[i], end='')
"""

print(f'A frase invertida é: {frase_invertida}')

# Do jeito que Thiago gosta
# print(input('Informe uma frase: ')[::-1]
