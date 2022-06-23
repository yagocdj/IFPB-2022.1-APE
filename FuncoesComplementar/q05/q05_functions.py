# Biblioteca de funções para a questão 5

"""
Função para calcular o fatorial de um número
"""


def fatorial(numero):
    if numero < 0:
        return None  # Caso seja informado um valor negativo
    resultado = 1
    for i in range(numero, 0, -1):
        resultado *= i
    return resultado


"""
Função para calcular uma potência
"""
