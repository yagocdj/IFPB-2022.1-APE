"""A Companhia de Carros Usados João Honesto paga seus empregados um salário de R$
1.000,00 por mês mais uma comissão de R$ 200,00 por cada carro vendido mais 5% do
valor da venda.
Escreva um programa que leia o nome, o número de carros vendidos e o valor total das
vendas de um vendedor, e calcule e exiba o seu salário.
"""
comissao = 200
salarioFixo = 1000.00
percentual = 0.05

nome = input('Vendedor, informe o seu nome:')
carros = int(input('Agora digite quantos carros você vendeu:'))
valorVendas = float(input('Informe o valor total resultante das suas vendas:'))

salario = salarioFixo + comissao * carros + valorVendas * percentual

print(f'\n{nome}, o seu salário é igual a R$ {salario:.2f}')
