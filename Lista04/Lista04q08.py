"""
 8. O cardápio de uma casa de lanches, especializada em sanduíches, é dado a
seguir.
CÓDIGO NOME PREÇO
H Hamburger R$ 5,00
C Cheese Burger R$ 6,00
B Cheese Bacon R$ 7,00
F Cheese Frango R$ 4,00

Faça um programa que leia o código e a quantidade de cada item comprado
por um cliente (a leitura do código “X” indica o fim dos dados de entrada). Ao
final, calcule e exiba o total a pagar.
Veja o exemplo abaixo, considerando que o cliente pediu 3 Hamburger e 2
Cheese Bacon:
Entrada:
Código: H
Quantidade: 3
Código: B
Quantidade: 2
Código: X
Saída:
Total a pagar: R$ 29.00
"""

texto_codigo = 'Digite o código do produto escolhido: '
codigo = input(texto_codigo).upper()

texto_quantidade = 'Digite a quantidade de itens do produto escolhido: '
quantidade = int(input(texto_quantidade))

flag = 'X'

produto_h = 5.0
produto_c = 6.0
produto_b = 7.0
produto_f = 4.0

total = 0.0

while codigo != flag:
    if codigo == 'H':
        total = total + (produto_h * quantidade)
    if codigo == 'C':
        total = total + (produto_c * quantidade)
    if codigo == 'B':
        total = total + (produto_b * quantidade)
    if codigo == 'F':
        total = total + (produto_f * quantidade)
    codigo = input(texto_codigo).upper()
    if codigo != flag:
        quantidade = int(input(texto_quantidade))

print()
print(f'Total a pagar: R${total:.2f}')
