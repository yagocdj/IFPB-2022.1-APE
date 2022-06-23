"""
6. Chico tem 1,50 metros e cresce 2 centímetros por ano, enquanto Zé tem 1,10
metros e cresce 3 centímetros por ano. Faça um programa que calcule e
imprima quantos anos serão necessários para que Zé seja maior que Chico.
"""

altura_chico = 150  # Ambas as alturas estão em centímetros
altura_ze = 110
tempo = 0  # tempo em anos

while altura_chico >= altura_ze:
    tempo += 1
    altura_chico = altura_chico + 2
    altura_ze = altura_ze + 3
    print(f'Altura atual de Chico: {altura_chico}.')
    print(f'Altura atual de Zé: {altura_ze}.')

print(f'São necessários {tempo} anos para que Zé seja maior que Chico.')
