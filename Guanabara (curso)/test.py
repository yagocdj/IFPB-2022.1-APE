n1 = int(input('Digite um valor inteiro:'))
n2 = int(input('Agora digite outro valor inteiro:'))
s = n1 + n2
print(f'A soma entre {n1} e {n2} vale {s}.')
print('A soma entre {} e {} vale {}.'.format(n1, n2, s))

x = bool(input('Digite um valor qualquer para True ou deixe em branco e aperte "Enter" para False:'))
print(x)
print(type(x))

# Detectando se "n" é numérico.
n = input('Digite algo:')
print(n.isnumeric())

# Detectando se "v" é alpha.
v = input('Digite alguma coisa:')
print(v.isalpha())

# Detectando se "y" é alfanumérico.
y = input('Digite mais outra coisa:')
print(y.isalnum())

# Detectando se "z" possui uppercase (letra maiúscula)
z = input('Digite algo novamente:')
print(z.isupper())
