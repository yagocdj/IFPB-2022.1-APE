"""
1. Faça um programa que leia o email de uma pessoa e mostre, separadamente,
qual o login e qual o domínio.
Por exemplo, suponha que o email seja "fulano@provedor.com.br", então o login
será "fulano" e o domínio será "provedor.com.br".
"""

email = input('Digite seu e-mail: ')

# Separando login e domínio
login_dominio = email.split('@')

print(f'Login: {login_dominio[0]}')
print(f'Domínio: {login_dominio[1]}')

# Versão usando a funçaõ find e slicing
email = input('Digite novamente o seu e-mail: ')

indice = email.find('@')

print(f'Login: {email[:indice]}')
print(f'Login: {email[indice + 1:]}')
