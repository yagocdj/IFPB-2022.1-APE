"""
4. Um dado material radioativo perde metade de sua massa a cada 50
segundos. Faça um programa que leia uma certa quantidade de massa, em
gramas, deste material e imprima o tempo necessário para que sua massa
se torne menor que 0.5g.
"""

massa = float(input('Massa em gramas: '))  # Massa em gramas
massa_reduzida = massa / 2
tempo_massa = 50  # Tempo em segundos
flag = 0.5

while massa_reduzida >= flag:
    tempo_massa += 50
    massa = massa_reduzida
    massa_reduzida = massa / 2
print(f'Tempo necessário para que massa <= 0.5g: {tempo_massa} segundos.')
