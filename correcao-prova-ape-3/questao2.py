# Questão 2 da prova 3 de APE

# Função para calcular o IMC

def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    return imc

# Função para calcular o grau de obesidade da pessoa


def grau_obesidade(imc):
    grau = ''
    if imc < 26.0:
        grau = 'normal'
    elif imc < 30:
        grau = 'obeso'
    else:
        grau = 'obeso mórbido'
    return grau


# MAIN
for i in range(30):
    nome = input('\nDigite o seu nome: ')
    peso = float(input('Digite o seu peso: '))
    altura = float(input('Digite a sua altura: '))

    imc = calcular_imc(peso, altura)
    grau = grau_obesidade(imc)

    print(f'\nNome: {nome}.')
    print(f'IMC: {imc:.1f}.')
    print(f'Grau de obesidade: {grau}')
