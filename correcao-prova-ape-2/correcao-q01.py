# Correção da prova de APE 2

# Criando os vetores

quantidade_questoes = 50
gabarito = ['-'] * quantidade_questoes
resposta_aluno = ['-'] * quantidade_questoes

# Preenchendo o gabarito

print('\nA seguir, digite as respostas para preencher o gabarito.')

for i in range(quantidade_questoes):
    gabarito[i] = input(f'Questão {i + 1}: ')

# Recebendo as respostas do aluno

print('\nAgora, digite as repostas do aluno.')

pontuacao = 0

for i in range(quantidade_questoes):
    resposta_aluno[i] = input(f'Questão {i + 1}: ')
    if resposta_aluno[i] == gabarito[i]:
        pontuacao += 2

# Exibindo a pontuação final do aluno

print(f'\nO aluno obteve pontuação igual a {pontuacao}.')
