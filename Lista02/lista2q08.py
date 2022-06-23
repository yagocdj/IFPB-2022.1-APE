# 8. Escreva um programa que tenha a funcionalidade de uma calculadora simples. O programa deve
# solicitar a digitação de dois operandos e um operador (+ - x * / %) e deve imprimir ao resultado
# da operação aritmética. Caso o usuário digite um operador inválido, o programa deve imprimir
# "Operador desconhecido".

print('Calculadora simples.')

operando1 = float(input('Operando um: '))
operando2 = float(input('Operando dois: '))
operador = input('Operador aritmético: ')

if operador == '+':
    print('Resultado: ', operando1 + operando2)
elif operador == '-':
    print('Resultado: ', operando1 - operando2)
elif operador == '*' or operador == 'x':
    print('Resultado: ', operando1 * operando2)
elif operador == '/':
    print('Resultado: ', operando1 / operando2)
elif operador == '%':
    print('Resultado: ', operando1 % operando2)
else:
    print('Operador desconhecido.')
