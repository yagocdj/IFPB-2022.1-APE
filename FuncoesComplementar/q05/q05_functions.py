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


def potencia(numero, expoente):
    valor_final = numero ** expoente
    return valor_final


"""
Função para calcular o cosseno
"""


def cosseno(x):
    resultado = float()
    sinal = -1
    # i começa em 2 e vai até 40 com step de 2
    for i in range(2, 21, 2):
        if i == 2:
            resultado = 1 - (potencia(x, i) / fatorial(i))
        else:
            resultado += sinal * (potencia(x, i) / fatorial(i))
            sinal *= -1
    return resultado
