"""
Faça um programa que, para um grupo de N pessoas (obs: N será lido):
• Leia o sexo (M ou F) de cada pessoa;
• Calcule e escreva o percentual de homens;
• Calcule e escreva o percentual de mulheres.
"""

n = int(input('Digite o número de pessoas: '))
contagem_mulher = 0
contagem_homem = 0
percentual_homem = float()
percentual_mulher = float()

for i in range(1, n + 1):
    sexo = input('Digite o sexo da pessoa (M ou F): ').upper()
    if sexo == 'F':
        contagem_mulher = contagem_mulher + 1
    else:
        contagem_homem = contagem_homem + 1
    percentual_mulher = (contagem_mulher * 100) / n
    percentual_homem = (contagem_homem * 100) / n

print(f'Percentual de mulheres = {percentual_mulher:.1f}%.')
print(f'Percentual de homens = {percentual_homem:.1f}%.')
