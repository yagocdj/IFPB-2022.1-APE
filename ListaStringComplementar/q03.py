"""
3. Faça um programa que leia o nome de uma pessoa e exiba-o conforme o exemplo
abaixo.
Obs: Suponha que o nome lido não possua nenhuma preposição, artigo, etc.
Exemplo:
Entrada: FLAVIO RIBEIRO COUTINHO
Saída: COUTINHO, F. R.
"""

# Recebendo o nome e dando um split nele
nome = input('Digite o seu nome completo: ').upper().split()
# Formatando o nome
nome_formatado = f'{nome[-1]}, '

for i in range(len(nome) - 1):
    nome_formatado += nome[i][0] + '. '

print(f'Nome formatado: {nome_formatado}')
