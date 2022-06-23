# 4. Escreva um programa que leia o nome e o sexo (M ou F) de uma pessoa e exiba a mensagem
# "Olá, Sr. Fulano!" ou "Olá, Sra. Fulana!", de acordo com o sexo da pessoa. Obs: Fulano e Fulana
# são nomes exemplos.

nome = input('Digite o seu nome: ')
genero = input('Informe o seu sexo digitando M para masculino ou F para feminino: ').upper()

# .upper() é uma função.

if genero == 'F':
    tratamento = 'Sra.'
else:
    tratamento = 'Sr.'

print(f'Olá, {tratamento} {nome}!')
