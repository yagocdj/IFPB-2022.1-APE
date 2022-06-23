# Testando as funções

import q05_functions as q05f

# MAIN

x = int(input('Valor utilizado no teste: '))

resultado = float()
sinal = -1
# i começa em 2 e vai até 40 com step de 2
for i in range(2, 41, 2):
    print('i =', i)
    if i == 2:
        resultado = 1 - (q05f.potencia(x, i) / q05f.fatorial(i))
        print('resultado =', resultado)
    else:
        resultado = resultado + \
            (sinal * (q05f.potencia(x, i) / q05f.fatorial(i)))
        sinal *= -1
        print('Sinal =', sinal)
        print('resultado =', resultado)
print('Fim do programa.')
