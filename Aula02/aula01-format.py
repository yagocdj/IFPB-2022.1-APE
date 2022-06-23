# format()
# especificando a formatação de uma string
texto = '{} tem {} anos'
print(texto.format('Paulo', 20))
# ou
print('{} tem {} anos'.format('Paulo', 20))
# numerando ou nomeando o espaço reservado para dados
texto = '{0} tem {1} anos. {0} tem a mesma idade de {2}'
print(texto.format('Paulo', 20, 'Luis'))

anoAtual = int(input('Digite o ano atual: '))
anoNasc = int(input('Digite o ano de nascimento: '))
texto = '{} tem {idade} anos'
print(texto.format('Ana', idade=anoAtual-anoNasc))

# Especificando a formatação dos campos
texto = 'programando com Python'
print('{:40}'.format(texto))
print('{:>40}'.format(texto))
print('{:<40}'.format(texto))
print('{:^40}'.format(texto))
print('{:@^40}'.format(texto))

# Especificando a formatação dos campos (outros exemplos com números)
print('inteiro: {0:d} decimal: {1:5.2f}'.format(54, 54.789))

print('inteiro: {0:+d} decimal: {1:5.2f}'.format(54, -54.789))

print('inteiro: {0:d} decimal: {1:*^15.2f}'.format(54, 54.789))

# Apresentando dados em Python com f-strings.
# As regras são as mesmas do format, porém informamos o nome das variáveis na própria formatação
# f-string é o mais utilizado hoje em dia (código mais enxuto)
aluno = 'Pedro'
curso = 'Sistemas para Internet'
# print(aluno, 'está cursando', curso)
print(f'{aluno} está cursando {curso}')

n = 3
print(f'O dobro de {n} é {n*2}')

# resumindo
nome = 'Yago'
sobrenome = 'Cesar'
idade = 19.5
print('Meu nome é {} {}'.format(nome, sobrenome), ', olá')
print(f'Meu nome é {nome} {sobrenome}, olá')
print(f'Meu nome é {nome:x^20} {sobrenome} e tenho {idade} anos')

texto = 'Programando com Python'
print(f'{texto:40}')
print(f'{texto:>40}')
print(f'{texto:*^40}')

x = 123.456
print(f'{x:10.1f}')
# "Exiba o número com 10 espaços no total mas com apenas uma casa decimal"
