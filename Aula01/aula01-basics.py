vi = 1
vf = 1.1
vs = 'ifpb'
vb = True  # or False

# as variáveis acima representam os tipos
print(vi)
print(vf)
print(vs)
print(vb)

# fazendo os tipos aparecerem no "run"
print(type(vi))
print(type(vf))
print(type(vs))
print(type(vb))

# testando
vi = 2.5
print(type(vi))

# vi vira float (decimal)
vi = 1
print(type(vi))
print(float(vi))
print(type(vi))

# mudando realmente o tipo da variável
vi = float(vi)
print(type(vi))

# '' e ""
vs = "d'água"
print(vs)
vs = 'aula de "APE"'
print(vs)
print(1 + 1)
print('1'+'1')   # concatenação
print(type(vb))

# o bool ocupa menos espaço e é mais fácil de trabalhar (estrutura condicional)

# operadores aritméticos
print(2 % 2)
print(123 % 4567)

# atribuindo valores
a = 1
b = 3 * 2
c = a + b
print(c)

# entrada: input()
x = input('digite um valor qualquer:')
print(x)
print(type(x))

# input() sempre é string por padrão
y = int(input('digite um número inteiro:'))

# 'digite um número inteiro:' -> prompt
print(y)
print(type(y))

# ou
y = input('digite um número inteiro:')
y = int(y)
print(y)
print(type(y))

# print
z = 5
print('z =', z)
a = 7
b = 8
c = 9
print(a, b, c)

# sep = ''
print(a, b, c, sep='@')
print(a, b, c, sep='')

# end (por padrão, end='\n'
print('Olá turma!')
print('aula de APE')
print('OK')
print('Olá turma!', end='')
print('aula de APE', end='-')
print('OK', end='\n')

# A divisão "/" sempre retorna um valor do tipo "float".
