"""As Ilhas Weblands formam um reino independente nos mares do Pacífico. Como é um
reino recente, a sociedade é muito influenciada pela informática. A moeda oficial é o Bit;
existem notas de B$ 50, B$ 10, B$ 5 e B$ 1. Você foi contratado(a) para ajudar na
programação dos caixas automáticos de um grande banco das Ilhas Weblands.
Os caixas eletrônicos das Ilhas Weblands operam com todos os tipos de notas
disponíveis, mantendo um estoque para cada valor de cédula. Os clientes do banco
utilizam os caixas eletrônicos para efetuar retiradas de um certo número inteiro de Bits.
Sua tarefa é escrever um programa que, dado o valor de Bits desejado pelo cliente,
determine o número de cada uma das notas necessário para totalizar esse valor, de
modo a minimizar a quantidade de cédulas entregues.
Exemplo:
Para B$ 72 seriam as seguintes notas:
- 1 nota de B$ 50
- 2 notas de B$ 10
- 0 notas de B$ 5
- 2 notas de B$ 1
"""

valorSaque = int(input('Digite o valor a ser sacado em B$:'))

qtdNotasCinquenta = valorSaque // 50
restoCinquenta = valorSaque % 50
qtdNotasDez = restoCinquenta // 10
restoDez = restoCinquenta % 10
qtdNotasCinco = restoDez // 5
restoCinco = restoDez % 5
qtdNotasUm = restoCinco

print(f'{qtdNotasCinquenta} nota(s) de B$ 50.')
print(f'{qtdNotasDez} nota(s) de B$ 10.')
print(f'{qtdNotasCinco} nota(s) de B$ 5.')
print(f'{qtdNotasUm} nota(s) de B$ 1.')
