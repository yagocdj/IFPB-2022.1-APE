"""
7. Faça um programa que leia a idade de várias pessoas visitantes de um show (a
leitura da idade 0 indicará o fim dos dados de entrada), calcule e exiba:
• A média de idade do público;
• A porcentagem de pessoas com idade entre 18 e 21 anos;
• Idade do visitante mais jovem.
"""

texto_idade = 'Digite a sua idade: '
idade = int(input(texto_idade))
soma_idade = 0
flag = 0
# Porcentagem de pessoas com idade entre 18 e 21 anos
porcentagem = float()
quantidade_idade = 0
quantidade_porcentagem = 0
menor_idade = 0

while idade != flag:
    quantidade_idade += 1
    soma_idade += idade
    media = soma_idade / quantidade_idade
    if (idade >= 18) and (idade <= 21):
        quantidade_porcentagem += 1
        porcentagem = quantidade_porcentagem / idade
    if idade < menor_idade:
        menor_idade = idade
    print('Digite "0" caso queira parar o programa.')
    if idade != flag:
        idade = int(input(texto_idade))

print()
print(f'Média de idade do público: {media}.')
print(f'Porcentagem de pessoas com idade entre 18 e 21 anos: {porcentagem}.')
print(f'Idade do visitante mais jovem do show: {menor_idade}')
print('Fim do programa')
