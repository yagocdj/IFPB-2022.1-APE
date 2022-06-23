n = int(input())  # número de mensagens trazidas pelo ancião
mensagens = [input() for i in range(n)]
contador_fada = 0

# percorrendo cada mensagem e verificando se há pelo menos um trecho "fada"
# nelas
for mensagem in mensagens:
    mensagem.lower()
    if mensagem.count('fada') >= 1:
        contador_fada += 1
print(contador_fada)
