"""
4. Faça um programa que leia os seguintes dados de um conjunto de alunos:
matrícula, nome e as duas notas que ele obteve em suas avaliações. A
condição de parada será a digitação de uma matrícula igual 0 (zero). O
programa deverá mostrar, para cada aluno, as seguintes informações:
matrícula, nome, média e situação (aprovado, se a média for igual ou superior
a 7 e, reprovado, se a média for inferior a 7).
"""

texto_matricula = 'Matrícula do aluno: '
matricula = int(input(texto_matricula))

texto_nome = 'Nome do aluno: '
nome = input(texto_nome)

texto_nota1 = 'Primeira nota: '
nota1 = float(input(texto_nota1))

texto_nota2 = 'Segunda nota: '
nota2 = float(input(texto_nota2))

flag = 0
media = (nota1 + nota2) / (2)
situacao = str()

while matricula != 0:
    if media >= 7:
        situacao = 'aprovado'
    else:
        situacao = 'reprovado'
    print(f'Nome: {nome}.')
    print(f'Matrícula: {matricula}.')
    print(f'Média: {media}.')
    print(f'Situação: {situacao}.')
    if matricula != 0:
        matricula = int(input(texto_matricula))
        nome = input(texto_nome)
        nota1 = float(input(texto_nota1))
        nota2 = float(input(texto_nota2))

print('Fim do programa')
