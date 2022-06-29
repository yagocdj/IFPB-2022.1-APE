# Questão 1 da prova 3 de APE

nome = input('Digite o seu nome:\n').lower()
lista_nome = nome.split()
login = lista_nome[0]

for i in range(1, len(lista_nome)):
    login += lista_nome[i][0]

print(login)
