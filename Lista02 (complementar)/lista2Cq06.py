# 6. Na primeira etapa de um concurso, o candidato tem que fazer duas provas. Dessas duas notas é
# tirada a média do candidato. Caso essa média seja maior ou igual a 7.0, ele estará apto a fazer a
# segunda etapa do concurso. Na segunda etapa, ele fará mais uma prova, onde deverá obter uma
# nota maior ou igual a 8.0 para ser aprovado no concurso.
# Escreva um programa que leia as notas da primeira etapa, calcule a média da primeira etapa, e
# se o candidato for aprovado na primeira etapa, leia a nota dele na segunda etapa e diga se ele
# foi aprovado ou não no concurso.

# Primeira etapa
nota1 = float(input('Nota da prova 1: '))
nota2 = float(input('Nota da prova 2: '))
media = (nota1 + nota2) / 2
nota3 = float()
situacao = str()

if media >= 7.0:
    situacao = 'passou para a segunda etapa'
    nota3 = float(input('Nota da prova 3 (segunda etapa): '))
    if nota3 >= 8.0:
        situacao = 'aprovado no concurso'
    else:
        situacao = 'pontuação insuficiente para ser aprovado no concurso'
else:
    situacao = 'não passou para a segunda etapa'

print(f'Resultado: {situacao}.')
