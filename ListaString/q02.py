"""
2. Faça um programa que leia uma frase e a exiba sem os espaços em branco.
"""

# Recebendo a frase e tirando os espaços
frase = input('Digite uma frase: ')
frase_noblank = frase.replace(' ', '')

# .replace(string, string, count)

print(f'Frase sem espaços: {frase_noblank}')
