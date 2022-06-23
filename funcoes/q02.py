"""
2. Escreva uma função chamada fatorial que receba um número inteiro e retorne
seu fatorial. Faça também um programa para testar a função.
"""

# Função fatorial


def fatorial(numero):
    if numero < 0:
        return None  # Caso seja informado um valor negativo
    resultado = 1
    for i in range(numero, 0, -1):
        resultado *= i
    return resultado


# Programa principal
valor = int(input('Digite um valor para que seja calculado o seu fatorial: '))
novo_valor = fatorial(valor)
print(f'{valor}! = {novo_valor}')
