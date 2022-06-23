# 5. A empresa Vende Tudo Ltda paga o salário de cada vendedor com uma comissão de 5% sobre o
# total de vendas daquele vendedor, mas essa comissão nunca deve ser inferior ao salário-
# mínimo. Escreva um programa que leia o valor total das vendas de um vendedor e escreva seu
# salário.

salarioMinimo = 1200.00
percentual = 0.05

totalVendas = float(input('Vendendor, digite o seu total de vendas: R$ '))

salario = totalVendas * percentual

if salario < salarioMinimo:
    print(f'O seu salário é R${salarioMinimo:.2f}')
else:
    print(f'O seu salário é R${salario:.2f}')
